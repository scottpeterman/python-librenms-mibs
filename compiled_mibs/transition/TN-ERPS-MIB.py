# SNMP MIB module (TN-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ERPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:25 2025
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

(Dot1agCfmMepId,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProtectionMIB,) = mibBuilder.importSymbols(
    "TN-PROTECTION-MIB",
    "tnProtectionMIB")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnERPSMIB_ObjectIdentity = ObjectIdentity
tnERPSMIB = _TnERPSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3)
)
_TnERPSMIBNotifications_ObjectIdentity = ObjectIdentity
tnERPSMIBNotifications = _TnERPSMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 1)
)
_TnERPSMgmtObjects_ObjectIdentity = ObjectIdentity
tnERPSMgmtObjects = _TnERPSMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2)
)
_TnERPSTable_Object = MibTable
tnERPSTable = _TnERPSTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tnERPSTable.setStatus("current")
_TnERPSEntry_Object = MibTableRow
tnERPSEntry = _TnERPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1)
)
tnERPSEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
)
if mibBuilder.loadTexts:
    tnERPSEntry.setStatus("current")


class _TnERPSinstance_Type(Unsigned32):
    """Custom type tnERPSinstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnERPSinstance_Type.__name__ = "Unsigned32"
_TnERPSinstance_Object = MibTableColumn
tnERPSinstance = _TnERPSinstance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 1),
    _TnERPSinstance_Type()
)
tnERPSinstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnERPSinstance.setStatus("current")
_TnERPSPort0_Type = Integer32
_TnERPSPort0_Object = MibTableColumn
tnERPSPort0 = _TnERPSPort0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 2),
    _TnERPSPort0_Type()
)
tnERPSPort0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSPort0.setStatus("current")
_TnERPSPort1_Type = Integer32
_TnERPSPort1_Object = MibTableColumn
tnERPSPort1 = _TnERPSPort1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 3),
    _TnERPSPort1_Type()
)
tnERPSPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSPort1.setStatus("current")
_TnERPSPort0ApsMep_Type = Integer32
_TnERPSPort0ApsMep_Object = MibTableColumn
tnERPSPort0ApsMep = _TnERPSPort0ApsMep_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 4),
    _TnERPSPort0ApsMep_Type()
)
tnERPSPort0ApsMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSPort0ApsMep.setStatus("current")
_TnERPSPort1ApsMep_Type = Integer32
_TnERPSPort1ApsMep_Object = MibTableColumn
tnERPSPort1ApsMep = _TnERPSPort1ApsMep_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 5),
    _TnERPSPort1ApsMep_Type()
)
tnERPSPort1ApsMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSPort1ApsMep.setStatus("current")
_TnERPSPort0SfMep_Type = Integer32
_TnERPSPort0SfMep_Object = MibTableColumn
tnERPSPort0SfMep = _TnERPSPort0SfMep_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 6),
    _TnERPSPort0SfMep_Type()
)
tnERPSPort0SfMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSPort0SfMep.setStatus("current")
_TnERPSPort1SfMep_Type = Integer32
_TnERPSPort1SfMep_Object = MibTableColumn
tnERPSPort1SfMep = _TnERPSPort1SfMep_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 7),
    _TnERPSPort1SfMep_Type()
)
tnERPSPort1SfMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSPort1SfMep.setStatus("current")


class _TnERPSRingType_Type(Integer32):
    """Custom type tnERPSRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 1),
          ("sub", 2))
    )


_TnERPSRingType_Type.__name__ = "Integer32"
_TnERPSRingType_Object = MibTableColumn
tnERPSRingType = _TnERPSRingType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 8),
    _TnERPSRingType_Type()
)
tnERPSRingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSRingType.setStatus("current")
_TnERPSInterconnectednode_Type = TruthValue
_TnERPSInterconnectednode_Object = MibTableColumn
tnERPSInterconnectednode = _TnERPSInterconnectednode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 9),
    _TnERPSInterconnectednode_Type()
)
tnERPSInterconnectednode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSInterconnectednode.setStatus("current")
_TnERPSVirtualChannel_Type = TruthValue
_TnERPSVirtualChannel_Object = MibTableColumn
tnERPSVirtualChannel = _TnERPSVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 10),
    _TnERPSVirtualChannel_Type()
)
tnERPSVirtualChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSVirtualChannel.setStatus("current")
_TnERPSMajorRingID_Type = Integer32
_TnERPSMajorRingID_Object = MibTableColumn
tnERPSMajorRingID = _TnERPSMajorRingID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 11),
    _TnERPSMajorRingID_Type()
)
tnERPSMajorRingID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSMajorRingID.setStatus("current")


