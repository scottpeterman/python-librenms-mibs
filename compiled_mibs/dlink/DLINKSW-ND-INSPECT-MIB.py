# SNMP MIB module (DLINKSW-ND-INSPECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-ND-INSPECT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:36 2025
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

dlinkSwNdInspecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144)
)
if mibBuilder.loadTexts:
    dlinkSwNdInspecMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DNdInspecNotifications_ObjectIdentity = ObjectIdentity
dNdInspecNotifications = _DNdInspecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 0)
)
_DNdInspecObjects_ObjectIdentity = ObjectIdentity
dNdInspecObjects = _DNdInspecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1)
)
_DNdInspecPolicy_ObjectIdentity = ObjectIdentity
dNdInspecPolicy = _DNdInspecPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1)
)
_DNdInspecPolicyNumber_Type = Unsigned32
_DNdInspecPolicyNumber_Object = MibScalar
dNdInspecPolicyNumber = _DNdInspecPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1, 1),
    _DNdInspecPolicyNumber_Type()
)
dNdInspecPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNdInspecPolicyNumber.setStatus("current")
_DNdInspecPolicyTable_Object = MibTable
dNdInspecPolicyTable = _DNdInspecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dNdInspecPolicyTable.setStatus("current")
_DNdInspecPolicyEntry_Object = MibTableRow
dNdInspecPolicyEntry = _DNdInspecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1, 2, 1)
)
dNdInspecPolicyEntry.setIndexNames(
    (0, "DLINKSW-ND-INSPECT-MIB", "dNdInspecPolicyName"),
)
if mibBuilder.loadTexts:
    dNdInspecPolicyEntry.setStatus("current")


class _DNdInspecPolicyName_Type(DisplayString):
    """Custom type dNdInspecPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DNdInspecPolicyName_Type.__name__ = "DisplayString"
_DNdInspecPolicyName_Object = MibTableColumn
dNdInspecPolicyName = _DNdInspecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1, 2, 1, 1),
    _DNdInspecPolicyName_Type()
)
dNdInspecPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNdInspecPolicyName.setStatus("current")


class _DNdInspecPolicyDeviceRole_Type(Integer32):
    """Custom type dNdInspecPolicyDeviceRole based on Integer32"""
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


_DNdInspecPolicyDeviceRole_Type.__name__ = "Integer32"
_DNdInspecPolicyDeviceRole_Object = MibTableColumn
dNdInspecPolicyDeviceRole = _DNdInspecPolicyDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1, 2, 1, 2),
    _DNdInspecPolicyDeviceRole_Type()
)
dNdInspecPolicyDeviceRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNdInspecPolicyDeviceRole.setStatus("current")


class _DNdInspecPolicyValidateSrcMac_Type(TruthValue):
    """Custom type dNdInspecPolicyValidateSrcMac based on TruthValue"""
    defaultValue = 2


_DNdInspecPolicyValidateSrcMac_Type.__name__ = "TruthValue"
_DNdInspecPolicyValidateSrcMac_Object = MibTableColumn
dNdInspecPolicyValidateSrcMac = _DNdInspecPolicyValidateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1, 2, 1, 3),
    _DNdInspecPolicyValidateSrcMac_Type()
)
dNdInspecPolicyValidateSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNdInspecPolicyValidateSrcMac.setStatus("current")
_DNdInspecPolicyRowStatus_Type = RowStatus
_DNdInspecPolicyRowStatus_Object = MibTableColumn
dNdInspecPolicyRowStatus = _DNdInspecPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 1, 2, 1, 99),
    _DNdInspecPolicyRowStatus_Type()
)
dNdInspecPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNdInspecPolicyRowStatus.setStatus("current")
_DNdInspecInterface_ObjectIdentity = ObjectIdentity
dNdInspecInterface = _DNdInspecInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2)
)
_DNdInspecIfConfigTable_Object = MibTable
dNdInspecIfConfigTable = _DNdInspecIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dNdInspecIfConfigTable.setStatus("current")
_DNdInspecIfConfigEntry_Object = MibTableRow
dNdInspecIfConfigEntry = _DNdInspecIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2, 1, 1)
)
dNdInspecIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dNdInspecIfConfigEntry.setStatus("current")
_DNdInspecIfEnabled_Type = TruthValue
_DNdInspecIfEnabled_Object = MibTableColumn
dNdInspecIfEnabled = _DNdInspecIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2, 1, 1, 1),
    _DNdInspecIfEnabled_Type()
)
dNdInspecIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNdInspecIfEnabled.setStatus("current")
_DNdInspecIfAttachTable_Object = MibTable
dNdInspecIfAttachTable = _DNdInspecIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dNdInspecIfAttachTable.setStatus("current")
_DNdInspecIfAttachEntry_Object = MibTableRow
dNdInspecIfAttachEntry = _DNdInspecIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2, 2, 1)
)
dNdInspecIfAttachEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dNdInspecIfAttachEntry.setStatus("current")


class _DNdInspecIfAttachPolicy_Type(DisplayString):
    """Custom type dNdInspecIfAttachPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DNdInspecIfAttachPolicy_Type.__name__ = "DisplayString"
