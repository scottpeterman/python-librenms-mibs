# SNMP MIB module (TROPIC-SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\1830\TROPIC-SHELF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:11 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(tnShelfMIB,
 tnShelfModules,
 tropicEmptyCard) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnShelfMIB",
    "tnShelfModules",
    "tropicEmptyCard")

(AluWdmExpectedCruType,
 AluWdmWtClkValues,
 TnCommand,
 TnRackSize,
 TropicCardCLEI,
 TropicCardManufacturingPartNumber,
 TropicCardSerialNumber,
 TropicLEDColorType,
 TropicLEDStateType,
 TropicShelfIndexType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmExpectedCruType",
    "AluWdmWtClkValues",
    "TnCommand",
    "TnRackSize",
    "TropicCardCLEI",
    "TropicCardManufacturingPartNumber",
    "TropicCardSerialNumber",
    "TropicLEDColorType",
    "TropicLEDStateType",
    "TropicShelfIndexType")


# MODULE-IDENTITY

tnShelfMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfMibModule.setRevisions(
        ("2023-02-03 12:00",
         "2023-01-27 12:00",
         "2022-02-25 12:00",
         "2022-02-11 12:00",
         "2022-01-28 12:00",
         "2021-11-26 12:00",
         "2021-06-25 12:00",
         "2021-05-21 12:00",
         "2021-03-05 12:00",
         "2021-02-12 12:00",
         "2020-10-02 12:00",
         "2020-08-07 12:00",
         "2020-07-24 12:00",
         "2020-04-03 12:00",
         "2020-03-27 12:00",
         "2020-03-13 12:00",
         "2020-02-28 12:00",
         "2019-12-20 12:00",
         "2019-11-01 12:00",
         "2019-09-13 12:00",
         "2019-09-06 12:00",
         "2019-07-05 12:00",
         "2019-04-19 12:00",
         "2018-11-26 12:00",
         "2018-11-07 12:00",
         "2018-10-26 12:00",
         "2018-10-19 12:00",
         "2018-10-10 12:00",
         "2018-07-20 12:00",
         "2018-02-23 12:00",
         "2018-01-19 12:00",
         "2017-12-15 12:00",
         "2017-10-13 12:00",
         "2017-09-08 12:00",
         "2017-07-07 12:00",
         "2017-06-30 12:00",
         "2017-06-14 12:00",
         "2017-05-26 12:00",
         "2017-03-24 12:00",
         "2017-01-20 12:00",
         "2016-11-16 12:00",
         "2016-10-19 12:00",
         "2016-10-04 12:00",
         "2016-06-03 12:00",
         "2016-05-06 12:00",
         "2016-02-01 12:00",
         "2015-12-24 12:00",
         "2015-12-07 12:00",
         "2015-10-20 12:00",
         "2015-09-30 12:00",
         "2015-08-25 12:00",
         "2015-08-06 12:00",
         "2015-07-31 12:00",
         "2015-06-04 12:00",
         "2014-09-12 12:00",
         "2014-07-25 12:00",
         "2014-02-26 12:00",
         "2013-12-15 12:00",
         "2013-11-14 12:00",
         "2013-09-06 12:00",
         "2013-08-07 12:00",
         "2013-05-21 12:00",
         "2013-04-29 12:00",
         "2012-12-14 12:00",
         "2012-09-25 12:00",
         "2012-09-06 12:00",
         "2012-03-29 12:00",
         "2012-02-23 12:00",
         "2012-02-06 12:00",
         "2011-04-07 12:00",
         "2011-02-06 12:00",
         "2010-12-16 12:00",
         "2010-10-12 12:00",
         "2010-10-04 12:00",
         "2010-09-13 12:00",
         "2010-06-28 12:00",
         "2010-06-04 12:00",
         "2009-12-11 12:00",
         "2009-09-15 12:00",
         "2009-09-09 12:00",
         "2009-07-15 12:00",
         "2009-06-07 12:00",
         "2009-05-19 12:00",
         "2009-04-27 12:00",
         "2008-06-05 12:00",
         "2008-05-29 12:00",
         "2008-04-05 12:00",
         "2008-03-06 12:00",
         "2008-02-16 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmExpectedAmpPF(TextualConvention, Integer32):
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
        *(("amps3dot7", 1),
          ("amps4dot1", 2),
          ("amps8dot5", 3),
          ("amps20dot6", 4),
          ("ampsdc30", 5),
          ("ampsac7", 6),
          ("na", 7))
    )



class TropicShelfInvAvailabilityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )



class TropicShelfInvCustomerInvField(TextualConvention, OctetString):
    status = "current"
    displayHint = "46a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )



class TropicShelfInvFiberType(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicShelfInvDcmSize(TextualConvention, OctetString):
    status = "current"
    displayHint = "3a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicShelfInvInsertionLoss(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicShelfInvInsertionLossSlope(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicShelfInvDispersionFit(TextualConvention, OctetString):
    status = "current"
    displayHint = "40a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class TropicShelfInvFiberLength(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicShelfInvPmd(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicShelfInvLatencyMismatch(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



# MIB Managed Objects in the order of their OIDs

_TnShelfConf_ObjectIdentity = ObjectIdentity
tnShelfConf = _TnShelfConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1)
)
_TnShelfGroups_ObjectIdentity = ObjectIdentity
tnShelfGroups = _TnShelfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1)
)
_TnShelfCompliances_ObjectIdentity = ObjectIdentity
tnShelfCompliances = _TnShelfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 2)
)
_TnShelfObjs_ObjectIdentity = ObjectIdentity
tnShelfObjs = _TnShelfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2)
)
_TnShelfBasics_ObjectIdentity = ObjectIdentity
tnShelfBasics = _TnShelfBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1)
)
_TnShelfTable_Object = MibTable
tnShelfTable = _TnShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfTable.setStatus("current")
_TnShelfEntry_Object = MibTableRow
tnShelfEntry = _TnShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1)
)
tnShelfEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnShelfEntry.setStatus("current")
_TnShelfIndex_Type = TropicShelfIndexType
_TnShelfIndex_Object = MibTableColumn
tnShelfIndex = _TnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 1),
    _TnShelfIndex_Type()
)
tnShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnShelfIndex.setStatus("current")


class _TnShelfName_Type(SnmpAdminString):
    """Custom type tnShelfName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnShelfName_Type.__name__ = "SnmpAdminString"
_TnShelfName_Object = MibTableColumn
tnShelfName = _TnShelfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 2),
    _TnShelfName_Type()
)
tnShelfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfName.setStatus("current")


class _TnShelfDescr_Type(SnmpAdminString):
    """Custom type tnShelfDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnShelfDescr_Type.__name__ = "SnmpAdminString"
_TnShelfDescr_Object = MibTableColumn
tnShelfDescr = _TnShelfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 3),
    _TnShelfDescr_Type()
)
tnShelfDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDescr.setStatus("current")
_TnShelfSerialNum_Type = Integer32
_TnShelfSerialNum_Object = MibTableColumn
tnShelfSerialNum = _TnShelfSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 4),
    _TnShelfSerialNum_Type()
)
tnShelfSerialNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfSerialNum.setStatus("current")


class _TnShelfProgrammedType_Type(ObjectIdentifier):
    """Custom type tnShelfProgrammedType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)


_TnShelfProgrammedType_Type.__name__ = "ObjectIdentifier"
_TnShelfProgrammedType_Object = MibTableColumn
tnShelfProgrammedType = _TnShelfProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 5),
    _TnShelfProgrammedType_Type()
)
tnShelfProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfProgrammedType.setStatus("current")


class _TnShelfPresentType_Type(ObjectIdentifier):
    """Custom type tnShelfPresentType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)


_TnShelfPresentType_Type.__name__ = "ObjectIdentifier"
_TnShelfPresentType_Object = MibTableColumn
tnShelfPresentType = _TnShelfPresentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 6),
    _TnShelfPresentType_Type()
)
tnShelfPresentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfPresentType.setStatus("current")


class _TnShelfActivitySwitch_Type(TnCommand):
    """Custom type tnShelfActivitySwitch based on TnCommand"""
    defaultValue = 1


_TnShelfActivitySwitch_Type.__name__ = "TnCommand"
_TnShelfActivitySwitch_Object = MibTableColumn
tnShelfActivitySwitch = _TnShelfActivitySwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 7),
    _TnShelfActivitySwitch_Type()
)
tnShelfActivitySwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfActivitySwitch.setStatus("current")


class _TnShelfLampTest_Type(TnCommand):
    """Custom type tnShelfLampTest based on TnCommand"""
    defaultValue = 1


_TnShelfLampTest_Type.__name__ = "TnCommand"
_TnShelfLampTest_Object = MibTableColumn
tnShelfLampTest = _TnShelfLampTest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 8),
    _TnShelfLampTest_Type()
)
tnShelfLampTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLampTest.setStatus("current")
_TnShelfMateCCReadyToProtect_Type = TruthValue
_TnShelfMateCCReadyToProtect_Object = MibTableColumn
tnShelfMateCCReadyToProtect = _TnShelfMateCCReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 9),
    _TnShelfMateCCReadyToProtect_Type()
)
tnShelfMateCCReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfMateCCReadyToProtect.setStatus("current")


class _TnShelfIsUnmanaged_Type(TruthValue):
    """Custom type tnShelfIsUnmanaged based on TruthValue"""
    defaultValue = 2


_TnShelfIsUnmanaged_Type.__name__ = "TruthValue"
_TnShelfIsUnmanaged_Object = MibTableColumn
tnShelfIsUnmanaged = _TnShelfIsUnmanaged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 10),
    _TnShelfIsUnmanaged_Type()
)
tnShelfIsUnmanaged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfIsUnmanaged.setStatus("current")


class _TnShelfExpectedAmps_Type(Integer32):
    """Custom type tnShelfExpectedAmps based on Integer32"""
    defaultValue = 5

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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("amps30", 1),
          ("amps50", 2),
          ("amps70", 3),
          ("amps20", 4),
          ("auto", 5),
          ("amps35", 6),
          ("amps5", 7),
          ("amps7", 8),
          ("amps100", 9),
          ("amps150", 10),
          ("amps60", 11),
          ("amps275", 12),
          ("amps2x50", 13),
          ("amps2x60", 14),
          ("amps3x60", 15),
          ("amps20dot6", 16),
          ("amps8dot5", 17),
          ("amps3dot7", 18),
          ("ampsMix", 19),
          ("amps4dot1", 20),
          ("ampsNa", 21),
          ("amps3x50", 22),
          ("amps320", 23),
          ("amps63", 24),
          ("amps16", 25),
          ("amps60a", 26))
    )


_TnShelfExpectedAmps_Type.__name__ = "Integer32"
_TnShelfExpectedAmps_Object = MibTableColumn
tnShelfExpectedAmps = _TnShelfExpectedAmps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 11),
    _TnShelfExpectedAmps_Type()
)
tnShelfExpectedAmps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedAmps.setStatus("current")


