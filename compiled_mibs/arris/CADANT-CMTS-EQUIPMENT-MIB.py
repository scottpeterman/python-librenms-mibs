# SNMP MIB module (CADANT-CMTS-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\CADANT-CMTS-EQUIPMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:14 2025
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

(cadEquipment,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadEquipment")

(AdminState,
 CardId,
 CardSubType,
 CardType,
 DiskVolumeUsageLevel,
 DuplexStatus,
 EqActionType,
 FirmwareSource,
 FlowControlMode,
 PicType,
 PortDetectedMode,
 PortId,
 PortMode,
 PortType,
 PrimaryState,
 SecondaryState,
 ShelfId,
 UnknownState) = mibBuilder.importSymbols(
    "CADANT-TC",
    "AdminState",
    "CardId",
    "CardSubType",
    "CardType",
    "DiskVolumeUsageLevel",
    "DuplexStatus",
    "EqActionType",
    "FirmwareSource",
    "FlowControlMode",
    "PicType",
    "PortDetectedMode",
    "PortId",
    "PortMode",
    "PortType",
    "PrimaryState",
    "SecondaryState",
    "ShelfId",
    "UnknownState")

(TenthdBmV,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadEquipmentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cadEquipmentMib.setRevisions(
        ("2009-03-03 00:00",
         "2009-01-05 00:00",
         "2008-10-14 00:00",
         "2008-10-01 00:00",
         "2008-07-03 00:00",
         "2008-06-18 00:00",
         "2008-04-28 00:00",
         "2008-04-02 00:00",
         "2008-02-25 00:00",
         "2007-11-05 00:00",
         "2007-01-10 00:00",
         "2006-11-13 00:00",
         "2006-09-12 00:00",
         "2006-08-23 00:00",
         "2006-02-14 00:00",
         "2005-08-30 00:00",
         "2005-04-06 00:00",
         "2005-02-04 00:00",
         "2005-01-24 00:00",
         "2004-12-01 00:00",
         "2004-11-18 00:00",
         "2004-11-11 00:00",
         "2004-09-07 00:00",
         "2004-07-23 00:00",
         "2004-03-22 00:00",
         "2004-03-18 00:00",
         "2004-02-04 00:00",
         "2003-12-18 00:00",
         "2003-03-31 00:00",
         "2003-03-17 00:00",
         "2003-03-05 00:00",
         "2003-03-02 00:00",
         "2003-01-29 00:00",
         "2002-12-14 00:00",
         "2002-11-07 00:00",
         "2002-09-25 00:00",
         "2002-09-01 00:00",
         "2002-05-01 00:00",
         "2001-12-28 16:30",
         "2001-12-21 16:30",
         "2001-10-03 00:00",
         "2001-07-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TestId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TestType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("test", 1),
          ("diagnostic", 2),
          ("unknown", 3))
    )



class TestCommand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("stop", 2),
          ("disable", 3),
          ("enable", 4),
          ("runNow", 5))
    )



class TestScheduleCommand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("disable", 2),
          ("enable", 3))
    )



class TestSchedule(TextualConvention, Integer32):
    status = "current"


class TestResult(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notRun", 1),
          ("inProgress", 2),
          ("pass", 3),
          ("fail", 4),
          ("inconclusive", 5),
          ("timeOut", 6),
          ("abort", 7))
    )



class TestTransactionId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_EquipmentTraps_ObjectIdentity = ObjectIdentity
equipmentTraps = _EquipmentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0)
)
_SystemGeneral_ObjectIdentity = ObjectIdentity
systemGeneral = _SystemGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1)
)
_SystemClock_Type = DateAndTime
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 1),
    _SystemClock_Type()
)
systemClock.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemClock.setStatus("current")
_TrapCounter_Type = Counter32
_TrapCounter_Object = MibScalar
trapCounter = _TrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 2),
    _TrapCounter_Type()
)
trapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCounter.setStatus("current")


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("indeterminate", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6),
          ("informational", 7))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 3),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_SystemKey_Type = DisplayString
_SystemKey_Object = MibScalar
systemKey = _SystemKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 4),
    _SystemKey_Type()
)
systemKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemKey.setStatus("current")


class _CardNumber_Type(CardId):
    """Custom type cardNumber based on CardId"""
    defaultValue = 99


_CardNumber_Type.__name__ = "CardId"
_CardNumber_Object = MibScalar
cardNumber = _CardNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 98),
    _CardNumber_Type()
)
cardNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cardNumber.setStatus("current")


class _PortNumber_Type(PortId):
    """Custom type portNumber based on PortId"""
    defaultValue = 99


_PortNumber_Type.__name__ = "PortId"
_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 99),
    _PortNumber_Type()
)
portNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")


class _DiskDriveNumber_Type(Integer32):
    """Custom type diskDriveNumber based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DiskDriveNumber_Type.__name__ = "Integer32"
_DiskDriveNumber_Object = MibScalar
diskDriveNumber = _DiskDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 100),
    _DiskDriveNumber_Type()
)
diskDriveNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    diskDriveNumber.setStatus("current")


class _DiskVolumeNumber_Type(Integer32):
    """Custom type diskVolumeNumber based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DiskVolumeNumber_Type.__name__ = "Integer32"
_DiskVolumeNumber_Object = MibScalar
diskVolumeNumber = _DiskVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 101),
    _DiskVolumeNumber_Type()
)
diskVolumeNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    diskVolumeNumber.setStatus("current")
_ShelfObjects_ObjectIdentity = ObjectIdentity
shelfObjects = _ShelfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 2)
)


class _ShelfNumber_Type(ShelfId):
    """Custom type shelfNumber based on ShelfId"""
    defaultValue = 1


_ShelfNumber_Type.__name__ = "ShelfId"
_ShelfNumber_Object = MibScalar
shelfNumber = _ShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 2, 1),
    _ShelfNumber_Type()
)
shelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfNumber.setStatus("deprecated")


class _ShelfName_Type(DisplayString):
    """Custom type shelfName based on DisplayString"""
    defaultValue = OctetString("Cadant C4 CMTS")


_ShelfName_Type.__name__ = "DisplayString"
_ShelfName_Object = MibScalar
shelfName = _ShelfName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 2, 2),
    _ShelfName_Type()
)
shelfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfName.setStatus("current")
_ShelfSwVersion_Type = DisplayString
_ShelfSwVersion_Object = MibScalar
shelfSwVersion = _ShelfSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 2, 3),
    _ShelfSwVersion_Type()
)
shelfSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSwVersion.setStatus("current")
_EquipmentState_ObjectIdentity = ObjectIdentity
equipmentState = _EquipmentState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 3)
)
_CardLastChangeTime_Type = TimeStamp
_CardLastChangeTime_Object = MibScalar
cardLastChangeTime = _CardLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 3, 2),
    _CardLastChangeTime_Type()
)
cardLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastChangeTime.setStatus("current")
_PortLastChangeTime_Type = TimeStamp
_PortLastChangeTime_Object = MibScalar
portLastChangeTime = _PortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 3, 3),
    _PortLastChangeTime_Type()
)
portLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastChangeTime.setStatus("current")
_EquipmentTbl_ObjectIdentity = ObjectIdentity
equipmentTbl = _EquipmentTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4)
)
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("current")
_CardEntry_Object = MibTableRow
cardEntry = _CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1)
)
cardEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardShelfId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardId"),
)
if mibBuilder.loadTexts:
    cardEntry.setStatus("current")
_CardShelfId_Type = ShelfId
_CardShelfId_Object = MibTableColumn
cardShelfId = _CardShelfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 1),
    _CardShelfId_Type()
)
cardShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardShelfId.setStatus("obsolete")
_CardId_Type = CardId
_CardId_Object = MibTableColumn
cardId = _CardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 2),
    _CardId_Type()
)
cardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cardId.setStatus("current")


class _CardName_Type(DisplayString):
    """Custom type cardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardName_Type.__name__ = "DisplayString"
_CardName_Object = MibTableColumn
cardName = _CardName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 3),
    _CardName_Type()
)
cardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardName.setStatus("current")
_CardType_Type = CardType
_CardType_Object = MibTableColumn
cardType = _CardType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 4),
    _CardType_Type()
)
cardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardType.setStatus("current")
_CardSubType_Type = CardSubType
_CardSubType_Object = MibTableColumn
cardSubType = _CardSubType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 5),
    _CardSubType_Type()
)
cardSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSubType.setStatus("current")


class _CardSerialNum_Type(DisplayString):
    """Custom type cardSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardSerialNum_Type.__name__ = "DisplayString"
_CardSerialNum_Object = MibTableColumn
cardSerialNum = _CardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 6),
    _CardSerialNum_Type()
)
cardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSerialNum.setStatus("current")


