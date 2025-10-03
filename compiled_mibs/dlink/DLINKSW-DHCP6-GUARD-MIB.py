# SNMP MIB module (DLINKSW-DHCP6-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP6-GUARD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:55 2025
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

dlinkSwDhcp6GuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142)
)
if mibBuilder.loadTexts:
    dlinkSwDhcp6GuardMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDhcp6GuardNotifications_ObjectIdentity = ObjectIdentity
dDhcp6GuardNotifications = _DDhcp6GuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 0)
)
_DDhcp6GuardObjects_ObjectIdentity = ObjectIdentity
dDhcp6GuardObjects = _DDhcp6GuardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1)
)
_DDhcp6GuardPolicy_ObjectIdentity = ObjectIdentity
dDhcp6GuardPolicy = _DDhcp6GuardPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1)
)
_DDhcp6GuardPolicyNumber_Type = Unsigned32
_DDhcp6GuardPolicyNumber_Object = MibScalar
dDhcp6GuardPolicyNumber = _DDhcp6GuardPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 1),
    _DDhcp6GuardPolicyNumber_Type()
)
dDhcp6GuardPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDhcp6GuardPolicyNumber.setStatus("current")
_DDhcp6GuardPolicyTable_Object = MibTable
dDhcp6GuardPolicyTable = _DDhcp6GuardPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dDhcp6GuardPolicyTable.setStatus("current")
_DDhcp6GuardPolicyEntry_Object = MibTableRow
dDhcp6GuardPolicyEntry = _DDhcp6GuardPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 2, 1)
)
dDhcp6GuardPolicyEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardPolicyName"),
)
if mibBuilder.loadTexts:
    dDhcp6GuardPolicyEntry.setStatus("current")


class _DDhcp6GuardPolicyName_Type(DisplayString):
    """Custom type dDhcp6GuardPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6GuardPolicyName_Type.__name__ = "DisplayString"
_DDhcp6GuardPolicyName_Object = MibTableColumn
dDhcp6GuardPolicyName = _DDhcp6GuardPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 2, 1, 1),
    _DDhcp6GuardPolicyName_Type()
)
dDhcp6GuardPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcp6GuardPolicyName.setStatus("current")


class _DDhcp6GuardPolicyDeviceRole_Type(Integer32):
    """Custom type dDhcp6GuardPolicyDeviceRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_DDhcp6GuardPolicyDeviceRole_Type.__name__ = "Integer32"
_DDhcp6GuardPolicyDeviceRole_Object = MibTableColumn
dDhcp6GuardPolicyDeviceRole = _DDhcp6GuardPolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 2, 1, 2),
    _DDhcp6GuardPolicyDeviceRole_Type()
)
dDhcp6GuardPolicyDeviceRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6GuardPolicyDeviceRole.setStatus("current")
_DDhcp6GuardPolicyRowStatus_Type = RowStatus
_DDhcp6GuardPolicyRowStatus_Object = MibTableColumn
dDhcp6GuardPolicyRowStatus = _DDhcp6GuardPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 2, 1, 99),
    _DDhcp6GuardPolicyRowStatus_Type()
)
dDhcp6GuardPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6GuardPolicyRowStatus.setStatus("current")
_DDhcp6GuardMatchAclTable_Object = MibTable
dDhcp6GuardMatchAclTable = _DDhcp6GuardMatchAclTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dDhcp6GuardMatchAclTable.setStatus("current")
_DDhcp6GuardMatchAclEntry_Object = MibTableRow
dDhcp6GuardMatchAclEntry = _DDhcp6GuardMatchAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 3, 1)
)
dDhcp6GuardMatchAclEntry.setIndexNames(
    (0, "DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardPolicyName"),
)
if mibBuilder.loadTexts:
    dDhcp6GuardMatchAclEntry.setStatus("current")