class _TnERPSAlarm_Type(Integer32):
    """Custom type tnERPSAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_TnERPSAlarm_Type.__name__ = "Integer32"
_TnERPSAlarm_Object = MibTableColumn
tnERPSAlarm = _TnERPSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 12),
    _TnERPSAlarm_Type()
)
tnERPSAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSAlarm.setStatus("current")
_TnERPSRowStatus_Type = RowStatus
_TnERPSRowStatus_Object = MibTableColumn
tnERPSRowStatus = _TnERPSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 1, 1, 13),
    _TnERPSRowStatus_Type()
)
tnERPSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnERPSRowStatus.setStatus("current")
_TnERPSConfigTable_Object = MibTable
tnERPSConfigTable = _TnERPSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tnERPSConfigTable.setStatus("current")
_TnERPSConfigEntry_Object = MibTableRow
tnERPSConfigEntry = _TnERPSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2, 1)
)
tnERPSConfigEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
)
if mibBuilder.loadTexts:
    tnERPSConfigEntry.setStatus("current")


class _TnERPSConfigStatus_Type(Integer32):
    """Custom type tnERPSConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_TnERPSConfigStatus_Type.__name__ = "Integer32"
_TnERPSConfigStatus_Object = MibTableColumn
tnERPSConfigStatus = _TnERPSConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2, 1, 1),
    _TnERPSConfigStatus_Type()
)
tnERPSConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSConfigStatus.setStatus("current")
_TnERPSConfigGuardTime_Type = Integer32
_TnERPSConfigGuardTime_Object = MibTableColumn
tnERPSConfigGuardTime = _TnERPSConfigGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2, 1, 2),
    _TnERPSConfigGuardTime_Type()
)
tnERPSConfigGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSConfigGuardTime.setStatus("current")


class _TnERPSConfigWtrTime_Type(Integer32):
    """Custom type tnERPSConfigWtrTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("t1min", 1),
          ("t2min", 2),
          ("t3min", 3),
          ("t4min", 4),
          ("t5min", 5),
          ("t6min", 6),
          ("t7min", 7),
          ("t8min", 8),
          ("t9min", 9),
          ("t10min", 10),
          ("t11min", 11),
          ("t12min", 12))
    )


_TnERPSConfigWtrTime_Type.__name__ = "Integer32"
_TnERPSConfigWtrTime_Object = MibTableColumn
tnERPSConfigWtrTime = _TnERPSConfigWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2, 1, 3),
    _TnERPSConfigWtrTime_Type()
)
tnERPSConfigWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSConfigWtrTime.setStatus("current")
_TnERPSConfigHoldOffTime_Type = Integer32
_TnERPSConfigHoldOffTime_Object = MibTableColumn
tnERPSConfigHoldOffTime = _TnERPSConfigHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2, 1, 4),
    _TnERPSConfigHoldOffTime_Type()
)
tnERPSConfigHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSConfigHoldOffTime.setStatus("current")


class _TnERPSConfigVersion_Type(Integer32):
    """Custom type tnERPSConfigVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_TnERPSConfigVersion_Type.__name__ = "Integer32"
_TnERPSConfigVersion_Object = MibTableColumn
tnERPSConfigVersion = _TnERPSConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2, 1, 5),
    _TnERPSConfigVersion_Type()
)
tnERPSConfigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSConfigVersion.setStatus("current")
_TnERPSConfigRevertive_Type = TruthValue
_TnERPSConfigRevertive_Object = MibTableColumn
tnERPSConfigRevertive = _TnERPSConfigRevertive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 2, 1, 6),
    _TnERPSConfigRevertive_Type()
)
tnERPSConfigRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSConfigRevertive.setStatus("current")
_TnERPSRPLTable_Object = MibTable
tnERPSRPLTable = _TnERPSRPLTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 3)
)
if mibBuilder.loadTexts:
    tnERPSRPLTable.setStatus("current")