class _CardFwVersion_Type(DisplayString):
    """Custom type cardFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CardFwVersion_Type.__name__ = "DisplayString"
_CardFwVersion_Object = MibTableColumn
cardFwVersion = _CardFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 7),
    _CardFwVersion_Type()
)
cardFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFwVersion.setStatus("current")


class _CardHwVersion_Type(DisplayString):
    """Custom type cardHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CardHwVersion_Type.__name__ = "DisplayString"
_CardHwVersion_Object = MibTableColumn
cardHwVersion = _CardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 8),
    _CardHwVersion_Type()
)
cardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHwVersion.setStatus("current")


class _CardSwVersion_Type(DisplayString):
    """Custom type cardSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardSwVersion_Type.__name__ = "DisplayString"
_CardSwVersion_Object = MibTableColumn
cardSwVersion = _CardSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 9),
    _CardSwVersion_Type()
)
cardSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwVersion.setStatus("current")
_CardAdminState_Type = AdminState
_CardAdminState_Object = MibTableColumn
cardAdminState = _CardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 12),
    _CardAdminState_Type()
)
cardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAdminState.setStatus("current")
_CardPrState_Type = PrimaryState
_CardPrState_Object = MibTableColumn
cardPrState = _CardPrState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 13),
    _CardPrState_Type()
)
cardPrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPrState.setStatus("current")
_CardSecState_Type = SecondaryState
_CardSecState_Object = MibTableColumn
cardSecState = _CardSecState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 14),
    _CardSecState_Type()
)
cardSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSecState.setStatus("current")
_CardDplxStatus_Type = DuplexStatus
_CardDplxStatus_Object = MibTableColumn
cardDplxStatus = _CardDplxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 15),
    _CardDplxStatus_Type()
)
cardDplxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDplxStatus.setStatus("current")
_CardAction_Type = EqActionType
_CardAction_Object = MibTableColumn
cardAction = _CardAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 17),
    _CardAction_Type()
)
cardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardAction.setStatus("current")


class _CardTrapInh_Type(Bits):
    """Custom type cardTrapInh based on Bits"""
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1),
          ("duplex", 2),
          ("detected", 3),
          ("tempoutofrange", 4),
          ("tempnoreport", 5),
          ("tempoverheat", 6))
    )

_CardTrapInh_Type.__name__ = "Bits"
_CardTrapInh_Object = MibTableColumn
cardTrapInh = _CardTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 18),
    _CardTrapInh_Type()
)
cardTrapInh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTrapInh.setStatus("current")


class _CardNumPorts_Type(Integer32):
    """Custom type cardNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CardNumPorts_Type.__name__ = "Integer32"
_CardNumPorts_Object = MibTableColumn
cardNumPorts = _CardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 19),
    _CardNumPorts_Type()
)
cardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNumPorts.setStatus("current")
_CardDetected_Type = CardType
_CardDetected_Object = MibTableColumn
cardDetected = _CardDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 20),
    _CardDetected_Type()
)
cardDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDetected.setStatus("current")
_CardSubDetected_Type = CardSubType
_CardSubDetected_Object = MibTableColumn
cardSubDetected = _CardSubDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 21),
    _CardSubDetected_Type()
)
cardSubDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSubDetected.setStatus("current")


class _CardFwUpdateStatus_Type(TruthValue):
    """Custom type cardFwUpdateStatus based on TruthValue"""
    defaultValue = 2


_CardFwUpdateStatus_Type.__name__ = "TruthValue"
_CardFwUpdateStatus_Object = MibTableColumn
cardFwUpdateStatus = _CardFwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 23),
    _CardFwUpdateStatus_Type()
)
cardFwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFwUpdateStatus.setStatus("current")
_CardSpareGroupId_Type = CardId
_CardSpareGroupId_Object = MibTableColumn
cardSpareGroupId = _CardSpareGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 24),
    _CardSpareGroupId_Type()
)
cardSpareGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSpareGroupId.setStatus("current")


class _CardSpareGroupMode_Type(Integer32):
    """Custom type cardSpareGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2),
          ("invalid", 99))
    )


_CardSpareGroupMode_Type.__name__ = "Integer32"
_CardSpareGroupMode_Object = MibTableColumn
cardSpareGroupMode = _CardSpareGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 25),
    _CardSpareGroupMode_Type()
)
cardSpareGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardSpareGroupMode.setStatus("current")
_CardUpTime_Type = TimeTicks
_CardUpTime_Object = MibTableColumn
cardUpTime = _CardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 26),
    _CardUpTime_Type()
)
cardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardUpTime.setStatus("current")


class _CardTemperature_Type(Integer32):
    """Custom type cardTemperature based on Integer32"""
    defaultValue = 999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 120),
        ValueRangeConstraint(999, 999),
    )


_CardTemperature_Type.__name__ = "Integer32"
_CardTemperature_Object = MibTableColumn
cardTemperature = _CardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 29),
    _CardTemperature_Type()
)
cardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cardTemperature.setUnits("degrees Centigrade")


class _CardCpuType_Type(DisplayString):
    """Custom type cardCpuType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CardCpuType_Type.__name__ = "DisplayString"
_CardCpuType_Object = MibTableColumn
cardCpuType = _CardCpuType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 30),
    _CardCpuType_Type()
)
cardCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCpuType.setStatus("current")
_CardCpuSpeed_Type = Unsigned32
_CardCpuSpeed_Object = MibTableColumn
cardCpuSpeed = _CardCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 31),
    _CardCpuSpeed_Type()
)
cardCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCpuSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cardCpuSpeed.setUnits("MHz")
_CardBusSpeed_Type = Unsigned32
_CardBusSpeed_Object = MibTableColumn
cardBusSpeed = _CardBusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 32),
    _CardBusSpeed_Type()
)
cardBusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBusSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cardBusSpeed.setUnits("hertz")
_CardRamSize_Type = Unsigned32
_CardRamSize_Object = MibTableColumn
cardRamSize = _CardRamSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 33),
    _CardRamSize_Type()
)
cardRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRamSize.setStatus("current")
if mibBuilder.loadTexts:
    cardRamSize.setUnits("bytes")
_CardFlashSize_Type = Unsigned32
_CardFlashSize_Object = MibTableColumn
cardFlashSize = _CardFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 34),
    _CardFlashSize_Type()
)
cardFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    cardFlashSize.setUnits("bytes")


class _CardCPLDVersion_Type(DisplayString):
    """Custom type cardCPLDVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardCPLDVersion_Type.__name__ = "DisplayString"
_CardCPLDVersion_Object = MibTableColumn
cardCPLDVersion = _CardCPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 35),
    _CardCPLDVersion_Type()
)
cardCPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCPLDVersion.setStatus("current")


class _CardFpgaSource_Type(FirmwareSource):
    """Custom type cardFpgaSource based on FirmwareSource"""
    defaultValue = 1


_CardFpgaSource_Type.__name__ = "FirmwareSource"
_CardFpgaSource_Object = MibTableColumn
cardFpgaSource = _CardFpgaSource_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 36),
    _CardFpgaSource_Type()
)
cardFpgaSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardFpgaSource.setStatus("current")


class _CardBootVersion_Type(DisplayString):
    """Custom type cardBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_CardBootVersion_Type.__name__ = "DisplayString"
_CardBootVersion_Object = MibTableColumn
cardBootVersion = _CardBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 37),
    _CardBootVersion_Type()
)
cardBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardBootVersion.setStatus("current")


class _CardLastBootVersion_Type(DisplayString):
    """Custom type cardLastBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CardLastBootVersion_Type.__name__ = "DisplayString"
_CardLastBootVersion_Object = MibTableColumn
cardLastBootVersion = _CardLastBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 38),
    _CardLastBootVersion_Type()
)
cardLastBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastBootVersion.setStatus("current")


class _CardLastBootSource_Type(FirmwareSource):
    """Custom type cardLastBootSource based on FirmwareSource"""
    defaultValue = 3


_CardLastBootSource_Type.__name__ = "FirmwareSource"
_CardLastBootSource_Object = MibTableColumn
cardLastBootSource = _CardLastBootSource_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 39),
    _CardLastBootSource_Type()
)
cardLastBootSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastBootSource.setStatus("current")


class _CardPicDetected_Type(PicType):
    """Custom type cardPicDetected based on PicType"""
    defaultValue = 99


_CardPicDetected_Type.__name__ = "PicType"
_CardPicDetected_Object = MibTableColumn
cardPicDetected = _CardPicDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 40),
    _CardPicDetected_Type()
)
cardPicDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPicDetected.setStatus("current")


class _CardPicSerialNum_Type(DisplayString):
    """Custom type cardPicSerialNum based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardPicSerialNum_Type.__name__ = "DisplayString"
