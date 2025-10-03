# SNMP MIB module (DLINKSW-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-ERPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:05 2025
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

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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


# MODULE-IDENTITY

dlinkSwErpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78)
)
if mibBuilder.loadTexts:
    dlinkSwErpsMIB.setRevisions(
        ("2013-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DErpsMIBNotification_ObjectIdentity = ObjectIdentity
dErpsMIBNotification = _DErpsMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 0)
)
_DErpsMIBObjects_ObjectIdentity = ObjectIdentity
dErpsMIBObjects = _DErpsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1)
)
_DErpsGenCtrl_ObjectIdentity = ObjectIdentity
dErpsGenCtrl = _DErpsGenCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 1)
)
_DErpsNotificationEnabled_Type = TruthValue
_DErpsNotificationEnabled_Object = MibScalar
dErpsNotificationEnabled = _DErpsNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 1, 3),
    _DErpsNotificationEnabled_Type()
)
dErpsNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dErpsNotificationEnabled.setStatus("current")
_DErpsProfileTable_Object = MibTable
dErpsProfileTable = _DErpsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2)
)
if mibBuilder.loadTexts:
    dErpsProfileTable.setStatus("current")
_DErpsProfileEntry_Object = MibTableRow
dErpsProfileEntry = _DErpsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1)
)
dErpsProfileEntry.setIndexNames(
    (0, "DLINKSW-ERPS-MIB", "dErpsProfName"),
)
if mibBuilder.loadTexts:
    dErpsProfileEntry.setStatus("current")


class _DErpsProfName_Type(DisplayString):
    """Custom type dErpsProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DErpsProfName_Type.__name__ = "DisplayString"
_DErpsProfName_Object = MibTableColumn
dErpsProfName = _DErpsProfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1, 1),
    _DErpsProfName_Type()
)
dErpsProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErpsProfName.setStatus("current")
_DErpsProfRowStatus_Type = RowStatus
_DErpsProfRowStatus_Object = MibTableColumn
dErpsProfRowStatus = _DErpsProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1, 2),
    _DErpsProfRowStatus_Type()
)
dErpsProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsProfRowStatus.setStatus("current")


class _DErpsProfTcnPropagationEnabled_Type(TruthValue):
    """Custom type dErpsProfTcnPropagationEnabled based on TruthValue"""
    defaultValue = 2


_DErpsProfTcnPropagationEnabled_Type.__name__ = "TruthValue"
_DErpsProfTcnPropagationEnabled_Object = MibTableColumn
dErpsProfTcnPropagationEnabled = _DErpsProfTcnPropagationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1, 3),
    _DErpsProfTcnPropagationEnabled_Type()
)
dErpsProfTcnPropagationEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsProfTcnPropagationEnabled.setStatus("current")


class _DErpsProfRevertiveEnabled_Type(TruthValue):
    """Custom type dErpsProfRevertiveEnabled based on TruthValue"""
    defaultValue = 1


_DErpsProfRevertiveEnabled_Type.__name__ = "TruthValue"
_DErpsProfRevertiveEnabled_Object = MibTableColumn
dErpsProfRevertiveEnabled = _DErpsProfRevertiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1, 4),
    _DErpsProfRevertiveEnabled_Type()
)
dErpsProfRevertiveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsProfRevertiveEnabled.setStatus("current")


class _DErpsProfGuardTimer_Type(Unsigned32):
    """Custom type dErpsProfGuardTimer based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_DErpsProfGuardTimer_Type.__name__ = "Unsigned32"
_DErpsProfGuardTimer_Object = MibTableColumn
dErpsProfGuardTimer = _DErpsProfGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1, 5),
    _DErpsProfGuardTimer_Type()
)
dErpsProfGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsProfGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    dErpsProfGuardTimer.setUnits("milliseconds")


