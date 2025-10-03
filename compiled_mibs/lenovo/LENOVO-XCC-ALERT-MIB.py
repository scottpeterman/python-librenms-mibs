# SNMP MIB module (LENOVO-XCC-ALERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\lenovo\LENOVO-XCC-ALERT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:27 2025
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

(supportProcessor,) = mibBuilder.importSymbols(
    "LENOVO-XCC-MIB",
    "supportProcessor")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lenovoXCCAlertMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5)
)
if mibBuilder.loadTexts:
    lenovoXCCAlertMIB.setRevisions(
        ("2016-10-27 18:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xcctrapg_ObjectIdentity = ObjectIdentity
xcctrapg = _Xcctrapg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1)
)
_AltDateTime_Type = DisplayString
_AltDateTime_Object = MibScalar
altDateTime = _AltDateTime_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 1),
    _AltDateTime_Type()
)
altDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altDateTime.setStatus("mandatory")
_AltSpTxtId_Type = DisplayString
_AltSpTxtId_Object = MibScalar
altSpTxtId = _AltSpTxtId_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 3),
    _AltSpTxtId_Type()
)
altSpTxtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSpTxtId.setStatus("mandatory")
_AltSysUuid_Type = DisplayString
_AltSysUuid_Object = MibScalar
altSysUuid = _AltSysUuid_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 5),
    _AltSysUuid_Type()
)
altSysUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSysUuid.setStatus("mandatory")
_AltSysSern_Type = DisplayString
_AltSysSern_Object = MibScalar
altSysSern = _AltSysSern_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 6),
    _AltSysSern_Type()
)
altSysSern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSysSern.setStatus("mandatory")


class _AltPriority_Type(Integer32):
    """Custom type altPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AltPriority_Type.__name__ = "Integer32"
_AltPriority_Object = MibScalar
altPriority = _AltPriority_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 8),
    _AltPriority_Type()
)
altPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altPriority.setStatus("mandatory")
_AltMsgText_Type = DisplayString
_AltMsgText_Object = MibScalar
altMsgText = _AltMsgText_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 9),
    _AltMsgText_Type()
)
altMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altMsgText.setStatus("mandatory")
_AltMsgID_Type = Integer32
_AltMsgID_Object = MibScalar
altMsgID = _AltMsgID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 10),
    _AltMsgID_Type()
)
altMsgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altMsgID.setStatus("mandatory")
_AltMsgIDPrefix_Type = DisplayString
_AltMsgIDPrefix_Object = MibScalar
altMsgIDPrefix = _AltMsgIDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 11),
    _AltMsgIDPrefix_Type()
)
altMsgIDPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altMsgIDPrefix.setStatus("mandatory")
_AltHostContact_Type = DisplayString
_AltHostContact_Object = MibScalar
altHostContact = _AltHostContact_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 12),
    _AltHostContact_Type()
)
altHostContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostContact.setStatus("mandatory")
_AltHostLocation_Type = DisplayString
_AltHostLocation_Object = MibScalar
altHostLocation = _AltHostLocation_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 13),
    _AltHostLocation_Type()
)
altHostLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostLocation.setStatus("mandatory")
_AltHostRoomID_Type = DisplayString
_AltHostRoomID_Object = MibScalar
altHostRoomID = _AltHostRoomID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 14),
    _AltHostRoomID_Type()
)
altHostRoomID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostRoomID.setStatus("mandatory")
_AltHostRackID_Type = DisplayString
_AltHostRackID_Object = MibScalar
altHostRackID = _AltHostRackID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 15),
    _AltHostRackID_Type()
)
altHostRackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostRackID.setStatus("mandatory")
_AltHostLowestUpos_Type = DisplayString
_AltHostLowestUpos_Object = MibScalar
altHostLowestUpos = _AltHostLowestUpos_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 16),
    _AltHostLowestUpos_Type()
)
altHostLowestUpos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostLowestUpos.setStatus("mandatory")
_AltHostBladeBay_Type = DisplayString
_AltHostBladeBay_Object = MibScalar
altHostBladeBay = _AltHostBladeBay_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 17),
    _AltHostBladeBay_Type()
)
altHostBladeBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostBladeBay.setStatus("mandatory")
_AltEventID_Type = DisplayString
_AltEventID_Object = MibScalar
altEventID = _AltEventID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 18),
    _AltEventID_Type()
)
altEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altEventID.setStatus("mandatory")


class _AltServiceable_Type(Integer32):
    """Custom type altServiceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notServiceable", 0),
          ("serviceableByLenovo", 1),
          ("serviceableByCustomer", 2))
    )