_CardPicSerialNum_Object = MibTableColumn
cardPicSerialNum = _CardPicSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 41),
    _CardPicSerialNum_Type()
)
cardPicSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPicSerialNum.setStatus("current")


class _CardPicHwVersion_Type(DisplayString):
    """Custom type cardPicHwVersion based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CardPicHwVersion_Type.__name__ = "DisplayString"
_CardPicHwVersion_Object = MibTableColumn
cardPicHwVersion = _CardPicHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 42),
    _CardPicHwVersion_Type()
)
cardPicHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardPicHwVersion.setStatus("current")


class _CardLastResetReason_Type(DisplayString):
    """Custom type cardLastResetReason based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CardLastResetReason_Type.__name__ = "DisplayString"
_CardLastResetReason_Object = MibTableColumn
cardLastResetReason = _CardLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 43),
    _CardLastResetReason_Type()
)
cardLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastResetReason.setStatus("current")


class _CardTemperatureHighWarn_Type(Integer32):
    """Custom type cardTemperatureHighWarn based on Integer32"""
    defaultValue = 70


_CardTemperatureHighWarn_Type.__name__ = "Integer32"
_CardTemperatureHighWarn_Object = MibTableColumn
cardTemperatureHighWarn = _CardTemperatureHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 44),
    _CardTemperatureHighWarn_Type()
)
cardTemperatureHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTemperatureHighWarn.setStatus("current")
if mibBuilder.loadTexts:
    cardTemperatureHighWarn.setUnits("degrees Centigrade")


class _CardTemperatureHighError_Type(Integer32):
    """Custom type cardTemperatureHighError based on Integer32"""
    defaultValue = 90


_CardTemperatureHighError_Type.__name__ = "Integer32"
_CardTemperatureHighError_Object = MibTableColumn
cardTemperatureHighError = _CardTemperatureHighError_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 45),
    _CardTemperatureHighError_Type()
)
cardTemperatureHighError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTemperatureHighError.setStatus("current")
if mibBuilder.loadTexts:
    cardTemperatureHighError.setUnits("degrees Centigrade")


class _CardCarrierSerialNum_Type(DisplayString):
    """Custom type cardCarrierSerialNum based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CardCarrierSerialNum_Type.__name__ = "DisplayString"
_CardCarrierSerialNum_Object = MibTableColumn
cardCarrierSerialNum = _CardCarrierSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 46),
    _CardCarrierSerialNum_Type()
)
cardCarrierSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCarrierSerialNum.setStatus("current")


class _CardCarrierFwVersion_Type(DisplayString):
    """Custom type cardCarrierFwVersion based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CardCarrierFwVersion_Type.__name__ = "DisplayString"
_CardCarrierFwVersion_Object = MibTableColumn
cardCarrierFwVersion = _CardCarrierFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 47),
    _CardCarrierFwVersion_Type()
)
cardCarrierFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCarrierFwVersion.setStatus("current")


class _CardCarrierHwVersion_Type(DisplayString):
    """Custom type cardCarrierHwVersion based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CardCarrierHwVersion_Type.__name__ = "DisplayString"
_CardCarrierHwVersion_Object = MibTableColumn
cardCarrierHwVersion = _CardCarrierHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 2, 1, 48),
    _CardCarrierHwVersion_Type()
)
cardCarrierHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardCarrierHwVersion.setStatus("current")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1)
)
portEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "portShelfId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "portCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortShelfId_Type = ShelfId
_PortShelfId_Object = MibTableColumn
portShelfId = _PortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 1),
    _PortShelfId_Type()
)
portShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portShelfId.setStatus("deprecated")
_PortCardId_Type = CardId
_PortCardId_Object = MibTableColumn
portCardId = _PortCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 2),
    _PortCardId_Type()
)
portCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portCardId.setStatus("current")
_PortId_Type = PortId
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 3),
    _PortId_Type()
)
portId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portId.setStatus("current")
_PortType_Type = PortType
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 4),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")
_PortAdminState_Type = AdminState
_PortAdminState_Object = MibTableColumn
portAdminState = _PortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 6),
    _PortAdminState_Type()
)
portAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminState.setStatus("current")
_PortPrState_Type = PrimaryState
_PortPrState_Object = MibTableColumn
portPrState = _PortPrState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 7),
    _PortPrState_Type()
)
portPrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPrState.setStatus("current")
_PortSecState_Type = SecondaryState
_PortSecState_Object = MibTableColumn
portSecState = _PortSecState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 8),
    _PortSecState_Type()
)
portSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecState.setStatus("current")
_PortDplxStatus_Type = DuplexStatus
_PortDplxStatus_Object = MibTableColumn
portDplxStatus = _PortDplxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 9),
    _PortDplxStatus_Type()
)
portDplxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDplxStatus.setStatus("current")
_PortAction_Type = EqActionType
_PortAction_Object = MibTableColumn
portAction = _PortAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 11),
    _PortAction_Type()
)
portAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAction.setStatus("current")


class _PortTrapInh_Type(Bits):
    """Custom type portTrapInh based on Bits"""
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1),
          ("duplex", 2),
          ("linkUpLinkDown", 3))
    )

_PortTrapInh_Type.__name__ = "Bits"
_PortTrapInh_Object = MibTableColumn
portTrapInh = _PortTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 12),
    _PortTrapInh_Type()
)
portTrapInh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrapInh.setStatus("current")


class _PortNumChans_Type(Integer32):
    """Custom type portNumChans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_PortNumChans_Type.__name__ = "Integer32"
_PortNumChans_Object = MibTableColumn
portNumChans = _PortNumChans_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 13),
    _PortNumChans_Type()
)
portNumChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumChans.setStatus("current")
_PortDocsIfIndex_Type = InterfaceIndexOrZero
_PortDocsIfIndex_Object = MibTableColumn
portDocsIfIndex = _PortDocsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 14),
    _PortDocsIfIndex_Type()
)
portDocsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDocsIfIndex.setStatus("current")
_PortMacAddress_Type = MacAddress
_PortMacAddress_Object = MibTableColumn
portMacAddress = _PortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 15),
    _PortMacAddress_Type()
)
portMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacAddress.setStatus("current")


class _PortMode_Type(PortMode):
    """Custom type portMode based on PortMode"""
    defaultValue = 1


_PortMode_Type.__name__ = "PortMode"
_PortMode_Object = MibTableColumn
portMode = _PortMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 16),
    _PortMode_Type()
)
portMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMode.setStatus("current")
_PortDetectedMode_Type = PortDetectedMode
_PortDetectedMode_Object = MibTableColumn
portDetectedMode = _PortDetectedMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 17),
    _PortDetectedMode_Type()
)
portDetectedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDetectedMode.setStatus("current")


class _PortBgpId_Type(Integer32):
    """Custom type portBgpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_PortBgpId_Type.__name__ = "Integer32"
_PortBgpId_Object = MibTableColumn
portBgpId = _PortBgpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 19),
    _PortBgpId_Type()
)
portBgpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBgpId.setStatus("current")


class _PortConnectorId_Type(PortId):
    """Custom type portConnectorId based on PortId"""
    defaultValue = 99


_PortConnectorId_Type.__name__ = "PortId"
_PortConnectorId_Object = MibTableColumn
portConnectorId = _PortConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 20),
    _PortConnectorId_Type()
)
portConnectorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConnectorId.setStatus("current")
_PortCardSubType_Type = CardSubType
_PortCardSubType_Object = MibTableColumn
portCardSubType = _PortCardSubType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 21),
    _PortCardSubType_Type()
)
portCardSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardSubType.setStatus("current")


class _PortDescription_Type(DisplayString):
    """Custom type portDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortDescription_Type.__name__ = "DisplayString"
_PortDescription_Object = MibTableColumn
portDescription = _PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 27),
    _PortDescription_Type()
)
portDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDescription.setStatus("current")


class _PortCurrDsPower_Type(TenthdBmV):
    """Custom type portCurrDsPower based on TenthdBmV"""
    defaultValue = 0


_PortCurrDsPower_Type.__name__ = "TenthdBmV"
_PortCurrDsPower_Object = MibTableColumn
portCurrDsPower = _PortCurrDsPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 28),
    _PortCurrDsPower_Type()
)
portCurrDsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCurrDsPower.setStatus("current")


class _PortMinDsPower_Type(TenthdBmV):
    """Custom type portMinDsPower based on TenthdBmV"""
    defaultValue = 0


_PortMinDsPower_Type.__name__ = "TenthdBmV"
_PortMinDsPower_Object = MibTableColumn
portMinDsPower = _PortMinDsPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 29),
    _PortMinDsPower_Type()
)
portMinDsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMinDsPower.setStatus("current")