_TnERPSRPLEntry_Object = MibTableRow
tnERPSRPLEntry = _TnERPSRPLEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 3, 1)
)
tnERPSRPLEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
)
if mibBuilder.loadTexts:
    tnERPSRPLEntry.setStatus("current")


class _TnERPSRPLRole_Type(Integer32):
    """Custom type tnERPSRPLRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("owner", 2),
          ("neighbour", 3))
    )


_TnERPSRPLRole_Type.__name__ = "Integer32"
_TnERPSRPLRole_Object = MibTableColumn
tnERPSRPLRole = _TnERPSRPLRole_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 3, 1, 1),
    _TnERPSRPLRole_Type()
)
tnERPSRPLRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSRPLRole.setStatus("current")


class _TnERPSRPLPort_Type(Integer32):
    """Custom type tnERPSRPLPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("port0", 2),
          ("port1", 3))
    )


_TnERPSRPLPort_Type.__name__ = "Integer32"
_TnERPSRPLPort_Object = MibTableColumn
tnERPSRPLPort = _TnERPSRPLPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 3, 1, 2),
    _TnERPSRPLPort_Type()
)
tnERPSRPLPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSRPLPort.setStatus("current")
_TnERPSRPLClear_Type = TruthValue
_TnERPSRPLClear_Object = MibTableColumn
tnERPSRPLClear = _TnERPSRPLClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 3, 1, 3),
    _TnERPSRPLClear_Type()
)
tnERPSRPLClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSRPLClear.setStatus("current")
_TnERPSCommandTable_Object = MibTable
tnERPSCommandTable = _TnERPSCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 4)
)
if mibBuilder.loadTexts:
    tnERPSCommandTable.setStatus("current")
_TnERPSCommandEntry_Object = MibTableRow
tnERPSCommandEntry = _TnERPSCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 4, 1)
)
tnERPSCommandEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
)
if mibBuilder.loadTexts:
    tnERPSCommandEntry.setStatus("current")


class _TnERPSCommand_Type(Integer32):
    """Custom type tnERPSCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("manual", 2),
          ("forced", 3),
          ("clear", 4))
    )


_TnERPSCommand_Type.__name__ = "Integer32"
_TnERPSCommand_Object = MibTableColumn
tnERPSCommand = _TnERPSCommand_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 4, 1, 1),
    _TnERPSCommand_Type()
)
tnERPSCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSCommand.setStatus("current")


class _TnERPSCommandPort_Type(Integer32):
    """Custom type tnERPSCommandPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("port0", 2),
          ("port1", 3))
    )


_TnERPSCommandPort_Type.__name__ = "Integer32"
_TnERPSCommandPort_Object = MibTableColumn
tnERPSCommandPort = _TnERPSCommandPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 4, 1, 2),
    _TnERPSCommandPort_Type()
)
tnERPSCommandPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSCommandPort.setStatus("current")
_TnERPSStateTable_Object = MibTable
tnERPSStateTable = _TnERPSStateTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5)
)
if mibBuilder.loadTexts:
    tnERPSStateTable.setStatus("current")
_TnERPSStateEntry_Object = MibTableRow
tnERPSStateEntry = _TnERPSStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1)
)
tnERPSStateEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
)
if mibBuilder.loadTexts:
    tnERPSStateEntry.setStatus("current")


class _TnERPSState_Type(Integer32):
    """Custom type tnERPSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("protected", 2),
          ("manual", 3),
          ("forced", 4),
          ("pending", 5),
          ("unknown", 6))
    )


_TnERPSState_Type.__name__ = "Integer32"
_TnERPSState_Object = MibTableColumn
tnERPSState = _TnERPSState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 1),
    _TnERPSState_Type()
)
tnERPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSState.setStatus("current")


class _TnERPSStatePort0_Type(Integer32):
    """Custom type tnERPSStatePort0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("sf", 2))
    )


_TnERPSStatePort0_Type.__name__ = "Integer32"
_TnERPSStatePort0_Object = MibTableColumn
tnERPSStatePort0 = _TnERPSStatePort0_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 2),
    _TnERPSStatePort0_Type()
)
tnERPSStatePort0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStatePort0.setStatus("current")