class _TnShelfSerialNumber_Type(SnmpAdminString):
    """Custom type tnShelfSerialNumber based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnShelfSerialNumber_Type.__name__ = "SnmpAdminString"
_TnShelfSerialNumber_Object = MibTableColumn
tnShelfSerialNumber = _TnShelfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 12),
    _TnShelfSerialNumber_Type()
)
tnShelfSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfSerialNumber.setStatus("current")


class _TnShelfAINS_Type(TruthValue):
    """Custom type tnShelfAINS based on TruthValue"""
    defaultValue = 2


_TnShelfAINS_Type.__name__ = "TruthValue"
_TnShelfAINS_Object = MibTableColumn
tnShelfAINS = _TnShelfAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 13),
    _TnShelfAINS_Type()
)
tnShelfAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfAINS.setStatus("current")
_TnShelfStatusLEDColor_Type = TropicLEDColorType
_TnShelfStatusLEDColor_Object = MibTableColumn
tnShelfStatusLEDColor = _TnShelfStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 15),
    _TnShelfStatusLEDColor_Type()
)
tnShelfStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfStatusLEDColor.setStatus("current")
_TnShelfStatusLEDState_Type = TropicLEDStateType
_TnShelfStatusLEDState_Object = MibTableColumn
tnShelfStatusLEDState = _TnShelfStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 16),
    _TnShelfStatusLEDState_Type()
)
tnShelfStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfStatusLEDState.setStatus("current")


class _TnShelfWTMode_Type(TruthValue):
    """Custom type tnShelfWTMode based on TruthValue"""
    defaultValue = 1


_TnShelfWTMode_Type.__name__ = "TruthValue"
_TnShelfWTMode_Object = MibTableColumn
tnShelfWTMode = _TnShelfWTMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 17),
    _TnShelfWTMode_Type()
)
tnShelfWTMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfWTMode.setStatus("current")


class _TnShelfActivityMt0cSwitch_Type(TnCommand):
    """Custom type tnShelfActivityMt0cSwitch based on TnCommand"""
    defaultValue = 1


_TnShelfActivityMt0cSwitch_Type.__name__ = "TnCommand"
_TnShelfActivityMt0cSwitch_Object = MibTableColumn
tnShelfActivityMt0cSwitch = _TnShelfActivityMt0cSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 18),
    _TnShelfActivityMt0cSwitch_Type()
)
tnShelfActivityMt0cSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfActivityMt0cSwitch.setStatus("current")
_TnShelfMateMt0cReadyToProtect_Type = TruthValue
_TnShelfMateMt0cReadyToProtect_Object = MibTableColumn
tnShelfMateMt0cReadyToProtect = _TnShelfMateMt0cReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 19),
    _TnShelfMateMt0cReadyToProtect_Type()
)
tnShelfMateMt0cReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfMateMt0cReadyToProtect.setStatus("current")


class _TnShelfExpectedPfa_Type(AluWdmExpectedAmpPF):
    """Custom type tnShelfExpectedPfa based on AluWdmExpectedAmpPF"""
    defaultValue = 1


_TnShelfExpectedPfa_Type.__name__ = "AluWdmExpectedAmpPF"
_TnShelfExpectedPfa_Object = MibTableColumn
tnShelfExpectedPfa = _TnShelfExpectedPfa_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 20),
    _TnShelfExpectedPfa_Type()
)
tnShelfExpectedPfa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedPfa.setStatus("current")


class _TnShelfExpectedPfb_Type(AluWdmExpectedAmpPF):
    """Custom type tnShelfExpectedPfb based on AluWdmExpectedAmpPF"""
    defaultValue = 3


_TnShelfExpectedPfb_Type.__name__ = "AluWdmExpectedAmpPF"
_TnShelfExpectedPfb_Object = MibTableColumn
tnShelfExpectedPfb = _TnShelfExpectedPfb_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 21),
    _TnShelfExpectedPfb_Type()
)
tnShelfExpectedPfb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedPfb.setStatus("current")


class _TnShelfHighVoltageThreshold_Type(Unsigned32):
    """Custom type tnShelfHighVoltageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8500),
    )


_TnShelfHighVoltageThreshold_Type.__name__ = "Unsigned32"
_TnShelfHighVoltageThreshold_Object = MibTableColumn
tnShelfHighVoltageThreshold = _TnShelfHighVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 22),
    _TnShelfHighVoltageThreshold_Type()
)
tnShelfHighVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThreshold.setUnits("1/100 volts")


class _TnShelfLowVoltageThreshold_Type(Unsigned32):
    """Custom type tnShelfLowVoltageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8500),
    )


_TnShelfLowVoltageThreshold_Type.__name__ = "Unsigned32"
_TnShelfLowVoltageThreshold_Object = MibTableColumn
tnShelfLowVoltageThreshold = _TnShelfLowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 23),
    _TnShelfLowVoltageThreshold_Type()
)
tnShelfLowVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThreshold.setUnits("1/100 volts")


class _TnShelfVoltageThresholdTol_Type(Unsigned32):
    """Custom type tnShelfVoltageThresholdTol based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 500),
    )


_TnShelfVoltageThresholdTol_Type.__name__ = "Unsigned32"
_TnShelfVoltageThresholdTol_Object = MibTableColumn
tnShelfVoltageThresholdTol = _TnShelfVoltageThresholdTol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 24),
    _TnShelfVoltageThresholdTol_Type()
)
tnShelfVoltageThresholdTol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTol.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTol.setUnits("1/100 volts")


class _TnShelfExpectedVolts_Type(Integer32):
    """Custom type tnShelfExpectedVolts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v48", 1),
          ("v60", 2))
    )


_TnShelfExpectedVolts_Type.__name__ = "Integer32"
_TnShelfExpectedVolts_Object = MibTableColumn
tnShelfExpectedVolts = _TnShelfExpectedVolts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 25),
    _TnShelfExpectedVolts_Type()
)
tnShelfExpectedVolts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedVolts.setStatus("current")


class _TnShelfMatrixSize_Type(Integer32):
    """Custom type tnShelfMatrixSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("ms1dot2T", 2),
          ("ms1dot9T", 3))
    )


_TnShelfMatrixSize_Type.__name__ = "Integer32"
_TnShelfMatrixSize_Object = MibTableColumn
tnShelfMatrixSize = _TnShelfMatrixSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 26),
    _TnShelfMatrixSize_Type()
)
tnShelfMatrixSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfMatrixSize.setStatus("current")


class _TnShelfVoltageFloor_Type(Unsigned32):
    """Custom type tnShelfVoltageFloor based on Unsigned32"""
    defaultValue = 3900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3900, 7200),
    )


_TnShelfVoltageFloor_Type.__name__ = "Unsigned32"
_TnShelfVoltageFloor_Object = MibTableColumn
tnShelfVoltageFloor = _TnShelfVoltageFloor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 27),
    _TnShelfVoltageFloor_Type()
)
tnShelfVoltageFloor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageFloor.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageFloor.setUnits("1/100 volts")
_TnShelfCalculatedLoad_Type = Unsigned32
_TnShelfCalculatedLoad_Object = MibTableColumn
tnShelfCalculatedLoad = _TnShelfCalculatedLoad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 28),
    _TnShelfCalculatedLoad_Type()
)
tnShelfCalculatedLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoad.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoad.setUnits("mA")


class _TnShelfClkSwitch_Type(AluWdmWtClkValues):
    """Custom type tnShelfClkSwitch based on AluWdmWtClkValues"""
    defaultValue = 1


_TnShelfClkSwitch_Type.__name__ = "AluWdmWtClkValues"
_TnShelfClkSwitch_Object = MibTableColumn
tnShelfClkSwitch = _TnShelfClkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 29),
    _TnShelfClkSwitch_Type()
)
tnShelfClkSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfClkSwitch.setStatus("current")


class _TnShelfExpectedVoltsAC_Type(Unsigned32):
    """Custom type tnShelfExpectedVoltsAC based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 264),
    )


_TnShelfExpectedVoltsAC_Type.__name__ = "Unsigned32"
_TnShelfExpectedVoltsAC_Object = MibTableColumn
tnShelfExpectedVoltsAC = _TnShelfExpectedVoltsAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 30),
    _TnShelfExpectedVoltsAC_Type()
)
tnShelfExpectedVoltsAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedVoltsAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfExpectedVoltsAC.setUnits("volts")


class _TnShelfHighVoltageThresholdAC_Type(Unsigned32):
    """Custom type tnShelfHighVoltageThresholdAC based on Unsigned32"""
    defaultValue = 11700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 28800),
    )


_TnShelfHighVoltageThresholdAC_Type.__name__ = "Unsigned32"
_TnShelfHighVoltageThresholdAC_Object = MibTableColumn
tnShelfHighVoltageThresholdAC = _TnShelfHighVoltageThresholdAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 31),
    _TnShelfHighVoltageThresholdAC_Type()
)
tnShelfHighVoltageThresholdAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThresholdAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThresholdAC.setUnits("1/100 volts")


class _TnShelfLowVoltageThresholdAC_Type(Unsigned32):
    """Custom type tnShelfLowVoltageThresholdAC based on Unsigned32"""
    defaultValue = 9900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 26400),
    )


_TnShelfLowVoltageThresholdAC_Type.__name__ = "Unsigned32"
_TnShelfLowVoltageThresholdAC_Object = MibTableColumn
tnShelfLowVoltageThresholdAC = _TnShelfLowVoltageThresholdAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 32),
    _TnShelfLowVoltageThresholdAC_Type()
)
tnShelfLowVoltageThresholdAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThresholdAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThresholdAC.setUnits("1/100 volts")


class _TnShelfVoltageFloorAC_Type(Unsigned32):
    """Custom type tnShelfVoltageFloorAC based on Unsigned32"""
    defaultValue = 9100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9000, 26400),
    )


_TnShelfVoltageFloorAC_Type.__name__ = "Unsigned32"
_TnShelfVoltageFloorAC_Object = MibTableColumn
tnShelfVoltageFloorAC = _TnShelfVoltageFloorAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 33),
    _TnShelfVoltageFloorAC_Type()
)
tnShelfVoltageFloorAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageFloorAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageFloorAC.setUnits("1/100 volts")


class _TnShelfExternalAcPower_Type(Unsigned32):
    """Custom type tnShelfExternalAcPower based on Unsigned32"""
    defaultValue = 0


_TnShelfExternalAcPower_Type.__name__ = "Unsigned32"
_TnShelfExternalAcPower_Object = MibTableColumn
tnShelfExternalAcPower = _TnShelfExternalAcPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 34),
    _TnShelfExternalAcPower_Type()
)
tnShelfExternalAcPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExternalAcPower.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfExternalAcPower.setUnits("1/10 watt")


class _TnShelfLoadWarningThreshold_Type(Unsigned32):
    """Custom type tnShelfLoadWarningThreshold based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1000),
    )


_TnShelfLoadWarningThreshold_Type.__name__ = "Unsigned32"
_TnShelfLoadWarningThreshold_Object = MibTableColumn
tnShelfLoadWarningThreshold = _TnShelfLoadWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 35),
    _TnShelfLoadWarningThreshold_Type()
)
tnShelfLoadWarningThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLoadWarningThreshold.setStatus("current")