class _PortMaxDsPower_Type(TenthdBmV):
    """Custom type portMaxDsPower based on TenthdBmV"""
    defaultValue = 0


_PortMaxDsPower_Type.__name__ = "TenthdBmV"
_PortMaxDsPower_Object = MibTableColumn
portMaxDsPower = _PortMaxDsPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 30),
    _PortMaxDsPower_Type()
)
portMaxDsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaxDsPower.setStatus("current")


class _PortTxFlowControlMode_Type(FlowControlMode):
    """Custom type portTxFlowControlMode based on FlowControlMode"""
    defaultValue = 3


_PortTxFlowControlMode_Type.__name__ = "FlowControlMode"
_PortTxFlowControlMode_Object = MibTableColumn
portTxFlowControlMode = _PortTxFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 31),
    _PortTxFlowControlMode_Type()
)
portTxFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTxFlowControlMode.setStatus("current")


class _PortRxFlowControlMode_Type(FlowControlMode):
    """Custom type portRxFlowControlMode based on FlowControlMode"""
    defaultValue = 3


_PortRxFlowControlMode_Type.__name__ = "FlowControlMode"
_PortRxFlowControlMode_Object = MibTableColumn
portRxFlowControlMode = _PortRxFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 32),
    _PortRxFlowControlMode_Type()
)
portRxFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRxFlowControlMode.setStatus("current")


class _PortTxFlowControlDetected_Type(FlowControlMode):
    """Custom type portTxFlowControlDetected based on FlowControlMode"""
    defaultValue = 98


_PortTxFlowControlDetected_Type.__name__ = "FlowControlMode"
_PortTxFlowControlDetected_Object = MibTableColumn
portTxFlowControlDetected = _PortTxFlowControlDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 33),
    _PortTxFlowControlDetected_Type()
)
portTxFlowControlDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTxFlowControlDetected.setStatus("current")


class _PortRxFlowControlDetected_Type(FlowControlMode):
    """Custom type portRxFlowControlDetected based on FlowControlMode"""
    defaultValue = 98


_PortRxFlowControlDetected_Type.__name__ = "FlowControlMode"
_PortRxFlowControlDetected_Object = MibTableColumn
portRxFlowControlDetected = _PortRxFlowControlDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 34),
    _PortRxFlowControlDetected_Type()
)
portRxFlowControlDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRxFlowControlDetected.setStatus("current")


class _PortMacIfIndex_Type(InterfaceIndexOrZero):
    """Custom type portMacIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PortMacIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_PortMacIfIndex_Object = MibTableColumn
portMacIfIndex = _PortMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 3, 1, 35),
    _PortMacIfIndex_Type()
)
portMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacIfIndex.setStatus("current")
_DiskVolumeTable_Object = MibTable
diskVolumeTable = _DiskVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4)
)
if mibBuilder.loadTexts:
    diskVolumeTable.setStatus("current")
_DiskVolumeEntry_Object = MibTableRow
diskVolumeEntry = _DiskVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1)
)
diskVolumeEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeShelfId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeDriveId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeId"),
)
if mibBuilder.loadTexts:
    diskVolumeEntry.setStatus("current")
_DiskVolumeShelfId_Type = ShelfId
_DiskVolumeShelfId_Object = MibTableColumn
diskVolumeShelfId = _DiskVolumeShelfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 1),
    _DiskVolumeShelfId_Type()
)
diskVolumeShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolumeShelfId.setStatus("deprecated")
_DiskVolumeCardId_Type = CardId
_DiskVolumeCardId_Object = MibTableColumn
diskVolumeCardId = _DiskVolumeCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 2),
    _DiskVolumeCardId_Type()
)
diskVolumeCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskVolumeCardId.setStatus("current")


class _DiskVolumeDriveId_Type(Integer32):
    """Custom type diskVolumeDriveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_DiskVolumeDriveId_Type.__name__ = "Integer32"
_DiskVolumeDriveId_Object = MibTableColumn
diskVolumeDriveId = _DiskVolumeDriveId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 3),
    _DiskVolumeDriveId_Type()
)
diskVolumeDriveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskVolumeDriveId.setStatus("current")


class _DiskVolumeId_Type(Integer32):
    """Custom type diskVolumeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_DiskVolumeId_Type.__name__ = "Integer32"
_DiskVolumeId_Object = MibTableColumn
diskVolumeId = _DiskVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 4),
    _DiskVolumeId_Type()
)
diskVolumeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskVolumeId.setStatus("current")
_DiskVolumeName_Type = DisplayString
_DiskVolumeName_Object = MibTableColumn
diskVolumeName = _DiskVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 5),
    _DiskVolumeName_Type()
)
diskVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolumeName.setStatus("current")
_DiskVolumeSize_Type = Integer32
_DiskVolumeSize_Object = MibTableColumn
diskVolumeSize = _DiskVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 6),
    _DiskVolumeSize_Type()
)
diskVolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolumeSize.setStatus("current")
if mibBuilder.loadTexts:
    diskVolumeSize.setUnits("bytes")
_DiskVolumeUsageLevel_Type = DiskVolumeUsageLevel
_DiskVolumeUsageLevel_Object = MibTableColumn
diskVolumeUsageLevel = _DiskVolumeUsageLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 7),
    _DiskVolumeUsageLevel_Type()
)
diskVolumeUsageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolumeUsageLevel.setStatus("current")


class _DiskVolumeUsagePercentage_Type(Integer32):
    """Custom type diskVolumeUsagePercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskVolumeUsagePercentage_Type.__name__ = "Integer32"
_DiskVolumeUsagePercentage_Object = MibTableColumn
diskVolumeUsagePercentage = _DiskVolumeUsagePercentage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 8),
    _DiskVolumeUsagePercentage_Type()
)
diskVolumeUsagePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolumeUsagePercentage.setStatus("current")
if mibBuilder.loadTexts:
    diskVolumeUsagePercentage.setUnits("percent")


class _DiskVolumeUsageCriticalThreshold_Type(Integer32):
    """Custom type diskVolumeUsageCriticalThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskVolumeUsageCriticalThreshold_Type.__name__ = "Integer32"
_DiskVolumeUsageCriticalThreshold_Object = MibTableColumn
diskVolumeUsageCriticalThreshold = _DiskVolumeUsageCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 9),
    _DiskVolumeUsageCriticalThreshold_Type()
)
diskVolumeUsageCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskVolumeUsageCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diskVolumeUsageCriticalThreshold.setUnits("percent")


class _DiskVolumeUsageMajorThreshold_Type(Integer32):
    """Custom type diskVolumeUsageMajorThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskVolumeUsageMajorThreshold_Type.__name__ = "Integer32"
_DiskVolumeUsageMajorThreshold_Object = MibTableColumn
diskVolumeUsageMajorThreshold = _DiskVolumeUsageMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 10),
    _DiskVolumeUsageMajorThreshold_Type()
)
diskVolumeUsageMajorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskVolumeUsageMajorThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diskVolumeUsageMajorThreshold.setUnits("percent")


class _DiskVolumeUsageMinorThreshold_Type(Integer32):
    """Custom type diskVolumeUsageMinorThreshold based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskVolumeUsageMinorThreshold_Type.__name__ = "Integer32"
_DiskVolumeUsageMinorThreshold_Object = MibTableColumn
diskVolumeUsageMinorThreshold = _DiskVolumeUsageMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 11),
    _DiskVolumeUsageMinorThreshold_Type()
)
diskVolumeUsageMinorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskVolumeUsageMinorThreshold.setStatus("current")
if mibBuilder.loadTexts:
    diskVolumeUsageMinorThreshold.setUnits("percent")


class _DiskVolumeAutoDeleteUnusedFile_Type(TruthValue):
    """Custom type diskVolumeAutoDeleteUnusedFile based on TruthValue"""
    defaultValue = 2


_DiskVolumeAutoDeleteUnusedFile_Type.__name__ = "TruthValue"
_DiskVolumeAutoDeleteUnusedFile_Object = MibTableColumn
diskVolumeAutoDeleteUnusedFile = _DiskVolumeAutoDeleteUnusedFile_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 12),
    _DiskVolumeAutoDeleteUnusedFile_Type()
)
diskVolumeAutoDeleteUnusedFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskVolumeAutoDeleteUnusedFile.setStatus("current")


class _DiskVolumeTrapInh_Type(Bits):
    """Custom type diskVolumeTrapInh based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("criticalUsageLevel", 0),
          ("majorUsageLevel", 1),
          ("minorUsageLevel", 2),
          ("autoDeleteFiles", 3))
    )

