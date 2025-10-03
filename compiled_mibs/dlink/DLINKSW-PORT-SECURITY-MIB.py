# SNMP MIB module (DLINKSW-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-PORT-SECURITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:44 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
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

dlinkSwPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 8)
)
if mibBuilder.loadTexts:
    dlinkSwPortSecurityMIB.setRevisions(
        ("2013-07-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DPortSecNotifications_ObjectIdentity = ObjectIdentity
dPortSecNotifications = _DPortSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 0)
)
_DPortSecObjects_ObjectIdentity = ObjectIdentity
dPortSecObjects = _DPortSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1)
)


class _DPortSecGlobalNotifControl_Type(TruthValue):
    """Custom type dPortSecGlobalNotifControl based on TruthValue"""
    defaultValue = 2


_DPortSecGlobalNotifControl_Type.__name__ = "TruthValue"
_DPortSecGlobalNotifControl_Object = MibScalar
dPortSecGlobalNotifControl = _DPortSecGlobalNotifControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 1),
    _DPortSecGlobalNotifControl_Type()
)
dPortSecGlobalNotifControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecGlobalNotifControl.setStatus("current")


class _DPortSecGlobalNotifRate_Type(Unsigned32):
    """Custom type dPortSecGlobalNotifRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DPortSecGlobalNotifRate_Type.__name__ = "Unsigned32"
_DPortSecGlobalNotifRate_Object = MibScalar
dPortSecGlobalNotifRate = _DPortSecGlobalNotifRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 2),
    _DPortSecGlobalNotifRate_Type()
)
dPortSecGlobalNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecGlobalNotifRate.setStatus("current")
if mibBuilder.loadTexts:
    dPortSecGlobalNotifRate.setUnits("notifications per second")
_DPortSecNotifyInfo_ObjectIdentity = ObjectIdentity
dPortSecNotifyInfo = _DPortSecNotifyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 3)
)
_DPortSecIfViolationMacAddress_Type = MacAddress
_DPortSecIfViolationMacAddress_Object = MibScalar
dPortSecIfViolationMacAddress = _DPortSecIfViolationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 3, 1),
    _DPortSecIfViolationMacAddress_Type()
)
dPortSecIfViolationMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dPortSecIfViolationMacAddress.setStatus("current")


class _DPortSecGlobalMaximumNum_Type(Integer32):
    """Custom type dPortSecGlobalMaximumNum based on Integer32"""
    defaultValue = -1


_DPortSecGlobalMaximumNum_Type.__name__ = "Integer32"
_DPortSecGlobalMaximumNum_Object = MibScalar
dPortSecGlobalMaximumNum = _DPortSecGlobalMaximumNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 4),
    _DPortSecGlobalMaximumNum_Type()
)
dPortSecGlobalMaximumNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecGlobalMaximumNum.setStatus("current")
_DPortSecVlanTable_Object = MibTable
dPortSecVlanTable = _DPortSecVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 5)
)
if mibBuilder.loadTexts:
    dPortSecVlanTable.setStatus("current")
_DPortSecVlanEntry_Object = MibTableRow
dPortSecVlanEntry = _DPortSecVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 5, 1)
)
dPortSecVlanEntry.setIndexNames(
    (0, "DLINKSW-PORT-SECURITY-MIB", "dPortSecVlanID"),
)
if mibBuilder.loadTexts:
    dPortSecVlanEntry.setStatus("current")
_DPortSecVlanID_Type = VlanId
_DPortSecVlanID_Object = MibTableColumn
dPortSecVlanID = _DPortSecVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 5, 1, 1),
    _DPortSecVlanID_Type()
)
dPortSecVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPortSecVlanID.setStatus("current")


class _DPortSecVlanMaximumNum_Type(Integer32):
    """Custom type dPortSecVlanMaximumNum based on Integer32"""
    defaultValue = -1


_DPortSecVlanMaximumNum_Type.__name__ = "Integer32"
_DPortSecVlanMaximumNum_Object = MibTableColumn
dPortSecVlanMaximumNum = _DPortSecVlanMaximumNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 5, 1, 2),
    _DPortSecVlanMaximumNum_Type()
)
dPortSecVlanMaximumNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecVlanMaximumNum.setStatus("current")
_DPortSecVlanCurrentNum_Type = Unsigned32
_DPortSecVlanCurrentNum_Object = MibTableColumn
dPortSecVlanCurrentNum = _DPortSecVlanCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 5, 1, 3),
    _DPortSecVlanCurrentNum_Type()
)
dPortSecVlanCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPortSecVlanCurrentNum.setStatus("current")
_DPortSecIfTable_Object = MibTable
dPortSecIfTable = _DPortSecIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6)
)
if mibBuilder.loadTexts:
    dPortSecIfTable.setStatus("current")
_DPortSecIfEntry_Object = MibTableRow
dPortSecIfEntry = _DPortSecIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1)
)
dPortSecIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dPortSecIfEntry.setStatus("current")


class _DPortSecIfEnable_Type(TruthValue):
    """Custom type dPortSecIfEnable based on TruthValue"""
    defaultValue = 2


_DPortSecIfEnable_Type.__name__ = "TruthValue"
_DPortSecIfEnable_Object = MibTableColumn
dPortSecIfEnable = _DPortSecIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 1),
    _DPortSecIfEnable_Type()
)
dPortSecIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecIfEnable.setStatus("current")


class _DPortSecIfCurrentStatus_Type(Integer32):
    """Custom type dPortSecIfCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notEnabled", 1),
          ("forwarding", 2),
          ("errDisabled", 3))
    )


