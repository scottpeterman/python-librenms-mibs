# SNMP MIB module (DLINKSW-IPV6-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-IPV6-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:20 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

dlinkSwIpv6SnoopMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143)
)
if mibBuilder.loadTexts:
    dlinkSwIpv6SnoopMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DIpv6SnoopNotifications_ObjectIdentity = ObjectIdentity
dIpv6SnoopNotifications = _DIpv6SnoopNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 0)
)
_DIpv6SnoopObjects_ObjectIdentity = ObjectIdentity
dIpv6SnoopObjects = _DIpv6SnoopObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1)
)
_DIpv6SnoopGlobal_ObjectIdentity = ObjectIdentity
dIpv6SnoopGlobal = _DIpv6SnoopGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 1)
)
_DIpv6SnoopStationMoveEnabled_Type = TruthValue
_DIpv6SnoopStationMoveEnabled_Object = MibScalar
dIpv6SnoopStationMoveEnabled = _DIpv6SnoopStationMoveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 1, 1),
    _DIpv6SnoopStationMoveEnabled_Type()
)
dIpv6SnoopStationMoveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIpv6SnoopStationMoveEnabled.setStatus("current")
_DIpv6SnoopPolicy_ObjectIdentity = ObjectIdentity
dIpv6SnoopPolicy = _DIpv6SnoopPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2)
)
_DIpv6SnoopPolicyNumber_Type = Unsigned32
_DIpv6SnoopPolicyNumber_Object = MibScalar
dIpv6SnoopPolicyNumber = _DIpv6SnoopPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2, 1),
    _DIpv6SnoopPolicyNumber_Type()
)
dIpv6SnoopPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyNumber.setStatus("current")
_DIpv6SnoopPolicyTable_Object = MibTable
dIpv6SnoopPolicyTable = _DIpv6SnoopPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyTable.setStatus("current")
_DIpv6SnoopPolicyEntry_Object = MibTableRow
dIpv6SnoopPolicyEntry = _DIpv6SnoopPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2, 2, 1)
)
dIpv6SnoopPolicyEntry.setIndexNames(
    (0, "DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyName"),
)
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyEntry.setStatus("current")


class _DIpv6SnoopPolicyName_Type(DisplayString):
    """Custom type dIpv6SnoopPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DIpv6SnoopPolicyName_Type.__name__ = "DisplayString"
_DIpv6SnoopPolicyName_Object = MibTableColumn
dIpv6SnoopPolicyName = _DIpv6SnoopPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2, 2, 1, 1),
    _DIpv6SnoopPolicyName_Type()
)
dIpv6SnoopPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyName.setStatus("current")


class _DIpv6SnoopPolicyProtocol_Type(Bits):
    """Custom type dIpv6SnoopPolicyProtocol based on Bits"""
    namedValues = NamedValues(
        *(("ndp", 0),
          ("dhcp", 1))
    )

_DIpv6SnoopPolicyProtocol_Type.__name__ = "Bits"
_DIpv6SnoopPolicyProtocol_Object = MibTableColumn
dIpv6SnoopPolicyProtocol = _DIpv6SnoopPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2, 2, 1, 2),
    _DIpv6SnoopPolicyProtocol_Type()
)
dIpv6SnoopPolicyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyProtocol.setStatus("current")
_DIpv6SnoopPolicyLimitAddrCount_Type = Unsigned32
_DIpv6SnoopPolicyLimitAddrCount_Object = MibTableColumn
dIpv6SnoopPolicyLimitAddrCount = _DIpv6SnoopPolicyLimitAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2, 2, 1, 3),
    _DIpv6SnoopPolicyLimitAddrCount_Type()
)
dIpv6SnoopPolicyLimitAddrCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyLimitAddrCount.setStatus("current")
_DIpv6SnoopPolicyRowStatus_Type = RowStatus
_DIpv6SnoopPolicyRowStatus_Object = MibTableColumn
dIpv6SnoopPolicyRowStatus = _DIpv6SnoopPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 2, 2, 1, 99),
    _DIpv6SnoopPolicyRowStatus_Type()
)
dIpv6SnoopPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyRowStatus.setStatus("current")
_DIpv6SnoopInterface_ObjectIdentity = ObjectIdentity
dIpv6SnoopInterface = _DIpv6SnoopInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 3)
)
_DIpv6SnoopPolicyAttachTable_Object = MibTable
dIpv6SnoopPolicyAttachTable = _DIpv6SnoopPolicyAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyAttachTable.setStatus("current")
_DIpv6SnoopPolicyAttachEntry_Object = MibTableRow
dIpv6SnoopPolicyAttachEntry = _DIpv6SnoopPolicyAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 3, 1, 1)
)
dIpv6SnoopPolicyAttachEntry.setIndexNames(
    (0, "DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyAttachVlanId"),
)
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyAttachEntry.setStatus("current")
_DIpv6SnoopPolicyAttachVlanId_Type = VlanId
_DIpv6SnoopPolicyAttachVlanId_Object = MibTableColumn
dIpv6SnoopPolicyAttachVlanId = _DIpv6SnoopPolicyAttachVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 3, 1, 1, 1),
    _DIpv6SnoopPolicyAttachVlanId_Type()
)
dIpv6SnoopPolicyAttachVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyAttachVlanId.setStatus("current")


class _DIpv6SnoopPolicyAttachPolicy_Type(DisplayString):
    """Custom type dIpv6SnoopPolicyAttachPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DIpv6SnoopPolicyAttachPolicy_Type.__name__ = "DisplayString"