class _DErpsProfHoldOffTimer_Type(Unsigned32):
    """Custom type dErpsProfHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DErpsProfHoldOffTimer_Type.__name__ = "Unsigned32"
_DErpsProfHoldOffTimer_Object = MibTableColumn
dErpsProfHoldOffTimer = _DErpsProfHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1, 6),
    _DErpsProfHoldOffTimer_Type()
)
dErpsProfHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsProfHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    dErpsProfHoldOffTimer.setUnits("seconds")


class _DErpsProfWtrTimer_Type(Unsigned32):
    """Custom type dErpsProfWtrTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DErpsProfWtrTimer_Type.__name__ = "Unsigned32"
_DErpsProfWtrTimer_Object = MibTableColumn
dErpsProfWtrTimer = _DErpsProfWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 2, 1, 7),
    _DErpsProfWtrTimer_Type()
)
dErpsProfWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsProfWtrTimer.setStatus("current")
if mibBuilder.loadTexts:
    dErpsProfWtrTimer.setUnits("minutes")
_DErpsEtherRingTable_Object = MibTable
dErpsEtherRingTable = _DErpsEtherRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 3)
)
if mibBuilder.loadTexts:
    dErpsEtherRingTable.setStatus("current")
_DErpsEtherRingEntry_Object = MibTableRow
dErpsEtherRingEntry = _DErpsEtherRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 3, 1)
)
dErpsEtherRingEntry.setIndexNames(
    (0, "DLINKSW-ERPS-MIB", "dErpsEtherRingName"),
)
if mibBuilder.loadTexts:
    dErpsEtherRingEntry.setStatus("current")


class _DErpsEtherRingName_Type(DisplayString):
    """Custom type dErpsEtherRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DErpsEtherRingName_Type.__name__ = "DisplayString"
_DErpsEtherRingName_Object = MibTableColumn
dErpsEtherRingName = _DErpsEtherRingName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 3, 1, 1),
    _DErpsEtherRingName_Type()
)
dErpsEtherRingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErpsEtherRingName.setStatus("current")
_DErpsEtherRingRowStatus_Type = RowStatus
_DErpsEtherRingRowStatus_Object = MibTableColumn
dErpsEtherRingRowStatus = _DErpsEtherRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 3, 1, 2),
    _DErpsEtherRingRowStatus_Type()
)
dErpsEtherRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsEtherRingRowStatus.setStatus("current")


class _DErpsEtherRingAdminPort0IfIdx_Type(InterfaceIndexOrZero):
    """Custom type dErpsEtherRingAdminPort0IfIdx based on InterfaceIndexOrZero"""
    defaultValue = 0


_DErpsEtherRingAdminPort0IfIdx_Type.__name__ = "InterfaceIndexOrZero"
_DErpsEtherRingAdminPort0IfIdx_Object = MibTableColumn
dErpsEtherRingAdminPort0IfIdx = _DErpsEtherRingAdminPort0IfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 3, 1, 3),
    _DErpsEtherRingAdminPort0IfIdx_Type()
)
dErpsEtherRingAdminPort0IfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsEtherRingAdminPort0IfIdx.setStatus("current")


class _DErpsEtherRingAdminPort1IfIdx_Type(InterfaceIndexOrZero):
    """Custom type dErpsEtherRingAdminPort1IfIdx based on InterfaceIndexOrZero"""
    defaultValue = 0


_DErpsEtherRingAdminPort1IfIdx_Type.__name__ = "InterfaceIndexOrZero"
_DErpsEtherRingAdminPort1IfIdx_Object = MibTableColumn
dErpsEtherRingAdminPort1IfIdx = _DErpsEtherRingAdminPort1IfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 3, 1, 4),
    _DErpsEtherRingAdminPort1IfIdx_Type()
)
dErpsEtherRingAdminPort1IfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsEtherRingAdminPort1IfIdx.setStatus("current")
_DErpsEtherSubRingTable_Object = MibTable
dErpsEtherSubRingTable = _DErpsEtherSubRingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 4)
)
if mibBuilder.loadTexts:
    dErpsEtherSubRingTable.setStatus("current")
_DErpsEtherSubRingEntry_Object = MibTableRow
dErpsEtherSubRingEntry = _DErpsEtherSubRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 4, 1)
)
dErpsEtherSubRingEntry.setIndexNames(
    (0, "DLINKSW-ERPS-MIB", "dErpsEtherRingName"),
    (0, "DLINKSW-ERPS-MIB", "dErpsEtherSubRingName"),
)
if mibBuilder.loadTexts:
    dErpsEtherSubRingEntry.setStatus("current")


class _DErpsEtherSubRingName_Type(DisplayString):
    """Custom type dErpsEtherSubRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DErpsEtherSubRingName_Type.__name__ = "DisplayString"