_AltServiceable_Type.__name__ = "Integer32"
_AltServiceable_Object = MibScalar
altServiceable = _AltServiceable_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 19),
    _AltServiceable_Type()
)
altServiceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altServiceable.setStatus("mandatory")


class _AltTest_Type(Integer32):
    """Custom type altTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AltTest_Type.__name__ = "Integer32"
_AltTest_Object = MibScalar
altTest = _AltTest_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 20),
    _AltTest_Type()
)
altTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altTest.setStatus("mandatory")
_AltFailingFRUs_Type = DisplayString
_AltFailingFRUs_Object = MibScalar
altFailingFRUs = _AltFailingFRUs_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 21),
    _AltFailingFRUs_Type()
)
altFailingFRUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altFailingFRUs.setStatus("mandatory")
_AltHostMTM_Type = DisplayString
_AltHostMTM_Object = MibScalar
altHostMTM = _AltHostMTM_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 22),
    _AltHostMTM_Type()
)
altHostMTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostMTM.setStatus("mandatory")
_AltAuxData_Type = DisplayString
_AltAuxData_Object = MibScalar
altAuxData = _AltAuxData_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 23),
    _AltAuxData_Type()
)
altAuxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altAuxData.setStatus("mandatory")
_AltCommonEventID_Type = DisplayString
_AltCommonEventID_Object = MibScalar
altCommonEventID = _AltCommonEventID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 24),
    _AltCommonEventID_Type()
)
altCommonEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altCommonEventID.setStatus("mandatory")


class _AltEventType_Type(Integer32):
    """Custom type altEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AltEventType_Type.__name__ = "Integer32"
_AltEventType_Object = MibScalar
altEventType = _AltEventType_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 25),
    _AltEventType_Type()
)
altEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altEventType.setStatus("mandatory")
_AltDetectorID_Type = DisplayString
_AltDetectorID_Object = MibScalar
altDetectorID = _AltDetectorID_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 26),
    _AltDetectorID_Type()
)
altDetectorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altDetectorID.setStatus("mandatory")
_AltDIMMPartNumber_Type = DisplayString
_AltDIMMPartNumber_Object = MibScalar
altDIMMPartNumber = _AltDIMMPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 1, 27),
    _AltDIMMPartNumber_Type()
)
altDIMMPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altDIMMPartNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lenovoSpTrapTempC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 0)
)
lenovoSpTrapTempC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapTempC.setStatus(
        ""
    )

lenovoSpTrapVoltC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 1)
)
lenovoSpTrapVoltC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapVoltC.setStatus(
        ""
    )

lenovoSpTrapPowerC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 4)
)
lenovoSpTrapPowerC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapPowerC.setStatus(
        ""
    )

lenovoSpTrapHdC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 5)
)
lenovoSpTrapHdC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapHdC.setStatus(
        ""
    )

lenovoSpTrapRdpsC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 9)
)
lenovoSpTrapRdpsC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapRdpsC.setStatus(
        ""
    )

lenovoSpTrapRdpsN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 10)
)
lenovoSpTrapRdpsN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapRdpsN.setStatus(
        ""
    )

lenovoSpTrapFanC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 11)
)
lenovoSpTrapFanC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapFanC.setStatus(
        ""
    )