_DIpv6SnoopPolicyAttachPolicy_Object = MibTableColumn
dIpv6SnoopPolicyAttachPolicy = _DIpv6SnoopPolicyAttachPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 3, 1, 1, 2),
    _DIpv6SnoopPolicyAttachPolicy_Type()
)
dIpv6SnoopPolicyAttachPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyAttachPolicy.setStatus("current")
_DIpv6SnoopPolicyAttachRowStatus_Type = RowStatus
_DIpv6SnoopPolicyAttachRowStatus_Object = MibTableColumn
dIpv6SnoopPolicyAttachRowStatus = _DIpv6SnoopPolicyAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 1, 3, 1, 1, 99),
    _DIpv6SnoopPolicyAttachRowStatus_Type()
)
dIpv6SnoopPolicyAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyAttachRowStatus.setStatus("current")
_DIpv6SnoopConformance_ObjectIdentity = ObjectIdentity
dIpv6SnoopConformance = _DIpv6SnoopConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 2)
)
_DIpv6SnoopMIBCompliances_ObjectIdentity = ObjectIdentity
dIpv6SnoopMIBCompliances = _DIpv6SnoopMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 2, 1)
)
_DIpv6SnoopMIBGroups_ObjectIdentity = ObjectIdentity
dIpv6SnoopMIBGroups = _DIpv6SnoopMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 2, 2)
)

# Managed Objects groups

dIpv6SnoopPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 2, 2, 1)
)
dIpv6SnoopPolicyGroup.setObjects(
      *(("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyNumber"),
        ("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyProtocol"),
        ("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyLimitAddrCount"),
        ("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyGroup.setStatus("current")

dIpv6SnoopPolicyAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 2, 2, 2)
)
dIpv6SnoopPolicyAttachGroup.setObjects(
      *(("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyAttachPolicy"),
        ("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyAttachRowStatus"))
)
if mibBuilder.loadTexts:
    dIpv6SnoopPolicyAttachGroup.setStatus("current")

dIpv6SnoopStationMoveCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 2, 2, 3)
)
dIpv6SnoopStationMoveCfgGroup.setObjects(
    ("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopStationMoveEnabled")
)
if mibBuilder.loadTexts:
    dIpv6SnoopStationMoveCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dIpv6SnoopMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 143, 2, 1, 1)
)
dIpv6SnoopMIBCompliance.setObjects(
      *(("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyGroup"),
        ("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopPolicyAttachGroup"),
        ("DLINKSW-IPV6-SNOOPING-MIB", "dIpv6SnoopStationMoveCfgGroup"))
)
if mibBuilder.loadTexts:
    dIpv6SnoopMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-IPV6-SNOOPING-MIB",
    **{"dlinkSwIpv6SnoopMIB": dlinkSwIpv6SnoopMIB,
       "dIpv6SnoopNotifications": dIpv6SnoopNotifications,
       "dIpv6SnoopObjects": dIpv6SnoopObjects,
       "dIpv6SnoopGlobal": dIpv6SnoopGlobal,
       "dIpv6SnoopStationMoveEnabled": dIpv6SnoopStationMoveEnabled,
       "dIpv6SnoopPolicy": dIpv6SnoopPolicy,
       "dIpv6SnoopPolicyNumber": dIpv6SnoopPolicyNumber,
       "dIpv6SnoopPolicyTable": dIpv6SnoopPolicyTable,
       "dIpv6SnoopPolicyEntry": dIpv6SnoopPolicyEntry,
       "dIpv6SnoopPolicyName": dIpv6SnoopPolicyName,
       "dIpv6SnoopPolicyProtocol": dIpv6SnoopPolicyProtocol,
       "dIpv6SnoopPolicyLimitAddrCount": dIpv6SnoopPolicyLimitAddrCount,
       "dIpv6SnoopPolicyRowStatus": dIpv6SnoopPolicyRowStatus,
       "dIpv6SnoopInterface": dIpv6SnoopInterface,
       "dIpv6SnoopPolicyAttachTable": dIpv6SnoopPolicyAttachTable,
       "dIpv6SnoopPolicyAttachEntry": dIpv6SnoopPolicyAttachEntry,
       "dIpv6SnoopPolicyAttachVlanId": dIpv6SnoopPolicyAttachVlanId,
       "dIpv6SnoopPolicyAttachPolicy": dIpv6SnoopPolicyAttachPolicy,
       "dIpv6SnoopPolicyAttachRowStatus": dIpv6SnoopPolicyAttachRowStatus,
       "dIpv6SnoopConformance": dIpv6SnoopConformance,
       "dIpv6SnoopMIBCompliances": dIpv6SnoopMIBCompliances,
       "dIpv6SnoopMIBCompliance": dIpv6SnoopMIBCompliance,
       "dIpv6SnoopMIBGroups": dIpv6SnoopMIBGroups,
       "dIpv6SnoopPolicyGroup": dIpv6SnoopPolicyGroup,
       "dIpv6SnoopPolicyAttachGroup": dIpv6SnoopPolicyAttachGroup,
       "dIpv6SnoopStationMoveCfgGroup": dIpv6SnoopStationMoveCfgGroup}
)