_DPortSecIfCurrentStatus_Type.__name__ = "Integer32"
_DPortSecIfCurrentStatus_Object = MibTableColumn
dPortSecIfCurrentStatus = _DPortSecIfCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 2),
    _DPortSecIfCurrentStatus_Type()
)
dPortSecIfCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPortSecIfCurrentStatus.setStatus("current")


class _DPortSecIfMaximumNum_Type(Unsigned32):
    """Custom type dPortSecIfMaximumNum based on Unsigned32"""
    defaultValue = 32


_DPortSecIfMaximumNum_Type.__name__ = "Unsigned32"
_DPortSecIfMaximumNum_Object = MibTableColumn
dPortSecIfMaximumNum = _DPortSecIfMaximumNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 3),
    _DPortSecIfMaximumNum_Type()
)
dPortSecIfMaximumNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecIfMaximumNum.setStatus("current")


class _DPortSecIfViolationAction_Type(Integer32):
    """Custom type dPortSecIfViolationAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protect", 1),
          ("restrict", 2),
          ("shutdown", 3))
    )


_DPortSecIfViolationAction_Type.__name__ = "Integer32"
_DPortSecIfViolationAction_Object = MibTableColumn
dPortSecIfViolationAction = _DPortSecIfViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 4),
    _DPortSecIfViolationAction_Type()
)
dPortSecIfViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecIfViolationAction.setStatus("current")


class _DPortSecIfSecureMode_Type(Integer32):
    """Custom type dPortSecIfSecureMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("deleteOnTimeout", 2))
    )


_DPortSecIfSecureMode_Type.__name__ = "Integer32"
_DPortSecIfSecureMode_Object = MibTableColumn
dPortSecIfSecureMode = _DPortSecIfSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 5),
    _DPortSecIfSecureMode_Type()
)
dPortSecIfSecureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecIfSecureMode.setStatus("current")


class _DPortSecIfAgingTime_Type(Integer32):
    """Custom type dPortSecIfAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_DPortSecIfAgingTime_Type.__name__ = "Integer32"
_DPortSecIfAgingTime_Object = MibTableColumn
dPortSecIfAgingTime = _DPortSecIfAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 6),
    _DPortSecIfAgingTime_Type()
)
dPortSecIfAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecIfAgingTime.setStatus("current")


class _DPortSecIfAgingType_Type(Integer32):
    """Custom type dPortSecIfAgingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("inactivity", 2))
    )


_DPortSecIfAgingType_Type.__name__ = "Integer32"
_DPortSecIfAgingType_Object = MibTableColumn
dPortSecIfAgingType = _DPortSecIfAgingType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 7),
    _DPortSecIfAgingType_Type()
)
dPortSecIfAgingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecIfAgingType.setStatus("current")