lenovoSpTrapTempN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 12)
)
lenovoSpTrapTempN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapTempN.setStatus(
        ""
    )

lenovoSpTrapVoltN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 13)
)
lenovoSpTrapVoltN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapVoltN.setStatus(
        ""
    )

lenovoSpTrapOsToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 21)
)
lenovoSpTrapOsToS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapOsToS.setStatus(
        ""
    )

lenovoSpTrapAppS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 22)
)
lenovoSpTrapAppS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapAppS.setStatus(
        ""
    )

lenovoSpTrapPoffS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 23)
)
lenovoSpTrapPoffS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapPoffS.setStatus(
        ""
    )

lenovoSpTrapPonS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 24)
)
lenovoSpTrapPonS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapPonS.setStatus(
        ""
    )

lenovoSpTrapBootS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 25)
)
lenovoSpTrapBootS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapBootS.setStatus(
        ""
    )

lenovoSpTrapLdrToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 26)
)
lenovoSpTrapLdrToS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapLdrToS.setStatus(
        ""
    )

lenovoSpTrapPFAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 27)
)
lenovoSpTrapPFAS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapPFAS.setStatus(
        ""
    )

lenovoSpTrapRLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 30)
)
lenovoSpTrapRLogin.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapRLogin.setStatus(
        ""
    )

lenovoSpTrapSysLogS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 35)
)
lenovoSpTrapSysLogS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapSysLogS.setStatus(
        ""
    )

lenovoSpTrapIhcC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 36)
)
lenovoSpTrapIhcC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapIhcC.setStatus(
        ""
    )

lenovoSpTrapNwChangeS = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 37)
)
lenovoSpTrapNwChangeS.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapNwChangeS.setStatus(
        ""
    )

lenovoSpTrapCPUC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 40)
)
lenovoSpTrapCPUC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapCPUC.setStatus(
        ""
    )

lenovoSpTrapMemoryC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 41)
)
lenovoSpTrapMemoryC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapMemoryC.setStatus(
        ""
    )

lenovoSpTrapCPUN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 42)
)
lenovoSpTrapCPUN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapCPUN.setStatus(
        ""
    )

lenovoSpTrapMemoryN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 43)
)
lenovoSpTrapMemoryN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapMemoryN.setStatus(
        ""
    )

lenovoSpTrapHardwareC = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 50)
)
lenovoSpTrapHardwareC.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapHardwareC.setStatus(
        ""
    )

lenovoSpTrapHardwareN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 60)
)
lenovoSpTrapHardwareN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapHardwareN.setStatus(
        ""
    )