class _TnERPSStatePort1_Type(Integer32):
    """Custom type tnERPSStatePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("sf", 2))
    )


_TnERPSStatePort1_Type.__name__ = "Integer32"
_TnERPSStatePort1_Object = MibTableColumn
tnERPSStatePort1 = _TnERPSStatePort1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 3),
    _TnERPSStatePort1_Type()
)
tnERPSStatePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStatePort1.setStatus("current")
_TnERPSStateTxAps_Type = DisplayString
_TnERPSStateTxAps_Object = MibTableColumn
tnERPSStateTxAps = _TnERPSStateTxAps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 4),
    _TnERPSStateTxAps_Type()
)
tnERPSStateTxAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStateTxAps.setStatus("current")
_TnERPSStatePort0RxAps_Type = DisplayString
_TnERPSStatePort0RxAps_Object = MibTableColumn
tnERPSStatePort0RxAps = _TnERPSStatePort0RxAps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 5),
    _TnERPSStatePort0RxAps_Type()
)
tnERPSStatePort0RxAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStatePort0RxAps.setStatus("current")
_TnERPSStatePort1RxAps_Type = DisplayString
_TnERPSStatePort1RxAps_Object = MibTableColumn
tnERPSStatePort1RxAps = _TnERPSStatePort1RxAps_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 6),
    _TnERPSStatePort1RxAps_Type()
)
tnERPSStatePort1RxAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStatePort1RxAps.setStatus("current")
_TnERPSStateWtrRemaining_Type = Integer32
_TnERPSStateWtrRemaining_Object = MibTableColumn
tnERPSStateWtrRemaining = _TnERPSStateWtrRemaining_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 7),
    _TnERPSStateWtrRemaining_Type()
)
tnERPSStateWtrRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStateWtrRemaining.setStatus("current")


class _TnERPSStateRPLUnBlocked_Type(Integer32):
    """Custom type tnERPSStateRPLUnBlocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("unblock", 1))
    )


_TnERPSStateRPLUnBlocked_Type.__name__ = "Integer32"
_TnERPSStateRPLUnBlocked_Object = MibTableColumn
tnERPSStateRPLUnBlocked = _TnERPSStateRPLUnBlocked_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 8),
    _TnERPSStateRPLUnBlocked_Type()
)
tnERPSStateRPLUnBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStateRPLUnBlocked.setStatus("current")


class _TnERPSStateNoApsReceived_Type(Integer32):
    """Custom type tnERPSStateNoApsReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noapsReceived", 0),
          ("apsReceived", 1))
    )


_TnERPSStateNoApsReceived_Type.__name__ = "Integer32"
_TnERPSStateNoApsReceived_Object = MibTableColumn
tnERPSStateNoApsReceived = _TnERPSStateNoApsReceived_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 9),
    _TnERPSStateNoApsReceived_Type()
)
tnERPSStateNoApsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStateNoApsReceived.setStatus("current")


class _TnERPSStatePort0Blockstatus_Type(Integer32):
    """Custom type tnERPSStatePort0Blockstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("unblock", 1))
    )


_TnERPSStatePort0Blockstatus_Type.__name__ = "Integer32"
_TnERPSStatePort0Blockstatus_Object = MibTableColumn
tnERPSStatePort0Blockstatus = _TnERPSStatePort0Blockstatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 10),
    _TnERPSStatePort0Blockstatus_Type()
)
tnERPSStatePort0Blockstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStatePort0Blockstatus.setStatus("current")