class _DDhcp6GuardMatchAccessListName_Type(DisplayString):
    """Custom type dDhcp6GuardMatchAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6GuardMatchAccessListName_Type.__name__ = "DisplayString"
_DDhcp6GuardMatchAccessListName_Object = MibTableColumn
dDhcp6GuardMatchAccessListName = _DDhcp6GuardMatchAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 3, 1, 1),
    _DDhcp6GuardMatchAccessListName_Type()
)
dDhcp6GuardMatchAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6GuardMatchAccessListName.setStatus("current")
_DDhcp6GuardMatchAclRowStatus_Type = RowStatus
_DDhcp6GuardMatchAclRowStatus_Object = MibTableColumn
dDhcp6GuardMatchAclRowStatus = _DDhcp6GuardMatchAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 1, 3, 1, 99),
    _DDhcp6GuardMatchAclRowStatus_Type()
)
dDhcp6GuardMatchAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6GuardMatchAclRowStatus.setStatus("current")
_DDhcp6GuardInterface_ObjectIdentity = ObjectIdentity
dDhcp6GuardInterface = _DDhcp6GuardInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2)
)
_DDhcp6GuardIfConfigTable_Object = MibTable
dDhcp6GuardIfConfigTable = _DDhcp6GuardIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dDhcp6GuardIfConfigTable.setStatus("current")
_DDhcp6GuardIfConfigEntry_Object = MibTableRow
dDhcp6GuardIfConfigEntry = _DDhcp6GuardIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2, 1, 1)
)
dDhcp6GuardIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6GuardIfConfigEntry.setStatus("current")
_DDhcp6GuardIfEnabled_Type = TruthValue
_DDhcp6GuardIfEnabled_Object = MibTableColumn
dDhcp6GuardIfEnabled = _DDhcp6GuardIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2, 1, 1, 1),
    _DDhcp6GuardIfEnabled_Type()
)
dDhcp6GuardIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcp6GuardIfEnabled.setStatus("current")
_DDhcp6GuardIfAttachTable_Object = MibTable
dDhcp6GuardIfAttachTable = _DDhcp6GuardIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dDhcp6GuardIfAttachTable.setStatus("current")
_DDhcp6GuardIfAttachEntry_Object = MibTableRow
dDhcp6GuardIfAttachEntry = _DDhcp6GuardIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2, 2, 1)
)
dDhcp6GuardIfAttachEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDhcp6GuardIfAttachEntry.setStatus("current")


class _DDhcp6GuardIfAttachPolicy_Type(DisplayString):
    """Custom type dDhcp6GuardIfAttachPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcp6GuardIfAttachPolicy_Type.__name__ = "DisplayString"
_DDhcp6GuardIfAttachPolicy_Object = MibTableColumn
dDhcp6GuardIfAttachPolicy = _DDhcp6GuardIfAttachPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2, 2, 1, 1),
    _DDhcp6GuardIfAttachPolicy_Type()
)
dDhcp6GuardIfAttachPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6GuardIfAttachPolicy.setStatus("current")
_DDhcp6GuardIfAttachRowStatus_Type = RowStatus
_DDhcp6GuardIfAttachRowStatus_Object = MibTableColumn
dDhcp6GuardIfAttachRowStatus = _DDhcp6GuardIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 1, 2, 2, 1, 99),
    _DDhcp6GuardIfAttachRowStatus_Type()
)
dDhcp6GuardIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcp6GuardIfAttachRowStatus.setStatus("current")
_DDhcp6GuardConformance_ObjectIdentity = ObjectIdentity
dDhcp6GuardConformance = _DDhcp6GuardConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2)
)
_DDhcp6GuardMIBCompliances_ObjectIdentity = ObjectIdentity
dDhcp6GuardMIBCompliances = _DDhcp6GuardMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2, 1)
)
_DDhcp6GuardMIBGroups_ObjectIdentity = ObjectIdentity
dDhcp6GuardMIBGroups = _DDhcp6GuardMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2, 2)
)

# Managed Objects groups

dDhcp6GuardIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2, 2, 1)
)
dDhcp6GuardIfConfigGroup.setObjects(
    ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardIfEnabled")
)
if mibBuilder.loadTexts:
    dDhcp6GuardIfConfigGroup.setStatus("current")