_DNdInspecIfAttachPolicy_Object = MibTableColumn
dNdInspecIfAttachPolicy = _DNdInspecIfAttachPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2, 2, 1, 1),
    _DNdInspecIfAttachPolicy_Type()
)
dNdInspecIfAttachPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNdInspecIfAttachPolicy.setStatus("current")
_DNdInspecIfAttachRowStatus_Type = RowStatus
_DNdInspecIfAttachRowStatus_Object = MibTableColumn
dNdInspecIfAttachRowStatus = _DNdInspecIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 1, 2, 2, 1, 99),
    _DNdInspecIfAttachRowStatus_Type()
)
dNdInspecIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dNdInspecIfAttachRowStatus.setStatus("current")
_DNdInspecConformance_ObjectIdentity = ObjectIdentity
dNdInspecConformance = _DNdInspecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 2)
)
_DNdInspecMIBCompliances_ObjectIdentity = ObjectIdentity
dNdInspecMIBCompliances = _DNdInspecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 2, 1)
)
_DNdInspecMIBGroups_ObjectIdentity = ObjectIdentity
dNdInspecMIBGroups = _DNdInspecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 2, 2)
)

# Managed Objects groups

dNdInspecIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 2, 2, 1)
)
dNdInspecIfConfigGroup.setObjects(
    ("DLINKSW-ND-INSPECT-MIB", "dNdInspecIfEnabled")
)
if mibBuilder.loadTexts:
    dNdInspecIfConfigGroup.setStatus("current")

dNdInspecPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 2, 2, 2)
)
dNdInspecPolicyGroup.setObjects(
      *(("DLINKSW-ND-INSPECT-MIB", "dNdInspecPolicyNumber"),
        ("DLINKSW-ND-INSPECT-MIB", "dNdInspecPolicyDeviceRole"),
        ("DLINKSW-ND-INSPECT-MIB", "dNdInspecPolicyValidateSrcMac"),
        ("DLINKSW-ND-INSPECT-MIB", "dNdInspecPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    dNdInspecPolicyGroup.setStatus("current")

dNdInspecIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 2, 2, 3)
)
dNdInspecIfAttachGroup.setObjects(
      *(("DLINKSW-ND-INSPECT-MIB", "dNdInspecIfAttachPolicy"),
        ("DLINKSW-ND-INSPECT-MIB", "dNdInspecIfAttachRowStatus"))
)
if mibBuilder.loadTexts:
    dNdInspecIfAttachGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dNdInspecMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 144, 2, 1, 1)
)
dNdInspecMIBCompliance.setObjects(
      *(("DLINKSW-ND-INSPECT-MIB", "dNdInspecIfConfigGroup"),
        ("DLINKSW-ND-INSPECT-MIB", "dNdInspecPolicyGroup"),
        ("DLINKSW-ND-INSPECT-MIB", "dNdInspecIfAttachGroup"))
)
if mibBuilder.loadTexts:
    dNdInspecMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-ND-INSPECT-MIB",
    **{"dlinkSwNdInspecMIB": dlinkSwNdInspecMIB,
       "dNdInspecNotifications": dNdInspecNotifications,
       "dNdInspecObjects": dNdInspecObjects,
       "dNdInspecPolicy": dNdInspecPolicy,
       "dNdInspecPolicyNumber": dNdInspecPolicyNumber,
       "dNdInspecPolicyTable": dNdInspecPolicyTable,
       "dNdInspecPolicyEntry": dNdInspecPolicyEntry,
       "dNdInspecPolicyName": dNdInspecPolicyName,
       "dNdInspecPolicyDeviceRole": dNdInspecPolicyDeviceRole,
       "dNdInspecPolicyValidateSrcMac": dNdInspecPolicyValidateSrcMac,
       "dNdInspecPolicyRowStatus": dNdInspecPolicyRowStatus,
       "dNdInspecInterface": dNdInspecInterface,
       "dNdInspecIfConfigTable": dNdInspecIfConfigTable,
       "dNdInspecIfConfigEntry": dNdInspecIfConfigEntry,
       "dNdInspecIfEnabled": dNdInspecIfEnabled,
       "dNdInspecIfAttachTable": dNdInspecIfAttachTable,
       "dNdInspecIfAttachEntry": dNdInspecIfAttachEntry,
       "dNdInspecIfAttachPolicy": dNdInspecIfAttachPolicy,
       "dNdInspecIfAttachRowStatus": dNdInspecIfAttachRowStatus,
       "dNdInspecConformance": dNdInspecConformance,
       "dNdInspecMIBCompliances": dNdInspecMIBCompliances,
       "dNdInspecMIBCompliance": dNdInspecMIBCompliance,
       "dNdInspecMIBGroups": dNdInspecMIBGroups,
       "dNdInspecIfConfigGroup": dNdInspecIfConfigGroup,
       "dNdInspecPolicyGroup": dNdInspecPolicyGroup,
       "dNdInspecIfAttachGroup": dNdInspecIfAttachGroup}
)