_DErpsEtherSubRingName_Object = MibTableColumn
dErpsEtherSubRingName = _DErpsEtherSubRingName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 4, 1, 1),
    _DErpsEtherSubRingName_Type()
)
dErpsEtherSubRingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErpsEtherSubRingName.setStatus("current")
_DErpsEtherSubRingRowStatus_Type = RowStatus
_DErpsEtherSubRingRowStatus_Object = MibTableColumn
dErpsEtherSubRingRowStatus = _DErpsEtherSubRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 4, 1, 2),
    _DErpsEtherSubRingRowStatus_Type()
)
dErpsEtherSubRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsEtherSubRingRowStatus.setStatus("current")
_DErpsInstTable_Object = MibTable
dErpsInstTable = _DErpsInstTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5)
)
if mibBuilder.loadTexts:
    dErpsInstTable.setStatus("current")
_DErpsInstEntry_Object = MibTableRow
dErpsInstEntry = _DErpsInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1)
)
dErpsInstEntry.setIndexNames(
    (0, "DLINKSW-ERPS-MIB", "dErpsEtherRingName"),
    (0, "DLINKSW-ERPS-MIB", "dErpsInstInstanceId"),
)
if mibBuilder.loadTexts:
    dErpsInstEntry.setStatus("current")


class _DErpsInstInstanceId_Type(Unsigned32):
    """Custom type dErpsInstInstanceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DErpsInstInstanceId_Type.__name__ = "Unsigned32"
_DErpsInstInstanceId_Object = MibTableColumn
dErpsInstInstanceId = _DErpsInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 1),
    _DErpsInstInstanceId_Type()
)
dErpsInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dErpsInstInstanceId.setStatus("current")
_DErpsInstRowStatus_Type = RowStatus
_DErpsInstRowStatus_Object = MibTableColumn
dErpsInstRowStatus = _DErpsInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 2),
    _DErpsInstRowStatus_Type()
)
dErpsInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstRowStatus.setStatus("current")


class _DErpsInstDescription_Type(DisplayString):
    """Custom type dErpsInstDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DErpsInstDescription_Type.__name__ = "DisplayString"
_DErpsInstDescription_Object = MibTableColumn
dErpsInstDescription = _DErpsInstDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 3),
    _DErpsInstDescription_Type()
)
dErpsInstDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstDescription.setStatus("current")


class _DErpsInstMel_Type(Unsigned32):
    """Custom type dErpsInstMel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DErpsInstMel_Type.__name__ = "Unsigned32"
_DErpsInstMel_Object = MibTableColumn
dErpsInstMel = _DErpsInstMel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 4),
    _DErpsInstMel_Type()
)
dErpsInstMel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstMel.setStatus("current")


class _DErpsInstProfile_Type(DisplayString):
    """Custom type dErpsInstProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DErpsInstProfile_Type.__name__ = "DisplayString"
_DErpsInstProfile_Object = MibTableColumn
dErpsInstProfile = _DErpsInstProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 5),
    _DErpsInstProfile_Type()
)
dErpsInstProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstProfile.setStatus("current")
_DErpsInstApsChannelVlanId_Type = VlanIdOrNone
_DErpsInstApsChannelVlanId_Object = MibTableColumn
dErpsInstApsChannelVlanId = _DErpsInstApsChannelVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 6),
    _DErpsInstApsChannelVlanId_Type()
)
dErpsInstApsChannelVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstApsChannelVlanId.setStatus("current")
_DErpsInstIncludeVlansFirst2K_Type = Dlink2kVlanList
_DErpsInstIncludeVlansFirst2K_Object = MibTableColumn
dErpsInstIncludeVlansFirst2K = _DErpsInstIncludeVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 7),
    _DErpsInstIncludeVlansFirst2K_Type()
)
dErpsInstIncludeVlansFirst2K.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstIncludeVlansFirst2K.setStatus("current")
_DErpsInstIncludeVlansSecond2K_Type = Dlink2kVlanList
_DErpsInstIncludeVlansSecond2K_Object = MibTableColumn
dErpsInstIncludeVlansSecond2K = _DErpsInstIncludeVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 8),
    _DErpsInstIncludeVlansSecond2K_Type()
)
dErpsInstIncludeVlansSecond2K.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstIncludeVlansSecond2K.setStatus("current")