lenovoSpTrapPowerN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 164)
)
lenovoSpTrapPowerN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"),
        ("LENOVO-XCC-ALERT-MIB", "altDIMMPartNumber"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapPowerN.setStatus(
        ""
    )

lenovoSpTrapFanN = NotificationType(
    (1, 3, 6, 1, 4, 1, 19046, 11, 1, 158, 5, 0, 165)
)
lenovoSpTrapFanN.setObjects(
      *(("LENOVO-XCC-ALERT-MIB", "altDateTime"),
        ("LENOVO-XCC-ALERT-MIB", "altSpTxtId"),
        ("LENOVO-XCC-ALERT-MIB", "altSysUuid"),
        ("LENOVO-XCC-ALERT-MIB", "altSysSern"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgID"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgIDPrefix"),
        ("LENOVO-XCC-ALERT-MIB", "altPriority"),
        ("LENOVO-XCC-ALERT-MIB", "altMsgText"),
        ("LENOVO-XCC-ALERT-MIB", "altHostContact"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLocation"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRoomID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostRackID"),
        ("LENOVO-XCC-ALERT-MIB", "altHostLowestUpos"),
        ("LENOVO-XCC-ALERT-MIB", "altHostBladeBay"),
        ("LENOVO-XCC-ALERT-MIB", "altEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altServiceable"),
        ("LENOVO-XCC-ALERT-MIB", "altTest"),
        ("LENOVO-XCC-ALERT-MIB", "altFailingFRUs"),
        ("LENOVO-XCC-ALERT-MIB", "altHostMTM"),
        ("LENOVO-XCC-ALERT-MIB", "altAuxData"),
        ("LENOVO-XCC-ALERT-MIB", "altCommonEventID"),
        ("LENOVO-XCC-ALERT-MIB", "altEventType"),
        ("LENOVO-XCC-ALERT-MIB", "altDetectorID"))
)
if mibBuilder.loadTexts:
    lenovoSpTrapFanN.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LENOVO-XCC-ALERT-MIB",
    **{"lenovoXCCAlertMIB": lenovoXCCAlertMIB,
       "lenovoSpTrapTempC": lenovoSpTrapTempC,
       "lenovoSpTrapVoltC": lenovoSpTrapVoltC,
       "lenovoSpTrapPowerC": lenovoSpTrapPowerC,
       "lenovoSpTrapHdC": lenovoSpTrapHdC,
       "lenovoSpTrapRdpsC": lenovoSpTrapRdpsC,
       "lenovoSpTrapRdpsN": lenovoSpTrapRdpsN,
       "lenovoSpTrapFanC": lenovoSpTrapFanC,
       "lenovoSpTrapTempN": lenovoSpTrapTempN,
       "lenovoSpTrapVoltN": lenovoSpTrapVoltN,
       "lenovoSpTrapOsToS": lenovoSpTrapOsToS,
       "lenovoSpTrapAppS": lenovoSpTrapAppS,
       "lenovoSpTrapPoffS": lenovoSpTrapPoffS,
       "lenovoSpTrapPonS": lenovoSpTrapPonS,
       "lenovoSpTrapBootS": lenovoSpTrapBootS,
       "lenovoSpTrapLdrToS": lenovoSpTrapLdrToS,
       "lenovoSpTrapPFAS": lenovoSpTrapPFAS,
       "lenovoSpTrapRLogin": lenovoSpTrapRLogin,
       "lenovoSpTrapSysLogS": lenovoSpTrapSysLogS,
       "lenovoSpTrapIhcC": lenovoSpTrapIhcC,
       "lenovoSpTrapNwChangeS": lenovoSpTrapNwChangeS,
       "lenovoSpTrapCPUC": lenovoSpTrapCPUC,
       "lenovoSpTrapMemoryC": lenovoSpTrapMemoryC,
       "lenovoSpTrapCPUN": lenovoSpTrapCPUN,
       "lenovoSpTrapMemoryN": lenovoSpTrapMemoryN,
       "lenovoSpTrapHardwareC": lenovoSpTrapHardwareC,
       "lenovoSpTrapHardwareN": lenovoSpTrapHardwareN,
       "lenovoSpTrapPowerN": lenovoSpTrapPowerN,
       "lenovoSpTrapFanN": lenovoSpTrapFanN,
       "xcctrapg": xcctrapg,
       "altDateTime": altDateTime,
       "altSpTxtId": altSpTxtId,
       "altSysUuid": altSysUuid,
       "altSysSern": altSysSern,
       "altPriority": altPriority,
       "altMsgText": altMsgText,
       "altMsgID": altMsgID,
       "altMsgIDPrefix": altMsgIDPrefix,
       "altHostContact": altHostContact,
       "altHostLocation": altHostLocation,
       "altHostRoomID": altHostRoomID,
       "altHostRackID": altHostRackID,
       "altHostLowestUpos": altHostLowestUpos,
       "altHostBladeBay": altHostBladeBay,
       "altEventID": altEventID,
       "altServiceable": altServiceable,
       "altTest": altTest,
       "altFailingFRUs": altFailingFRUs,
       "altHostMTM": altHostMTM,
       "altAuxData": altAuxData,
       "altCommonEventID": altCommonEventID,
       "altEventType": altEventType,
       "altDetectorID": altDetectorID,
       "altDIMMPartNumber": altDIMMPartNumber}
)