_DiskVolumeTrapInh_Type.__name__ = "Bits"
_DiskVolumeTrapInh_Object = MibTableColumn
diskVolumeTrapInh = _DiskVolumeTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 13),
    _DiskVolumeTrapInh_Type()
)
diskVolumeTrapInh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskVolumeTrapInh.setStatus("current")


class _DiskVolumeDiskSize_Type(Integer32):
    """Custom type diskVolumeDiskSize based on Integer32"""
    defaultValue = 0


_DiskVolumeDiskSize_Type.__name__ = "Integer32"
_DiskVolumeDiskSize_Object = MibTableColumn
diskVolumeDiskSize = _DiskVolumeDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 4, 1, 14),
    _DiskVolumeDiskSize_Type()
)
diskVolumeDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskVolumeDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    diskVolumeDiskSize.setUnits("bytes")
_DiskVolumeFileName_Type = DisplayString
_DiskVolumeFileName_Object = MibScalar
diskVolumeFileName = _DiskVolumeFileName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 5),
    _DiskVolumeFileName_Type()
)
diskVolumeFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    diskVolumeFileName.setStatus("current")
_EquipmentDiag_ObjectIdentity = ObjectIdentity
equipmentDiag = _EquipmentDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5)
)
_EqDiagConfig_ObjectIdentity = ObjectIdentity
eqDiagConfig = _EqDiagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1)
)


class _RemainInDiagMode_Type(TruthValue):
    """Custom type remainInDiagMode based on TruthValue"""
    defaultValue = 1


_RemainInDiagMode_Type.__name__ = "TruthValue"
_RemainInDiagMode_Object = MibScalar
remainInDiagMode = _RemainInDiagMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1, 1),
    _RemainInDiagMode_Type()
)
remainInDiagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remainInDiagMode.setStatus("current")


class _ConsoleOutput_Type(TruthValue):
    """Custom type consoleOutput based on TruthValue"""
    defaultValue = 2


_ConsoleOutput_Type.__name__ = "TruthValue"
_ConsoleOutput_Object = MibScalar
consoleOutput = _ConsoleOutput_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1, 2),
    _ConsoleOutput_Type()
)
consoleOutput.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    consoleOutput.setStatus("obsolete")


class _VerboseLevel_Type(Integer32):
    """Custom type verboseLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VerboseLevel_Type.__name__ = "Integer32"
_VerboseLevel_Object = MibScalar
verboseLevel = _VerboseLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1, 3),
    _VerboseLevel_Type()
)
verboseLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verboseLevel.setStatus("current")
_DiagTestId_Type = TestId
_DiagTestId_Object = MibScalar
diagTestId = _DiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 2),
    _DiagTestId_Type()
)
diagTestId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    diagTestId.setStatus("current")
_CardTestTable_Object = MibTable
cardTestTable = _CardTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cardTestTable.setStatus("current")
_CardTestEntry_Object = MibTableRow
cardTestEntry = _CardTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1)
)
cardTestEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardShelfTestIndex"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardTestIndex"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardTestId"),
)
if mibBuilder.loadTexts:
    cardTestEntry.setStatus("current")
_CardShelfTestIndex_Type = ShelfId
_CardShelfTestIndex_Object = MibTableColumn
cardShelfTestIndex = _CardShelfTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 1),
    _CardShelfTestIndex_Type()
)
cardShelfTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardShelfTestIndex.setStatus("deprecated")
_CardTestIndex_Type = CardId
_CardTestIndex_Object = MibTableColumn
cardTestIndex = _CardTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 2),
    _CardTestIndex_Type()
)
cardTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cardTestIndex.setStatus("current")
_CardTestId_Type = TestId
_CardTestId_Object = MibTableColumn
cardTestId = _CardTestId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 3),
    _CardTestId_Type()
)
cardTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cardTestId.setStatus("current")


class _CardTestName_Type(DisplayString):
    """Custom type cardTestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CardTestName_Type.__name__ = "DisplayString"
_CardTestName_Object = MibTableColumn
cardTestName = _CardTestName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 4),
    _CardTestName_Type()
)
cardTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestName.setStatus("current")


class _CardTestType_Type(TestType):
    """Custom type cardTestType based on TestType"""
    defaultValue = 3


_CardTestType_Type.__name__ = "TestType"
_CardTestType_Object = MibTableColumn
cardTestType = _CardTestType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 5),
    _CardTestType_Type()
)
cardTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestType.setStatus("current")
_CardTestDescription_Type = DisplayString
_CardTestDescription_Object = MibTableColumn
cardTestDescription = _CardTestDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 6),
    _CardTestDescription_Type()
)
cardTestDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestDescription.setStatus("current")


class _CardTestCommand_Type(TestCommand):
    """Custom type cardTestCommand based on TestCommand"""
    defaultValue = 1


_CardTestCommand_Type.__name__ = "TestCommand"
_CardTestCommand_Object = MibTableColumn
cardTestCommand = _CardTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 7),
    _CardTestCommand_Type()
)
cardTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestCommand.setStatus("current")


class _CardTestScheduleCommand_Type(TestScheduleCommand):
    """Custom type cardTestScheduleCommand based on TestScheduleCommand"""
    defaultValue = 1


_CardTestScheduleCommand_Type.__name__ = "TestScheduleCommand"
_CardTestScheduleCommand_Object = MibTableColumn
cardTestScheduleCommand = _CardTestScheduleCommand_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 8),
    _CardTestScheduleCommand_Type()
)
cardTestScheduleCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestScheduleCommand.setStatus("current")


class _CardTestSchedule_Type(TestSchedule):
    """Custom type cardTestSchedule based on TestSchedule"""
    defaultValue = 0


_CardTestSchedule_Type.__name__ = "TestSchedule"
_CardTestSchedule_Object = MibTableColumn
cardTestSchedule = _CardTestSchedule_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 9),
    _CardTestSchedule_Type()
)
cardTestSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestSchedule.setStatus("current")
_CardTestTime_Type = DateAndTime
_CardTestTime_Object = MibTableColumn
cardTestTime = _CardTestTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 10),
    _CardTestTime_Type()
)
cardTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestTime.setStatus("current")


class _CardTestResult_Type(TestResult):
    """Custom type cardTestResult based on TestResult"""
    defaultValue = 1


_CardTestResult_Type.__name__ = "TestResult"
_CardTestResult_Object = MibTableColumn
cardTestResult = _CardTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 11),
    _CardTestResult_Type()
)
cardTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestResult.setStatus("current")
_CardTestResultDesc_Type = DisplayString
_CardTestResultDesc_Object = MibTableColumn
cardTestResultDesc = _CardTestResultDesc_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 12),
    _CardTestResultDesc_Type()
)
cardTestResultDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestResultDesc.setStatus("current")
_CardTestTransId_Type = TestTransactionId
_CardTestTransId_Object = MibTableColumn
cardTestTransId = _CardTestTransId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 13),
    _CardTestTransId_Type()
)
cardTestTransId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestTransId.setStatus("current")
_EquipmentAudit_ObjectIdentity = ObjectIdentity
equipmentAudit = _EquipmentAudit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6)
)


class _AuditAutoScheduling_Type(TruthValue):
    """Custom type auditAutoScheduling based on TruthValue"""
    defaultValue = 1


_AuditAutoScheduling_Type.__name__ = "TruthValue"
_AuditAutoScheduling_Object = MibScalar
auditAutoScheduling = _AuditAutoScheduling_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 1),
    _AuditAutoScheduling_Type()
)
auditAutoScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditAutoScheduling.setStatus("current")


class _AuditLogOutput_Type(TruthValue):
    """Custom type auditLogOutput based on TruthValue"""
    defaultValue = 1


_AuditLogOutput_Type.__name__ = "TruthValue"
_AuditLogOutput_Object = MibScalar
auditLogOutput = _AuditLogOutput_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 2),
    _AuditLogOutput_Type()
)
auditLogOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogOutput.setStatus("current")


class _AuditLogThrottle_Type(TruthValue):
    """Custom type auditLogThrottle based on TruthValue"""
    defaultValue = 1


_AuditLogThrottle_Type.__name__ = "TruthValue"
_AuditLogThrottle_Object = MibScalar
auditLogThrottle = _AuditLogThrottle_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 3),
    _AuditLogThrottle_Type()
)
auditLogThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogThrottle.setStatus("current")
_AuditTable_Object = MibTable
auditTable = _AuditTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4)
)
if mibBuilder.loadTexts:
    auditTable.setStatus("current")
_AuditEntry_Object = MibTableRow
auditEntry = _AuditEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1)
)
auditEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "auditShelfId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "auditCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "auditId"),
)
if mibBuilder.loadTexts:
    auditEntry.setStatus("current")