class _DErpsInstAdminRplPort_Type(Integer32):
    """Custom type dErpsInstAdminRplPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 0),
          ("port1", 1),
          ("none", 2))
    )


_DErpsInstAdminRplPort_Type.__name__ = "Integer32"
_DErpsInstAdminRplPort_Object = MibTableColumn
dErpsInstAdminRplPort = _DErpsInstAdminRplPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 9),
    _DErpsInstAdminRplPort_Type()
)
dErpsInstAdminRplPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstAdminRplPort.setStatus("current")


class _DErpsInstOperRplPort_Type(Integer32):
    """Custom type dErpsInstOperRplPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 0),
          ("port1", 1),
          ("none", 2))
    )


_DErpsInstOperRplPort_Type.__name__ = "Integer32"
_DErpsInstOperRplPort_Object = MibTableColumn
dErpsInstOperRplPort = _DErpsInstOperRplPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 10),
    _DErpsInstOperRplPort_Type()
)
dErpsInstOperRplPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErpsInstOperRplPort.setStatus("current")


class _DErpsInstAdminRplNodeRole_Type(Integer32):
    """Custom type dErpsInstAdminRplNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("owner", 1),
          ("neighbor", 2))
    )


_DErpsInstAdminRplNodeRole_Type.__name__ = "Integer32"
_DErpsInstAdminRplNodeRole_Object = MibTableColumn
dErpsInstAdminRplNodeRole = _DErpsInstAdminRplNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 11),
    _DErpsInstAdminRplNodeRole_Type()
)
dErpsInstAdminRplNodeRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstAdminRplNodeRole.setStatus("current")


class _DErpsInstOperRplNodeRole_Type(Integer32):
    """Custom type dErpsInstOperRplNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("owner", 1),
          ("neighbor", 2))
    )


_DErpsInstOperRplNodeRole_Type.__name__ = "Integer32"
_DErpsInstOperRplNodeRole_Object = MibTableColumn
dErpsInstOperRplNodeRole = _DErpsInstOperRplNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 12),
    _DErpsInstOperRplNodeRole_Type()
)
dErpsInstOperRplNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErpsInstOperRplNodeRole.setStatus("current")
_DErpsInstOperPort0IfIdx_Type = InterfaceIndexOrZero
_DErpsInstOperPort0IfIdx_Object = MibTableColumn
dErpsInstOperPort0IfIdx = _DErpsInstOperPort0IfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 13),
    _DErpsInstOperPort0IfIdx_Type()
)
dErpsInstOperPort0IfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErpsInstOperPort0IfIdx.setStatus("current")


class _DErpsInstOperPort0State_Type(Integer32):
    """Custom type dErpsInstOperPort0State based on Integer32"""
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
        *(("notApplicable", 1),
          ("forwarding", 2),
          ("blocked", 3),
          ("virtualChannel", 4))
    )


_DErpsInstOperPort0State_Type.__name__ = "Integer32"
_DErpsInstOperPort0State_Object = MibTableColumn
dErpsInstOperPort0State = _DErpsInstOperPort0State_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 14),
    _DErpsInstOperPort0State_Type()
)
dErpsInstOperPort0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErpsInstOperPort0State.setStatus("current")
_DErpsInstOperPort1IfIdx_Type = InterfaceIndexOrZero
_DErpsInstOperPort1IfIdx_Object = MibTableColumn
dErpsInstOperPort1IfIdx = _DErpsInstOperPort1IfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 15),
    _DErpsInstOperPort1IfIdx_Type()
)
dErpsInstOperPort1IfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErpsInstOperPort1IfIdx.setStatus("current")