class _TnShelfTimingSwitch_Type(Integer32):
    """Custom type tnShelfTimingSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timingSwitchAuto", 1),
          ("timingSwitchA", 2),
          ("timingSwitchB", 3))
    )


_TnShelfTimingSwitch_Type.__name__ = "Integer32"
_TnShelfTimingSwitch_Object = MibTableColumn
tnShelfTimingSwitch = _TnShelfTimingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 36),
    _TnShelfTimingSwitch_Type()
)
tnShelfTimingSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfTimingSwitch.setStatus("current")


class _TnShelfCalculatedLoadAC_Type(Unsigned32):
    """Custom type tnShelfCalculatedLoadAC based on Unsigned32"""
    defaultValue = 0


_TnShelfCalculatedLoadAC_Type.__name__ = "Unsigned32"
_TnShelfCalculatedLoadAC_Object = MibTableColumn
tnShelfCalculatedLoadAC = _TnShelfCalculatedLoadAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 37),
    _TnShelfCalculatedLoadAC_Type()
)
tnShelfCalculatedLoadAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoadAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfCalculatedLoadAC.setUnits("mA")


class _TnShelfPowerCapacity_Type(Unsigned32):
    """Custom type tnShelfPowerCapacity based on Unsigned32"""
    defaultValue = 0


_TnShelfPowerCapacity_Type.__name__ = "Unsigned32"
_TnShelfPowerCapacity_Object = MibTableColumn
tnShelfPowerCapacity = _TnShelfPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 38),
    _TnShelfPowerCapacity_Type()
)
tnShelfPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfPowerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfPowerCapacity.setUnits("1/10 watt")


class _TnShelfRemainingPowerCapacity_Type(Integer32):
    """Custom type tnShelfRemainingPowerCapacity based on Integer32"""
    defaultValue = 0


_TnShelfRemainingPowerCapacity_Type.__name__ = "Integer32"
_TnShelfRemainingPowerCapacity_Object = MibTableColumn
tnShelfRemainingPowerCapacity = _TnShelfRemainingPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 39),
    _TnShelfRemainingPowerCapacity_Type()
)
tnShelfRemainingPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRemainingPowerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfRemainingPowerCapacity.setUnits("1/10 watt")


class _TnShelfLockout_Type(Integer32):
    """Custom type tnShelfLockout based on Integer32"""
    defaultValue = 4

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
        *(("swc1", 1),
          ("swc2", 2),
          ("swc3", 3),
          ("clear", 4))
    )


_TnShelfLockout_Type.__name__ = "Integer32"
_TnShelfLockout_Object = MibTableColumn
tnShelfLockout = _TnShelfLockout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 40),
    _TnShelfLockout_Type()
)
tnShelfLockout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLockout.setStatus("current")


class _TnShelfFilterMonitorStatus_Type(TruthValue):
    """Custom type tnShelfFilterMonitorStatus based on TruthValue"""
    defaultValue = 2


_TnShelfFilterMonitorStatus_Type.__name__ = "TruthValue"
_TnShelfFilterMonitorStatus_Object = MibTableColumn
tnShelfFilterMonitorStatus = _TnShelfFilterMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 41),
    _TnShelfFilterMonitorStatus_Type()
)
tnShelfFilterMonitorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFilterMonitorStatus.setStatus("current")


class _TnShelfFilterInspectionInterval_Type(Unsigned32):
    """Custom type tnShelfFilterInspectionInterval based on Unsigned32"""
    defaultValue = 26

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 104),
    )


_TnShelfFilterInspectionInterval_Type.__name__ = "Unsigned32"
_TnShelfFilterInspectionInterval_Object = MibTableColumn
tnShelfFilterInspectionInterval = _TnShelfFilterInspectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 42),
    _TnShelfFilterInspectionInterval_Type()
)
tnShelfFilterInspectionInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFilterInspectionInterval.setStatus("current")


class _TnShelfFilterStartDate_Type(Unsigned32):
    """Custom type tnShelfFilterStartDate based on Unsigned32"""
    defaultValue = 426770689


_TnShelfFilterStartDate_Type.__name__ = "Unsigned32"
_TnShelfFilterStartDate_Object = MibTableColumn
tnShelfFilterStartDate = _TnShelfFilterStartDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 43),
    _TnShelfFilterStartDate_Type()
)
tnShelfFilterStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFilterStartDate.setStatus("current")
_TnShelfAlmProfName_Type = OctetString
_TnShelfAlmProfName_Object = MibTableColumn
tnShelfAlmProfName = _TnShelfAlmProfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 44),
    _TnShelfAlmProfName_Type()
)
tnShelfAlmProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfAlmProfName.setStatus("current")


class _TnShelfBranchPowerCap1_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap1 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap1_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap1_Object = MibTableColumn
tnShelfBranchPowerCap1 = _TnShelfBranchPowerCap1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 45),
    _TnShelfBranchPowerCap1_Type()
)
tnShelfBranchPowerCap1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap1.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap1.setUnits("1/10 watt")


class _TnShelfBranchPowerCap2_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap2 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap2_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap2_Object = MibTableColumn
tnShelfBranchPowerCap2 = _TnShelfBranchPowerCap2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 46),
    _TnShelfBranchPowerCap2_Type()
)
tnShelfBranchPowerCap2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap2.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap2.setUnits("1/10 watt")


class _TnShelfBranchPowerCap3_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap3 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap3_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap3_Object = MibTableColumn
tnShelfBranchPowerCap3 = _TnShelfBranchPowerCap3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 47),
    _TnShelfBranchPowerCap3_Type()
)
tnShelfBranchPowerCap3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap3.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap3.setUnits("1/10 watt")


class _TnShelfBranchPowerCap4_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap4 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap4_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap4_Object = MibTableColumn
tnShelfBranchPowerCap4 = _TnShelfBranchPowerCap4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 48),
    _TnShelfBranchPowerCap4_Type()
)
tnShelfBranchPowerCap4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap4.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap4.setUnits("1/10 watt")


class _TnShelfBranchPowerCap5_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap5 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap5_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap5_Object = MibTableColumn
tnShelfBranchPowerCap5 = _TnShelfBranchPowerCap5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 49),
    _TnShelfBranchPowerCap5_Type()
)
tnShelfBranchPowerCap5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap5.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap5.setUnits("1/10 watt")


class _TnShelfBranchPowerCap6_Type(Unsigned32):
    """Custom type tnShelfBranchPowerCap6 based on Unsigned32"""
    defaultValue = 0


_TnShelfBranchPowerCap6_Type.__name__ = "Unsigned32"
_TnShelfBranchPowerCap6_Object = MibTableColumn
tnShelfBranchPowerCap6 = _TnShelfBranchPowerCap6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 50),
    _TnShelfBranchPowerCap6_Type()
)
tnShelfBranchPowerCap6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap6.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchPowerCap6.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap1_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap1 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap1_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap1_Object = MibTableColumn
tnShelfBranchRemainingPwrCap1 = _TnShelfBranchRemainingPwrCap1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 51),
    _TnShelfBranchRemainingPwrCap1_Type()
)
tnShelfBranchRemainingPwrCap1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap1.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap1.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap2_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap2 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap2_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap2_Object = MibTableColumn
tnShelfBranchRemainingPwrCap2 = _TnShelfBranchRemainingPwrCap2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 52),
    _TnShelfBranchRemainingPwrCap2_Type()
)
tnShelfBranchRemainingPwrCap2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap2.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap2.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap3_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap3 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap3_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap3_Object = MibTableColumn
tnShelfBranchRemainingPwrCap3 = _TnShelfBranchRemainingPwrCap3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 53),
    _TnShelfBranchRemainingPwrCap3_Type()
)
tnShelfBranchRemainingPwrCap3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap3.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap3.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap4_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap4 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap4_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap4_Object = MibTableColumn
tnShelfBranchRemainingPwrCap4 = _TnShelfBranchRemainingPwrCap4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 54),
    _TnShelfBranchRemainingPwrCap4_Type()
)
tnShelfBranchRemainingPwrCap4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap4.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap4.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap5_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap5 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap5_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap5_Object = MibTableColumn
tnShelfBranchRemainingPwrCap5 = _TnShelfBranchRemainingPwrCap5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 55),
    _TnShelfBranchRemainingPwrCap5_Type()
)
tnShelfBranchRemainingPwrCap5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap5.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap5.setUnits("1/10 watt")


class _TnShelfBranchRemainingPwrCap6_Type(Integer32):
    """Custom type tnShelfBranchRemainingPwrCap6 based on Integer32"""
    defaultValue = 0


_TnShelfBranchRemainingPwrCap6_Type.__name__ = "Integer32"
_TnShelfBranchRemainingPwrCap6_Object = MibTableColumn
tnShelfBranchRemainingPwrCap6 = _TnShelfBranchRemainingPwrCap6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 56),
    _TnShelfBranchRemainingPwrCap6_Type()
)
tnShelfBranchRemainingPwrCap6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap6.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfBranchRemainingPwrCap6.setUnits("1/10 watt")


class _TnShelfFabricEQPStatus_Type(Integer32):
    """Custom type tnShelfFabricEQPStatus based on Integer32"""
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
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2),
          ("inUse", 3),
          ("trafficImpaired", 4),
          ("allTrafficLost", 5),
          ("reEvalInProg", 6),
          ("unknown", 7),
          ("loadBalancing", 8),
          ("balancingDegraded", 9),
          ("peerRedNotAvail", 10),
          ("peerRedInUse", 11),
          ("peerTrafficImpaired", 12),
          ("peerAllTrafficLost", 13),
          ("peerReEvalInProg", 14))
    )


_TnShelfFabricEQPStatus_Type.__name__ = "Integer32"
_TnShelfFabricEQPStatus_Object = MibTableColumn
tnShelfFabricEQPStatus = _TnShelfFabricEQPStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 57),
    _TnShelfFabricEQPStatus_Type()
)
tnShelfFabricEQPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricEQPStatus.setStatus("current")
_TnShelfFabricActivityState_Type = OctetString
_TnShelfFabricActivityState_Object = MibTableColumn
tnShelfFabricActivityState = _TnShelfFabricActivityState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 58),
    _TnShelfFabricActivityState_Type()
)
tnShelfFabricActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricActivityState.setStatus("current")
_TnShelfFabricFailures_Type = OctetString
_TnShelfFabricFailures_Object = MibTableColumn
tnShelfFabricFailures = _TnShelfFabricFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 59),
    _TnShelfFabricFailures_Type()
)
tnShelfFabricFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricFailures.setStatus("current")


class _TnShelfFabricUsage_Type(Integer32):
    """Custom type tnShelfFabricUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_TnShelfFabricUsage_Type.__name__ = "Integer32"
_TnShelfFabricUsage_Object = MibTableColumn
tnShelfFabricUsage = _TnShelfFabricUsage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 60),
    _TnShelfFabricUsage_Type()
)
tnShelfFabricUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricUsage.setStatus("current")
_TnShelfFabricEqpsLEDColor_Type = OctetString
_TnShelfFabricEqpsLEDColor_Object = MibTableColumn
tnShelfFabricEqpsLEDColor = _TnShelfFabricEqpsLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 61),
    _TnShelfFabricEqpsLEDColor_Type()
)
tnShelfFabricEqpsLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricEqpsLEDColor.setStatus("current")


class _TnShelfFabricReadyToProtect_Type(Integer32):
    """Custom type tnShelfFabricReadyToProtect based on Integer32"""
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
        *(("yes", 1),
          ("partially", 2),
          ("no", 3),
          ("invalid", 4))
    )


_TnShelfFabricReadyToProtect_Type.__name__ = "Integer32"
_TnShelfFabricReadyToProtect_Object = MibTableColumn
tnShelfFabricReadyToProtect = _TnShelfFabricReadyToProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 62),
    _TnShelfFabricReadyToProtect_Type()
)
tnShelfFabricReadyToProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfFabricReadyToProtect.setStatus("current")


class _TnShelfRackType_Type(TnRackSize):
    """Custom type tnShelfRackType based on TnRackSize"""
    defaultValue = 1


_TnShelfRackType_Type.__name__ = "TnRackSize"
_TnShelfRackType_Object = MibTableColumn
tnShelfRackType = _TnShelfRackType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 63),
    _TnShelfRackType_Type()
)
tnShelfRackType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRackType.setStatus("current")


class _TnShelfInventoryAction_Type(Integer32):
    """Custom type tnShelfInventoryAction based on Integer32"""
    defaultValue = 1

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
        *(("unInitialized", 1),
          ("toDb", 2),
          ("toHw", 3),
          ("ready", 4),
          ("fail", 5))
    )


