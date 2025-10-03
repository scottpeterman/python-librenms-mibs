# SNMP MIB module (DLINKSW-RA-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-RA-GUARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:48 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwRaGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141)
)
if mibBuilder.loadTexts:
    dlinkSwRaGuardMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DRaGuardNotifications_ObjectIdentity = ObjectIdentity
dRaGuardNotifications = _DRaGuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 0)
)
_DRaGuardObjects_ObjectIdentity = ObjectIdentity
dRaGuardObjects = _DRaGuardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1)
)
_DRaGuardPolicy_ObjectIdentity = ObjectIdentity
dRaGuardPolicy = _DRaGuardPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1)
)
_DRaGuardPolicyNumber_Type = Unsigned32
_DRaGuardPolicyNumber_Object = MibScalar
dRaGuardPolicyNumber = _DRaGuardPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 1),
    _DRaGuardPolicyNumber_Type()
)
dRaGuardPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dRaGuardPolicyNumber.setStatus("current")
_DRaGuardPolicyTable_Object = MibTable
dRaGuardPolicyTable = _DRaGuardPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dRaGuardPolicyTable.setStatus("current")
_DRaGuardPolicyEntry_Object = MibTableRow
dRaGuardPolicyEntry = _DRaGuardPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 2, 1)
)
dRaGuardPolicyEntry.setIndexNames(
    (0, "DLINKSW-RA-GUARD-MIB", "dRaGuardPolicyName"),
)
if mibBuilder.loadTexts:
    dRaGuardPolicyEntry.setStatus("current")


class _DRaGuardPolicyName_Type(DisplayString):
    """Custom type dRaGuardPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DRaGuardPolicyName_Type.__name__ = "DisplayString"
_DRaGuardPolicyName_Object = MibTableColumn
dRaGuardPolicyName = _DRaGuardPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 2, 1, 1),
    _DRaGuardPolicyName_Type()
)
dRaGuardPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dRaGuardPolicyName.setStatus("current")


class _DRaGuardPolicyDeviceRole_Type(Integer32):
    """Custom type dRaGuardPolicyDeviceRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )


_DRaGuardPolicyDeviceRole_Type.__name__ = "Integer32"
_DRaGuardPolicyDeviceRole_Object = MibTableColumn
dRaGuardPolicyDeviceRole = _DRaGuardPolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 2, 1, 2),
    _DRaGuardPolicyDeviceRole_Type()
)
dRaGuardPolicyDeviceRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRaGuardPolicyDeviceRole.setStatus("current")
_DRaGuardPolicyRowStatus_Type = RowStatus
_DRaGuardPolicyRowStatus_Object = MibTableColumn
dRaGuardPolicyRowStatus = _DRaGuardPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 2, 1, 99),
    _DRaGuardPolicyRowStatus_Type()
)
dRaGuardPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRaGuardPolicyRowStatus.setStatus("current")
_DRaGuardMatchAclTable_Object = MibTable
dRaGuardMatchAclTable = _DRaGuardMatchAclTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dRaGuardMatchAclTable.setStatus("current")
_DRaGuardMatchAclEntry_Object = MibTableRow
dRaGuardMatchAclEntry = _DRaGuardMatchAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 3, 1)
)
dRaGuardMatchAclEntry.setIndexNames(
    (0, "DLINKSW-RA-GUARD-MIB", "dRaGuardPolicyName"),
)
if mibBuilder.loadTexts:
    dRaGuardMatchAclEntry.setStatus("current")


class _DRaGuardMatchAccessListName_Type(DisplayString):
    """Custom type dRaGuardMatchAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DRaGuardMatchAccessListName_Type.__name__ = "DisplayString"
_DRaGuardMatchAccessListName_Object = MibTableColumn
dRaGuardMatchAccessListName = _DRaGuardMatchAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 3, 1, 1),
    _DRaGuardMatchAccessListName_Type()
)
dRaGuardMatchAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRaGuardMatchAccessListName.setStatus("current")
_DRaGuardMatchAclRowStatus_Type = RowStatus
_DRaGuardMatchAclRowStatus_Object = MibTableColumn
dRaGuardMatchAclRowStatus = _DRaGuardMatchAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 1, 3, 1, 99),
    _DRaGuardMatchAclRowStatus_Type()
)
dRaGuardMatchAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRaGuardMatchAclRowStatus.setStatus("current")
_DRaGuardInterface_ObjectIdentity = ObjectIdentity
dRaGuardInterface = _DRaGuardInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2)
)
_DRaGuardIfConfigTable_Object = MibTable
dRaGuardIfConfigTable = _DRaGuardIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dRaGuardIfConfigTable.setStatus("current")
_DRaGuardIfConfigEntry_Object = MibTableRow
dRaGuardIfConfigEntry = _DRaGuardIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2, 1, 1)
)
dRaGuardIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dRaGuardIfConfigEntry.setStatus("current")
_DRaGuardIfEnabled_Type = TruthValue
_DRaGuardIfEnabled_Object = MibTableColumn
dRaGuardIfEnabled = _DRaGuardIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2, 1, 1, 1),
    _DRaGuardIfEnabled_Type()
)
dRaGuardIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dRaGuardIfEnabled.setStatus("current")
_DRaGuardIfAttachTable_Object = MibTable
dRaGuardIfAttachTable = _DRaGuardIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dRaGuardIfAttachTable.setStatus("current")
_DRaGuardIfAttachEntry_Object = MibTableRow
dRaGuardIfAttachEntry = _DRaGuardIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2, 2, 1)
)
dRaGuardIfAttachEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dRaGuardIfAttachEntry.setStatus("current")


class _DRaGuardIfAttachPolicy_Type(DisplayString):
    """Custom type dRaGuardIfAttachPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DRaGuardIfAttachPolicy_Type.__name__ = "DisplayString"