class _TnERPSStatePort1Blockstatus_Type(Integer32):
    """Custom type tnERPSStatePort1Blockstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("unblock", 1))
    )


_TnERPSStatePort1Blockstatus_Type.__name__ = "Integer32"
_TnERPSStatePort1Blockstatus_Object = MibTableColumn
tnERPSStatePort1Blockstatus = _TnERPSStatePort1Blockstatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 11),
    _TnERPSStatePort1Blockstatus_Type()
)
tnERPSStatePort1Blockstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStatePort1Blockstatus.setStatus("current")
_TnERPSStateFopAlarm_Type = TruthValue
_TnERPSStateFopAlarm_Object = MibTableColumn
tnERPSStateFopAlarm = _TnERPSStateFopAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 5, 1, 12),
    _TnERPSStateFopAlarm_Type()
)
tnERPSStateFopAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSStateFopAlarm.setStatus("current")
_TnERPSVlanTable_Object = MibTable
tnERPSVlanTable = _TnERPSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 6)
)
if mibBuilder.loadTexts:
    tnERPSVlanTable.setStatus("current")
_TnERPSVlanEntry_Object = MibTableRow
tnERPSVlanEntry = _TnERPSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 6, 1)
)
tnERPSVlanEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
    (0, "TN-ERPS-MIB", "tnERPSVlanInstance"),
)
if mibBuilder.loadTexts:
    tnERPSVlanEntry.setStatus("current")


class _TnERPSVlanInstance_Type(Unsigned32):
    """Custom type tnERPSVlanInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TnERPSVlanInstance_Type.__name__ = "Unsigned32"
_TnERPSVlanInstance_Object = MibTableColumn
tnERPSVlanInstance = _TnERPSVlanInstance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 6, 1, 1),
    _TnERPSVlanInstance_Type()
)
tnERPSVlanInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnERPSVlanInstance.setStatus("current")
_TnERPSVlanId_Type = VlanId
_TnERPSVlanId_Object = MibTableColumn
tnERPSVlanId = _TnERPSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 6, 1, 2),
    _TnERPSVlanId_Type()
)
tnERPSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSVlanId.setStatus("current")
_TnERPSVlanRowStatus_Type = RowStatus
_TnERPSVlanRowStatus_Object = MibTableColumn
tnERPSVlanRowStatus = _TnERPSVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 6, 1, 3),
    _TnERPSVlanRowStatus_Type()
)
tnERPSVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSVlanRowStatus.setStatus("current")
_TnERPSSubRingCfgTable_Object = MibTable
tnERPSSubRingCfgTable = _TnERPSSubRingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 7)
)
if mibBuilder.loadTexts:
    tnERPSSubRingCfgTable.setStatus("current")
_TnERPSSubRingCfgEntry_Object = MibTableRow
tnERPSSubRingCfgEntry = _TnERPSSubRingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 7, 1)
)
tnERPSSubRingCfgEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
)
if mibBuilder.loadTexts:
    tnERPSSubRingCfgEntry.setStatus("current")
_TnERPSSubRingType_Type = DisplayString
_TnERPSSubRingType_Object = MibTableColumn
tnERPSSubRingType = _TnERPSSubRingType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 7, 1, 1),
    _TnERPSSubRingType_Type()
)
tnERPSSubRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSSubRingType.setStatus("current")
_TnERPSSubRingTopologyChange_Type = TruthValue
_TnERPSSubRingTopologyChange_Object = MibTableColumn
tnERPSSubRingTopologyChange = _TnERPSSubRingTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 7, 1, 2),
    _TnERPSSubRingTopologyChange_Type()
)
tnERPSSubRingTopologyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnERPSSubRingTopologyChange.setStatus("current")
_TnERPSStatisticsTable_Object = MibTable
tnERPSStatisticsTable = _TnERPSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8)
)
if mibBuilder.loadTexts:
    tnERPSStatisticsTable.setStatus("current")
_TnERPSStatisticsEntry_Object = MibTableRow
tnERPSStatisticsEntry = _TnERPSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1)
)
tnERPSStatisticsEntry.setIndexNames(
    (0, "TN-ERPS-MIB", "tnERPSinstance"),
)
if mibBuilder.loadTexts:
    tnERPSStatisticsEntry.setStatus("current")