_TnShelfInventoryAction_Type.__name__ = "Integer32"
_TnShelfInventoryAction_Object = MibTableColumn
tnShelfInventoryAction = _TnShelfInventoryAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 64),
    _TnShelfInventoryAction_Type()
)
tnShelfInventoryAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfInventoryAction.setStatus("current")


class _TnShelfFilterAction_Type(Integer32):
    """Custom type tnShelfFilterAction based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 1),
          ("ready", 2),
          ("fail", 3),
          ("tune", 4),
          ("tuneInProgress", 5),
          ("tuneSuccess", 6),
          ("tuneFail", 7),
          ("check", 8),
          ("checkInProgress", 9),
          ("checkSuccess", 10),
          ("checkFail", 11))
    )


_TnShelfFilterAction_Type.__name__ = "Integer32"
_TnShelfFilterAction_Object = MibTableColumn
tnShelfFilterAction = _TnShelfFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 65),
    _TnShelfFilterAction_Type()
)
tnShelfFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFilterAction.setStatus("current")


class _TnShelfExpectedCruA_Type(AluWdmExpectedCruType):
    """Custom type tnShelfExpectedCruA based on AluWdmExpectedCruType"""
    defaultValue = 1


_TnShelfExpectedCruA_Type.__name__ = "AluWdmExpectedCruType"
_TnShelfExpectedCruA_Object = MibTableColumn
tnShelfExpectedCruA = _TnShelfExpectedCruA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 66),
    _TnShelfExpectedCruA_Type()
)
tnShelfExpectedCruA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedCruA.setStatus("current")


class _TnShelfExpectedCruB_Type(AluWdmExpectedCruType):
    """Custom type tnShelfExpectedCruB based on AluWdmExpectedCruType"""
    defaultValue = 1


_TnShelfExpectedCruB_Type.__name__ = "AluWdmExpectedCruType"
_TnShelfExpectedCruB_Object = MibTableColumn
tnShelfExpectedCruB = _TnShelfExpectedCruB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 67),
    _TnShelfExpectedCruB_Type()
)
tnShelfExpectedCruB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedCruB.setStatus("current")


class _TnShelfPanelTimingPort_Type(TruthValue):
    """Custom type tnShelfPanelTimingPort based on TruthValue"""
    defaultValue = 1


_TnShelfPanelTimingPort_Type.__name__ = "TruthValue"
_TnShelfPanelTimingPort_Object = MibTableColumn
tnShelfPanelTimingPort = _TnShelfPanelTimingPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 68),
    _TnShelfPanelTimingPort_Type()
)
tnShelfPanelTimingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPanelTimingPort.setStatus("current")


class _TnShelfDelegateFCRUSlot_Type(Unsigned32):
    """Custom type tnShelfDelegateFCRUSlot based on Unsigned32"""
    defaultValue = 0


_TnShelfDelegateFCRUSlot_Type.__name__ = "Unsigned32"
_TnShelfDelegateFCRUSlot_Object = MibTableColumn
tnShelfDelegateFCRUSlot = _TnShelfDelegateFCRUSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 69),
    _TnShelfDelegateFCRUSlot_Type()
)
tnShelfDelegateFCRUSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDelegateFCRUSlot.setStatus("current")


class _TnShelfUID_Type(Integer32):
    """Custom type tnShelfUID based on Integer32"""
    defaultValue = 2

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
        *(("on", 1),
          ("off", 2),
          ("active", 3),
          ("inactive", 4))
    )


_TnShelfUID_Type.__name__ = "Integer32"
_TnShelfUID_Object = MibTableColumn
tnShelfUID = _TnShelfUID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 70),
    _TnShelfUID_Type()
)
tnShelfUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfUID.setStatus("current")
_TnShelfUIDStatusLEDState_Type = TropicLEDStateType
_TnShelfUIDStatusLEDState_Object = MibTableColumn
tnShelfUIDStatusLEDState = _TnShelfUIDStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 71),
    _TnShelfUIDStatusLEDState_Type()
)
tnShelfUIDStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfUIDStatusLEDState.setStatus("current")


class _TnShelfMTXSIZE_Type(Integer32):
    """Custom type tnShelfMTXSIZE based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("oTN9T6", 2),
          ("oTN4T8", 3),
          ("oTN1T6", 4),
          ("oTN24T", 5),
          ("pKT9T6PTP", 6),
          ("unknown", 7),
          ("oTN24TC", 8),
          ("oTN4T", 9),
          ("oTN12T", 10),
          ("oTN48TPrim", 11),
          ("oTN48TSec", 12))
    )


_TnShelfMTXSIZE_Type.__name__ = "Integer32"
_TnShelfMTXSIZE_Object = MibTableColumn
tnShelfMTXSIZE = _TnShelfMTXSIZE_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 72),
    _TnShelfMTXSIZE_Type()
)
tnShelfMTXSIZE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfMTXSIZE.setStatus("current")


class _TnShelfRMNMTXCAP_Type(Integer32):
    """Custom type tnShelfRMNMTXCAP based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9600),
    )


_TnShelfRMNMTXCAP_Type.__name__ = "Integer32"
_TnShelfRMNMTXCAP_Object = MibTableColumn
tnShelfRMNMTXCAP = _TnShelfRMNMTXCAP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 73),
    _TnShelfRMNMTXCAP_Type()
)
tnShelfRMNMTXCAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRMNMTXCAP.setStatus("current")
_TnShelfUIDStatusLEDColor_Type = TropicLEDColorType
_TnShelfUIDStatusLEDColor_Object = MibTableColumn
tnShelfUIDStatusLEDColor = _TnShelfUIDStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 74),
    _TnShelfUIDStatusLEDColor_Type()
)
tnShelfUIDStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfUIDStatusLEDColor.setStatus("current")


class _TnShelfFanMode_Type(Integer32):
    """Custom type tnShelfFanMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cool", 1),
          ("quite", 2))
    )


_TnShelfFanMode_Type.__name__ = "Integer32"
_TnShelfFanMode_Object = MibTableColumn
tnShelfFanMode = _TnShelfFanMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 75),
    _TnShelfFanMode_Type()
)
tnShelfFanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFanMode.setStatus("current")


class _TnShelfExpectedVoltsHVDC_Type(Unsigned32):
    """Custom type tnShelfExpectedVoltsHVDC based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(240, 333),
    )


_TnShelfExpectedVoltsHVDC_Type.__name__ = "Unsigned32"
_TnShelfExpectedVoltsHVDC_Object = MibTableColumn
tnShelfExpectedVoltsHVDC = _TnShelfExpectedVoltsHVDC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 76),
    _TnShelfExpectedVoltsHVDC_Type()
)
tnShelfExpectedVoltsHVDC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfExpectedVoltsHVDC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfExpectedVoltsHVDC.setUnits("volts")


class _TnShelfHighVoltageThresholdHVDC_Type(Unsigned32):
    """Custom type tnShelfHighVoltageThresholdHVDC based on Unsigned32"""
    defaultValue = 26880

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25200, 40000),
    )


_TnShelfHighVoltageThresholdHVDC_Type.__name__ = "Unsigned32"
_TnShelfHighVoltageThresholdHVDC_Object = MibTableColumn
tnShelfHighVoltageThresholdHVDC = _TnShelfHighVoltageThresholdHVDC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 77),
    _TnShelfHighVoltageThresholdHVDC_Type()
)
tnShelfHighVoltageThresholdHVDC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThresholdHVDC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfHighVoltageThresholdHVDC.setUnits("1/100 volts")


class _TnShelfLowVoltageThresholdHVDC_Type(Unsigned32):
    """Custom type tnShelfLowVoltageThresholdHVDC based on Unsigned32"""
    defaultValue = 19200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 31500),
    )


_TnShelfLowVoltageThresholdHVDC_Type.__name__ = "Unsigned32"
_TnShelfLowVoltageThresholdHVDC_Object = MibTableColumn
tnShelfLowVoltageThresholdHVDC = _TnShelfLowVoltageThresholdHVDC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 78),
    _TnShelfLowVoltageThresholdHVDC_Type()
)
tnShelfLowVoltageThresholdHVDC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThresholdHVDC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfLowVoltageThresholdHVDC.setUnits("1/100 volts")


class _TnShelfVoltageThresholdTolHVDC_Type(Unsigned32):
    """Custom type tnShelfVoltageThresholdTolHVDC based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4000),
    )


_TnShelfVoltageThresholdTolHVDC_Type.__name__ = "Unsigned32"
_TnShelfVoltageThresholdTolHVDC_Object = MibTableColumn
tnShelfVoltageThresholdTolHVDC = _TnShelfVoltageThresholdTolHVDC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 79),
    _TnShelfVoltageThresholdTolHVDC_Type()
)
tnShelfVoltageThresholdTolHVDC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTolHVDC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTolHVDC.setUnits("1/100 volts")


class _TnShelfVoltageFloorHVDC_Type(Unsigned32):
    """Custom type tnShelfVoltageFloorHVDC based on Unsigned32"""
    defaultValue = 18000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16000, 48000),
    )


_TnShelfVoltageFloorHVDC_Type.__name__ = "Unsigned32"
_TnShelfVoltageFloorHVDC_Object = MibTableColumn
tnShelfVoltageFloorHVDC = _TnShelfVoltageFloorHVDC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 80),
    _TnShelfVoltageFloorHVDC_Type()
)
tnShelfVoltageFloorHVDC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageFloorHVDC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageFloorHVDC.setUnits("1/100 volts")


class _TnShelfVoltageThresholdTolAC_Type(Unsigned32):
    """Custom type tnShelfVoltageThresholdTolAC based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1100),
    )


_TnShelfVoltageThresholdTolAC_Type.__name__ = "Unsigned32"
_TnShelfVoltageThresholdTolAC_Object = MibTableColumn
tnShelfVoltageThresholdTolAC = _TnShelfVoltageThresholdTolAC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 81),
    _TnShelfVoltageThresholdTolAC_Type()
)
tnShelfVoltageThresholdTolAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTolAC.setStatus("current")
if mibBuilder.loadTexts:
    tnShelfVoltageThresholdTolAC.setUnits("1/100 volts")


class _TnShelfTsiFreeze_Type(Integer32):
    """Custom type tnShelfTsiFreeze based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_TnShelfTsiFreeze_Type.__name__ = "Integer32"
_TnShelfTsiFreeze_Object = MibTableColumn
tnShelfTsiFreeze = _TnShelfTsiFreeze_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 82),
    _TnShelfTsiFreeze_Type()
)
tnShelfTsiFreeze.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfTsiFreeze.setStatus("current")


class _TnShelfPosition_Type(SnmpAdminString):
    """Custom type tnShelfPosition based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TnShelfPosition_Type.__name__ = "SnmpAdminString"
_TnShelfPosition_Object = MibTableColumn
tnShelfPosition = _TnShelfPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 84),
    _TnShelfPosition_Type()
)
tnShelfPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPosition.setStatus("current")


class _TnShelfLifeCycleState_Type(SnmpAdminString):
    """Custom type tnShelfLifeCycleState based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnShelfLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnShelfLifeCycleState_Object = MibTableColumn
tnShelfLifeCycleState = _TnShelfLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 85),
    _TnShelfLifeCycleState_Type()
)
tnShelfLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfLifeCycleState.setStatus("current")


class _TnShelfDueDate_Type(SnmpAdminString):
    """Custom type tnShelfDueDate based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnShelfDueDate_Type.__name__ = "SnmpAdminString"
_TnShelfDueDate_Object = MibTableColumn
tnShelfDueDate = _TnShelfDueDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 86),
    _TnShelfDueDate_Type()
)
tnShelfDueDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDueDate.setStatus("current")


class _TnShelfRackLocation_Type(SnmpAdminString):
    """Custom type tnShelfRackLocation based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnShelfRackLocation_Type.__name__ = "SnmpAdminString"