_DRaGuardIfAttachPolicy_Object = MibTableColumn
dRaGuardIfAttachPolicy = _DRaGuardIfAttachPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2, 2, 1, 1),
    _DRaGuardIfAttachPolicy_Type()
)
dRaGuardIfAttachPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRaGuardIfAttachPolicy.setStatus("current")
_DRaGuardIfAttachRowStatus_Type = RowStatus
_DRaGuardIfAttachRowStatus_Object = MibTableColumn
dRaGuardIfAttachRowStatus = _DRaGuardIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 1, 2, 2, 1, 99),
    _DRaGuardIfAttachRowStatus_Type()
)
dRaGuardIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dRaGuardIfAttachRowStatus.setStatus("current")
_DRaGuardConformance_ObjectIdentity = ObjectIdentity
dRaGuardConformance = _DRaGuardConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2)
)
_DRaGuardMIBCompliances_ObjectIdentity = ObjectIdentity
dRaGuardMIBCompliances = _DRaGuardMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2, 1)
)
_DRaGuardMIBGroups_ObjectIdentity = ObjectIdentity
dRaGuardMIBGroups = _DRaGuardMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2, 2)
)

# Managed Objects groups

dRaGuardIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2, 2, 1)
)
dRaGuardIfConfigGroup.setObjects(
    ("DLINKSW-RA-GUARD-MIB", "dRaGuardIfEnabled")
)
if mibBuilder.loadTexts:
    dRaGuardIfConfigGroup.setStatus("current")

dRaGuardPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2, 2, 2)
)
dRaGuardPolicyGroup.setObjects(
      *(("DLINKSW-RA-GUARD-MIB", "dRaGuardPolicyNumber"),
        ("DLINKSW-RA-GUARD-MIB", "dRaGuardPolicyDeviceRole"),
        ("DLINKSW-RA-GUARD-MIB", "dRaGuardPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    dRaGuardPolicyGroup.setStatus("current")

dRaGuardMatchAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2, 2, 3)
)
dRaGuardMatchAclGroup.setObjects(
      *(("DLINKSW-RA-GUARD-MIB", "dRaGuardMatchAccessListName"),
        ("DLINKSW-RA-GUARD-MIB", "dRaGuardMatchAclRowStatus"))
)
if mibBuilder.loadTexts:
    dRaGuardMatchAclGroup.setStatus("current")

dRaGuardIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2, 2, 4)
)
dRaGuardIfAttachGroup.setObjects(
      *(("DLINKSW-RA-GUARD-MIB", "dRaGuardIfAttachPolicy"),
        ("DLINKSW-RA-GUARD-MIB", "dRaGuardIfAttachRowStatus"))
)
if mibBuilder.loadTexts:
    dRaGuardIfAttachGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dRaGuardMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 141, 2, 1, 1)
)
dRaGuardMIBCompliance.setObjects(
      *(("DLINKSW-RA-GUARD-MIB", "dRaGuardIfConfigGroup"),
        ("DLINKSW-RA-GUARD-MIB", "dRaGuardPolicyGroup"),
        ("DLINKSW-RA-GUARD-MIB", "dRaGuardIfAttachGroup"),
        ("DLINKSW-RA-GUARD-MIB", "dRaGuardMatchAclGroup"))
)
if mibBuilder.loadTexts:
    dRaGuardMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-RA-GUARD-MIB",
    **{"dlinkSwRaGuardMIB": dlinkSwRaGuardMIB,
       "dRaGuardNotifications": dRaGuardNotifications,
       "dRaGuardObjects": dRaGuardObjects,
       "dRaGuardPolicy": dRaGuardPolicy,
       "dRaGuardPolicyNumber": dRaGuardPolicyNumber,
       "dRaGuardPolicyTable": dRaGuardPolicyTable,
       "dRaGuardPolicyEntry": dRaGuardPolicyEntry,
       "dRaGuardPolicyName": dRaGuardPolicyName,
       "dRaGuardPolicyDeviceRole": dRaGuardPolicyDeviceRole,
       "dRaGuardPolicyRowStatus": dRaGuardPolicyRowStatus,
       "dRaGuardMatchAclTable": dRaGuardMatchAclTable,
       "dRaGuardMatchAclEntry": dRaGuardMatchAclEntry,
       "dRaGuardMatchAccessListName": dRaGuardMatchAccessListName,
       "dRaGuardMatchAclRowStatus": dRaGuardMatchAclRowStatus,
       "dRaGuardInterface": dRaGuardInterface,
       "dRaGuardIfConfigTable": dRaGuardIfConfigTable,
       "dRaGuardIfConfigEntry": dRaGuardIfConfigEntry,
       "dRaGuardIfEnabled": dRaGuardIfEnabled,
       "dRaGuardIfAttachTable": dRaGuardIfAttachTable,
       "dRaGuardIfAttachEntry": dRaGuardIfAttachEntry,
       "dRaGuardIfAttachPolicy": dRaGuardIfAttachPolicy,
       "dRaGuardIfAttachRowStatus": dRaGuardIfAttachRowStatus,
       "dRaGuardConformance": dRaGuardConformance,
       "dRaGuardMIBCompliances": dRaGuardMIBCompliances,
       "dRaGuardMIBCompliance": dRaGuardMIBCompliance,
       "dRaGuardMIBGroups": dRaGuardMIBGroups,
       "dRaGuardIfConfigGroup": dRaGuardIfConfigGroup,
       "dRaGuardPolicyGroup": dRaGuardPolicyGroup,
       "dRaGuardMatchAclGroup": dRaGuardMatchAclGroup,
       "dRaGuardIfAttachGroup": dRaGuardIfAttachGroup}
)