class _DPortSecIfClearDynamicAddr_Type(Integer32):
    """Custom type dPortSecIfClearDynamicAddr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DPortSecIfClearDynamicAddr_Type.__name__ = "Integer32"
_DPortSecIfClearDynamicAddr_Object = MibTableColumn
dPortSecIfClearDynamicAddr = _DPortSecIfClearDynamicAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 8),
    _DPortSecIfClearDynamicAddr_Type()
)
dPortSecIfClearDynamicAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dPortSecIfClearDynamicAddr.setStatus("current")
_DPortSecIfCurrentNum_Type = Unsigned32
_DPortSecIfCurrentNum_Object = MibTableColumn
dPortSecIfCurrentNum = _DPortSecIfCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 9),
    _DPortSecIfCurrentNum_Type()
)
dPortSecIfCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPortSecIfCurrentNum.setStatus("current")
_DPortSecIfViolationCount_Type = Counter64
_DPortSecIfViolationCount_Object = MibTableColumn
dPortSecIfViolationCount = _DPortSecIfViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 6, 1, 10),
    _DPortSecIfViolationCount_Type()
)
dPortSecIfViolationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPortSecIfViolationCount.setStatus("current")
_DPortSecAddrTableCurrentNum_Type = Unsigned32
_DPortSecAddrTableCurrentNum_Object = MibScalar
dPortSecAddrTableCurrentNum = _DPortSecAddrTableCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 7),
    _DPortSecAddrTableCurrentNum_Type()
)
dPortSecAddrTableCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPortSecAddrTableCurrentNum.setStatus("current")
_DPortSecAddrTable_Object = MibTable
dPortSecAddrTable = _DPortSecAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8)
)
if mibBuilder.loadTexts:
    dPortSecAddrTable.setStatus("current")
_DPortSecAddrEntry_Object = MibTableRow
dPortSecAddrEntry = _DPortSecAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8, 1)
)
dPortSecAddrEntry.setIndexNames(
    (0, "DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrIfIndex"),
    (0, "DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrVlanID"),
    (0, "DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrMacAddress"),
)
if mibBuilder.loadTexts:
    dPortSecAddrEntry.setStatus("current")
_DPortSecAddrIfIndex_Type = InterfaceIndex
_DPortSecAddrIfIndex_Object = MibTableColumn
dPortSecAddrIfIndex = _DPortSecAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8, 1, 1),
    _DPortSecAddrIfIndex_Type()
)
dPortSecAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPortSecAddrIfIndex.setStatus("current")
_DPortSecAddrVlanID_Type = VlanIdOrNone
_DPortSecAddrVlanID_Object = MibTableColumn
dPortSecAddrVlanID = _DPortSecAddrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8, 1, 2),
    _DPortSecAddrVlanID_Type()
)
dPortSecAddrVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPortSecAddrVlanID.setStatus("current")
_DPortSecAddrMacAddress_Type = MacAddress
_DPortSecAddrMacAddress_Object = MibTableColumn
dPortSecAddrMacAddress = _DPortSecAddrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8, 1, 3),
    _DPortSecAddrMacAddress_Type()
)
dPortSecAddrMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dPortSecAddrMacAddress.setStatus("current")


class _DPortSecAddrSecureMode_Type(Integer32):
    """Custom type dPortSecAddrSecureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("deleteOnTimeout", 2))
    )


_DPortSecAddrSecureMode_Type.__name__ = "Integer32"
_DPortSecAddrSecureMode_Object = MibTableColumn
dPortSecAddrSecureMode = _DPortSecAddrSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8, 1, 4),
    _DPortSecAddrSecureMode_Type()
)
dPortSecAddrSecureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPortSecAddrSecureMode.setStatus("current")
_DPortSecAddrRemainTime_Type = Integer32
_DPortSecAddrRemainTime_Object = MibTableColumn
dPortSecAddrRemainTime = _DPortSecAddrRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8, 1, 5),
    _DPortSecAddrRemainTime_Type()
)
dPortSecAddrRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dPortSecAddrRemainTime.setStatus("current")
_DPortSecAddrRowStatus_Type = RowStatus
_DPortSecAddrRowStatus_Object = MibTableColumn
dPortSecAddrRowStatus = _DPortSecAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 1, 8, 1, 99),
    _DPortSecAddrRowStatus_Type()
)
dPortSecAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dPortSecAddrRowStatus.setStatus("current")
_DPortSecConformance_ObjectIdentity = ObjectIdentity
dPortSecConformance = _DPortSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2)
)
_DPortSecMIBCompliances_ObjectIdentity = ObjectIdentity
dPortSecMIBCompliances = _DPortSecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 1)
)
_DPortSecMIBGroups_ObjectIdentity = ObjectIdentity
dPortSecMIBGroups = _DPortSecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 2)
)

# Managed Objects groups

dPortSecIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 2, 1)
)
dPortSecIfCfgGroup.setObjects(
      *(("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfEnable"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfMaximumNum"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfViolationAction"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfSecureMode"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfAgingTime"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfAgingType"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfClearDynamicAddr"))
)
if mibBuilder.loadTexts:
    dPortSecIfCfgGroup.setStatus("current")

dPortSecIfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 2, 2)
)
dPortSecIfStatusGroup.setObjects(
      *(("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfCurrentNum"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfCurrentStatus"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfViolationCount"))
)
if mibBuilder.loadTexts:
    dPortSecIfStatusGroup.setStatus("current")

dPortSecAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 2, 3)
)
dPortSecAddrGroup.setObjects(
      *(("DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrRowStatus"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrSecureMode"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrRemainTime"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrTableCurrentNum"))
)
if mibBuilder.loadTexts:
    dPortSecAddrGroup.setStatus("current")

dPortSecAddrNumCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 2, 4)
)
dPortSecAddrNumCtrlGroup.setObjects(
      *(("DLINKSW-PORT-SECURITY-MIB", "dPortSecGlobalMaximumNum"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecVlanMaximumNum"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecVlanCurrentNum"))
)
if mibBuilder.loadTexts:
    dPortSecAddrNumCtrlGroup.setStatus("current")

dPortSecNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 2, 5)
)
dPortSecNotifEnableGroup.setObjects(
      *(("DLINKSW-PORT-SECURITY-MIB", "dPortSecGlobalNotifControl"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecGlobalNotifRate"))
)
if mibBuilder.loadTexts:
    dPortSecNotifEnableGroup.setStatus("current")


# Notification objects

dPortSecMacAddrViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 0, 1)
)
dPortSecMacAddrViolation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfCurrentStatus"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfViolationMacAddress"))
)
if mibBuilder.loadTexts:
    dPortSecMacAddrViolation.setStatus(
        "current"
    )


# Notifications groups

dPortSecNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 2, 6)
)
dPortSecNotifGroup.setObjects(
    ("DLINKSW-PORT-SECURITY-MIB", "dPortSecMacAddrViolation")
)
if mibBuilder.loadTexts:
    dPortSecNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dPortSecMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 8, 2, 1, 1)
)
dPortSecMIBCompliance.setObjects(
      *(("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfCfgGroup"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecIfStatusGroup"),
        ("DLINKSW-PORT-SECURITY-MIB", "dPortSecAddrGroup"))
)
if mibBuilder.loadTexts:
    dPortSecMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-PORT-SECURITY-MIB",
    **{"dlinkSwPortSecurityMIB": dlinkSwPortSecurityMIB,
       "dPortSecNotifications": dPortSecNotifications,
       "dPortSecMacAddrViolation": dPortSecMacAddrViolation,
       "dPortSecObjects": dPortSecObjects,
       "dPortSecGlobalNotifControl": dPortSecGlobalNotifControl,
       "dPortSecGlobalNotifRate": dPortSecGlobalNotifRate,
       "dPortSecNotifyInfo": dPortSecNotifyInfo,
       "dPortSecIfViolationMacAddress": dPortSecIfViolationMacAddress,
       "dPortSecGlobalMaximumNum": dPortSecGlobalMaximumNum,
       "dPortSecVlanTable": dPortSecVlanTable,
       "dPortSecVlanEntry": dPortSecVlanEntry,
       "dPortSecVlanID": dPortSecVlanID,
       "dPortSecVlanMaximumNum": dPortSecVlanMaximumNum,
       "dPortSecVlanCurrentNum": dPortSecVlanCurrentNum,
       "dPortSecIfTable": dPortSecIfTable,
       "dPortSecIfEntry": dPortSecIfEntry,
       "dPortSecIfEnable": dPortSecIfEnable,
       "dPortSecIfCurrentStatus": dPortSecIfCurrentStatus,
       "dPortSecIfMaximumNum": dPortSecIfMaximumNum,
       "dPortSecIfViolationAction": dPortSecIfViolationAction,
       "dPortSecIfSecureMode": dPortSecIfSecureMode,
       "dPortSecIfAgingTime": dPortSecIfAgingTime,
       "dPortSecIfAgingType": dPortSecIfAgingType,
       "dPortSecIfClearDynamicAddr": dPortSecIfClearDynamicAddr,
       "dPortSecIfCurrentNum": dPortSecIfCurrentNum,
       "dPortSecIfViolationCount": dPortSecIfViolationCount,
       "dPortSecAddrTableCurrentNum": dPortSecAddrTableCurrentNum,
       "dPortSecAddrTable": dPortSecAddrTable,
       "dPortSecAddrEntry": dPortSecAddrEntry,
       "dPortSecAddrIfIndex": dPortSecAddrIfIndex,
       "dPortSecAddrVlanID": dPortSecAddrVlanID,
       "dPortSecAddrMacAddress": dPortSecAddrMacAddress,
       "dPortSecAddrSecureMode": dPortSecAddrSecureMode,
       "dPortSecAddrRemainTime": dPortSecAddrRemainTime,
       "dPortSecAddrRowStatus": dPortSecAddrRowStatus,
       "dPortSecConformance": dPortSecConformance,
       "dPortSecMIBCompliances": dPortSecMIBCompliances,
       "dPortSecMIBCompliance": dPortSecMIBCompliance,
       "dPortSecMIBGroups": dPortSecMIBGroups,
       "dPortSecIfCfgGroup": dPortSecIfCfgGroup,
       "dPortSecIfStatusGroup": dPortSecIfStatusGroup,
       "dPortSecAddrGroup": dPortSecAddrGroup,
       "dPortSecAddrNumCtrlGroup": dPortSecAddrNumCtrlGroup,
       "dPortSecNotifEnableGroup": dPortSecNotifEnableGroup,
       "dPortSecNotifGroup": dPortSecNotifGroup}
)