_TnShelfRackLocation_Object = MibTableColumn
tnShelfRackLocation = _TnShelfRackLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 87),
    _TnShelfRackLocation_Type()
)
tnShelfRackLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRackLocation.setStatus("current")
_TnShelfXpdrNumber_Type = Integer32
_TnShelfXpdrNumber_Object = MibTableColumn
tnShelfXpdrNumber = _TnShelfXpdrNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 88),
    _TnShelfXpdrNumber_Type()
)
tnShelfXpdrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfXpdrNumber.setStatus("current")
_TnShelfCoupledNumber_Type = Integer32
_TnShelfCoupledNumber_Object = MibTableColumn
tnShelfCoupledNumber = _TnShelfCoupledNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 89),
    _TnShelfCoupledNumber_Type()
)
tnShelfCoupledNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfCoupledNumber.setStatus("current")


class _TnShelfCoupledCmd_Type(Integer32):
    """Custom type tnShelfCoupledCmd based on Integer32"""
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
        *(("config", 1),
          ("upgrade", 2),
          ("commit", 3),
          ("cancel", 4))
    )


_TnShelfCoupledCmd_Type.__name__ = "Integer32"
_TnShelfCoupledCmd_Object = MibTableColumn
tnShelfCoupledCmd = _TnShelfCoupledCmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 90),
    _TnShelfCoupledCmd_Type()
)
tnShelfCoupledCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfCoupledCmd.setStatus("current")


class _TnShelfCustomerLifeCycleState_Type(SnmpAdminString):
    """Custom type tnShelfCustomerLifeCycleState based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnShelfCustomerLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnShelfCustomerLifeCycleState_Object = MibTableColumn
tnShelfCustomerLifeCycleState = _TnShelfCustomerLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 91),
    _TnShelfCustomerLifeCycleState_Type()
)
tnShelfCustomerLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfCustomerLifeCycleState.setStatus("current")


class _TnShelfXponderLifeCycleState_Type(SnmpAdminString):
    """Custom type tnShelfXponderLifeCycleState based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TnShelfXponderLifeCycleState_Type.__name__ = "SnmpAdminString"
_TnShelfXponderLifeCycleState_Object = MibTableColumn
tnShelfXponderLifeCycleState = _TnShelfXponderLifeCycleState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 92),
    _TnShelfXponderLifeCycleState_Type()
)
tnShelfXponderLifeCycleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfXponderLifeCycleState.setStatus("current")


class _TnShelfCouplingState_Type(Integer32):
    """Custom type tnShelfCouplingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("intermediate", 2),
          ("committed", 3))
    )


_TnShelfCouplingState_Type.__name__ = "Integer32"
_TnShelfCouplingState_Object = MibTableColumn
tnShelfCouplingState = _TnShelfCouplingState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 93),
    _TnShelfCouplingState_Type()
)
tnShelfCouplingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfCouplingState.setStatus("current")


class _TnShelfPowerFeed_Type(Integer32):
    """Custom type tnShelfPowerFeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uniform", 1),
          ("mixed", 2))
    )


_TnShelfPowerFeed_Type.__name__ = "Integer32"
_TnShelfPowerFeed_Object = MibTableColumn
tnShelfPowerFeed = _TnShelfPowerFeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 94),
    _TnShelfPowerFeed_Type()
)
tnShelfPowerFeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPowerFeed.setStatus("current")
_TnShelfPfaExpectedVolts_Type = Unsigned32
_TnShelfPfaExpectedVolts_Object = MibTableColumn
tnShelfPfaExpectedVolts = _TnShelfPfaExpectedVolts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 95),
    _TnShelfPfaExpectedVolts_Type()
)
tnShelfPfaExpectedVolts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfaExpectedVolts.setStatus("current")
_TnShelfPfaLowVoltageThreshold_Type = Unsigned32
_TnShelfPfaLowVoltageThreshold_Object = MibTableColumn
tnShelfPfaLowVoltageThreshold = _TnShelfPfaLowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 96),
    _TnShelfPfaLowVoltageThreshold_Type()
)
tnShelfPfaLowVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfaLowVoltageThreshold.setStatus("current")
_TnShelfPfaHighVoltageThreshold_Type = Unsigned32
_TnShelfPfaHighVoltageThreshold_Object = MibTableColumn
tnShelfPfaHighVoltageThreshold = _TnShelfPfaHighVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 97),
    _TnShelfPfaHighVoltageThreshold_Type()
)
tnShelfPfaHighVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfaHighVoltageThreshold.setStatus("current")
_TnShelfPfaVoltageThresholdTol_Type = Unsigned32
_TnShelfPfaVoltageThresholdTol_Object = MibTableColumn
tnShelfPfaVoltageThresholdTol = _TnShelfPfaVoltageThresholdTol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 98),
    _TnShelfPfaVoltageThresholdTol_Type()
)
tnShelfPfaVoltageThresholdTol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfaVoltageThresholdTol.setStatus("current")
_TnShelfPfbExpectedVolts_Type = Unsigned32
_TnShelfPfbExpectedVolts_Object = MibTableColumn
tnShelfPfbExpectedVolts = _TnShelfPfbExpectedVolts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 99),
    _TnShelfPfbExpectedVolts_Type()
)
tnShelfPfbExpectedVolts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfbExpectedVolts.setStatus("current")
_TnShelfPfbLowVoltageThreshold_Type = Unsigned32
_TnShelfPfbLowVoltageThreshold_Object = MibTableColumn
tnShelfPfbLowVoltageThreshold = _TnShelfPfbLowVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 100),
    _TnShelfPfbLowVoltageThreshold_Type()
)
tnShelfPfbLowVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfbLowVoltageThreshold.setStatus("current")
_TnShelfPfbHighVoltageThreshold_Type = Unsigned32
_TnShelfPfbHighVoltageThreshold_Object = MibTableColumn
tnShelfPfbHighVoltageThreshold = _TnShelfPfbHighVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 101),
    _TnShelfPfbHighVoltageThreshold_Type()
)
tnShelfPfbHighVoltageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfbHighVoltageThreshold.setStatus("current")
_TnShelfPfbVoltageThresholdTol_Type = Unsigned32
_TnShelfPfbVoltageThresholdTol_Object = MibTableColumn
tnShelfPfbVoltageThresholdTol = _TnShelfPfbVoltageThresholdTol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 102),
    _TnShelfPfbVoltageThresholdTol_Type()
)
tnShelfPfbVoltageThresholdTol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfPfbVoltageThresholdTol.setStatus("current")
_TnShelfTotal_Type = Integer32
_TnShelfTotal_Object = MibScalar
tnShelfTotal = _TnShelfTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 2),
    _TnShelfTotal_Type()
)
tnShelfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfTotal.setStatus("current")
_TnShelfRiDataTable_Object = MibTable
tnShelfRiDataTable = _TnShelfRiDataTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnShelfRiDataTable.setStatus("current")
_TnShelfRiDataEntry_Object = MibTableRow
tnShelfRiDataEntry = _TnShelfRiDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1)
)
tnShelfRiDataEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnShelfRiDataEntry.setStatus("current")


class _TnShelfRiCompanyID_Type(SnmpAdminString):
    """Custom type tnShelfRiCompanyID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiCompanyID_Type.__name__ = "SnmpAdminString"
_TnShelfRiCompanyID_Object = MibTableColumn
tnShelfRiCompanyID = _TnShelfRiCompanyID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 1),
    _TnShelfRiCompanyID_Type()
)
tnShelfRiCompanyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiCompanyID.setStatus("current")


class _TnShelfRiMnemonic_Type(SnmpAdminString):
    """Custom type tnShelfRiMnemonic based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiMnemonic_Type.__name__ = "SnmpAdminString"
_TnShelfRiMnemonic_Object = MibTableColumn
tnShelfRiMnemonic = _TnShelfRiMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 2),
    _TnShelfRiMnemonic_Type()
)
tnShelfRiMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiMnemonic.setStatus("current")


class _TnShelfRiCLEI_Type(TropicCardCLEI):
    """Custom type tnShelfRiCLEI based on TropicCardCLEI"""
    defaultValue = OctetString("")


_TnShelfRiCLEI_Type.__name__ = "TropicCardCLEI"
_TnShelfRiCLEI_Object = MibTableColumn
tnShelfRiCLEI = _TnShelfRiCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 3),
    _TnShelfRiCLEI_Type()
)
tnShelfRiCLEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRiCLEI.setStatus("current")


class _TnShelfRiManufacturingPartNumber_Type(TropicCardManufacturingPartNumber):
    """Custom type tnShelfRiManufacturingPartNumber based on TropicCardManufacturingPartNumber"""
    defaultValue = OctetString("")


_TnShelfRiManufacturingPartNumber_Type.__name__ = "TropicCardManufacturingPartNumber"
_TnShelfRiManufacturingPartNumber_Object = MibTableColumn
tnShelfRiManufacturingPartNumber = _TnShelfRiManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 4),
    _TnShelfRiManufacturingPartNumber_Type()
)
tnShelfRiManufacturingPartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRiManufacturingPartNumber.setStatus("current")


class _TnShelfRiSWPartNum_Type(SnmpAdminString):
    """Custom type tnShelfRiSWPartNum based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiSWPartNum_Type.__name__ = "SnmpAdminString"
_TnShelfRiSWPartNum_Object = MibTableColumn
tnShelfRiSWPartNum = _TnShelfRiSWPartNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 5),
    _TnShelfRiSWPartNum_Type()
)
tnShelfRiSWPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiSWPartNum.setStatus("current")


class _TnShelfRiFactoryID_Type(SnmpAdminString):
    """Custom type tnShelfRiFactoryID based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiFactoryID_Type.__name__ = "SnmpAdminString"
_TnShelfRiFactoryID_Object = MibTableColumn
tnShelfRiFactoryID = _TnShelfRiFactoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 6),
    _TnShelfRiFactoryID_Type()
)
tnShelfRiFactoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiFactoryID.setStatus("current")


class _TnShelfRiSerialNumber_Type(TropicCardSerialNumber):
    """Custom type tnShelfRiSerialNumber based on TropicCardSerialNumber"""
    defaultValue = OctetString("")


_TnShelfRiSerialNumber_Type.__name__ = "TropicCardSerialNumber"
_TnShelfRiSerialNumber_Object = MibTableColumn
tnShelfRiSerialNumber = _TnShelfRiSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 7),
    _TnShelfRiSerialNumber_Type()
)
tnShelfRiSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRiSerialNumber.setStatus("current")