class _DErpsInstOperPort1State_Type(Integer32):
    """Custom type dErpsInstOperPort1State based on Integer32"""
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
        *(("notApplicable", 1),
          ("forwarding", 2),
          ("blocked", 3),
          ("virtualChannel", 4))
    )


_DErpsInstOperPort1State_Type.__name__ = "Integer32"
_DErpsInstOperPort1State_Object = MibTableColumn
dErpsInstOperPort1State = _DErpsInstOperPort1State_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 16),
    _DErpsInstOperPort1State_Type()
)
dErpsInstOperPort1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErpsInstOperPort1State.setStatus("current")


class _DErpsInstAdminActivate_Type(TruthValue):
    """Custom type dErpsInstAdminActivate based on TruthValue"""
    defaultValue = 2


_DErpsInstAdminActivate_Type.__name__ = "TruthValue"
_DErpsInstAdminActivate_Object = MibTableColumn
dErpsInstAdminActivate = _DErpsInstAdminActivate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 17),
    _DErpsInstAdminActivate_Type()
)
dErpsInstAdminActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dErpsInstAdminActivate.setStatus("current")


class _DErpsInstInstanceState_Type(Integer32):
    """Custom type dErpsInstInstanceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deactivated", 0),
          ("nonOperational", 1),
          ("init", 2),
          ("idle", 3),
          ("protection", 4))
    )


_DErpsInstInstanceState_Type.__name__ = "Integer32"
_DErpsInstInstanceState_Object = MibTableColumn
dErpsInstInstanceState = _DErpsInstInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 5, 1, 18),
    _DErpsInstInstanceState_Type()
)
dErpsInstInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dErpsInstInstanceState.setStatus("current")
_DErpsEventInfo_ObjectIdentity = ObjectIdentity
dErpsEventInfo = _DErpsEventInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 6)
)
_DErpsEventNodeId_Type = MacAddress
_DErpsEventNodeId_Object = MibScalar
dErpsEventNodeId = _DErpsEventNodeId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 1, 6, 1),
    _DErpsEventNodeId_Type()
)
dErpsEventNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dErpsEventNodeId.setStatus("current")
_DErpsMIBConformance_ObjectIdentity = ObjectIdentity
dErpsMIBConformance = _DErpsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2)
)
_DErpsCompliances_ObjectIdentity = ObjectIdentity
dErpsCompliances = _DErpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2, 1)
)
_DErpsGroups_ObjectIdentity = ObjectIdentity
dErpsGroups = _DErpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2, 2)
)

# Managed Objects groups

dErpsInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2, 2, 1)
)
dErpsInstanceGroup.setObjects(
      *(("DLINKSW-ERPS-MIB", "dErpsEtherRingRowStatus"),
        ("DLINKSW-ERPS-MIB", "dErpsEtherRingAdminPort0IfIdx"),
        ("DLINKSW-ERPS-MIB", "dErpsEtherRingAdminPort1IfIdx"),
        ("DLINKSW-ERPS-MIB", "dErpsEtherSubRingRowStatus"),
        ("DLINKSW-ERPS-MIB", "dErpsInstRowStatus"),
        ("DLINKSW-ERPS-MIB", "dErpsInstInstanceState"),
        ("DLINKSW-ERPS-MIB", "dErpsInstDescription"),
        ("DLINKSW-ERPS-MIB", "dErpsInstMel"),
        ("DLINKSW-ERPS-MIB", "dErpsInstProfile"),
        ("DLINKSW-ERPS-MIB", "dErpsInstApsChannelVlanId"),
        ("DLINKSW-ERPS-MIB", "dErpsInstIncludeVlansFirst2K"),
        ("DLINKSW-ERPS-MIB", "dErpsInstIncludeVlansSecond2K"),
        ("DLINKSW-ERPS-MIB", "dErpsInstAdminRplPort"),
        ("DLINKSW-ERPS-MIB", "dErpsInstOperRplPort"),
        ("DLINKSW-ERPS-MIB", "dErpsInstAdminRplNodeRole"),
        ("DLINKSW-ERPS-MIB", "dErpsInstOperRplNodeRole"),
        ("DLINKSW-ERPS-MIB", "dErpsInstOperPort0IfIdx"),
        ("DLINKSW-ERPS-MIB", "dErpsInstOperPort0State"),
        ("DLINKSW-ERPS-MIB", "dErpsInstOperPort1IfIdx"),
        ("DLINKSW-ERPS-MIB", "dErpsInstOperPort1State"),
        ("DLINKSW-ERPS-MIB", "dErpsInstAdminActivate"))
)
if mibBuilder.loadTexts:
    dErpsInstanceGroup.setStatus("current")

dErpsProfileCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2, 2, 2)
)
dErpsProfileCfgGroup.setObjects(
      *(("DLINKSW-ERPS-MIB", "dErpsProfRowStatus"),
        ("DLINKSW-ERPS-MIB", "dErpsProfTcnPropagationEnabled"),
        ("DLINKSW-ERPS-MIB", "dErpsProfRevertiveEnabled"),
        ("DLINKSW-ERPS-MIB", "dErpsProfGuardTimer"),
        ("DLINKSW-ERPS-MIB", "dErpsProfHoldOffTimer"),
        ("DLINKSW-ERPS-MIB", "dErpsProfWtrTimer"))
)
if mibBuilder.loadTexts:
    dErpsProfileCfgGroup.setStatus("current")

dErpsNotifyCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2, 2, 3)
)
dErpsNotifyCfgGroup.setObjects(
      *(("DLINKSW-ERPS-MIB", "dErpsNotificationEnabled"),
        ("DLINKSW-ERPS-MIB", "dErpsEventNodeId"))
)
if mibBuilder.loadTexts:
    dErpsNotifyCfgGroup.setStatus("current")


# Notification objects

dErpsFailuredetectedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 0, 1)
)
dErpsFailuredetectedNotif.setObjects(
    ("DLINKSW-ERPS-MIB", "dErpsEventNodeId")
)
if mibBuilder.loadTexts:
    dErpsFailuredetectedNotif.setStatus(
        "current"
    )

dErpsFailureClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 0, 2)
)
dErpsFailureClearedNotif.setObjects(
    ("DLINKSW-ERPS-MIB", "dErpsEventNodeId")
)
if mibBuilder.loadTexts:
    dErpsFailureClearedNotif.setStatus(
        "current"
    )

dErpsRPLOwnerConflictNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 0, 3)
)
dErpsRPLOwnerConflictNotif.setObjects(
    ("DLINKSW-ERPS-MIB", "dErpsEventNodeId")
)
if mibBuilder.loadTexts:
    dErpsRPLOwnerConflictNotif.setStatus(
        "current"
    )


# Notifications groups

dErpsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2, 2, 4)
)
dErpsNotificationGroup.setObjects(
      *(("DLINKSW-ERPS-MIB", "dErpsFailuredetectedNotif"),
        ("DLINKSW-ERPS-MIB", "dErpsFailureClearedNotif"),
        ("DLINKSW-ERPS-MIB", "dErpsRPLOwnerConflictNotif"))
)
if mibBuilder.loadTexts:
    dErpsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dErpsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 78, 2, 1, 1)
)
dErpsCompliance.setObjects(
      *(("DLINKSW-ERPS-MIB", "dErpsInstanceGroup"),
        ("DLINKSW-ERPS-MIB", "dErpsProfileCfgGroup"),
        ("DLINKSW-ERPS-MIB", "dErpsNotifyCfgGroup"),
        ("DLINKSW-ERPS-MIB", "dErpsNotificationGroup"))
)
if mibBuilder.loadTexts:
    dErpsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-ERPS-MIB",
    **{"dlinkSwErpsMIB": dlinkSwErpsMIB,
       "dErpsMIBNotification": dErpsMIBNotification,
       "dErpsFailuredetectedNotif": dErpsFailuredetectedNotif,
       "dErpsFailureClearedNotif": dErpsFailureClearedNotif,
       "dErpsRPLOwnerConflictNotif": dErpsRPLOwnerConflictNotif,
       "dErpsMIBObjects": dErpsMIBObjects,
       "dErpsGenCtrl": dErpsGenCtrl,
       "dErpsNotificationEnabled": dErpsNotificationEnabled,
       "dErpsProfileTable": dErpsProfileTable,
       "dErpsProfileEntry": dErpsProfileEntry,
       "dErpsProfName": dErpsProfName,
       "dErpsProfRowStatus": dErpsProfRowStatus,
       "dErpsProfTcnPropagationEnabled": dErpsProfTcnPropagationEnabled,
       "dErpsProfRevertiveEnabled": dErpsProfRevertiveEnabled,
       "dErpsProfGuardTimer": dErpsProfGuardTimer,
       "dErpsProfHoldOffTimer": dErpsProfHoldOffTimer,
       "dErpsProfWtrTimer": dErpsProfWtrTimer,
       "dErpsEtherRingTable": dErpsEtherRingTable,
       "dErpsEtherRingEntry": dErpsEtherRingEntry,
       "dErpsEtherRingName": dErpsEtherRingName,
       "dErpsEtherRingRowStatus": dErpsEtherRingRowStatus,
       "dErpsEtherRingAdminPort0IfIdx": dErpsEtherRingAdminPort0IfIdx,
       "dErpsEtherRingAdminPort1IfIdx": dErpsEtherRingAdminPort1IfIdx,
       "dErpsEtherSubRingTable": dErpsEtherSubRingTable,
       "dErpsEtherSubRingEntry": dErpsEtherSubRingEntry,
       "dErpsEtherSubRingName": dErpsEtherSubRingName,
       "dErpsEtherSubRingRowStatus": dErpsEtherSubRingRowStatus,
       "dErpsInstTable": dErpsInstTable,
       "dErpsInstEntry": dErpsInstEntry,
       "dErpsInstInstanceId": dErpsInstInstanceId,
       "dErpsInstRowStatus": dErpsInstRowStatus,
       "dErpsInstDescription": dErpsInstDescription,
       "dErpsInstMel": dErpsInstMel,
       "dErpsInstProfile": dErpsInstProfile,
       "dErpsInstApsChannelVlanId": dErpsInstApsChannelVlanId,
       "dErpsInstIncludeVlansFirst2K": dErpsInstIncludeVlansFirst2K,
       "dErpsInstIncludeVlansSecond2K": dErpsInstIncludeVlansSecond2K,
       "dErpsInstAdminRplPort": dErpsInstAdminRplPort,
       "dErpsInstOperRplPort": dErpsInstOperRplPort,
       "dErpsInstAdminRplNodeRole": dErpsInstAdminRplNodeRole,
       "dErpsInstOperRplNodeRole": dErpsInstOperRplNodeRole,
       "dErpsInstOperPort0IfIdx": dErpsInstOperPort0IfIdx,
       "dErpsInstOperPort0State": dErpsInstOperPort0State,
       "dErpsInstOperPort1IfIdx": dErpsInstOperPort1IfIdx,
       "dErpsInstOperPort1State": dErpsInstOperPort1State,
       "dErpsInstAdminActivate": dErpsInstAdminActivate,
       "dErpsInstInstanceState": dErpsInstInstanceState,
       "dErpsEventInfo": dErpsEventInfo,
       "dErpsEventNodeId": dErpsEventNodeId,
       "dErpsMIBConformance": dErpsMIBConformance,
       "dErpsCompliances": dErpsCompliances,
       "dErpsCompliance": dErpsCompliance,
       "dErpsGroups": dErpsGroups,
       "dErpsInstanceGroup": dErpsInstanceGroup,
       "dErpsProfileCfgGroup": dErpsProfileCfgGroup,
       "dErpsNotifyCfgGroup": dErpsNotifyCfgGroup,
       "dErpsNotificationGroup": dErpsNotificationGroup}
)