dDhcp6GuardPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2, 2, 2)
)
dDhcp6GuardPolicyGroup.setObjects(
      *(("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardPolicyNumber"),
        ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardPolicyDeviceRole"),
        ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6GuardPolicyGroup.setStatus("current")

dDhcp6GuardMatchAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2, 2, 3)
)
dDhcp6GuardMatchAclGroup.setObjects(
      *(("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardMatchAccessListName"),
        ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardMatchAclRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6GuardMatchAclGroup.setStatus("current")

dDhcp6GuardIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2, 2, 4)
)
dDhcp6GuardIfAttachGroup.setObjects(
      *(("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardIfAttachPolicy"),
        ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardIfAttachRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcp6GuardIfAttachGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDhcp6GuardMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 142, 2, 1, 1)
)
dDhcp6GuardMIBCompliance.setObjects(
      *(("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardIfConfigGroup"),
        ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardPolicyGroup"),
        ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardIfAttachGroup"),
        ("DLINKSW-DHCP6-GUARD-MIB", "dDhcp6GuardMatchAclGroup"))
)
if mibBuilder.loadTexts:
    dDhcp6GuardMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP6-GUARD-MIB",
    **{"dlinkSwDhcp6GuardMIB": dlinkSwDhcp6GuardMIB,
       "dDhcp6GuardNotifications": dDhcp6GuardNotifications,
       "dDhcp6GuardObjects": dDhcp6GuardObjects,
       "dDhcp6GuardPolicy": dDhcp6GuardPolicy,
       "dDhcp6GuardPolicyNumber": dDhcp6GuardPolicyNumber,
       "dDhcp6GuardPolicyTable": dDhcp6GuardPolicyTable,
       "dDhcp6GuardPolicyEntry": dDhcp6GuardPolicyEntry,
       "dDhcp6GuardPolicyName": dDhcp6GuardPolicyName,
       "dDhcp6GuardPolicyDeviceRole": dDhcp6GuardPolicyDeviceRole,
       "dDhcp6GuardPolicyRowStatus": dDhcp6GuardPolicyRowStatus,
       "dDhcp6GuardMatchAclTable": dDhcp6GuardMatchAclTable,
       "dDhcp6GuardMatchAclEntry": dDhcp6GuardMatchAclEntry,
       "dDhcp6GuardMatchAccessListName": dDhcp6GuardMatchAccessListName,
       "dDhcp6GuardMatchAclRowStatus": dDhcp6GuardMatchAclRowStatus,
       "dDhcp6GuardInterface": dDhcp6GuardInterface,
       "dDhcp6GuardIfConfigTable": dDhcp6GuardIfConfigTable,
       "dDhcp6GuardIfConfigEntry": dDhcp6GuardIfConfigEntry,
       "dDhcp6GuardIfEnabled": dDhcp6GuardIfEnabled,
       "dDhcp6GuardIfAttachTable": dDhcp6GuardIfAttachTable,
       "dDhcp6GuardIfAttachEntry": dDhcp6GuardIfAttachEntry,
       "dDhcp6GuardIfAttachPolicy": dDhcp6GuardIfAttachPolicy,
       "dDhcp6GuardIfAttachRowStatus": dDhcp6GuardIfAttachRowStatus,
       "dDhcp6GuardConformance": dDhcp6GuardConformance,
       "dDhcp6GuardMIBCompliances": dDhcp6GuardMIBCompliances,
       "dDhcp6GuardMIBCompliance": dDhcp6GuardMIBCompliance,
       "dDhcp6GuardMIBGroups": dDhcp6GuardMIBGroups,
       "dDhcp6GuardIfConfigGroup": dDhcp6GuardIfConfigGroup,
       "dDhcp6GuardPolicyGroup": dDhcp6GuardPolicyGroup,
       "dDhcp6GuardMatchAclGroup": dDhcp6GuardMatchAclGroup,
       "dDhcp6GuardIfAttachGroup": dDhcp6GuardIfAttachGroup}
)