class _TnShelfRiDate_Type(SnmpAdminString):
    """Custom type tnShelfRiDate based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiDate_Type.__name__ = "SnmpAdminString"
_TnShelfRiDate_Object = MibTableColumn
tnShelfRiDate = _TnShelfRiDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 8),
    _TnShelfRiDate_Type()
)
tnShelfRiDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiDate.setStatus("current")


class _TnShelfRiExtraData_Type(SnmpAdminString):
    """Custom type tnShelfRiExtraData based on SnmpAdminString"""
    defaultValue = OctetString("")


_TnShelfRiExtraData_Type.__name__ = "SnmpAdminString"
_TnShelfRiExtraData_Object = MibTableColumn
tnShelfRiExtraData = _TnShelfRiExtraData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 3, 1, 9),
    _TnShelfRiExtraData_Type()
)
tnShelfRiExtraData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfRiExtraData.setStatus("current")
_TnShelfInvTable_Object = MibTable
tnShelfInvTable = _TnShelfInvTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnShelfInvTable.setStatus("current")
_TnShelfInvEntry_Object = MibTableRow
tnShelfInvEntry = _TnShelfInvEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1)
)
tnShelfInvEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnShelfInvEntry.setStatus("current")
_TnShelfInvInvStatus_Type = TropicShelfInvAvailabilityStatus
_TnShelfInvInvStatus_Object = MibTableColumn
tnShelfInvInvStatus = _TnShelfInvInvStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 1),
    _TnShelfInvInvStatus_Type()
)
tnShelfInvInvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvInvStatus.setStatus("current")
_TnShelfInvCustInvField_Type = TropicShelfInvCustomerInvField
_TnShelfInvCustInvField_Object = MibTableColumn
tnShelfInvCustInvField = _TnShelfInvCustInvField_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 2),
    _TnShelfInvCustInvField_Type()
)
tnShelfInvCustInvField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvCustInvField.setStatus("current")
_TnShelfInvFiberType_Type = TropicShelfInvFiberType
_TnShelfInvFiberType_Object = MibTableColumn
tnShelfInvFiberType = _TnShelfInvFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 3),
    _TnShelfInvFiberType_Type()
)
tnShelfInvFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvFiberType.setStatus("current")
_TnShelfInvDcmSize_Type = TropicShelfInvDcmSize
_TnShelfInvDcmSize_Object = MibTableColumn
tnShelfInvDcmSize = _TnShelfInvDcmSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 4),
    _TnShelfInvDcmSize_Type()
)
tnShelfInvDcmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvDcmSize.setStatus("current")
_TnShelfInvAvgInsertionLoss_Type = TropicShelfInvInsertionLoss
_TnShelfInvAvgInsertionLoss_Object = MibTableColumn
tnShelfInvAvgInsertionLoss = _TnShelfInvAvgInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 5),
    _TnShelfInvAvgInsertionLoss_Type()
)
tnShelfInvAvgInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvAvgInsertionLoss.setStatus("current")
_TnShelfInvInsertionLossSlope_Type = TropicShelfInvInsertionLossSlope
_TnShelfInvInsertionLossSlope_Object = MibTableColumn
tnShelfInvInsertionLossSlope = _TnShelfInvInsertionLossSlope_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 6),
    _TnShelfInvInsertionLossSlope_Type()
)
tnShelfInvInsertionLossSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvInsertionLossSlope.setStatus("current")
_TnShelfInvTotalDispFit_Type = TropicShelfInvDispersionFit
_TnShelfInvTotalDispFit_Object = MibTableColumn
tnShelfInvTotalDispFit = _TnShelfInvTotalDispFit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 7),
    _TnShelfInvTotalDispFit_Type()
)
tnShelfInvTotalDispFit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvTotalDispFit.setStatus("current")
_TnShelfInvDispFiberLength_Type = TropicShelfInvFiberLength
_TnShelfInvDispFiberLength_Object = MibTableColumn
tnShelfInvDispFiberLength = _TnShelfInvDispFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 8),
    _TnShelfInvDispFiberLength_Type()
)
tnShelfInvDispFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvDispFiberLength.setStatus("current")
_TnShelfInvPmd_Type = TropicShelfInvPmd
_TnShelfInvPmd_Object = MibTableColumn
tnShelfInvPmd = _TnShelfInvPmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 9),
    _TnShelfInvPmd_Type()
)
tnShelfInvPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvPmd.setStatus("current")
_TnShelfInvLatencyMismatch_Type = TropicShelfInvLatencyMismatch
_TnShelfInvLatencyMismatch_Object = MibTableColumn
tnShelfInvLatencyMismatch = _TnShelfInvLatencyMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 4, 1, 10),
    _TnShelfInvLatencyMismatch_Type()
)
tnShelfInvLatencyMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfInvLatencyMismatch.setStatus("current")
_TnMultiShelfTable_Object = MibTable
tnMultiShelfTable = _TnMultiShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnMultiShelfTable.setStatus("current")
_TnMultiShelfEntry_Object = MibTableRow
tnMultiShelfEntry = _TnMultiShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 5, 1)
)
tnMultiShelfEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnMultiShelfIndex"),
)
if mibBuilder.loadTexts:
    tnMultiShelfEntry.setStatus("current")


class _TnMultiShelfIndex_Type(Unsigned32):
    """Custom type tnMultiShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 31),
    )


_TnMultiShelfIndex_Type.__name__ = "Unsigned32"
_TnMultiShelfIndex_Object = MibTableColumn
tnMultiShelfIndex = _TnMultiShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 5, 1, 1),
    _TnMultiShelfIndex_Type()
)
tnMultiShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMultiShelfIndex.setStatus("current")


class _TnMultiShelfSerialNumber_Type(SnmpAdminString):
    """Custom type tnMultiShelfSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnMultiShelfSerialNumber_Type.__name__ = "SnmpAdminString"
_TnMultiShelfSerialNumber_Object = MibTableColumn
tnMultiShelfSerialNumber = _TnMultiShelfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 5, 1, 2),
    _TnMultiShelfSerialNumber_Type()
)
tnMultiShelfSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMultiShelfSerialNumber.setStatus("current")
_TnMultiShelfRowStatus_Type = RowStatus
_TnMultiShelfRowStatus_Object = MibTableColumn
tnMultiShelfRowStatus = _TnMultiShelfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 5, 1, 3),
    _TnMultiShelfRowStatus_Type()
)
tnMultiShelfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnMultiShelfRowStatus.setStatus("current")
_TnShelfDisplayTable_Object = MibTable
tnShelfDisplayTable = _TnShelfDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnShelfDisplayTable.setStatus("current")
_TnShelfDisplayEntry_Object = MibTableRow
tnShelfDisplayEntry = _TnShelfDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1)
)
tnShelfDisplayEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnShelfDisplayEntry.setStatus("current")


class _TnShelfDisplayIdType_Type(Integer32):
    """Custom type tnShelfDisplayIdType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )


_TnShelfDisplayIdType_Type.__name__ = "Integer32"
_TnShelfDisplayIdType_Object = MibTableColumn
tnShelfDisplayIdType = _TnShelfDisplayIdType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1, 1),
    _TnShelfDisplayIdType_Type()
)
tnShelfDisplayIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDisplayIdType.setStatus("current")


class _TnShelfDisplayIdIntf_Type(Integer32):
    """Custom type tnShelfDisplayIdIntf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oamp", 1),
          ("es1", 2),
          ("es2", 3))
    )


_TnShelfDisplayIdIntf_Type.__name__ = "Integer32"
_TnShelfDisplayIdIntf_Object = MibTableColumn
tnShelfDisplayIdIntf = _TnShelfDisplayIdIntf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1, 2),
    _TnShelfDisplayIdIntf_Type()
)
tnShelfDisplayIdIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDisplayIdIntf.setStatus("current")


class _TnShelfDisplayIdString_Type(SnmpAdminString):
    """Custom type tnShelfDisplayIdString based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TnShelfDisplayIdString_Type.__name__ = "SnmpAdminString"
_TnShelfDisplayIdString_Object = MibTableColumn
tnShelfDisplayIdString = _TnShelfDisplayIdString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1, 3),
    _TnShelfDisplayIdString_Type()
)
tnShelfDisplayIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfDisplayIdString.setStatus("current")


class _TnShelfDisplayUserMessage_Type(SnmpAdminString):
    """Custom type tnShelfDisplayUserMessage based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnShelfDisplayUserMessage_Type.__name__ = "SnmpAdminString"
_TnShelfDisplayUserMessage_Object = MibTableColumn
tnShelfDisplayUserMessage = _TnShelfDisplayUserMessage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1, 4),
    _TnShelfDisplayUserMessage_Type()
)
tnShelfDisplayUserMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDisplayUserMessage.setStatus("current")


class _TnShelfDisplayFMMessage_Type(SnmpAdminString):
    """Custom type tnShelfDisplayFMMessage based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnShelfDisplayFMMessage_Type.__name__ = "SnmpAdminString"
_TnShelfDisplayFMMessage_Object = MibTableColumn
tnShelfDisplayFMMessage = _TnShelfDisplayFMMessage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1, 5),
    _TnShelfDisplayFMMessage_Type()
)
tnShelfDisplayFMMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnShelfDisplayFMMessage.setStatus("current")


class _TnShelfDisplayShortPush_Type(SnmpAdminString):
    """Custom type tnShelfDisplayShortPush based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnShelfDisplayShortPush_Type.__name__ = "SnmpAdminString"
_TnShelfDisplayShortPush_Object = MibTableColumn
tnShelfDisplayShortPush = _TnShelfDisplayShortPush_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1, 6),
    _TnShelfDisplayShortPush_Type()
)
tnShelfDisplayShortPush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDisplayShortPush.setStatus("current")


class _TnShelfDisplayLongPush_Type(SnmpAdminString):
    """Custom type tnShelfDisplayLongPush based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnShelfDisplayLongPush_Type.__name__ = "SnmpAdminString"
_TnShelfDisplayLongPush_Object = MibTableColumn
tnShelfDisplayLongPush = _TnShelfDisplayLongPush_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 6, 1, 7),
    _TnShelfDisplayLongPush_Type()
)
tnShelfDisplayLongPush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfDisplayLongPush.setStatus("current")
_TnShelfRackTable_Object = MibTable
tnShelfRackTable = _TnShelfRackTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnShelfRackTable.setStatus("current")
_TnShelfRackEntry_Object = MibTableRow
tnShelfRackEntry = _TnShelfRackEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 7, 1)
)
tnShelfRackEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfRackNumber"),
)
if mibBuilder.loadTexts:
    tnShelfRackEntry.setStatus("current")
_TnShelfRackNumber_Type = Unsigned32
_TnShelfRackNumber_Object = MibTableColumn
tnShelfRackNumber = _TnShelfRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 7, 1, 1),
    _TnShelfRackNumber_Type()
)
tnShelfRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnShelfRackNumber.setStatus("current")


class _TnShelfRackDescription_Type(SnmpAdminString):
    """Custom type tnShelfRackDescription based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnShelfRackDescription_Type.__name__ = "SnmpAdminString"
_TnShelfRackDescription_Object = MibTableColumn
tnShelfRackDescription = _TnShelfRackDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 7, 1, 2),
    _TnShelfRackDescription_Type()
)
tnShelfRackDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRackDescription.setStatus("current")


class _TnShelfRackBlockNumber_Type(SnmpAdminString):
    """Custom type tnShelfRackBlockNumber based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TnShelfRackBlockNumber_Type.__name__ = "SnmpAdminString"
_TnShelfRackBlockNumber_Object = MibTableColumn
tnShelfRackBlockNumber = _TnShelfRackBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 7, 1, 3),
    _TnShelfRackBlockNumber_Type()
)
tnShelfRackBlockNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfRackBlockNumber.setStatus("current")
_TnShelfFiberTrayTable_Object = MibTable
tnShelfFiberTrayTable = _TnShelfFiberTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnShelfFiberTrayTable.setStatus("current")
_TnShelfFiberTrayEntry_Object = MibTableRow
tnShelfFiberTrayEntry = _TnShelfFiberTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 8, 1)
)
tnShelfFiberTrayEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfFiberTrayNumber"),
)
if mibBuilder.loadTexts:
    tnShelfFiberTrayEntry.setStatus("current")
_TnShelfFiberTrayNumber_Type = Unsigned32
_TnShelfFiberTrayNumber_Object = MibTableColumn
tnShelfFiberTrayNumber = _TnShelfFiberTrayNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 8, 1, 1),
    _TnShelfFiberTrayNumber_Type()
)
tnShelfFiberTrayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnShelfFiberTrayNumber.setStatus("current")