_TnERPSRAPSPDUReceived_Type = Integer32
_TnERPSRAPSPDUReceived_Object = MibTableColumn
tnERPSRAPSPDUReceived = _TnERPSRAPSPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1, 1),
    _TnERPSRAPSPDUReceived_Type()
)
tnERPSRAPSPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSRAPSPDUReceived.setStatus("current")
_TnERPSRAPSPDUDropped_Type = Integer32
_TnERPSRAPSPDUDropped_Object = MibTableColumn
tnERPSRAPSPDUDropped = _TnERPSRAPSPDUDropped_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1, 2),
    _TnERPSRAPSPDUDropped_Type()
)
tnERPSRAPSPDUDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSRAPSPDUDropped.setStatus("current")
_TnERPSLocalSFOccurred_Type = Integer32
_TnERPSLocalSFOccurred_Object = MibTableColumn
tnERPSLocalSFOccurred = _TnERPSLocalSFOccurred_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1, 3),
    _TnERPSLocalSFOccurred_Type()
)
tnERPSLocalSFOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSLocalSFOccurred.setStatus("current")
_TnERPSLocalSFCleared_Type = Integer32
_TnERPSLocalSFCleared_Object = MibTableColumn
tnERPSLocalSFCleared = _TnERPSLocalSFCleared_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1, 4),
    _TnERPSLocalSFCleared_Type()
)
tnERPSLocalSFCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSLocalSFCleared.setStatus("current")
_TnERPSRemoteSFReceived_Type = Integer32
_TnERPSRemoteSFReceived_Object = MibTableColumn
tnERPSRemoteSFReceived = _TnERPSRemoteSFReceived_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1, 5),
    _TnERPSRemoteSFReceived_Type()
)
tnERPSRemoteSFReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSRemoteSFReceived.setStatus("current")
_TnERPSRemoteFSReceived_Type = Integer32
_TnERPSRemoteFSReceived_Object = MibTableColumn
tnERPSRemoteFSReceived = _TnERPSRemoteFSReceived_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1, 6),
    _TnERPSRemoteFSReceived_Type()
)
tnERPSRemoteFSReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSRemoteFSReceived.setStatus("current")
_TnERPSNRMessageSent_Type = Integer32
_TnERPSNRMessageSent_Object = MibTableColumn
tnERPSNRMessageSent = _TnERPSNRMessageSent_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 2, 8, 1, 7),
    _TnERPSNRMessageSent_Type()
)
tnERPSNRMessageSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnERPSNRMessageSent.setStatus("current")
_TnERPSMIBConformance_ObjectIdentity = ObjectIdentity
tnERPSMIBConformance = _TnERPSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 3)
)

# Managed Objects groups


# Notification objects

tnErpsAlarmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 1, 1)
)
tnErpsAlarmUp.setObjects(
      *(("TN-ERPS-MIB", "tnERPSState"),
        ("TN-ERPS-MIB", "tnERPSStatePort0"),
        ("TN-ERPS-MIB", "tnERPSStatePort1"),
        ("TN-ERPS-MIB", "tnERPSStateRPLUnBlocked"),
        ("TN-ERPS-MIB", "tnERPSStateNoApsReceived"),
        ("TN-ERPS-MIB", "tnERPSStatePort0Blockstatus"),
        ("TN-ERPS-MIB", "tnERPSStatePort1Blockstatus"))
)
if mibBuilder.loadTexts:
    tnErpsAlarmUp.setStatus(
        "current"
    )

tnErpsAlarmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 109, 3, 1, 2)
)
tnErpsAlarmDown.setObjects(
      *(("TN-ERPS-MIB", "tnERPSState"),
        ("TN-ERPS-MIB", "tnERPSStatePort0"),
        ("TN-ERPS-MIB", "tnERPSStatePort1"),
        ("TN-ERPS-MIB", "tnERPSStateRPLUnBlocked"),
        ("TN-ERPS-MIB", "tnERPSStateNoApsReceived"),
        ("TN-ERPS-MIB", "tnERPSStatePort0Blockstatus"),
        ("TN-ERPS-MIB", "tnERPSStatePort1Blockstatus"))
)
if mibBuilder.loadTexts:
    tnErpsAlarmDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ERPS-MIB",
    **{"tnERPSMIB": tnERPSMIB,
       "tnERPSMIBNotifications": tnERPSMIBNotifications,
       "tnErpsAlarmUp": tnErpsAlarmUp,
       "tnErpsAlarmDown": tnErpsAlarmDown,
       "tnERPSMgmtObjects": tnERPSMgmtObjects,
       "tnERPSTable": tnERPSTable,
       "tnERPSEntry": tnERPSEntry,
       "tnERPSinstance": tnERPSinstance,
       "tnERPSPort0": tnERPSPort0,
       "tnERPSPort1": tnERPSPort1,
       "tnERPSPort0ApsMep": tnERPSPort0ApsMep,
       "tnERPSPort1ApsMep": tnERPSPort1ApsMep,
       "tnERPSPort0SfMep": tnERPSPort0SfMep,
       "tnERPSPort1SfMep": tnERPSPort1SfMep,
       "tnERPSRingType": tnERPSRingType,
       "tnERPSInterconnectednode": tnERPSInterconnectednode,
       "tnERPSVirtualChannel": tnERPSVirtualChannel,
       "tnERPSMajorRingID": tnERPSMajorRingID,
       "tnERPSAlarm": tnERPSAlarm,
       "tnERPSRowStatus": tnERPSRowStatus,
       "tnERPSConfigTable": tnERPSConfigTable,
       "tnERPSConfigEntry": tnERPSConfigEntry,
       "tnERPSConfigStatus": tnERPSConfigStatus,
       "tnERPSConfigGuardTime": tnERPSConfigGuardTime,
       "tnERPSConfigWtrTime": tnERPSConfigWtrTime,
       "tnERPSConfigHoldOffTime": tnERPSConfigHoldOffTime,
       "tnERPSConfigVersion": tnERPSConfigVersion,
       "tnERPSConfigRevertive": tnERPSConfigRevertive,
       "tnERPSRPLTable": tnERPSRPLTable,
       "tnERPSRPLEntry": tnERPSRPLEntry,
       "tnERPSRPLRole": tnERPSRPLRole,
       "tnERPSRPLPort": tnERPSRPLPort,
       "tnERPSRPLClear": tnERPSRPLClear,
       "tnERPSCommandTable": tnERPSCommandTable,
       "tnERPSCommandEntry": tnERPSCommandEntry,
       "tnERPSCommand": tnERPSCommand,
       "tnERPSCommandPort": tnERPSCommandPort,
       "tnERPSStateTable": tnERPSStateTable,
       "tnERPSStateEntry": tnERPSStateEntry,
       "tnERPSState": tnERPSState,
       "tnERPSStatePort0": tnERPSStatePort0,
       "tnERPSStatePort1": tnERPSStatePort1,
       "tnERPSStateTxAps": tnERPSStateTxAps,
       "tnERPSStatePort0RxAps": tnERPSStatePort0RxAps,
       "tnERPSStatePort1RxAps": tnERPSStatePort1RxAps,
       "tnERPSStateWtrRemaining": tnERPSStateWtrRemaining,
       "tnERPSStateRPLUnBlocked": tnERPSStateRPLUnBlocked,
       "tnERPSStateNoApsReceived": tnERPSStateNoApsReceived,
       "tnERPSStatePort0Blockstatus": tnERPSStatePort0Blockstatus,
       "tnERPSStatePort1Blockstatus": tnERPSStatePort1Blockstatus,
       "tnERPSStateFopAlarm": tnERPSStateFopAlarm,
       "tnERPSVlanTable": tnERPSVlanTable,
       "tnERPSVlanEntry": tnERPSVlanEntry,
       "tnERPSVlanInstance": tnERPSVlanInstance,
       "tnERPSVlanId": tnERPSVlanId,
       "tnERPSVlanRowStatus": tnERPSVlanRowStatus,
       "tnERPSSubRingCfgTable": tnERPSSubRingCfgTable,
       "tnERPSSubRingCfgEntry": tnERPSSubRingCfgEntry,
       "tnERPSSubRingType": tnERPSSubRingType,
       "tnERPSSubRingTopologyChange": tnERPSSubRingTopologyChange,
       "tnERPSStatisticsTable": tnERPSStatisticsTable,
       "tnERPSStatisticsEntry": tnERPSStatisticsEntry,
       "tnERPSRAPSPDUReceived": tnERPSRAPSPDUReceived,
       "tnERPSRAPSPDUDropped": tnERPSRAPSPDUDropped,
       "tnERPSLocalSFOccurred": tnERPSLocalSFOccurred,
       "tnERPSLocalSFCleared": tnERPSLocalSFCleared,
       "tnERPSRemoteSFReceived": tnERPSRemoteSFReceived,
       "tnERPSRemoteFSReceived": tnERPSRemoteFSReceived,
       "tnERPSNRMessageSent": tnERPSNRMessageSent,
       "tnERPSMIBConformance": tnERPSMIBConformance}
)