_AuditShelfId_Type = ShelfId
_AuditShelfId_Object = MibTableColumn
auditShelfId = _AuditShelfId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 1),
    _AuditShelfId_Type()
)
auditShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditShelfId.setStatus("deprecated")
_AuditCardId_Type = CardId
_AuditCardId_Object = MibTableColumn
auditCardId = _AuditCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 2),
    _AuditCardId_Type()
)
auditCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auditCardId.setStatus("current")
_AuditId_Type = Unsigned32
_AuditId_Object = MibTableColumn
auditId = _AuditId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 3),
    _AuditId_Type()
)
auditId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auditId.setStatus("current")
_AuditName_Type = DisplayString
_AuditName_Object = MibTableColumn
auditName = _AuditName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 4),
    _AuditName_Type()
)
auditName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditName.setStatus("current")
_AuditDescription_Type = DisplayString
_AuditDescription_Object = MibTableColumn
auditDescription = _AuditDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 5),
    _AuditDescription_Type()
)
auditDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditDescription.setStatus("current")
_AuditTime_Type = DateAndTime
_AuditTime_Object = MibTableColumn
auditTime = _AuditTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 6),
    _AuditTime_Type()
)
auditTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditTime.setStatus("current")


class _AuditCommand_Type(Integer32):
    """Custom type auditCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("runnow", 4))
    )


_AuditCommand_Type.__name__ = "Integer32"
_AuditCommand_Object = MibTableColumn
auditCommand = _AuditCommand_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 7),
    _AuditCommand_Type()
)
auditCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditCommand.setStatus("current")


class _AuditStatus_Type(Integer32):
    """Custom type auditStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AuditStatus_Type.__name__ = "Integer32"
_AuditStatus_Object = MibTableColumn
auditStatus = _AuditStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 8),
    _AuditStatus_Type()
)
auditStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditStatus.setStatus("current")


class _AuditResult_Type(Integer32):
    """Custom type auditResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("passed", 1),
          ("failed", 2),
          ("abort", 4),
          ("notRun", 5))
    )


_AuditResult_Type.__name__ = "Integer32"
_AuditResult_Object = MibTableColumn
auditResult = _AuditResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 9),
    _AuditResult_Type()
)
auditResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditResult.setStatus("current")
_AuditPassedCount_Type = Unsigned32
_AuditPassedCount_Object = MibTableColumn
auditPassedCount = _AuditPassedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 10),
    _AuditPassedCount_Type()
)
auditPassedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditPassedCount.setStatus("current")
_AuditFailedCount_Type = Unsigned32
_AuditFailedCount_Object = MibTableColumn
auditFailedCount = _AuditFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 11),
    _AuditFailedCount_Type()
)
auditFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditFailedCount.setStatus("current")
_AuditCycleCount_Type = Unsigned32
_AuditCycleCount_Object = MibTableColumn
auditCycleCount = _AuditCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 12),
    _AuditCycleCount_Type()
)
auditCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditCycleCount.setStatus("current")
_AuditTotalPassedCount_Type = Unsigned32
_AuditTotalPassedCount_Object = MibTableColumn
auditTotalPassedCount = _AuditTotalPassedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 13),
    _AuditTotalPassedCount_Type()
)
auditTotalPassedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditTotalPassedCount.setStatus("current")
_AuditTotalFailedCount_Type = Unsigned32
_AuditTotalFailedCount_Object = MibTableColumn
auditTotalFailedCount = _AuditTotalFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 14),
    _AuditTotalFailedCount_Type()
)
auditTotalFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditTotalFailedCount.setStatus("current")
_CmDevice_ObjectIdentity = ObjectIdentity
cmDevice = _CmDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8)
)
_CmMacAddress_Type = MacAddress
_CmMacAddress_Object = MibScalar
cmMacAddress = _CmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 1),
    _CmMacAddress_Type()
)
cmMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmMacAddress.setStatus("current")
_CmVendor_Type = DisplayString
_CmVendor_Object = MibScalar
cmVendor = _CmVendor_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 2),
    _CmVendor_Type()
)
cmVendor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmVendor.setStatus("current")
_CmResetReason_Type = DisplayString
_CmResetReason_Object = MibScalar
cmResetReason = _CmResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 3),
    _CmResetReason_Type()
)
cmResetReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetReason.setStatus("current")


class _CmUChannelID_Type(Integer32):
    """Custom type cmUChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUChannelID_Type.__name__ = "Integer32"
_CmUChannelID_Object = MibScalar
cmUChannelID = _CmUChannelID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 4),
    _CmUChannelID_Type()
)
cmUChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmUChannelID.setStatus("current")


class _CmPrimarySID_Type(Unsigned32):
    """Custom type cmPrimarySID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CmPrimarySID_Type.__name__ = "Unsigned32"
_CmPrimarySID_Object = MibScalar
cmPrimarySID = _CmPrimarySID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 5),
    _CmPrimarySID_Type()
)
cmPrimarySID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmPrimarySID.setStatus("current")
_CmResetStatus_Type = DisplayString
_CmResetStatus_Object = MibScalar
cmResetStatus = _CmResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 6),
    _CmResetStatus_Type()
)
cmResetStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetStatus.setStatus("current")
_CmResetUpTime_Type = TimeTicks
_CmResetUpTime_Object = MibScalar
cmResetUpTime = _CmResetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 7),
    _CmResetUpTime_Type()
)
cmResetUpTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetUpTime.setStatus("current")
_CmResetInfo_Type = DisplayString
_CmResetInfo_Object = MibScalar
cmResetInfo = _CmResetInfo_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 8),
    _CmResetInfo_Type()
)
cmResetInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetInfo.setStatus("current")


class _CmIpAddress_Type(OctetString):
    """Custom type cmIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmIpAddress_Type.__name__ = "OctetString"
_CmIpAddress_Object = MibScalar
cmIpAddress = _CmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 9),
    _CmIpAddress_Type()
)
cmIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmIpAddress.setStatus("current")
_EquipmentError_ObjectIdentity = ObjectIdentity
equipmentError = _EquipmentError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9)
)
_FpgaErrorEventTable_Object = MibTable
fpgaErrorEventTable = _FpgaErrorEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1)
)
if mibBuilder.loadTexts:
    fpgaErrorEventTable.setStatus("current")
_FpgaErrorEventEntry_Object = MibTableRow
fpgaErrorEventEntry = _FpgaErrorEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1)
)
fpgaErrorEventEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "errEventId"),
)
if mibBuilder.loadTexts:
    fpgaErrorEventEntry.setStatus("current")


class _ErrEventId_Type(Unsigned32):
    """Custom type errEventId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ErrEventId_Type.__name__ = "Unsigned32"
_ErrEventId_Object = MibTableColumn
errEventId = _ErrEventId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 1),
    _ErrEventId_Type()
)
errEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    errEventId.setStatus("current")


class _ErrEvRecoveryEnabled_Type(TruthValue):
    """Custom type errEvRecoveryEnabled based on TruthValue"""
    defaultValue = 1


_ErrEvRecoveryEnabled_Type.__name__ = "TruthValue"
_ErrEvRecoveryEnabled_Object = MibTableColumn
errEvRecoveryEnabled = _ErrEvRecoveryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 2),
    _ErrEvRecoveryEnabled_Type()
)
errEvRecoveryEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvRecoveryEnabled.setStatus("current")


class _ErrEvLoggingEnabled_Type(TruthValue):
    """Custom type errEvLoggingEnabled based on TruthValue"""
    defaultValue = 1


_ErrEvLoggingEnabled_Type.__name__ = "TruthValue"
_ErrEvLoggingEnabled_Object = MibTableColumn
errEvLoggingEnabled = _ErrEvLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 3),
    _ErrEvLoggingEnabled_Type()
)
errEvLoggingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvLoggingEnabled.setStatus("current")


class _ErrEvLogLevel_Type(Integer32):
    """Custom type errEvLogLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ErrEvLogLevel_Type.__name__ = "Integer32"
_ErrEvLogLevel_Object = MibTableColumn
errEvLogLevel = _ErrEvLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 4),
    _ErrEvLogLevel_Type()
)
errEvLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvLogLevel.setStatus("current")
_ErrEvRowStatus_Type = RowStatus
_ErrEvRowStatus_Object = MibTableColumn
errEvRowStatus = _ErrEvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 5),
    _ErrEvRowStatus_Type()
)
errEvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvRowStatus.setStatus("current")
_CadEquipmentMibConformance_ObjectIdentity = ObjectIdentity
cadEquipmentMibConformance = _CadEquipmentMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10)
)
_CadEquipmentMibCompliances_ObjectIdentity = ObjectIdentity
cadEquipmentMibCompliances = _CadEquipmentMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 1)
)
_CadEquipmentMibGroup_ObjectIdentity = ObjectIdentity
cadEquipmentMibGroup = _CadEquipmentMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2)
)