class _TnShelfFiberTrayPosition_Type(SnmpAdminString):
    """Custom type tnShelfFiberTrayPosition based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnShelfFiberTrayPosition_Type.__name__ = "SnmpAdminString"
_TnShelfFiberTrayPosition_Object = MibTableColumn
tnShelfFiberTrayPosition = _TnShelfFiberTrayPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 8, 1, 2),
    _TnShelfFiberTrayPosition_Type()
)
tnShelfFiberTrayPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnShelfFiberTrayPosition.setStatus("current")

# Managed Objects groups

tnShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 1)
)
tnShelfGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfName"),
        ("TROPIC-SHELF-MIB", "tnShelfDescr"),
        ("TROPIC-SHELF-MIB", "tnShelfSerialNum"),
        ("TROPIC-SHELF-MIB", "tnShelfProgrammedType"),
        ("TROPIC-SHELF-MIB", "tnShelfPresentType"),
        ("TROPIC-SHELF-MIB", "tnShelfActivitySwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfLampTest"),
        ("TROPIC-SHELF-MIB", "tnShelfMateCCReadyToProtect"),
        ("TROPIC-SHELF-MIB", "tnShelfIsUnmanaged"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedAmps"),
        ("TROPIC-SHELF-MIB", "tnShelfSerialNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfAINS"),
        ("TROPIC-SHELF-MIB", "tnShelfStatusLEDColor"),
        ("TROPIC-SHELF-MIB", "tnShelfStatusLEDState"),
        ("TROPIC-SHELF-MIB", "tnShelfWTMode"),
        ("TROPIC-SHELF-MIB", "tnShelfActivityMt0cSwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfMateMt0cReadyToProtect"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedPfa"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedPfb"),
        ("TROPIC-SHELF-MIB", "tnShelfHighVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfLowVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageThresholdTol"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedVolts"),
        ("TROPIC-SHELF-MIB", "tnShelfMatrixSize"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageFloor"),
        ("TROPIC-SHELF-MIB", "tnShelfCalculatedLoad"),
        ("TROPIC-SHELF-MIB", "tnShelfClkSwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedVoltsAC"),
        ("TROPIC-SHELF-MIB", "tnShelfHighVoltageThresholdAC"),
        ("TROPIC-SHELF-MIB", "tnShelfLowVoltageThresholdAC"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageFloorAC"),
        ("TROPIC-SHELF-MIB", "tnShelfExternalAcPower"),
        ("TROPIC-SHELF-MIB", "tnShelfLoadWarningThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfTimingSwitch"),
        ("TROPIC-SHELF-MIB", "tnShelfCalculatedLoadAC"),
        ("TROPIC-SHELF-MIB", "tnShelfPowerCapacity"),
        ("TROPIC-SHELF-MIB", "tnShelfRemainingPowerCapacity"),
        ("TROPIC-SHELF-MIB", "tnShelfLockout"),
        ("TROPIC-SHELF-MIB", "tnShelfFilterMonitorStatus"),
        ("TROPIC-SHELF-MIB", "tnShelfFilterInspectionInterval"),
        ("TROPIC-SHELF-MIB", "tnShelfFilterStartDate"),
        ("TROPIC-SHELF-MIB", "tnShelfAlmProfName"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap1"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap2"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap3"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap4"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap5"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchPowerCap6"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap1"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap2"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap3"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap4"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap5"),
        ("TROPIC-SHELF-MIB", "tnShelfBranchRemainingPwrCap6"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricEQPStatus"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricActivityState"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricFailures"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricUsage"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricEqpsLEDColor"),
        ("TROPIC-SHELF-MIB", "tnShelfFabricReadyToProtect"),
        ("TROPIC-SHELF-MIB", "tnShelfRackType"),
        ("TROPIC-SHELF-MIB", "tnShelfInventoryAction"),
        ("TROPIC-SHELF-MIB", "tnShelfFilterAction"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedCruA"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedCruB"),
        ("TROPIC-SHELF-MIB", "tnShelfPanelTimingPort"),
        ("TROPIC-SHELF-MIB", "tnShelfDelegateFCRUSlot"),
        ("TROPIC-SHELF-MIB", "tnShelfUID"),
        ("TROPIC-SHELF-MIB", "tnShelfUIDStatusLEDState"),
        ("TROPIC-SHELF-MIB", "tnShelfMTXSIZE"),
        ("TROPIC-SHELF-MIB", "tnShelfRMNMTXCAP"),
        ("TROPIC-SHELF-MIB", "tnShelfUIDStatusLEDColor"),
        ("TROPIC-SHELF-MIB", "tnShelfFanMode"),
        ("TROPIC-SHELF-MIB", "tnShelfExpectedVoltsHVDC"),
        ("TROPIC-SHELF-MIB", "tnShelfHighVoltageThresholdHVDC"),
        ("TROPIC-SHELF-MIB", "tnShelfLowVoltageThresholdHVDC"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageThresholdTolHVDC"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageFloorHVDC"),
        ("TROPIC-SHELF-MIB", "tnShelfVoltageThresholdTolAC"),
        ("TROPIC-SHELF-MIB", "tnShelfTsiFreeze"),
        ("TROPIC-SHELF-MIB", "tnShelfPosition"),
        ("TROPIC-SHELF-MIB", "tnShelfLifeCycleState"),
        ("TROPIC-SHELF-MIB", "tnShelfDueDate"),
        ("TROPIC-SHELF-MIB", "tnShelfRackLocation"),
        ("TROPIC-SHELF-MIB", "tnShelfXpdrNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfCoupledNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfCoupledCmd"),
        ("TROPIC-SHELF-MIB", "tnShelfCustomerLifeCycleState"),
        ("TROPIC-SHELF-MIB", "tnShelfXponderLifeCycleState"),
        ("TROPIC-SHELF-MIB", "tnShelfCouplingState"),
        ("TROPIC-SHELF-MIB", "tnShelfPowerFeed"),
        ("TROPIC-SHELF-MIB", "tnShelfPfaExpectedVolts"),
        ("TROPIC-SHELF-MIB", "tnShelfPfaLowVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfPfaHighVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfPfaVoltageThresholdTol"),
        ("TROPIC-SHELF-MIB", "tnShelfPfbExpectedVolts"),
        ("TROPIC-SHELF-MIB", "tnShelfPfbLowVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfPfbHighVoltageThreshold"),
        ("TROPIC-SHELF-MIB", "tnShelfPfbVoltageThresholdTol"))
)
if mibBuilder.loadTexts:
    tnShelfGroup.setStatus("current")

tnShelfScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 2)
)
tnShelfScalarsGroup.setObjects(
    ("TROPIC-SHELF-MIB", "tnShelfTotal")
)
if mibBuilder.loadTexts:
    tnShelfScalarsGroup.setStatus("current")

tnShelfRiDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 3)
)
tnShelfRiDataGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfRiCompanyID"),
        ("TROPIC-SHELF-MIB", "tnShelfRiMnemonic"),
        ("TROPIC-SHELF-MIB", "tnShelfRiCLEI"),
        ("TROPIC-SHELF-MIB", "tnShelfRiManufacturingPartNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfRiSWPartNum"),
        ("TROPIC-SHELF-MIB", "tnShelfRiFactoryID"),
        ("TROPIC-SHELF-MIB", "tnShelfRiSerialNumber"),
        ("TROPIC-SHELF-MIB", "tnShelfRiDate"),
        ("TROPIC-SHELF-MIB", "tnShelfRiExtraData"))
)
if mibBuilder.loadTexts:
    tnShelfRiDataGroup.setStatus("current")

tnShelfInvDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 4)
)
tnShelfInvDataGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfInvInvStatus"),
        ("TROPIC-SHELF-MIB", "tnShelfInvCustInvField"),
        ("TROPIC-SHELF-MIB", "tnShelfInvFiberType"),
        ("TROPIC-SHELF-MIB", "tnShelfInvDcmSize"),
        ("TROPIC-SHELF-MIB", "tnShelfInvAvgInsertionLoss"),
        ("TROPIC-SHELF-MIB", "tnShelfInvInsertionLossSlope"),
        ("TROPIC-SHELF-MIB", "tnShelfInvTotalDispFit"),
        ("TROPIC-SHELF-MIB", "tnShelfInvDispFiberLength"),
        ("TROPIC-SHELF-MIB", "tnShelfInvPmd"),
        ("TROPIC-SHELF-MIB", "tnShelfInvLatencyMismatch"))
)
if mibBuilder.loadTexts:
    tnShelfInvDataGroup.setStatus("current")

tnMultiShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 5)
)
tnMultiShelfGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnMultiShelfSerialNumber"),
        ("TROPIC-SHELF-MIB", "tnMultiShelfRowStatus"))
)
if mibBuilder.loadTexts:
    tnMultiShelfGroup.setStatus("current")

tnShelfDisplayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 6)
)
tnShelfDisplayGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfDisplayIdType"),
        ("TROPIC-SHELF-MIB", "tnShelfDisplayIdIntf"),
        ("TROPIC-SHELF-MIB", "tnShelfDisplayIdString"),
        ("TROPIC-SHELF-MIB", "tnShelfDisplayUserMessage"),
        ("TROPIC-SHELF-MIB", "tnShelfDisplayFMMessage"),
        ("TROPIC-SHELF-MIB", "tnShelfDisplayShortPush"),
        ("TROPIC-SHELF-MIB", "tnShelfDisplayLongPush"))
)
if mibBuilder.loadTexts:
    tnShelfDisplayGroup.setStatus("current")

tnShelfRackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 7)
)
tnShelfRackGroup.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfRackDescription"),
        ("TROPIC-SHELF-MIB", "tnShelfRackBlockNumber"))
)
if mibBuilder.loadTexts:
    tnShelfRackGroup.setStatus("current")

tnShelfFiberTrayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 1, 8)
)
tnShelfFiberTrayGroup.setObjects(
    ("TROPIC-SHELF-MIB", "tnShelfFiberTrayPosition")
)
if mibBuilder.loadTexts:
    tnShelfFiberTrayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnShelfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 1, 2, 1)
)
tnShelfCompliance.setObjects(
      *(("TROPIC-SHELF-MIB", "tnShelfGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfScalarsGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfRiDataGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfInvDataGroup"),
        ("TROPIC-SHELF-MIB", "tnMultiShelfGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfDisplayGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfRackGroup"),
        ("TROPIC-SHELF-MIB", "tnShelfFiberTrayGroup"))
)
if mibBuilder.loadTexts:
    tnShelfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SHELF-MIB",
    **{"AluWdmExpectedAmpPF": AluWdmExpectedAmpPF,
       "TropicShelfInvAvailabilityStatus": TropicShelfInvAvailabilityStatus,
       "TropicShelfInvCustomerInvField": TropicShelfInvCustomerInvField,
       "TropicShelfInvFiberType": TropicShelfInvFiberType,
       "TropicShelfInvDcmSize": TropicShelfInvDcmSize,
       "TropicShelfInvInsertionLoss": TropicShelfInvInsertionLoss,
       "TropicShelfInvInsertionLossSlope": TropicShelfInvInsertionLossSlope,
       "TropicShelfInvDispersionFit": TropicShelfInvDispersionFit,
       "TropicShelfInvFiberLength": TropicShelfInvFiberLength,
       "TropicShelfInvPmd": TropicShelfInvPmd,
       "TropicShelfInvLatencyMismatch": TropicShelfInvLatencyMismatch,
       "tnShelfMibModule": tnShelfMibModule,
       "tnShelfConf": tnShelfConf,
       "tnShelfGroups": tnShelfGroups,
       "tnShelfGroup": tnShelfGroup,
       "tnShelfScalarsGroup": tnShelfScalarsGroup,
       "tnShelfRiDataGroup": tnShelfRiDataGroup,
       "tnShelfInvDataGroup": tnShelfInvDataGroup,
       "tnMultiShelfGroup": tnMultiShelfGroup,
       "tnShelfDisplayGroup": tnShelfDisplayGroup,
       "tnShelfRackGroup": tnShelfRackGroup,
       "tnShelfFiberTrayGroup": tnShelfFiberTrayGroup,
       "tnShelfCompliances": tnShelfCompliances,
       "tnShelfCompliance": tnShelfCompliance,
       "tnShelfObjs": tnShelfObjs,
       "tnShelfBasics": tnShelfBasics,
       "tnShelfTable": tnShelfTable,
       "tnShelfEntry": tnShelfEntry,
       "tnShelfIndex": tnShelfIndex,
       "tnShelfName": tnShelfName,
       "tnShelfDescr": tnShelfDescr,
       "tnShelfSerialNum": tnShelfSerialNum,
       "tnShelfProgrammedType": tnShelfProgrammedType,
       "tnShelfPresentType": tnShelfPresentType,
       "tnShelfActivitySwitch": tnShelfActivitySwitch,
       "tnShelfLampTest": tnShelfLampTest,
       "tnShelfMateCCReadyToProtect": tnShelfMateCCReadyToProtect,
       "tnShelfIsUnmanaged": tnShelfIsUnmanaged,
       "tnShelfExpectedAmps": tnShelfExpectedAmps,
       "tnShelfSerialNumber": tnShelfSerialNumber,
       "tnShelfAINS": tnShelfAINS,
       "tnShelfStatusLEDColor": tnShelfStatusLEDColor,
       "tnShelfStatusLEDState": tnShelfStatusLEDState,
       "tnShelfWTMode": tnShelfWTMode,
       "tnShelfActivityMt0cSwitch": tnShelfActivityMt0cSwitch,
       "tnShelfMateMt0cReadyToProtect": tnShelfMateMt0cReadyToProtect,
       "tnShelfExpectedPfa": tnShelfExpectedPfa,
       "tnShelfExpectedPfb": tnShelfExpectedPfb,
       "tnShelfHighVoltageThreshold": tnShelfHighVoltageThreshold,
       "tnShelfLowVoltageThreshold": tnShelfLowVoltageThreshold,
       "tnShelfVoltageThresholdTol": tnShelfVoltageThresholdTol,
       "tnShelfExpectedVolts": tnShelfExpectedVolts,
       "tnShelfMatrixSize": tnShelfMatrixSize,
       "tnShelfVoltageFloor": tnShelfVoltageFloor,
       "tnShelfCalculatedLoad": tnShelfCalculatedLoad,
       "tnShelfClkSwitch": tnShelfClkSwitch,
       "tnShelfExpectedVoltsAC": tnShelfExpectedVoltsAC,
       "tnShelfHighVoltageThresholdAC": tnShelfHighVoltageThresholdAC,
       "tnShelfLowVoltageThresholdAC": tnShelfLowVoltageThresholdAC,
       "tnShelfVoltageFloorAC": tnShelfVoltageFloorAC,
       "tnShelfExternalAcPower": tnShelfExternalAcPower,
       "tnShelfLoadWarningThreshold": tnShelfLoadWarningThreshold,
       "tnShelfTimingSwitch": tnShelfTimingSwitch,
       "tnShelfCalculatedLoadAC": tnShelfCalculatedLoadAC,
       "tnShelfPowerCapacity": tnShelfPowerCapacity,
       "tnShelfRemainingPowerCapacity": tnShelfRemainingPowerCapacity,
       "tnShelfLockout": tnShelfLockout,
       "tnShelfFilterMonitorStatus": tnShelfFilterMonitorStatus,
       "tnShelfFilterInspectionInterval": tnShelfFilterInspectionInterval,
       "tnShelfFilterStartDate": tnShelfFilterStartDate,
       "tnShelfAlmProfName": tnShelfAlmProfName,
       "tnShelfBranchPowerCap1": tnShelfBranchPowerCap1,
       "tnShelfBranchPowerCap2": tnShelfBranchPowerCap2,
       "tnShelfBranchPowerCap3": tnShelfBranchPowerCap3,
       "tnShelfBranchPowerCap4": tnShelfBranchPowerCap4,
       "tnShelfBranchPowerCap5": tnShelfBranchPowerCap5,
       "tnShelfBranchPowerCap6": tnShelfBranchPowerCap6,
       "tnShelfBranchRemainingPwrCap1": tnShelfBranchRemainingPwrCap1,
       "tnShelfBranchRemainingPwrCap2": tnShelfBranchRemainingPwrCap2,
       "tnShelfBranchRemainingPwrCap3": tnShelfBranchRemainingPwrCap3,
       "tnShelfBranchRemainingPwrCap4": tnShelfBranchRemainingPwrCap4,
       "tnShelfBranchRemainingPwrCap5": tnShelfBranchRemainingPwrCap5,
       "tnShelfBranchRemainingPwrCap6": tnShelfBranchRemainingPwrCap6,
       "tnShelfFabricEQPStatus": tnShelfFabricEQPStatus,
       "tnShelfFabricActivityState": tnShelfFabricActivityState,
       "tnShelfFabricFailures": tnShelfFabricFailures,
       "tnShelfFabricUsage": tnShelfFabricUsage,
       "tnShelfFabricEqpsLEDColor": tnShelfFabricEqpsLEDColor,
       "tnShelfFabricReadyToProtect": tnShelfFabricReadyToProtect,
       "tnShelfRackType": tnShelfRackType,
       "tnShelfInventoryAction": tnShelfInventoryAction,
       "tnShelfFilterAction": tnShelfFilterAction,
       "tnShelfExpectedCruA": tnShelfExpectedCruA,
       "tnShelfExpectedCruB": tnShelfExpectedCruB,
       "tnShelfPanelTimingPort": tnShelfPanelTimingPort,
       "tnShelfDelegateFCRUSlot": tnShelfDelegateFCRUSlot,
       "tnShelfUID": tnShelfUID,
       "tnShelfUIDStatusLEDState": tnShelfUIDStatusLEDState,
       "tnShelfMTXSIZE": tnShelfMTXSIZE,
       "tnShelfRMNMTXCAP": tnShelfRMNMTXCAP,
       "tnShelfUIDStatusLEDColor": tnShelfUIDStatusLEDColor,
       "tnShelfFanMode": tnShelfFanMode,
       "tnShelfExpectedVoltsHVDC": tnShelfExpectedVoltsHVDC,
       "tnShelfHighVoltageThresholdHVDC": tnShelfHighVoltageThresholdHVDC,
       "tnShelfLowVoltageThresholdHVDC": tnShelfLowVoltageThresholdHVDC,
       "tnShelfVoltageThresholdTolHVDC": tnShelfVoltageThresholdTolHVDC,
       "tnShelfVoltageFloorHVDC": tnShelfVoltageFloorHVDC,
       "tnShelfVoltageThresholdTolAC": tnShelfVoltageThresholdTolAC,
       "tnShelfTsiFreeze": tnShelfTsiFreeze,
       "tnShelfPosition": tnShelfPosition,
       "tnShelfLifeCycleState": tnShelfLifeCycleState,
       "tnShelfDueDate": tnShelfDueDate,
       "tnShelfRackLocation": tnShelfRackLocation,
       "tnShelfXpdrNumber": tnShelfXpdrNumber,
       "tnShelfCoupledNumber": tnShelfCoupledNumber,
       "tnShelfCoupledCmd": tnShelfCoupledCmd,
       "tnShelfCustomerLifeCycleState": tnShelfCustomerLifeCycleState,
       "tnShelfXponderLifeCycleState": tnShelfXponderLifeCycleState,
       "tnShelfCouplingState": tnShelfCouplingState,
       "tnShelfPowerFeed": tnShelfPowerFeed,
       "tnShelfPfaExpectedVolts": tnShelfPfaExpectedVolts,
       "tnShelfPfaLowVoltageThreshold": tnShelfPfaLowVoltageThreshold,
       "tnShelfPfaHighVoltageThreshold": tnShelfPfaHighVoltageThreshold,
       "tnShelfPfaVoltageThresholdTol": tnShelfPfaVoltageThresholdTol,
       "tnShelfPfbExpectedVolts": tnShelfPfbExpectedVolts,
       "tnShelfPfbLowVoltageThreshold": tnShelfPfbLowVoltageThreshold,
       "tnShelfPfbHighVoltageThreshold": tnShelfPfbHighVoltageThreshold,
       "tnShelfPfbVoltageThresholdTol": tnShelfPfbVoltageThresholdTol,
       "tnShelfTotal": tnShelfTotal,
       "tnShelfRiDataTable": tnShelfRiDataTable,
       "tnShelfRiDataEntry": tnShelfRiDataEntry,
       "tnShelfRiCompanyID": tnShelfRiCompanyID,
       "tnShelfRiMnemonic": tnShelfRiMnemonic,
       "tnShelfRiCLEI": tnShelfRiCLEI,
       "tnShelfRiManufacturingPartNumber": tnShelfRiManufacturingPartNumber,
       "tnShelfRiSWPartNum": tnShelfRiSWPartNum,
       "tnShelfRiFactoryID": tnShelfRiFactoryID,
       "tnShelfRiSerialNumber": tnShelfRiSerialNumber,
       "tnShelfRiDate": tnShelfRiDate,
       "tnShelfRiExtraData": tnShelfRiExtraData,
       "tnShelfInvTable": tnShelfInvTable,
       "tnShelfInvEntry": tnShelfInvEntry,
       "tnShelfInvInvStatus": tnShelfInvInvStatus,
       "tnShelfInvCustInvField": tnShelfInvCustInvField,
       "tnShelfInvFiberType": tnShelfInvFiberType,
       "tnShelfInvDcmSize": tnShelfInvDcmSize,
       "tnShelfInvAvgInsertionLoss": tnShelfInvAvgInsertionLoss,
       "tnShelfInvInsertionLossSlope": tnShelfInvInsertionLossSlope,
       "tnShelfInvTotalDispFit": tnShelfInvTotalDispFit,
       "tnShelfInvDispFiberLength": tnShelfInvDispFiberLength,
       "tnShelfInvPmd": tnShelfInvPmd,
       "tnShelfInvLatencyMismatch": tnShelfInvLatencyMismatch,
       "tnMultiShelfTable": tnMultiShelfTable,
       "tnMultiShelfEntry": tnMultiShelfEntry,
       "tnMultiShelfIndex": tnMultiShelfIndex,
       "tnMultiShelfSerialNumber": tnMultiShelfSerialNumber,
       "tnMultiShelfRowStatus": tnMultiShelfRowStatus,
       "tnShelfDisplayTable": tnShelfDisplayTable,
       "tnShelfDisplayEntry": tnShelfDisplayEntry,
       "tnShelfDisplayIdType": tnShelfDisplayIdType,
       "tnShelfDisplayIdIntf": tnShelfDisplayIdIntf,
       "tnShelfDisplayIdString": tnShelfDisplayIdString,
       "tnShelfDisplayUserMessage": tnShelfDisplayUserMessage,
       "tnShelfDisplayFMMessage": tnShelfDisplayFMMessage,
       "tnShelfDisplayShortPush": tnShelfDisplayShortPush,
       "tnShelfDisplayLongPush": tnShelfDisplayLongPush,
       "tnShelfRackTable": tnShelfRackTable,
       "tnShelfRackEntry": tnShelfRackEntry,
       "tnShelfRackNumber": tnShelfRackNumber,
       "tnShelfRackDescription": tnShelfRackDescription,
       "tnShelfRackBlockNumber": tnShelfRackBlockNumber,
       "tnShelfFiberTrayTable": tnShelfFiberTrayTable,
       "tnShelfFiberTrayEntry": tnShelfFiberTrayEntry,
       "tnShelfFiberTrayNumber": tnShelfFiberTrayNumber,
       "tnShelfFiberTrayPosition": tnShelfFiberTrayPosition}
)