# Managed Objects groups

systemGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 1)
)
systemGeneralGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemKey"))
)
if mibBuilder.loadTexts:
    systemGeneralGroup.setStatus("current")

equipmentStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 2)
)
equipmentStateGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cardLastChangeTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentStateGroup.setStatus("current")

equipmentShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 3)
)
equipmentShelfGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "shelfName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfSwVersion"))
)
if mibBuilder.loadTexts:
    equipmentShelfGroup.setStatus("current")

equipmentCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 4)
)
equipmentCardGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cardName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSerialNum"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardFwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardHwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardAdminState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardPrState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSecState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardDplxStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardAction"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTrapInh"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumPorts"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSubDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardFwUpdateStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSpareGroupId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSpareGroupMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardUpTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTemperature"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardCpuType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardCpuSpeed"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardBusSpeed"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardRamSize"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardFlashSize"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardCPLDVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardFpgaSource"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardBootVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardLastBootVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardLastBootSource"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardPicDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardPicSerialNum"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardPicHwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTemperatureHighWarn"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTemperatureHighError"))
)
if mibBuilder.loadTexts:
    equipmentCardGroup.setStatus("current")

equipmentPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 5)
)
equipmentPortGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "portType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portAdminState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portPrState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portSecState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portDplxStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portAction"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portTrapInh"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portNumChans"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portDetectedMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portDocsIfIndex"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portBgpId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portConnectorId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portDescription"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portCurrDsPower"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portMinDsPower"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portMaxDsPower"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portTxFlowControlMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portRxFlowControlMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portTxFlowControlDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portRxFlowControlDetected"))
)
if mibBuilder.loadTexts:
    equipmentPortGroup.setStatus("current")

equipmentDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 6)
)
equipmentDiagGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "remainInDiagMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "verboseLevel"))
)
if mibBuilder.loadTexts:
    equipmentDiagGroup.setStatus("current")

equipmentCardTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 8)
)
equipmentCardTestGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cardTestName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestDescription"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestCommand"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestScheduleCommand"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestSchedule"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResult"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResultDesc"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestTransId"))
)
if mibBuilder.loadTexts:
    equipmentCardTestGroup.setStatus("current")

equipmentAuditGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 10)
)
equipmentAuditGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "auditAutoScheduling"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditLogOutput"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditLogThrottle"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditDescription"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditCommand"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditResult"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditPassedCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditFailedCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditCycleCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditTotalPassedCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditTotalFailedCount"))
)
if mibBuilder.loadTexts:
    equipmentAuditGroup.setStatus("current")

diskVolumeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 11)
)
diskVolumeGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeSize"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeUsageLevel"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeUsagePercentage"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeUsageCriticalThreshold"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeUsageMajorThreshold"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeUsageMinorThreshold"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeAutoDeleteUnusedFile"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeTrapInh"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeFileName"))
)
if mibBuilder.loadTexts:
    diskVolumeGroup.setStatus("current")

fpgaErrorEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 12)
)
fpgaErrorEventGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "errEvRecoveryEnabled"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "errEvLoggingEnabled"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "errEvLogLevel"))
)
if mibBuilder.loadTexts:
    fpgaErrorEventGroup.setStatus("current")


# Notification objects

cardPrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 5)
)
cardPrStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardPrState"))
)
if mibBuilder.loadTexts:
    cardPrStateChange.setStatus(
        "current"
    )

cardSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 6)
)
cardSecStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSecState"))
)
if mibBuilder.loadTexts:
    cardSecStateChange.setStatus(
        "current"
    )

cardDetectedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 7)
)
cardDetectedChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSubDetected"))
)
if mibBuilder.loadTexts:
    cardDetectedChange.setStatus(
        "current"
    )

cardDplxStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 8)
)
cardDplxStatusChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardDplxStatus"))
)
if mibBuilder.loadTexts:
    cardDplxStatusChange.setStatus(
        "current"
    )

portPrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 9)
)
portPrStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portPrState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portDocsIfIndex"))
)
if mibBuilder.loadTexts:
    portPrStateChange.setStatus(
        "current"
    )

portSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 10)
)
portSecStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portSecState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portDocsIfIndex"))
)
if mibBuilder.loadTexts:
    portSecStateChange.setStatus(
        "current"
    )

portDplxStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 11)
)
portDplxStatusChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardDplxStatus"))
)
if mibBuilder.loadTexts:
    portDplxStatusChange.setStatus(
        "current"
    )

cardTestResultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 13)
)
cardTestResultNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diagTestId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResult"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResultDesc"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestTransId"))
)
if mibBuilder.loadTexts:
    cardTestResultNotification.setStatus(
        "current"
    )

cmResetClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 15)
)
cmResetClearNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmUChannelID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"))
)
if mibBuilder.loadTexts:
    cmResetClearNotification.setStatus(
        "current"
    )

cmResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 16)
)
cmResetNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmVendor"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetReason"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmUChannelID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmPrimarySID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetUpTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetInfo"))
)
if mibBuilder.loadTexts:
    cmResetNotification.setStatus(
        "current"
    )

diskVolumeUsageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 17)
)
diskVolumeUsageNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskDriveNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeUsageLevel"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeName"))
)
if mibBuilder.loadTexts:
    diskVolumeUsageNotification.setStatus(
        "current"
    )

diskVolumeAutoDeleteFileNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 18)
)
diskVolumeAutoDeleteFileNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskDriveNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeFileName"))
)
if mibBuilder.loadTexts:
    diskVolumeAutoDeleteFileNotification.setStatus(
        "current"
    )

cardTempOutOfRangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 19)
)
cardTempOutOfRangeNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"))
)
if mibBuilder.loadTexts:
    cardTempOutOfRangeNotification.setStatus(
        "current"
    )

cardTempNoReportNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 20)
)
cardTempNoReportNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"))
)
if mibBuilder.loadTexts:
    cardTempNoReportNotification.setStatus(
        "current"
    )

cardTempOverHeatNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 21)
)
cardTempOverHeatNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"))
)
if mibBuilder.loadTexts:
    cardTempOverHeatNotification.setStatus(
        "current"
    )

downstreamPowerLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 22)
)
downstreamPowerLoss.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portNumber"))
)
if mibBuilder.loadTexts:
    downstreamPowerLoss.setStatus(
        "current"
    )

cmRegistrationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 23)
)
cmRegistrationNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmVendor"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmUChannelID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmIpAddress"))
)
if mibBuilder.loadTexts:
    cmRegistrationNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cadEquipmentMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 1, 1)
)
cadEquipmentMibCompliance.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "systemGeneralGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "equipmentStateGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "equipmentShelfGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "equipmentCardGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "equipmentPortGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "equipmentDiagGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "equipmentCardTestGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "equipmentAuditGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diskVolumeGroup"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "fpgaErrorEventGroup"))
)
if mibBuilder.loadTexts:
    cadEquipmentMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-EQUIPMENT-MIB",
    **{"TestId": TestId,
       "TestType": TestType,
       "TestCommand": TestCommand,
       "TestScheduleCommand": TestScheduleCommand,
       "TestSchedule": TestSchedule,
       "TestResult": TestResult,
       "TestTransactionId": TestTransactionId,
       "cadEquipmentMib": cadEquipmentMib,
       "equipmentTraps": equipmentTraps,
       "cardPrStateChange": cardPrStateChange,
       "cardSecStateChange": cardSecStateChange,
       "cardDetectedChange": cardDetectedChange,
       "cardDplxStatusChange": cardDplxStatusChange,
       "portPrStateChange": portPrStateChange,
       "portSecStateChange": portSecStateChange,
       "portDplxStatusChange": portDplxStatusChange,
       "cardTestResultNotification": cardTestResultNotification,
       "cmResetClearNotification": cmResetClearNotification,
       "cmResetNotification": cmResetNotification,
       "diskVolumeUsageNotification": diskVolumeUsageNotification,
       "diskVolumeAutoDeleteFileNotification": diskVolumeAutoDeleteFileNotification,
       "cardTempOutOfRangeNotification": cardTempOutOfRangeNotification,
       "cardTempNoReportNotification": cardTempNoReportNotification,
       "cardTempOverHeatNotification": cardTempOverHeatNotification,
       "downstreamPowerLoss": downstreamPowerLoss,
       "cmRegistrationNotification": cmRegistrationNotification,
       "systemGeneral": systemGeneral,
       "systemClock": systemClock,
       "trapCounter": trapCounter,
       "trapSeverity": trapSeverity,
       "systemKey": systemKey,
       "cardNumber": cardNumber,
       "portNumber": portNumber,
       "diskDriveNumber": diskDriveNumber,
       "diskVolumeNumber": diskVolumeNumber,
       "shelfObjects": shelfObjects,
       "shelfNumber": shelfNumber,
       "shelfName": shelfName,
       "shelfSwVersion": shelfSwVersion,
       "equipmentState": equipmentState,
       "cardLastChangeTime": cardLastChangeTime,
       "portLastChangeTime": portLastChangeTime,
       "equipmentTbl": equipmentTbl,
       "cardTable": cardTable,
       "cardEntry": cardEntry,
       "cardShelfId": cardShelfId,
       "cardId": cardId,
       "cardName": cardName,
       "cardType": cardType,
       "cardSubType": cardSubType,
       "cardSerialNum": cardSerialNum,
       "cardFwVersion": cardFwVersion,
       "cardHwVersion": cardHwVersion,
       "cardSwVersion": cardSwVersion,
       "cardAdminState": cardAdminState,
       "cardPrState": cardPrState,
       "cardSecState": cardSecState,
       "cardDplxStatus": cardDplxStatus,
       "cardAction": cardAction,
       "cardTrapInh": cardTrapInh,
       "cardNumPorts": cardNumPorts,
       "cardDetected": cardDetected,
       "cardSubDetected": cardSubDetected,
       "cardFwUpdateStatus": cardFwUpdateStatus,
       "cardSpareGroupId": cardSpareGroupId,
       "cardSpareGroupMode": cardSpareGroupMode,
       "cardUpTime": cardUpTime,
       "cardTemperature": cardTemperature,
       "cardCpuType": cardCpuType,
       "cardCpuSpeed": cardCpuSpeed,
       "cardBusSpeed": cardBusSpeed,
       "cardRamSize": cardRamSize,
       "cardFlashSize": cardFlashSize,
       "cardCPLDVersion": cardCPLDVersion,
       "cardFpgaSource": cardFpgaSource,
       "cardBootVersion": cardBootVersion,
       "cardLastBootVersion": cardLastBootVersion,
       "cardLastBootSource": cardLastBootSource,
       "cardPicDetected": cardPicDetected,
       "cardPicSerialNum": cardPicSerialNum,
       "cardPicHwVersion": cardPicHwVersion,
       "cardLastResetReason": cardLastResetReason,
       "cardTemperatureHighWarn": cardTemperatureHighWarn,
       "cardTemperatureHighError": cardTemperatureHighError,
       "cardCarrierSerialNum": cardCarrierSerialNum,
       "cardCarrierFwVersion": cardCarrierFwVersion,
       "cardCarrierHwVersion": cardCarrierHwVersion,
       "portTable": portTable,
       "portEntry": portEntry,
       "portShelfId": portShelfId,
       "portCardId": portCardId,
       "portId": portId,
       "portType": portType,
       "portAdminState": portAdminState,
       "portPrState": portPrState,
       "portSecState": portSecState,
       "portDplxStatus": portDplxStatus,
       "portAction": portAction,
       "portTrapInh": portTrapInh,
       "portNumChans": portNumChans,
       "portDocsIfIndex": portDocsIfIndex,
       "portMacAddress": portMacAddress,
       "portMode": portMode,
       "portDetectedMode": portDetectedMode,
       "portBgpId": portBgpId,
       "portConnectorId": portConnectorId,
       "portCardSubType": portCardSubType,
       "portDescription": portDescription,
       "portCurrDsPower": portCurrDsPower,
       "portMinDsPower": portMinDsPower,
       "portMaxDsPower": portMaxDsPower,
       "portTxFlowControlMode": portTxFlowControlMode,
       "portRxFlowControlMode": portRxFlowControlMode,
       "portTxFlowControlDetected": portTxFlowControlDetected,
       "portRxFlowControlDetected": portRxFlowControlDetected,
       "portMacIfIndex": portMacIfIndex,
       "diskVolumeTable": diskVolumeTable,
       "diskVolumeEntry": diskVolumeEntry,
       "diskVolumeShelfId": diskVolumeShelfId,
       "diskVolumeCardId": diskVolumeCardId,
       "diskVolumeDriveId": diskVolumeDriveId,
       "diskVolumeId": diskVolumeId,
       "diskVolumeName": diskVolumeName,
       "diskVolumeSize": diskVolumeSize,
       "diskVolumeUsageLevel": diskVolumeUsageLevel,
       "diskVolumeUsagePercentage": diskVolumeUsagePercentage,
       "diskVolumeUsageCriticalThreshold": diskVolumeUsageCriticalThreshold,
       "diskVolumeUsageMajorThreshold": diskVolumeUsageMajorThreshold,
       "diskVolumeUsageMinorThreshold": diskVolumeUsageMinorThreshold,
       "diskVolumeAutoDeleteUnusedFile": diskVolumeAutoDeleteUnusedFile,
       "diskVolumeTrapInh": diskVolumeTrapInh,
       "diskVolumeDiskSize": diskVolumeDiskSize,
       "diskVolumeFileName": diskVolumeFileName,
       "equipmentDiag": equipmentDiag,
       "eqDiagConfig": eqDiagConfig,
       "remainInDiagMode": remainInDiagMode,
       "consoleOutput": consoleOutput,
       "verboseLevel": verboseLevel,
       "diagTestId": diagTestId,
       "cardTestTable": cardTestTable,
       "cardTestEntry": cardTestEntry,
       "cardShelfTestIndex": cardShelfTestIndex,
       "cardTestIndex": cardTestIndex,
       "cardTestId": cardTestId,
       "cardTestName": cardTestName,
       "cardTestType": cardTestType,
       "cardTestDescription": cardTestDescription,
       "cardTestCommand": cardTestCommand,
       "cardTestScheduleCommand": cardTestScheduleCommand,
       "cardTestSchedule": cardTestSchedule,
       "cardTestTime": cardTestTime,
       "cardTestResult": cardTestResult,
       "cardTestResultDesc": cardTestResultDesc,
       "cardTestTransId": cardTestTransId,
       "equipmentAudit": equipmentAudit,
       "auditAutoScheduling": auditAutoScheduling,
       "auditLogOutput": auditLogOutput,
       "auditLogThrottle": auditLogThrottle,
       "auditTable": auditTable,
       "auditEntry": auditEntry,
       "auditShelfId": auditShelfId,
       "auditCardId": auditCardId,
       "auditId": auditId,
       "auditName": auditName,
       "auditDescription": auditDescription,
       "auditTime": auditTime,
       "auditCommand": auditCommand,
       "auditStatus": auditStatus,
       "auditResult": auditResult,
       "auditPassedCount": auditPassedCount,
       "auditFailedCount": auditFailedCount,
       "auditCycleCount": auditCycleCount,
       "auditTotalPassedCount": auditTotalPassedCount,
       "auditTotalFailedCount": auditTotalFailedCount,
       "cmDevice": cmDevice,
       "cmMacAddress": cmMacAddress,
       "cmVendor": cmVendor,
       "cmResetReason": cmResetReason,
       "cmUChannelID": cmUChannelID,
       "cmPrimarySID": cmPrimarySID,
       "cmResetStatus": cmResetStatus,
       "cmResetUpTime": cmResetUpTime,
       "cmResetInfo": cmResetInfo,
       "cmIpAddress": cmIpAddress,
       "equipmentError": equipmentError,
       "fpgaErrorEventTable": fpgaErrorEventTable,
       "fpgaErrorEventEntry": fpgaErrorEventEntry,
       "errEventId": errEventId,
       "errEvRecoveryEnabled": errEvRecoveryEnabled,
       "errEvLoggingEnabled": errEvLoggingEnabled,
       "errEvLogLevel": errEvLogLevel,
       "errEvRowStatus": errEvRowStatus,
       "cadEquipmentMibConformance": cadEquipmentMibConformance,
       "cadEquipmentMibCompliances": cadEquipmentMibCompliances,
       "cadEquipmentMibCompliance": cadEquipmentMibCompliance,
       "cadEquipmentMibGroup": cadEquipmentMibGroup,
       "systemGeneralGroup": systemGeneralGroup,
       "equipmentStateGroup": equipmentStateGroup,
       "equipmentShelfGroup": equipmentShelfGroup,
       "equipmentCardGroup": equipmentCardGroup,
       "equipmentPortGroup": equipmentPortGroup,
       "equipmentDiagGroup": equipmentDiagGroup,
       "equipmentCardTestGroup": equipmentCardTestGroup,
       "equipmentAuditGroup": equipmentAuditGroup,
       "diskVolumeGroup": diskVolumeGroup,
       "fpgaErrorEventGroup": fpgaErrorEventGroup}
)
