# SNMP MIB module (PT3080-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\protelevision\PT3080-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:32 2025
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

(pt,) = mibBuilder.importSymbols(
    "PT-MIB",
    "pt")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pt3080 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080)
)
if mibBuilder.loadTexts:
    pt3080.setRevisions(
        ("2015-06-22 09:40",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pt3080System_ObjectIdentity = ObjectIdentity
pt3080System = _Pt3080System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1)
)
_Pt3080SystemInstrumentKU_Type = DisplayString
_Pt3080SystemInstrumentKU_Object = MibScalar
pt3080SystemInstrumentKU = _Pt3080SystemInstrumentKU_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 1),
    _Pt3080SystemInstrumentKU_Type()
)
pt3080SystemInstrumentKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentKU.setStatus("current")
_Pt3080SystemInstrumentType_Type = DisplayString
_Pt3080SystemInstrumentType_Object = MibScalar
pt3080SystemInstrumentType = _Pt3080SystemInstrumentType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 2),
    _Pt3080SystemInstrumentType_Type()
)
pt3080SystemInstrumentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentType.setStatus("current")
_Pt3080SystemInstrumentSWRev_Type = DisplayString
_Pt3080SystemInstrumentSWRev_Object = MibScalar
pt3080SystemInstrumentSWRev = _Pt3080SystemInstrumentSWRev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 3),
    _Pt3080SystemInstrumentSWRev_Type()
)
pt3080SystemInstrumentSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentSWRev.setStatus("current")
_Pt3080SystemInstrumentBootLoaderRev_Type = DisplayString
_Pt3080SystemInstrumentBootLoaderRev_Object = MibScalar
pt3080SystemInstrumentBootLoaderRev = _Pt3080SystemInstrumentBootLoaderRev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 4),
    _Pt3080SystemInstrumentBootLoaderRev_Type()
)
pt3080SystemInstrumentBootLoaderRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentBootLoaderRev.setStatus("current")
_Pt3080SystemInstrumentKernelRev_Type = DisplayString
_Pt3080SystemInstrumentKernelRev_Object = MibScalar
pt3080SystemInstrumentKernelRev = _Pt3080SystemInstrumentKernelRev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 5),
    _Pt3080SystemInstrumentKernelRev_Type()
)
pt3080SystemInstrumentKernelRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentKernelRev.setStatus("current")
_Pt3080SystemInstrumentOptions_Type = DisplayString
_Pt3080SystemInstrumentOptions_Object = MibScalar
pt3080SystemInstrumentOptions = _Pt3080SystemInstrumentOptions_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 6),
    _Pt3080SystemInstrumentOptions_Type()
)
pt3080SystemInstrumentOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentOptions.setStatus("current")
_Pt3080SystemInstrumentFW1Rev_Type = DisplayString
_Pt3080SystemInstrumentFW1Rev_Object = MibScalar
pt3080SystemInstrumentFW1Rev = _Pt3080SystemInstrumentFW1Rev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 7),
    _Pt3080SystemInstrumentFW1Rev_Type()
)
pt3080SystemInstrumentFW1Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentFW1Rev.setStatus("current")
_Pt3080SystemInstrumentFW1RevBL_Type = DisplayString
_Pt3080SystemInstrumentFW1RevBL_Object = MibScalar
pt3080SystemInstrumentFW1RevBL = _Pt3080SystemInstrumentFW1RevBL_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 8),
    _Pt3080SystemInstrumentFW1RevBL_Type()
)
pt3080SystemInstrumentFW1RevBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentFW1RevBL.setStatus("current")
_Pt3080SystemInstrumentFW2Rev_Type = DisplayString
_Pt3080SystemInstrumentFW2Rev_Object = MibScalar
pt3080SystemInstrumentFW2Rev = _Pt3080SystemInstrumentFW2Rev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 9),
    _Pt3080SystemInstrumentFW2Rev_Type()
)
pt3080SystemInstrumentFW2Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentFW2Rev.setStatus("current")
_Pt3080SystemInstrumentFW2RevBL_Type = DisplayString
_Pt3080SystemInstrumentFW2RevBL_Object = MibScalar
pt3080SystemInstrumentFW2RevBL = _Pt3080SystemInstrumentFW2RevBL_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 10),
    _Pt3080SystemInstrumentFW2RevBL_Type()
)
pt3080SystemInstrumentFW2RevBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentFW2RevBL.setStatus("current")
_Pt3080SystemInstrumentFW3Rev_Type = DisplayString
_Pt3080SystemInstrumentFW3Rev_Object = MibScalar
pt3080SystemInstrumentFW3Rev = _Pt3080SystemInstrumentFW3Rev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 11),
    _Pt3080SystemInstrumentFW3Rev_Type()
)
pt3080SystemInstrumentFW3Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentFW3Rev.setStatus("current")
_Pt3080SystemInstrumentFW4Rev_Type = DisplayString
_Pt3080SystemInstrumentFW4Rev_Object = MibScalar
pt3080SystemInstrumentFW4Rev = _Pt3080SystemInstrumentFW4Rev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 12),
    _Pt3080SystemInstrumentFW4Rev_Type()
)
pt3080SystemInstrumentFW4Rev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentFW4Rev.setStatus("current")
_Pt3080SystemInstrumentPCBRev_Type = DisplayString
_Pt3080SystemInstrumentPCBRev_Object = MibScalar
pt3080SystemInstrumentPCBRev = _Pt3080SystemInstrumentPCBRev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 13),
    _Pt3080SystemInstrumentPCBRev_Type()
)
pt3080SystemInstrumentPCBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentPCBRev.setStatus("current")
_Pt3080SystemInstrumentCalibrationRev_Type = DisplayString
_Pt3080SystemInstrumentCalibrationRev_Object = MibScalar
pt3080SystemInstrumentCalibrationRev = _Pt3080SystemInstrumentCalibrationRev_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 14),
    _Pt3080SystemInstrumentCalibrationRev_Type()
)
pt3080SystemInstrumentCalibrationRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentCalibrationRev.setStatus("current")
_Pt3080SystemInstrumentCalibrationDate_Type = DisplayString
_Pt3080SystemInstrumentCalibrationDate_Object = MibScalar
pt3080SystemInstrumentCalibrationDate = _Pt3080SystemInstrumentCalibrationDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 15),
    _Pt3080SystemInstrumentCalibrationDate_Type()
)
pt3080SystemInstrumentCalibrationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemInstrumentCalibrationDate.setStatus("current")


class _Pt3080SystemReboot_Type(Integer32):
    """Custom type pt3080SystemReboot based on Integer32"""
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
        *(("keeprunning", 0),
          ("sameimage", 1),
          ("otherimage", 2),
          ("image0", 3),
          ("image1", 4))
    )


_Pt3080SystemReboot_Type.__name__ = "Integer32"
_Pt3080SystemReboot_Object = MibScalar
pt3080SystemReboot = _Pt3080SystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 16),
    _Pt3080SystemReboot_Type()
)
pt3080SystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemReboot.setStatus("current")


class _Pt3080SystemRebootDefaultConfig_Type(Integer32):
    """Custom type pt3080SystemRebootDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keeprunning", 0),
          ("reboot", 1))
    )


_Pt3080SystemRebootDefaultConfig_Type.__name__ = "Integer32"
_Pt3080SystemRebootDefaultConfig_Object = MibScalar
pt3080SystemRebootDefaultConfig = _Pt3080SystemRebootDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 19),
    _Pt3080SystemRebootDefaultConfig_Type()
)
pt3080SystemRebootDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemRebootDefaultConfig.setStatus("current")


class _Pt3080SystemDateTimeSync_Type(Integer32):
    """Custom type pt3080SystemDateTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1),
          ("gps", 2),
          ("ntp", 3))
    )


_Pt3080SystemDateTimeSync_Type.__name__ = "Integer32"
_Pt3080SystemDateTimeSync_Object = MibScalar
pt3080SystemDateTimeSync = _Pt3080SystemDateTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 20),
    _Pt3080SystemDateTimeSync_Type()
)
pt3080SystemDateTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemDateTimeSync.setStatus("current")
_Pt3080SystemTimezone_Type = DisplayString
_Pt3080SystemTimezone_Object = MibScalar
pt3080SystemTimezone = _Pt3080SystemTimezone_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 21),
    _Pt3080SystemTimezone_Type()
)
pt3080SystemTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemTimezone.setStatus("current")
_Pt3080SystemDateTime_Type = DisplayString
_Pt3080SystemDateTime_Object = MibScalar
pt3080SystemDateTime = _Pt3080SystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 22),
    _Pt3080SystemDateTime_Type()
)
pt3080SystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemDateTime.setStatus("current")
_Pt3080SystemCurrentImage_Type = Integer32
_Pt3080SystemCurrentImage_Object = MibScalar
pt3080SystemCurrentImage = _Pt3080SystemCurrentImage_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 23),
    _Pt3080SystemCurrentImage_Type()
)
pt3080SystemCurrentImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemCurrentImage.setStatus("current")
_Pt3080SystemImage0Version_Type = DisplayString
_Pt3080SystemImage0Version_Object = MibScalar
pt3080SystemImage0Version = _Pt3080SystemImage0Version_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 24),
    _Pt3080SystemImage0Version_Type()
)
pt3080SystemImage0Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemImage0Version.setStatus("current")
_Pt3080SystemImage0InstalledDate_Type = DateAndTime
_Pt3080SystemImage0InstalledDate_Object = MibScalar
pt3080SystemImage0InstalledDate = _Pt3080SystemImage0InstalledDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 25),
    _Pt3080SystemImage0InstalledDate_Type()
)
pt3080SystemImage0InstalledDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemImage0InstalledDate.setStatus("current")
_Pt3080SystemImage1version_Type = DisplayString
_Pt3080SystemImage1version_Object = MibScalar
pt3080SystemImage1version = _Pt3080SystemImage1version_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 26),
    _Pt3080SystemImage1version_Type()
)
pt3080SystemImage1version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemImage1version.setStatus("current")
_Pt3080SystemImage1InstalledDate_Type = DateAndTime
_Pt3080SystemImage1InstalledDate_Object = MibScalar
pt3080SystemImage1InstalledDate = _Pt3080SystemImage1InstalledDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 27),
    _Pt3080SystemImage1InstalledDate_Type()
)
pt3080SystemImage1InstalledDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemImage1InstalledDate.setStatus("current")


class _Pt3080SystemServiceLED_Type(Integer32):
    """Custom type pt3080SystemServiceLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080SystemServiceLED_Type.__name__ = "Integer32"
_Pt3080SystemServiceLED_Object = MibScalar
pt3080SystemServiceLED = _Pt3080SystemServiceLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 28),
    _Pt3080SystemServiceLED_Type()
)
pt3080SystemServiceLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemServiceLED.setStatus("current")


class _Pt3080SystemType_Type(Integer32):
    """Custom type pt3080SystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("modulator", 0),
          ("repeater", 1))
    )


_Pt3080SystemType_Type.__name__ = "Integer32"
_Pt3080SystemType_Object = MibScalar
pt3080SystemType = _Pt3080SystemType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 30),
    _Pt3080SystemType_Type()
)
pt3080SystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemType.setStatus("current")


class _Pt3080SystemDateTimeSyncActual_Type(Integer32):
    """Custom type pt3080SystemDateTimeSyncActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1),
          ("gps", 2),
          ("ntp", 3))
    )


_Pt3080SystemDateTimeSyncActual_Type.__name__ = "Integer32"
_Pt3080SystemDateTimeSyncActual_Object = MibScalar
pt3080SystemDateTimeSyncActual = _Pt3080SystemDateTimeSyncActual_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 31),
    _Pt3080SystemDateTimeSyncActual_Type()
)
pt3080SystemDateTimeSyncActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemDateTimeSyncActual.setStatus("current")


class _Pt3080SystemModulationStandard_Type(Integer32):
    """Custom type pt3080SystemModulationStandard based on Integer32"""
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
        *(("dvbt", 0),
          ("dvbt2", 1),
          ("atsc", 2),
          ("isdbt", 3),
          ("iboc", 4))
    )


_Pt3080SystemModulationStandard_Type.__name__ = "Integer32"
_Pt3080SystemModulationStandard_Object = MibScalar
pt3080SystemModulationStandard = _Pt3080SystemModulationStandard_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 32),
    _Pt3080SystemModulationStandard_Type()
)
pt3080SystemModulationStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemModulationStandard.setStatus("current")


class _Pt3080SystemLanguage_Type(Integer32):
    """Custom type pt3080SystemLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("c", 0),
          ("da-dk", 1),
          ("ru-ru", 2),
          ("es-es", 3),
          ("pt-br", 4),
          ("it-it", 5),
          ("de-de", 6),
          ("fr-fr", 7))
    )


_Pt3080SystemLanguage_Type.__name__ = "Integer32"
_Pt3080SystemLanguage_Object = MibScalar
pt3080SystemLanguage = _Pt3080SystemLanguage_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 33),
    _Pt3080SystemLanguage_Type()
)
pt3080SystemLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemLanguage.setStatus("current")
_Pt3080SystemOperationOnTime_Type = Integer32
_Pt3080SystemOperationOnTime_Object = MibScalar
pt3080SystemOperationOnTime = _Pt3080SystemOperationOnTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 34),
    _Pt3080SystemOperationOnTime_Type()
)
pt3080SystemOperationOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemOperationOnTime.setStatus("current")
if mibBuilder.loadTexts:
    pt3080SystemOperationOnTime.setUnits("1 secs")
_Pt3080SystemOperationOnAirTime_Type = Integer32
_Pt3080SystemOperationOnAirTime_Object = MibScalar
pt3080SystemOperationOnAirTime = _Pt3080SystemOperationOnAirTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 35),
    _Pt3080SystemOperationOnAirTime_Type()
)
pt3080SystemOperationOnAirTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemOperationOnAirTime.setStatus("current")
if mibBuilder.loadTexts:
    pt3080SystemOperationOnAirTime.setUnits("1 secs")
_Pt3080SystemOperationNumberOfBoots_Type = Integer32
_Pt3080SystemOperationNumberOfBoots_Object = MibScalar
pt3080SystemOperationNumberOfBoots = _Pt3080SystemOperationNumberOfBoots_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 36),
    _Pt3080SystemOperationNumberOfBoots_Type()
)
pt3080SystemOperationNumberOfBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemOperationNumberOfBoots.setStatus("current")
_Pt3080SystemBackplaneid_Type = Integer32
_Pt3080SystemBackplaneid_Object = MibScalar
pt3080SystemBackplaneid = _Pt3080SystemBackplaneid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 40),
    _Pt3080SystemBackplaneid_Type()
)
pt3080SystemBackplaneid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneid.setStatus("current")
_Pt3080SystemBackplaneIdRaw_Type = Integer32
_Pt3080SystemBackplaneIdRaw_Object = MibScalar
pt3080SystemBackplaneIdRaw = _Pt3080SystemBackplaneIdRaw_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 41),
    _Pt3080SystemBackplaneIdRaw_Type()
)
pt3080SystemBackplaneIdRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneIdRaw.setStatus("current")
_Pt3080SystemBackplaneIdPcb_Type = Integer32
_Pt3080SystemBackplaneIdPcb_Object = MibScalar
pt3080SystemBackplaneIdPcb = _Pt3080SystemBackplaneIdPcb_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 42),
    _Pt3080SystemBackplaneIdPcb_Type()
)
pt3080SystemBackplaneIdPcb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneIdPcb.setStatus("current")
_Pt3080SystemBackplaneIdCableOptions_Type = Integer32
_Pt3080SystemBackplaneIdCableOptions_Object = MibScalar
pt3080SystemBackplaneIdCableOptions = _Pt3080SystemBackplaneIdCableOptions_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 43),
    _Pt3080SystemBackplaneIdCableOptions_Type()
)
pt3080SystemBackplaneIdCableOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneIdCableOptions.setStatus("current")
_Pt3080SystemBackplaneIdMAnuf_Type = DisplayString
_Pt3080SystemBackplaneIdMAnuf_Object = MibScalar
pt3080SystemBackplaneIdMAnuf = _Pt3080SystemBackplaneIdMAnuf_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 44),
    _Pt3080SystemBackplaneIdMAnuf_Type()
)
pt3080SystemBackplaneIdMAnuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneIdMAnuf.setStatus("current")
_Pt3080SystemBackplaneCalibrationDate_Type = DisplayString
_Pt3080SystemBackplaneCalibrationDate_Object = MibScalar
pt3080SystemBackplaneCalibrationDate = _Pt3080SystemBackplaneCalibrationDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 45),
    _Pt3080SystemBackplaneCalibrationDate_Type()
)
pt3080SystemBackplaneCalibrationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneCalibrationDate.setStatus("current")
_Pt3080SystemBackplaneCalibrationSw_Type = Integer32
_Pt3080SystemBackplaneCalibrationSw_Object = MibScalar
pt3080SystemBackplaneCalibrationSw = _Pt3080SystemBackplaneCalibrationSw_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 46),
    _Pt3080SystemBackplaneCalibrationSw_Type()
)
pt3080SystemBackplaneCalibrationSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneCalibrationSw.setStatus("current")
_Pt3080SystemBackplaneIdPartlist_Type = Integer32
_Pt3080SystemBackplaneIdPartlist_Object = MibScalar
pt3080SystemBackplaneIdPartlist = _Pt3080SystemBackplaneIdPartlist_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 47),
    _Pt3080SystemBackplaneIdPartlist_Type()
)
pt3080SystemBackplaneIdPartlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SystemBackplaneIdPartlist.setStatus("current")
_Pt3080SystemScheduledActionTable_Object = MibTable
pt3080SystemScheduledActionTable = _Pt3080SystemScheduledActionTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50)
)
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionTable.setStatus("current")
_Pt3080SystemScheduledActionEntry_Object = MibTableRow
pt3080SystemScheduledActionEntry = _Pt3080SystemScheduledActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1)
)
pt3080SystemScheduledActionEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080SystemScheduledActionID"),
)
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionEntry.setStatus("current")


class _Pt3080SystemScheduledActionID_Type(Integer32):
    """Custom type pt3080SystemScheduledActionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Pt3080SystemScheduledActionID_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionID_Object = MibTableColumn
pt3080SystemScheduledActionID = _Pt3080SystemScheduledActionID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 1),
    _Pt3080SystemScheduledActionID_Type()
)
pt3080SystemScheduledActionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionID.setStatus("current")


class _Pt3080SystemScheduledActionRecurrence_Type(Integer32):
    """Custom type pt3080SystemScheduledActionRecurrence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("never", 0),
          ("immediate", 1),
          ("once", 2),
          ("hourly", 3),
          ("daily", 4),
          ("weekly", 5),
          ("monthly", 6))
    )


_Pt3080SystemScheduledActionRecurrence_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionRecurrence_Object = MibTableColumn
pt3080SystemScheduledActionRecurrence = _Pt3080SystemScheduledActionRecurrence_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 2),
    _Pt3080SystemScheduledActionRecurrence_Type()
)
pt3080SystemScheduledActionRecurrence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionRecurrence.setStatus("current")


class _Pt3080SystemScheduledActionHour_Type(Integer32):
    """Custom type pt3080SystemScheduledActionHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Pt3080SystemScheduledActionHour_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionHour_Object = MibTableColumn
pt3080SystemScheduledActionHour = _Pt3080SystemScheduledActionHour_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 3),
    _Pt3080SystemScheduledActionHour_Type()
)
pt3080SystemScheduledActionHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionHour.setStatus("current")


class _Pt3080SystemScheduledActionMinute_Type(Integer32):
    """Custom type pt3080SystemScheduledActionMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Pt3080SystemScheduledActionMinute_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionMinute_Object = MibTableColumn
pt3080SystemScheduledActionMinute = _Pt3080SystemScheduledActionMinute_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 4),
    _Pt3080SystemScheduledActionMinute_Type()
)
pt3080SystemScheduledActionMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionMinute.setStatus("current")


class _Pt3080SystemScheduledActionWeekday_Type(Integer32):
    """Custom type pt3080SystemScheduledActionWeekday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("monday", 0),
          ("tuesday", 1),
          ("wednesday", 2),
          ("thursday", 3),
          ("friday", 4),
          ("saturday", 5),
          ("sunday", 6))
    )


_Pt3080SystemScheduledActionWeekday_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionWeekday_Object = MibTableColumn
pt3080SystemScheduledActionWeekday = _Pt3080SystemScheduledActionWeekday_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 5),
    _Pt3080SystemScheduledActionWeekday_Type()
)
pt3080SystemScheduledActionWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionWeekday.setStatus("current")


class _Pt3080SystemScheduledActionMonthDay_Type(Integer32):
    """Custom type pt3080SystemScheduledActionMonthDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Pt3080SystemScheduledActionMonthDay_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionMonthDay_Object = MibTableColumn
pt3080SystemScheduledActionMonthDay = _Pt3080SystemScheduledActionMonthDay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 6),
    _Pt3080SystemScheduledActionMonthDay_Type()
)
pt3080SystemScheduledActionMonthDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionMonthDay.setStatus("current")
_Pt3080SystemScheduledActionDate_Type = DisplayString
_Pt3080SystemScheduledActionDate_Object = MibTableColumn
pt3080SystemScheduledActionDate = _Pt3080SystemScheduledActionDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 7),
    _Pt3080SystemScheduledActionDate_Type()
)
pt3080SystemScheduledActionDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionDate.setStatus("current")


class _Pt3080SystemScheduledActionRandomDelay_Type(Integer32):
    """Custom type pt3080SystemScheduledActionRandomDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Pt3080SystemScheduledActionRandomDelay_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionRandomDelay_Object = MibTableColumn
pt3080SystemScheduledActionRandomDelay = _Pt3080SystemScheduledActionRandomDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 8),
    _Pt3080SystemScheduledActionRandomDelay_Type()
)
pt3080SystemScheduledActionRandomDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionRandomDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionRandomDelay.setUnits("secs")


class _Pt3080SystemScheduledActionAction_Type(Integer32):
    """Custom type pt3080SystemScheduledActionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("repeatermode", 1),
          ("preset", 2),
          ("swupgrade", 3),
          ("reboot", 4),
          ("mute", 5))
    )


_Pt3080SystemScheduledActionAction_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionAction_Object = MibTableColumn
pt3080SystemScheduledActionAction = _Pt3080SystemScheduledActionAction_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 9),
    _Pt3080SystemScheduledActionAction_Type()
)
pt3080SystemScheduledActionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionAction.setStatus("current")


class _Pt3080SystemScheduledActionRepeaterMode_Type(Integer32):
    """Custom type pt3080SystemScheduledActionRepeaterMode based on Integer32"""
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
        *(("auto", 0),
          ("digital-iso-repeater", 1),
          ("digital-transposer", 2),
          ("analog-iso-repeater", 3),
          ("analog-transposer", 4))
    )


_Pt3080SystemScheduledActionRepeaterMode_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionRepeaterMode_Object = MibTableColumn
pt3080SystemScheduledActionRepeaterMode = _Pt3080SystemScheduledActionRepeaterMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 10),
    _Pt3080SystemScheduledActionRepeaterMode_Type()
)
pt3080SystemScheduledActionRepeaterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionRepeaterMode.setStatus("current")


class _Pt3080SystemScheduledActionPresetNo_Type(Integer32):
    """Custom type pt3080SystemScheduledActionPresetNo based on Integer32"""
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
        *(("auto", 0),
          ("digital-iso-repeater", 1),
          ("digital-transposer", 2),
          ("analog-iso-repeater", 3),
          ("analog-transposer", 4))
    )


_Pt3080SystemScheduledActionPresetNo_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionPresetNo_Object = MibTableColumn
pt3080SystemScheduledActionPresetNo = _Pt3080SystemScheduledActionPresetNo_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 11),
    _Pt3080SystemScheduledActionPresetNo_Type()
)
pt3080SystemScheduledActionPresetNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionPresetNo.setStatus("current")


class _Pt3080SystemScheduledActionRebootImage_Type(Integer32):
    """Custom type pt3080SystemScheduledActionRebootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sameimage", 0),
          ("otherimage", 1),
          ("image0", 2),
          ("image1", 3))
    )


_Pt3080SystemScheduledActionRebootImage_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionRebootImage_Object = MibTableColumn
pt3080SystemScheduledActionRebootImage = _Pt3080SystemScheduledActionRebootImage_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 12),
    _Pt3080SystemScheduledActionRebootImage_Type()
)
pt3080SystemScheduledActionRebootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionRebootImage.setStatus("current")


class _Pt3080SystemScheduledActionRebootSystemType_Type(Integer32):
    """Custom type pt3080SystemScheduledActionRebootSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulator", 0),
          ("repeater", 1),
          ("same", 2))
    )


_Pt3080SystemScheduledActionRebootSystemType_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionRebootSystemType_Object = MibTableColumn
pt3080SystemScheduledActionRebootSystemType = _Pt3080SystemScheduledActionRebootSystemType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 13),
    _Pt3080SystemScheduledActionRebootSystemType_Type()
)
pt3080SystemScheduledActionRebootSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionRebootSystemType.setStatus("current")


class _Pt3080SystemScheduledActionMute_Type(Integer32):
    """Custom type pt3080SystemScheduledActionMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080SystemScheduledActionMute_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionMute_Object = MibTableColumn
pt3080SystemScheduledActionMute = _Pt3080SystemScheduledActionMute_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 14),
    _Pt3080SystemScheduledActionMute_Type()
)
pt3080SystemScheduledActionMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionMute.setStatus("current")


class _Pt3080SystemScheduledActionSWUpgradeProtocol_Type(Integer32):
    """Custom type pt3080SystemScheduledActionSWUpgradeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("http", 0),
          ("ftp", 1))
    )


_Pt3080SystemScheduledActionSWUpgradeProtocol_Type.__name__ = "Integer32"
_Pt3080SystemScheduledActionSWUpgradeProtocol_Object = MibTableColumn
pt3080SystemScheduledActionSWUpgradeProtocol = _Pt3080SystemScheduledActionSWUpgradeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 15),
    _Pt3080SystemScheduledActionSWUpgradeProtocol_Type()
)
pt3080SystemScheduledActionSWUpgradeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionSWUpgradeProtocol.setStatus("current")
_Pt3080SystemScheduledActionSWUpgradeUsername_Type = DisplayString
_Pt3080SystemScheduledActionSWUpgradeUsername_Object = MibTableColumn
pt3080SystemScheduledActionSWUpgradeUsername = _Pt3080SystemScheduledActionSWUpgradeUsername_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 16),
    _Pt3080SystemScheduledActionSWUpgradeUsername_Type()
)
pt3080SystemScheduledActionSWUpgradeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionSWUpgradeUsername.setStatus("current")
_Pt3080SystemScheduledActionSWUpgradePassword_Type = DisplayString
_Pt3080SystemScheduledActionSWUpgradePassword_Object = MibTableColumn
pt3080SystemScheduledActionSWUpgradePassword = _Pt3080SystemScheduledActionSWUpgradePassword_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 17),
    _Pt3080SystemScheduledActionSWUpgradePassword_Type()
)
pt3080SystemScheduledActionSWUpgradePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionSWUpgradePassword.setStatus("current")
_Pt3080SystemScheduledActionSWUpgradeImageServer_Type = DisplayString
_Pt3080SystemScheduledActionSWUpgradeImageServer_Object = MibTableColumn
pt3080SystemScheduledActionSWUpgradeImageServer = _Pt3080SystemScheduledActionSWUpgradeImageServer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 18),
    _Pt3080SystemScheduledActionSWUpgradeImageServer_Type()
)
pt3080SystemScheduledActionSWUpgradeImageServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionSWUpgradeImageServer.setStatus("current")
_Pt3080SystemScheduledActionSWUpgradeImagePath_Type = DisplayString
_Pt3080SystemScheduledActionSWUpgradeImagePath_Object = MibTableColumn
pt3080SystemScheduledActionSWUpgradeImagePath = _Pt3080SystemScheduledActionSWUpgradeImagePath_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 1, 50, 1, 19),
    _Pt3080SystemScheduledActionSWUpgradeImagePath_Type()
)
pt3080SystemScheduledActionSWUpgradeImagePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SystemScheduledActionSWUpgradeImagePath.setStatus("current")
_Pt3080Mode_ObjectIdentity = ObjectIdentity
pt3080Mode = _Pt3080Mode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2)
)


class _Pt3080ModeNetwork_Type(Integer32):
    """Custom type pt3080ModeNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("network-mode-mfn", 0),
          ("network-mode-sfn", 1))
    )


_Pt3080ModeNetwork_Type.__name__ = "Integer32"
_Pt3080ModeNetwork_Object = MibScalar
pt3080ModeNetwork = _Pt3080ModeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 1),
    _Pt3080ModeNetwork_Type()
)
pt3080ModeNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeNetwork.setStatus("current")


class _Pt3080ModeHierarchy_Type(Integer32):
    """Custom type pt3080ModeHierarchy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network-hierarchy-none", 0),
          ("network-hierarchy-h1", 1),
          ("network-hierarchy-h2", 2),
          ("network-hierarchy-h4", 3))
    )


_Pt3080ModeHierarchy_Type.__name__ = "Integer32"
_Pt3080ModeHierarchy_Object = MibScalar
pt3080ModeHierarchy = _Pt3080ModeHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 2),
    _Pt3080ModeHierarchy_Type()
)
pt3080ModeHierarchy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeHierarchy.setStatus("current")


class _Pt3080Modeifft_Type(Integer32):
    """Custom type pt3080Modeifft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifft-mode-2k", 0),
          ("ifft-mode-4k", 1),
          ("ifft-mode-8k", 2))
    )


_Pt3080Modeifft_Type.__name__ = "Integer32"
_Pt3080Modeifft_Object = MibScalar
pt3080Modeifft = _Pt3080Modeifft_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 3),
    _Pt3080Modeifft_Type()
)
pt3080Modeifft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Modeifft.setStatus("current")


class _Pt3080ModeCodeRateHighPrio_Type(Integer32):
    """Custom type pt3080ModeCodeRateHighPrio based on Integer32"""
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
        *(("code-rate-1-2", 0),
          ("code-rate-2-3", 1),
          ("code-rate-3-4", 2),
          ("code-rate-5-6", 3),
          ("code-rate-7-8", 4))
    )


_Pt3080ModeCodeRateHighPrio_Type.__name__ = "Integer32"
_Pt3080ModeCodeRateHighPrio_Object = MibScalar
pt3080ModeCodeRateHighPrio = _Pt3080ModeCodeRateHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 4),
    _Pt3080ModeCodeRateHighPrio_Type()
)
pt3080ModeCodeRateHighPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeCodeRateHighPrio.setStatus("current")


class _Pt3080ModeCodeRateLowPrio_Type(Integer32):
    """Custom type pt3080ModeCodeRateLowPrio based on Integer32"""
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
        *(("code-rate-1-2", 0),
          ("code-rate-2-3", 1),
          ("code-rate-3-4", 2),
          ("code-rate-5-6", 3),
          ("code-rate-7-8", 4))
    )


_Pt3080ModeCodeRateLowPrio_Type.__name__ = "Integer32"
_Pt3080ModeCodeRateLowPrio_Object = MibScalar
pt3080ModeCodeRateLowPrio = _Pt3080ModeCodeRateLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 5),
    _Pt3080ModeCodeRateLowPrio_Type()
)
pt3080ModeCodeRateLowPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeCodeRateLowPrio.setStatus("current")


class _Pt3080ModeConstellation_Type(Integer32):
    """Custom type pt3080ModeConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qpsk", 0),
          ("qam16", 1),
          ("qam64", 2))
    )


_Pt3080ModeConstellation_Type.__name__ = "Integer32"
_Pt3080ModeConstellation_Object = MibScalar
pt3080ModeConstellation = _Pt3080ModeConstellation_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 6),
    _Pt3080ModeConstellation_Type()
)
pt3080ModeConstellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeConstellation.setStatus("current")


class _Pt3080ModeGuardInterval_Type(Integer32):
    """Custom type pt3080ModeGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("guard-1-32", 0),
          ("guard-1-16", 1),
          ("guard-1-8", 2),
          ("guard-1-4", 3))
    )


_Pt3080ModeGuardInterval_Type.__name__ = "Integer32"
_Pt3080ModeGuardInterval_Object = MibScalar
pt3080ModeGuardInterval = _Pt3080ModeGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 7),
    _Pt3080ModeGuardInterval_Type()
)
pt3080ModeGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeGuardInterval.setStatus("current")


class _Pt3080ModeCellID_Type(Integer32):
    """Custom type pt3080ModeCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080ModeCellID_Type.__name__ = "Integer32"
_Pt3080ModeCellID_Object = MibScalar
pt3080ModeCellID = _Pt3080ModeCellID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 8),
    _Pt3080ModeCellID_Type()
)
pt3080ModeCellID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeCellID.setStatus("current")


class _Pt3080ModeEnableCellID_Type(Integer32):
    """Custom type pt3080ModeEnableCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeEnableCellID_Type.__name__ = "Integer32"
_Pt3080ModeEnableCellID_Object = MibScalar
pt3080ModeEnableCellID = _Pt3080ModeEnableCellID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 9),
    _Pt3080ModeEnableCellID_Type()
)
pt3080ModeEnableCellID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeEnableCellID.setStatus("current")


class _Pt3080ModeDeepInterleaver_Type(Integer32):
    """Custom type pt3080ModeDeepInterleaver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeDeepInterleaver_Type.__name__ = "Integer32"
_Pt3080ModeDeepInterleaver_Object = MibScalar
pt3080ModeDeepInterleaver = _Pt3080ModeDeepInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 10),
    _Pt3080ModeDeepInterleaver_Type()
)
pt3080ModeDeepInterleaver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeDeepInterleaver.setStatus("current")


class _Pt3080ModeEnableDVBH_Type(Integer32):
    """Custom type pt3080ModeEnableDVBH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeEnableDVBH_Type.__name__ = "Integer32"
_Pt3080ModeEnableDVBH_Object = MibScalar
pt3080ModeEnableDVBH = _Pt3080ModeEnableDVBH_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 11),
    _Pt3080ModeEnableDVBH_Type()
)
pt3080ModeEnableDVBH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeEnableDVBH.setStatus("current")


class _Pt3080ModeMpeFecLowPrio_Type(Integer32):
    """Custom type pt3080ModeMpeFecLowPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMpeFecLowPrio_Type.__name__ = "Integer32"
_Pt3080ModeMpeFecLowPrio_Object = MibScalar
pt3080ModeMpeFecLowPrio = _Pt3080ModeMpeFecLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 12),
    _Pt3080ModeMpeFecLowPrio_Type()
)
pt3080ModeMpeFecLowPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMpeFecLowPrio.setStatus("current")


class _Pt3080ModeMpeFecHighPrio_Type(Integer32):
    """Custom type pt3080ModeMpeFecHighPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMpeFecHighPrio_Type.__name__ = "Integer32"
_Pt3080ModeMpeFecHighPrio_Object = MibScalar
pt3080ModeMpeFecHighPrio = _Pt3080ModeMpeFecHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 13),
    _Pt3080ModeMpeFecHighPrio_Type()
)
pt3080ModeMpeFecHighPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMpeFecHighPrio.setStatus("current")


class _Pt3080ModeTimeSlicingLowPrio_Type(Integer32):
    """Custom type pt3080ModeTimeSlicingLowPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeTimeSlicingLowPrio_Type.__name__ = "Integer32"
_Pt3080ModeTimeSlicingLowPrio_Object = MibScalar
pt3080ModeTimeSlicingLowPrio = _Pt3080ModeTimeSlicingLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 14),
    _Pt3080ModeTimeSlicingLowPrio_Type()
)
pt3080ModeTimeSlicingLowPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeTimeSlicingLowPrio.setStatus("current")


class _Pt3080ModeTimeSlicingHighPrio_Type(Integer32):
    """Custom type pt3080ModeTimeSlicingHighPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeTimeSlicingHighPrio_Type.__name__ = "Integer32"
_Pt3080ModeTimeSlicingHighPrio_Object = MibScalar
pt3080ModeTimeSlicingHighPrio = _Pt3080ModeTimeSlicingHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 15),
    _Pt3080ModeTimeSlicingHighPrio_Type()
)
pt3080ModeTimeSlicingHighPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeTimeSlicingHighPrio.setStatus("current")


class _Pt3080ModeSfnDelayOffset_Type(Integer32):
    """Custom type pt3080ModeSfnDelayOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999999, 9999999),
    )


_Pt3080ModeSfnDelayOffset_Type.__name__ = "Integer32"
_Pt3080ModeSfnDelayOffset_Object = MibScalar
pt3080ModeSfnDelayOffset = _Pt3080ModeSfnDelayOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 16),
    _Pt3080ModeSfnDelayOffset_Type()
)
pt3080ModeSfnDelayOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeSfnDelayOffset.setStatus("current")


class _Pt3080ModeTxIdent_Type(Integer32):
    """Custom type pt3080ModeTxIdent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080ModeTxIdent_Type.__name__ = "Integer32"
_Pt3080ModeTxIdent_Object = MibScalar
pt3080ModeTxIdent = _Pt3080ModeTxIdent_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 17),
    _Pt3080ModeTxIdent_Type()
)
pt3080ModeTxIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeTxIdent.setStatus("current")


class _Pt3080ModeMipControl_Type(Integer32):
    """Custom type pt3080ModeMipControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMipControl_Type.__name__ = "Integer32"
_Pt3080ModeMipControl_Object = MibScalar
pt3080ModeMipControl = _Pt3080ModeMipControl_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 18),
    _Pt3080ModeMipControl_Type()
)
pt3080ModeMipControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMipControl.setStatus("current")


class _Pt3080ModeMfnKeepNullPackets_Type(Integer32):
    """Custom type pt3080ModeMfnKeepNullPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMfnKeepNullPackets_Type.__name__ = "Integer32"
_Pt3080ModeMfnKeepNullPackets_Object = MibScalar
pt3080ModeMfnKeepNullPackets = _Pt3080ModeMfnKeepNullPackets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 19),
    _Pt3080ModeMfnKeepNullPackets_Type()
)
pt3080ModeMfnKeepNullPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMfnKeepNullPackets.setStatus("current")
_Pt3080ModeNetworkDelayHP_Type = Integer32
_Pt3080ModeNetworkDelayHP_Object = MibScalar
pt3080ModeNetworkDelayHP = _Pt3080ModeNetworkDelayHP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 20),
    _Pt3080ModeNetworkDelayHP_Type()
)
pt3080ModeNetworkDelayHP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayHP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayHP.setUnits("100ns")
_Pt3080ModeNetworkDelayMinHP_Type = Integer32
_Pt3080ModeNetworkDelayMinHP_Object = MibScalar
pt3080ModeNetworkDelayMinHP = _Pt3080ModeNetworkDelayMinHP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 21),
    _Pt3080ModeNetworkDelayMinHP_Type()
)
pt3080ModeNetworkDelayMinHP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMinHP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMinHP.setUnits("100ns")
_Pt3080ModeNetworkDelayMaxHP_Type = Integer32
_Pt3080ModeNetworkDelayMaxHP_Object = MibScalar
pt3080ModeNetworkDelayMaxHP = _Pt3080ModeNetworkDelayMaxHP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 22),
    _Pt3080ModeNetworkDelayMaxHP_Type()
)
pt3080ModeNetworkDelayMaxHP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMaxHP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMaxHP.setUnits("100ns")
_Pt3080ModeMaxNetworkDelayHP_Type = Integer32
_Pt3080ModeMaxNetworkDelayHP_Object = MibScalar
pt3080ModeMaxNetworkDelayHP = _Pt3080ModeMaxNetworkDelayHP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 23),
    _Pt3080ModeMaxNetworkDelayHP_Type()
)
pt3080ModeMaxNetworkDelayHP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeMaxNetworkDelayHP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeMaxNetworkDelayHP.setUnits("100ns")
_Pt3080ModeNetworkDelayMarginHP_Type = Integer32
_Pt3080ModeNetworkDelayMarginHP_Object = MibScalar
pt3080ModeNetworkDelayMarginHP = _Pt3080ModeNetworkDelayMarginHP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 24),
    _Pt3080ModeNetworkDelayMarginHP_Type()
)
pt3080ModeNetworkDelayMarginHP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMarginHP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMarginHP.setUnits("100ns")
_Pt3080ModeNetworkDelayLP_Type = Integer32
_Pt3080ModeNetworkDelayLP_Object = MibScalar
pt3080ModeNetworkDelayLP = _Pt3080ModeNetworkDelayLP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 25),
    _Pt3080ModeNetworkDelayLP_Type()
)
pt3080ModeNetworkDelayLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayLP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayLP.setUnits("100ns")
_Pt3080ModeNetworkDelayMinLP_Type = Integer32
_Pt3080ModeNetworkDelayMinLP_Object = MibScalar
pt3080ModeNetworkDelayMinLP = _Pt3080ModeNetworkDelayMinLP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 26),
    _Pt3080ModeNetworkDelayMinLP_Type()
)
pt3080ModeNetworkDelayMinLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMinLP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMinLP.setUnits("100ns")
_Pt3080ModeNetworkDelayMaxLP_Type = Integer32
_Pt3080ModeNetworkDelayMaxLP_Object = MibScalar
pt3080ModeNetworkDelayMaxLP = _Pt3080ModeNetworkDelayMaxLP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 27),
    _Pt3080ModeNetworkDelayMaxLP_Type()
)
pt3080ModeNetworkDelayMaxLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMaxLP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMaxLP.setUnits("100ns")
_Pt3080ModeMaxNetworkDelayLP_Type = Integer32
_Pt3080ModeMaxNetworkDelayLP_Object = MibScalar
pt3080ModeMaxNetworkDelayLP = _Pt3080ModeMaxNetworkDelayLP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 28),
    _Pt3080ModeMaxNetworkDelayLP_Type()
)
pt3080ModeMaxNetworkDelayLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeMaxNetworkDelayLP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeMaxNetworkDelayLP.setUnits("100ns")
_Pt3080ModeNetworkDelayMarginLP_Type = Integer32
_Pt3080ModeNetworkDelayMarginLP_Object = MibScalar
pt3080ModeNetworkDelayMarginLP = _Pt3080ModeNetworkDelayMarginLP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 29),
    _Pt3080ModeNetworkDelayMarginLP_Type()
)
pt3080ModeNetworkDelayMarginLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMarginLP.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayMarginLP.setUnits("100ns")


class _Pt3080ModeNetworkDelayReset_Type(Integer32):
    """Custom type pt3080ModeNetworkDelayReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("reset", 1))
    )


_Pt3080ModeNetworkDelayReset_Type.__name__ = "Integer32"
_Pt3080ModeNetworkDelayReset_Object = MibScalar
pt3080ModeNetworkDelayReset = _Pt3080ModeNetworkDelayReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 30),
    _Pt3080ModeNetworkDelayReset_Type()
)
pt3080ModeNetworkDelayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeNetworkDelayReset.setStatus("current")


class _Pt3080ModeDefaultMIPOutputPower_Type(Integer32):
    """Custom type pt3080ModeDefaultMIPOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pt3080ModeDefaultMIPOutputPower_Type.__name__ = "Integer32"
_Pt3080ModeDefaultMIPOutputPower_Object = MibScalar
pt3080ModeDefaultMIPOutputPower = _Pt3080ModeDefaultMIPOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 31),
    _Pt3080ModeDefaultMIPOutputPower_Type()
)
pt3080ModeDefaultMIPOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeDefaultMIPOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeDefaultMIPOutputPower.setUnits("0.1 dBm")


class _Pt3080ModeDefaultMIPOutputTimeOffset_Type(Integer32):
    """Custom type pt3080ModeDefaultMIPOutputTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999999, 9999999),
    )


_Pt3080ModeDefaultMIPOutputTimeOffset_Type.__name__ = "Integer32"
_Pt3080ModeDefaultMIPOutputTimeOffset_Object = MibScalar
pt3080ModeDefaultMIPOutputTimeOffset = _Pt3080ModeDefaultMIPOutputTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 32),
    _Pt3080ModeDefaultMIPOutputTimeOffset_Type()
)
pt3080ModeDefaultMIPOutputTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeDefaultMIPOutputTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeDefaultMIPOutputTimeOffset.setUnits("x100ns")


class _Pt3080ModeDefaultMIPOutputCellID_Type(Integer32):
    """Custom type pt3080ModeDefaultMIPOutputCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080ModeDefaultMIPOutputCellID_Type.__name__ = "Integer32"
_Pt3080ModeDefaultMIPOutputCellID_Object = MibScalar
pt3080ModeDefaultMIPOutputCellID = _Pt3080ModeDefaultMIPOutputCellID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 33),
    _Pt3080ModeDefaultMIPOutputCellID_Type()
)
pt3080ModeDefaultMIPOutputCellID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeDefaultMIPOutputCellID.setStatus("current")


class _Pt3080ModeDefaultMIPOutputFreqOffset_Type(Integer32):
    """Custom type pt3080ModeDefaultMIPOutputFreqOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8388608, 8388607),
    )


_Pt3080ModeDefaultMIPOutputFreqOffset_Type.__name__ = "Integer32"
_Pt3080ModeDefaultMIPOutputFreqOffset_Object = MibScalar
pt3080ModeDefaultMIPOutputFreqOffset = _Pt3080ModeDefaultMIPOutputFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 34),
    _Pt3080ModeDefaultMIPOutputFreqOffset_Type()
)
pt3080ModeDefaultMIPOutputFreqOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeDefaultMIPOutputFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeDefaultMIPOutputFreqOffset.setUnits("Hz")
_Pt3080ModeMIPMaxSFNDelay_Type = Integer32
_Pt3080ModeMIPMaxSFNDelay_Object = MibScalar
pt3080ModeMIPMaxSFNDelay = _Pt3080ModeMIPMaxSFNDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 35),
    _Pt3080ModeMIPMaxSFNDelay_Type()
)
pt3080ModeMIPMaxSFNDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ModeMIPMaxSFNDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ModeMIPMaxSFNDelay.setUnits("x100ns")


class _Pt3080ModeMipControlOutputPower_Type(Integer32):
    """Custom type pt3080ModeMipControlOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMipControlOutputPower_Type.__name__ = "Integer32"
_Pt3080ModeMipControlOutputPower_Object = MibScalar
pt3080ModeMipControlOutputPower = _Pt3080ModeMipControlOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 36),
    _Pt3080ModeMipControlOutputPower_Type()
)
pt3080ModeMipControlOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMipControlOutputPower.setStatus("current")


class _Pt3080ModeMipControlOutputTimeOffset_Type(Integer32):
    """Custom type pt3080ModeMipControlOutputTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMipControlOutputTimeOffset_Type.__name__ = "Integer32"
_Pt3080ModeMipControlOutputTimeOffset_Object = MibScalar
pt3080ModeMipControlOutputTimeOffset = _Pt3080ModeMipControlOutputTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 37),
    _Pt3080ModeMipControlOutputTimeOffset_Type()
)
pt3080ModeMipControlOutputTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMipControlOutputTimeOffset.setStatus("current")


class _Pt3080ModeMipControlOutputCellId_Type(Integer32):
    """Custom type pt3080ModeMipControlOutputCellId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMipControlOutputCellId_Type.__name__ = "Integer32"
_Pt3080ModeMipControlOutputCellId_Object = MibScalar
pt3080ModeMipControlOutputCellId = _Pt3080ModeMipControlOutputCellId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 38),
    _Pt3080ModeMipControlOutputCellId_Type()
)
pt3080ModeMipControlOutputCellId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMipControlOutputCellId.setStatus("current")


class _Pt3080ModeMipControlOutputFreqOffset_Type(Integer32):
    """Custom type pt3080ModeMipControlOutputFreqOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeMipControlOutputFreqOffset_Type.__name__ = "Integer32"
_Pt3080ModeMipControlOutputFreqOffset_Object = MibScalar
pt3080ModeMipControlOutputFreqOffset = _Pt3080ModeMipControlOutputFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 39),
    _Pt3080ModeMipControlOutputFreqOffset_Type()
)
pt3080ModeMipControlOutputFreqOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeMipControlOutputFreqOffset.setStatus("current")


class _Pt3080ModeListenBroadcast_Type(Integer32):
    """Custom type pt3080ModeListenBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ModeListenBroadcast_Type.__name__ = "Integer32"
_Pt3080ModeListenBroadcast_Object = MibScalar
pt3080ModeListenBroadcast = _Pt3080ModeListenBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 2, 40),
    _Pt3080ModeListenBroadcast_Type()
)
pt3080ModeListenBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ModeListenBroadcast.setStatus("current")
_Pt3080Input_ObjectIdentity = ObjectIdentity
pt3080Input = _Pt3080Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3)
)


class _Pt3080InputRefDirection_Type(Integer32):
    """Custom type pt3080InputRefDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("input", 0),
          ("output", 1))
    )


_Pt3080InputRefDirection_Type.__name__ = "Integer32"
_Pt3080InputRefDirection_Object = MibScalar
pt3080InputRefDirection = _Pt3080InputRefDirection_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 1),
    _Pt3080InputRefDirection_Type()
)
pt3080InputRefDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRefDirection.setStatus("current")


class _Pt3080InputRefSource_Type(Integer32):
    """Custom type pt3080InputRefSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("ext", 1),
          ("int", 2),
          ("gps", 3))
    )


_Pt3080InputRefSource_Type.__name__ = "Integer32"
_Pt3080InputRefSource_Object = MibScalar
pt3080InputRefSource = _Pt3080InputRefSource_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 2),
    _Pt3080InputRefSource_Type()
)
pt3080InputRefSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRefSource.setStatus("current")


class _Pt3080InputRef10MhzImpedance_Type(Integer32):
    """Custom type pt3080InputRef10MhzImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("o-50", 0),
          ("himp", 1))
    )


_Pt3080InputRef10MhzImpedance_Type.__name__ = "Integer32"
_Pt3080InputRef10MhzImpedance_Object = MibScalar
pt3080InputRef10MhzImpedance = _Pt3080InputRef10MhzImpedance_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 3),
    _Pt3080InputRef10MhzImpedance_Type()
)
pt3080InputRef10MhzImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef10MhzImpedance.setStatus("current")


class _Pt3080InputRef1PPSImpedance_Type(Integer32):
    """Custom type pt3080InputRef1PPSImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("o-50", 0),
          ("himp", 1))
    )


_Pt3080InputRef1PPSImpedance_Type.__name__ = "Integer32"
_Pt3080InputRef1PPSImpedance_Object = MibScalar
pt3080InputRef1PPSImpedance = _Pt3080InputRef1PPSImpedance_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 4),
    _Pt3080InputRef1PPSImpedance_Type()
)
pt3080InputRef1PPSImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef1PPSImpedance.setStatus("current")


class _Pt3080InputRef1PPSTrigSlope_Type(Integer32):
    """Custom type pt3080InputRef1PPSTrigSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rising", 0),
          ("falling", 1))
    )


_Pt3080InputRef1PPSTrigSlope_Type.__name__ = "Integer32"
_Pt3080InputRef1PPSTrigSlope_Object = MibScalar
pt3080InputRef1PPSTrigSlope = _Pt3080InputRef1PPSTrigSlope_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 5),
    _Pt3080InputRef1PPSTrigSlope_Type()
)
pt3080InputRef1PPSTrigSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef1PPSTrigSlope.setStatus("current")


class _Pt3080InputRef1PPSTrigLevel_Type(Integer32):
    """Custom type pt3080InputRef1PPSTrigLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 16),
    )


_Pt3080InputRef1PPSTrigLevel_Type.__name__ = "Integer32"
_Pt3080InputRef1PPSTrigLevel_Object = MibScalar
pt3080InputRef1PPSTrigLevel = _Pt3080InputRef1PPSTrigLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 6),
    _Pt3080InputRef1PPSTrigLevel_Type()
)
pt3080InputRef1PPSTrigLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef1PPSTrigLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputRef1PPSTrigLevel.setUnits("0.1 v")


class _Pt3080InputRef10MhzHoldoverDelay_Type(Integer32):
    """Custom type pt3080InputRef10MhzHoldoverDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 172800),
    )


_Pt3080InputRef10MhzHoldoverDelay_Type.__name__ = "Integer32"
_Pt3080InputRef10MhzHoldoverDelay_Object = MibScalar
pt3080InputRef10MhzHoldoverDelay = _Pt3080InputRef10MhzHoldoverDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 7),
    _Pt3080InputRef10MhzHoldoverDelay_Type()
)
pt3080InputRef10MhzHoldoverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef10MhzHoldoverDelay.setStatus("current")


class _Pt3080InputRef10MhzHoldoverForever_Type(Integer32):
    """Custom type pt3080InputRef10MhzHoldoverForever based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080InputRef10MhzHoldoverForever_Type.__name__ = "Integer32"
_Pt3080InputRef10MhzHoldoverForever_Object = MibScalar
pt3080InputRef10MhzHoldoverForever = _Pt3080InputRef10MhzHoldoverForever_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 8),
    _Pt3080InputRef10MhzHoldoverForever_Type()
)
pt3080InputRef10MhzHoldoverForever.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef10MhzHoldoverForever.setStatus("current")


class _Pt3080InputRef1PPSHoldoverDelay_Type(Integer32):
    """Custom type pt3080InputRef1PPSHoldoverDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 172800),
    )


_Pt3080InputRef1PPSHoldoverDelay_Type.__name__ = "Integer32"
_Pt3080InputRef1PPSHoldoverDelay_Object = MibScalar
pt3080InputRef1PPSHoldoverDelay = _Pt3080InputRef1PPSHoldoverDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 9),
    _Pt3080InputRef1PPSHoldoverDelay_Type()
)
pt3080InputRef1PPSHoldoverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef1PPSHoldoverDelay.setStatus("current")


class _Pt3080InputRef1PPSHoldoverForever_Type(Integer32):
    """Custom type pt3080InputRef1PPSHoldoverForever based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080InputRef1PPSHoldoverForever_Type.__name__ = "Integer32"
_Pt3080InputRef1PPSHoldoverForever_Object = MibScalar
pt3080InputRef1PPSHoldoverForever = _Pt3080InputRef1PPSHoldoverForever_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 10),
    _Pt3080InputRef1PPSHoldoverForever_Type()
)
pt3080InputRef1PPSHoldoverForever.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputRef1PPSHoldoverForever.setStatus("current")


class _Pt3080InputRefStatus_Type(Integer32):
    """Custom type pt3080InputRefStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("external", 0),
          ("external-10mhz", 1),
          ("external-1pps", 2),
          ("internal", 3),
          ("gnss", 4),
          ("asi1", 5),
          ("asi2", 6),
          ("ndel", 7))
    )


_Pt3080InputRefStatus_Type.__name__ = "Integer32"
_Pt3080InputRefStatus_Object = MibScalar
pt3080InputRefStatus = _Pt3080InputRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 11),
    _Pt3080InputRefStatus_Type()
)
pt3080InputRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputRefStatus.setStatus("current")


class _Pt3080InputASITSPrimarySource_Type(Integer32):
    """Custom type pt3080InputASITSPrimarySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("asi-in-1", 0),
          ("asi-in-2", 1),
          ("demodulator-1", 2),
          ("demodulator-2", 3),
          ("tsoip-rx1", 4),
          ("tsoip-rx2", 5),
          ("satRecv", 6))
    )


_Pt3080InputASITSPrimarySource_Type.__name__ = "Integer32"
_Pt3080InputASITSPrimarySource_Object = MibScalar
pt3080InputASITSPrimarySource = _Pt3080InputASITSPrimarySource_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 12),
    _Pt3080InputASITSPrimarySource_Type()
)
pt3080InputASITSPrimarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputASITSPrimarySource.setStatus("current")


class _Pt3080InputASITSSecondarySource_Type(Integer32):
    """Custom type pt3080InputASITSSecondarySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("asi-in-1", 0),
          ("asi-in-2", 1),
          ("demodulator-1", 2),
          ("demodulator-2", 3),
          ("tsoip-rx1", 4),
          ("tsoip-rx2", 5),
          ("satRecv", 6))
    )


_Pt3080InputASITSSecondarySource_Type.__name__ = "Integer32"
_Pt3080InputASITSSecondarySource_Object = MibScalar
pt3080InputASITSSecondarySource = _Pt3080InputASITSSecondarySource_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 13),
    _Pt3080InputASITSSecondarySource_Type()
)
pt3080InputASITSSecondarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputASITSSecondarySource.setStatus("current")


class _Pt3080InputASIAutoRoutingPolicy_Type(Integer32):
    """Custom type pt3080InputASIAutoRoutingPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("only-use-primary", 0),
          ("only-use-secondary", 1),
          ("use-primary-if-available", 2),
          ("use-any-available", 3))
    )


_Pt3080InputASIAutoRoutingPolicy_Type.__name__ = "Integer32"
_Pt3080InputASIAutoRoutingPolicy_Object = MibScalar
pt3080InputASIAutoRoutingPolicy = _Pt3080InputASIAutoRoutingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 14),
    _Pt3080InputASIAutoRoutingPolicy_Type()
)
pt3080InputASIAutoRoutingPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputASIAutoRoutingPolicy.setStatus("current")


class _Pt3080InputASIAutoRoutingDelayHp2Lp_Type(Integer32):
    """Custom type pt3080InputASIAutoRoutingDelayHp2Lp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Pt3080InputASIAutoRoutingDelayHp2Lp_Type.__name__ = "Integer32"
_Pt3080InputASIAutoRoutingDelayHp2Lp_Object = MibScalar
pt3080InputASIAutoRoutingDelayHp2Lp = _Pt3080InputASIAutoRoutingDelayHp2Lp_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 15),
    _Pt3080InputASIAutoRoutingDelayHp2Lp_Type()
)
pt3080InputASIAutoRoutingDelayHp2Lp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputASIAutoRoutingDelayHp2Lp.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputASIAutoRoutingDelayHp2Lp.setUnits("1 secs")


class _Pt3080InputASIAutoRoutingDelayLp2Hp_Type(Integer32):
    """Custom type pt3080InputASIAutoRoutingDelayLp2Hp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Pt3080InputASIAutoRoutingDelayLp2Hp_Type.__name__ = "Integer32"
_Pt3080InputASIAutoRoutingDelayLp2Hp_Object = MibScalar
pt3080InputASIAutoRoutingDelayLp2Hp = _Pt3080InputASIAutoRoutingDelayLp2Hp_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 16),
    _Pt3080InputASIAutoRoutingDelayLp2Hp_Type()
)
pt3080InputASIAutoRoutingDelayLp2Hp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputASIAutoRoutingDelayLp2Hp.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputASIAutoRoutingDelayLp2Hp.setUnits("1 secs")


class _Pt3080InputASIHoldoverTimeout_Type(Integer32):
    """Custom type pt3080InputASIHoldoverTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Pt3080InputASIHoldoverTimeout_Type.__name__ = "Integer32"
_Pt3080InputASIHoldoverTimeout_Object = MibScalar
pt3080InputASIHoldoverTimeout = _Pt3080InputASIHoldoverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 17),
    _Pt3080InputASIHoldoverTimeout_Type()
)
pt3080InputASIHoldoverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputASIHoldoverTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputASIHoldoverTimeout.setUnits("1 secs")


class _Pt3080InputTSPrimaryMaxPATDelay_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMaxPATDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_Pt3080InputTSPrimaryMaxPATDelay_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMaxPATDelay_Object = MibScalar
pt3080InputTSPrimaryMaxPATDelay = _Pt3080InputTSPrimaryMaxPATDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 18),
    _Pt3080InputTSPrimaryMaxPATDelay_Type()
)
pt3080InputTSPrimaryMaxPATDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxPATDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxPATDelay.setUnits("1 ms")


class _Pt3080InputTSPrimaryMaxPATDelayEnable_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMaxPATDelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSPrimaryMaxPATDelayEnable_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMaxPATDelayEnable_Object = MibScalar
pt3080InputTSPrimaryMaxPATDelayEnable = _Pt3080InputTSPrimaryMaxPATDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 19),
    _Pt3080InputTSPrimaryMaxPATDelayEnable_Type()
)
pt3080InputTSPrimaryMaxPATDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxPATDelayEnable.setStatus("current")


class _Pt3080InputTSPrimaryExpectedTSID_Type(Integer32):
    """Custom type pt3080InputTSPrimaryExpectedTSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080InputTSPrimaryExpectedTSID_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryExpectedTSID_Object = MibScalar
pt3080InputTSPrimaryExpectedTSID = _Pt3080InputTSPrimaryExpectedTSID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 20),
    _Pt3080InputTSPrimaryExpectedTSID_Type()
)
pt3080InputTSPrimaryExpectedTSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryExpectedTSID.setStatus("current")


class _Pt3080InputTSPrimaryExpectedTSIDEnable_Type(Integer32):
    """Custom type pt3080InputTSPrimaryExpectedTSIDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSPrimaryExpectedTSIDEnable_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryExpectedTSIDEnable_Object = MibScalar
pt3080InputTSPrimaryExpectedTSIDEnable = _Pt3080InputTSPrimaryExpectedTSIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 21),
    _Pt3080InputTSPrimaryExpectedTSIDEnable_Type()
)
pt3080InputTSPrimaryExpectedTSIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryExpectedTSIDEnable.setStatus("current")


class _Pt3080InputTSPrimaryExpectedNWID_Type(Integer32):
    """Custom type pt3080InputTSPrimaryExpectedNWID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080InputTSPrimaryExpectedNWID_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryExpectedNWID_Object = MibScalar
pt3080InputTSPrimaryExpectedNWID = _Pt3080InputTSPrimaryExpectedNWID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 22),
    _Pt3080InputTSPrimaryExpectedNWID_Type()
)
pt3080InputTSPrimaryExpectedNWID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryExpectedNWID.setStatus("current")


class _Pt3080InputTSPrimaryExpectedNWIDEnable_Type(Integer32):
    """Custom type pt3080InputTSPrimaryExpectedNWIDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSPrimaryExpectedNWIDEnable_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryExpectedNWIDEnable_Object = MibScalar
pt3080InputTSPrimaryExpectedNWIDEnable = _Pt3080InputTSPrimaryExpectedNWIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 23),
    _Pt3080InputTSPrimaryExpectedNWIDEnable_Type()
)
pt3080InputTSPrimaryExpectedNWIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryExpectedNWIDEnable.setStatus("current")


class _Pt3080InputTSPrimaryMaxStuffingrate_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMaxStuffingrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pt3080InputTSPrimaryMaxStuffingrate_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMaxStuffingrate_Object = MibScalar
pt3080InputTSPrimaryMaxStuffingrate = _Pt3080InputTSPrimaryMaxStuffingrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 24),
    _Pt3080InputTSPrimaryMaxStuffingrate_Type()
)
pt3080InputTSPrimaryMaxStuffingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxStuffingrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxStuffingrate.setUnits("1 %")


class _Pt3080InputTSPrimaryMaxStuffingrateEnable_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMaxStuffingrateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSPrimaryMaxStuffingrateEnable_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMaxStuffingrateEnable_Object = MibScalar
pt3080InputTSPrimaryMaxStuffingrateEnable = _Pt3080InputTSPrimaryMaxStuffingrateEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 25),
    _Pt3080InputTSPrimaryMaxStuffingrateEnable_Type()
)
pt3080InputTSPrimaryMaxStuffingrateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxStuffingrateEnable.setStatus("current")


class _Pt3080InputTSPrimaryMaxStsJitter_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMaxStsJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Pt3080InputTSPrimaryMaxStsJitter_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMaxStsJitter_Object = MibScalar
pt3080InputTSPrimaryMaxStsJitter = _Pt3080InputTSPrimaryMaxStsJitter_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 26),
    _Pt3080InputTSPrimaryMaxStsJitter_Type()
)
pt3080InputTSPrimaryMaxStsJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxStsJitter.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxStsJitter.setUnits("100ns")


class _Pt3080InputTSSecondaryMaxPATDelay_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMaxPATDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_Pt3080InputTSSecondaryMaxPATDelay_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMaxPATDelay_Object = MibScalar
pt3080InputTSSecondaryMaxPATDelay = _Pt3080InputTSSecondaryMaxPATDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 27),
    _Pt3080InputTSSecondaryMaxPATDelay_Type()
)
pt3080InputTSSecondaryMaxPATDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxPATDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxPATDelay.setUnits("1 ms")


class _Pt3080InputTSSecondaryMaxPATDelayEnable_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMaxPATDelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSSecondaryMaxPATDelayEnable_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMaxPATDelayEnable_Object = MibScalar
pt3080InputTSSecondaryMaxPATDelayEnable = _Pt3080InputTSSecondaryMaxPATDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 28),
    _Pt3080InputTSSecondaryMaxPATDelayEnable_Type()
)
pt3080InputTSSecondaryMaxPATDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxPATDelayEnable.setStatus("current")


class _Pt3080InputTSSecondaryExpectedTSID_Type(Integer32):
    """Custom type pt3080InputTSSecondaryExpectedTSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080InputTSSecondaryExpectedTSID_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryExpectedTSID_Object = MibScalar
pt3080InputTSSecondaryExpectedTSID = _Pt3080InputTSSecondaryExpectedTSID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 29),
    _Pt3080InputTSSecondaryExpectedTSID_Type()
)
pt3080InputTSSecondaryExpectedTSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryExpectedTSID.setStatus("current")


class _Pt3080InputTSSecondaryExpectedTSIDEnable_Type(Integer32):
    """Custom type pt3080InputTSSecondaryExpectedTSIDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSSecondaryExpectedTSIDEnable_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryExpectedTSIDEnable_Object = MibScalar
pt3080InputTSSecondaryExpectedTSIDEnable = _Pt3080InputTSSecondaryExpectedTSIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 30),
    _Pt3080InputTSSecondaryExpectedTSIDEnable_Type()
)
pt3080InputTSSecondaryExpectedTSIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryExpectedTSIDEnable.setStatus("current")


class _Pt3080InputTSSecondaryExpectedNWID_Type(Integer32):
    """Custom type pt3080InputTSSecondaryExpectedNWID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080InputTSSecondaryExpectedNWID_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryExpectedNWID_Object = MibScalar
pt3080InputTSSecondaryExpectedNWID = _Pt3080InputTSSecondaryExpectedNWID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 31),
    _Pt3080InputTSSecondaryExpectedNWID_Type()
)
pt3080InputTSSecondaryExpectedNWID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryExpectedNWID.setStatus("current")


class _Pt3080InputTSSecondaryExpectedNWIDEnable_Type(Integer32):
    """Custom type pt3080InputTSSecondaryExpectedNWIDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSSecondaryExpectedNWIDEnable_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryExpectedNWIDEnable_Object = MibScalar
pt3080InputTSSecondaryExpectedNWIDEnable = _Pt3080InputTSSecondaryExpectedNWIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 32),
    _Pt3080InputTSSecondaryExpectedNWIDEnable_Type()
)
pt3080InputTSSecondaryExpectedNWIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryExpectedNWIDEnable.setStatus("current")


class _Pt3080InputTSSecondaryMaxStuffingrate_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMaxStuffingrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pt3080InputTSSecondaryMaxStuffingrate_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMaxStuffingrate_Object = MibScalar
pt3080InputTSSecondaryMaxStuffingrate = _Pt3080InputTSSecondaryMaxStuffingrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 33),
    _Pt3080InputTSSecondaryMaxStuffingrate_Type()
)
pt3080InputTSSecondaryMaxStuffingrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxStuffingrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxStuffingrate.setUnits("1 %")


class _Pt3080InputTSSecondaryMaxStuffingrateEnable_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMaxStuffingrateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSSecondaryMaxStuffingrateEnable_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMaxStuffingrateEnable_Object = MibScalar
pt3080InputTSSecondaryMaxStuffingrateEnable = _Pt3080InputTSSecondaryMaxStuffingrateEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 34),
    _Pt3080InputTSSecondaryMaxStuffingrateEnable_Type()
)
pt3080InputTSSecondaryMaxStuffingrateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxStuffingrateEnable.setStatus("current")


class _Pt3080InputTSSecondaryMaxStsJitter_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMaxStsJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Pt3080InputTSSecondaryMaxStsJitter_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMaxStsJitter_Object = MibScalar
pt3080InputTSSecondaryMaxStsJitter = _Pt3080InputTSSecondaryMaxStsJitter_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 35),
    _Pt3080InputTSSecondaryMaxStsJitter_Type()
)
pt3080InputTSSecondaryMaxStsJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxStsJitter.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxStsJitter.setUnits("100ns")


class _Pt3080InputTSPrimaryStatus_Type(Integer32):
    """Custom type pt3080InputTSPrimaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1),
          ("nosync", 2))
    )


_Pt3080InputTSPrimaryStatus_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryStatus_Object = MibScalar
pt3080InputTSPrimaryStatus = _Pt3080InputTSPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 36),
    _Pt3080InputTSPrimaryStatus_Type()
)
pt3080InputTSPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStatus.setStatus("current")


class _Pt3080InputTSSecondaryStatus_Type(Integer32):
    """Custom type pt3080InputTSSecondaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1),
          ("nosync", 2))
    )


_Pt3080InputTSSecondaryStatus_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryStatus_Object = MibScalar
pt3080InputTSSecondaryStatus = _Pt3080InputTSSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 37),
    _Pt3080InputTSSecondaryStatus_Type()
)
pt3080InputTSSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStatus.setStatus("current")


class _Pt3080InputTSHp_Type(Integer32):
    """Custom type pt3080InputTSHp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("asi-in-1", 0),
          ("asi-in-2", 1),
          ("demodulator-1", 2),
          ("demodulator-2", 3),
          ("tsoip-rx1", 4),
          ("tsoip-rx2", 5),
          ("satRecv", 6))
    )


_Pt3080InputTSHp_Type.__name__ = "Integer32"
_Pt3080InputTSHp_Object = MibScalar
pt3080InputTSHp = _Pt3080InputTSHp_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 38),
    _Pt3080InputTSHp_Type()
)
pt3080InputTSHp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSHp.setStatus("current")


class _Pt3080InputTSLp_Type(Integer32):
    """Custom type pt3080InputTSLp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("asi-in-1", 0),
          ("asi-in-2", 1),
          ("demodulator-1", 2),
          ("demodulator-2", 3),
          ("tsoip-rx1", 4),
          ("tsoip-rx2", 5),
          ("satRecv", 6))
    )


_Pt3080InputTSLp_Type.__name__ = "Integer32"
_Pt3080InputTSLp_Object = MibScalar
pt3080InputTSLp = _Pt3080InputTSLp_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 39),
    _Pt3080InputTSLp_Type()
)
pt3080InputTSLp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSLp.setStatus("current")


class _Pt3080InputEffectiveAutoroutingPolicy_Type(Integer32):
    """Custom type pt3080InputEffectiveAutoroutingPolicy based on Integer32"""
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
        *(("only-primary", 0),
          ("only-secondary", 1),
          ("prefer-primary", 2),
          ("any-available", 3),
          ("seamless", 4))
    )


_Pt3080InputEffectiveAutoroutingPolicy_Type.__name__ = "Integer32"
_Pt3080InputEffectiveAutoroutingPolicy_Object = MibScalar
pt3080InputEffectiveAutoroutingPolicy = _Pt3080InputEffectiveAutoroutingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 40),
    _Pt3080InputEffectiveAutoroutingPolicy_Type()
)
pt3080InputEffectiveAutoroutingPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputEffectiveAutoroutingPolicy.setStatus("current")
_Pt3080InputTSHpBitrate_Type = Integer32
_Pt3080InputTSHpBitrate_Object = MibScalar
pt3080InputTSHpBitrate = _Pt3080InputTSHpBitrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 41),
    _Pt3080InputTSHpBitrate_Type()
)
pt3080InputTSHpBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSHpBitrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSHpBitrate.setUnits("Kb/s")
_Pt3080InputTSHpPacketsBuffered_Type = Integer32
_Pt3080InputTSHpPacketsBuffered_Object = MibScalar
pt3080InputTSHpPacketsBuffered = _Pt3080InputTSHpPacketsBuffered_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 42),
    _Pt3080InputTSHpPacketsBuffered_Type()
)
pt3080InputTSHpPacketsBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSHpPacketsBuffered.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSHpPacketsBuffered.setUnits("packets")
_Pt3080InputTSHpPacketSize_Type = Integer32
_Pt3080InputTSHpPacketSize_Object = MibScalar
pt3080InputTSHpPacketSize = _Pt3080InputTSHpPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 43),
    _Pt3080InputTSHpPacketSize_Type()
)
pt3080InputTSHpPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSHpPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSHpPacketSize.setUnits("bytes")
_Pt3080InputTSHpStuffingrate_Type = Integer32
_Pt3080InputTSHpStuffingrate_Object = MibScalar
pt3080InputTSHpStuffingrate = _Pt3080InputTSHpStuffingrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 44),
    _Pt3080InputTSHpStuffingrate_Type()
)
pt3080InputTSHpStuffingrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSHpStuffingrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSHpStuffingrate.setUnits("Kb/s")
_Pt3080InputTSHpTSID_Type = Integer32
_Pt3080InputTSHpTSID_Object = MibScalar
pt3080InputTSHpTSID = _Pt3080InputTSHpTSID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 45),
    _Pt3080InputTSHpTSID_Type()
)
pt3080InputTSHpTSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSHpTSID.setStatus("current")
_Pt3080InputTSHpNWID_Type = Integer32
_Pt3080InputTSHpNWID_Object = MibScalar
pt3080InputTSHpNWID = _Pt3080InputTSHpNWID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 46),
    _Pt3080InputTSHpNWID_Type()
)
pt3080InputTSHpNWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSHpNWID.setStatus("current")
_Pt3080InputTSLpBitrate_Type = Integer32
_Pt3080InputTSLpBitrate_Object = MibScalar
pt3080InputTSLpBitrate = _Pt3080InputTSLpBitrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 47),
    _Pt3080InputTSLpBitrate_Type()
)
pt3080InputTSLpBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSLpBitrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSLpBitrate.setUnits("Kb/s")
_Pt3080InputTSLpPacketsBuffered_Type = Integer32
_Pt3080InputTSLpPacketsBuffered_Object = MibScalar
pt3080InputTSLpPacketsBuffered = _Pt3080InputTSLpPacketsBuffered_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 48),
    _Pt3080InputTSLpPacketsBuffered_Type()
)
pt3080InputTSLpPacketsBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSLpPacketsBuffered.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSLpPacketsBuffered.setUnits("packets")
_Pt3080InputTSLpPacketSize_Type = Integer32
_Pt3080InputTSLpPacketSize_Object = MibScalar
pt3080InputTSLpPacketSize = _Pt3080InputTSLpPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 49),
    _Pt3080InputTSLpPacketSize_Type()
)
pt3080InputTSLpPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSLpPacketSize.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSLpPacketSize.setUnits("bytes")
_Pt3080InputTSLpStuffingrate_Type = Integer32
_Pt3080InputTSLpStuffingrate_Object = MibScalar
pt3080InputTSLpStuffingrate = _Pt3080InputTSLpStuffingrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 50),
    _Pt3080InputTSLpStuffingrate_Type()
)
pt3080InputTSLpStuffingrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSLpStuffingrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSLpStuffingrate.setUnits("Permille")
_Pt3080InputTSLpTSID_Type = Integer32
_Pt3080InputTSLpTSID_Object = MibScalar
pt3080InputTSLpTSID = _Pt3080InputTSLpTSID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 51),
    _Pt3080InputTSLpTSID_Type()
)
pt3080InputTSLpTSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSLpTSID.setStatus("current")
_Pt3080InputTSLpNWID_Type = Integer32
_Pt3080InputTSLpNWID_Object = MibScalar
pt3080InputTSLpNWID = _Pt3080InputTSLpNWID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 52),
    _Pt3080InputTSLpNWID_Type()
)
pt3080InputTSLpNWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSLpNWID.setStatus("current")
_Pt3080InputTSPrimaryStsJitter_Type = Integer32
_Pt3080InputTSPrimaryStsJitter_Object = MibScalar
pt3080InputTSPrimaryStsJitter = _Pt3080InputTSPrimaryStsJitter_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 53),
    _Pt3080InputTSPrimaryStsJitter_Type()
)
pt3080InputTSPrimaryStsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStsJitter.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStsJitter.setUnits("100ns")
_Pt3080InputTSPrimaryStsJitterMax_Type = Integer32
_Pt3080InputTSPrimaryStsJitterMax_Object = MibScalar
pt3080InputTSPrimaryStsJitterMax = _Pt3080InputTSPrimaryStsJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 54),
    _Pt3080InputTSPrimaryStsJitterMax_Type()
)
pt3080InputTSPrimaryStsJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStsJitterMax.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStsJitterMax.setUnits("100ns")
_Pt3080InputTSPrimaryStsJitterMin_Type = Integer32
_Pt3080InputTSPrimaryStsJitterMin_Object = MibScalar
pt3080InputTSPrimaryStsJitterMin = _Pt3080InputTSPrimaryStsJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 55),
    _Pt3080InputTSPrimaryStsJitterMin_Type()
)
pt3080InputTSPrimaryStsJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStsJitterMin.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStsJitterMin.setUnits("100ns")


class _Pt3080InputTSPrimaryStsJitterReset_Type(Integer32):
    """Custom type pt3080InputTSPrimaryStsJitterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("reset-min-max", 1))
    )


_Pt3080InputTSPrimaryStsJitterReset_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryStsJitterReset_Object = MibScalar
pt3080InputTSPrimaryStsJitterReset = _Pt3080InputTSPrimaryStsJitterReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 56),
    _Pt3080InputTSPrimaryStsJitterReset_Type()
)
pt3080InputTSPrimaryStsJitterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryStsJitterReset.setStatus("current")
_Pt3080InputTSSecondaryStsJitter_Type = Integer32
_Pt3080InputTSSecondaryStsJitter_Object = MibScalar
pt3080InputTSSecondaryStsJitter = _Pt3080InputTSSecondaryStsJitter_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 57),
    _Pt3080InputTSSecondaryStsJitter_Type()
)
pt3080InputTSSecondaryStsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStsJitter.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStsJitter.setUnits("100ns")
_Pt3080InputTSSecondaryStsJitterMax_Type = Integer32
_Pt3080InputTSSecondaryStsJitterMax_Object = MibScalar
pt3080InputTSSecondaryStsJitterMax = _Pt3080InputTSSecondaryStsJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 58),
    _Pt3080InputTSSecondaryStsJitterMax_Type()
)
pt3080InputTSSecondaryStsJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStsJitterMax.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStsJitterMax.setUnits("100ns")
_Pt3080InputTSSecondaryStsJitterMin_Type = Integer32
_Pt3080InputTSSecondaryStsJitterMin_Object = MibScalar
pt3080InputTSSecondaryStsJitterMin = _Pt3080InputTSSecondaryStsJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 59),
    _Pt3080InputTSSecondaryStsJitterMin_Type()
)
pt3080InputTSSecondaryStsJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStsJitterMin.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStsJitterMin.setUnits("100ns")


class _Pt3080InputTSSecondaryStsJitterReset_Type(Integer32):
    """Custom type pt3080InputTSSecondaryStsJitterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("reset-min-max", 1))
    )


_Pt3080InputTSSecondaryStsJitterReset_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryStsJitterReset_Object = MibScalar
pt3080InputTSSecondaryStsJitterReset = _Pt3080InputTSSecondaryStsJitterReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 60),
    _Pt3080InputTSSecondaryStsJitterReset_Type()
)
pt3080InputTSSecondaryStsJitterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryStsJitterReset.setStatus("current")


class _Pt3080InputTSPrimaryMinDelaymargin_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMinDelaymargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pt3080InputTSPrimaryMinDelaymargin_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMinDelaymargin_Object = MibScalar
pt3080InputTSPrimaryMinDelaymargin = _Pt3080InputTSPrimaryMinDelaymargin_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 64),
    _Pt3080InputTSPrimaryMinDelaymargin_Type()
)
pt3080InputTSPrimaryMinDelaymargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMinDelaymargin.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMinDelaymargin.setUnits("1 ms")


class _Pt3080InputTSPrimaryMinDelaymarginEnable_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMinDelaymarginEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSPrimaryMinDelaymarginEnable_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMinDelaymarginEnable_Object = MibScalar
pt3080InputTSPrimaryMinDelaymarginEnable = _Pt3080InputTSPrimaryMinDelaymarginEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 65),
    _Pt3080InputTSPrimaryMinDelaymarginEnable_Type()
)
pt3080InputTSPrimaryMinDelaymarginEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMinDelaymarginEnable.setStatus("current")


class _Pt3080InputTSSecondaryMinDelaymargin_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMinDelaymargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pt3080InputTSSecondaryMinDelaymargin_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMinDelaymargin_Object = MibScalar
pt3080InputTSSecondaryMinDelaymargin = _Pt3080InputTSSecondaryMinDelaymargin_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 66),
    _Pt3080InputTSSecondaryMinDelaymargin_Type()
)
pt3080InputTSSecondaryMinDelaymargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMinDelaymargin.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMinDelaymargin.setUnits("1 ms")


class _Pt3080InputTSSecondaryMinDelaymarginEnable_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMinDelaymarginEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSSecondaryMinDelaymarginEnable_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMinDelaymarginEnable_Object = MibScalar
pt3080InputTSSecondaryMinDelaymarginEnable = _Pt3080InputTSSecondaryMinDelaymarginEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 67),
    _Pt3080InputTSSecondaryMinDelaymarginEnable_Type()
)
pt3080InputTSSecondaryMinDelaymarginEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMinDelaymarginEnable.setStatus("current")


class _Pt3080InputTSPrimaryMaxMissingmip_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMaxMissingmip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Pt3080InputTSPrimaryMaxMissingmip_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMaxMissingmip_Object = MibScalar
pt3080InputTSPrimaryMaxMissingmip = _Pt3080InputTSPrimaryMaxMissingmip_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 68),
    _Pt3080InputTSPrimaryMaxMissingmip_Type()
)
pt3080InputTSPrimaryMaxMissingmip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxMissingmip.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxMissingmip.setUnits("1 secs")


class _Pt3080InputTSPrimaryMaxMissingmipEnable_Type(Integer32):
    """Custom type pt3080InputTSPrimaryMaxMissingmipEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSPrimaryMaxMissingmipEnable_Type.__name__ = "Integer32"
_Pt3080InputTSPrimaryMaxMissingmipEnable_Object = MibScalar
pt3080InputTSPrimaryMaxMissingmipEnable = _Pt3080InputTSPrimaryMaxMissingmipEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 69),
    _Pt3080InputTSPrimaryMaxMissingmipEnable_Type()
)
pt3080InputTSPrimaryMaxMissingmipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSPrimaryMaxMissingmipEnable.setStatus("current")


class _Pt3080InputTSSecondaryMaxMissingmip_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMaxMissingmip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Pt3080InputTSSecondaryMaxMissingmip_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMaxMissingmip_Object = MibScalar
pt3080InputTSSecondaryMaxMissingmip = _Pt3080InputTSSecondaryMaxMissingmip_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 73),
    _Pt3080InputTSSecondaryMaxMissingmip_Type()
)
pt3080InputTSSecondaryMaxMissingmip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxMissingmip.setStatus("current")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxMissingmip.setUnits("1 secs")


class _Pt3080InputTSSecondaryMaxMissingmipEnable_Type(Integer32):
    """Custom type pt3080InputTSSecondaryMaxMissingmipEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080InputTSSecondaryMaxMissingmipEnable_Type.__name__ = "Integer32"
_Pt3080InputTSSecondaryMaxMissingmipEnable_Object = MibScalar
pt3080InputTSSecondaryMaxMissingmipEnable = _Pt3080InputTSSecondaryMaxMissingmipEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 74),
    _Pt3080InputTSSecondaryMaxMissingmipEnable_Type()
)
pt3080InputTSSecondaryMaxMissingmipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InputTSSecondaryMaxMissingmipEnable.setStatus("current")


class _Pt3080InputRefDevType_Type(Integer32):
    """Custom type pt3080InputRefDevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcxo-int", 0),
          ("ocxo-pt3710-10", 1),
          ("ocxo-pt3710-20", 2))
    )


_Pt3080InputRefDevType_Type.__name__ = "Integer32"
_Pt3080InputRefDevType_Object = MibScalar
pt3080InputRefDevType = _Pt3080InputRefDevType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 90),
    _Pt3080InputRefDevType_Type()
)
pt3080InputRefDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputRefDevType.setStatus("current")
_Pt3080InputRefCalDate_Type = DisplayString
_Pt3080InputRefCalDate_Object = MibScalar
pt3080InputRefCalDate = _Pt3080InputRefCalDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 91),
    _Pt3080InputRefCalDate_Type()
)
pt3080InputRefCalDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputRefCalDate.setStatus("current")
_Pt3080InputRefCalVer_Type = Integer32
_Pt3080InputRefCalVer_Object = MibScalar
pt3080InputRefCalVer = _Pt3080InputRefCalVer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 3, 92),
    _Pt3080InputRefCalVer_Type()
)
pt3080InputRefCalVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InputRefCalVer.setStatus("current")
_Pt3080Output_ObjectIdentity = ObjectIdentity
pt3080Output = _Pt3080Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4)
)


class _Pt3080OutputMode_Type(Integer32):
    """Custom type pt3080OutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("standby", 1))
    )


_Pt3080OutputMode_Type.__name__ = "Integer32"
_Pt3080OutputMode_Object = MibScalar
pt3080OutputMode = _Pt3080OutputMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 1),
    _Pt3080OutputMode_Type()
)
pt3080OutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputMode.setStatus("current")


class _Pt3080OutputRfFrequency_Type(Integer32):
    """Custom type pt3080OutputRfFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000000, 860000000),
    )


_Pt3080OutputRfFrequency_Type.__name__ = "Integer32"
_Pt3080OutputRfFrequency_Object = MibScalar
pt3080OutputRfFrequency = _Pt3080OutputRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 2),
    _Pt3080OutputRfFrequency_Type()
)
pt3080OutputRfFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfFrequency.setUnits("1 Hz")


class _Pt3080OutputRfLevel_Type(Integer32):
    """Custom type pt3080OutputRfLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_Pt3080OutputRfLevel_Type.__name__ = "Integer32"
_Pt3080OutputRfLevel_Object = MibScalar
pt3080OutputRfLevel = _Pt3080OutputRfLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 3),
    _Pt3080OutputRfLevel_Type()
)
pt3080OutputRfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfLevel.setUnits("0.01 dBm")


class _Pt3080OutputBandwidth_Type(Integer32):
    """Custom type pt3080OutputBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_Pt3080OutputBandwidth_Type.__name__ = "Integer32"
_Pt3080OutputBandwidth_Object = MibScalar
pt3080OutputBandwidth = _Pt3080OutputBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 4),
    _Pt3080OutputBandwidth_Type()
)
pt3080OutputBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputBandwidth.setUnits("MHz")


class _Pt3080OutputChannel_Type(Integer32):
    """Custom type pt3080OutputChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 69),
    )


_Pt3080OutputChannel_Type.__name__ = "Integer32"
_Pt3080OutputChannel_Object = MibScalar
pt3080OutputChannel = _Pt3080OutputChannel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 5),
    _Pt3080OutputChannel_Type()
)
pt3080OutputChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputChannel.setStatus("current")


class _Pt3080OutputSynchronized_Type(Integer32):
    """Custom type pt3080OutputSynchronized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-synchronized", 0),
          ("synchronized", 1))
    )


_Pt3080OutputSynchronized_Type.__name__ = "Integer32"
_Pt3080OutputSynchronized_Object = MibScalar
pt3080OutputSynchronized = _Pt3080OutputSynchronized_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 6),
    _Pt3080OutputSynchronized_Type()
)
pt3080OutputSynchronized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080OutputSynchronized.setStatus("current")


class _Pt3080OutputMute_Type(Integer32):
    """Custom type pt3080OutputMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080OutputMute_Type.__name__ = "Integer32"
_Pt3080OutputMute_Object = MibScalar
pt3080OutputMute = _Pt3080OutputMute_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 7),
    _Pt3080OutputMute_Type()
)
pt3080OutputMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputMute.setStatus("current")


class _Pt3080OutputPolarity_Type(Integer32):
    """Custom type pt3080OutputPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("norm", 0),
          ("inv", 1))
    )


_Pt3080OutputPolarity_Type.__name__ = "Integer32"
_Pt3080OutputPolarity_Object = MibScalar
pt3080OutputPolarity = _Pt3080OutputPolarity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 8),
    _Pt3080OutputPolarity_Type()
)
pt3080OutputPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputPolarity.setStatus("current")


class _Pt3080OutputPowerLevel_Type(Integer32):
    """Custom type pt3080OutputPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(280, 490),
    )


_Pt3080OutputPowerLevel_Type.__name__ = "Integer32"
_Pt3080OutputPowerLevel_Object = MibScalar
pt3080OutputPowerLevel = _Pt3080OutputPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 9),
    _Pt3080OutputPowerLevel_Type()
)
pt3080OutputPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputPowerLevel.setUnits("0.1 dBm")


class _Pt3080OutputRfFrequencyOffset_Type(Integer32):
    """Custom type pt3080OutputRfFrequencyOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8388608, 8388607),
    )


_Pt3080OutputRfFrequencyOffset_Type.__name__ = "Integer32"
_Pt3080OutputRfFrequencyOffset_Object = MibScalar
pt3080OutputRfFrequencyOffset = _Pt3080OutputRfFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 10),
    _Pt3080OutputRfFrequencyOffset_Type()
)
pt3080OutputRfFrequencyOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfFrequencyOffset.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfFrequencyOffset.setUnits("1 Hz")


class _Pt3080OutputIfEnable_Type(Integer32):
    """Custom type pt3080OutputIfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080OutputIfEnable_Type.__name__ = "Integer32"
_Pt3080OutputIfEnable_Object = MibScalar
pt3080OutputIfEnable = _Pt3080OutputIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 13),
    _Pt3080OutputIfEnable_Type()
)
pt3080OutputIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputIfEnable.setStatus("current")


class _Pt3080OutputIfFrequency_Type(Integer32):
    """Custom type pt3080OutputIfFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35150000, 37150000),
    )


_Pt3080OutputIfFrequency_Type.__name__ = "Integer32"
_Pt3080OutputIfFrequency_Object = MibScalar
pt3080OutputIfFrequency = _Pt3080OutputIfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 14),
    _Pt3080OutputIfFrequency_Type()
)
pt3080OutputIfFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputIfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputIfFrequency.setUnits("1 Hz")


class _Pt3080OutputIfPolarity_Type(Integer32):
    """Custom type pt3080OutputIfPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("norm", 0),
          ("inv", 1))
    )


_Pt3080OutputIfPolarity_Type.__name__ = "Integer32"
_Pt3080OutputIfPolarity_Object = MibScalar
pt3080OutputIfPolarity = _Pt3080OutputIfPolarity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 15),
    _Pt3080OutputIfPolarity_Type()
)
pt3080OutputIfPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputIfPolarity.setStatus("current")


class _Pt3080OutputIfLevel_Type(Integer32):
    """Custom type pt3080OutputIfLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 0),
    )


_Pt3080OutputIfLevel_Type.__name__ = "Integer32"
_Pt3080OutputIfLevel_Object = MibScalar
pt3080OutputIfLevel = _Pt3080OutputIfLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 16),
    _Pt3080OutputIfLevel_Type()
)
pt3080OutputIfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputIfLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputIfLevel.setUnits("0.01 dBm")
_Pt3080OutputEffectiveLevel_Type = Integer32
_Pt3080OutputEffectiveLevel_Object = MibScalar
pt3080OutputEffectiveLevel = _Pt3080OutputEffectiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 17),
    _Pt3080OutputEffectiveLevel_Type()
)
pt3080OutputEffectiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080OutputEffectiveLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputEffectiveLevel.setUnits("0.01 dBm")
_Pt3080OutputActualLevel_Type = Integer32
_Pt3080OutputActualLevel_Object = MibScalar
pt3080OutputActualLevel = _Pt3080OutputActualLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 18),
    _Pt3080OutputActualLevel_Type()
)
pt3080OutputActualLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080OutputActualLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputActualLevel.setUnits("0.01 dBm")
_Pt3080OutputRfDetectedActualLevel_Type = Integer32
_Pt3080OutputRfDetectedActualLevel_Object = MibScalar
pt3080OutputRfDetectedActualLevel = _Pt3080OutputRfDetectedActualLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 19),
    _Pt3080OutputRfDetectedActualLevel_Type()
)
pt3080OutputRfDetectedActualLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedActualLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedActualLevel.setUnits("0.01 dBm")


class _Pt3080OutputRfDetectedLowerLevelLimit_Type(Integer32):
    """Custom type pt3080OutputRfDetectedLowerLevelLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_Pt3080OutputRfDetectedLowerLevelLimit_Type.__name__ = "Integer32"
_Pt3080OutputRfDetectedLowerLevelLimit_Object = MibScalar
pt3080OutputRfDetectedLowerLevelLimit = _Pt3080OutputRfDetectedLowerLevelLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 20),
    _Pt3080OutputRfDetectedLowerLevelLimit_Type()
)
pt3080OutputRfDetectedLowerLevelLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedLowerLevelLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedLowerLevelLimit.setUnits("0.1 dB")


class _Pt3080OutputRfDetectedLowerLevelcontrol_Type(Integer32):
    """Custom type pt3080OutputRfDetectedLowerLevelcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080OutputRfDetectedLowerLevelcontrol_Type.__name__ = "Integer32"
_Pt3080OutputRfDetectedLowerLevelcontrol_Object = MibScalar
pt3080OutputRfDetectedLowerLevelcontrol = _Pt3080OutputRfDetectedLowerLevelcontrol_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 21),
    _Pt3080OutputRfDetectedLowerLevelcontrol_Type()
)
pt3080OutputRfDetectedLowerLevelcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedLowerLevelcontrol.setStatus("current")


class _Pt3080OutputRfDetectedHigherLevelLimit_Type(Integer32):
    """Custom type pt3080OutputRfDetectedHigherLevelLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_Pt3080OutputRfDetectedHigherLevelLimit_Type.__name__ = "Integer32"
_Pt3080OutputRfDetectedHigherLevelLimit_Object = MibScalar
pt3080OutputRfDetectedHigherLevelLimit = _Pt3080OutputRfDetectedHigherLevelLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 22),
    _Pt3080OutputRfDetectedHigherLevelLimit_Type()
)
pt3080OutputRfDetectedHigherLevelLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedHigherLevelLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedHigherLevelLimit.setUnits("0.1 dB")


class _Pt3080OutputRfDetectedHigherLevelcontrol_Type(Integer32):
    """Custom type pt3080OutputRfDetectedHigherLevelcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080OutputRfDetectedHigherLevelcontrol_Type.__name__ = "Integer32"
_Pt3080OutputRfDetectedHigherLevelcontrol_Object = MibScalar
pt3080OutputRfDetectedHigherLevelcontrol = _Pt3080OutputRfDetectedHigherLevelcontrol_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 23),
    _Pt3080OutputRfDetectedHigherLevelcontrol_Type()
)
pt3080OutputRfDetectedHigherLevelcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfDetectedHigherLevelcontrol.setStatus("current")


class _Pt3080OutputRfAlcControl_Type(Integer32):
    """Custom type pt3080OutputRfAlcControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080OutputRfAlcControl_Type.__name__ = "Integer32"
_Pt3080OutputRfAlcControl_Object = MibScalar
pt3080OutputRfAlcControl = _Pt3080OutputRfAlcControl_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 30),
    _Pt3080OutputRfAlcControl_Type()
)
pt3080OutputRfAlcControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcControl.setStatus("current")


class _Pt3080OutputRfAlcSense_Type(Integer32):
    """Custom type pt3080OutputRfAlcSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfsense1", 0),
          ("rfsense2", 1))
    )


_Pt3080OutputRfAlcSense_Type.__name__ = "Integer32"
_Pt3080OutputRfAlcSense_Object = MibScalar
pt3080OutputRfAlcSense = _Pt3080OutputRfAlcSense_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 31),
    _Pt3080OutputRfAlcSense_Type()
)
pt3080OutputRfAlcSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcSense.setStatus("current")


class _Pt3080OutputRfAlcSetpointPort1_Type(Integer32):
    """Custom type pt3080OutputRfAlcSetpointPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-11000, 11000),
    )


_Pt3080OutputRfAlcSetpointPort1_Type.__name__ = "Integer32"
_Pt3080OutputRfAlcSetpointPort1_Object = MibScalar
pt3080OutputRfAlcSetpointPort1 = _Pt3080OutputRfAlcSetpointPort1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 32),
    _Pt3080OutputRfAlcSetpointPort1_Type()
)
pt3080OutputRfAlcSetpointPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcSetpointPort1.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcSetpointPort1.setUnits("0.01 dB")


class _Pt3080OutputRfAlcSetpointPort2_Type(Integer32):
    """Custom type pt3080OutputRfAlcSetpointPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-11000, 11000),
    )


_Pt3080OutputRfAlcSetpointPort2_Type.__name__ = "Integer32"
_Pt3080OutputRfAlcSetpointPort2_Object = MibScalar
pt3080OutputRfAlcSetpointPort2 = _Pt3080OutputRfAlcSetpointPort2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 33),
    _Pt3080OutputRfAlcSetpointPort2_Type()
)
pt3080OutputRfAlcSetpointPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcSetpointPort2.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcSetpointPort2.setUnits("0.01 dB")


class _Pt3080OutputRfAlcStatus_Type(Integer32):
    """Custom type pt3080OutputRfAlcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080OutputRfAlcStatus_Type.__name__ = "Integer32"
_Pt3080OutputRfAlcStatus_Object = MibScalar
pt3080OutputRfAlcStatus = _Pt3080OutputRfAlcStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 34),
    _Pt3080OutputRfAlcStatus_Type()
)
pt3080OutputRfAlcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcStatus.setStatus("current")
_Pt3080OutputRfAlcStatusInformation_Type = DisplayString
_Pt3080OutputRfAlcStatusInformation_Object = MibScalar
pt3080OutputRfAlcStatusInformation = _Pt3080OutputRfAlcStatusInformation_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 35),
    _Pt3080OutputRfAlcStatusInformation_Type()
)
pt3080OutputRfAlcStatusInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080OutputRfAlcStatusInformation.setStatus("current")


class _Pt3080OutputRfCableMode_Type(Integer32):
    """Custom type pt3080OutputRfCableMode based on Integer32"""
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
          ("const", 1),
          ("auto", 2))
    )


_Pt3080OutputRfCableMode_Type.__name__ = "Integer32"
_Pt3080OutputRfCableMode_Object = MibScalar
pt3080OutputRfCableMode = _Pt3080OutputRfCableMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 50),
    _Pt3080OutputRfCableMode_Type()
)
pt3080OutputRfCableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableMode.setStatus("current")


class _Pt3080OutputRfCableConstantLevelOffset_Type(Integer32):
    """Custom type pt3080OutputRfCableConstantLevelOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Pt3080OutputRfCableConstantLevelOffset_Type.__name__ = "Integer32"
_Pt3080OutputRfCableConstantLevelOffset_Object = MibScalar
pt3080OutputRfCableConstantLevelOffset = _Pt3080OutputRfCableConstantLevelOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 51),
    _Pt3080OutputRfCableConstantLevelOffset_Type()
)
pt3080OutputRfCableConstantLevelOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableConstantLevelOffset.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfCableConstantLevelOffset.setUnits("0.001 dBm")


class _Pt3080OutputRfCableFrequencyLevelOffset0_Type(Integer32):
    """Custom type pt3080OutputRfCableFrequencyLevelOffset0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Pt3080OutputRfCableFrequencyLevelOffset0_Type.__name__ = "Integer32"
_Pt3080OutputRfCableFrequencyLevelOffset0_Object = MibScalar
pt3080OutputRfCableFrequencyLevelOffset0 = _Pt3080OutputRfCableFrequencyLevelOffset0_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 52),
    _Pt3080OutputRfCableFrequencyLevelOffset0_Type()
)
pt3080OutputRfCableFrequencyLevelOffset0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset0.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset0.setUnits("0.001 dBm")


class _Pt3080OutputRfCableFrequencyLevelOffset1_Type(Integer32):
    """Custom type pt3080OutputRfCableFrequencyLevelOffset1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Pt3080OutputRfCableFrequencyLevelOffset1_Type.__name__ = "Integer32"
_Pt3080OutputRfCableFrequencyLevelOffset1_Object = MibScalar
pt3080OutputRfCableFrequencyLevelOffset1 = _Pt3080OutputRfCableFrequencyLevelOffset1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 53),
    _Pt3080OutputRfCableFrequencyLevelOffset1_Type()
)
pt3080OutputRfCableFrequencyLevelOffset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset1.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset1.setUnits("0.001 dBm")


class _Pt3080OutputRfCableFrequencyLevelOffset2_Type(Integer32):
    """Custom type pt3080OutputRfCableFrequencyLevelOffset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Pt3080OutputRfCableFrequencyLevelOffset2_Type.__name__ = "Integer32"
_Pt3080OutputRfCableFrequencyLevelOffset2_Object = MibScalar
pt3080OutputRfCableFrequencyLevelOffset2 = _Pt3080OutputRfCableFrequencyLevelOffset2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 54),
    _Pt3080OutputRfCableFrequencyLevelOffset2_Type()
)
pt3080OutputRfCableFrequencyLevelOffset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset2.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset2.setUnits("0.001 dBm")


class _Pt3080OutputRfCableFrequencyLevelOffset3_Type(Integer32):
    """Custom type pt3080OutputRfCableFrequencyLevelOffset3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Pt3080OutputRfCableFrequencyLevelOffset3_Type.__name__ = "Integer32"
_Pt3080OutputRfCableFrequencyLevelOffset3_Object = MibScalar
pt3080OutputRfCableFrequencyLevelOffset3 = _Pt3080OutputRfCableFrequencyLevelOffset3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 55),
    _Pt3080OutputRfCableFrequencyLevelOffset3_Type()
)
pt3080OutputRfCableFrequencyLevelOffset3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset3.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset3.setUnits("0.001 dBm")


class _Pt3080OutputRfCableFrequencyLevelOffset4_Type(Integer32):
    """Custom type pt3080OutputRfCableFrequencyLevelOffset4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Pt3080OutputRfCableFrequencyLevelOffset4_Type.__name__ = "Integer32"
_Pt3080OutputRfCableFrequencyLevelOffset4_Object = MibScalar
pt3080OutputRfCableFrequencyLevelOffset4 = _Pt3080OutputRfCableFrequencyLevelOffset4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 56),
    _Pt3080OutputRfCableFrequencyLevelOffset4_Type()
)
pt3080OutputRfCableFrequencyLevelOffset4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset4.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset4.setUnits("0.001 dBm")


class _Pt3080OutputRfCableFrequencyLevelOffset5_Type(Integer32):
    """Custom type pt3080OutputRfCableFrequencyLevelOffset5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_Pt3080OutputRfCableFrequencyLevelOffset5_Type.__name__ = "Integer32"
_Pt3080OutputRfCableFrequencyLevelOffset5_Object = MibScalar
pt3080OutputRfCableFrequencyLevelOffset5 = _Pt3080OutputRfCableFrequencyLevelOffset5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 4, 57),
    _Pt3080OutputRfCableFrequencyLevelOffset5_Type()
)
pt3080OutputRfCableFrequencyLevelOffset5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset5.setStatus("current")
if mibBuilder.loadTexts:
    pt3080OutputRfCableFrequencyLevelOffset5.setUnits("0.001 dBm")
_Pt3080Gps_ObjectIdentity = ObjectIdentity
pt3080Gps = _Pt3080Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7)
)


class _Pt3080Gps1PPSStatus_Type(Integer32):
    """Custom type pt3080Gps1PPSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Pt3080Gps1PPSStatus_Type.__name__ = "Integer32"
_Pt3080Gps1PPSStatus_Object = MibScalar
pt3080Gps1PPSStatus = _Pt3080Gps1PPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 1),
    _Pt3080Gps1PPSStatus_Type()
)
pt3080Gps1PPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Gps1PPSStatus.setStatus("current")
_Pt3080GpsVisibleSatellites_Type = Integer32
_Pt3080GpsVisibleSatellites_Object = MibScalar
pt3080GpsVisibleSatellites = _Pt3080GpsVisibleSatellites_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 2),
    _Pt3080GpsVisibleSatellites_Type()
)
pt3080GpsVisibleSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsVisibleSatellites.setStatus("current")
_Pt3080GpsTrackedSatellites_Type = Integer32
_Pt3080GpsTrackedSatellites_Object = MibScalar
pt3080GpsTrackedSatellites = _Pt3080GpsTrackedSatellites_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 3),
    _Pt3080GpsTrackedSatellites_Type()
)
pt3080GpsTrackedSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsTrackedSatellites.setStatus("current")


class _Pt3080GpsBias_Type(Integer32):
    """Custom type pt3080GpsBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080GpsBias_Type.__name__ = "Integer32"
_Pt3080GpsBias_Object = MibScalar
pt3080GpsBias = _Pt3080GpsBias_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 4),
    _Pt3080GpsBias_Type()
)
pt3080GpsBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsBias.setStatus("current")
_Pt3080GpsLongtitude_Type = DisplayString
_Pt3080GpsLongtitude_Object = MibScalar
pt3080GpsLongtitude = _Pt3080GpsLongtitude_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 6),
    _Pt3080GpsLongtitude_Type()
)
pt3080GpsLongtitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsLongtitude.setStatus("current")
_Pt3080GpsLatitude_Type = DisplayString
_Pt3080GpsLatitude_Object = MibScalar
pt3080GpsLatitude = _Pt3080GpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 7),
    _Pt3080GpsLatitude_Type()
)
pt3080GpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsLatitude.setStatus("current")
_Pt3080GpsAltitude_Type = DisplayString
_Pt3080GpsAltitude_Object = MibScalar
pt3080GpsAltitude = _Pt3080GpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 8),
    _Pt3080GpsAltitude_Type()
)
pt3080GpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsAltitude.setStatus("current")
_Pt3080GpsVersion_Type = DisplayString
_Pt3080GpsVersion_Object = MibScalar
pt3080GpsVersion = _Pt3080GpsVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 9),
    _Pt3080GpsVersion_Type()
)
pt3080GpsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsVersion.setStatus("current")


class _Pt3080GpsHoldoverTime_Type(Integer32):
    """Custom type pt3080GpsHoldoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 172800),
    )


_Pt3080GpsHoldoverTime_Type.__name__ = "Integer32"
_Pt3080GpsHoldoverTime_Object = MibScalar
pt3080GpsHoldoverTime = _Pt3080GpsHoldoverTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 10),
    _Pt3080GpsHoldoverTime_Type()
)
pt3080GpsHoldoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsHoldoverTime.setStatus("current")


class _Pt3080GpsHoldoverForever_Type(Integer32):
    """Custom type pt3080GpsHoldoverForever based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080GpsHoldoverForever_Type.__name__ = "Integer32"
_Pt3080GpsHoldoverForever_Object = MibScalar
pt3080GpsHoldoverForever = _Pt3080GpsHoldoverForever_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 11),
    _Pt3080GpsHoldoverForever_Type()
)
pt3080GpsHoldoverForever.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsHoldoverForever.setStatus("current")


class _Pt3080GpsCableDelay_Type(Integer32):
    """Custom type pt3080GpsCableDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18125, 13750),
    )


_Pt3080GpsCableDelay_Type.__name__ = "Integer32"
_Pt3080GpsCableDelay_Object = MibScalar
pt3080GpsCableDelay = _Pt3080GpsCableDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 12),
    _Pt3080GpsCableDelay_Type()
)
pt3080GpsCableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsCableDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080GpsCableDelay.setUnits("0.1 ns")
_Pt3080GpsState_Type = DisplayString
_Pt3080GpsState_Object = MibScalar
pt3080GpsState = _Pt3080GpsState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 13),
    _Pt3080GpsState_Type()
)
pt3080GpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsState.setStatus("current")
_Pt3080GpsVisibleSatellitesSnr_Type = Integer32
_Pt3080GpsVisibleSatellitesSnr_Object = MibScalar
pt3080GpsVisibleSatellitesSnr = _Pt3080GpsVisibleSatellitesSnr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 14),
    _Pt3080GpsVisibleSatellitesSnr_Type()
)
pt3080GpsVisibleSatellitesSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GpsVisibleSatellitesSnr.setStatus("current")
if mibBuilder.loadTexts:
    pt3080GpsVisibleSatellitesSnr.setUnits("0.1 dBHz")


class _Pt3080GpsbiasVoltage_Type(Integer32):
    """Custom type pt3080GpsbiasVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gpsant-5v", 0),
          ("gpsant-33v", 1))
    )


_Pt3080GpsbiasVoltage_Type.__name__ = "Integer32"
_Pt3080GpsbiasVoltage_Object = MibScalar
pt3080GpsbiasVoltage = _Pt3080GpsbiasVoltage_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 15),
    _Pt3080GpsbiasVoltage_Type()
)
pt3080GpsbiasVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsbiasVoltage.setStatus("current")


class _Pt3080GpsSatelliteSystemGPS_Type(Integer32):
    """Custom type pt3080GpsSatelliteSystemGPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080GpsSatelliteSystemGPS_Type.__name__ = "Integer32"
_Pt3080GpsSatelliteSystemGPS_Object = MibScalar
pt3080GpsSatelliteSystemGPS = _Pt3080GpsSatelliteSystemGPS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 16),
    _Pt3080GpsSatelliteSystemGPS_Type()
)
pt3080GpsSatelliteSystemGPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsSatelliteSystemGPS.setStatus("current")


class _Pt3080GpsSatelliteSystemGLONASS_Type(Integer32):
    """Custom type pt3080GpsSatelliteSystemGLONASS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080GpsSatelliteSystemGLONASS_Type.__name__ = "Integer32"
_Pt3080GpsSatelliteSystemGLONASS_Object = MibScalar
pt3080GpsSatelliteSystemGLONASS = _Pt3080GpsSatelliteSystemGLONASS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 17),
    _Pt3080GpsSatelliteSystemGLONASS_Type()
)
pt3080GpsSatelliteSystemGLONASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsSatelliteSystemGLONASS.setStatus("current")


class _Pt3080GpsSatelliteSystemGALILEO_Type(Integer32):
    """Custom type pt3080GpsSatelliteSystemGALILEO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080GpsSatelliteSystemGALILEO_Type.__name__ = "Integer32"
_Pt3080GpsSatelliteSystemGALILEO_Object = MibScalar
pt3080GpsSatelliteSystemGALILEO = _Pt3080GpsSatelliteSystemGALILEO_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 18),
    _Pt3080GpsSatelliteSystemGALILEO_Type()
)
pt3080GpsSatelliteSystemGALILEO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsSatelliteSystemGALILEO.setStatus("current")


class _Pt3080GpsSatelliteSystemCOMPASS_Type(Integer32):
    """Custom type pt3080GpsSatelliteSystemCOMPASS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080GpsSatelliteSystemCOMPASS_Type.__name__ = "Integer32"
_Pt3080GpsSatelliteSystemCOMPASS_Object = MibScalar
pt3080GpsSatelliteSystemCOMPASS = _Pt3080GpsSatelliteSystemCOMPASS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 7, 19),
    _Pt3080GpsSatelliteSystemCOMPASS_Type()
)
pt3080GpsSatelliteSystemCOMPASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GpsSatelliteSystemCOMPASS.setStatus("current")
_Pt3080TSoIP_ObjectIdentity = ObjectIdentity
pt3080TSoIP = _Pt3080TSoIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10)
)


class _Pt3080TSoIPRx1SyncTimeout_Type(Integer32):
    """Custom type pt3080TSoIPRx1SyncTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 250),
    )


_Pt3080TSoIPRx1SyncTimeout_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1SyncTimeout_Object = MibScalar
pt3080TSoIPRx1SyncTimeout = _Pt3080TSoIPRx1SyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 9),
    _Pt3080TSoIPRx1SyncTimeout_Type()
)
pt3080TSoIPRx1SyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1SyncTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1SyncTimeout.setUnits("1 ms")


class _Pt3080TSoIPRx1MinumimLatency_Type(Integer32):
    """Custom type pt3080TSoIPRx1MinumimLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Pt3080TSoIPRx1MinumimLatency_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1MinumimLatency_Object = MibScalar
pt3080TSoIPRx1MinumimLatency = _Pt3080TSoIPRx1MinumimLatency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 10),
    _Pt3080TSoIPRx1MinumimLatency_Type()
)
pt3080TSoIPRx1MinumimLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1MinumimLatency.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1MinumimLatency.setUnits("0.1 ms")


class _Pt3080TSoIPRx1LanSelect_Type(Integer32):
    """Custom type pt3080TSoIPRx1LanSelect based on Integer32"""
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
        *(("flan", 0),
          ("alan", 1),
          ("tlan", 2),
          ("blan", 3),
          ("plan", 4))
    )


_Pt3080TSoIPRx1LanSelect_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1LanSelect_Object = MibScalar
pt3080TSoIPRx1LanSelect = _Pt3080TSoIPRx1LanSelect_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 11),
    _Pt3080TSoIPRx1LanSelect_Type()
)
pt3080TSoIPRx1LanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1LanSelect.setStatus("current")


class _Pt3080TSoIPRx1Multicast_Type(Integer32):
    """Custom type pt3080TSoIPRx1Multicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080TSoIPRx1Multicast_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1Multicast_Object = MibScalar
pt3080TSoIPRx1Multicast = _Pt3080TSoIPRx1Multicast_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 12),
    _Pt3080TSoIPRx1Multicast_Type()
)
pt3080TSoIPRx1Multicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1Multicast.setStatus("current")


class _Pt3080TSoIPRx1Protocol_Type(Integer32):
    """Custom type pt3080TSoIPRx1Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("rtp", 1),
          ("auto", 2))
    )


_Pt3080TSoIPRx1Protocol_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1Protocol_Object = MibScalar
pt3080TSoIPRx1Protocol = _Pt3080TSoIPRx1Protocol_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 13),
    _Pt3080TSoIPRx1Protocol_Type()
)
pt3080TSoIPRx1Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1Protocol.setStatus("current")


class _Pt3080TSoIPRx1Portnumber_Type(Integer32):
    """Custom type pt3080TSoIPRx1Portnumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080TSoIPRx1Portnumber_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1Portnumber_Object = MibScalar
pt3080TSoIPRx1Portnumber = _Pt3080TSoIPRx1Portnumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 14),
    _Pt3080TSoIPRx1Portnumber_Type()
)
pt3080TSoIPRx1Portnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1Portnumber.setStatus("current")


class _Pt3080TSoIPRx1ReceiverEnable_Type(Integer32):
    """Custom type pt3080TSoIPRx1ReceiverEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080TSoIPRx1ReceiverEnable_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1ReceiverEnable_Object = MibScalar
pt3080TSoIPRx1ReceiverEnable = _Pt3080TSoIPRx1ReceiverEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 15),
    _Pt3080TSoIPRx1ReceiverEnable_Type()
)
pt3080TSoIPRx1ReceiverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1ReceiverEnable.setStatus("current")


class _Pt3080TSoIPRx1PacketErrorRatioLimit_Type(Integer32):
    """Custom type pt3080TSoIPRx1PacketErrorRatioLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Pt3080TSoIPRx1PacketErrorRatioLimit_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1PacketErrorRatioLimit_Object = MibScalar
pt3080TSoIPRx1PacketErrorRatioLimit = _Pt3080TSoIPRx1PacketErrorRatioLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 16),
    _Pt3080TSoIPRx1PacketErrorRatioLimit_Type()
)
pt3080TSoIPRx1PacketErrorRatioLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1PacketErrorRatioLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1PacketErrorRatioLimit.setUnits("0.1 %")


class _Pt3080TSoIPRx1Status_Type(Integer32):
    """Custom type pt3080TSoIPRx1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1),
          ("disabled", 2))
    )


_Pt3080TSoIPRx1Status_Type.__name__ = "Integer32"
_Pt3080TSoIPRx1Status_Object = MibScalar
pt3080TSoIPRx1Status = _Pt3080TSoIPRx1Status_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 17),
    _Pt3080TSoIPRx1Status_Type()
)
pt3080TSoIPRx1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1Status.setStatus("current")
_Pt3080TSoIPRx1CurrentIPAddress_Type = IpAddress
_Pt3080TSoIPRx1CurrentIPAddress_Object = MibScalar
pt3080TSoIPRx1CurrentIPAddress = _Pt3080TSoIPRx1CurrentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 18),
    _Pt3080TSoIPRx1CurrentIPAddress_Type()
)
pt3080TSoIPRx1CurrentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1CurrentIPAddress.setStatus("current")
_Pt3080TSoIPRx1SequenceErrors_Type = Integer32
_Pt3080TSoIPRx1SequenceErrors_Object = MibScalar
pt3080TSoIPRx1SequenceErrors = _Pt3080TSoIPRx1SequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 19),
    _Pt3080TSoIPRx1SequenceErrors_Type()
)
pt3080TSoIPRx1SequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1SequenceErrors.setStatus("current")
_Pt3080TSoIPRx1PacketErrorRatio_Type = Integer32
_Pt3080TSoIPRx1PacketErrorRatio_Object = MibScalar
pt3080TSoIPRx1PacketErrorRatio = _Pt3080TSoIPRx1PacketErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 20),
    _Pt3080TSoIPRx1PacketErrorRatio_Type()
)
pt3080TSoIPRx1PacketErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1PacketErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1PacketErrorRatio.setUnits("0.1 %")
_Pt3080TSoIPRx1LostIPFrames_Type = Integer32
_Pt3080TSoIPRx1LostIPFrames_Object = MibScalar
pt3080TSoIPRx1LostIPFrames = _Pt3080TSoIPRx1LostIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 21),
    _Pt3080TSoIPRx1LostIPFrames_Type()
)
pt3080TSoIPRx1LostIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1LostIPFrames.setStatus("current")
_Pt3080TSoIPRx1CorrectedIPFrames_Type = Integer32
_Pt3080TSoIPRx1CorrectedIPFrames_Object = MibScalar
pt3080TSoIPRx1CorrectedIPFrames = _Pt3080TSoIPRx1CorrectedIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 22),
    _Pt3080TSoIPRx1CorrectedIPFrames_Type()
)
pt3080TSoIPRx1CorrectedIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1CorrectedIPFrames.setStatus("current")
_Pt3080TSoIPRx1FecColumn_Type = Integer32
_Pt3080TSoIPRx1FecColumn_Object = MibScalar
pt3080TSoIPRx1FecColumn = _Pt3080TSoIPRx1FecColumn_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 23),
    _Pt3080TSoIPRx1FecColumn_Type()
)
pt3080TSoIPRx1FecColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1FecColumn.setStatus("current")
_Pt3080TSoIPRx1FecRow_Type = Integer32
_Pt3080TSoIPRx1FecRow_Object = MibScalar
pt3080TSoIPRx1FecRow = _Pt3080TSoIPRx1FecRow_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 24),
    _Pt3080TSoIPRx1FecRow_Type()
)
pt3080TSoIPRx1FecRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1FecRow.setStatus("current")
_Pt3080TSoIPRx1PacketsPerFrame_Type = Integer32
_Pt3080TSoIPRx1PacketsPerFrame_Object = MibScalar
pt3080TSoIPRx1PacketsPerFrame = _Pt3080TSoIPRx1PacketsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 25),
    _Pt3080TSoIPRx1PacketsPerFrame_Type()
)
pt3080TSoIPRx1PacketsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1PacketsPerFrame.setStatus("current")
_Pt3080TSoIPRx1IpBitrate_Type = Integer32
_Pt3080TSoIPRx1IpBitrate_Object = MibScalar
pt3080TSoIPRx1IpBitrate = _Pt3080TSoIPRx1IpBitrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 26),
    _Pt3080TSoIPRx1IpBitrate_Type()
)
pt3080TSoIPRx1IpBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1IpBitrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1IpBitrate.setUnits("0.001 Mbps")
_Pt3080TSoIPRx1QueueSize_Type = Integer32
_Pt3080TSoIPRx1QueueSize_Object = MibScalar
pt3080TSoIPRx1QueueSize = _Pt3080TSoIPRx1QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 27),
    _Pt3080TSoIPRx1QueueSize_Type()
)
pt3080TSoIPRx1QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1QueueSize.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1QueueSize.setUnits("1 Frames")
_Pt3080TSoIPRx1CurrentLatency_Type = Integer32
_Pt3080TSoIPRx1CurrentLatency_Object = MibScalar
pt3080TSoIPRx1CurrentLatency = _Pt3080TSoIPRx1CurrentLatency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 28),
    _Pt3080TSoIPRx1CurrentLatency_Type()
)
pt3080TSoIPRx1CurrentLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1CurrentLatency.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1CurrentLatency.setUnits("0.1 ms")
_Pt3080TSoIPRx1TSPacketSize_Type = Integer32
_Pt3080TSoIPRx1TSPacketSize_Object = MibScalar
pt3080TSoIPRx1TSPacketSize = _Pt3080TSoIPRx1TSPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 29),
    _Pt3080TSoIPRx1TSPacketSize_Type()
)
pt3080TSoIPRx1TSPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1TSPacketSize.setStatus("current")
_Pt3080TSoIPRx1OverrunIPFrames_Type = Integer32
_Pt3080TSoIPRx1OverrunIPFrames_Object = MibScalar
pt3080TSoIPRx1OverrunIPFrames = _Pt3080TSoIPRx1OverrunIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 30),
    _Pt3080TSoIPRx1OverrunIPFrames_Type()
)
pt3080TSoIPRx1OverrunIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx1OverrunIPFrames.setStatus("current")


class _Pt3080TSoIPRx2SyncTimeout_Type(Integer32):
    """Custom type pt3080TSoIPRx2SyncTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 250),
    )


_Pt3080TSoIPRx2SyncTimeout_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2SyncTimeout_Object = MibScalar
pt3080TSoIPRx2SyncTimeout = _Pt3080TSoIPRx2SyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 39),
    _Pt3080TSoIPRx2SyncTimeout_Type()
)
pt3080TSoIPRx2SyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2SyncTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2SyncTimeout.setUnits("1 ms")


class _Pt3080TSoIPRx2MinumimLatency_Type(Integer32):
    """Custom type pt3080TSoIPRx2MinumimLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Pt3080TSoIPRx2MinumimLatency_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2MinumimLatency_Object = MibScalar
pt3080TSoIPRx2MinumimLatency = _Pt3080TSoIPRx2MinumimLatency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 40),
    _Pt3080TSoIPRx2MinumimLatency_Type()
)
pt3080TSoIPRx2MinumimLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2MinumimLatency.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2MinumimLatency.setUnits("0.1 ms")


class _Pt3080TSoIPRx2LanSelect_Type(Integer32):
    """Custom type pt3080TSoIPRx2LanSelect based on Integer32"""
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
        *(("flan", 0),
          ("alan", 1),
          ("tlan", 2),
          ("blan", 3),
          ("plan", 4))
    )


_Pt3080TSoIPRx2LanSelect_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2LanSelect_Object = MibScalar
pt3080TSoIPRx2LanSelect = _Pt3080TSoIPRx2LanSelect_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 41),
    _Pt3080TSoIPRx2LanSelect_Type()
)
pt3080TSoIPRx2LanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2LanSelect.setStatus("current")


class _Pt3080TSoIPRx2Multicast_Type(Integer32):
    """Custom type pt3080TSoIPRx2Multicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080TSoIPRx2Multicast_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2Multicast_Object = MibScalar
pt3080TSoIPRx2Multicast = _Pt3080TSoIPRx2Multicast_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 42),
    _Pt3080TSoIPRx2Multicast_Type()
)
pt3080TSoIPRx2Multicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2Multicast.setStatus("current")


class _Pt3080TSoIPRx2Protocol_Type(Integer32):
    """Custom type pt3080TSoIPRx2Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("rtp", 1),
          ("auto", 2))
    )


_Pt3080TSoIPRx2Protocol_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2Protocol_Object = MibScalar
pt3080TSoIPRx2Protocol = _Pt3080TSoIPRx2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 43),
    _Pt3080TSoIPRx2Protocol_Type()
)
pt3080TSoIPRx2Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2Protocol.setStatus("current")


class _Pt3080TSoIPRx2Portnumber_Type(Integer32):
    """Custom type pt3080TSoIPRx2Portnumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080TSoIPRx2Portnumber_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2Portnumber_Object = MibScalar
pt3080TSoIPRx2Portnumber = _Pt3080TSoIPRx2Portnumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 44),
    _Pt3080TSoIPRx2Portnumber_Type()
)
pt3080TSoIPRx2Portnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2Portnumber.setStatus("current")


class _Pt3080TSoIPRx2ReceiverEnable_Type(Integer32):
    """Custom type pt3080TSoIPRx2ReceiverEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080TSoIPRx2ReceiverEnable_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2ReceiverEnable_Object = MibScalar
pt3080TSoIPRx2ReceiverEnable = _Pt3080TSoIPRx2ReceiverEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 45),
    _Pt3080TSoIPRx2ReceiverEnable_Type()
)
pt3080TSoIPRx2ReceiverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2ReceiverEnable.setStatus("current")


class _Pt3080TSoIPRx2PacketErrorRatioLimit_Type(Integer32):
    """Custom type pt3080TSoIPRx2PacketErrorRatioLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Pt3080TSoIPRx2PacketErrorRatioLimit_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2PacketErrorRatioLimit_Object = MibScalar
pt3080TSoIPRx2PacketErrorRatioLimit = _Pt3080TSoIPRx2PacketErrorRatioLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 46),
    _Pt3080TSoIPRx2PacketErrorRatioLimit_Type()
)
pt3080TSoIPRx2PacketErrorRatioLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2PacketErrorRatioLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2PacketErrorRatioLimit.setUnits("0.1 %")


class _Pt3080TSoIPRx2Status_Type(Integer32):
    """Custom type pt3080TSoIPRx2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1),
          ("disabled", 2))
    )


_Pt3080TSoIPRx2Status_Type.__name__ = "Integer32"
_Pt3080TSoIPRx2Status_Object = MibScalar
pt3080TSoIPRx2Status = _Pt3080TSoIPRx2Status_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 47),
    _Pt3080TSoIPRx2Status_Type()
)
pt3080TSoIPRx2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2Status.setStatus("current")
_Pt3080TSoIPRx2CurrentIPAddress_Type = IpAddress
_Pt3080TSoIPRx2CurrentIPAddress_Object = MibScalar
pt3080TSoIPRx2CurrentIPAddress = _Pt3080TSoIPRx2CurrentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 48),
    _Pt3080TSoIPRx2CurrentIPAddress_Type()
)
pt3080TSoIPRx2CurrentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2CurrentIPAddress.setStatus("current")
_Pt3080TSoIPRx2SequenceErrors_Type = Integer32
_Pt3080TSoIPRx2SequenceErrors_Object = MibScalar
pt3080TSoIPRx2SequenceErrors = _Pt3080TSoIPRx2SequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 49),
    _Pt3080TSoIPRx2SequenceErrors_Type()
)
pt3080TSoIPRx2SequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2SequenceErrors.setStatus("current")
_Pt3080TSoIPRx2PacketErrorRatio_Type = Integer32
_Pt3080TSoIPRx2PacketErrorRatio_Object = MibScalar
pt3080TSoIPRx2PacketErrorRatio = _Pt3080TSoIPRx2PacketErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 50),
    _Pt3080TSoIPRx2PacketErrorRatio_Type()
)
pt3080TSoIPRx2PacketErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2PacketErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2PacketErrorRatio.setUnits("0.1 %")
_Pt3080TSoIPRx2LostIPFrames_Type = Integer32
_Pt3080TSoIPRx2LostIPFrames_Object = MibScalar
pt3080TSoIPRx2LostIPFrames = _Pt3080TSoIPRx2LostIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 51),
    _Pt3080TSoIPRx2LostIPFrames_Type()
)
pt3080TSoIPRx2LostIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2LostIPFrames.setStatus("current")
_Pt3080TSoIPRx2CorrectedIPFrames_Type = Integer32
_Pt3080TSoIPRx2CorrectedIPFrames_Object = MibScalar
pt3080TSoIPRx2CorrectedIPFrames = _Pt3080TSoIPRx2CorrectedIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 52),
    _Pt3080TSoIPRx2CorrectedIPFrames_Type()
)
pt3080TSoIPRx2CorrectedIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2CorrectedIPFrames.setStatus("current")
_Pt3080TSoIPRx2FecColumn_Type = Integer32
_Pt3080TSoIPRx2FecColumn_Object = MibScalar
pt3080TSoIPRx2FecColumn = _Pt3080TSoIPRx2FecColumn_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 53),
    _Pt3080TSoIPRx2FecColumn_Type()
)
pt3080TSoIPRx2FecColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2FecColumn.setStatus("current")
_Pt3080TSoIPRx2FecRow_Type = Integer32
_Pt3080TSoIPRx2FecRow_Object = MibScalar
pt3080TSoIPRx2FecRow = _Pt3080TSoIPRx2FecRow_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 54),
    _Pt3080TSoIPRx2FecRow_Type()
)
pt3080TSoIPRx2FecRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2FecRow.setStatus("current")
_Pt3080TSoIPRx2PacketsPerFrame_Type = Integer32
_Pt3080TSoIPRx2PacketsPerFrame_Object = MibScalar
pt3080TSoIPRx2PacketsPerFrame = _Pt3080TSoIPRx2PacketsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 55),
    _Pt3080TSoIPRx2PacketsPerFrame_Type()
)
pt3080TSoIPRx2PacketsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2PacketsPerFrame.setStatus("current")
_Pt3080TSoIPRx2IpBitrate_Type = Integer32
_Pt3080TSoIPRx2IpBitrate_Object = MibScalar
pt3080TSoIPRx2IpBitrate = _Pt3080TSoIPRx2IpBitrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 56),
    _Pt3080TSoIPRx2IpBitrate_Type()
)
pt3080TSoIPRx2IpBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2IpBitrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2IpBitrate.setUnits("0.001 Mbps")
_Pt3080TSoIPRx2QueueSize_Type = Integer32
_Pt3080TSoIPRx2QueueSize_Object = MibScalar
pt3080TSoIPRx2QueueSize = _Pt3080TSoIPRx2QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 57),
    _Pt3080TSoIPRx2QueueSize_Type()
)
pt3080TSoIPRx2QueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2QueueSize.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2QueueSize.setUnits("1 Frames")
_Pt3080TSoIPRx2CurrentLatency_Type = Integer32
_Pt3080TSoIPRx2CurrentLatency_Object = MibScalar
pt3080TSoIPRx2CurrentLatency = _Pt3080TSoIPRx2CurrentLatency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 58),
    _Pt3080TSoIPRx2CurrentLatency_Type()
)
pt3080TSoIPRx2CurrentLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2CurrentLatency.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2CurrentLatency.setUnits("0.1 ms")
_Pt3080TSoIPRx2TSPacketSize_Type = Integer32
_Pt3080TSoIPRx2TSPacketSize_Object = MibScalar
pt3080TSoIPRx2TSPacketSize = _Pt3080TSoIPRx2TSPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 59),
    _Pt3080TSoIPRx2TSPacketSize_Type()
)
pt3080TSoIPRx2TSPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2TSPacketSize.setStatus("current")
_Pt3080TSoIPRx2OverrunIPFrames_Type = Integer32
_Pt3080TSoIPRx2OverrunIPFrames_Object = MibScalar
pt3080TSoIPRx2OverrunIPFrames = _Pt3080TSoIPRx2OverrunIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 10, 60),
    _Pt3080TSoIPRx2OverrunIPFrames_Type()
)
pt3080TSoIPRx2OverrunIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPRx2OverrunIPFrames.setStatus("current")
_Pt3080Monitor_ObjectIdentity = ObjectIdentity
pt3080Monitor = _Pt3080Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12)
)


class _Pt3080MonitorSource_Type(Integer32):
    """Custom type pt3080MonitorSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("asi-in1", 0),
          ("asi-in2", 1),
          ("aux1", 2),
          ("aux2", 3),
          ("tsoiprx1", 4),
          ("tsoiprx2", 5),
          ("ts-hp", 6),
          ("ts-lp", 7),
          ("backplane1", 8),
          ("backplane2", 9))
    )


_Pt3080MonitorSource_Type.__name__ = "Integer32"
_Pt3080MonitorSource_Object = MibScalar
pt3080MonitorSource = _Pt3080MonitorSource_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 1),
    _Pt3080MonitorSource_Type()
)
pt3080MonitorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorSource.setStatus("current")


class _Pt3080MonitorTSoIPEnable_Type(Integer32):
    """Custom type pt3080MonitorTSoIPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080MonitorTSoIPEnable_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPEnable_Object = MibScalar
pt3080MonitorTSoIPEnable = _Pt3080MonitorTSoIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 10),
    _Pt3080MonitorTSoIPEnable_Type()
)
pt3080MonitorTSoIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPEnable.setStatus("current")


class _Pt3080MonitorTSoIPSource_Type(Integer32):
    """Custom type pt3080MonitorTSoIPSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("asi-in1", 0),
          ("asi-in2", 1),
          ("aux1", 2),
          ("aux2", 3),
          ("tsoiprx1", 4),
          ("tsoiprx2", 5),
          ("ts-hp", 6),
          ("ts-lp", 7),
          ("backplane1", 8),
          ("backplane2", 9))
    )


_Pt3080MonitorTSoIPSource_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPSource_Object = MibScalar
pt3080MonitorTSoIPSource = _Pt3080MonitorTSoIPSource_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 11),
    _Pt3080MonitorTSoIPSource_Type()
)
pt3080MonitorTSoIPSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPSource.setStatus("current")
_Pt3080MonitorTSoIPDestIPAddress_Type = IpAddress
_Pt3080MonitorTSoIPDestIPAddress_Object = MibScalar
pt3080MonitorTSoIPDestIPAddress = _Pt3080MonitorTSoIPDestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 12),
    _Pt3080MonitorTSoIPDestIPAddress_Type()
)
pt3080MonitorTSoIPDestIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPDestIPAddress.setStatus("current")


class _Pt3080MonitorTSoIPDestPort_Type(Integer32):
    """Custom type pt3080MonitorTSoIPDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080MonitorTSoIPDestPort_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPDestPort_Object = MibScalar
pt3080MonitorTSoIPDestPort = _Pt3080MonitorTSoIPDestPort_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 13),
    _Pt3080MonitorTSoIPDestPort_Type()
)
pt3080MonitorTSoIPDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPDestPort.setStatus("current")


class _Pt3080MonitorTSoIPProtocol_Type(Integer32):
    """Custom type pt3080MonitorTSoIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("rtp", 1))
    )


_Pt3080MonitorTSoIPProtocol_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPProtocol_Object = MibScalar
pt3080MonitorTSoIPProtocol = _Pt3080MonitorTSoIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 14),
    _Pt3080MonitorTSoIPProtocol_Type()
)
pt3080MonitorTSoIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPProtocol.setStatus("current")


class _Pt3080MonitorTSoIPEnableFec_Type(Integer32):
    """Custom type pt3080MonitorTSoIPEnableFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080MonitorTSoIPEnableFec_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPEnableFec_Object = MibScalar
pt3080MonitorTSoIPEnableFec = _Pt3080MonitorTSoIPEnableFec_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 15),
    _Pt3080MonitorTSoIPEnableFec_Type()
)
pt3080MonitorTSoIPEnableFec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPEnableFec.setStatus("current")


class _Pt3080MonitorTSoIPFecColumn_Type(Integer32):
    """Custom type pt3080MonitorTSoIPFecColumn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Pt3080MonitorTSoIPFecColumn_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPFecColumn_Object = MibScalar
pt3080MonitorTSoIPFecColumn = _Pt3080MonitorTSoIPFecColumn_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 16),
    _Pt3080MonitorTSoIPFecColumn_Type()
)
pt3080MonitorTSoIPFecColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPFecColumn.setStatus("current")


class _Pt3080MonitorTSoIPFecRow_Type(Integer32):
    """Custom type pt3080MonitorTSoIPFecRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_Pt3080MonitorTSoIPFecRow_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPFecRow_Object = MibScalar
pt3080MonitorTSoIPFecRow = _Pt3080MonitorTSoIPFecRow_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 17),
    _Pt3080MonitorTSoIPFecRow_Type()
)
pt3080MonitorTSoIPFecRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPFecRow.setStatus("current")


class _Pt3080MonitorTSoIPFecSkew_Type(Integer32):
    """Custom type pt3080MonitorTSoIPFecSkew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Pt3080MonitorTSoIPFecSkew_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPFecSkew_Object = MibScalar
pt3080MonitorTSoIPFecSkew = _Pt3080MonitorTSoIPFecSkew_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 18),
    _Pt3080MonitorTSoIPFecSkew_Type()
)
pt3080MonitorTSoIPFecSkew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPFecSkew.setStatus("current")


class _Pt3080MonitorTSoIPKeepNullPackets_Type(Integer32):
    """Custom type pt3080MonitorTSoIPKeepNullPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080MonitorTSoIPKeepNullPackets_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPKeepNullPackets_Object = MibScalar
pt3080MonitorTSoIPKeepNullPackets = _Pt3080MonitorTSoIPKeepNullPackets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 19),
    _Pt3080MonitorTSoIPKeepNullPackets_Type()
)
pt3080MonitorTSoIPKeepNullPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPKeepNullPackets.setStatus("current")


class _Pt3080MonitorTSoIPPacketsPerFrame_Type(Integer32):
    """Custom type pt3080MonitorTSoIPPacketsPerFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Pt3080MonitorTSoIPPacketsPerFrame_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPPacketsPerFrame_Object = MibScalar
pt3080MonitorTSoIPPacketsPerFrame = _Pt3080MonitorTSoIPPacketsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 20),
    _Pt3080MonitorTSoIPPacketsPerFrame_Type()
)
pt3080MonitorTSoIPPacketsPerFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPPacketsPerFrame.setStatus("current")


class _Pt3080MonitorTSoIPUDPChecksum_Type(Integer32):
    """Custom type pt3080MonitorTSoIPUDPChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080MonitorTSoIPUDPChecksum_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPUDPChecksum_Object = MibScalar
pt3080MonitorTSoIPUDPChecksum = _Pt3080MonitorTSoIPUDPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 21),
    _Pt3080MonitorTSoIPUDPChecksum_Type()
)
pt3080MonitorTSoIPUDPChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPUDPChecksum.setStatus("current")


class _Pt3080MonitorTSoIPDSCP_Type(Integer32):
    """Custom type pt3080MonitorTSoIPDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080MonitorTSoIPDSCP_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPDSCP_Object = MibScalar
pt3080MonitorTSoIPDSCP = _Pt3080MonitorTSoIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 22),
    _Pt3080MonitorTSoIPDSCP_Type()
)
pt3080MonitorTSoIPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPDSCP.setStatus("current")


class _Pt3080MonitorTSoIPTTL_Type(Integer32):
    """Custom type pt3080MonitorTSoIPTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Pt3080MonitorTSoIPTTL_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPTTL_Object = MibScalar
pt3080MonitorTSoIPTTL = _Pt3080MonitorTSoIPTTL_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 23),
    _Pt3080MonitorTSoIPTTL_Type()
)
pt3080MonitorTSoIPTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPTTL.setStatus("current")


class _Pt3080MonitorTSoIPGenerateError_Type(Integer32):
    """Custom type pt3080MonitorTSoIPGenerateError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pt3080MonitorTSoIPGenerateError_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPGenerateError_Object = MibScalar
pt3080MonitorTSoIPGenerateError = _Pt3080MonitorTSoIPGenerateError_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 24),
    _Pt3080MonitorTSoIPGenerateError_Type()
)
pt3080MonitorTSoIPGenerateError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPGenerateError.setStatus("current")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPGenerateError.setUnits("0.1 %")


class _Pt3080MonitorTSoIPMulticastLanSelect_Type(Integer32):
    """Custom type pt3080MonitorTSoIPMulticastLanSelect based on Integer32"""
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
        *(("flan", 0),
          ("alan", 1),
          ("tlan", 2),
          ("blan", 3),
          ("plan", 4))
    )


_Pt3080MonitorTSoIPMulticastLanSelect_Type.__name__ = "Integer32"
_Pt3080MonitorTSoIPMulticastLanSelect_Object = MibScalar
pt3080MonitorTSoIPMulticastLanSelect = _Pt3080MonitorTSoIPMulticastLanSelect_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 25),
    _Pt3080MonitorTSoIPMulticastLanSelect_Type()
)
pt3080MonitorTSoIPMulticastLanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPMulticastLanSelect.setStatus("current")
_Pt3080MonitorTSoIPIpBitrate_Type = Integer32
_Pt3080MonitorTSoIPIpBitrate_Object = MibScalar
pt3080MonitorTSoIPIpBitrate = _Pt3080MonitorTSoIPIpBitrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 30),
    _Pt3080MonitorTSoIPIpBitrate_Type()
)
pt3080MonitorTSoIPIpBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPIpBitrate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPIpBitrate.setUnits("0.001 Mbps")
_Pt3080MonitorTSoIPLostIPFrames_Type = Integer32
_Pt3080MonitorTSoIPLostIPFrames_Object = MibScalar
pt3080MonitorTSoIPLostIPFrames = _Pt3080MonitorTSoIPLostIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 31),
    _Pt3080MonitorTSoIPLostIPFrames_Type()
)
pt3080MonitorTSoIPLostIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPLostIPFrames.setStatus("current")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPLostIPFrames.setUnits("1 Mbps")
_Pt3080MonitorTSoIPTSSize_Type = Integer32
_Pt3080MonitorTSoIPTSSize_Object = MibScalar
pt3080MonitorTSoIPTSSize = _Pt3080MonitorTSoIPTSSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 12, 32),
    _Pt3080MonitorTSoIPTSSize_Type()
)
pt3080MonitorTSoIPTSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPTSSize.setStatus("current")
if mibBuilder.loadTexts:
    pt3080MonitorTSoIPTSSize.setUnits("1 bytes")
_Pt3080Test_ObjectIdentity = ObjectIdentity
pt3080Test = _Pt3080Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 13)
)


class _Pt3080TestEnable_Type(Integer32):
    """Custom type pt3080TestEnable based on Integer32"""
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
        *(("off", 0),
          ("scar", 1),
          ("sweep2", 2),
          ("prbs-on", 3),
          ("prbs-auto", 4))
    )


_Pt3080TestEnable_Type.__name__ = "Integer32"
_Pt3080TestEnable_Object = MibScalar
pt3080TestEnable = _Pt3080TestEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 13, 1),
    _Pt3080TestEnable_Type()
)
pt3080TestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TestEnable.setStatus("current")


class _Pt3080TestEnableReconnect_Type(Integer32):
    """Custom type pt3080TestEnableReconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080TestEnableReconnect_Type.__name__ = "Integer32"
_Pt3080TestEnableReconnect_Object = MibScalar
pt3080TestEnableReconnect = _Pt3080TestEnableReconnect_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 13, 2),
    _Pt3080TestEnableReconnect_Type()
)
pt3080TestEnableReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TestEnableReconnect.setStatus("current")


class _Pt3080TestScarrierLevel_Type(Integer32):
    """Custom type pt3080TestScarrierLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pt3080TestScarrierLevel_Type.__name__ = "Integer32"
_Pt3080TestScarrierLevel_Object = MibScalar
pt3080TestScarrierLevel = _Pt3080TestScarrierLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 13, 3),
    _Pt3080TestScarrierLevel_Type()
)
pt3080TestScarrierLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TestScarrierLevel.setStatus("current")


class _Pt3080TestscarrierFrequencyOffset_Type(Integer32):
    """Custom type pt3080TestscarrierFrequencyOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000000, 4000000),
    )


_Pt3080TestscarrierFrequencyOffset_Type.__name__ = "Integer32"
_Pt3080TestscarrierFrequencyOffset_Object = MibScalar
pt3080TestscarrierFrequencyOffset = _Pt3080TestscarrierFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 13, 4),
    _Pt3080TestscarrierFrequencyOffset_Type()
)
pt3080TestscarrierFrequencyOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TestscarrierFrequencyOffset.setStatus("current")
if mibBuilder.loadTexts:
    pt3080TestscarrierFrequencyOffset.setUnits("1 Hz")
_Pt3080Alarm_ObjectIdentity = ObjectIdentity
pt3080Alarm = _Pt3080Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14)
)
_Pt3080GroupAlarmTable_Object = MibTable
pt3080GroupAlarmTable = _Pt3080GroupAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1)
)
if mibBuilder.loadTexts:
    pt3080GroupAlarmTable.setStatus("current")
_Pt3080GroupAlarmEntry_Object = MibTableRow
pt3080GroupAlarmEntry = _Pt3080GroupAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1)
)
pt3080GroupAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080GroupAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080GroupAlarmEntry.setStatus("current")


class _Pt3080GroupAlarmID_Type(Integer32):
    """Custom type pt3080GroupAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080GroupAlarmID_Type.__name__ = "Integer32"
_Pt3080GroupAlarmID_Object = MibTableColumn
pt3080GroupAlarmID = _Pt3080GroupAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 1),
    _Pt3080GroupAlarmID_Type()
)
pt3080GroupAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080GroupAlarmID.setStatus("current")
_Pt3080GroupAlarmDescription_Type = DisplayString
_Pt3080GroupAlarmDescription_Object = MibTableColumn
pt3080GroupAlarmDescription = _Pt3080GroupAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 2),
    _Pt3080GroupAlarmDescription_Type()
)
pt3080GroupAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GroupAlarmDescription.setStatus("current")


class _Pt3080GroupAlarmState_Type(Integer32):
    """Custom type pt3080GroupAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080GroupAlarmState_Type.__name__ = "Integer32"
_Pt3080GroupAlarmState_Object = MibTableColumn
pt3080GroupAlarmState = _Pt3080GroupAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 3),
    _Pt3080GroupAlarmState_Type()
)
pt3080GroupAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GroupAlarmState.setStatus("current")


class _Pt3080GroupAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080GroupAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GroupAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080GroupAlarmActionEventlog_Object = MibTableColumn
pt3080GroupAlarmActionEventlog = _Pt3080GroupAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 4),
    _Pt3080GroupAlarmActionEventlog_Type()
)
pt3080GroupAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GroupAlarmActionEventlog.setStatus("current")


class _Pt3080GroupAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080GroupAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GroupAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080GroupAlarmActionRelay1_Object = MibTableColumn
pt3080GroupAlarmActionRelay1 = _Pt3080GroupAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 5),
    _Pt3080GroupAlarmActionRelay1_Type()
)
pt3080GroupAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GroupAlarmActionRelay1.setStatus("current")


class _Pt3080GroupAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080GroupAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GroupAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080GroupAlarmActionRelay2_Object = MibTableColumn
pt3080GroupAlarmActionRelay2 = _Pt3080GroupAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 6),
    _Pt3080GroupAlarmActionRelay2_Type()
)
pt3080GroupAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GroupAlarmActionRelay2.setStatus("current")


class _Pt3080GroupAlarmActionTrap_Type(Integer32):
    """Custom type pt3080GroupAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GroupAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080GroupAlarmActionTrap_Object = MibTableColumn
pt3080GroupAlarmActionTrap = _Pt3080GroupAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 7),
    _Pt3080GroupAlarmActionTrap_Type()
)
pt3080GroupAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GroupAlarmActionTrap.setStatus("current")


class _Pt3080GroupAlarmActionEmail_Type(Integer32):
    """Custom type pt3080GroupAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GroupAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080GroupAlarmActionEmail_Object = MibTableColumn
pt3080GroupAlarmActionEmail = _Pt3080GroupAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 8),
    _Pt3080GroupAlarmActionEmail_Type()
)
pt3080GroupAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GroupAlarmActionEmail.setStatus("current")


class _Pt3080GroupAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080GroupAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GroupAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080GroupAlarmActionAlarmLED_Object = MibTableColumn
pt3080GroupAlarmActionAlarmLED = _Pt3080GroupAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 9),
    _Pt3080GroupAlarmActionAlarmLED_Type()
)
pt3080GroupAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GroupAlarmActionAlarmLED.setStatus("current")


class _Pt3080GroupAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080GroupAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080GroupAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080GroupAlarmActionForceMode_Object = MibTableColumn
pt3080GroupAlarmActionForceMode = _Pt3080GroupAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 1, 1, 10),
    _Pt3080GroupAlarmActionForceMode_Type()
)
pt3080GroupAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GroupAlarmActionForceMode.setStatus("current")
_Pt3080ASITSPrimaryAlarmTable_Object = MibTable
pt3080ASITSPrimaryAlarmTable = _Pt3080ASITSPrimaryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5)
)
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmTable.setStatus("current")
_Pt3080ASITSPrimaryAlarmEntry_Object = MibTableRow
pt3080ASITSPrimaryAlarmEntry = _Pt3080ASITSPrimaryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1)
)
pt3080ASITSPrimaryAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080ASITSPrimaryAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmEntry.setStatus("current")


class _Pt3080ASITSPrimaryAlarmID_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080ASITSPrimaryAlarmID_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmID_Object = MibTableColumn
pt3080ASITSPrimaryAlarmID = _Pt3080ASITSPrimaryAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 1),
    _Pt3080ASITSPrimaryAlarmID_Type()
)
pt3080ASITSPrimaryAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmID.setStatus("current")
_Pt3080ASITSPrimaryAlarmDescription_Type = DisplayString
_Pt3080ASITSPrimaryAlarmDescription_Object = MibTableColumn
pt3080ASITSPrimaryAlarmDescription = _Pt3080ASITSPrimaryAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 2),
    _Pt3080ASITSPrimaryAlarmDescription_Type()
)
pt3080ASITSPrimaryAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmDescription.setStatus("current")


class _Pt3080ASITSPrimaryAlarmState_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080ASITSPrimaryAlarmState_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmState_Object = MibTableColumn
pt3080ASITSPrimaryAlarmState = _Pt3080ASITSPrimaryAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 3),
    _Pt3080ASITSPrimaryAlarmState_Type()
)
pt3080ASITSPrimaryAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmState.setStatus("current")


class _Pt3080ASITSPrimaryAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSPrimaryAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmActionEventlog_Object = MibTableColumn
pt3080ASITSPrimaryAlarmActionEventlog = _Pt3080ASITSPrimaryAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 4),
    _Pt3080ASITSPrimaryAlarmActionEventlog_Type()
)
pt3080ASITSPrimaryAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmActionEventlog.setStatus("current")


class _Pt3080ASITSPrimaryAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSPrimaryAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmActionRelay1_Object = MibTableColumn
pt3080ASITSPrimaryAlarmActionRelay1 = _Pt3080ASITSPrimaryAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 5),
    _Pt3080ASITSPrimaryAlarmActionRelay1_Type()
)
pt3080ASITSPrimaryAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmActionRelay1.setStatus("current")


class _Pt3080ASITSPrimaryAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSPrimaryAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmActionRelay2_Object = MibTableColumn
pt3080ASITSPrimaryAlarmActionRelay2 = _Pt3080ASITSPrimaryAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 6),
    _Pt3080ASITSPrimaryAlarmActionRelay2_Type()
)
pt3080ASITSPrimaryAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmActionRelay2.setStatus("current")


class _Pt3080ASITSPrimaryAlarmActionTrap_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSPrimaryAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmActionTrap_Object = MibTableColumn
pt3080ASITSPrimaryAlarmActionTrap = _Pt3080ASITSPrimaryAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 7),
    _Pt3080ASITSPrimaryAlarmActionTrap_Type()
)
pt3080ASITSPrimaryAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmActionTrap.setStatus("current")


class _Pt3080ASITSPrimaryAlarmActionEmail_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSPrimaryAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmActionEmail_Object = MibTableColumn
pt3080ASITSPrimaryAlarmActionEmail = _Pt3080ASITSPrimaryAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 8),
    _Pt3080ASITSPrimaryAlarmActionEmail_Type()
)
pt3080ASITSPrimaryAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmActionEmail.setStatus("current")


class _Pt3080ASITSPrimaryAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSPrimaryAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmActionAlarmLED_Object = MibTableColumn
pt3080ASITSPrimaryAlarmActionAlarmLED = _Pt3080ASITSPrimaryAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 9),
    _Pt3080ASITSPrimaryAlarmActionAlarmLED_Type()
)
pt3080ASITSPrimaryAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmActionAlarmLED.setStatus("current")


class _Pt3080ASITSPrimaryAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080ASITSPrimaryAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080ASITSPrimaryAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080ASITSPrimaryAlarmActionForceMode_Object = MibTableColumn
pt3080ASITSPrimaryAlarmActionForceMode = _Pt3080ASITSPrimaryAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 5, 1, 10),
    _Pt3080ASITSPrimaryAlarmActionForceMode_Type()
)
pt3080ASITSPrimaryAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSPrimaryAlarmActionForceMode.setStatus("current")
_Pt3080ASITSSecondaryAlarmTable_Object = MibTable
pt3080ASITSSecondaryAlarmTable = _Pt3080ASITSSecondaryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6)
)
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmTable.setStatus("current")
_Pt3080ASITSSecondaryAlarmEntry_Object = MibTableRow
pt3080ASITSSecondaryAlarmEntry = _Pt3080ASITSSecondaryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1)
)
pt3080ASITSSecondaryAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080ASITSSecondaryAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmEntry.setStatus("current")


class _Pt3080ASITSSecondaryAlarmID_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080ASITSSecondaryAlarmID_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmID_Object = MibTableColumn
pt3080ASITSSecondaryAlarmID = _Pt3080ASITSSecondaryAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 1),
    _Pt3080ASITSSecondaryAlarmID_Type()
)
pt3080ASITSSecondaryAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmID.setStatus("current")
_Pt3080ASITSSecondaryAlarmDescription_Type = DisplayString
_Pt3080ASITSSecondaryAlarmDescription_Object = MibTableColumn
pt3080ASITSSecondaryAlarmDescription = _Pt3080ASITSSecondaryAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 2),
    _Pt3080ASITSSecondaryAlarmDescription_Type()
)
pt3080ASITSSecondaryAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmDescription.setStatus("current")


class _Pt3080ASITSSecondaryAlarmState_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080ASITSSecondaryAlarmState_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmState_Object = MibTableColumn
pt3080ASITSSecondaryAlarmState = _Pt3080ASITSSecondaryAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 3),
    _Pt3080ASITSSecondaryAlarmState_Type()
)
pt3080ASITSSecondaryAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmState.setStatus("current")


class _Pt3080ASITSSecondaryAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSSecondaryAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmActionEventlog_Object = MibTableColumn
pt3080ASITSSecondaryAlarmActionEventlog = _Pt3080ASITSSecondaryAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 4),
    _Pt3080ASITSSecondaryAlarmActionEventlog_Type()
)
pt3080ASITSSecondaryAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmActionEventlog.setStatus("current")


class _Pt3080ASITSSecondaryAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSSecondaryAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmActionRelay1_Object = MibTableColumn
pt3080ASITSSecondaryAlarmActionRelay1 = _Pt3080ASITSSecondaryAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 5),
    _Pt3080ASITSSecondaryAlarmActionRelay1_Type()
)
pt3080ASITSSecondaryAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmActionRelay1.setStatus("current")


class _Pt3080ASITSSecondaryAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSSecondaryAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmActionRelay2_Object = MibTableColumn
pt3080ASITSSecondaryAlarmActionRelay2 = _Pt3080ASITSSecondaryAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 6),
    _Pt3080ASITSSecondaryAlarmActionRelay2_Type()
)
pt3080ASITSSecondaryAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmActionRelay2.setStatus("current")


class _Pt3080ASITSSecondaryAlarmActionTrap_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSSecondaryAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmActionTrap_Object = MibTableColumn
pt3080ASITSSecondaryAlarmActionTrap = _Pt3080ASITSSecondaryAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 7),
    _Pt3080ASITSSecondaryAlarmActionTrap_Type()
)
pt3080ASITSSecondaryAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmActionTrap.setStatus("current")


class _Pt3080ASITSSecondaryAlarmActionEmail_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSSecondaryAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmActionEmail_Object = MibTableColumn
pt3080ASITSSecondaryAlarmActionEmail = _Pt3080ASITSSecondaryAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 8),
    _Pt3080ASITSSecondaryAlarmActionEmail_Type()
)
pt3080ASITSSecondaryAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmActionEmail.setStatus("current")


class _Pt3080ASITSSecondaryAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASITSSecondaryAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmActionAlarmLED_Object = MibTableColumn
pt3080ASITSSecondaryAlarmActionAlarmLED = _Pt3080ASITSSecondaryAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 9),
    _Pt3080ASITSSecondaryAlarmActionAlarmLED_Type()
)
pt3080ASITSSecondaryAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmActionAlarmLED.setStatus("current")


class _Pt3080ASITSSecondaryAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080ASITSSecondaryAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080ASITSSecondaryAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080ASITSSecondaryAlarmActionForceMode_Object = MibTableColumn
pt3080ASITSSecondaryAlarmActionForceMode = _Pt3080ASITSSecondaryAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 6, 1, 10),
    _Pt3080ASITSSecondaryAlarmActionForceMode_Type()
)
pt3080ASITSSecondaryAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASITSSecondaryAlarmActionForceMode.setStatus("current")
_Pt3080SFNAlarmTable_Object = MibTable
pt3080SFNAlarmTable = _Pt3080SFNAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7)
)
if mibBuilder.loadTexts:
    pt3080SFNAlarmTable.setStatus("current")
_Pt3080SFNAlarmEntry_Object = MibTableRow
pt3080SFNAlarmEntry = _Pt3080SFNAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1)
)
pt3080SFNAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080SFNAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080SFNAlarmEntry.setStatus("current")


class _Pt3080SFNAlarmID_Type(Integer32):
    """Custom type pt3080SFNAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080SFNAlarmID_Type.__name__ = "Integer32"
_Pt3080SFNAlarmID_Object = MibTableColumn
pt3080SFNAlarmID = _Pt3080SFNAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 1),
    _Pt3080SFNAlarmID_Type()
)
pt3080SFNAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080SFNAlarmID.setStatus("current")
_Pt3080SFNAlarmDescription_Type = DisplayString
_Pt3080SFNAlarmDescription_Object = MibTableColumn
pt3080SFNAlarmDescription = _Pt3080SFNAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 2),
    _Pt3080SFNAlarmDescription_Type()
)
pt3080SFNAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SFNAlarmDescription.setStatus("current")


class _Pt3080SFNAlarmState_Type(Integer32):
    """Custom type pt3080SFNAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080SFNAlarmState_Type.__name__ = "Integer32"
_Pt3080SFNAlarmState_Object = MibTableColumn
pt3080SFNAlarmState = _Pt3080SFNAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 3),
    _Pt3080SFNAlarmState_Type()
)
pt3080SFNAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080SFNAlarmState.setStatus("current")


class _Pt3080SFNAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080SFNAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080SFNAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080SFNAlarmActionEventlog_Object = MibTableColumn
pt3080SFNAlarmActionEventlog = _Pt3080SFNAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 4),
    _Pt3080SFNAlarmActionEventlog_Type()
)
pt3080SFNAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SFNAlarmActionEventlog.setStatus("current")


class _Pt3080SFNAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080SFNAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080SFNAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080SFNAlarmActionRelay1_Object = MibTableColumn
pt3080SFNAlarmActionRelay1 = _Pt3080SFNAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 5),
    _Pt3080SFNAlarmActionRelay1_Type()
)
pt3080SFNAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SFNAlarmActionRelay1.setStatus("current")


class _Pt3080SFNAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080SFNAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080SFNAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080SFNAlarmActionRelay2_Object = MibTableColumn
pt3080SFNAlarmActionRelay2 = _Pt3080SFNAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 6),
    _Pt3080SFNAlarmActionRelay2_Type()
)
pt3080SFNAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SFNAlarmActionRelay2.setStatus("current")


class _Pt3080SFNAlarmActionTrap_Type(Integer32):
    """Custom type pt3080SFNAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080SFNAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080SFNAlarmActionTrap_Object = MibTableColumn
pt3080SFNAlarmActionTrap = _Pt3080SFNAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 7),
    _Pt3080SFNAlarmActionTrap_Type()
)
pt3080SFNAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SFNAlarmActionTrap.setStatus("current")


class _Pt3080SFNAlarmActionEmail_Type(Integer32):
    """Custom type pt3080SFNAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080SFNAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080SFNAlarmActionEmail_Object = MibTableColumn
pt3080SFNAlarmActionEmail = _Pt3080SFNAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 8),
    _Pt3080SFNAlarmActionEmail_Type()
)
pt3080SFNAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SFNAlarmActionEmail.setStatus("current")


class _Pt3080SFNAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080SFNAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080SFNAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080SFNAlarmActionAlarmLED_Object = MibTableColumn
pt3080SFNAlarmActionAlarmLED = _Pt3080SFNAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 9),
    _Pt3080SFNAlarmActionAlarmLED_Type()
)
pt3080SFNAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SFNAlarmActionAlarmLED.setStatus("current")


class _Pt3080SFNAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080SFNAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080SFNAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080SFNAlarmActionForceMode_Object = MibTableColumn
pt3080SFNAlarmActionForceMode = _Pt3080SFNAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 7, 1, 10),
    _Pt3080SFNAlarmActionForceMode_Type()
)
pt3080SFNAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080SFNAlarmActionForceMode.setStatus("current")
_Pt3080ReferenceAlarmTable_Object = MibTable
pt3080ReferenceAlarmTable = _Pt3080ReferenceAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8)
)
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmTable.setStatus("current")
_Pt3080ReferenceAlarmEntry_Object = MibTableRow
pt3080ReferenceAlarmEntry = _Pt3080ReferenceAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1)
)
pt3080ReferenceAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080ReferenceAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmEntry.setStatus("current")


class _Pt3080ReferenceAlarmID_Type(Integer32):
    """Custom type pt3080ReferenceAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080ReferenceAlarmID_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmID_Object = MibTableColumn
pt3080ReferenceAlarmID = _Pt3080ReferenceAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 1),
    _Pt3080ReferenceAlarmID_Type()
)
pt3080ReferenceAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmID.setStatus("current")
_Pt3080ReferenceAlarmDescription_Type = DisplayString
_Pt3080ReferenceAlarmDescription_Object = MibTableColumn
pt3080ReferenceAlarmDescription = _Pt3080ReferenceAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 2),
    _Pt3080ReferenceAlarmDescription_Type()
)
pt3080ReferenceAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmDescription.setStatus("current")


class _Pt3080ReferenceAlarmState_Type(Integer32):
    """Custom type pt3080ReferenceAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080ReferenceAlarmState_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmState_Object = MibTableColumn
pt3080ReferenceAlarmState = _Pt3080ReferenceAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 3),
    _Pt3080ReferenceAlarmState_Type()
)
pt3080ReferenceAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmState.setStatus("current")


class _Pt3080ReferenceAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080ReferenceAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ReferenceAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmActionEventlog_Object = MibTableColumn
pt3080ReferenceAlarmActionEventlog = _Pt3080ReferenceAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 4),
    _Pt3080ReferenceAlarmActionEventlog_Type()
)
pt3080ReferenceAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmActionEventlog.setStatus("current")


class _Pt3080ReferenceAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080ReferenceAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ReferenceAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmActionRelay1_Object = MibTableColumn
pt3080ReferenceAlarmActionRelay1 = _Pt3080ReferenceAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 5),
    _Pt3080ReferenceAlarmActionRelay1_Type()
)
pt3080ReferenceAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmActionRelay1.setStatus("current")


class _Pt3080ReferenceAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080ReferenceAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ReferenceAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmActionRelay2_Object = MibTableColumn
pt3080ReferenceAlarmActionRelay2 = _Pt3080ReferenceAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 6),
    _Pt3080ReferenceAlarmActionRelay2_Type()
)
pt3080ReferenceAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmActionRelay2.setStatus("current")


class _Pt3080ReferenceAlarmActionTrap_Type(Integer32):
    """Custom type pt3080ReferenceAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ReferenceAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmActionTrap_Object = MibTableColumn
pt3080ReferenceAlarmActionTrap = _Pt3080ReferenceAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 7),
    _Pt3080ReferenceAlarmActionTrap_Type()
)
pt3080ReferenceAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmActionTrap.setStatus("current")


class _Pt3080ReferenceAlarmActionEmail_Type(Integer32):
    """Custom type pt3080ReferenceAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ReferenceAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmActionEmail_Object = MibTableColumn
pt3080ReferenceAlarmActionEmail = _Pt3080ReferenceAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 8),
    _Pt3080ReferenceAlarmActionEmail_Type()
)
pt3080ReferenceAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmActionEmail.setStatus("current")


class _Pt3080ReferenceAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080ReferenceAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ReferenceAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmActionAlarmLED_Object = MibTableColumn
pt3080ReferenceAlarmActionAlarmLED = _Pt3080ReferenceAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 9),
    _Pt3080ReferenceAlarmActionAlarmLED_Type()
)
pt3080ReferenceAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmActionAlarmLED.setStatus("current")


class _Pt3080ReferenceAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080ReferenceAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080ReferenceAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080ReferenceAlarmActionForceMode_Object = MibTableColumn
pt3080ReferenceAlarmActionForceMode = _Pt3080ReferenceAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 8, 1, 10),
    _Pt3080ReferenceAlarmActionForceMode_Type()
)
pt3080ReferenceAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReferenceAlarmActionForceMode.setStatus("current")
_Pt3080RFAlarmTable_Object = MibTable
pt3080RFAlarmTable = _Pt3080RFAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9)
)
if mibBuilder.loadTexts:
    pt3080RFAlarmTable.setStatus("current")
_Pt3080RFAlarmEntry_Object = MibTableRow
pt3080RFAlarmEntry = _Pt3080RFAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1)
)
pt3080RFAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080RFAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080RFAlarmEntry.setStatus("current")


class _Pt3080RFAlarmID_Type(Integer32):
    """Custom type pt3080RFAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080RFAlarmID_Type.__name__ = "Integer32"
_Pt3080RFAlarmID_Object = MibTableColumn
pt3080RFAlarmID = _Pt3080RFAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 1),
    _Pt3080RFAlarmID_Type()
)
pt3080RFAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080RFAlarmID.setStatus("current")
_Pt3080RFAlarmDescription_Type = DisplayString
_Pt3080RFAlarmDescription_Object = MibTableColumn
pt3080RFAlarmDescription = _Pt3080RFAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 2),
    _Pt3080RFAlarmDescription_Type()
)
pt3080RFAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080RFAlarmDescription.setStatus("current")


class _Pt3080RFAlarmState_Type(Integer32):
    """Custom type pt3080RFAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080RFAlarmState_Type.__name__ = "Integer32"
_Pt3080RFAlarmState_Object = MibTableColumn
pt3080RFAlarmState = _Pt3080RFAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 3),
    _Pt3080RFAlarmState_Type()
)
pt3080RFAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080RFAlarmState.setStatus("current")


class _Pt3080RFAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080RFAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080RFAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080RFAlarmActionEventlog_Object = MibTableColumn
pt3080RFAlarmActionEventlog = _Pt3080RFAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 4),
    _Pt3080RFAlarmActionEventlog_Type()
)
pt3080RFAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080RFAlarmActionEventlog.setStatus("current")


class _Pt3080RFAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080RFAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080RFAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080RFAlarmActionRelay1_Object = MibTableColumn
pt3080RFAlarmActionRelay1 = _Pt3080RFAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 5),
    _Pt3080RFAlarmActionRelay1_Type()
)
pt3080RFAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080RFAlarmActionRelay1.setStatus("current")


class _Pt3080RFAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080RFAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080RFAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080RFAlarmActionRelay2_Object = MibTableColumn
pt3080RFAlarmActionRelay2 = _Pt3080RFAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 6),
    _Pt3080RFAlarmActionRelay2_Type()
)
pt3080RFAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080RFAlarmActionRelay2.setStatus("current")


class _Pt3080RFAlarmActionTrap_Type(Integer32):
    """Custom type pt3080RFAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080RFAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080RFAlarmActionTrap_Object = MibTableColumn
pt3080RFAlarmActionTrap = _Pt3080RFAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 7),
    _Pt3080RFAlarmActionTrap_Type()
)
pt3080RFAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080RFAlarmActionTrap.setStatus("current")


class _Pt3080RFAlarmActionEmail_Type(Integer32):
    """Custom type pt3080RFAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080RFAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080RFAlarmActionEmail_Object = MibTableColumn
pt3080RFAlarmActionEmail = _Pt3080RFAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 8),
    _Pt3080RFAlarmActionEmail_Type()
)
pt3080RFAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080RFAlarmActionEmail.setStatus("current")


class _Pt3080RFAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080RFAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080RFAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080RFAlarmActionAlarmLED_Object = MibTableColumn
pt3080RFAlarmActionAlarmLED = _Pt3080RFAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 9),
    _Pt3080RFAlarmActionAlarmLED_Type()
)
pt3080RFAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080RFAlarmActionAlarmLED.setStatus("current")


class _Pt3080RFAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080RFAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080RFAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080RFAlarmActionForceMode_Object = MibTableColumn
pt3080RFAlarmActionForceMode = _Pt3080RFAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 9, 1, 10),
    _Pt3080RFAlarmActionForceMode_Type()
)
pt3080RFAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080RFAlarmActionForceMode.setStatus("current")
_Pt3080GPSAlarmTable_Object = MibTable
pt3080GPSAlarmTable = _Pt3080GPSAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10)
)
if mibBuilder.loadTexts:
    pt3080GPSAlarmTable.setStatus("current")
_Pt3080GPSAlarmEntry_Object = MibTableRow
pt3080GPSAlarmEntry = _Pt3080GPSAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1)
)
pt3080GPSAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080GPSAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080GPSAlarmEntry.setStatus("current")


class _Pt3080GPSAlarmID_Type(Integer32):
    """Custom type pt3080GPSAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080GPSAlarmID_Type.__name__ = "Integer32"
_Pt3080GPSAlarmID_Object = MibTableColumn
pt3080GPSAlarmID = _Pt3080GPSAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 1),
    _Pt3080GPSAlarmID_Type()
)
pt3080GPSAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080GPSAlarmID.setStatus("current")
_Pt3080GPSAlarmDescription_Type = DisplayString
_Pt3080GPSAlarmDescription_Object = MibTableColumn
pt3080GPSAlarmDescription = _Pt3080GPSAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 2),
    _Pt3080GPSAlarmDescription_Type()
)
pt3080GPSAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GPSAlarmDescription.setStatus("current")


class _Pt3080GPSAlarmState_Type(Integer32):
    """Custom type pt3080GPSAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080GPSAlarmState_Type.__name__ = "Integer32"
_Pt3080GPSAlarmState_Object = MibTableColumn
pt3080GPSAlarmState = _Pt3080GPSAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 3),
    _Pt3080GPSAlarmState_Type()
)
pt3080GPSAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080GPSAlarmState.setStatus("current")


class _Pt3080GPSAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080GPSAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GPSAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080GPSAlarmActionEventlog_Object = MibTableColumn
pt3080GPSAlarmActionEventlog = _Pt3080GPSAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 4),
    _Pt3080GPSAlarmActionEventlog_Type()
)
pt3080GPSAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GPSAlarmActionEventlog.setStatus("current")


class _Pt3080GPSAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080GPSAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GPSAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080GPSAlarmActionRelay1_Object = MibTableColumn
pt3080GPSAlarmActionRelay1 = _Pt3080GPSAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 5),
    _Pt3080GPSAlarmActionRelay1_Type()
)
pt3080GPSAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GPSAlarmActionRelay1.setStatus("current")


class _Pt3080GPSAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080GPSAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GPSAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080GPSAlarmActionRelay2_Object = MibTableColumn
pt3080GPSAlarmActionRelay2 = _Pt3080GPSAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 6),
    _Pt3080GPSAlarmActionRelay2_Type()
)
pt3080GPSAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GPSAlarmActionRelay2.setStatus("current")


class _Pt3080GPSAlarmActionTrap_Type(Integer32):
    """Custom type pt3080GPSAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GPSAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080GPSAlarmActionTrap_Object = MibTableColumn
pt3080GPSAlarmActionTrap = _Pt3080GPSAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 7),
    _Pt3080GPSAlarmActionTrap_Type()
)
pt3080GPSAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GPSAlarmActionTrap.setStatus("current")


class _Pt3080GPSAlarmActionEmail_Type(Integer32):
    """Custom type pt3080GPSAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GPSAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080GPSAlarmActionEmail_Object = MibTableColumn
pt3080GPSAlarmActionEmail = _Pt3080GPSAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 8),
    _Pt3080GPSAlarmActionEmail_Type()
)
pt3080GPSAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GPSAlarmActionEmail.setStatus("current")


class _Pt3080GPSAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080GPSAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080GPSAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080GPSAlarmActionAlarmLED_Object = MibTableColumn
pt3080GPSAlarmActionAlarmLED = _Pt3080GPSAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 9),
    _Pt3080GPSAlarmActionAlarmLED_Type()
)
pt3080GPSAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GPSAlarmActionAlarmLED.setStatus("current")


class _Pt3080GPSAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080GPSAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080GPSAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080GPSAlarmActionForceMode_Object = MibTableColumn
pt3080GPSAlarmActionForceMode = _Pt3080GPSAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 10, 1, 10),
    _Pt3080GPSAlarmActionForceMode_Type()
)
pt3080GPSAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080GPSAlarmActionForceMode.setStatus("current")
_Pt3080TSoIPAlarmTable_Object = MibTable
pt3080TSoIPAlarmTable = _Pt3080TSoIPAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12)
)
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmTable.setStatus("current")
_Pt3080TSoIPAlarmEntry_Object = MibTableRow
pt3080TSoIPAlarmEntry = _Pt3080TSoIPAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1)
)
pt3080TSoIPAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080TSoIPAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmEntry.setStatus("current")


class _Pt3080TSoIPAlarmID_Type(Integer32):
    """Custom type pt3080TSoIPAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080TSoIPAlarmID_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmID_Object = MibTableColumn
pt3080TSoIPAlarmID = _Pt3080TSoIPAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 1),
    _Pt3080TSoIPAlarmID_Type()
)
pt3080TSoIPAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmID.setStatus("current")
_Pt3080TSoIPAlarmDescription_Type = DisplayString
_Pt3080TSoIPAlarmDescription_Object = MibTableColumn
pt3080TSoIPAlarmDescription = _Pt3080TSoIPAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 2),
    _Pt3080TSoIPAlarmDescription_Type()
)
pt3080TSoIPAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmDescription.setStatus("current")


class _Pt3080TSoIPAlarmState_Type(Integer32):
    """Custom type pt3080TSoIPAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080TSoIPAlarmState_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmState_Object = MibTableColumn
pt3080TSoIPAlarmState = _Pt3080TSoIPAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 3),
    _Pt3080TSoIPAlarmState_Type()
)
pt3080TSoIPAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmState.setStatus("current")


class _Pt3080TSoIPAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080TSoIPAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080TSoIPAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmActionEventlog_Object = MibTableColumn
pt3080TSoIPAlarmActionEventlog = _Pt3080TSoIPAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 4),
    _Pt3080TSoIPAlarmActionEventlog_Type()
)
pt3080TSoIPAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmActionEventlog.setStatus("current")


class _Pt3080TSoIPAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080TSoIPAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080TSoIPAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmActionRelay1_Object = MibTableColumn
pt3080TSoIPAlarmActionRelay1 = _Pt3080TSoIPAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 5),
    _Pt3080TSoIPAlarmActionRelay1_Type()
)
pt3080TSoIPAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmActionRelay1.setStatus("current")


class _Pt3080TSoIPAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080TSoIPAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080TSoIPAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmActionRelay2_Object = MibTableColumn
pt3080TSoIPAlarmActionRelay2 = _Pt3080TSoIPAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 6),
    _Pt3080TSoIPAlarmActionRelay2_Type()
)
pt3080TSoIPAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmActionRelay2.setStatus("current")


class _Pt3080TSoIPAlarmActionTrap_Type(Integer32):
    """Custom type pt3080TSoIPAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080TSoIPAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmActionTrap_Object = MibTableColumn
pt3080TSoIPAlarmActionTrap = _Pt3080TSoIPAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 7),
    _Pt3080TSoIPAlarmActionTrap_Type()
)
pt3080TSoIPAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmActionTrap.setStatus("current")


class _Pt3080TSoIPAlarmActionEmail_Type(Integer32):
    """Custom type pt3080TSoIPAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080TSoIPAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmActionEmail_Object = MibTableColumn
pt3080TSoIPAlarmActionEmail = _Pt3080TSoIPAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 8),
    _Pt3080TSoIPAlarmActionEmail_Type()
)
pt3080TSoIPAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmActionEmail.setStatus("current")


class _Pt3080TSoIPAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080TSoIPAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080TSoIPAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmActionAlarmLED_Object = MibTableColumn
pt3080TSoIPAlarmActionAlarmLED = _Pt3080TSoIPAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 9),
    _Pt3080TSoIPAlarmActionAlarmLED_Type()
)
pt3080TSoIPAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmActionAlarmLED.setStatus("current")


class _Pt3080TSoIPAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080TSoIPAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080TSoIPAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080TSoIPAlarmActionForceMode_Object = MibTableColumn
pt3080TSoIPAlarmActionForceMode = _Pt3080TSoIPAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 12, 1, 10),
    _Pt3080TSoIPAlarmActionForceMode_Type()
)
pt3080TSoIPAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080TSoIPAlarmActionForceMode.setStatus("current")
_Pt3080ExternalAlarmTable_Object = MibTable
pt3080ExternalAlarmTable = _Pt3080ExternalAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13)
)
if mibBuilder.loadTexts:
    pt3080ExternalAlarmTable.setStatus("current")
_Pt3080ExternalAlarmEntry_Object = MibTableRow
pt3080ExternalAlarmEntry = _Pt3080ExternalAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1)
)
pt3080ExternalAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080ExternalAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080ExternalAlarmEntry.setStatus("current")


class _Pt3080ExternalAlarmID_Type(Integer32):
    """Custom type pt3080ExternalAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080ExternalAlarmID_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmID_Object = MibTableColumn
pt3080ExternalAlarmID = _Pt3080ExternalAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 1),
    _Pt3080ExternalAlarmID_Type()
)
pt3080ExternalAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmID.setStatus("current")
_Pt3080ExternalAlarmDescription_Type = DisplayString
_Pt3080ExternalAlarmDescription_Object = MibTableColumn
pt3080ExternalAlarmDescription = _Pt3080ExternalAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 2),
    _Pt3080ExternalAlarmDescription_Type()
)
pt3080ExternalAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmDescription.setStatus("current")


class _Pt3080ExternalAlarmState_Type(Integer32):
    """Custom type pt3080ExternalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080ExternalAlarmState_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmState_Object = MibTableColumn
pt3080ExternalAlarmState = _Pt3080ExternalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 3),
    _Pt3080ExternalAlarmState_Type()
)
pt3080ExternalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmState.setStatus("current")


class _Pt3080ExternalAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080ExternalAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ExternalAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmActionEventlog_Object = MibTableColumn
pt3080ExternalAlarmActionEventlog = _Pt3080ExternalAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 4),
    _Pt3080ExternalAlarmActionEventlog_Type()
)
pt3080ExternalAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmActionEventlog.setStatus("current")


class _Pt3080ExternalAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080ExternalAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ExternalAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmActionRelay1_Object = MibTableColumn
pt3080ExternalAlarmActionRelay1 = _Pt3080ExternalAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 5),
    _Pt3080ExternalAlarmActionRelay1_Type()
)
pt3080ExternalAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmActionRelay1.setStatus("current")


class _Pt3080ExternalAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080ExternalAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ExternalAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmActionRelay2_Object = MibTableColumn
pt3080ExternalAlarmActionRelay2 = _Pt3080ExternalAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 6),
    _Pt3080ExternalAlarmActionRelay2_Type()
)
pt3080ExternalAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmActionRelay2.setStatus("current")


class _Pt3080ExternalAlarmActionTrap_Type(Integer32):
    """Custom type pt3080ExternalAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ExternalAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmActionTrap_Object = MibTableColumn
pt3080ExternalAlarmActionTrap = _Pt3080ExternalAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 7),
    _Pt3080ExternalAlarmActionTrap_Type()
)
pt3080ExternalAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmActionTrap.setStatus("current")


class _Pt3080ExternalAlarmActionEmail_Type(Integer32):
    """Custom type pt3080ExternalAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ExternalAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmActionEmail_Object = MibTableColumn
pt3080ExternalAlarmActionEmail = _Pt3080ExternalAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 8),
    _Pt3080ExternalAlarmActionEmail_Type()
)
pt3080ExternalAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmActionEmail.setStatus("current")


class _Pt3080ExternalAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080ExternalAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ExternalAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmActionAlarmLED_Object = MibTableColumn
pt3080ExternalAlarmActionAlarmLED = _Pt3080ExternalAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 9),
    _Pt3080ExternalAlarmActionAlarmLED_Type()
)
pt3080ExternalAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmActionAlarmLED.setStatus("current")


class _Pt3080ExternalAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080ExternalAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080ExternalAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080ExternalAlarmActionForceMode_Object = MibTableColumn
pt3080ExternalAlarmActionForceMode = _Pt3080ExternalAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 13, 1, 10),
    _Pt3080ExternalAlarmActionForceMode_Type()
)
pt3080ExternalAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ExternalAlarmActionForceMode.setStatus("current")
_Pt3080HWMonitorAlarmTable_Object = MibTable
pt3080HWMonitorAlarmTable = _Pt3080HWMonitorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14)
)
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmTable.setStatus("current")
_Pt3080HWMonitorAlarmEntry_Object = MibTableRow
pt3080HWMonitorAlarmEntry = _Pt3080HWMonitorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1)
)
pt3080HWMonitorAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080HWMonitorAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmEntry.setStatus("current")


class _Pt3080HWMonitorAlarmID_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080HWMonitorAlarmID_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmID_Object = MibTableColumn
pt3080HWMonitorAlarmID = _Pt3080HWMonitorAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 1),
    _Pt3080HWMonitorAlarmID_Type()
)
pt3080HWMonitorAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmID.setStatus("current")
_Pt3080HWMonitorAlarmDescription_Type = DisplayString
_Pt3080HWMonitorAlarmDescription_Object = MibTableColumn
pt3080HWMonitorAlarmDescription = _Pt3080HWMonitorAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 2),
    _Pt3080HWMonitorAlarmDescription_Type()
)
pt3080HWMonitorAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmDescription.setStatus("current")


class _Pt3080HWMonitorAlarmState_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080HWMonitorAlarmState_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmState_Object = MibTableColumn
pt3080HWMonitorAlarmState = _Pt3080HWMonitorAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 3),
    _Pt3080HWMonitorAlarmState_Type()
)
pt3080HWMonitorAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmState.setStatus("current")


class _Pt3080HWMonitorAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080HWMonitorAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmActionEventlog_Object = MibTableColumn
pt3080HWMonitorAlarmActionEventlog = _Pt3080HWMonitorAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 4),
    _Pt3080HWMonitorAlarmActionEventlog_Type()
)
pt3080HWMonitorAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmActionEventlog.setStatus("current")


class _Pt3080HWMonitorAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080HWMonitorAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmActionRelay1_Object = MibTableColumn
pt3080HWMonitorAlarmActionRelay1 = _Pt3080HWMonitorAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 5),
    _Pt3080HWMonitorAlarmActionRelay1_Type()
)
pt3080HWMonitorAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmActionRelay1.setStatus("current")


class _Pt3080HWMonitorAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080HWMonitorAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmActionRelay2_Object = MibTableColumn
pt3080HWMonitorAlarmActionRelay2 = _Pt3080HWMonitorAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 6),
    _Pt3080HWMonitorAlarmActionRelay2_Type()
)
pt3080HWMonitorAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmActionRelay2.setStatus("current")


class _Pt3080HWMonitorAlarmActionTrap_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080HWMonitorAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmActionTrap_Object = MibTableColumn
pt3080HWMonitorAlarmActionTrap = _Pt3080HWMonitorAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 7),
    _Pt3080HWMonitorAlarmActionTrap_Type()
)
pt3080HWMonitorAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmActionTrap.setStatus("current")


class _Pt3080HWMonitorAlarmActionEmail_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080HWMonitorAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmActionEmail_Object = MibTableColumn
pt3080HWMonitorAlarmActionEmail = _Pt3080HWMonitorAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 8),
    _Pt3080HWMonitorAlarmActionEmail_Type()
)
pt3080HWMonitorAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmActionEmail.setStatus("current")


class _Pt3080HWMonitorAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080HWMonitorAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmActionAlarmLED_Object = MibTableColumn
pt3080HWMonitorAlarmActionAlarmLED = _Pt3080HWMonitorAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 9),
    _Pt3080HWMonitorAlarmActionAlarmLED_Type()
)
pt3080HWMonitorAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmActionAlarmLED.setStatus("current")


class _Pt3080HWMonitorAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080HWMonitorAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080HWMonitorAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080HWMonitorAlarmActionForceMode_Object = MibTableColumn
pt3080HWMonitorAlarmActionForceMode = _Pt3080HWMonitorAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 14, 1, 10),
    _Pt3080HWMonitorAlarmActionForceMode_Type()
)
pt3080HWMonitorAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080HWMonitorAlarmActionForceMode.setStatus("current")
_Pt3080CommsAlarmTable_Object = MibTable
pt3080CommsAlarmTable = _Pt3080CommsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15)
)
if mibBuilder.loadTexts:
    pt3080CommsAlarmTable.setStatus("current")
_Pt3080CommsAlarmEntry_Object = MibTableRow
pt3080CommsAlarmEntry = _Pt3080CommsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1)
)
pt3080CommsAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080CommsAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080CommsAlarmEntry.setStatus("current")


class _Pt3080CommsAlarmID_Type(Integer32):
    """Custom type pt3080CommsAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080CommsAlarmID_Type.__name__ = "Integer32"
_Pt3080CommsAlarmID_Object = MibTableColumn
pt3080CommsAlarmID = _Pt3080CommsAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 1),
    _Pt3080CommsAlarmID_Type()
)
pt3080CommsAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080CommsAlarmID.setStatus("current")
_Pt3080CommsAlarmDescription_Type = DisplayString
_Pt3080CommsAlarmDescription_Object = MibTableColumn
pt3080CommsAlarmDescription = _Pt3080CommsAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 2),
    _Pt3080CommsAlarmDescription_Type()
)
pt3080CommsAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsAlarmDescription.setStatus("current")


class _Pt3080CommsAlarmState_Type(Integer32):
    """Custom type pt3080CommsAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080CommsAlarmState_Type.__name__ = "Integer32"
_Pt3080CommsAlarmState_Object = MibTableColumn
pt3080CommsAlarmState = _Pt3080CommsAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 3),
    _Pt3080CommsAlarmState_Type()
)
pt3080CommsAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsAlarmState.setStatus("current")


class _Pt3080CommsAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080CommsAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080CommsAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080CommsAlarmActionEventlog_Object = MibTableColumn
pt3080CommsAlarmActionEventlog = _Pt3080CommsAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 4),
    _Pt3080CommsAlarmActionEventlog_Type()
)
pt3080CommsAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmActionEventlog.setStatus("current")


class _Pt3080CommsAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080CommsAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080CommsAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080CommsAlarmActionRelay1_Object = MibTableColumn
pt3080CommsAlarmActionRelay1 = _Pt3080CommsAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 5),
    _Pt3080CommsAlarmActionRelay1_Type()
)
pt3080CommsAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmActionRelay1.setStatus("current")


class _Pt3080CommsAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080CommsAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080CommsAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080CommsAlarmActionRelay2_Object = MibTableColumn
pt3080CommsAlarmActionRelay2 = _Pt3080CommsAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 6),
    _Pt3080CommsAlarmActionRelay2_Type()
)
pt3080CommsAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmActionRelay2.setStatus("current")


class _Pt3080CommsAlarmActionTrap_Type(Integer32):
    """Custom type pt3080CommsAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080CommsAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080CommsAlarmActionTrap_Object = MibTableColumn
pt3080CommsAlarmActionTrap = _Pt3080CommsAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 7),
    _Pt3080CommsAlarmActionTrap_Type()
)
pt3080CommsAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmActionTrap.setStatus("current")


class _Pt3080CommsAlarmActionEmail_Type(Integer32):
    """Custom type pt3080CommsAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080CommsAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080CommsAlarmActionEmail_Object = MibTableColumn
pt3080CommsAlarmActionEmail = _Pt3080CommsAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 8),
    _Pt3080CommsAlarmActionEmail_Type()
)
pt3080CommsAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmActionEmail.setStatus("current")


class _Pt3080CommsAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080CommsAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080CommsAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080CommsAlarmActionAlarmLED_Object = MibTableColumn
pt3080CommsAlarmActionAlarmLED = _Pt3080CommsAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 9),
    _Pt3080CommsAlarmActionAlarmLED_Type()
)
pt3080CommsAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmActionAlarmLED.setStatus("current")


class _Pt3080CommsAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080CommsAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080CommsAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080CommsAlarmActionForceMode_Object = MibTableColumn
pt3080CommsAlarmActionForceMode = _Pt3080CommsAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 15, 1, 10),
    _Pt3080CommsAlarmActionForceMode_Type()
)
pt3080CommsAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmActionForceMode.setStatus("current")
_Pt3080ASIAlarmTable_Object = MibTable
pt3080ASIAlarmTable = _Pt3080ASIAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16)
)
if mibBuilder.loadTexts:
    pt3080ASIAlarmTable.setStatus("current")
_Pt3080ASIAlarmEntry_Object = MibTableRow
pt3080ASIAlarmEntry = _Pt3080ASIAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1)
)
pt3080ASIAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080ASIAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080ASIAlarmEntry.setStatus("current")


class _Pt3080ASIAlarmID_Type(Integer32):
    """Custom type pt3080ASIAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080ASIAlarmID_Type.__name__ = "Integer32"
_Pt3080ASIAlarmID_Object = MibTableColumn
pt3080ASIAlarmID = _Pt3080ASIAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 1),
    _Pt3080ASIAlarmID_Type()
)
pt3080ASIAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080ASIAlarmID.setStatus("current")
_Pt3080ASIAlarmDescription_Type = DisplayString
_Pt3080ASIAlarmDescription_Object = MibTableColumn
pt3080ASIAlarmDescription = _Pt3080ASIAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 2),
    _Pt3080ASIAlarmDescription_Type()
)
pt3080ASIAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIAlarmDescription.setStatus("current")


class _Pt3080ASIAlarmState_Type(Integer32):
    """Custom type pt3080ASIAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080ASIAlarmState_Type.__name__ = "Integer32"
_Pt3080ASIAlarmState_Object = MibTableColumn
pt3080ASIAlarmState = _Pt3080ASIAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 3),
    _Pt3080ASIAlarmState_Type()
)
pt3080ASIAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIAlarmState.setStatus("current")


class _Pt3080ASIAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080ASIAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASIAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080ASIAlarmActionEventlog_Object = MibTableColumn
pt3080ASIAlarmActionEventlog = _Pt3080ASIAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 4),
    _Pt3080ASIAlarmActionEventlog_Type()
)
pt3080ASIAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIAlarmActionEventlog.setStatus("current")


class _Pt3080ASIAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080ASIAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASIAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080ASIAlarmActionRelay1_Object = MibTableColumn
pt3080ASIAlarmActionRelay1 = _Pt3080ASIAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 5),
    _Pt3080ASIAlarmActionRelay1_Type()
)
pt3080ASIAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIAlarmActionRelay1.setStatus("current")


class _Pt3080ASIAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080ASIAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASIAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080ASIAlarmActionRelay2_Object = MibTableColumn
pt3080ASIAlarmActionRelay2 = _Pt3080ASIAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 6),
    _Pt3080ASIAlarmActionRelay2_Type()
)
pt3080ASIAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIAlarmActionRelay2.setStatus("current")


class _Pt3080ASIAlarmActionTrap_Type(Integer32):
    """Custom type pt3080ASIAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASIAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080ASIAlarmActionTrap_Object = MibTableColumn
pt3080ASIAlarmActionTrap = _Pt3080ASIAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 7),
    _Pt3080ASIAlarmActionTrap_Type()
)
pt3080ASIAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIAlarmActionTrap.setStatus("current")


class _Pt3080ASIAlarmActionEmail_Type(Integer32):
    """Custom type pt3080ASIAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASIAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080ASIAlarmActionEmail_Object = MibTableColumn
pt3080ASIAlarmActionEmail = _Pt3080ASIAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 8),
    _Pt3080ASIAlarmActionEmail_Type()
)
pt3080ASIAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIAlarmActionEmail.setStatus("current")


class _Pt3080ASIAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080ASIAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080ASIAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080ASIAlarmActionAlarmLED_Object = MibTableColumn
pt3080ASIAlarmActionAlarmLED = _Pt3080ASIAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 9),
    _Pt3080ASIAlarmActionAlarmLED_Type()
)
pt3080ASIAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIAlarmActionAlarmLED.setStatus("current")


class _Pt3080ASIAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080ASIAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080ASIAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080ASIAlarmActionForceMode_Object = MibTableColumn
pt3080ASIAlarmActionForceMode = _Pt3080ASIAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 16, 1, 10),
    _Pt3080ASIAlarmActionForceMode_Type()
)
pt3080ASIAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIAlarmActionForceMode.setStatus("current")
_Pt3080DemodulatorAlarmTable_Object = MibTable
pt3080DemodulatorAlarmTable = _Pt3080DemodulatorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17)
)
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmTable.setStatus("current")
_Pt3080DemodulatorAlarmEntry_Object = MibTableRow
pt3080DemodulatorAlarmEntry = _Pt3080DemodulatorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1)
)
pt3080DemodulatorAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080DemodulatorAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmEntry.setStatus("current")


class _Pt3080DemodulatorAlarmID_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080DemodulatorAlarmID_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmID_Object = MibTableColumn
pt3080DemodulatorAlarmID = _Pt3080DemodulatorAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 1),
    _Pt3080DemodulatorAlarmID_Type()
)
pt3080DemodulatorAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmID.setStatus("current")
_Pt3080DemodulatorAlarmDescription_Type = DisplayString
_Pt3080DemodulatorAlarmDescription_Object = MibTableColumn
pt3080DemodulatorAlarmDescription = _Pt3080DemodulatorAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 2),
    _Pt3080DemodulatorAlarmDescription_Type()
)
pt3080DemodulatorAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmDescription.setStatus("current")


class _Pt3080DemodulatorAlarmState_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080DemodulatorAlarmState_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmState_Object = MibTableColumn
pt3080DemodulatorAlarmState = _Pt3080DemodulatorAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 3),
    _Pt3080DemodulatorAlarmState_Type()
)
pt3080DemodulatorAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmState.setStatus("current")


class _Pt3080DemodulatorAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080DemodulatorAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmActionEventlog_Object = MibTableColumn
pt3080DemodulatorAlarmActionEventlog = _Pt3080DemodulatorAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 4),
    _Pt3080DemodulatorAlarmActionEventlog_Type()
)
pt3080DemodulatorAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmActionEventlog.setStatus("current")


class _Pt3080DemodulatorAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080DemodulatorAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmActionRelay1_Object = MibTableColumn
pt3080DemodulatorAlarmActionRelay1 = _Pt3080DemodulatorAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 5),
    _Pt3080DemodulatorAlarmActionRelay1_Type()
)
pt3080DemodulatorAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmActionRelay1.setStatus("current")


class _Pt3080DemodulatorAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080DemodulatorAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmActionRelay2_Object = MibTableColumn
pt3080DemodulatorAlarmActionRelay2 = _Pt3080DemodulatorAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 6),
    _Pt3080DemodulatorAlarmActionRelay2_Type()
)
pt3080DemodulatorAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmActionRelay2.setStatus("current")


class _Pt3080DemodulatorAlarmActionTrap_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080DemodulatorAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmActionTrap_Object = MibTableColumn
pt3080DemodulatorAlarmActionTrap = _Pt3080DemodulatorAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 7),
    _Pt3080DemodulatorAlarmActionTrap_Type()
)
pt3080DemodulatorAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmActionTrap.setStatus("current")


class _Pt3080DemodulatorAlarmActionEmail_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080DemodulatorAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmActionEmail_Object = MibTableColumn
pt3080DemodulatorAlarmActionEmail = _Pt3080DemodulatorAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 8),
    _Pt3080DemodulatorAlarmActionEmail_Type()
)
pt3080DemodulatorAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmActionEmail.setStatus("current")


class _Pt3080DemodulatorAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080DemodulatorAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmActionAlarmLED_Object = MibTableColumn
pt3080DemodulatorAlarmActionAlarmLED = _Pt3080DemodulatorAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 9),
    _Pt3080DemodulatorAlarmActionAlarmLED_Type()
)
pt3080DemodulatorAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmActionAlarmLED.setStatus("current")


class _Pt3080DemodulatorAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080DemodulatorAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080DemodulatorAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080DemodulatorAlarmActionForceMode_Object = MibTableColumn
pt3080DemodulatorAlarmActionForceMode = _Pt3080DemodulatorAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 17, 1, 10),
    _Pt3080DemodulatorAlarmActionForceMode_Type()
)
pt3080DemodulatorAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorAlarmActionForceMode.setStatus("current")
_Pt3080InternalAlarmTable_Object = MibTable
pt3080InternalAlarmTable = _Pt3080InternalAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18)
)
if mibBuilder.loadTexts:
    pt3080InternalAlarmTable.setStatus("current")
_Pt3080InternalAlarmEntry_Object = MibTableRow
pt3080InternalAlarmEntry = _Pt3080InternalAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1)
)
pt3080InternalAlarmEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080InternalAlarmID"),
)
if mibBuilder.loadTexts:
    pt3080InternalAlarmEntry.setStatus("current")


class _Pt3080InternalAlarmID_Type(Integer32):
    """Custom type pt3080InternalAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pt3080InternalAlarmID_Type.__name__ = "Integer32"
_Pt3080InternalAlarmID_Object = MibTableColumn
pt3080InternalAlarmID = _Pt3080InternalAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 1),
    _Pt3080InternalAlarmID_Type()
)
pt3080InternalAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080InternalAlarmID.setStatus("current")
_Pt3080InternalAlarmDescription_Type = DisplayString
_Pt3080InternalAlarmDescription_Object = MibTableColumn
pt3080InternalAlarmDescription = _Pt3080InternalAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 2),
    _Pt3080InternalAlarmDescription_Type()
)
pt3080InternalAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InternalAlarmDescription.setStatus("current")


class _Pt3080InternalAlarmState_Type(Integer32):
    """Custom type pt3080InternalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080InternalAlarmState_Type.__name__ = "Integer32"
_Pt3080InternalAlarmState_Object = MibTableColumn
pt3080InternalAlarmState = _Pt3080InternalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 3),
    _Pt3080InternalAlarmState_Type()
)
pt3080InternalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080InternalAlarmState.setStatus("current")


class _Pt3080InternalAlarmActionEventlog_Type(Integer32):
    """Custom type pt3080InternalAlarmActionEventlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080InternalAlarmActionEventlog_Type.__name__ = "Integer32"
_Pt3080InternalAlarmActionEventlog_Object = MibTableColumn
pt3080InternalAlarmActionEventlog = _Pt3080InternalAlarmActionEventlog_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 4),
    _Pt3080InternalAlarmActionEventlog_Type()
)
pt3080InternalAlarmActionEventlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InternalAlarmActionEventlog.setStatus("current")


class _Pt3080InternalAlarmActionRelay1_Type(Integer32):
    """Custom type pt3080InternalAlarmActionRelay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080InternalAlarmActionRelay1_Type.__name__ = "Integer32"
_Pt3080InternalAlarmActionRelay1_Object = MibTableColumn
pt3080InternalAlarmActionRelay1 = _Pt3080InternalAlarmActionRelay1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 5),
    _Pt3080InternalAlarmActionRelay1_Type()
)
pt3080InternalAlarmActionRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InternalAlarmActionRelay1.setStatus("current")


class _Pt3080InternalAlarmActionRelay2_Type(Integer32):
    """Custom type pt3080InternalAlarmActionRelay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080InternalAlarmActionRelay2_Type.__name__ = "Integer32"
_Pt3080InternalAlarmActionRelay2_Object = MibTableColumn
pt3080InternalAlarmActionRelay2 = _Pt3080InternalAlarmActionRelay2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 6),
    _Pt3080InternalAlarmActionRelay2_Type()
)
pt3080InternalAlarmActionRelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InternalAlarmActionRelay2.setStatus("current")


class _Pt3080InternalAlarmActionTrap_Type(Integer32):
    """Custom type pt3080InternalAlarmActionTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080InternalAlarmActionTrap_Type.__name__ = "Integer32"
_Pt3080InternalAlarmActionTrap_Object = MibTableColumn
pt3080InternalAlarmActionTrap = _Pt3080InternalAlarmActionTrap_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 7),
    _Pt3080InternalAlarmActionTrap_Type()
)
pt3080InternalAlarmActionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InternalAlarmActionTrap.setStatus("current")


class _Pt3080InternalAlarmActionEmail_Type(Integer32):
    """Custom type pt3080InternalAlarmActionEmail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080InternalAlarmActionEmail_Type.__name__ = "Integer32"
_Pt3080InternalAlarmActionEmail_Object = MibTableColumn
pt3080InternalAlarmActionEmail = _Pt3080InternalAlarmActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 8),
    _Pt3080InternalAlarmActionEmail_Type()
)
pt3080InternalAlarmActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InternalAlarmActionEmail.setStatus("current")


class _Pt3080InternalAlarmActionAlarmLED_Type(Integer32):
    """Custom type pt3080InternalAlarmActionAlarmLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pt3080InternalAlarmActionAlarmLED_Type.__name__ = "Integer32"
_Pt3080InternalAlarmActionAlarmLED_Object = MibTableColumn
pt3080InternalAlarmActionAlarmLED = _Pt3080InternalAlarmActionAlarmLED_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 9),
    _Pt3080InternalAlarmActionAlarmLED_Type()
)
pt3080InternalAlarmActionAlarmLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InternalAlarmActionAlarmLED.setStatus("current")


class _Pt3080InternalAlarmActionForceMode_Type(Integer32):
    """Custom type pt3080InternalAlarmActionForceMode based on Integer32"""
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
          ("mute", 1),
          ("reboot", 2))
    )


_Pt3080InternalAlarmActionForceMode_Type.__name__ = "Integer32"
_Pt3080InternalAlarmActionForceMode_Object = MibTableColumn
pt3080InternalAlarmActionForceMode = _Pt3080InternalAlarmActionForceMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 14, 18, 1, 10),
    _Pt3080InternalAlarmActionForceMode_Type()
)
pt3080InternalAlarmActionForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080InternalAlarmActionForceMode.setStatus("current")
_Pt3080Preset_ObjectIdentity = ObjectIdentity
pt3080Preset = _Pt3080Preset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 15)
)
_Pt3080PresetTable_Object = MibTable
pt3080PresetTable = _Pt3080PresetTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 15, 1)
)
if mibBuilder.loadTexts:
    pt3080PresetTable.setStatus("current")
_Pt3080PresetEntry_Object = MibTableRow
pt3080PresetEntry = _Pt3080PresetEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 15, 1, 1)
)
pt3080PresetEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080PresetNo"),
)
if mibBuilder.loadTexts:
    pt3080PresetEntry.setStatus("current")


class _Pt3080PresetNo_Type(Integer32):
    """Custom type pt3080PresetNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Pt3080PresetNo_Type.__name__ = "Integer32"
_Pt3080PresetNo_Object = MibTableColumn
pt3080PresetNo = _Pt3080PresetNo_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 15, 1, 1, 1),
    _Pt3080PresetNo_Type()
)
pt3080PresetNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080PresetNo.setStatus("current")
_Pt3080PresetName_Type = DisplayString
_Pt3080PresetName_Object = MibTableColumn
pt3080PresetName = _Pt3080PresetName_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 15, 1, 1, 2),
    _Pt3080PresetName_Type()
)
pt3080PresetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PresetName.setStatus("current")


class _Pt3080PresetRecall_Type(Integer32):
    """Custom type pt3080PresetRecall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Pt3080PresetRecall_Type.__name__ = "Integer32"
_Pt3080PresetRecall_Object = MibScalar
pt3080PresetRecall = _Pt3080PresetRecall_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 15, 2),
    _Pt3080PresetRecall_Type()
)
pt3080PresetRecall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PresetRecall.setStatus("current")


class _Pt3080PresetStore_Type(Integer32):
    """Custom type pt3080PresetStore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Pt3080PresetStore_Type.__name__ = "Integer32"
_Pt3080PresetStore_Object = MibScalar
pt3080PresetStore = _Pt3080PresetStore_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 15, 3),
    _Pt3080PresetStore_Type()
)
pt3080PresetStore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PresetStore.setStatus("current")
_Pt3080Eventlog_ObjectIdentity = ObjectIdentity
pt3080Eventlog = _Pt3080Eventlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16)
)
_Pt3080EventlogTable_Object = MibTable
pt3080EventlogTable = _Pt3080EventlogTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 1)
)
if mibBuilder.loadTexts:
    pt3080EventlogTable.setStatus("current")
_Pt3080EventlogEntry_Object = MibTableRow
pt3080EventlogEntry = _Pt3080EventlogEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 1, 1)
)
pt3080EventlogEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080EventlogNo"),
)
if mibBuilder.loadTexts:
    pt3080EventlogEntry.setStatus("current")


class _Pt3080EventlogNo_Type(Integer32):
    """Custom type pt3080EventlogNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_Pt3080EventlogNo_Type.__name__ = "Integer32"
_Pt3080EventlogNo_Object = MibTableColumn
pt3080EventlogNo = _Pt3080EventlogNo_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 1, 1, 1),
    _Pt3080EventlogNo_Type()
)
pt3080EventlogNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080EventlogNo.setStatus("current")
_Pt3080EventlogID_Type = Integer32
_Pt3080EventlogID_Object = MibTableColumn
pt3080EventlogID = _Pt3080EventlogID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 1, 1, 2),
    _Pt3080EventlogID_Type()
)
pt3080EventlogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080EventlogID.setStatus("current")
_Pt3080EventlogTimestamp_Type = DateAndTime
_Pt3080EventlogTimestamp_Object = MibTableColumn
pt3080EventlogTimestamp = _Pt3080EventlogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 1, 1, 3),
    _Pt3080EventlogTimestamp_Type()
)
pt3080EventlogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080EventlogTimestamp.setStatus("current")
_Pt3080EventlogText_Type = DisplayString
_Pt3080EventlogText_Object = MibTableColumn
pt3080EventlogText = _Pt3080EventlogText_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 1, 1, 4),
    _Pt3080EventlogText_Type()
)
pt3080EventlogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080EventlogText.setStatus("current")


class _Pt3080EventlogClear_Type(Integer32):
    """Custom type pt3080EventlogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("clear", 1))
    )


_Pt3080EventlogClear_Type.__name__ = "Integer32"
_Pt3080EventlogClear_Object = MibScalar
pt3080EventlogClear = _Pt3080EventlogClear_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 2),
    _Pt3080EventlogClear_Type()
)
pt3080EventlogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080EventlogClear.setStatus("current")


class _Pt3080EventlogEnable_Type(Integer32):
    """Custom type pt3080EventlogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080EventlogEnable_Type.__name__ = "Integer32"
_Pt3080EventlogEnable_Object = MibScalar
pt3080EventlogEnable = _Pt3080EventlogEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 3),
    _Pt3080EventlogEnable_Type()
)
pt3080EventlogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080EventlogEnable.setStatus("current")


class _Pt3080EventlogMode_Type(Integer32):
    """Custom type pt3080EventlogMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fifo", 0),
          ("full", 1))
    )


_Pt3080EventlogMode_Type.__name__ = "Integer32"
_Pt3080EventlogMode_Object = MibScalar
pt3080EventlogMode = _Pt3080EventlogMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 16, 4),
    _Pt3080EventlogMode_Type()
)
pt3080EventlogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080EventlogMode.setStatus("current")
_Pt3080Comms_ObjectIdentity = ObjectIdentity
pt3080Comms = _Pt3080Comms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17)
)
_Pt3080CommsLocalStaticIpAddr_Type = IpAddress
_Pt3080CommsLocalStaticIpAddr_Object = MibScalar
pt3080CommsLocalStaticIpAddr = _Pt3080CommsLocalStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 1),
    _Pt3080CommsLocalStaticIpAddr_Type()
)
pt3080CommsLocalStaticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalStaticIpAddr.setStatus("current")
_Pt3080CommsLocalStaticNetmask_Type = IpAddress
_Pt3080CommsLocalStaticNetmask_Object = MibScalar
pt3080CommsLocalStaticNetmask = _Pt3080CommsLocalStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2),
    _Pt3080CommsLocalStaticNetmask_Type()
)
pt3080CommsLocalStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalStaticNetmask.setStatus("current")


class _Pt3080CommsLocalDhcpMode_Type(Integer32):
    """Custom type pt3080CommsLocalDhcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("client", 1))
    )


_Pt3080CommsLocalDhcpMode_Type.__name__ = "Integer32"
_Pt3080CommsLocalDhcpMode_Object = MibScalar
pt3080CommsLocalDhcpMode = _Pt3080CommsLocalDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 3),
    _Pt3080CommsLocalDhcpMode_Type()
)
pt3080CommsLocalDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalDhcpMode.setStatus("current")
_Pt3080CommsLocalCurrentIpAddr_Type = IpAddress
_Pt3080CommsLocalCurrentIpAddr_Object = MibScalar
pt3080CommsLocalCurrentIpAddr = _Pt3080CommsLocalCurrentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 4),
    _Pt3080CommsLocalCurrentIpAddr_Type()
)
pt3080CommsLocalCurrentIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsLocalCurrentIpAddr.setStatus("current")
_Pt3080CommsLocalCurrentNetmask_Type = IpAddress
_Pt3080CommsLocalCurrentNetmask_Object = MibScalar
pt3080CommsLocalCurrentNetmask = _Pt3080CommsLocalCurrentNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 5),
    _Pt3080CommsLocalCurrentNetmask_Type()
)
pt3080CommsLocalCurrentNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsLocalCurrentNetmask.setStatus("current")
_Pt3080CommsRemoteStaticIpAddr_Type = IpAddress
_Pt3080CommsRemoteStaticIpAddr_Object = MibScalar
pt3080CommsRemoteStaticIpAddr = _Pt3080CommsRemoteStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 7),
    _Pt3080CommsRemoteStaticIpAddr_Type()
)
pt3080CommsRemoteStaticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteStaticIpAddr.setStatus("current")
_Pt3080CommsRemoteStaticNetmask_Type = IpAddress
_Pt3080CommsRemoteStaticNetmask_Object = MibScalar
pt3080CommsRemoteStaticNetmask = _Pt3080CommsRemoteStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 8),
    _Pt3080CommsRemoteStaticNetmask_Type()
)
pt3080CommsRemoteStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteStaticNetmask.setStatus("current")
_Pt3080CommsRemoteCurrentIpAddr_Type = IpAddress
_Pt3080CommsRemoteCurrentIpAddr_Object = MibScalar
pt3080CommsRemoteCurrentIpAddr = _Pt3080CommsRemoteCurrentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 10),
    _Pt3080CommsRemoteCurrentIpAddr_Type()
)
pt3080CommsRemoteCurrentIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsRemoteCurrentIpAddr.setStatus("current")
_Pt3080CommsRemoteCurrentNetmask_Type = IpAddress
_Pt3080CommsRemoteCurrentNetmask_Object = MibScalar
pt3080CommsRemoteCurrentNetmask = _Pt3080CommsRemoteCurrentNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 11),
    _Pt3080CommsRemoteCurrentNetmask_Type()
)
pt3080CommsRemoteCurrentNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsRemoteCurrentNetmask.setStatus("current")
_Pt3080CommsGbeAdminStaticIpAddr_Type = IpAddress
_Pt3080CommsGbeAdminStaticIpAddr_Object = MibScalar
pt3080CommsGbeAdminStaticIpAddr = _Pt3080CommsGbeAdminStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 13),
    _Pt3080CommsGbeAdminStaticIpAddr_Type()
)
pt3080CommsGbeAdminStaticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminStaticIpAddr.setStatus("current")
_Pt3080CommsGbeAdminStaticNetmask_Type = IpAddress
_Pt3080CommsGbeAdminStaticNetmask_Object = MibScalar
pt3080CommsGbeAdminStaticNetmask = _Pt3080CommsGbeAdminStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 14),
    _Pt3080CommsGbeAdminStaticNetmask_Type()
)
pt3080CommsGbeAdminStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminStaticNetmask.setStatus("current")
_Pt3080CommsGbeAdminCurrentIpAddr_Type = IpAddress
_Pt3080CommsGbeAdminCurrentIpAddr_Object = MibScalar
pt3080CommsGbeAdminCurrentIpAddr = _Pt3080CommsGbeAdminCurrentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 16),
    _Pt3080CommsGbeAdminCurrentIpAddr_Type()
)
pt3080CommsGbeAdminCurrentIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminCurrentIpAddr.setStatus("current")
_Pt3080CommsGbeAdminCurrentNetmask_Type = IpAddress
_Pt3080CommsGbeAdminCurrentNetmask_Object = MibScalar
pt3080CommsGbeAdminCurrentNetmask = _Pt3080CommsGbeAdminCurrentNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 17),
    _Pt3080CommsGbeAdminCurrentNetmask_Type()
)
pt3080CommsGbeAdminCurrentNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminCurrentNetmask.setStatus("current")
_Pt3080CommsStaticDNS1ServerAddress_Type = IpAddress
_Pt3080CommsStaticDNS1ServerAddress_Object = MibScalar
pt3080CommsStaticDNS1ServerAddress = _Pt3080CommsStaticDNS1ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 19),
    _Pt3080CommsStaticDNS1ServerAddress_Type()
)
pt3080CommsStaticDNS1ServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticDNS1ServerAddress.setStatus("current")
_Pt3080CommsCurrentDNS1ServerAddress_Type = IpAddress
_Pt3080CommsCurrentDNS1ServerAddress_Object = MibScalar
pt3080CommsCurrentDNS1ServerAddress = _Pt3080CommsCurrentDNS1ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 20),
    _Pt3080CommsCurrentDNS1ServerAddress_Type()
)
pt3080CommsCurrentDNS1ServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsCurrentDNS1ServerAddress.setStatus("current")
_Pt3080CommsStaticDNS2ServerAddress_Type = IpAddress
_Pt3080CommsStaticDNS2ServerAddress_Object = MibScalar
pt3080CommsStaticDNS2ServerAddress = _Pt3080CommsStaticDNS2ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 21),
    _Pt3080CommsStaticDNS2ServerAddress_Type()
)
pt3080CommsStaticDNS2ServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticDNS2ServerAddress.setStatus("current")
_Pt3080CommsCurrentDNS2ServerAddress_Type = IpAddress
_Pt3080CommsCurrentDNS2ServerAddress_Object = MibScalar
pt3080CommsCurrentDNS2ServerAddress = _Pt3080CommsCurrentDNS2ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 22),
    _Pt3080CommsCurrentDNS2ServerAddress_Type()
)
pt3080CommsCurrentDNS2ServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsCurrentDNS2ServerAddress.setStatus("current")
_Pt3080CommsStaticDNS3ServerAddress_Type = IpAddress
_Pt3080CommsStaticDNS3ServerAddress_Object = MibScalar
pt3080CommsStaticDNS3ServerAddress = _Pt3080CommsStaticDNS3ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 23),
    _Pt3080CommsStaticDNS3ServerAddress_Type()
)
pt3080CommsStaticDNS3ServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticDNS3ServerAddress.setStatus("current")
_Pt3080CommsCurrentDNS3ServerAddress_Type = IpAddress
_Pt3080CommsCurrentDNS3ServerAddress_Object = MibScalar
pt3080CommsCurrentDNS3ServerAddress = _Pt3080CommsCurrentDNS3ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 24),
    _Pt3080CommsCurrentDNS3ServerAddress_Type()
)
pt3080CommsCurrentDNS3ServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsCurrentDNS3ServerAddress.setStatus("current")
_Pt3080CommsStaticDNSDomain_Type = DisplayString
_Pt3080CommsStaticDNSDomain_Object = MibScalar
pt3080CommsStaticDNSDomain = _Pt3080CommsStaticDNSDomain_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 25),
    _Pt3080CommsStaticDNSDomain_Type()
)
pt3080CommsStaticDNSDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticDNSDomain.setStatus("current")
_Pt3080CommsCurrentDNSDomain_Type = DisplayString
_Pt3080CommsCurrentDNSDomain_Object = MibScalar
pt3080CommsCurrentDNSDomain = _Pt3080CommsCurrentDNSDomain_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 26),
    _Pt3080CommsCurrentDNSDomain_Type()
)
pt3080CommsCurrentDNSDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsCurrentDNSDomain.setStatus("current")
_Pt3080CommsStaticHostname_Type = DisplayString
_Pt3080CommsStaticHostname_Object = MibScalar
pt3080CommsStaticHostname = _Pt3080CommsStaticHostname_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 27),
    _Pt3080CommsStaticHostname_Type()
)
pt3080CommsStaticHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticHostname.setStatus("current")
_Pt3080CommsCurrentHostname_Type = DisplayString
_Pt3080CommsCurrentHostname_Object = MibScalar
pt3080CommsCurrentHostname = _Pt3080CommsCurrentHostname_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 28),
    _Pt3080CommsCurrentHostname_Type()
)
pt3080CommsCurrentHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsCurrentHostname.setStatus("current")
_Pt3080CommsStaticGateway_Type = IpAddress
_Pt3080CommsStaticGateway_Object = MibScalar
pt3080CommsStaticGateway = _Pt3080CommsStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 29),
    _Pt3080CommsStaticGateway_Type()
)
pt3080CommsStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticGateway.setStatus("current")
_Pt3080CommsCurrentGateway_Type = IpAddress
_Pt3080CommsCurrentGateway_Object = MibScalar
pt3080CommsCurrentGateway = _Pt3080CommsCurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 30),
    _Pt3080CommsCurrentGateway_Type()
)
pt3080CommsCurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsCurrentGateway.setStatus("current")
_Pt3080CommsStaticNtpServerAddress_Type = DisplayString
_Pt3080CommsStaticNtpServerAddress_Object = MibScalar
pt3080CommsStaticNtpServerAddress = _Pt3080CommsStaticNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 31),
    _Pt3080CommsStaticNtpServerAddress_Type()
)
pt3080CommsStaticNtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticNtpServerAddress.setStatus("current")
_Pt3080CommsCurrentNtpServerAddress_Type = DisplayString
_Pt3080CommsCurrentNtpServerAddress_Object = MibScalar
pt3080CommsCurrentNtpServerAddress = _Pt3080CommsCurrentNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 32),
    _Pt3080CommsCurrentNtpServerAddress_Type()
)
pt3080CommsCurrentNtpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsCurrentNtpServerAddress.setStatus("current")
_Pt3080CommsEmailServerAddress_Type = DisplayString
_Pt3080CommsEmailServerAddress_Object = MibScalar
pt3080CommsEmailServerAddress = _Pt3080CommsEmailServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 33),
    _Pt3080CommsEmailServerAddress_Type()
)
pt3080CommsEmailServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsEmailServerAddress.setStatus("current")
_Pt3080CommsAlarmEmailReceiver_Type = DisplayString
_Pt3080CommsAlarmEmailReceiver_Object = MibScalar
pt3080CommsAlarmEmailReceiver = _Pt3080CommsAlarmEmailReceiver_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 34),
    _Pt3080CommsAlarmEmailReceiver_Type()
)
pt3080CommsAlarmEmailReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAlarmEmailReceiver.setStatus("current")


class _Pt3080CommsWebServicePort_Type(Integer32):
    """Custom type pt3080CommsWebServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsWebServicePort_Type.__name__ = "Integer32"
_Pt3080CommsWebServicePort_Object = MibScalar
pt3080CommsWebServicePort = _Pt3080CommsWebServicePort_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 35),
    _Pt3080CommsWebServicePort_Type()
)
pt3080CommsWebServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsWebServicePort.setStatus("current")


class _Pt3080CommsSCPIServicePort_Type(Integer32):
    """Custom type pt3080CommsSCPIServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsSCPIServicePort_Type.__name__ = "Integer32"
_Pt3080CommsSCPIServicePort_Object = MibScalar
pt3080CommsSCPIServicePort = _Pt3080CommsSCPIServicePort_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 36),
    _Pt3080CommsSCPIServicePort_Type()
)
pt3080CommsSCPIServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSCPIServicePort.setStatus("current")


class _Pt3080CommsSCPIServerBaudrate_Type(Integer32):
    """Custom type pt3080CommsSCPIServerBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("r2400", 0),
          ("r4800", 1),
          ("r9600", 2),
          ("r19200", 3),
          ("r38400", 4),
          ("r57600", 5),
          ("r115200", 6))
    )


_Pt3080CommsSCPIServerBaudrate_Type.__name__ = "Integer32"
_Pt3080CommsSCPIServerBaudrate_Object = MibScalar
pt3080CommsSCPIServerBaudrate = _Pt3080CommsSCPIServerBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 37),
    _Pt3080CommsSCPIServerBaudrate_Type()
)
pt3080CommsSCPIServerBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSCPIServerBaudrate.setStatus("current")


class _Pt3080CommsRipPort_Type(Integer32):
    """Custom type pt3080CommsRipPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsRipPort_Type.__name__ = "Integer32"
_Pt3080CommsRipPort_Object = MibScalar
pt3080CommsRipPort = _Pt3080CommsRipPort_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 38),
    _Pt3080CommsRipPort_Type()
)
pt3080CommsRipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRipPort.setStatus("current")


class _Pt3080CommsSCPIUartInterface_Type(Integer32):
    """Custom type pt3080CommsSCPIUartInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 0),
          ("rs485", 1),
          ("rs485hd", 2))
    )


_Pt3080CommsSCPIUartInterface_Type.__name__ = "Integer32"
_Pt3080CommsSCPIUartInterface_Object = MibScalar
pt3080CommsSCPIUartInterface = _Pt3080CommsSCPIUartInterface_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 39),
    _Pt3080CommsSCPIUartInterface_Type()
)
pt3080CommsSCPIUartInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSCPIUartInterface.setStatus("current")


class _Pt3080CommsAccessAllowed_Type(Integer32):
    """Custom type pt3080CommsAccessAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remote", 0),
          ("local-disable-set", 1))
    )


_Pt3080CommsAccessAllowed_Type.__name__ = "Integer32"
_Pt3080CommsAccessAllowed_Object = MibScalar
pt3080CommsAccessAllowed = _Pt3080CommsAccessAllowed_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 48),
    _Pt3080CommsAccessAllowed_Type()
)
pt3080CommsAccessAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAccessAllowed.setStatus("current")


class _Pt3080CommsAccessAllowedTimeout_Type(Integer32):
    """Custom type pt3080CommsAccessAllowedTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Pt3080CommsAccessAllowedTimeout_Type.__name__ = "Integer32"
_Pt3080CommsAccessAllowedTimeout_Object = MibScalar
pt3080CommsAccessAllowedTimeout = _Pt3080CommsAccessAllowedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 49),
    _Pt3080CommsAccessAllowedTimeout_Type()
)
pt3080CommsAccessAllowedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAccessAllowedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pt3080CommsAccessAllowedTimeout.setUnits("1 min")
_Pt3080CommsAccessAllowedTimeLeft_Type = Integer32
_Pt3080CommsAccessAllowedTimeLeft_Object = MibScalar
pt3080CommsAccessAllowedTimeLeft = _Pt3080CommsAccessAllowedTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 50),
    _Pt3080CommsAccessAllowedTimeLeft_Type()
)
pt3080CommsAccessAllowedTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsAccessAllowedTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    pt3080CommsAccessAllowedTimeLeft.setUnits("1 secs")
_Pt3080CommsAccessPasswordObserver_Type = DisplayString
_Pt3080CommsAccessPasswordObserver_Object = MibScalar
pt3080CommsAccessPasswordObserver = _Pt3080CommsAccessPasswordObserver_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 51),
    _Pt3080CommsAccessPasswordObserver_Type()
)
pt3080CommsAccessPasswordObserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAccessPasswordObserver.setStatus("current")
_Pt3080CommsAccessPasswordOperator_Type = DisplayString
_Pt3080CommsAccessPasswordOperator_Object = MibScalar
pt3080CommsAccessPasswordOperator = _Pt3080CommsAccessPasswordOperator_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 52),
    _Pt3080CommsAccessPasswordOperator_Type()
)
pt3080CommsAccessPasswordOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAccessPasswordOperator.setStatus("current")
_Pt3080CommsAccessPasswordAdministrator_Type = DisplayString
_Pt3080CommsAccessPasswordAdministrator_Object = MibScalar
pt3080CommsAccessPasswordAdministrator = _Pt3080CommsAccessPasswordAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 53),
    _Pt3080CommsAccessPasswordAdministrator_Type()
)
pt3080CommsAccessPasswordAdministrator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsAccessPasswordAdministrator.setStatus("current")


class _Pt3080CommsSNMPServicePort_Type(Integer32):
    """Custom type pt3080CommsSNMPServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsSNMPServicePort_Type.__name__ = "Integer32"
_Pt3080CommsSNMPServicePort_Object = MibScalar
pt3080CommsSNMPServicePort = _Pt3080CommsSNMPServicePort_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 55),
    _Pt3080CommsSNMPServicePort_Type()
)
pt3080CommsSNMPServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPServicePort.setStatus("current")
_Pt3080CommsSNMPReadOnlyCommunity_Type = DisplayString
_Pt3080CommsSNMPReadOnlyCommunity_Object = MibScalar
pt3080CommsSNMPReadOnlyCommunity = _Pt3080CommsSNMPReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 56),
    _Pt3080CommsSNMPReadOnlyCommunity_Type()
)
pt3080CommsSNMPReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPReadOnlyCommunity.setStatus("current")
_Pt3080CommsSNMPReadWriteCommunity_Type = DisplayString
_Pt3080CommsSNMPReadWriteCommunity_Object = MibScalar
pt3080CommsSNMPReadWriteCommunity = _Pt3080CommsSNMPReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 57),
    _Pt3080CommsSNMPReadWriteCommunity_Type()
)
pt3080CommsSNMPReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPReadWriteCommunity.setStatus("current")
_Pt3080CommsSNMPTrapCommunity_Type = DisplayString
_Pt3080CommsSNMPTrapCommunity_Object = MibScalar
pt3080CommsSNMPTrapCommunity = _Pt3080CommsSNMPTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 58),
    _Pt3080CommsSNMPTrapCommunity_Type()
)
pt3080CommsSNMPTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapCommunity.setStatus("current")
_Pt3080CommsSNMPTrapDestination_Type = DisplayString
_Pt3080CommsSNMPTrapDestination_Object = MibScalar
pt3080CommsSNMPTrapDestination = _Pt3080CommsSNMPTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 59),
    _Pt3080CommsSNMPTrapDestination_Type()
)
pt3080CommsSNMPTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestination.setStatus("current")


class _Pt3080CommsSNMPTrapDestinationPort_Type(Integer32):
    """Custom type pt3080CommsSNMPTrapDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsSNMPTrapDestinationPort_Type.__name__ = "Integer32"
_Pt3080CommsSNMPTrapDestinationPort_Object = MibScalar
pt3080CommsSNMPTrapDestinationPort = _Pt3080CommsSNMPTrapDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 60),
    _Pt3080CommsSNMPTrapDestinationPort_Type()
)
pt3080CommsSNMPTrapDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestinationPort.setStatus("current")


class _Pt3080CommsRemoteDhcpMode_Type(Integer32):
    """Custom type pt3080CommsRemoteDhcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("client", 1))
    )


_Pt3080CommsRemoteDhcpMode_Type.__name__ = "Integer32"
_Pt3080CommsRemoteDhcpMode_Object = MibScalar
pt3080CommsRemoteDhcpMode = _Pt3080CommsRemoteDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 73),
    _Pt3080CommsRemoteDhcpMode_Type()
)
pt3080CommsRemoteDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteDhcpMode.setStatus("current")


class _Pt3080CommsGbeAdminDhcpMode_Type(Integer32):
    """Custom type pt3080CommsGbeAdminDhcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("client", 1))
    )


_Pt3080CommsGbeAdminDhcpMode_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminDhcpMode_Object = MibScalar
pt3080CommsGbeAdminDhcpMode = _Pt3080CommsGbeAdminDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 74),
    _Pt3080CommsGbeAdminDhcpMode_Type()
)
pt3080CommsGbeAdminDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminDhcpMode.setStatus("current")


class _Pt3080CommsBackupDhcpMode_Type(Integer32):
    """Custom type pt3080CommsBackupDhcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("client", 1))
    )


_Pt3080CommsBackupDhcpMode_Type.__name__ = "Integer32"
_Pt3080CommsBackupDhcpMode_Object = MibScalar
pt3080CommsBackupDhcpMode = _Pt3080CommsBackupDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 75),
    _Pt3080CommsBackupDhcpMode_Type()
)
pt3080CommsBackupDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupDhcpMode.setStatus("current")


class _Pt3080CommsLocalPhysicalInterface_Type(Integer32):
    """Custom type pt3080CommsLocalPhysicalInterface based on Integer32"""
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
        *(("eth0", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4))
    )


_Pt3080CommsLocalPhysicalInterface_Type.__name__ = "Integer32"
_Pt3080CommsLocalPhysicalInterface_Object = MibScalar
pt3080CommsLocalPhysicalInterface = _Pt3080CommsLocalPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 80),
    _Pt3080CommsLocalPhysicalInterface_Type()
)
pt3080CommsLocalPhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalPhysicalInterface.setStatus("current")


class _Pt3080CommsRemotePhysicalInterface_Type(Integer32):
    """Custom type pt3080CommsRemotePhysicalInterface based on Integer32"""
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
        *(("eth0", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4))
    )


_Pt3080CommsRemotePhysicalInterface_Type.__name__ = "Integer32"
_Pt3080CommsRemotePhysicalInterface_Object = MibScalar
pt3080CommsRemotePhysicalInterface = _Pt3080CommsRemotePhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 81),
    _Pt3080CommsRemotePhysicalInterface_Type()
)
pt3080CommsRemotePhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemotePhysicalInterface.setStatus("current")


class _Pt3080CommsGbeAdminPhysicalInterface_Type(Integer32):
    """Custom type pt3080CommsGbeAdminPhysicalInterface based on Integer32"""
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
        *(("eth0", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4))
    )


_Pt3080CommsGbeAdminPhysicalInterface_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminPhysicalInterface_Object = MibScalar
pt3080CommsGbeAdminPhysicalInterface = _Pt3080CommsGbeAdminPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 82),
    _Pt3080CommsGbeAdminPhysicalInterface_Type()
)
pt3080CommsGbeAdminPhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminPhysicalInterface.setStatus("current")


class _Pt3080CommsBroadcastStormProtection_Type(Integer32):
    """Custom type pt3080CommsBroadcastStormProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080CommsBroadcastStormProtection_Type.__name__ = "Integer32"
_Pt3080CommsBroadcastStormProtection_Object = MibScalar
pt3080CommsBroadcastStormProtection = _Pt3080CommsBroadcastStormProtection_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 94),
    _Pt3080CommsBroadcastStormProtection_Type()
)
pt3080CommsBroadcastStormProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBroadcastStormProtection.setStatus("current")


class _Pt3080CommsIGMPv2UnsolicitedReportInterval_Type(Integer32):
    """Custom type pt3080CommsIGMPv2UnsolicitedReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Pt3080CommsIGMPv2UnsolicitedReportInterval_Type.__name__ = "Integer32"
_Pt3080CommsIGMPv2UnsolicitedReportInterval_Object = MibScalar
pt3080CommsIGMPv2UnsolicitedReportInterval = _Pt3080CommsIGMPv2UnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 95),
    _Pt3080CommsIGMPv2UnsolicitedReportInterval_Type()
)
pt3080CommsIGMPv2UnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsIGMPv2UnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    pt3080CommsIGMPv2UnsolicitedReportInterval.setUnits("1 ms")


class _Pt3080CommsIGMPv3UnsolicitedReportInterval_Type(Integer32):
    """Custom type pt3080CommsIGMPv3UnsolicitedReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Pt3080CommsIGMPv3UnsolicitedReportInterval_Type.__name__ = "Integer32"
_Pt3080CommsIGMPv3UnsolicitedReportInterval_Object = MibScalar
pt3080CommsIGMPv3UnsolicitedReportInterval = _Pt3080CommsIGMPv3UnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 96),
    _Pt3080CommsIGMPv3UnsolicitedReportInterval_Type()
)
pt3080CommsIGMPv3UnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsIGMPv3UnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    pt3080CommsIGMPv3UnsolicitedReportInterval.setUnits("1 ms")


class _Pt3080CommsIGMPQueryRobustnessCount_Type(Integer32):
    """Custom type pt3080CommsIGMPQueryRobustnessCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_Pt3080CommsIGMPQueryRobustnessCount_Type.__name__ = "Integer32"
_Pt3080CommsIGMPQueryRobustnessCount_Object = MibScalar
pt3080CommsIGMPQueryRobustnessCount = _Pt3080CommsIGMPQueryRobustnessCount_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 97),
    _Pt3080CommsIGMPQueryRobustnessCount_Type()
)
pt3080CommsIGMPQueryRobustnessCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsIGMPQueryRobustnessCount.setStatus("current")


class _Pt3080CommsSeparatedSwitchPorts_Type(Integer32):
    """Custom type pt3080CommsSeparatedSwitchPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080CommsSeparatedSwitchPorts_Type.__name__ = "Integer32"
_Pt3080CommsSeparatedSwitchPorts_Object = MibScalar
pt3080CommsSeparatedSwitchPorts = _Pt3080CommsSeparatedSwitchPorts_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 98),
    _Pt3080CommsSeparatedSwitchPorts_Type()
)
pt3080CommsSeparatedSwitchPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSeparatedSwitchPorts.setStatus("current")


class _Pt3080CommsIGMPVersion_Type(Integer32):
    """Custom type pt3080CommsIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_Pt3080CommsIGMPVersion_Type.__name__ = "Integer32"
_Pt3080CommsIGMPVersion_Object = MibScalar
pt3080CommsIGMPVersion = _Pt3080CommsIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 99),
    _Pt3080CommsIGMPVersion_Type()
)
pt3080CommsIGMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsIGMPVersion.setStatus("current")
_Pt3080CommsLocalIpMulticastAddr_Type = IpAddress
_Pt3080CommsLocalIpMulticastAddr_Object = MibScalar
pt3080CommsLocalIpMulticastAddr = _Pt3080CommsLocalIpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 100),
    _Pt3080CommsLocalIpMulticastAddr_Type()
)
pt3080CommsLocalIpMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastAddr.setStatus("current")


class _Pt3080CommsLocalVlanEnable_Type(Integer32):
    """Custom type pt3080CommsLocalVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsLocalVlanEnable_Type.__name__ = "Integer32"
_Pt3080CommsLocalVlanEnable_Object = MibScalar
pt3080CommsLocalVlanEnable = _Pt3080CommsLocalVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 101),
    _Pt3080CommsLocalVlanEnable_Type()
)
pt3080CommsLocalVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalVlanEnable.setStatus("current")


class _Pt3080CommsLocalVlanId_Type(Integer32):
    """Custom type pt3080CommsLocalVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Pt3080CommsLocalVlanId_Type.__name__ = "Integer32"
_Pt3080CommsLocalVlanId_Object = MibScalar
pt3080CommsLocalVlanId = _Pt3080CommsLocalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 102),
    _Pt3080CommsLocalVlanId_Type()
)
pt3080CommsLocalVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalVlanId.setStatus("current")


class _Pt3080CommsLocalServiceSNMP_Type(Integer32):
    """Custom type pt3080CommsLocalServiceSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsLocalServiceSNMP_Type.__name__ = "Integer32"
_Pt3080CommsLocalServiceSNMP_Object = MibScalar
pt3080CommsLocalServiceSNMP = _Pt3080CommsLocalServiceSNMP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 103),
    _Pt3080CommsLocalServiceSNMP_Type()
)
pt3080CommsLocalServiceSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalServiceSNMP.setStatus("current")


class _Pt3080CommsLocalServiceSCPI_Type(Integer32):
    """Custom type pt3080CommsLocalServiceSCPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsLocalServiceSCPI_Type.__name__ = "Integer32"
_Pt3080CommsLocalServiceSCPI_Object = MibScalar
pt3080CommsLocalServiceSCPI = _Pt3080CommsLocalServiceSCPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 104),
    _Pt3080CommsLocalServiceSCPI_Type()
)
pt3080CommsLocalServiceSCPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalServiceSCPI.setStatus("current")


class _Pt3080CommsLocalServiceTSoIP_Type(Integer32):
    """Custom type pt3080CommsLocalServiceTSoIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsLocalServiceTSoIP_Type.__name__ = "Integer32"
_Pt3080CommsLocalServiceTSoIP_Object = MibScalar
pt3080CommsLocalServiceTSoIP = _Pt3080CommsLocalServiceTSoIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 105),
    _Pt3080CommsLocalServiceTSoIP_Type()
)
pt3080CommsLocalServiceTSoIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalServiceTSoIP.setStatus("current")


class _Pt3080CommsLocalServiceRIP_Type(Integer32):
    """Custom type pt3080CommsLocalServiceRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsLocalServiceRIP_Type.__name__ = "Integer32"
_Pt3080CommsLocalServiceRIP_Object = MibScalar
pt3080CommsLocalServiceRIP = _Pt3080CommsLocalServiceRIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 106),
    _Pt3080CommsLocalServiceRIP_Type()
)
pt3080CommsLocalServiceRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalServiceRIP.setStatus("current")
_Pt3080CommsRemoteIpMulticastAddr_Type = IpAddress
_Pt3080CommsRemoteIpMulticastAddr_Object = MibScalar
pt3080CommsRemoteIpMulticastAddr = _Pt3080CommsRemoteIpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 110),
    _Pt3080CommsRemoteIpMulticastAddr_Type()
)
pt3080CommsRemoteIpMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastAddr.setStatus("current")


class _Pt3080CommsRemoteVlanEnable_Type(Integer32):
    """Custom type pt3080CommsRemoteVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsRemoteVlanEnable_Type.__name__ = "Integer32"
_Pt3080CommsRemoteVlanEnable_Object = MibScalar
pt3080CommsRemoteVlanEnable = _Pt3080CommsRemoteVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 111),
    _Pt3080CommsRemoteVlanEnable_Type()
)
pt3080CommsRemoteVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteVlanEnable.setStatus("current")


class _Pt3080CommsRemoteVlanId_Type(Integer32):
    """Custom type pt3080CommsRemoteVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Pt3080CommsRemoteVlanId_Type.__name__ = "Integer32"
_Pt3080CommsRemoteVlanId_Object = MibScalar
pt3080CommsRemoteVlanId = _Pt3080CommsRemoteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 112),
    _Pt3080CommsRemoteVlanId_Type()
)
pt3080CommsRemoteVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteVlanId.setStatus("current")


class _Pt3080CommsRemoteServiceSNMP_Type(Integer32):
    """Custom type pt3080CommsRemoteServiceSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsRemoteServiceSNMP_Type.__name__ = "Integer32"
_Pt3080CommsRemoteServiceSNMP_Object = MibScalar
pt3080CommsRemoteServiceSNMP = _Pt3080CommsRemoteServiceSNMP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 113),
    _Pt3080CommsRemoteServiceSNMP_Type()
)
pt3080CommsRemoteServiceSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteServiceSNMP.setStatus("current")


class _Pt3080CommsRemoteServiceSCPI_Type(Integer32):
    """Custom type pt3080CommsRemoteServiceSCPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsRemoteServiceSCPI_Type.__name__ = "Integer32"
_Pt3080CommsRemoteServiceSCPI_Object = MibScalar
pt3080CommsRemoteServiceSCPI = _Pt3080CommsRemoteServiceSCPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 114),
    _Pt3080CommsRemoteServiceSCPI_Type()
)
pt3080CommsRemoteServiceSCPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteServiceSCPI.setStatus("current")


class _Pt3080CommsRemoteServiceTSoIP_Type(Integer32):
    """Custom type pt3080CommsRemoteServiceTSoIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsRemoteServiceTSoIP_Type.__name__ = "Integer32"
_Pt3080CommsRemoteServiceTSoIP_Object = MibScalar
pt3080CommsRemoteServiceTSoIP = _Pt3080CommsRemoteServiceTSoIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 115),
    _Pt3080CommsRemoteServiceTSoIP_Type()
)
pt3080CommsRemoteServiceTSoIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteServiceTSoIP.setStatus("current")


class _Pt3080CommsRemoteServiceWeb_Type(Integer32):
    """Custom type pt3080CommsRemoteServiceWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsRemoteServiceWeb_Type.__name__ = "Integer32"
_Pt3080CommsRemoteServiceWeb_Object = MibScalar
pt3080CommsRemoteServiceWeb = _Pt3080CommsRemoteServiceWeb_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 116),
    _Pt3080CommsRemoteServiceWeb_Type()
)
pt3080CommsRemoteServiceWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteServiceWeb.setStatus("current")


class _Pt3080CommsRemoteEnable_Type(Integer32):
    """Custom type pt3080CommsRemoteEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsRemoteEnable_Type.__name__ = "Integer32"
_Pt3080CommsRemoteEnable_Object = MibScalar
pt3080CommsRemoteEnable = _Pt3080CommsRemoteEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 117),
    _Pt3080CommsRemoteEnable_Type()
)
pt3080CommsRemoteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteEnable.setStatus("current")


class _Pt3080CommsRemoteServiceRIP_Type(Integer32):
    """Custom type pt3080CommsRemoteServiceRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsRemoteServiceRIP_Type.__name__ = "Integer32"
_Pt3080CommsRemoteServiceRIP_Object = MibScalar
pt3080CommsRemoteServiceRIP = _Pt3080CommsRemoteServiceRIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 118),
    _Pt3080CommsRemoteServiceRIP_Type()
)
pt3080CommsRemoteServiceRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteServiceRIP.setStatus("current")
_Pt3080CommsGbeAdminIpMulticastAddr_Type = IpAddress
_Pt3080CommsGbeAdminIpMulticastAddr_Object = MibScalar
pt3080CommsGbeAdminIpMulticastAddr = _Pt3080CommsGbeAdminIpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 120),
    _Pt3080CommsGbeAdminIpMulticastAddr_Type()
)
pt3080CommsGbeAdminIpMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastAddr.setStatus("current")


class _Pt3080CommsGbeAdminVlanEnable_Type(Integer32):
    """Custom type pt3080CommsGbeAdminVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsGbeAdminVlanEnable_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminVlanEnable_Object = MibScalar
pt3080CommsGbeAdminVlanEnable = _Pt3080CommsGbeAdminVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 121),
    _Pt3080CommsGbeAdminVlanEnable_Type()
)
pt3080CommsGbeAdminVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminVlanEnable.setStatus("current")


class _Pt3080CommsGbeAdminVlanId_Type(Integer32):
    """Custom type pt3080CommsGbeAdminVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Pt3080CommsGbeAdminVlanId_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminVlanId_Object = MibScalar
pt3080CommsGbeAdminVlanId = _Pt3080CommsGbeAdminVlanId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 122),
    _Pt3080CommsGbeAdminVlanId_Type()
)
pt3080CommsGbeAdminVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminVlanId.setStatus("current")


class _Pt3080CommsGbeAdminServiceSNMP_Type(Integer32):
    """Custom type pt3080CommsGbeAdminServiceSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsGbeAdminServiceSNMP_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminServiceSNMP_Object = MibScalar
pt3080CommsGbeAdminServiceSNMP = _Pt3080CommsGbeAdminServiceSNMP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 123),
    _Pt3080CommsGbeAdminServiceSNMP_Type()
)
pt3080CommsGbeAdminServiceSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminServiceSNMP.setStatus("current")


class _Pt3080CommsGbeAdminServiceSCPI_Type(Integer32):
    """Custom type pt3080CommsGbeAdminServiceSCPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsGbeAdminServiceSCPI_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminServiceSCPI_Object = MibScalar
pt3080CommsGbeAdminServiceSCPI = _Pt3080CommsGbeAdminServiceSCPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 124),
    _Pt3080CommsGbeAdminServiceSCPI_Type()
)
pt3080CommsGbeAdminServiceSCPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminServiceSCPI.setStatus("current")


class _Pt3080CommsGbeAdminServiceTSoIP_Type(Integer32):
    """Custom type pt3080CommsGbeAdminServiceTSoIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsGbeAdminServiceTSoIP_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminServiceTSoIP_Object = MibScalar
pt3080CommsGbeAdminServiceTSoIP = _Pt3080CommsGbeAdminServiceTSoIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 125),
    _Pt3080CommsGbeAdminServiceTSoIP_Type()
)
pt3080CommsGbeAdminServiceTSoIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminServiceTSoIP.setStatus("current")


class _Pt3080CommsGbeAdminServiceWeb_Type(Integer32):
    """Custom type pt3080CommsGbeAdminServiceWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsGbeAdminServiceWeb_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminServiceWeb_Object = MibScalar
pt3080CommsGbeAdminServiceWeb = _Pt3080CommsGbeAdminServiceWeb_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 126),
    _Pt3080CommsGbeAdminServiceWeb_Type()
)
pt3080CommsGbeAdminServiceWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminServiceWeb.setStatus("current")


class _Pt3080CommsGbeAdminEnable_Type(Integer32):
    """Custom type pt3080CommsGbeAdminEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsGbeAdminEnable_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminEnable_Object = MibScalar
pt3080CommsGbeAdminEnable = _Pt3080CommsGbeAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 127),
    _Pt3080CommsGbeAdminEnable_Type()
)
pt3080CommsGbeAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminEnable.setStatus("current")


class _Pt3080CommsGbeAdminServiceRIP_Type(Integer32):
    """Custom type pt3080CommsGbeAdminServiceRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsGbeAdminServiceRIP_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminServiceRIP_Object = MibScalar
pt3080CommsGbeAdminServiceRIP = _Pt3080CommsGbeAdminServiceRIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 128),
    _Pt3080CommsGbeAdminServiceRIP_Type()
)
pt3080CommsGbeAdminServiceRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminServiceRIP.setStatus("current")


class _Pt3080CommsBackupEnable_Type(Integer32):
    """Custom type pt3080CommsBackupEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsBackupEnable_Type.__name__ = "Integer32"
_Pt3080CommsBackupEnable_Object = MibScalar
pt3080CommsBackupEnable = _Pt3080CommsBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 150),
    _Pt3080CommsBackupEnable_Type()
)
pt3080CommsBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupEnable.setStatus("current")


class _Pt3080CommsBackupPhysicalInterface_Type(Integer32):
    """Custom type pt3080CommsBackupPhysicalInterface based on Integer32"""
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
        *(("eth0", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4))
    )


_Pt3080CommsBackupPhysicalInterface_Type.__name__ = "Integer32"
_Pt3080CommsBackupPhysicalInterface_Object = MibScalar
pt3080CommsBackupPhysicalInterface = _Pt3080CommsBackupPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 151),
    _Pt3080CommsBackupPhysicalInterface_Type()
)
pt3080CommsBackupPhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupPhysicalInterface.setStatus("current")
_Pt3080CommsBackupStaticIpAddr_Type = IpAddress
_Pt3080CommsBackupStaticIpAddr_Object = MibScalar
pt3080CommsBackupStaticIpAddr = _Pt3080CommsBackupStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 152),
    _Pt3080CommsBackupStaticIpAddr_Type()
)
pt3080CommsBackupStaticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupStaticIpAddr.setStatus("current")
_Pt3080CommsBackupStaticNetmask_Type = IpAddress
_Pt3080CommsBackupStaticNetmask_Object = MibScalar
pt3080CommsBackupStaticNetmask = _Pt3080CommsBackupStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 153),
    _Pt3080CommsBackupStaticNetmask_Type()
)
pt3080CommsBackupStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupStaticNetmask.setStatus("current")
_Pt3080CommsBackupIpMulticastAddr_Type = IpAddress
_Pt3080CommsBackupIpMulticastAddr_Object = MibScalar
pt3080CommsBackupIpMulticastAddr = _Pt3080CommsBackupIpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 154),
    _Pt3080CommsBackupIpMulticastAddr_Type()
)
pt3080CommsBackupIpMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastAddr.setStatus("current")


class _Pt3080CommsBackupVlanEnable_Type(Integer32):
    """Custom type pt3080CommsBackupVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsBackupVlanEnable_Type.__name__ = "Integer32"
_Pt3080CommsBackupVlanEnable_Object = MibScalar
pt3080CommsBackupVlanEnable = _Pt3080CommsBackupVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 155),
    _Pt3080CommsBackupVlanEnable_Type()
)
pt3080CommsBackupVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupVlanEnable.setStatus("current")


class _Pt3080CommsBackupVlanId_Type(Integer32):
    """Custom type pt3080CommsBackupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Pt3080CommsBackupVlanId_Type.__name__ = "Integer32"
_Pt3080CommsBackupVlanId_Object = MibScalar
pt3080CommsBackupVlanId = _Pt3080CommsBackupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 156),
    _Pt3080CommsBackupVlanId_Type()
)
pt3080CommsBackupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupVlanId.setStatus("current")


class _Pt3080CommsBackupServiceSNMP_Type(Integer32):
    """Custom type pt3080CommsBackupServiceSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsBackupServiceSNMP_Type.__name__ = "Integer32"
_Pt3080CommsBackupServiceSNMP_Object = MibScalar
pt3080CommsBackupServiceSNMP = _Pt3080CommsBackupServiceSNMP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 157),
    _Pt3080CommsBackupServiceSNMP_Type()
)
pt3080CommsBackupServiceSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupServiceSNMP.setStatus("current")


class _Pt3080CommsBackupServiceSCPI_Type(Integer32):
    """Custom type pt3080CommsBackupServiceSCPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsBackupServiceSCPI_Type.__name__ = "Integer32"
_Pt3080CommsBackupServiceSCPI_Object = MibScalar
pt3080CommsBackupServiceSCPI = _Pt3080CommsBackupServiceSCPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 158),
    _Pt3080CommsBackupServiceSCPI_Type()
)
pt3080CommsBackupServiceSCPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupServiceSCPI.setStatus("current")


class _Pt3080CommsBackupServiceTSoIP_Type(Integer32):
    """Custom type pt3080CommsBackupServiceTSoIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsBackupServiceTSoIP_Type.__name__ = "Integer32"
_Pt3080CommsBackupServiceTSoIP_Object = MibScalar
pt3080CommsBackupServiceTSoIP = _Pt3080CommsBackupServiceTSoIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 159),
    _Pt3080CommsBackupServiceTSoIP_Type()
)
pt3080CommsBackupServiceTSoIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupServiceTSoIP.setStatus("current")


class _Pt3080CommsBackupServiceWeb_Type(Integer32):
    """Custom type pt3080CommsBackupServiceWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsBackupServiceWeb_Type.__name__ = "Integer32"
_Pt3080CommsBackupServiceWeb_Object = MibScalar
pt3080CommsBackupServiceWeb = _Pt3080CommsBackupServiceWeb_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 160),
    _Pt3080CommsBackupServiceWeb_Type()
)
pt3080CommsBackupServiceWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupServiceWeb.setStatus("current")


class _Pt3080CommsBackupServiceRIP_Type(Integer32):
    """Custom type pt3080CommsBackupServiceRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsBackupServiceRIP_Type.__name__ = "Integer32"
_Pt3080CommsBackupServiceRIP_Object = MibScalar
pt3080CommsBackupServiceRIP = _Pt3080CommsBackupServiceRIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 161),
    _Pt3080CommsBackupServiceRIP_Type()
)
pt3080CommsBackupServiceRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupServiceRIP.setStatus("current")
_Pt3080CommsBackupCurrentIpAddr_Type = IpAddress
_Pt3080CommsBackupCurrentIpAddr_Object = MibScalar
pt3080CommsBackupCurrentIpAddr = _Pt3080CommsBackupCurrentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 162),
    _Pt3080CommsBackupCurrentIpAddr_Type()
)
pt3080CommsBackupCurrentIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsBackupCurrentIpAddr.setStatus("current")
_Pt3080CommsBackupCurrentNetmask_Type = IpAddress
_Pt3080CommsBackupCurrentNetmask_Object = MibScalar
pt3080CommsBackupCurrentNetmask = _Pt3080CommsBackupCurrentNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 163),
    _Pt3080CommsBackupCurrentNetmask_Type()
)
pt3080CommsBackupCurrentNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsBackupCurrentNetmask.setStatus("current")
_Pt3080CommsBackupIpMulticastSourceFilterAddress1_Type = IpAddress
_Pt3080CommsBackupIpMulticastSourceFilterAddress1_Object = MibScalar
pt3080CommsBackupIpMulticastSourceFilterAddress1 = _Pt3080CommsBackupIpMulticastSourceFilterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 170),
    _Pt3080CommsBackupIpMulticastSourceFilterAddress1_Type()
)
pt3080CommsBackupIpMulticastSourceFilterAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastSourceFilterAddress1.setStatus("current")
_Pt3080CommsBackupIpMulticastSourceFilterAddress2_Type = IpAddress
_Pt3080CommsBackupIpMulticastSourceFilterAddress2_Object = MibScalar
pt3080CommsBackupIpMulticastSourceFilterAddress2 = _Pt3080CommsBackupIpMulticastSourceFilterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 171),
    _Pt3080CommsBackupIpMulticastSourceFilterAddress2_Type()
)
pt3080CommsBackupIpMulticastSourceFilterAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastSourceFilterAddress2.setStatus("current")
_Pt3080CommsBackupIpMulticastSourceFilterAddress3_Type = IpAddress
_Pt3080CommsBackupIpMulticastSourceFilterAddress3_Object = MibScalar
pt3080CommsBackupIpMulticastSourceFilterAddress3 = _Pt3080CommsBackupIpMulticastSourceFilterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 172),
    _Pt3080CommsBackupIpMulticastSourceFilterAddress3_Type()
)
pt3080CommsBackupIpMulticastSourceFilterAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastSourceFilterAddress3.setStatus("current")
_Pt3080CommsBackupIpMulticastSourceFilterAddress4_Type = IpAddress
_Pt3080CommsBackupIpMulticastSourceFilterAddress4_Object = MibScalar
pt3080CommsBackupIpMulticastSourceFilterAddress4 = _Pt3080CommsBackupIpMulticastSourceFilterAddress4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 173),
    _Pt3080CommsBackupIpMulticastSourceFilterAddress4_Type()
)
pt3080CommsBackupIpMulticastSourceFilterAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastSourceFilterAddress4.setStatus("current")
_Pt3080CommsBackupIpMulticastSourceFilterAddress5_Type = IpAddress
_Pt3080CommsBackupIpMulticastSourceFilterAddress5_Object = MibScalar
pt3080CommsBackupIpMulticastSourceFilterAddress5 = _Pt3080CommsBackupIpMulticastSourceFilterAddress5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 174),
    _Pt3080CommsBackupIpMulticastSourceFilterAddress5_Type()
)
pt3080CommsBackupIpMulticastSourceFilterAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastSourceFilterAddress5.setStatus("current")
_Pt3080CommsBackupIpMulticastSourceFilterAddress6_Type = IpAddress
_Pt3080CommsBackupIpMulticastSourceFilterAddress6_Object = MibScalar
pt3080CommsBackupIpMulticastSourceFilterAddress6 = _Pt3080CommsBackupIpMulticastSourceFilterAddress6_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 175),
    _Pt3080CommsBackupIpMulticastSourceFilterAddress6_Type()
)
pt3080CommsBackupIpMulticastSourceFilterAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastSourceFilterAddress6.setStatus("current")


class _Pt3080CommsLocalIpMulticastSourceFilterMode_Type(Integer32):
    """Custom type pt3080CommsLocalIpMulticastSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfinclude", 0),
          ("sfexclude", 1))
    )


_Pt3080CommsLocalIpMulticastSourceFilterMode_Type.__name__ = "Integer32"
_Pt3080CommsLocalIpMulticastSourceFilterMode_Object = MibScalar
pt3080CommsLocalIpMulticastSourceFilterMode = _Pt3080CommsLocalIpMulticastSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 190),
    _Pt3080CommsLocalIpMulticastSourceFilterMode_Type()
)
pt3080CommsLocalIpMulticastSourceFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastSourceFilterMode.setStatus("current")


class _Pt3080CommsRemoteIpMulticastSourceFilterMode_Type(Integer32):
    """Custom type pt3080CommsRemoteIpMulticastSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfinclude", 0),
          ("sfexclude", 1))
    )


_Pt3080CommsRemoteIpMulticastSourceFilterMode_Type.__name__ = "Integer32"
_Pt3080CommsRemoteIpMulticastSourceFilterMode_Object = MibScalar
pt3080CommsRemoteIpMulticastSourceFilterMode = _Pt3080CommsRemoteIpMulticastSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 191),
    _Pt3080CommsRemoteIpMulticastSourceFilterMode_Type()
)
pt3080CommsRemoteIpMulticastSourceFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastSourceFilterMode.setStatus("current")


class _Pt3080CommsGbeAdminIpMulticastSourceFilterMode_Type(Integer32):
    """Custom type pt3080CommsGbeAdminIpMulticastSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfinclude", 0),
          ("sfexclude", 1))
    )


_Pt3080CommsGbeAdminIpMulticastSourceFilterMode_Type.__name__ = "Integer32"
_Pt3080CommsGbeAdminIpMulticastSourceFilterMode_Object = MibScalar
pt3080CommsGbeAdminIpMulticastSourceFilterMode = _Pt3080CommsGbeAdminIpMulticastSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 192),
    _Pt3080CommsGbeAdminIpMulticastSourceFilterMode_Type()
)
pt3080CommsGbeAdminIpMulticastSourceFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastSourceFilterMode.setStatus("current")


class _Pt3080CommsBackupIpMulticastSourceFilterMode_Type(Integer32):
    """Custom type pt3080CommsBackupIpMulticastSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfinclude", 0),
          ("sfexclude", 1))
    )


_Pt3080CommsBackupIpMulticastSourceFilterMode_Type.__name__ = "Integer32"
_Pt3080CommsBackupIpMulticastSourceFilterMode_Object = MibScalar
pt3080CommsBackupIpMulticastSourceFilterMode = _Pt3080CommsBackupIpMulticastSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 193),
    _Pt3080CommsBackupIpMulticastSourceFilterMode_Type()
)
pt3080CommsBackupIpMulticastSourceFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsBackupIpMulticastSourceFilterMode.setStatus("current")
_Pt3080CommsLocalIpMulticastSourceFilterAddress1_Type = IpAddress
_Pt3080CommsLocalIpMulticastSourceFilterAddress1_Object = MibScalar
pt3080CommsLocalIpMulticastSourceFilterAddress1 = _Pt3080CommsLocalIpMulticastSourceFilterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 200),
    _Pt3080CommsLocalIpMulticastSourceFilterAddress1_Type()
)
pt3080CommsLocalIpMulticastSourceFilterAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastSourceFilterAddress1.setStatus("current")
_Pt3080CommsLocalIpMulticastSourceFilterAddress2_Type = IpAddress
_Pt3080CommsLocalIpMulticastSourceFilterAddress2_Object = MibScalar
pt3080CommsLocalIpMulticastSourceFilterAddress2 = _Pt3080CommsLocalIpMulticastSourceFilterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 201),
    _Pt3080CommsLocalIpMulticastSourceFilterAddress2_Type()
)
pt3080CommsLocalIpMulticastSourceFilterAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastSourceFilterAddress2.setStatus("current")
_Pt3080CommsLocalIpMulticastSourceFilterAddress3_Type = IpAddress
_Pt3080CommsLocalIpMulticastSourceFilterAddress3_Object = MibScalar
pt3080CommsLocalIpMulticastSourceFilterAddress3 = _Pt3080CommsLocalIpMulticastSourceFilterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 202),
    _Pt3080CommsLocalIpMulticastSourceFilterAddress3_Type()
)
pt3080CommsLocalIpMulticastSourceFilterAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastSourceFilterAddress3.setStatus("current")
_Pt3080CommsLocalIpMulticastSourceFilterAddress4_Type = IpAddress
_Pt3080CommsLocalIpMulticastSourceFilterAddress4_Object = MibScalar
pt3080CommsLocalIpMulticastSourceFilterAddress4 = _Pt3080CommsLocalIpMulticastSourceFilterAddress4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 203),
    _Pt3080CommsLocalIpMulticastSourceFilterAddress4_Type()
)
pt3080CommsLocalIpMulticastSourceFilterAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastSourceFilterAddress4.setStatus("current")
_Pt3080CommsLocalIpMulticastSourceFilterAddress5_Type = IpAddress
_Pt3080CommsLocalIpMulticastSourceFilterAddress5_Object = MibScalar
pt3080CommsLocalIpMulticastSourceFilterAddress5 = _Pt3080CommsLocalIpMulticastSourceFilterAddress5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 204),
    _Pt3080CommsLocalIpMulticastSourceFilterAddress5_Type()
)
pt3080CommsLocalIpMulticastSourceFilterAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastSourceFilterAddress5.setStatus("current")
_Pt3080CommsLocalIpMulticastSourceFilterAddress6_Type = IpAddress
_Pt3080CommsLocalIpMulticastSourceFilterAddress6_Object = MibScalar
pt3080CommsLocalIpMulticastSourceFilterAddress6 = _Pt3080CommsLocalIpMulticastSourceFilterAddress6_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 205),
    _Pt3080CommsLocalIpMulticastSourceFilterAddress6_Type()
)
pt3080CommsLocalIpMulticastSourceFilterAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsLocalIpMulticastSourceFilterAddress6.setStatus("current")
_Pt3080CommsRemoteIpMulticastSourceFilterAddress1_Type = IpAddress
_Pt3080CommsRemoteIpMulticastSourceFilterAddress1_Object = MibScalar
pt3080CommsRemoteIpMulticastSourceFilterAddress1 = _Pt3080CommsRemoteIpMulticastSourceFilterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 220),
    _Pt3080CommsRemoteIpMulticastSourceFilterAddress1_Type()
)
pt3080CommsRemoteIpMulticastSourceFilterAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastSourceFilterAddress1.setStatus("current")
_Pt3080CommsRemoteIpMulticastSourceFilterAddress2_Type = IpAddress
_Pt3080CommsRemoteIpMulticastSourceFilterAddress2_Object = MibScalar
pt3080CommsRemoteIpMulticastSourceFilterAddress2 = _Pt3080CommsRemoteIpMulticastSourceFilterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 221),
    _Pt3080CommsRemoteIpMulticastSourceFilterAddress2_Type()
)
pt3080CommsRemoteIpMulticastSourceFilterAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastSourceFilterAddress2.setStatus("current")
_Pt3080CommsRemoteIpMulticastSourceFilterAddress3_Type = IpAddress
_Pt3080CommsRemoteIpMulticastSourceFilterAddress3_Object = MibScalar
pt3080CommsRemoteIpMulticastSourceFilterAddress3 = _Pt3080CommsRemoteIpMulticastSourceFilterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 222),
    _Pt3080CommsRemoteIpMulticastSourceFilterAddress3_Type()
)
pt3080CommsRemoteIpMulticastSourceFilterAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastSourceFilterAddress3.setStatus("current")
_Pt3080CommsRemoteIpMulticastSourceFilterAddress4_Type = IpAddress
_Pt3080CommsRemoteIpMulticastSourceFilterAddress4_Object = MibScalar
pt3080CommsRemoteIpMulticastSourceFilterAddress4 = _Pt3080CommsRemoteIpMulticastSourceFilterAddress4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 223),
    _Pt3080CommsRemoteIpMulticastSourceFilterAddress4_Type()
)
pt3080CommsRemoteIpMulticastSourceFilterAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastSourceFilterAddress4.setStatus("current")
_Pt3080CommsRemoteIpMulticastSourceFilterAddress5_Type = IpAddress
_Pt3080CommsRemoteIpMulticastSourceFilterAddress5_Object = MibScalar
pt3080CommsRemoteIpMulticastSourceFilterAddress5 = _Pt3080CommsRemoteIpMulticastSourceFilterAddress5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 224),
    _Pt3080CommsRemoteIpMulticastSourceFilterAddress5_Type()
)
pt3080CommsRemoteIpMulticastSourceFilterAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastSourceFilterAddress5.setStatus("current")
_Pt3080CommsRemoteIpMulticastSourceFilterAddress6_Type = IpAddress
_Pt3080CommsRemoteIpMulticastSourceFilterAddress6_Object = MibScalar
pt3080CommsRemoteIpMulticastSourceFilterAddress6 = _Pt3080CommsRemoteIpMulticastSourceFilterAddress6_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 225),
    _Pt3080CommsRemoteIpMulticastSourceFilterAddress6_Type()
)
pt3080CommsRemoteIpMulticastSourceFilterAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsRemoteIpMulticastSourceFilterAddress6.setStatus("current")
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress1_Type = IpAddress
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress1_Object = MibScalar
pt3080CommsGbeAdminIpMulticastSourceFilterAddress1 = _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 230),
    _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress1_Type()
)
pt3080CommsGbeAdminIpMulticastSourceFilterAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastSourceFilterAddress1.setStatus("current")
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress2_Type = IpAddress
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress2_Object = MibScalar
pt3080CommsGbeAdminIpMulticastSourceFilterAddress2 = _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 231),
    _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress2_Type()
)
pt3080CommsGbeAdminIpMulticastSourceFilterAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastSourceFilterAddress2.setStatus("current")
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress3_Type = IpAddress
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress3_Object = MibScalar
pt3080CommsGbeAdminIpMulticastSourceFilterAddress3 = _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 232),
    _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress3_Type()
)
pt3080CommsGbeAdminIpMulticastSourceFilterAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastSourceFilterAddress3.setStatus("current")
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress4_Type = IpAddress
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress4_Object = MibScalar
pt3080CommsGbeAdminIpMulticastSourceFilterAddress4 = _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 233),
    _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress4_Type()
)
pt3080CommsGbeAdminIpMulticastSourceFilterAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastSourceFilterAddress4.setStatus("current")
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress5_Type = IpAddress
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress5_Object = MibScalar
pt3080CommsGbeAdminIpMulticastSourceFilterAddress5 = _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 234),
    _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress5_Type()
)
pt3080CommsGbeAdminIpMulticastSourceFilterAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastSourceFilterAddress5.setStatus("current")
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress6_Type = IpAddress
_Pt3080CommsGbeAdminIpMulticastSourceFilterAddress6_Object = MibScalar
pt3080CommsGbeAdminIpMulticastSourceFilterAddress6 = _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress6_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 235),
    _Pt3080CommsGbeAdminIpMulticastSourceFilterAddress6_Type()
)
pt3080CommsGbeAdminIpMulticastSourceFilterAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsGbeAdminIpMulticastSourceFilterAddress6.setStatus("current")
_Pt3080CommsStaticRouteTable_Object = MibTable
pt3080CommsStaticRouteTable = _Pt3080CommsStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300)
)
if mibBuilder.loadTexts:
    pt3080CommsStaticRouteTable.setStatus("current")
_Pt3080CommsStaticRouteEntry_Object = MibTableRow
pt3080CommsStaticRouteEntry = _Pt3080CommsStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300, 1)
)
pt3080CommsStaticRouteEntry.setIndexNames(
    (0, "PT3080-MIB", "pt3080CommsStaticRouteNO"),
)
if mibBuilder.loadTexts:
    pt3080CommsStaticRouteEntry.setStatus("current")


class _Pt3080CommsStaticRouteNO_Type(Integer32):
    """Custom type pt3080CommsStaticRouteNO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pt3080CommsStaticRouteNO_Type.__name__ = "Integer32"
_Pt3080CommsStaticRouteNO_Object = MibTableColumn
pt3080CommsStaticRouteNO = _Pt3080CommsStaticRouteNO_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300, 1, 1),
    _Pt3080CommsStaticRouteNO_Type()
)
pt3080CommsStaticRouteNO.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pt3080CommsStaticRouteNO.setStatus("current")


class _Pt3080CommsStaticRouteType_Type(Integer32):
    """Custom type pt3080CommsStaticRouteType based on Integer32"""
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
        *(("unused", 0),
          ("normal", 1),
          ("physicalif", 2),
          ("recursive", 3),
          ("drop", 4))
    )


_Pt3080CommsStaticRouteType_Type.__name__ = "Integer32"
_Pt3080CommsStaticRouteType_Object = MibTableColumn
pt3080CommsStaticRouteType = _Pt3080CommsStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300, 1, 2),
    _Pt3080CommsStaticRouteType_Type()
)
pt3080CommsStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticRouteType.setStatus("current")
_Pt3080CommsStaticRoutePrefix_Type = IpAddress
_Pt3080CommsStaticRoutePrefix_Object = MibTableColumn
pt3080CommsStaticRoutePrefix = _Pt3080CommsStaticRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300, 1, 3),
    _Pt3080CommsStaticRoutePrefix_Type()
)
pt3080CommsStaticRoutePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticRoutePrefix.setStatus("current")


class _Pt3080CommsStaticRoutePrefixSize_Type(Integer32):
    """Custom type pt3080CommsStaticRoutePrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Pt3080CommsStaticRoutePrefixSize_Type.__name__ = "Integer32"
_Pt3080CommsStaticRoutePrefixSize_Object = MibTableColumn
pt3080CommsStaticRoutePrefixSize = _Pt3080CommsStaticRoutePrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300, 1, 4),
    _Pt3080CommsStaticRoutePrefixSize_Type()
)
pt3080CommsStaticRoutePrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticRoutePrefixSize.setStatus("current")
_Pt3080CommsStaticRouteTarget_Type = IpAddress
_Pt3080CommsStaticRouteTarget_Object = MibTableColumn
pt3080CommsStaticRouteTarget = _Pt3080CommsStaticRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300, 1, 5),
    _Pt3080CommsStaticRouteTarget_Type()
)
pt3080CommsStaticRouteTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticRouteTarget.setStatus("current")


class _Pt3080CommsStaticRoutePhysicalInterface_Type(Integer32):
    """Custom type pt3080CommsStaticRoutePhysicalInterface based on Integer32"""
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
        *(("eth0", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4))
    )


_Pt3080CommsStaticRoutePhysicalInterface_Type.__name__ = "Integer32"
_Pt3080CommsStaticRoutePhysicalInterface_Object = MibTableColumn
pt3080CommsStaticRoutePhysicalInterface = _Pt3080CommsStaticRoutePhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 300, 1, 6),
    _Pt3080CommsStaticRoutePhysicalInterface_Type()
)
pt3080CommsStaticRoutePhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsStaticRoutePhysicalInterface.setStatus("current")
_Pt3080CommsSNMPTrapDestination2_Type = DisplayString
_Pt3080CommsSNMPTrapDestination2_Object = MibScalar
pt3080CommsSNMPTrapDestination2 = _Pt3080CommsSNMPTrapDestination2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 419),
    _Pt3080CommsSNMPTrapDestination2_Type()
)
pt3080CommsSNMPTrapDestination2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestination2.setStatus("current")


class _Pt3080CommsSNMPTrapDestinationPort2_Type(Integer32):
    """Custom type pt3080CommsSNMPTrapDestinationPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsSNMPTrapDestinationPort2_Type.__name__ = "Integer32"
_Pt3080CommsSNMPTrapDestinationPort2_Object = MibScalar
pt3080CommsSNMPTrapDestinationPort2 = _Pt3080CommsSNMPTrapDestinationPort2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 420),
    _Pt3080CommsSNMPTrapDestinationPort2_Type()
)
pt3080CommsSNMPTrapDestinationPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestinationPort2.setStatus("current")
_Pt3080CommsSNMPTrapDestination3_Type = DisplayString
_Pt3080CommsSNMPTrapDestination3_Object = MibScalar
pt3080CommsSNMPTrapDestination3 = _Pt3080CommsSNMPTrapDestination3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 779),
    _Pt3080CommsSNMPTrapDestination3_Type()
)
pt3080CommsSNMPTrapDestination3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestination3.setStatus("current")


class _Pt3080CommsSNMPTrapDestinationPort3_Type(Integer32):
    """Custom type pt3080CommsSNMPTrapDestinationPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsSNMPTrapDestinationPort3_Type.__name__ = "Integer32"
_Pt3080CommsSNMPTrapDestinationPort3_Object = MibScalar
pt3080CommsSNMPTrapDestinationPort3 = _Pt3080CommsSNMPTrapDestinationPort3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 780),
    _Pt3080CommsSNMPTrapDestinationPort3_Type()
)
pt3080CommsSNMPTrapDestinationPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestinationPort3.setStatus("current")
_Pt3080CommsSNMPTrapDestination4_Type = DisplayString
_Pt3080CommsSNMPTrapDestination4_Object = MibScalar
pt3080CommsSNMPTrapDestination4 = _Pt3080CommsSNMPTrapDestination4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 1139),
    _Pt3080CommsSNMPTrapDestination4_Type()
)
pt3080CommsSNMPTrapDestination4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestination4.setStatus("current")


class _Pt3080CommsSNMPTrapDestinationPort4_Type(Integer32):
    """Custom type pt3080CommsSNMPTrapDestinationPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsSNMPTrapDestinationPort4_Type.__name__ = "Integer32"
_Pt3080CommsSNMPTrapDestinationPort4_Object = MibScalar
pt3080CommsSNMPTrapDestinationPort4 = _Pt3080CommsSNMPTrapDestinationPort4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 1140),
    _Pt3080CommsSNMPTrapDestinationPort4_Type()
)
pt3080CommsSNMPTrapDestinationPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestinationPort4.setStatus("current")
_Pt3080CommsSNMPTrapDestination5_Type = DisplayString
_Pt3080CommsSNMPTrapDestination5_Object = MibScalar
pt3080CommsSNMPTrapDestination5 = _Pt3080CommsSNMPTrapDestination5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 1499),
    _Pt3080CommsSNMPTrapDestination5_Type()
)
pt3080CommsSNMPTrapDestination5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestination5.setStatus("current")


class _Pt3080CommsSNMPTrapDestinationPort5_Type(Integer32):
    """Custom type pt3080CommsSNMPTrapDestinationPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pt3080CommsSNMPTrapDestinationPort5_Type.__name__ = "Integer32"
_Pt3080CommsSNMPTrapDestinationPort5_Object = MibScalar
pt3080CommsSNMPTrapDestinationPort5 = _Pt3080CommsSNMPTrapDestinationPort5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 1500),
    _Pt3080CommsSNMPTrapDestinationPort5_Type()
)
pt3080CommsSNMPTrapDestinationPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsSNMPTrapDestinationPort5.setStatus("current")


class _Pt3080CommsPortDhcpMode_Type(Integer32):
    """Custom type pt3080CommsPortDhcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("client", 1))
    )


_Pt3080CommsPortDhcpMode_Type.__name__ = "Integer32"
_Pt3080CommsPortDhcpMode_Object = MibScalar
pt3080CommsPortDhcpMode = _Pt3080CommsPortDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2075),
    _Pt3080CommsPortDhcpMode_Type()
)
pt3080CommsPortDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortDhcpMode.setStatus("current")


class _Pt3080CommsPortPhysicalInterface_Type(Integer32):
    """Custom type pt3080CommsPortPhysicalInterface based on Integer32"""
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
        *(("eth0", 0),
          ("eth1", 1),
          ("eth2", 2),
          ("eth3", 3),
          ("eth4", 4))
    )


_Pt3080CommsPortPhysicalInterface_Type.__name__ = "Integer32"
_Pt3080CommsPortPhysicalInterface_Object = MibScalar
pt3080CommsPortPhysicalInterface = _Pt3080CommsPortPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2151),
    _Pt3080CommsPortPhysicalInterface_Type()
)
pt3080CommsPortPhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortPhysicalInterface.setStatus("current")
_Pt3080CommsPortStaticIpAddr_Type = IpAddress
_Pt3080CommsPortStaticIpAddr_Object = MibScalar
pt3080CommsPortStaticIpAddr = _Pt3080CommsPortStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2152),
    _Pt3080CommsPortStaticIpAddr_Type()
)
pt3080CommsPortStaticIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortStaticIpAddr.setStatus("current")
_Pt3080CommsPortStaticNetmask_Type = IpAddress
_Pt3080CommsPortStaticNetmask_Object = MibScalar
pt3080CommsPortStaticNetmask = _Pt3080CommsPortStaticNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2153),
    _Pt3080CommsPortStaticNetmask_Type()
)
pt3080CommsPortStaticNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortStaticNetmask.setStatus("current")
_Pt3080CommsPortIpMulticastAddr_Type = IpAddress
_Pt3080CommsPortIpMulticastAddr_Object = MibScalar
pt3080CommsPortIpMulticastAddr = _Pt3080CommsPortIpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2154),
    _Pt3080CommsPortIpMulticastAddr_Type()
)
pt3080CommsPortIpMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastAddr.setStatus("current")


class _Pt3080CommsPortVlanEnable_Type(Integer32):
    """Custom type pt3080CommsPortVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsPortVlanEnable_Type.__name__ = "Integer32"
_Pt3080CommsPortVlanEnable_Object = MibScalar
pt3080CommsPortVlanEnable = _Pt3080CommsPortVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2155),
    _Pt3080CommsPortVlanEnable_Type()
)
pt3080CommsPortVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortVlanEnable.setStatus("current")


class _Pt3080CommsPortVlanId_Type(Integer32):
    """Custom type pt3080CommsPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Pt3080CommsPortVlanId_Type.__name__ = "Integer32"
_Pt3080CommsPortVlanId_Object = MibScalar
pt3080CommsPortVlanId = _Pt3080CommsPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2156),
    _Pt3080CommsPortVlanId_Type()
)
pt3080CommsPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortVlanId.setStatus("current")


class _Pt3080CommsPortServiceSNMP_Type(Integer32):
    """Custom type pt3080CommsPortServiceSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsPortServiceSNMP_Type.__name__ = "Integer32"
_Pt3080CommsPortServiceSNMP_Object = MibScalar
pt3080CommsPortServiceSNMP = _Pt3080CommsPortServiceSNMP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2157),
    _Pt3080CommsPortServiceSNMP_Type()
)
pt3080CommsPortServiceSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortServiceSNMP.setStatus("current")


class _Pt3080CommsPortServiceSCPI_Type(Integer32):
    """Custom type pt3080CommsPortServiceSCPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsPortServiceSCPI_Type.__name__ = "Integer32"
_Pt3080CommsPortServiceSCPI_Object = MibScalar
pt3080CommsPortServiceSCPI = _Pt3080CommsPortServiceSCPI_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2158),
    _Pt3080CommsPortServiceSCPI_Type()
)
pt3080CommsPortServiceSCPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortServiceSCPI.setStatus("current")


class _Pt3080CommsPortServiceTSoIP_Type(Integer32):
    """Custom type pt3080CommsPortServiceTSoIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsPortServiceTSoIP_Type.__name__ = "Integer32"
_Pt3080CommsPortServiceTSoIP_Object = MibScalar
pt3080CommsPortServiceTSoIP = _Pt3080CommsPortServiceTSoIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2159),
    _Pt3080CommsPortServiceTSoIP_Type()
)
pt3080CommsPortServiceTSoIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortServiceTSoIP.setStatus("current")


class _Pt3080CommsPortServiceWeb_Type(Integer32):
    """Custom type pt3080CommsPortServiceWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsPortServiceWeb_Type.__name__ = "Integer32"
_Pt3080CommsPortServiceWeb_Object = MibScalar
pt3080CommsPortServiceWeb = _Pt3080CommsPortServiceWeb_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2160),
    _Pt3080CommsPortServiceWeb_Type()
)
pt3080CommsPortServiceWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortServiceWeb.setStatus("current")


class _Pt3080CommsPortServiceRIP_Type(Integer32):
    """Custom type pt3080CommsPortServiceRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsPortServiceRIP_Type.__name__ = "Integer32"
_Pt3080CommsPortServiceRIP_Object = MibScalar
pt3080CommsPortServiceRIP = _Pt3080CommsPortServiceRIP_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2161),
    _Pt3080CommsPortServiceRIP_Type()
)
pt3080CommsPortServiceRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortServiceRIP.setStatus("current")
_Pt3080CommsPortCurrentIpAddr_Type = IpAddress
_Pt3080CommsPortCurrentIpAddr_Object = MibScalar
pt3080CommsPortCurrentIpAddr = _Pt3080CommsPortCurrentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2162),
    _Pt3080CommsPortCurrentIpAddr_Type()
)
pt3080CommsPortCurrentIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsPortCurrentIpAddr.setStatus("current")
_Pt3080CommsPortCurrentNetmask_Type = IpAddress
_Pt3080CommsPortCurrentNetmask_Object = MibScalar
pt3080CommsPortCurrentNetmask = _Pt3080CommsPortCurrentNetmask_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2163),
    _Pt3080CommsPortCurrentNetmask_Type()
)
pt3080CommsPortCurrentNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080CommsPortCurrentNetmask.setStatus("current")
_Pt3080CommsPortIpMulticastSourceFilterAddress1_Type = IpAddress
_Pt3080CommsPortIpMulticastSourceFilterAddress1_Object = MibScalar
pt3080CommsPortIpMulticastSourceFilterAddress1 = _Pt3080CommsPortIpMulticastSourceFilterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2170),
    _Pt3080CommsPortIpMulticastSourceFilterAddress1_Type()
)
pt3080CommsPortIpMulticastSourceFilterAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastSourceFilterAddress1.setStatus("current")
_Pt3080CommsPortIpMulticastSourceFilterAddress2_Type = IpAddress
_Pt3080CommsPortIpMulticastSourceFilterAddress2_Object = MibScalar
pt3080CommsPortIpMulticastSourceFilterAddress2 = _Pt3080CommsPortIpMulticastSourceFilterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2171),
    _Pt3080CommsPortIpMulticastSourceFilterAddress2_Type()
)
pt3080CommsPortIpMulticastSourceFilterAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastSourceFilterAddress2.setStatus("current")
_Pt3080CommsPortIpMulticastSourceFilterAddress3_Type = IpAddress
_Pt3080CommsPortIpMulticastSourceFilterAddress3_Object = MibScalar
pt3080CommsPortIpMulticastSourceFilterAddress3 = _Pt3080CommsPortIpMulticastSourceFilterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2172),
    _Pt3080CommsPortIpMulticastSourceFilterAddress3_Type()
)
pt3080CommsPortIpMulticastSourceFilterAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastSourceFilterAddress3.setStatus("current")
_Pt3080CommsPortIpMulticastSourceFilterAddress4_Type = IpAddress
_Pt3080CommsPortIpMulticastSourceFilterAddress4_Object = MibScalar
pt3080CommsPortIpMulticastSourceFilterAddress4 = _Pt3080CommsPortIpMulticastSourceFilterAddress4_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2173),
    _Pt3080CommsPortIpMulticastSourceFilterAddress4_Type()
)
pt3080CommsPortIpMulticastSourceFilterAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastSourceFilterAddress4.setStatus("current")
_Pt3080CommsPortIpMulticastSourceFilterAddress5_Type = IpAddress
_Pt3080CommsPortIpMulticastSourceFilterAddress5_Object = MibScalar
pt3080CommsPortIpMulticastSourceFilterAddress5 = _Pt3080CommsPortIpMulticastSourceFilterAddress5_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2174),
    _Pt3080CommsPortIpMulticastSourceFilterAddress5_Type()
)
pt3080CommsPortIpMulticastSourceFilterAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastSourceFilterAddress5.setStatus("current")
_Pt3080CommsPortIpMulticastSourceFilterAddress6_Type = IpAddress
_Pt3080CommsPortIpMulticastSourceFilterAddress6_Object = MibScalar
pt3080CommsPortIpMulticastSourceFilterAddress6 = _Pt3080CommsPortIpMulticastSourceFilterAddress6_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2175),
    _Pt3080CommsPortIpMulticastSourceFilterAddress6_Type()
)
pt3080CommsPortIpMulticastSourceFilterAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastSourceFilterAddress6.setStatus("current")


class _Pt3080CommsPortIpMulticastSourceFilterMode_Type(Integer32):
    """Custom type pt3080CommsPortIpMulticastSourceFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfinclude", 0),
          ("sfexclude", 1))
    )


_Pt3080CommsPortIpMulticastSourceFilterMode_Type.__name__ = "Integer32"
_Pt3080CommsPortIpMulticastSourceFilterMode_Object = MibScalar
pt3080CommsPortIpMulticastSourceFilterMode = _Pt3080CommsPortIpMulticastSourceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2193),
    _Pt3080CommsPortIpMulticastSourceFilterMode_Type()
)
pt3080CommsPortIpMulticastSourceFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortIpMulticastSourceFilterMode.setStatus("current")


class _Pt3080CommsPortEnable_Type(Integer32):
    """Custom type pt3080CommsPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080CommsPortEnable_Type.__name__ = "Integer32"
_Pt3080CommsPortEnable_Object = MibScalar
pt3080CommsPortEnable = _Pt3080CommsPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 17, 2500),
    _Pt3080CommsPortEnable_Type()
)
pt3080CommsPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080CommsPortEnable.setStatus("current")
_Pt3080Demodulator_ObjectIdentity = ObjectIdentity
pt3080Demodulator = _Pt3080Demodulator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24)
)


class _Pt3080DemodulatorFollowMode_Type(Integer32):
    """Custom type pt3080DemodulatorFollowMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080DemodulatorFollowMode_Type.__name__ = "Integer32"
_Pt3080DemodulatorFollowMode_Object = MibScalar
pt3080DemodulatorFollowMode = _Pt3080DemodulatorFollowMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 1),
    _Pt3080DemodulatorFollowMode_Type()
)
pt3080DemodulatorFollowMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080DemodulatorFollowMode.setStatus("current")


class _Pt3080Demodulator1Available_Type(Integer32):
    """Custom type pt3080Demodulator1Available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080Demodulator1Available_Type.__name__ = "Integer32"
_Pt3080Demodulator1Available_Object = MibScalar
pt3080Demodulator1Available = _Pt3080Demodulator1Available_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 2),
    _Pt3080Demodulator1Available_Type()
)
pt3080Demodulator1Available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1Available.setStatus("current")
_Pt3080Demodulator1FWVersion_Type = DisplayString
_Pt3080Demodulator1FWVersion_Object = MibScalar
pt3080Demodulator1FWVersion = _Pt3080Demodulator1FWVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 3),
    _Pt3080Demodulator1FWVersion_Type()
)
pt3080Demodulator1FWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1FWVersion.setStatus("current")


class _Pt3080Demodulator1OutputTS_Type(Integer32):
    """Custom type pt3080Demodulator1OutputTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hp", 0),
          ("lp", 1))
    )


_Pt3080Demodulator1OutputTS_Type.__name__ = "Integer32"
_Pt3080Demodulator1OutputTS_Object = MibScalar
pt3080Demodulator1OutputTS = _Pt3080Demodulator1OutputTS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 4),
    _Pt3080Demodulator1OutputTS_Type()
)
pt3080Demodulator1OutputTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator1OutputTS.setStatus("current")


class _Pt3080Demodulator1MerLimit_Type(Integer32):
    """Custom type pt3080Demodulator1MerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 240),
    )


_Pt3080Demodulator1MerLimit_Type.__name__ = "Integer32"
_Pt3080Demodulator1MerLimit_Object = MibScalar
pt3080Demodulator1MerLimit = _Pt3080Demodulator1MerLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 5),
    _Pt3080Demodulator1MerLimit_Type()
)
pt3080Demodulator1MerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator1MerLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator1MerLimit.setUnits("0.1 dBm")


class _Pt3080Demodulator1PreVirterbiErrorRateLimit_Type(Integer32):
    """Custom type pt3080Demodulator1PreVirterbiErrorRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Pt3080Demodulator1PreVirterbiErrorRateLimit_Type.__name__ = "Integer32"
_Pt3080Demodulator1PreVirterbiErrorRateLimit_Object = MibScalar
pt3080Demodulator1PreVirterbiErrorRateLimit = _Pt3080Demodulator1PreVirterbiErrorRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 6),
    _Pt3080Demodulator1PreVirterbiErrorRateLimit_Type()
)
pt3080Demodulator1PreVirterbiErrorRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator1PreVirterbiErrorRateLimit.setStatus("current")


class _Pt3080Demodulator1PostVirterbiErrorRateLimit_Type(Integer32):
    """Custom type pt3080Demodulator1PostVirterbiErrorRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Pt3080Demodulator1PostVirterbiErrorRateLimit_Type.__name__ = "Integer32"
_Pt3080Demodulator1PostVirterbiErrorRateLimit_Object = MibScalar
pt3080Demodulator1PostVirterbiErrorRateLimit = _Pt3080Demodulator1PostVirterbiErrorRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 7),
    _Pt3080Demodulator1PostVirterbiErrorRateLimit_Type()
)
pt3080Demodulator1PostVirterbiErrorRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator1PostVirterbiErrorRateLimit.setStatus("current")


class _Pt3080Demodulator1FelStatus_Type(Integer32):
    """Custom type pt3080Demodulator1FelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Pt3080Demodulator1FelStatus_Type.__name__ = "Integer32"
_Pt3080Demodulator1FelStatus_Object = MibScalar
pt3080Demodulator1FelStatus = _Pt3080Demodulator1FelStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 8),
    _Pt3080Demodulator1FelStatus_Type()
)
pt3080Demodulator1FelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1FelStatus.setStatus("current")
_Pt3080Demodulator1UncorrectedPackets_Type = Integer32
_Pt3080Demodulator1UncorrectedPackets_Object = MibScalar
pt3080Demodulator1UncorrectedPackets = _Pt3080Demodulator1UncorrectedPackets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 9),
    _Pt3080Demodulator1UncorrectedPackets_Type()
)
pt3080Demodulator1UncorrectedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1UncorrectedPackets.setStatus("current")
_Pt3080Demodulator1Mer_Type = Integer32
_Pt3080Demodulator1Mer_Object = MibScalar
pt3080Demodulator1Mer = _Pt3080Demodulator1Mer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 11),
    _Pt3080Demodulator1Mer_Type()
)
pt3080Demodulator1Mer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1Mer.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator1Mer.setUnits("0.1 dBm")
_Pt3080Demodulator1PreVirterbiErrorRate_Type = Integer32
_Pt3080Demodulator1PreVirterbiErrorRate_Object = MibScalar
pt3080Demodulator1PreVirterbiErrorRate = _Pt3080Demodulator1PreVirterbiErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 12),
    _Pt3080Demodulator1PreVirterbiErrorRate_Type()
)
pt3080Demodulator1PreVirterbiErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1PreVirterbiErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator1PreVirterbiErrorRate.setUnits("0.1 x1e-7")
_Pt3080Demodulator1PostVirterbiErrorRate_Type = Integer32
_Pt3080Demodulator1PostVirterbiErrorRate_Object = MibScalar
pt3080Demodulator1PostVirterbiErrorRate = _Pt3080Demodulator1PostVirterbiErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 13),
    _Pt3080Demodulator1PostVirterbiErrorRate_Type()
)
pt3080Demodulator1PostVirterbiErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1PostVirterbiErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator1PostVirterbiErrorRate.setUnits("0.1 x1e-7")


class _Pt3080Demodulator1ActualGuardInterval_Type(Integer32):
    """Custom type pt3080Demodulator1ActualGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g1-32", 0),
          ("g1-16", 1),
          ("g1-8", 2),
          ("g1-4", 3))
    )


_Pt3080Demodulator1ActualGuardInterval_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualGuardInterval_Object = MibScalar
pt3080Demodulator1ActualGuardInterval = _Pt3080Demodulator1ActualGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 14),
    _Pt3080Demodulator1ActualGuardInterval_Type()
)
pt3080Demodulator1ActualGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualGuardInterval.setStatus("current")


class _Pt3080Demodulator1Actualifft_Type(Integer32):
    """Custom type pt3080Demodulator1Actualifft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f2k", 0),
          ("f4k", 1),
          ("f8k", 2))
    )


_Pt3080Demodulator1Actualifft_Type.__name__ = "Integer32"
_Pt3080Demodulator1Actualifft_Object = MibScalar
pt3080Demodulator1Actualifft = _Pt3080Demodulator1Actualifft_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 15),
    _Pt3080Demodulator1Actualifft_Type()
)
pt3080Demodulator1Actualifft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1Actualifft.setStatus("current")


class _Pt3080Demodulator1ActualConstellation_Type(Integer32):
    """Custom type pt3080Demodulator1ActualConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qpsk", 0),
          ("qam16", 1),
          ("qam64", 2))
    )


_Pt3080Demodulator1ActualConstellation_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualConstellation_Object = MibScalar
pt3080Demodulator1ActualConstellation = _Pt3080Demodulator1ActualConstellation_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 16),
    _Pt3080Demodulator1ActualConstellation_Type()
)
pt3080Demodulator1ActualConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualConstellation.setStatus("current")


class _Pt3080Demodulator1ActualHierarchy_Type(Integer32):
    """Custom type pt3080Demodulator1ActualHierarchy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("h-1", 1),
          ("h-2", 2),
          ("h-4", 3))
    )


_Pt3080Demodulator1ActualHierarchy_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualHierarchy_Object = MibScalar
pt3080Demodulator1ActualHierarchy = _Pt3080Demodulator1ActualHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 17),
    _Pt3080Demodulator1ActualHierarchy_Type()
)
pt3080Demodulator1ActualHierarchy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualHierarchy.setStatus("current")


class _Pt3080Demodulator1ActualCodeRateHighPrio_Type(Integer32):
    """Custom type pt3080Demodulator1ActualCodeRateHighPrio based on Integer32"""
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
        *(("r1-2", 0),
          ("r2-3", 1),
          ("r3-4", 2),
          ("r5-6", 3),
          ("r7-8", 4))
    )


_Pt3080Demodulator1ActualCodeRateHighPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualCodeRateHighPrio_Object = MibScalar
pt3080Demodulator1ActualCodeRateHighPrio = _Pt3080Demodulator1ActualCodeRateHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 18),
    _Pt3080Demodulator1ActualCodeRateHighPrio_Type()
)
pt3080Demodulator1ActualCodeRateHighPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualCodeRateHighPrio.setStatus("current")


class _Pt3080Demodulator1ActualCodeRateLowPrio_Type(Integer32):
    """Custom type pt3080Demodulator1ActualCodeRateLowPrio based on Integer32"""
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
        *(("r1-2", 0),
          ("r2-3", 1),
          ("r3-4", 2),
          ("r5-6", 3),
          ("r7-8", 4))
    )


_Pt3080Demodulator1ActualCodeRateLowPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualCodeRateLowPrio_Object = MibScalar
pt3080Demodulator1ActualCodeRateLowPrio = _Pt3080Demodulator1ActualCodeRateLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 19),
    _Pt3080Demodulator1ActualCodeRateLowPrio_Type()
)
pt3080Demodulator1ActualCodeRateLowPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualCodeRateLowPrio.setStatus("current")


class _Pt3080Demodulator1ActualDeepInterleaver_Type(Integer32):
    """Custom type pt3080Demodulator1ActualDeepInterleaver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator1ActualDeepInterleaver_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualDeepInterleaver_Object = MibScalar
pt3080Demodulator1ActualDeepInterleaver = _Pt3080Demodulator1ActualDeepInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 20),
    _Pt3080Demodulator1ActualDeepInterleaver_Type()
)
pt3080Demodulator1ActualDeepInterleaver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualDeepInterleaver.setStatus("current")


class _Pt3080Demodulator1ActualMpeFecHighPrio_Type(Integer32):
    """Custom type pt3080Demodulator1ActualMpeFecHighPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator1ActualMpeFecHighPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualMpeFecHighPrio_Object = MibScalar
pt3080Demodulator1ActualMpeFecHighPrio = _Pt3080Demodulator1ActualMpeFecHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 21),
    _Pt3080Demodulator1ActualMpeFecHighPrio_Type()
)
pt3080Demodulator1ActualMpeFecHighPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualMpeFecHighPrio.setStatus("current")


class _Pt3080Demodulator1ActualMpeFecLowPrio_Type(Integer32):
    """Custom type pt3080Demodulator1ActualMpeFecLowPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator1ActualMpeFecLowPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualMpeFecLowPrio_Object = MibScalar
pt3080Demodulator1ActualMpeFecLowPrio = _Pt3080Demodulator1ActualMpeFecLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 22),
    _Pt3080Demodulator1ActualMpeFecLowPrio_Type()
)
pt3080Demodulator1ActualMpeFecLowPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualMpeFecLowPrio.setStatus("current")


class _Pt3080Demodulator1ActualTimeSlicingHighPrio_Type(Integer32):
    """Custom type pt3080Demodulator1ActualTimeSlicingHighPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator1ActualTimeSlicingHighPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualTimeSlicingHighPrio_Object = MibScalar
pt3080Demodulator1ActualTimeSlicingHighPrio = _Pt3080Demodulator1ActualTimeSlicingHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 23),
    _Pt3080Demodulator1ActualTimeSlicingHighPrio_Type()
)
pt3080Demodulator1ActualTimeSlicingHighPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualTimeSlicingHighPrio.setStatus("current")


class _Pt3080Demodulator1ActualTimeSlicingLowPrio_Type(Integer32):
    """Custom type pt3080Demodulator1ActualTimeSlicingLowPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator1ActualTimeSlicingLowPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualTimeSlicingLowPrio_Object = MibScalar
pt3080Demodulator1ActualTimeSlicingLowPrio = _Pt3080Demodulator1ActualTimeSlicingLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 24),
    _Pt3080Demodulator1ActualTimeSlicingLowPrio_Type()
)
pt3080Demodulator1ActualTimeSlicingLowPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualTimeSlicingLowPrio.setStatus("current")
_Pt3080Demodulator1ActualCellID_Type = Integer32
_Pt3080Demodulator1ActualCellID_Object = MibScalar
pt3080Demodulator1ActualCellID = _Pt3080Demodulator1ActualCellID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 25),
    _Pt3080Demodulator1ActualCellID_Type()
)
pt3080Demodulator1ActualCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualCellID.setStatus("current")


class _Pt3080Demodulator1ActualDVBHMode_Type(Integer32):
    """Custom type pt3080Demodulator1ActualDVBHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator1ActualDVBHMode_Type.__name__ = "Integer32"
_Pt3080Demodulator1ActualDVBHMode_Object = MibScalar
pt3080Demodulator1ActualDVBHMode = _Pt3080Demodulator1ActualDVBHMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 26),
    _Pt3080Demodulator1ActualDVBHMode_Type()
)
pt3080Demodulator1ActualDVBHMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator1ActualDVBHMode.setStatus("current")


class _Pt3080Demodulator2Available_Type(Integer32):
    """Custom type pt3080Demodulator2Available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080Demodulator2Available_Type.__name__ = "Integer32"
_Pt3080Demodulator2Available_Object = MibScalar
pt3080Demodulator2Available = _Pt3080Demodulator2Available_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 29),
    _Pt3080Demodulator2Available_Type()
)
pt3080Demodulator2Available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2Available.setStatus("current")
_Pt3080Demodulator2FWVersion_Type = DisplayString
_Pt3080Demodulator2FWVersion_Object = MibScalar
pt3080Demodulator2FWVersion = _Pt3080Demodulator2FWVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 30),
    _Pt3080Demodulator2FWVersion_Type()
)
pt3080Demodulator2FWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2FWVersion.setStatus("current")


class _Pt3080Demodulator2OutputTS_Type(Integer32):
    """Custom type pt3080Demodulator2OutputTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hp", 0),
          ("lp", 1))
    )


_Pt3080Demodulator2OutputTS_Type.__name__ = "Integer32"
_Pt3080Demodulator2OutputTS_Object = MibScalar
pt3080Demodulator2OutputTS = _Pt3080Demodulator2OutputTS_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 31),
    _Pt3080Demodulator2OutputTS_Type()
)
pt3080Demodulator2OutputTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator2OutputTS.setStatus("current")


class _Pt3080Demodulator2MerLimit_Type(Integer32):
    """Custom type pt3080Demodulator2MerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 240),
    )


_Pt3080Demodulator2MerLimit_Type.__name__ = "Integer32"
_Pt3080Demodulator2MerLimit_Object = MibScalar
pt3080Demodulator2MerLimit = _Pt3080Demodulator2MerLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 32),
    _Pt3080Demodulator2MerLimit_Type()
)
pt3080Demodulator2MerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator2MerLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator2MerLimit.setUnits("0.1 dBm")


class _Pt3080Demodulator2PreVirterbiErrorRateLimit_Type(Integer32):
    """Custom type pt3080Demodulator2PreVirterbiErrorRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Pt3080Demodulator2PreVirterbiErrorRateLimit_Type.__name__ = "Integer32"
_Pt3080Demodulator2PreVirterbiErrorRateLimit_Object = MibScalar
pt3080Demodulator2PreVirterbiErrorRateLimit = _Pt3080Demodulator2PreVirterbiErrorRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 33),
    _Pt3080Demodulator2PreVirterbiErrorRateLimit_Type()
)
pt3080Demodulator2PreVirterbiErrorRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator2PreVirterbiErrorRateLimit.setStatus("current")


class _Pt3080Demodulator2PostVirterbiErrorRateLimit_Type(Integer32):
    """Custom type pt3080Demodulator2PostVirterbiErrorRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Pt3080Demodulator2PostVirterbiErrorRateLimit_Type.__name__ = "Integer32"
_Pt3080Demodulator2PostVirterbiErrorRateLimit_Object = MibScalar
pt3080Demodulator2PostVirterbiErrorRateLimit = _Pt3080Demodulator2PostVirterbiErrorRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 34),
    _Pt3080Demodulator2PostVirterbiErrorRateLimit_Type()
)
pt3080Demodulator2PostVirterbiErrorRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080Demodulator2PostVirterbiErrorRateLimit.setStatus("current")


class _Pt3080Demodulator2FelStatus_Type(Integer32):
    """Custom type pt3080Demodulator2FelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Pt3080Demodulator2FelStatus_Type.__name__ = "Integer32"
_Pt3080Demodulator2FelStatus_Object = MibScalar
pt3080Demodulator2FelStatus = _Pt3080Demodulator2FelStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 35),
    _Pt3080Demodulator2FelStatus_Type()
)
pt3080Demodulator2FelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2FelStatus.setStatus("current")
_Pt3080Demodulator2UncorrectedPackets_Type = Integer32
_Pt3080Demodulator2UncorrectedPackets_Object = MibScalar
pt3080Demodulator2UncorrectedPackets = _Pt3080Demodulator2UncorrectedPackets_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 36),
    _Pt3080Demodulator2UncorrectedPackets_Type()
)
pt3080Demodulator2UncorrectedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2UncorrectedPackets.setStatus("current")
_Pt3080Demodulator2Mer_Type = Integer32
_Pt3080Demodulator2Mer_Object = MibScalar
pt3080Demodulator2Mer = _Pt3080Demodulator2Mer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 38),
    _Pt3080Demodulator2Mer_Type()
)
pt3080Demodulator2Mer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2Mer.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator2Mer.setUnits("0.1 dBm")
_Pt3080Demodulator2PreVirterbiErrorRate_Type = Integer32
_Pt3080Demodulator2PreVirterbiErrorRate_Object = MibScalar
pt3080Demodulator2PreVirterbiErrorRate = _Pt3080Demodulator2PreVirterbiErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 39),
    _Pt3080Demodulator2PreVirterbiErrorRate_Type()
)
pt3080Demodulator2PreVirterbiErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2PreVirterbiErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator2PreVirterbiErrorRate.setUnits("0.1 x1e-7")
_Pt3080Demodulator2PostVirterbiErrorRate_Type = Integer32
_Pt3080Demodulator2PostVirterbiErrorRate_Object = MibScalar
pt3080Demodulator2PostVirterbiErrorRate = _Pt3080Demodulator2PostVirterbiErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 40),
    _Pt3080Demodulator2PostVirterbiErrorRate_Type()
)
pt3080Demodulator2PostVirterbiErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2PostVirterbiErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080Demodulator2PostVirterbiErrorRate.setUnits("0.1 x1e-7")


class _Pt3080Demodulator2ActualGuardInterval_Type(Integer32):
    """Custom type pt3080Demodulator2ActualGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g1-32", 0),
          ("g1-16", 1),
          ("g1-8", 2),
          ("g1-4", 3))
    )


_Pt3080Demodulator2ActualGuardInterval_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualGuardInterval_Object = MibScalar
pt3080Demodulator2ActualGuardInterval = _Pt3080Demodulator2ActualGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 41),
    _Pt3080Demodulator2ActualGuardInterval_Type()
)
pt3080Demodulator2ActualGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualGuardInterval.setStatus("current")


class _Pt3080Demodulator2Actualifft_Type(Integer32):
    """Custom type pt3080Demodulator2Actualifft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f2k", 0),
          ("f4k", 1),
          ("f8k", 2))
    )


_Pt3080Demodulator2Actualifft_Type.__name__ = "Integer32"
_Pt3080Demodulator2Actualifft_Object = MibScalar
pt3080Demodulator2Actualifft = _Pt3080Demodulator2Actualifft_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 42),
    _Pt3080Demodulator2Actualifft_Type()
)
pt3080Demodulator2Actualifft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2Actualifft.setStatus("current")


class _Pt3080Demodulator2ActualConstellation_Type(Integer32):
    """Custom type pt3080Demodulator2ActualConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qpsk", 0),
          ("qam16", 1),
          ("qam64", 2))
    )


_Pt3080Demodulator2ActualConstellation_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualConstellation_Object = MibScalar
pt3080Demodulator2ActualConstellation = _Pt3080Demodulator2ActualConstellation_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 43),
    _Pt3080Demodulator2ActualConstellation_Type()
)
pt3080Demodulator2ActualConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualConstellation.setStatus("current")


class _Pt3080Demodulator2ActualHierarchy_Type(Integer32):
    """Custom type pt3080Demodulator2ActualHierarchy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("h-1", 1),
          ("h-2", 2),
          ("h-4", 3))
    )


_Pt3080Demodulator2ActualHierarchy_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualHierarchy_Object = MibScalar
pt3080Demodulator2ActualHierarchy = _Pt3080Demodulator2ActualHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 44),
    _Pt3080Demodulator2ActualHierarchy_Type()
)
pt3080Demodulator2ActualHierarchy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualHierarchy.setStatus("current")


class _Pt3080Demodulator2ActualCodeRateHighPrio_Type(Integer32):
    """Custom type pt3080Demodulator2ActualCodeRateHighPrio based on Integer32"""
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
        *(("r1-2", 0),
          ("r2-3", 1),
          ("r3-4", 2),
          ("r5-6", 3),
          ("r7-8", 4))
    )


_Pt3080Demodulator2ActualCodeRateHighPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualCodeRateHighPrio_Object = MibScalar
pt3080Demodulator2ActualCodeRateHighPrio = _Pt3080Demodulator2ActualCodeRateHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 45),
    _Pt3080Demodulator2ActualCodeRateHighPrio_Type()
)
pt3080Demodulator2ActualCodeRateHighPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualCodeRateHighPrio.setStatus("current")


class _Pt3080Demodulator2ActualCodeRateLowPrio_Type(Integer32):
    """Custom type pt3080Demodulator2ActualCodeRateLowPrio based on Integer32"""
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
        *(("r1-2", 0),
          ("r2-3", 1),
          ("r3-4", 2),
          ("r5-6", 3),
          ("r7-8", 4))
    )


_Pt3080Demodulator2ActualCodeRateLowPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualCodeRateLowPrio_Object = MibScalar
pt3080Demodulator2ActualCodeRateLowPrio = _Pt3080Demodulator2ActualCodeRateLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 46),
    _Pt3080Demodulator2ActualCodeRateLowPrio_Type()
)
pt3080Demodulator2ActualCodeRateLowPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualCodeRateLowPrio.setStatus("current")


class _Pt3080Demodulator2ActualDeepInterleaver_Type(Integer32):
    """Custom type pt3080Demodulator2ActualDeepInterleaver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator2ActualDeepInterleaver_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualDeepInterleaver_Object = MibScalar
pt3080Demodulator2ActualDeepInterleaver = _Pt3080Demodulator2ActualDeepInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 47),
    _Pt3080Demodulator2ActualDeepInterleaver_Type()
)
pt3080Demodulator2ActualDeepInterleaver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualDeepInterleaver.setStatus("current")


class _Pt3080Demodulator2ActualMpeFecHighPrio_Type(Integer32):
    """Custom type pt3080Demodulator2ActualMpeFecHighPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator2ActualMpeFecHighPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualMpeFecHighPrio_Object = MibScalar
pt3080Demodulator2ActualMpeFecHighPrio = _Pt3080Demodulator2ActualMpeFecHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 48),
    _Pt3080Demodulator2ActualMpeFecHighPrio_Type()
)
pt3080Demodulator2ActualMpeFecHighPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualMpeFecHighPrio.setStatus("current")


class _Pt3080Demodulator2ActualMpeFecLowPrio_Type(Integer32):
    """Custom type pt3080Demodulator2ActualMpeFecLowPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator2ActualMpeFecLowPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualMpeFecLowPrio_Object = MibScalar
pt3080Demodulator2ActualMpeFecLowPrio = _Pt3080Demodulator2ActualMpeFecLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 49),
    _Pt3080Demodulator2ActualMpeFecLowPrio_Type()
)
pt3080Demodulator2ActualMpeFecLowPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualMpeFecLowPrio.setStatus("current")


class _Pt3080Demodulator2ActualTimeSlicingHighPrio_Type(Integer32):
    """Custom type pt3080Demodulator2ActualTimeSlicingHighPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator2ActualTimeSlicingHighPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualTimeSlicingHighPrio_Object = MibScalar
pt3080Demodulator2ActualTimeSlicingHighPrio = _Pt3080Demodulator2ActualTimeSlicingHighPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 50),
    _Pt3080Demodulator2ActualTimeSlicingHighPrio_Type()
)
pt3080Demodulator2ActualTimeSlicingHighPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualTimeSlicingHighPrio.setStatus("current")


class _Pt3080Demodulator2ActualTimeSlicingLowPrio_Type(Integer32):
    """Custom type pt3080Demodulator2ActualTimeSlicingLowPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator2ActualTimeSlicingLowPrio_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualTimeSlicingLowPrio_Object = MibScalar
pt3080Demodulator2ActualTimeSlicingLowPrio = _Pt3080Demodulator2ActualTimeSlicingLowPrio_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 51),
    _Pt3080Demodulator2ActualTimeSlicingLowPrio_Type()
)
pt3080Demodulator2ActualTimeSlicingLowPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualTimeSlicingLowPrio.setStatus("current")
_Pt3080Demodulator2ActualCellID_Type = Integer32
_Pt3080Demodulator2ActualCellID_Object = MibScalar
pt3080Demodulator2ActualCellID = _Pt3080Demodulator2ActualCellID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 52),
    _Pt3080Demodulator2ActualCellID_Type()
)
pt3080Demodulator2ActualCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualCellID.setStatus("current")


class _Pt3080Demodulator2ActualDVBHMode_Type(Integer32):
    """Custom type pt3080Demodulator2ActualDVBHMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080Demodulator2ActualDVBHMode_Type.__name__ = "Integer32"
_Pt3080Demodulator2ActualDVBHMode_Object = MibScalar
pt3080Demodulator2ActualDVBHMode = _Pt3080Demodulator2ActualDVBHMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 24, 53),
    _Pt3080Demodulator2ActualDVBHMode_Type()
)
pt3080Demodulator2ActualDVBHMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080Demodulator2ActualDVBHMode.setStatus("current")
_Pt3080Precorrector_ObjectIdentity = ObjectIdentity
pt3080Precorrector = _Pt3080Precorrector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25)
)


class _Pt3080PrecorrectorLinearAdaptiveMode_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAdaptiveMode based on Integer32"""
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
        *(("idle", 0),
          ("autorun", 1),
          ("runtotarget", 2),
          ("continuous", 3),
          ("single", 4))
    )


_Pt3080PrecorrectorLinearAdaptiveMode_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAdaptiveMode_Object = MibScalar
pt3080PrecorrectorLinearAdaptiveMode = _Pt3080PrecorrectorLinearAdaptiveMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 1),
    _Pt3080PrecorrectorLinearAdaptiveMode_Type()
)
pt3080PrecorrectorLinearAdaptiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveMode.setStatus("current")


class _Pt3080PrecorrectorLinearMode_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitoring", 0),
          ("static", 1),
          ("adaptive", 2))
    )


_Pt3080PrecorrectorLinearMode_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearMode_Object = MibScalar
pt3080PrecorrectorLinearMode = _Pt3080PrecorrectorLinearMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 2),
    _Pt3080PrecorrectorLinearMode_Type()
)
pt3080PrecorrectorLinearMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMode.setStatus("current")


class _Pt3080PrecorrectorNonlinearAdaptiveMode_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveMode based on Integer32"""
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
        *(("idle", 0),
          ("autorun", 1),
          ("runtotarget", 2),
          ("continuous", 3),
          ("single", 4))
    )


_Pt3080PrecorrectorNonlinearAdaptiveMode_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveMode_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveMode = _Pt3080PrecorrectorNonlinearAdaptiveMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 3),
    _Pt3080PrecorrectorNonlinearAdaptiveMode_Type()
)
pt3080PrecorrectorNonlinearAdaptiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMode.setStatus("current")


class _Pt3080PrecorrectorNonlinearMode_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitoring", 0),
          ("static", 1),
          ("adaptive", 2))
    )


_Pt3080PrecorrectorNonlinearMode_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearMode_Object = MibScalar
pt3080PrecorrectorNonlinearMode = _Pt3080PrecorrectorNonlinearMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 4),
    _Pt3080PrecorrectorNonlinearMode_Type()
)
pt3080PrecorrectorNonlinearMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMode.setStatus("current")
_Pt3080PrecorrectorLastTurnAroundTime_Type = Integer32
_Pt3080PrecorrectorLastTurnAroundTime_Object = MibScalar
pt3080PrecorrectorLastTurnAroundTime = _Pt3080PrecorrectorLastTurnAroundTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 6),
    _Pt3080PrecorrectorLastTurnAroundTime_Type()
)
pt3080PrecorrectorLastTurnAroundTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLastTurnAroundTime.setStatus("current")
_Pt3080PrecorrectorSecondsSinceLastUpdate_Type = Integer32
_Pt3080PrecorrectorSecondsSinceLastUpdate_Object = MibScalar
pt3080PrecorrectorSecondsSinceLastUpdate = _Pt3080PrecorrectorSecondsSinceLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 7),
    _Pt3080PrecorrectorSecondsSinceLastUpdate_Type()
)
pt3080PrecorrectorSecondsSinceLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorSecondsSinceLastUpdate.setStatus("current")
_Pt3080PrecorrectorLinearMonitorSenseBadCount_Type = Integer32
_Pt3080PrecorrectorLinearMonitorSenseBadCount_Object = MibScalar
pt3080PrecorrectorLinearMonitorSenseBadCount = _Pt3080PrecorrectorLinearMonitorSenseBadCount_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 8),
    _Pt3080PrecorrectorLinearMonitorSenseBadCount_Type()
)
pt3080PrecorrectorLinearMonitorSenseBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorSenseBadCount.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorSenseBadCount_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorSenseBadCount_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorSenseBadCount = _Pt3080PrecorrectorNonlinearMonitorSenseBadCount_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 9),
    _Pt3080PrecorrectorNonlinearMonitorSenseBadCount_Type()
)
pt3080PrecorrectorNonlinearMonitorSenseBadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorSenseBadCount.setStatus("current")


class _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable_Object = MibScalar
pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable = _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 10),
    _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable_Type()
)
pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable.setStatus("current")


class _Pt3080PrecorrectorLinearAdaptiveGroupDelayEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAdaptiveGroupDelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080PrecorrectorLinearAdaptiveGroupDelayEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAdaptiveGroupDelayEnable_Object = MibScalar
pt3080PrecorrectorLinearAdaptiveGroupDelayEnable = _Pt3080PrecorrectorLinearAdaptiveGroupDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 11),
    _Pt3080PrecorrectorLinearAdaptiveGroupDelayEnable_Type()
)
pt3080PrecorrectorLinearAdaptiveGroupDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveGroupDelayEnable.setStatus("current")


class _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable = _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 12),
    _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable_Type()
)
pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable.setStatus("current")


class _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable = _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 13),
    _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable_Type()
)
pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable.setStatus("current")


class _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis_Object = MibScalar
pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis = _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 14),
    _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis_Type()
)
pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis.setUnits("0.01 dB")


class _Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis_Object = MibScalar
pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis = _Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 15),
    _Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis_Type()
)
pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis.setUnits("0.01 ns")


class _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis = _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 16),
    _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis_Type()
)
pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis.setUnits("0.01 dB")


class _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis = _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 17),
    _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis_Type()
)
pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis.setUnits("0.01 dB")
_Pt3080PrecorrectorLinCleanrun_Type = Integer32
_Pt3080PrecorrectorLinCleanrun_Object = MibScalar
pt3080PrecorrectorLinCleanrun = _Pt3080PrecorrectorLinCleanrun_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 18),
    _Pt3080PrecorrectorLinCleanrun_Type()
)
pt3080PrecorrectorLinCleanrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinCleanrun.setStatus("current")
_Pt3080PrecorrectorLinearMonitorIterations_Type = Integer32
_Pt3080PrecorrectorLinearMonitorIterations_Object = MibScalar
pt3080PrecorrectorLinearMonitorIterations = _Pt3080PrecorrectorLinearMonitorIterations_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 19),
    _Pt3080PrecorrectorLinearMonitorIterations_Type()
)
pt3080PrecorrectorLinearMonitorIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorIterations.setStatus("current")


class _Pt3080PrecorrectorLinearLoadNeutral_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearLoadNeutral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("load", 1))
    )


_Pt3080PrecorrectorLinearLoadNeutral_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearLoadNeutral_Object = MibScalar
pt3080PrecorrectorLinearLoadNeutral = _Pt3080PrecorrectorLinearLoadNeutral_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 20),
    _Pt3080PrecorrectorLinearLoadNeutral_Type()
)
pt3080PrecorrectorLinearLoadNeutral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearLoadNeutral.setStatus("current")


class _Pt3080PrecorrectorLinearLoadFactory_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearLoadFactory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("load", 1))
    )


_Pt3080PrecorrectorLinearLoadFactory_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearLoadFactory_Object = MibScalar
pt3080PrecorrectorLinearLoadFactory = _Pt3080PrecorrectorLinearLoadFactory_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 21),
    _Pt3080PrecorrectorLinearLoadFactory_Type()
)
pt3080PrecorrectorLinearLoadFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearLoadFactory.setStatus("current")
_Pt3080PrecorrectorLinearMonitorSenseLevel_Type = Integer32
_Pt3080PrecorrectorLinearMonitorSenseLevel_Object = MibScalar
pt3080PrecorrectorLinearMonitorSenseLevel = _Pt3080PrecorrectorLinearMonitorSenseLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 22),
    _Pt3080PrecorrectorLinearMonitorSenseLevel_Type()
)
pt3080PrecorrectorLinearMonitorSenseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorSenseLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorSenseLevel.setUnits("0.1 dBm")
_Pt3080PrecorrectorLinearMonitorSenseValid_Type = Integer32
_Pt3080PrecorrectorLinearMonitorSenseValid_Object = MibScalar
pt3080PrecorrectorLinearMonitorSenseValid = _Pt3080PrecorrectorLinearMonitorSenseValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 23),
    _Pt3080PrecorrectorLinearMonitorSenseValid_Type()
)
pt3080PrecorrectorLinearMonitorSenseValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorSenseValid.setStatus("current")


class _Pt3080PrecorrectorLinearMonitorStatus_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("not-running", 0),
          ("monitoring", 1),
          ("initialising", 2),
          ("initialising-0", 3),
          ("initialising-10", 4),
          ("initialising-20", 5),
          ("initialising-30", 6),
          ("initialising-40", 7),
          ("initialising-50", 8),
          ("initialising-60", 9),
          ("initialising-70", 10),
          ("initialising-80", 11),
          ("initialising-90", 12),
          ("auto-applying", 13),
          ("completed", 14))
    )


_Pt3080PrecorrectorLinearMonitorStatus_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearMonitorStatus_Object = MibScalar
pt3080PrecorrectorLinearMonitorStatus = _Pt3080PrecorrectorLinearMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 24),
    _Pt3080PrecorrectorLinearMonitorStatus_Type()
)
pt3080PrecorrectorLinearMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorStatus.setStatus("current")


class _Pt3080PrecorrectorLinearUpdateFactoryCurve_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearUpdateFactoryCurve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("update", 1))
    )


_Pt3080PrecorrectorLinearUpdateFactoryCurve_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearUpdateFactoryCurve_Object = MibScalar
pt3080PrecorrectorLinearUpdateFactoryCurve = _Pt3080PrecorrectorLinearUpdateFactoryCurve_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 25),
    _Pt3080PrecorrectorLinearUpdateFactoryCurve_Type()
)
pt3080PrecorrectorLinearUpdateFactoryCurve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearUpdateFactoryCurve.setStatus("current")
_Pt3080PrecorrectorLinearMonitorAmplitudeRipple_Type = Integer32
_Pt3080PrecorrectorLinearMonitorAmplitudeRipple_Object = MibScalar
pt3080PrecorrectorLinearMonitorAmplitudeRipple = _Pt3080PrecorrectorLinearMonitorAmplitudeRipple_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 26),
    _Pt3080PrecorrectorLinearMonitorAmplitudeRipple_Type()
)
pt3080PrecorrectorLinearMonitorAmplitudeRipple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorAmplitudeRipple.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorAmplitudeRipple.setUnits("0.1 dB")
_Pt3080PrecorrectorLinearMonitorGroupDelay_Type = Integer32
_Pt3080PrecorrectorLinearMonitorGroupDelay_Object = MibScalar
pt3080PrecorrectorLinearMonitorGroupDelay = _Pt3080PrecorrectorLinearMonitorGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 27),
    _Pt3080PrecorrectorLinearMonitorGroupDelay_Type()
)
pt3080PrecorrectorLinearMonitorGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorGroupDelay.setUnits("0.1 ns")
_Pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel = _Pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 28),
    _Pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel_Type()
)
pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel.setUnits("0.1 dB")
_Pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel = _Pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 29),
    _Pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel_Type()
)
pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel.setUnits("0.1 dB")
_Pt3080PrecorrectorLinearMonitorAmplitudeRippleValid_Type = Integer32
_Pt3080PrecorrectorLinearMonitorAmplitudeRippleValid_Object = MibScalar
pt3080PrecorrectorLinearMonitorAmplitudeRippleValid = _Pt3080PrecorrectorLinearMonitorAmplitudeRippleValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 30),
    _Pt3080PrecorrectorLinearMonitorAmplitudeRippleValid_Type()
)
pt3080PrecorrectorLinearMonitorAmplitudeRippleValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorAmplitudeRippleValid.setStatus("current")
_Pt3080PrecorrectorLinearMonitorGroupDelayValid_Type = Integer32
_Pt3080PrecorrectorLinearMonitorGroupDelayValid_Object = MibScalar
pt3080PrecorrectorLinearMonitorGroupDelayValid = _Pt3080PrecorrectorLinearMonitorGroupDelayValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 31),
    _Pt3080PrecorrectorLinearMonitorGroupDelayValid_Type()
)
pt3080PrecorrectorLinearMonitorGroupDelayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorGroupDelayValid.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorLowerShoulderValid_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorLowerShoulderValid_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorLowerShoulderValid = _Pt3080PrecorrectorNonlinearMonitorLowerShoulderValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 32),
    _Pt3080PrecorrectorNonlinearMonitorLowerShoulderValid_Type()
)
pt3080PrecorrectorNonlinearMonitorLowerShoulderValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorLowerShoulderValid.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorUpperShoulderValid_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorUpperShoulderValid_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorUpperShoulderValid = _Pt3080PrecorrectorNonlinearMonitorUpperShoulderValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 33),
    _Pt3080PrecorrectorNonlinearMonitorUpperShoulderValid_Type()
)
pt3080PrecorrectorNonlinearMonitorUpperShoulderValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorUpperShoulderValid.setStatus("current")


class _Pt3080PrecorrectorNlinCleanrun_Type(Integer32):
    """Custom type pt3080PrecorrectorNlinCleanrun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080PrecorrectorNlinCleanrun_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNlinCleanrun_Object = MibScalar
pt3080PrecorrectorNlinCleanrun = _Pt3080PrecorrectorNlinCleanrun_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 34),
    _Pt3080PrecorrectorNlinCleanrun_Type()
)
pt3080PrecorrectorNlinCleanrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNlinCleanrun.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorIterations_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorIterations_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorIterations = _Pt3080PrecorrectorNonlinearMonitorIterations_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 35),
    _Pt3080PrecorrectorNonlinearMonitorIterations_Type()
)
pt3080PrecorrectorNonlinearMonitorIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorIterations.setStatus("current")


class _Pt3080PrecorrectorNonlinearLoadNeutral_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearLoadNeutral based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("load", 1))
    )


_Pt3080PrecorrectorNonlinearLoadNeutral_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearLoadNeutral_Object = MibScalar
pt3080PrecorrectorNonlinearLoadNeutral = _Pt3080PrecorrectorNonlinearLoadNeutral_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 36),
    _Pt3080PrecorrectorNonlinearLoadNeutral_Type()
)
pt3080PrecorrectorNonlinearLoadNeutral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearLoadNeutral.setStatus("current")


class _Pt3080PrecorrectorNonlinearLoadFactory_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearLoadFactory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("load", 1))
    )


_Pt3080PrecorrectorNonlinearLoadFactory_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearLoadFactory_Object = MibScalar
pt3080PrecorrectorNonlinearLoadFactory = _Pt3080PrecorrectorNonlinearLoadFactory_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 37),
    _Pt3080PrecorrectorNonlinearLoadFactory_Type()
)
pt3080PrecorrectorNonlinearLoadFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearLoadFactory.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorSenseLevel_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorSenseLevel_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorSenseLevel = _Pt3080PrecorrectorNonlinearMonitorSenseLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 38),
    _Pt3080PrecorrectorNonlinearMonitorSenseLevel_Type()
)
pt3080PrecorrectorNonlinearMonitorSenseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorSenseLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorSenseLevel.setUnits("0.1 dBm")
_Pt3080PrecorrectorNonlinearMonitorSenseValid_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorSenseValid_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorSenseValid = _Pt3080PrecorrectorNonlinearMonitorSenseValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 39),
    _Pt3080PrecorrectorNonlinearMonitorSenseValid_Type()
)
pt3080PrecorrectorNonlinearMonitorSenseValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorSenseValid.setStatus("current")


class _Pt3080PrecorrectorNonlinearMonitorStatus_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("not-running", 0),
          ("monitoring", 1),
          ("initialising", 2),
          ("initialising-0", 3),
          ("initialising-10", 4),
          ("initialising-20", 5),
          ("initialising-30", 6),
          ("initialising-40", 7),
          ("initialising-50", 8),
          ("initialising-60", 9),
          ("initialising-70", 10),
          ("initialising-80", 11),
          ("initialising-90", 12),
          ("auto-applying", 13),
          ("completed", 14))
    )


_Pt3080PrecorrectorNonlinearMonitorStatus_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearMonitorStatus_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorStatus = _Pt3080PrecorrectorNonlinearMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 40),
    _Pt3080PrecorrectorNonlinearMonitorStatus_Type()
)
pt3080PrecorrectorNonlinearMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorStatus.setStatus("current")


class _Pt3080PrecorrectorNonlinearUpdateFactoryCurve_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearUpdateFactoryCurve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("update", 1))
    )


_Pt3080PrecorrectorNonlinearUpdateFactoryCurve_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearUpdateFactoryCurve_Object = MibScalar
pt3080PrecorrectorNonlinearUpdateFactoryCurve = _Pt3080PrecorrectorNonlinearUpdateFactoryCurve_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 41),
    _Pt3080PrecorrectorNonlinearUpdateFactoryCurve_Type()
)
pt3080PrecorrectorNonlinearUpdateFactoryCurve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearUpdateFactoryCurve.setStatus("current")


class _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel_Object = MibScalar
pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel = _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 42),
    _Pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel_Type()
)
pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel.setUnits("0.1 dB")


class _Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel_Object = MibScalar
pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel = _Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 43),
    _Pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel_Type()
)
pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel.setUnits("0.1 ns")


class _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-800, 0),
    )


_Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel = _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 44),
    _Pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel_Type()
)
pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel.setUnits("0.1 dB")


class _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-800, 0),
    )


_Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel = _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 45),
    _Pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel_Type()
)
pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel.setUnits("0.1 dB")


class _Pt3080PrecorrectorLinearSenseEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearSenseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080PrecorrectorLinearSenseEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearSenseEnable_Object = MibScalar
pt3080PrecorrectorLinearSenseEnable = _Pt3080PrecorrectorLinearSenseEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 46),
    _Pt3080PrecorrectorLinearSenseEnable_Type()
)
pt3080PrecorrectorLinearSenseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearSenseEnable.setStatus("current")
_Pt3080PrecorrectorLinearMonitorDiscartedIterations_Type = Integer32
_Pt3080PrecorrectorLinearMonitorDiscartedIterations_Object = MibScalar
pt3080PrecorrectorLinearMonitorDiscartedIterations = _Pt3080PrecorrectorLinearMonitorDiscartedIterations_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 47),
    _Pt3080PrecorrectorLinearMonitorDiscartedIterations_Type()
)
pt3080PrecorrectorLinearMonitorDiscartedIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearMonitorDiscartedIterations.setStatus("current")


class _Pt3080PrecorrectorNonlinearSenseEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearSenseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080PrecorrectorNonlinearSenseEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearSenseEnable_Object = MibScalar
pt3080PrecorrectorNonlinearSenseEnable = _Pt3080PrecorrectorNonlinearSenseEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 48),
    _Pt3080PrecorrectorNonlinearSenseEnable_Type()
)
pt3080PrecorrectorNonlinearSenseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearSenseEnable.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorDiscartedIterations_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorDiscartedIterations_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorDiscartedIterations = _Pt3080PrecorrectorNonlinearMonitorDiscartedIterations_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 49),
    _Pt3080PrecorrectorNonlinearMonitorDiscartedIterations_Type()
)
pt3080PrecorrectorNonlinearMonitorDiscartedIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorDiscartedIterations.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorMer_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorMer_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorMer = _Pt3080PrecorrectorNonlinearMonitorMer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 50),
    _Pt3080PrecorrectorNonlinearMonitorMer_Type()
)
pt3080PrecorrectorNonlinearMonitorMer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorMer.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorMer.setUnits("0.1 dB")
_Pt3080PrecorrectorNonlinearMonitorMerValid_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorMerValid_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorMerValid = _Pt3080PrecorrectorNonlinearMonitorMerValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 51),
    _Pt3080PrecorrectorNonlinearMonitorMerValid_Type()
)
pt3080PrecorrectorNonlinearMonitorMerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorMerValid.setStatus("current")
_Pt3080PrecorrectorNonlinearMonitorPapr_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorPapr_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorPapr = _Pt3080PrecorrectorNonlinearMonitorPapr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 52),
    _Pt3080PrecorrectorNonlinearMonitorPapr_Type()
)
pt3080PrecorrectorNonlinearMonitorPapr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorPapr.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorPapr.setUnits("0.1 dB")
_Pt3080PrecorrectorNonlinearMonitorPaprValid_Type = Integer32
_Pt3080PrecorrectorNonlinearMonitorPaprValid_Object = MibScalar
pt3080PrecorrectorNonlinearMonitorPaprValid = _Pt3080PrecorrectorNonlinearMonitorPaprValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 53),
    _Pt3080PrecorrectorNonlinearMonitorPaprValid_Type()
)
pt3080PrecorrectorNonlinearMonitorPaprValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearMonitorPaprValid.setStatus("current")


class _Pt3080PrecorrectorNonlinearAdaptiveAveraging_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveAveraging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Pt3080PrecorrectorNonlinearAdaptiveAveraging_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveAveraging_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveAveraging = _Pt3080PrecorrectorNonlinearAdaptiveAveraging_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 54),
    _Pt3080PrecorrectorNonlinearAdaptiveAveraging_Type()
)
pt3080PrecorrectorNonlinearAdaptiveAveraging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveAveraging.setStatus("current")


class _Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable = _Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 55),
    _Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable_Type()
)
pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable.setStatus("current")


class _Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 180),
    )


_Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit = _Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 56),
    _Pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit_Type()
)
pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit.setUnits("0.1 dB")


class _Pt3080PrecorrectorNonlinearAdaptiveMerTarget_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveMerTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800),
    )


_Pt3080PrecorrectorNonlinearAdaptiveMerTarget_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveMerTarget_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveMerTarget = _Pt3080PrecorrectorNonlinearAdaptiveMerTarget_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 57),
    _Pt3080PrecorrectorNonlinearAdaptiveMerTarget_Type()
)
pt3080PrecorrectorNonlinearAdaptiveMerTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMerTarget.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMerTarget.setUnits("0.1 dB")


class _Pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis = _Pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 58),
    _Pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis_Type()
)
pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis.setUnits("0.01 dB")


class _Pt3080PrecorrectorNonlinearAdaptiveMerEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAdaptiveMerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080PrecorrectorNonlinearAdaptiveMerEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAdaptiveMerEnable_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptiveMerEnable = _Pt3080PrecorrectorNonlinearAdaptiveMerEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 59),
    _Pt3080PrecorrectorNonlinearAdaptiveMerEnable_Type()
)
pt3080PrecorrectorNonlinearAdaptiveMerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptiveMerEnable.setStatus("current")


class _Pt3080PrecorrectorPaprClipping_Type(Integer32):
    """Custom type pt3080PrecorrectorPaprClipping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1200),
    )


_Pt3080PrecorrectorPaprClipping_Type.__name__ = "Integer32"
_Pt3080PrecorrectorPaprClipping_Object = MibScalar
pt3080PrecorrectorPaprClipping = _Pt3080PrecorrectorPaprClipping_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 60),
    _Pt3080PrecorrectorPaprClipping_Type()
)
pt3080PrecorrectorPaprClipping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorPaprClipping.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorPaprClipping.setUnits("0.01 dB")


class _Pt3080PrecorrectorPaprShaping_Type(Integer32):
    """Custom type pt3080PrecorrectorPaprShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pt3080PrecorrectorPaprShaping_Type.__name__ = "Integer32"
_Pt3080PrecorrectorPaprShaping_Object = MibScalar
pt3080PrecorrectorPaprShaping = _Pt3080PrecorrectorPaprShaping_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 61),
    _Pt3080PrecorrectorPaprShaping_Type()
)
pt3080PrecorrectorPaprShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorPaprShaping.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorPaprShaping.setUnits("1 %")


class _Pt3080PrecorrectorClipperAdaptiveMode_Type(Integer32):
    """Custom type pt3080PrecorrectorClipperAdaptiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitoring", 0),
          ("continuous", 1),
          ("single", 2))
    )


_Pt3080PrecorrectorClipperAdaptiveMode_Type.__name__ = "Integer32"
_Pt3080PrecorrectorClipperAdaptiveMode_Object = MibScalar
pt3080PrecorrectorClipperAdaptiveMode = _Pt3080PrecorrectorClipperAdaptiveMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 63),
    _Pt3080PrecorrectorClipperAdaptiveMode_Type()
)
pt3080PrecorrectorClipperAdaptiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperAdaptiveMode.setStatus("current")


class _Pt3080PrecorrectorClipperMonitorStatus_Type(Integer32):
    """Custom type pt3080PrecorrectorClipperMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("not-running", 0),
          ("monitoring", 1),
          ("initialising", 2),
          ("initialising-0", 3),
          ("initialising-10", 4),
          ("initialising-20", 5),
          ("initialising-30", 6),
          ("initialising-40", 7),
          ("initialising-50", 8),
          ("initialising-60", 9),
          ("initialising-70", 10),
          ("initialising-80", 11),
          ("initialising-90", 12),
          ("auto-applying", 13),
          ("completed", 14))
    )


_Pt3080PrecorrectorClipperMonitorStatus_Type.__name__ = "Integer32"
_Pt3080PrecorrectorClipperMonitorStatus_Object = MibScalar
pt3080PrecorrectorClipperMonitorStatus = _Pt3080PrecorrectorClipperMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 64),
    _Pt3080PrecorrectorClipperMonitorStatus_Type()
)
pt3080PrecorrectorClipperMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorStatus.setStatus("current")
_Pt3080PrecorrectorClipperMonitorShoulderLevelLower_Type = Integer32
_Pt3080PrecorrectorClipperMonitorShoulderLevelLower_Object = MibScalar
pt3080PrecorrectorClipperMonitorShoulderLevelLower = _Pt3080PrecorrectorClipperMonitorShoulderLevelLower_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 65),
    _Pt3080PrecorrectorClipperMonitorShoulderLevelLower_Type()
)
pt3080PrecorrectorClipperMonitorShoulderLevelLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorShoulderLevelLower.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorShoulderLevelLower.setUnits("0.1 dB")
_Pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid_Type = Integer32
_Pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid_Object = MibScalar
pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid = _Pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 66),
    _Pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid_Type()
)
pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid.setStatus("current")
_Pt3080PrecorrectorClipperMonitorShoulderLevelUpper_Type = Integer32
_Pt3080PrecorrectorClipperMonitorShoulderLevelUpper_Object = MibScalar
pt3080PrecorrectorClipperMonitorShoulderLevelUpper = _Pt3080PrecorrectorClipperMonitorShoulderLevelUpper_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 67),
    _Pt3080PrecorrectorClipperMonitorShoulderLevelUpper_Type()
)
pt3080PrecorrectorClipperMonitorShoulderLevelUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorShoulderLevelUpper.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorShoulderLevelUpper.setUnits("0.1 dB")
_Pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid_Type = Integer32
_Pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid_Object = MibScalar
pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid = _Pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 68),
    _Pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid_Type()
)
pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid.setStatus("current")
_Pt3080PrecorrectorClipperMonitorMer_Type = Integer32
_Pt3080PrecorrectorClipperMonitorMer_Object = MibScalar
pt3080PrecorrectorClipperMonitorMer = _Pt3080PrecorrectorClipperMonitorMer_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 69),
    _Pt3080PrecorrectorClipperMonitorMer_Type()
)
pt3080PrecorrectorClipperMonitorMer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorMer.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorMer.setUnits("0.1 dB")
_Pt3080PrecorrectorClipperMonitorMerValid_Type = Integer32
_Pt3080PrecorrectorClipperMonitorMerValid_Object = MibScalar
pt3080PrecorrectorClipperMonitorMerValid = _Pt3080PrecorrectorClipperMonitorMerValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 70),
    _Pt3080PrecorrectorClipperMonitorMerValid_Type()
)
pt3080PrecorrectorClipperMonitorMerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorMerValid.setStatus("current")
_Pt3080PrecorrectorClipperMonitorPapr_Type = Integer32
_Pt3080PrecorrectorClipperMonitorPapr_Object = MibScalar
pt3080PrecorrectorClipperMonitorPapr = _Pt3080PrecorrectorClipperMonitorPapr_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 71),
    _Pt3080PrecorrectorClipperMonitorPapr_Type()
)
pt3080PrecorrectorClipperMonitorPapr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorPapr.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorPapr.setUnits("0.1 dB")
_Pt3080PrecorrectorClipperMonitorPaprValid_Type = Integer32
_Pt3080PrecorrectorClipperMonitorPaprValid_Object = MibScalar
pt3080PrecorrectorClipperMonitorPaprValid = _Pt3080PrecorrectorClipperMonitorPaprValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 72),
    _Pt3080PrecorrectorClipperMonitorPaprValid_Type()
)
pt3080PrecorrectorClipperMonitorPaprValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorPaprValid.setStatus("current")
_Pt3080PrecorrectorClipperMonitorIterations_Type = Integer32
_Pt3080PrecorrectorClipperMonitorIterations_Object = MibScalar
pt3080PrecorrectorClipperMonitorIterations = _Pt3080PrecorrectorClipperMonitorIterations_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 73),
    _Pt3080PrecorrectorClipperMonitorIterations_Type()
)
pt3080PrecorrectorClipperMonitorIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMonitorIterations.setStatus("current")


class _Pt3080PrecorrectorClipperMode_Type(Integer32):
    """Custom type pt3080PrecorrectorClipperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitoring", 0),
          ("static", 1),
          ("adaptive", 2))
    )


_Pt3080PrecorrectorClipperMode_Type.__name__ = "Integer32"
_Pt3080PrecorrectorClipperMode_Object = MibScalar
pt3080PrecorrectorClipperMode = _Pt3080PrecorrectorClipperMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 74),
    _Pt3080PrecorrectorClipperMode_Type()
)
pt3080PrecorrectorClipperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperMode.setStatus("current")
_Pt3080PrecorrectorClipperAdaptive_Type = Integer32
_Pt3080PrecorrectorClipperAdaptive_Object = MibScalar
pt3080PrecorrectorClipperAdaptive = _Pt3080PrecorrectorClipperAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 75),
    _Pt3080PrecorrectorClipperAdaptive_Type()
)
pt3080PrecorrectorClipperAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperAdaptive.setStatus("current")


class _Pt3080PrecorrectorClipperEnable_Type(Integer32):
    """Custom type pt3080PrecorrectorClipperEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080PrecorrectorClipperEnable_Type.__name__ = "Integer32"
_Pt3080PrecorrectorClipperEnable_Object = MibScalar
pt3080PrecorrectorClipperEnable = _Pt3080PrecorrectorClipperEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 76),
    _Pt3080PrecorrectorClipperEnable_Type()
)
pt3080PrecorrectorClipperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperEnable.setStatus("current")


class _Pt3080PrecorrectorNonlinearAttenuation_Type(Integer32):
    """Custom type pt3080PrecorrectorNonlinearAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_Pt3080PrecorrectorNonlinearAttenuation_Type.__name__ = "Integer32"
_Pt3080PrecorrectorNonlinearAttenuation_Object = MibScalar
pt3080PrecorrectorNonlinearAttenuation = _Pt3080PrecorrectorNonlinearAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 77),
    _Pt3080PrecorrectorNonlinearAttenuation_Type()
)
pt3080PrecorrectorNonlinearAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAttenuation.setUnits("0.1 dB")


class _Pt3080PrecorrectorLinearAttenuation_Type(Integer32):
    """Custom type pt3080PrecorrectorLinearAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_Pt3080PrecorrectorLinearAttenuation_Type.__name__ = "Integer32"
_Pt3080PrecorrectorLinearAttenuation_Object = MibScalar
pt3080PrecorrectorLinearAttenuation = _Pt3080PrecorrectorLinearAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 78),
    _Pt3080PrecorrectorLinearAttenuation_Type()
)
pt3080PrecorrectorLinearAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAttenuation.setUnits("0.1 dB")
_Pt3080PrecorrectorLinearAdaptive_Type = Integer32
_Pt3080PrecorrectorLinearAdaptive_Object = MibScalar
pt3080PrecorrectorLinearAdaptive = _Pt3080PrecorrectorLinearAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 79),
    _Pt3080PrecorrectorLinearAdaptive_Type()
)
pt3080PrecorrectorLinearAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorLinearAdaptive.setStatus("current")
_Pt3080PrecorrectorNonlinearAdaptive_Type = Integer32
_Pt3080PrecorrectorNonlinearAdaptive_Object = MibScalar
pt3080PrecorrectorNonlinearAdaptive = _Pt3080PrecorrectorNonlinearAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 80),
    _Pt3080PrecorrectorNonlinearAdaptive_Type()
)
pt3080PrecorrectorNonlinearAdaptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080PrecorrectorNonlinearAdaptive.setStatus("current")


class _Pt3080PrecorrectorClipperAdaptiveShaping_Type(Integer32):
    """Custom type pt3080PrecorrectorClipperAdaptiveShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(99, 100),
    )


_Pt3080PrecorrectorClipperAdaptiveShaping_Type.__name__ = "Integer32"
_Pt3080PrecorrectorClipperAdaptiveShaping_Object = MibScalar
pt3080PrecorrectorClipperAdaptiveShaping = _Pt3080PrecorrectorClipperAdaptiveShaping_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 25, 81),
    _Pt3080PrecorrectorClipperAdaptiveShaping_Type()
)
pt3080PrecorrectorClipperAdaptiveShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperAdaptiveShaping.setStatus("current")
if mibBuilder.loadTexts:
    pt3080PrecorrectorClipperAdaptiveShaping.setUnits("1 %")
_Pt3080Reception_ObjectIdentity = ObjectIdentity
pt3080Reception = _Pt3080Reception_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26)
)


class _Pt3080ReceptionRFFrequency_Type(Integer32):
    """Custom type pt3080ReceptionRFFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000000, 954000000),
    )


_Pt3080ReceptionRFFrequency_Type.__name__ = "Integer32"
_Pt3080ReceptionRFFrequency_Object = MibScalar
pt3080ReceptionRFFrequency = _Pt3080ReceptionRFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 1),
    _Pt3080ReceptionRFFrequency_Type()
)
pt3080ReceptionRFFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFFrequency.setUnits("1 hz")


class _Pt3080ReceptionRFFrequencyOffset_Type(Integer32):
    """Custom type pt3080ReceptionRFFrequencyOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500000, 500000),
    )


_Pt3080ReceptionRFFrequencyOffset_Type.__name__ = "Integer32"
_Pt3080ReceptionRFFrequencyOffset_Object = MibScalar
pt3080ReceptionRFFrequencyOffset = _Pt3080ReceptionRFFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 2),
    _Pt3080ReceptionRFFrequencyOffset_Type()
)
pt3080ReceptionRFFrequencyOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFFrequencyOffset.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFFrequencyOffset.setUnits("1 hz")


class _Pt3080ReceptionIFInputPolicy_Type(Integer32):
    """Custom type pt3080ReceptionIFInputPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rf", 0),
          ("if", 1),
          ("rfav", 2),
          ("ifav", 3))
    )


_Pt3080ReceptionIFInputPolicy_Type.__name__ = "Integer32"
_Pt3080ReceptionIFInputPolicy_Object = MibScalar
pt3080ReceptionIFInputPolicy = _Pt3080ReceptionIFInputPolicy_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 3),
    _Pt3080ReceptionIFInputPolicy_Type()
)
pt3080ReceptionIFInputPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionIFInputPolicy.setStatus("current")


class _Pt3080ReceptionIFFrequency_Type(Integer32):
    """Custom type pt3080ReceptionIFFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("if36mhz", 0),
          ("if36p15mhz", 1),
          ("if40mhz", 2))
    )


_Pt3080ReceptionIFFrequency_Type.__name__ = "Integer32"
_Pt3080ReceptionIFFrequency_Object = MibScalar
pt3080ReceptionIFFrequency = _Pt3080ReceptionIFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 4),
    _Pt3080ReceptionIFFrequency_Type()
)
pt3080ReceptionIFFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionIFFrequency.setStatus("current")


class _Pt3080ReceptionIFPolarity_Type(Integer32):
    """Custom type pt3080ReceptionIFPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("norm", 0),
          ("inv", 1))
    )


_Pt3080ReceptionIFPolarity_Type.__name__ = "Integer32"
_Pt3080ReceptionIFPolarity_Object = MibScalar
pt3080ReceptionIFPolarity = _Pt3080ReceptionIFPolarity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 5),
    _Pt3080ReceptionIFPolarity_Type()
)
pt3080ReceptionIFPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionIFPolarity.setStatus("current")


class _Pt3080ReceptionRFSquelchEnable_Type(Integer32):
    """Custom type pt3080ReceptionRFSquelchEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ReceptionRFSquelchEnable_Type.__name__ = "Integer32"
_Pt3080ReceptionRFSquelchEnable_Object = MibScalar
pt3080ReceptionRFSquelchEnable = _Pt3080ReceptionRFSquelchEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 6),
    _Pt3080ReceptionRFSquelchEnable_Type()
)
pt3080ReceptionRFSquelchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFSquelchEnable.setStatus("current")


class _Pt3080ReceptionRFSquelchThreshold_Type(Integer32):
    """Custom type pt3080ReceptionRFSquelchThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-800, -70),
    )


_Pt3080ReceptionRFSquelchThreshold_Type.__name__ = "Integer32"
_Pt3080ReceptionRFSquelchThreshold_Object = MibScalar
pt3080ReceptionRFSquelchThreshold = _Pt3080ReceptionRFSquelchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 7),
    _Pt3080ReceptionRFSquelchThreshold_Type()
)
pt3080ReceptionRFSquelchThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFSquelchThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFSquelchThreshold.setUnits("0.1 dBm")


class _Pt3080ReceptionRFSquelchHysteresis_Type(Integer32):
    """Custom type pt3080ReceptionRFSquelchHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_Pt3080ReceptionRFSquelchHysteresis_Type.__name__ = "Integer32"
_Pt3080ReceptionRFSquelchHysteresis_Object = MibScalar
pt3080ReceptionRFSquelchHysteresis = _Pt3080ReceptionRFSquelchHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 8),
    _Pt3080ReceptionRFSquelchHysteresis_Type()
)
pt3080ReceptionRFSquelchHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFSquelchHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFSquelchHysteresis.setUnits("0.01 dB")


class _Pt3080ReceptionGainControl_Type(Integer32):
    """Custom type pt3080ReceptionGainControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("freeze", 1),
          ("manual", 2))
    )


_Pt3080ReceptionGainControl_Type.__name__ = "Integer32"
_Pt3080ReceptionGainControl_Object = MibScalar
pt3080ReceptionGainControl = _Pt3080ReceptionGainControl_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 9),
    _Pt3080ReceptionGainControl_Type()
)
pt3080ReceptionGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionGainControl.setStatus("current")


class _Pt3080ReceptionGainManualValue_Type(Integer32):
    """Custom type pt3080ReceptionGainManualValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_Pt3080ReceptionGainManualValue_Type.__name__ = "Integer32"
_Pt3080ReceptionGainManualValue_Object = MibScalar
pt3080ReceptionGainManualValue = _Pt3080ReceptionGainManualValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 10),
    _Pt3080ReceptionGainManualValue_Type()
)
pt3080ReceptionGainManualValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionGainManualValue.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionGainManualValue.setUnits("0.1 dB")


class _Pt3080ReceptionGainLimitEnable_Type(Integer32):
    """Custom type pt3080ReceptionGainLimitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ReceptionGainLimitEnable_Type.__name__ = "Integer32"
_Pt3080ReceptionGainLimitEnable_Object = MibScalar
pt3080ReceptionGainLimitEnable = _Pt3080ReceptionGainLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 11),
    _Pt3080ReceptionGainLimitEnable_Type()
)
pt3080ReceptionGainLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionGainLimitEnable.setStatus("current")


class _Pt3080ReceptionGainLimit_Type(Integer32):
    """Custom type pt3080ReceptionGainLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 700),
    )


_Pt3080ReceptionGainLimit_Type.__name__ = "Integer32"
_Pt3080ReceptionGainLimit_Object = MibScalar
pt3080ReceptionGainLimit = _Pt3080ReceptionGainLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 12),
    _Pt3080ReceptionGainLimit_Type()
)
pt3080ReceptionGainLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionGainLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionGainLimit.setUnits("0.1 db")
_Pt3080ReceptionGainCurrent_Type = Integer32
_Pt3080ReceptionGainCurrent_Object = MibScalar
pt3080ReceptionGainCurrent = _Pt3080ReceptionGainCurrent_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 13),
    _Pt3080ReceptionGainCurrent_Type()
)
pt3080ReceptionGainCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionGainCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionGainCurrent.setUnits("0.01 db")


class _Pt3080ReceptionIFRFtoIFHoldoverDelay_Type(Integer32):
    """Custom type pt3080ReceptionIFRFtoIFHoldoverDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Pt3080ReceptionIFRFtoIFHoldoverDelay_Type.__name__ = "Integer32"
_Pt3080ReceptionIFRFtoIFHoldoverDelay_Object = MibScalar
pt3080ReceptionIFRFtoIFHoldoverDelay = _Pt3080ReceptionIFRFtoIFHoldoverDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 18),
    _Pt3080ReceptionIFRFtoIFHoldoverDelay_Type()
)
pt3080ReceptionIFRFtoIFHoldoverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionIFRFtoIFHoldoverDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionIFRFtoIFHoldoverDelay.setUnits("1 secs")


class _Pt3080ReceptionIFIFtoRFHoldoverDelay_Type(Integer32):
    """Custom type pt3080ReceptionIFIFtoRFHoldoverDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Pt3080ReceptionIFIFtoRFHoldoverDelay_Type.__name__ = "Integer32"
_Pt3080ReceptionIFIFtoRFHoldoverDelay_Object = MibScalar
pt3080ReceptionIFIFtoRFHoldoverDelay = _Pt3080ReceptionIFIFtoRFHoldoverDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 19),
    _Pt3080ReceptionIFIFtoRFHoldoverDelay_Type()
)
pt3080ReceptionIFIFtoRFHoldoverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionIFIFtoRFHoldoverDelay.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionIFIFtoRFHoldoverDelay.setUnits("1 secs")


class _Pt3080ReceptionIFInput_Type(Integer32):
    """Custom type pt3080ReceptionIFInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("if", 0),
          ("rf", 1))
    )


_Pt3080ReceptionIFInput_Type.__name__ = "Integer32"
_Pt3080ReceptionIFInput_Object = MibScalar
pt3080ReceptionIFInput = _Pt3080ReceptionIFInput_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 20),
    _Pt3080ReceptionIFInput_Type()
)
pt3080ReceptionIFInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionIFInput.setStatus("current")
_Pt3080ReceptionRFInputLevel_Type = Integer32
_Pt3080ReceptionRFInputLevel_Object = MibScalar
pt3080ReceptionRFInputLevel = _Pt3080ReceptionRFInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 21),
    _Pt3080ReceptionRFInputLevel_Type()
)
pt3080ReceptionRFInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionRFInputLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFInputLevel.setUnits("0.1 dBm")
_Pt3080ReceptionIFInputLevel_Type = Integer32
_Pt3080ReceptionIFInputLevel_Object = MibScalar
pt3080ReceptionIFInputLevel = _Pt3080ReceptionIFInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 22),
    _Pt3080ReceptionIFInputLevel_Type()
)
pt3080ReceptionIFInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionIFInputLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionIFInputLevel.setUnits("0.01 dBm")


class _Pt3080ReceptionBandwidth_Type(Integer32):
    """Custom type pt3080ReceptionBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("r5", 0),
          ("r6", 1),
          ("r7", 2),
          ("r8", 3))
    )


_Pt3080ReceptionBandwidth_Type.__name__ = "Integer32"
_Pt3080ReceptionBandwidth_Object = MibScalar
pt3080ReceptionBandwidth = _Pt3080ReceptionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 23),
    _Pt3080ReceptionBandwidth_Type()
)
pt3080ReceptionBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionBandwidth.setStatus("current")


class _Pt3080ReceptionRFPolarity_Type(Integer32):
    """Custom type pt3080ReceptionRFPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("norm", 0),
          ("inv", 1))
    )


_Pt3080ReceptionRFPolarity_Type.__name__ = "Integer32"
_Pt3080ReceptionRFPolarity_Object = MibScalar
pt3080ReceptionRFPolarity = _Pt3080ReceptionRFPolarity_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 24),
    _Pt3080ReceptionRFPolarity_Type()
)
pt3080ReceptionRFPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFPolarity.setStatus("current")


class _Pt3080ReceptionRFInputLevelHysteresis_Type(Integer32):
    """Custom type pt3080ReceptionRFInputLevelHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500),
    )


_Pt3080ReceptionRFInputLevelHysteresis_Type.__name__ = "Integer32"
_Pt3080ReceptionRFInputLevelHysteresis_Object = MibScalar
pt3080ReceptionRFInputLevelHysteresis = _Pt3080ReceptionRFInputLevelHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 25),
    _Pt3080ReceptionRFInputLevelHysteresis_Type()
)
pt3080ReceptionRFInputLevelHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFInputLevelHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFInputLevelHysteresis.setUnits("0.01 dB")


class _Pt3080ReceptionRFInputLevelThreshold_Type(Integer32):
    """Custom type pt3080ReceptionRFInputLevelThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8000, -700),
    )


_Pt3080ReceptionRFInputLevelThreshold_Type.__name__ = "Integer32"
_Pt3080ReceptionRFInputLevelThreshold_Object = MibScalar
pt3080ReceptionRFInputLevelThreshold = _Pt3080ReceptionRFInputLevelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 26),
    _Pt3080ReceptionRFInputLevelThreshold_Type()
)
pt3080ReceptionRFInputLevelThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFInputLevelThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFInputLevelThreshold.setUnits("0.01 dBm")


class _Pt3080ReceptionAGCMode_Type(Integer32):
    """Custom type pt3080ReceptionAGCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slow", 0),
          ("fast", 1))
    )


_Pt3080ReceptionAGCMode_Type.__name__ = "Integer32"
_Pt3080ReceptionAGCMode_Object = MibScalar
pt3080ReceptionAGCMode = _Pt3080ReceptionAGCMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 30),
    _Pt3080ReceptionAGCMode_Type()
)
pt3080ReceptionAGCMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionAGCMode.setStatus("current")


class _Pt3080ReceptionAGCHysteresis_Type(Integer32):
    """Custom type pt3080ReceptionAGCHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Pt3080ReceptionAGCHysteresis_Type.__name__ = "Integer32"
_Pt3080ReceptionAGCHysteresis_Object = MibScalar
pt3080ReceptionAGCHysteresis = _Pt3080ReceptionAGCHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 31),
    _Pt3080ReceptionAGCHysteresis_Type()
)
pt3080ReceptionAGCHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionAGCHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionAGCHysteresis.setUnits("0.01 dB")


class _Pt3080ReceptionRFTrackingFilterEnable_Type(Integer32):
    """Custom type pt3080ReceptionRFTrackingFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pt3080ReceptionRFTrackingFilterEnable_Type.__name__ = "Integer32"
_Pt3080ReceptionRFTrackingFilterEnable_Object = MibScalar
pt3080ReceptionRFTrackingFilterEnable = _Pt3080ReceptionRFTrackingFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 35),
    _Pt3080ReceptionRFTrackingFilterEnable_Type()
)
pt3080ReceptionRFTrackingFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFTrackingFilterEnable.setStatus("current")
_Pt3080ReceptionRFifLevel_Type = Integer32
_Pt3080ReceptionRFifLevel_Object = MibScalar
pt3080ReceptionRFifLevel = _Pt3080ReceptionRFifLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 36),
    _Pt3080ReceptionRFifLevel_Type()
)
pt3080ReceptionRFifLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionRFifLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFifLevel.setUnits("0.1 dB")


class _Pt3080ReceptionRFNominalInputLevel_Type(Integer32):
    """Custom type pt3080ReceptionRFNominalInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 100),
    )


_Pt3080ReceptionRFNominalInputLevel_Type.__name__ = "Integer32"
_Pt3080ReceptionRFNominalInputLevel_Object = MibScalar
pt3080ReceptionRFNominalInputLevel = _Pt3080ReceptionRFNominalInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 37),
    _Pt3080ReceptionRFNominalInputLevel_Type()
)
pt3080ReceptionRFNominalInputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ReceptionRFNominalInputLevel.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ReceptionRFNominalInputLevel.setUnits("0.1 dBm")
_Pt3080ReceptionTunerHWVersion_Type = DisplayString
_Pt3080ReceptionTunerHWVersion_Object = MibScalar
pt3080ReceptionTunerHWVersion = _Pt3080ReceptionTunerHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 40),
    _Pt3080ReceptionTunerHWVersion_Type()
)
pt3080ReceptionTunerHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionTunerHWVersion.setStatus("current")
_Pt3080ReceptionTunerHWType_Type = DisplayString
_Pt3080ReceptionTunerHWType_Object = MibScalar
pt3080ReceptionTunerHWType = _Pt3080ReceptionTunerHWType_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 41),
    _Pt3080ReceptionTunerHWType_Type()
)
pt3080ReceptionTunerHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionTunerHWType.setStatus("current")
_Pt3080ReceptionTunerHWID_Type = DisplayString
_Pt3080ReceptionTunerHWID_Object = MibScalar
pt3080ReceptionTunerHWID = _Pt3080ReceptionTunerHWID_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 42),
    _Pt3080ReceptionTunerHWID_Type()
)
pt3080ReceptionTunerHWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionTunerHWID.setStatus("current")
_Pt3080ReceptionTunerHWSerialNumber_Type = DisplayString
_Pt3080ReceptionTunerHWSerialNumber_Object = MibScalar
pt3080ReceptionTunerHWSerialNumber = _Pt3080ReceptionTunerHWSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 43),
    _Pt3080ReceptionTunerHWSerialNumber_Type()
)
pt3080ReceptionTunerHWSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionTunerHWSerialNumber.setStatus("current")
_Pt3080ReceptionTunerHWCalibrationDate_Type = DisplayString
_Pt3080ReceptionTunerHWCalibrationDate_Object = MibScalar
pt3080ReceptionTunerHWCalibrationDate = _Pt3080ReceptionTunerHWCalibrationDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 44),
    _Pt3080ReceptionTunerHWCalibrationDate_Type()
)
pt3080ReceptionTunerHWCalibrationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionTunerHWCalibrationDate.setStatus("current")
_Pt3080ReceptionTunerHWCalibrationDataVersion_Type = DisplayString
_Pt3080ReceptionTunerHWCalibrationDataVersion_Object = MibScalar
pt3080ReceptionTunerHWCalibrationDataVersion = _Pt3080ReceptionTunerHWCalibrationDataVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 45),
    _Pt3080ReceptionTunerHWCalibrationDataVersion_Type()
)
pt3080ReceptionTunerHWCalibrationDataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionTunerHWCalibrationDataVersion.setStatus("current")
_Pt3080ReceptionTunerHWCalibrationSWVersion_Type = DisplayString
_Pt3080ReceptionTunerHWCalibrationSWVersion_Object = MibScalar
pt3080ReceptionTunerHWCalibrationSWVersion = _Pt3080ReceptionTunerHWCalibrationSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 26, 46),
    _Pt3080ReceptionTunerHWCalibrationSWVersion_Type()
)
pt3080ReceptionTunerHWCalibrationSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ReceptionTunerHWCalibrationSWVersion.setStatus("current")
_Pt3080Backplane_ObjectIdentity = ObjectIdentity
pt3080Backplane = _Pt3080Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 27)
)


class _Pt3080BackplanePolarityHardMute_Type(Integer32):
    """Custom type pt3080BackplanePolarityHardMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activelow", 0),
          ("activehigh", 1))
    )


_Pt3080BackplanePolarityHardMute_Type.__name__ = "Integer32"
_Pt3080BackplanePolarityHardMute_Object = MibScalar
pt3080BackplanePolarityHardMute = _Pt3080BackplanePolarityHardMute_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 27, 1),
    _Pt3080BackplanePolarityHardMute_Type()
)
pt3080BackplanePolarityHardMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080BackplanePolarityHardMute.setStatus("current")


class _Pt3080BackplanePolarityRFFail_Type(Integer32):
    """Custom type pt3080BackplanePolarityRFFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activelow", 0),
          ("activehigh", 1))
    )


_Pt3080BackplanePolarityRFFail_Type.__name__ = "Integer32"
_Pt3080BackplanePolarityRFFail_Object = MibScalar
pt3080BackplanePolarityRFFail = _Pt3080BackplanePolarityRFFail_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 27, 2),
    _Pt3080BackplanePolarityRFFail_Type()
)
pt3080BackplanePolarityRFFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080BackplanePolarityRFFail.setStatus("current")
_Pt3080ASI_ObjectIdentity = ObjectIdentity
pt3080ASI = _Pt3080ASI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30)
)


class _Pt3080ASIInput1SyncTimeout_Type(Integer32):
    """Custom type pt3080ASIInput1SyncTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_Pt3080ASIInput1SyncTimeout_Type.__name__ = "Integer32"
_Pt3080ASIInput1SyncTimeout_Object = MibScalar
pt3080ASIInput1SyncTimeout = _Pt3080ASIInput1SyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 1),
    _Pt3080ASIInput1SyncTimeout_Type()
)
pt3080ASIInput1SyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIInput1SyncTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1SyncTimeout.setUnits("1 ms")


class _Pt3080ASIInput1DataErrorLimit_Type(Integer32):
    """Custom type pt3080ASIInput1DataErrorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_Pt3080ASIInput1DataErrorLimit_Type.__name__ = "Integer32"
_Pt3080ASIInput1DataErrorLimit_Object = MibScalar
pt3080ASIInput1DataErrorLimit = _Pt3080ASIInput1DataErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 2),
    _Pt3080ASIInput1DataErrorLimit_Type()
)
pt3080ASIInput1DataErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataErrorLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataErrorLimit.setUnits("0.1 bits/s")


class _Pt3080ASIInput1SyncStatus_Type(Integer32):
    """Custom type pt3080ASIInput1SyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Pt3080ASIInput1SyncStatus_Type.__name__ = "Integer32"
_Pt3080ASIInput1SyncStatus_Object = MibScalar
pt3080ASIInput1SyncStatus = _Pt3080ASIInput1SyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 3),
    _Pt3080ASIInput1SyncStatus_Type()
)
pt3080ASIInput1SyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1SyncStatus.setStatus("current")


class _Pt3080ASIInput1SyncSignal_Type(Integer32):
    """Custom type pt3080ASIInput1SyncSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("norm", 1),
          ("inv", 2))
    )


_Pt3080ASIInput1SyncSignal_Type.__name__ = "Integer32"
_Pt3080ASIInput1SyncSignal_Object = MibScalar
pt3080ASIInput1SyncSignal = _Pt3080ASIInput1SyncSignal_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 4),
    _Pt3080ASIInput1SyncSignal_Type()
)
pt3080ASIInput1SyncSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1SyncSignal.setStatus("current")


class _Pt3080ASIInput1SyncTSSize_Type(Integer32):
    """Custom type pt3080ASIInput1SyncTSSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ts188", 1),
          ("ts204", 2))
    )


_Pt3080ASIInput1SyncTSSize_Type.__name__ = "Integer32"
_Pt3080ASIInput1SyncTSSize_Object = MibScalar
pt3080ASIInput1SyncTSSize = _Pt3080ASIInput1SyncTSSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 5),
    _Pt3080ASIInput1SyncTSSize_Type()
)
pt3080ASIInput1SyncTSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1SyncTSSize.setStatus("current")
_Pt3080ASIInput1LineErrors_Type = Integer32
_Pt3080ASIInput1LineErrors_Object = MibScalar
pt3080ASIInput1LineErrors = _Pt3080ASIInput1LineErrors_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 6),
    _Pt3080ASIInput1LineErrors_Type()
)
pt3080ASIInput1LineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1LineErrors.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1LineErrors.setUnits("1 bits")
_Pt3080ASIInput1LineRate_Type = Integer32
_Pt3080ASIInput1LineRate_Object = MibScalar
pt3080ASIInput1LineRate = _Pt3080ASIInput1LineRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 7),
    _Pt3080ASIInput1LineRate_Type()
)
pt3080ASIInput1LineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1LineRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1LineRate.setUnits("0.1 Mbps")
_Pt3080ASIInput1LineErrorRate_Type = Integer32
_Pt3080ASIInput1LineErrorRate_Object = MibScalar
pt3080ASIInput1LineErrorRate = _Pt3080ASIInput1LineErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 8),
    _Pt3080ASIInput1LineErrorRate_Type()
)
pt3080ASIInput1LineErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1LineErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1LineErrorRate.setUnits("0.1 bits/s")
_Pt3080ASIInput1DataErrors_Type = Integer32
_Pt3080ASIInput1DataErrors_Object = MibScalar
pt3080ASIInput1DataErrors = _Pt3080ASIInput1DataErrors_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 9),
    _Pt3080ASIInput1DataErrors_Type()
)
pt3080ASIInput1DataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataErrors.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataErrors.setUnits("1 bits")
_Pt3080ASIInput1DataRate_Type = Integer32
_Pt3080ASIInput1DataRate_Object = MibScalar
pt3080ASIInput1DataRate = _Pt3080ASIInput1DataRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 10),
    _Pt3080ASIInput1DataRate_Type()
)
pt3080ASIInput1DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataRate.setUnits("0.1 Mbps/s")
_Pt3080ASIInput1DataErrorRate_Type = Integer32
_Pt3080ASIInput1DataErrorRate_Object = MibScalar
pt3080ASIInput1DataErrorRate = _Pt3080ASIInput1DataErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 11),
    _Pt3080ASIInput1DataErrorRate_Type()
)
pt3080ASIInput1DataErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput1DataErrorRate.setUnits("0.1 bits/s")


class _Pt3080ASIInput1ClearErrorCounters_Type(Integer32):
    """Custom type pt3080ASIInput1ClearErrorCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("activate", 1))
    )


_Pt3080ASIInput1ClearErrorCounters_Type.__name__ = "Integer32"
_Pt3080ASIInput1ClearErrorCounters_Object = MibScalar
pt3080ASIInput1ClearErrorCounters = _Pt3080ASIInput1ClearErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 12),
    _Pt3080ASIInput1ClearErrorCounters_Type()
)
pt3080ASIInput1ClearErrorCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIInput1ClearErrorCounters.setStatus("current")


class _Pt3080ASIInput2SyncTimeout_Type(Integer32):
    """Custom type pt3080ASIInput2SyncTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_Pt3080ASIInput2SyncTimeout_Type.__name__ = "Integer32"
_Pt3080ASIInput2SyncTimeout_Object = MibScalar
pt3080ASIInput2SyncTimeout = _Pt3080ASIInput2SyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 51),
    _Pt3080ASIInput2SyncTimeout_Type()
)
pt3080ASIInput2SyncTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIInput2SyncTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2SyncTimeout.setUnits("1 ms")


class _Pt3080ASIInput2DataErrorLimit_Type(Integer32):
    """Custom type pt3080ASIInput2DataErrorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_Pt3080ASIInput2DataErrorLimit_Type.__name__ = "Integer32"
_Pt3080ASIInput2DataErrorLimit_Object = MibScalar
pt3080ASIInput2DataErrorLimit = _Pt3080ASIInput2DataErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 52),
    _Pt3080ASIInput2DataErrorLimit_Type()
)
pt3080ASIInput2DataErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataErrorLimit.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataErrorLimit.setUnits("0.1 bits/s")


class _Pt3080ASIInput2SyncStatus_Type(Integer32):
    """Custom type pt3080ASIInput2SyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Pt3080ASIInput2SyncStatus_Type.__name__ = "Integer32"
_Pt3080ASIInput2SyncStatus_Object = MibScalar
pt3080ASIInput2SyncStatus = _Pt3080ASIInput2SyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 53),
    _Pt3080ASIInput2SyncStatus_Type()
)
pt3080ASIInput2SyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2SyncStatus.setStatus("current")


class _Pt3080ASIInput2SyncSignal_Type(Integer32):
    """Custom type pt3080ASIInput2SyncSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("norm", 1),
          ("inv", 2))
    )


_Pt3080ASIInput2SyncSignal_Type.__name__ = "Integer32"
_Pt3080ASIInput2SyncSignal_Object = MibScalar
pt3080ASIInput2SyncSignal = _Pt3080ASIInput2SyncSignal_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 54),
    _Pt3080ASIInput2SyncSignal_Type()
)
pt3080ASIInput2SyncSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2SyncSignal.setStatus("current")


class _Pt3080ASIInput2SyncTSSize_Type(Integer32):
    """Custom type pt3080ASIInput2SyncTSSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ts188", 1),
          ("ts204", 2))
    )


_Pt3080ASIInput2SyncTSSize_Type.__name__ = "Integer32"
_Pt3080ASIInput2SyncTSSize_Object = MibScalar
pt3080ASIInput2SyncTSSize = _Pt3080ASIInput2SyncTSSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 55),
    _Pt3080ASIInput2SyncTSSize_Type()
)
pt3080ASIInput2SyncTSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2SyncTSSize.setStatus("current")
_Pt3080ASIInput2LineErrors_Type = Integer32
_Pt3080ASIInput2LineErrors_Object = MibScalar
pt3080ASIInput2LineErrors = _Pt3080ASIInput2LineErrors_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 56),
    _Pt3080ASIInput2LineErrors_Type()
)
pt3080ASIInput2LineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2LineErrors.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2LineErrors.setUnits("1 bits")
_Pt3080ASIInput2LineRate_Type = Integer32
_Pt3080ASIInput2LineRate_Object = MibScalar
pt3080ASIInput2LineRate = _Pt3080ASIInput2LineRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 57),
    _Pt3080ASIInput2LineRate_Type()
)
pt3080ASIInput2LineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2LineRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2LineRate.setUnits("0.1 Mbps")
_Pt3080ASIInput2LineErrorRate_Type = Integer32
_Pt3080ASIInput2LineErrorRate_Object = MibScalar
pt3080ASIInput2LineErrorRate = _Pt3080ASIInput2LineErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 58),
    _Pt3080ASIInput2LineErrorRate_Type()
)
pt3080ASIInput2LineErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2LineErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2LineErrorRate.setUnits("0.1 bits/s")
_Pt3080ASIInput2DataErrors_Type = Integer32
_Pt3080ASIInput2DataErrors_Object = MibScalar
pt3080ASIInput2DataErrors = _Pt3080ASIInput2DataErrors_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 59),
    _Pt3080ASIInput2DataErrors_Type()
)
pt3080ASIInput2DataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataErrors.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataErrors.setUnits("1 bits")
_Pt3080ASIInput2DataRate_Type = Integer32
_Pt3080ASIInput2DataRate_Object = MibScalar
pt3080ASIInput2DataRate = _Pt3080ASIInput2DataRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 60),
    _Pt3080ASIInput2DataRate_Type()
)
pt3080ASIInput2DataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataRate.setUnits("0.1 Mbps/s")
_Pt3080ASIInput2DataErrorRate_Type = Integer32
_Pt3080ASIInput2DataErrorRate_Object = MibScalar
pt3080ASIInput2DataErrorRate = _Pt3080ASIInput2DataErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 61),
    _Pt3080ASIInput2DataErrorRate_Type()
)
pt3080ASIInput2DataErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    pt3080ASIInput2DataErrorRate.setUnits("0.1 bits/s")


class _Pt3080ASIInput2ClearErrorCounters_Type(Integer32):
    """Custom type pt3080ASIInput2ClearErrorCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("activate", 1))
    )


_Pt3080ASIInput2ClearErrorCounters_Type.__name__ = "Integer32"
_Pt3080ASIInput2ClearErrorCounters_Object = MibScalar
pt3080ASIInput2ClearErrorCounters = _Pt3080ASIInput2ClearErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 30, 62),
    _Pt3080ASIInput2ClearErrorCounters_Type()
)
pt3080ASIInput2ClearErrorCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pt3080ASIInput2ClearErrorCounters.setStatus("current")
_Pt3080Notifs_ObjectIdentity = ObjectIdentity
pt3080Notifs = _Pt3080Notifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64)
)
_Pt3080Notif_ObjectIdentity = ObjectIdentity
pt3080Notif = _Pt3080Notif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0)
)
_Pt3080NotifMessage_Type = DisplayString
_Pt3080NotifMessage_Object = MibScalar
pt3080NotifMessage = _Pt3080NotifMessage_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 1),
    _Pt3080NotifMessage_Type()
)
pt3080NotifMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pt3080NotifMessage.setStatus("current")


class _Pt3080NotifState_Type(Integer32):
    """Custom type pt3080NotifState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 1))
    )


_Pt3080NotifState_Type.__name__ = "Integer32"
_Pt3080NotifState_Object = MibScalar
pt3080NotifState = _Pt3080NotifState_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 2),
    _Pt3080NotifState_Type()
)
pt3080NotifState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pt3080NotifState.setStatus("current")
_Pt3080NotifLocalTime_Type = DateAndTime
_Pt3080NotifLocalTime_Object = MibScalar
pt3080NotifLocalTime = _Pt3080NotifLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 3),
    _Pt3080NotifLocalTime_Type()
)
pt3080NotifLocalTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pt3080NotifLocalTime.setStatus("current")
_Pt3080Conformance_ObjectIdentity = ObjectIdentity
pt3080Conformance = _Pt3080Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100)
)
_Pt3080Compliances_ObjectIdentity = ObjectIdentity
pt3080Compliances = _Pt3080Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 1)
)
_Pt3080Groups_ObjectIdentity = ObjectIdentity
pt3080Groups = _Pt3080Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2)
)
_Pt3080NotificationsGroups_ObjectIdentity = ObjectIdentity
pt3080NotificationsGroups = _Pt3080NotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4)
)

# Managed Objects groups

pt3080SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 1)
)
pt3080SystemGroup.setObjects(
      *(("PT3080-MIB", "pt3080SystemInstrumentFW1Rev"),
        ("PT3080-MIB", "pt3080SystemInstrumentFW1RevBL"),
        ("PT3080-MIB", "pt3080SystemInstrumentFW2Rev"),
        ("PT3080-MIB", "pt3080SystemInstrumentFW2RevBL"),
        ("PT3080-MIB", "pt3080SystemInstrumentFW3Rev"),
        ("PT3080-MIB", "pt3080SystemInstrumentFW4Rev"),
        ("PT3080-MIB", "pt3080SystemInstrumentPCBRev"),
        ("PT3080-MIB", "pt3080SystemInstrumentCalibrationRev"),
        ("PT3080-MIB", "pt3080SystemInstrumentCalibrationDate"),
        ("PT3080-MIB", "pt3080SystemReboot"),
        ("PT3080-MIB", "pt3080SystemRebootDefaultConfig"),
        ("PT3080-MIB", "pt3080SystemDateTime"),
        ("PT3080-MIB", "pt3080SystemImage0Version"),
        ("PT3080-MIB", "pt3080SystemImage0InstalledDate"),
        ("PT3080-MIB", "pt3080SystemImage1version"),
        ("PT3080-MIB", "pt3080SystemImage1InstalledDate"),
        ("PT3080-MIB", "pt3080SystemScheduledActionRecurrence"),
        ("PT3080-MIB", "pt3080SystemScheduledActionHour"),
        ("PT3080-MIB", "pt3080SystemScheduledActionMinute"),
        ("PT3080-MIB", "pt3080SystemScheduledActionWeekday"),
        ("PT3080-MIB", "pt3080SystemScheduledActionMonthDay"),
        ("PT3080-MIB", "pt3080SystemScheduledActionDate"),
        ("PT3080-MIB", "pt3080SystemScheduledActionRandomDelay"),
        ("PT3080-MIB", "pt3080SystemScheduledActionAction"),
        ("PT3080-MIB", "pt3080SystemScheduledActionRepeaterMode"),
        ("PT3080-MIB", "pt3080SystemScheduledActionPresetNo"),
        ("PT3080-MIB", "pt3080SystemScheduledActionRebootImage"),
        ("PT3080-MIB", "pt3080SystemScheduledActionRebootSystemType"),
        ("PT3080-MIB", "pt3080SystemScheduledActionMute"),
        ("PT3080-MIB", "pt3080SystemScheduledActionSWUpgradeProtocol"),
        ("PT3080-MIB", "pt3080SystemScheduledActionSWUpgradeUsername"),
        ("PT3080-MIB", "pt3080SystemScheduledActionSWUpgradePassword"),
        ("PT3080-MIB", "pt3080SystemScheduledActionSWUpgradeImageServer"),
        ("PT3080-MIB", "pt3080SystemScheduledActionSWUpgradeImagePath"),
        ("PT3080-MIB", "pt3080SystemServiceLED"),
        ("PT3080-MIB", "pt3080SystemLanguage"),
        ("PT3080-MIB", "pt3080SystemType"),
        ("PT3080-MIB", "pt3080SystemModulationStandard"),
        ("PT3080-MIB", "pt3080SystemCurrentImage"),
        ("PT3080-MIB", "pt3080SystemInstrumentKU"),
        ("PT3080-MIB", "pt3080SystemInstrumentType"),
        ("PT3080-MIB", "pt3080SystemInstrumentOptions"),
        ("PT3080-MIB", "pt3080SystemDateTimeSync"),
        ("PT3080-MIB", "pt3080SystemDateTimeSyncActual"),
        ("PT3080-MIB", "pt3080SystemTimezone"),
        ("PT3080-MIB", "pt3080SystemInstrumentSWRev"),
        ("PT3080-MIB", "pt3080SystemInstrumentBootLoaderRev"),
        ("PT3080-MIB", "pt3080SystemInstrumentKernelRev"),
        ("PT3080-MIB", "pt3080SystemOperationOnTime"),
        ("PT3080-MIB", "pt3080SystemOperationOnAirTime"),
        ("PT3080-MIB", "pt3080SystemOperationNumberOfBoots"),
        ("PT3080-MIB", "pt3080SystemBackplaneid"),
        ("PT3080-MIB", "pt3080SystemBackplaneIdRaw"),
        ("PT3080-MIB", "pt3080SystemBackplaneIdPcb"),
        ("PT3080-MIB", "pt3080SystemBackplaneIdCableOptions"),
        ("PT3080-MIB", "pt3080SystemBackplaneIdMAnuf"),
        ("PT3080-MIB", "pt3080SystemBackplaneCalibrationDate"),
        ("PT3080-MIB", "pt3080SystemBackplaneCalibrationSw"),
        ("PT3080-MIB", "pt3080SystemBackplaneIdPartlist"))
)
if mibBuilder.loadTexts:
    pt3080SystemGroup.setStatus("current")

pt3080ModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 2)
)
pt3080ModeGroup.setObjects(
      *(("PT3080-MIB", "pt3080ModeListenBroadcast"),
        ("PT3080-MIB", "pt3080ModeNetwork"),
        ("PT3080-MIB", "pt3080ModeHierarchy"),
        ("PT3080-MIB", "pt3080Modeifft"),
        ("PT3080-MIB", "pt3080ModeCodeRateHighPrio"),
        ("PT3080-MIB", "pt3080ModeCodeRateLowPrio"),
        ("PT3080-MIB", "pt3080ModeConstellation"),
        ("PT3080-MIB", "pt3080ModeGuardInterval"),
        ("PT3080-MIB", "pt3080ModeCellID"),
        ("PT3080-MIB", "pt3080ModeEnableCellID"),
        ("PT3080-MIB", "pt3080ModeDeepInterleaver"),
        ("PT3080-MIB", "pt3080ModeEnableDVBH"),
        ("PT3080-MIB", "pt3080ModeMpeFecLowPrio"),
        ("PT3080-MIB", "pt3080ModeMpeFecHighPrio"),
        ("PT3080-MIB", "pt3080ModeTimeSlicingLowPrio"),
        ("PT3080-MIB", "pt3080ModeTimeSlicingHighPrio"),
        ("PT3080-MIB", "pt3080ModeSfnDelayOffset"),
        ("PT3080-MIB", "pt3080ModeTxIdent"),
        ("PT3080-MIB", "pt3080ModeMipControl"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayHP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayMinHP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayMaxHP"),
        ("PT3080-MIB", "pt3080ModeMaxNetworkDelayHP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayMarginHP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayLP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayMinLP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayMaxLP"),
        ("PT3080-MIB", "pt3080ModeMaxNetworkDelayLP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayMarginLP"),
        ("PT3080-MIB", "pt3080ModeNetworkDelayReset"),
        ("PT3080-MIB", "pt3080ModeDefaultMIPOutputPower"),
        ("PT3080-MIB", "pt3080ModeDefaultMIPOutputTimeOffset"),
        ("PT3080-MIB", "pt3080ModeDefaultMIPOutputCellID"),
        ("PT3080-MIB", "pt3080ModeDefaultMIPOutputFreqOffset"),
        ("PT3080-MIB", "pt3080ModeMIPMaxSFNDelay"),
        ("PT3080-MIB", "pt3080ModeMipControlOutputPower"),
        ("PT3080-MIB", "pt3080ModeMipControlOutputTimeOffset"),
        ("PT3080-MIB", "pt3080ModeMipControlOutputCellId"),
        ("PT3080-MIB", "pt3080ModeMipControlOutputFreqOffset"),
        ("PT3080-MIB", "pt3080ModeMfnKeepNullPackets"))
)
if mibBuilder.loadTexts:
    pt3080ModeGroup.setStatus("current")

pt3080InputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 3)
)
pt3080InputGroup.setObjects(
      *(("PT3080-MIB", "pt3080InputASITSPrimarySource"),
        ("PT3080-MIB", "pt3080InputASITSSecondarySource"),
        ("PT3080-MIB", "pt3080InputASIAutoRoutingPolicy"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMaxPATDelay"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMaxPATDelayEnable"),
        ("PT3080-MIB", "pt3080InputTSPrimaryExpectedTSID"),
        ("PT3080-MIB", "pt3080InputTSPrimaryExpectedTSIDEnable"),
        ("PT3080-MIB", "pt3080InputTSPrimaryExpectedNWID"),
        ("PT3080-MIB", "pt3080InputTSPrimaryExpectedNWIDEnable"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMaxStuffingrate"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMaxStuffingrateEnable"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMinDelaymargin"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMinDelaymarginEnable"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMaxMissingmip"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMaxMissingmipEnable"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMaxPATDelay"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMaxPATDelayEnable"),
        ("PT3080-MIB", "pt3080InputTSSecondaryExpectedTSID"),
        ("PT3080-MIB", "pt3080InputTSSecondaryExpectedTSIDEnable"),
        ("PT3080-MIB", "pt3080InputTSSecondaryExpectedNWID"),
        ("PT3080-MIB", "pt3080InputTSSecondaryExpectedNWIDEnable"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMaxStuffingrate"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMaxStuffingrateEnable"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMinDelaymargin"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMinDelaymarginEnable"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMaxMissingmip"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMaxMissingmipEnable"),
        ("PT3080-MIB", "pt3080InputTSPrimaryMaxStsJitter"),
        ("PT3080-MIB", "pt3080InputTSSecondaryMaxStsJitter"),
        ("PT3080-MIB", "pt3080InputTSPrimaryStatus"),
        ("PT3080-MIB", "pt3080InputTSSecondaryStatus"),
        ("PT3080-MIB", "pt3080InputTSHp"),
        ("PT3080-MIB", "pt3080InputTSLp"),
        ("PT3080-MIB", "pt3080InputEffectiveAutoroutingPolicy"),
        ("PT3080-MIB", "pt3080InputTSHpBitrate"),
        ("PT3080-MIB", "pt3080InputTSLpBitrate"),
        ("PT3080-MIB", "pt3080InputTSHpPacketsBuffered"),
        ("PT3080-MIB", "pt3080InputTSHpPacketSize"),
        ("PT3080-MIB", "pt3080InputTSHpStuffingrate"),
        ("PT3080-MIB", "pt3080InputTSHpTSID"),
        ("PT3080-MIB", "pt3080InputTSLpPacketsBuffered"),
        ("PT3080-MIB", "pt3080InputTSLpPacketSize"),
        ("PT3080-MIB", "pt3080InputTSLpStuffingrate"),
        ("PT3080-MIB", "pt3080InputTSLpTSID"),
        ("PT3080-MIB", "pt3080InputTSHpNWID"),
        ("PT3080-MIB", "pt3080InputTSLpNWID"),
        ("PT3080-MIB", "pt3080InputTSPrimaryStsJitter"),
        ("PT3080-MIB", "pt3080InputTSPrimaryStsJitterMax"),
        ("PT3080-MIB", "pt3080InputTSPrimaryStsJitterMin"),
        ("PT3080-MIB", "pt3080InputTSPrimaryStsJitterReset"),
        ("PT3080-MIB", "pt3080InputTSSecondaryStsJitter"),
        ("PT3080-MIB", "pt3080InputTSSecondaryStsJitterMax"),
        ("PT3080-MIB", "pt3080InputTSSecondaryStsJitterMin"),
        ("PT3080-MIB", "pt3080InputTSSecondaryStsJitterReset"),
        ("PT3080-MIB", "pt3080InputRefDevType"),
        ("PT3080-MIB", "pt3080InputRefCalDate"),
        ("PT3080-MIB", "pt3080InputRefCalVer"),
        ("PT3080-MIB", "pt3080InputRefDirection"),
        ("PT3080-MIB", "pt3080InputRefSource"),
        ("PT3080-MIB", "pt3080InputRefStatus"),
        ("PT3080-MIB", "pt3080InputRef10MhzImpedance"),
        ("PT3080-MIB", "pt3080InputRef10MhzHoldoverDelay"),
        ("PT3080-MIB", "pt3080InputRef10MhzHoldoverForever"),
        ("PT3080-MIB", "pt3080InputRef1PPSImpedance"),
        ("PT3080-MIB", "pt3080InputRef1PPSHoldoverDelay"),
        ("PT3080-MIB", "pt3080InputRef1PPSHoldoverForever"),
        ("PT3080-MIB", "pt3080InputRef1PPSTrigSlope"),
        ("PT3080-MIB", "pt3080InputRef1PPSTrigLevel"),
        ("PT3080-MIB", "pt3080InputASIAutoRoutingDelayHp2Lp"),
        ("PT3080-MIB", "pt3080InputASIAutoRoutingDelayLp2Hp"),
        ("PT3080-MIB", "pt3080InputASIHoldoverTimeout"))
)
if mibBuilder.loadTexts:
    pt3080InputGroup.setStatus("current")

pt3080OutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 4)
)
pt3080OutputGroup.setObjects(
      *(("PT3080-MIB", "pt3080OutputIfEnable"),
        ("PT3080-MIB", "pt3080OutputIfFrequency"),
        ("PT3080-MIB", "pt3080OutputIfPolarity"),
        ("PT3080-MIB", "pt3080OutputIfLevel"),
        ("PT3080-MIB", "pt3080OutputMode"),
        ("PT3080-MIB", "pt3080OutputEffectiveLevel"),
        ("PT3080-MIB", "pt3080OutputActualLevel"),
        ("PT3080-MIB", "pt3080OutputPolarity"),
        ("PT3080-MIB", "pt3080OutputRfFrequency"),
        ("PT3080-MIB", "pt3080OutputRfFrequencyOffset"),
        ("PT3080-MIB", "pt3080OutputRfLevel"),
        ("PT3080-MIB", "pt3080OutputRfCableMode"),
        ("PT3080-MIB", "pt3080OutputRfCableConstantLevelOffset"),
        ("PT3080-MIB", "pt3080OutputRfCableFrequencyLevelOffset0"),
        ("PT3080-MIB", "pt3080OutputRfCableFrequencyLevelOffset1"),
        ("PT3080-MIB", "pt3080OutputRfCableFrequencyLevelOffset2"),
        ("PT3080-MIB", "pt3080OutputRfCableFrequencyLevelOffset3"),
        ("PT3080-MIB", "pt3080OutputRfCableFrequencyLevelOffset4"),
        ("PT3080-MIB", "pt3080OutputRfCableFrequencyLevelOffset5"),
        ("PT3080-MIB", "pt3080OutputRfDetectedActualLevel"),
        ("PT3080-MIB", "pt3080OutputRfDetectedLowerLevelLimit"),
        ("PT3080-MIB", "pt3080OutputRfDetectedLowerLevelcontrol"),
        ("PT3080-MIB", "pt3080OutputRfDetectedHigherLevelLimit"),
        ("PT3080-MIB", "pt3080OutputRfDetectedHigherLevelcontrol"),
        ("PT3080-MIB", "pt3080OutputRfAlcControl"),
        ("PT3080-MIB", "pt3080OutputRfAlcSense"),
        ("PT3080-MIB", "pt3080OutputRfAlcSetpointPort1"),
        ("PT3080-MIB", "pt3080OutputRfAlcSetpointPort2"),
        ("PT3080-MIB", "pt3080OutputRfAlcStatus"),
        ("PT3080-MIB", "pt3080OutputRfAlcStatusInformation"),
        ("PT3080-MIB", "pt3080OutputBandwidth"),
        ("PT3080-MIB", "pt3080OutputChannel"),
        ("PT3080-MIB", "pt3080OutputSynchronized"),
        ("PT3080-MIB", "pt3080OutputMute"),
        ("PT3080-MIB", "pt3080OutputPowerLevel"))
)
if mibBuilder.loadTexts:
    pt3080OutputGroup.setStatus("current")

pt3080GpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 7)
)
pt3080GpsGroup.setObjects(
      *(("PT3080-MIB", "pt3080GpsBias"),
        ("PT3080-MIB", "pt3080GpsbiasVoltage"),
        ("PT3080-MIB", "pt3080GpsCableDelay"),
        ("PT3080-MIB", "pt3080GpsHoldoverForever"),
        ("PT3080-MIB", "pt3080GpsHoldoverTime"),
        ("PT3080-MIB", "pt3080GpsSatelliteSystemGPS"),
        ("PT3080-MIB", "pt3080GpsSatelliteSystemGLONASS"),
        ("PT3080-MIB", "pt3080GpsSatelliteSystemGALILEO"),
        ("PT3080-MIB", "pt3080GpsSatelliteSystemCOMPASS"),
        ("PT3080-MIB", "pt3080GpsVersion"),
        ("PT3080-MIB", "pt3080Gps1PPSStatus"),
        ("PT3080-MIB", "pt3080GpsState"),
        ("PT3080-MIB", "pt3080GpsVisibleSatellitesSnr"),
        ("PT3080-MIB", "pt3080GpsVisibleSatellites"),
        ("PT3080-MIB", "pt3080GpsTrackedSatellites"),
        ("PT3080-MIB", "pt3080GpsLongtitude"),
        ("PT3080-MIB", "pt3080GpsLatitude"),
        ("PT3080-MIB", "pt3080GpsAltitude"))
)
if mibBuilder.loadTexts:
    pt3080GpsGroup.setStatus("current")

pt3080ChannelFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 8)
)
pt3080ChannelFilterGroup.setObjects(
    ("PT3080-MIB", "pt3080ChannelFiltersSelect")
)
if mibBuilder.loadTexts:
    pt3080ChannelFilterGroup.setStatus("current")

pt3080TSoIPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 10)
)
pt3080TSoIPGroup.setObjects(
      *(("PT3080-MIB", "pt3080TSoIPRx1ReceiverEnable"),
        ("PT3080-MIB", "pt3080TSoIPRx2ReceiverEnable"),
        ("PT3080-MIB", "pt3080TSoIPRx1LanSelect"),
        ("PT3080-MIB", "pt3080TSoIPRx2LanSelect"),
        ("PT3080-MIB", "pt3080TSoIPRx1Multicast"),
        ("PT3080-MIB", "pt3080TSoIPRx2Multicast"),
        ("PT3080-MIB", "pt3080TSoIPRx1Protocol"),
        ("PT3080-MIB", "pt3080TSoIPRx2Protocol"),
        ("PT3080-MIB", "pt3080TSoIPRx1Portnumber"),
        ("PT3080-MIB", "pt3080TSoIPRx2Portnumber"),
        ("PT3080-MIB", "pt3080TSoIPRx1PacketErrorRatioLimit"),
        ("PT3080-MIB", "pt3080TSoIPRx2PacketErrorRatioLimit"),
        ("PT3080-MIB", "pt3080TSoIPRx1MinumimLatency"),
        ("PT3080-MIB", "pt3080TSoIPRx2MinumimLatency"),
        ("PT3080-MIB", "pt3080TSoIPRx1SyncTimeout"),
        ("PT3080-MIB", "pt3080TSoIPRx2SyncTimeout"),
        ("PT3080-MIB", "pt3080TSoIPRx1Status"),
        ("PT3080-MIB", "pt3080TSoIPRx2Status"),
        ("PT3080-MIB", "pt3080TSoIPRx1CurrentIPAddress"),
        ("PT3080-MIB", "pt3080TSoIPRx2CurrentIPAddress"),
        ("PT3080-MIB", "pt3080TSoIPRx1IpBitrate"),
        ("PT3080-MIB", "pt3080TSoIPRx2IpBitrate"),
        ("PT3080-MIB", "pt3080TSoIPRx1PacketErrorRatio"),
        ("PT3080-MIB", "pt3080TSoIPRx2PacketErrorRatio"),
        ("PT3080-MIB", "pt3080TSoIPRx1SequenceErrors"),
        ("PT3080-MIB", "pt3080TSoIPRx2SequenceErrors"),
        ("PT3080-MIB", "pt3080TSoIPRx1LostIPFrames"),
        ("PT3080-MIB", "pt3080TSoIPRx2LostIPFrames"),
        ("PT3080-MIB", "pt3080TSoIPRx1CorrectedIPFrames"),
        ("PT3080-MIB", "pt3080TSoIPRx2CorrectedIPFrames"),
        ("PT3080-MIB", "pt3080TSoIPRx1OverrunIPFrames"),
        ("PT3080-MIB", "pt3080TSoIPRx2OverrunIPFrames"),
        ("PT3080-MIB", "pt3080TSoIPRx1PacketsPerFrame"),
        ("PT3080-MIB", "pt3080TSoIPRx2PacketsPerFrame"),
        ("PT3080-MIB", "pt3080TSoIPRx1TSPacketSize"),
        ("PT3080-MIB", "pt3080TSoIPRx2TSPacketSize"),
        ("PT3080-MIB", "pt3080TSoIPRx1FecColumn"),
        ("PT3080-MIB", "pt3080TSoIPRx2FecColumn"),
        ("PT3080-MIB", "pt3080TSoIPRx1FecRow"),
        ("PT3080-MIB", "pt3080TSoIPRx2FecRow"),
        ("PT3080-MIB", "pt3080TSoIPRx1QueueSize"),
        ("PT3080-MIB", "pt3080TSoIPRx2QueueSize"),
        ("PT3080-MIB", "pt3080TSoIPRx1CurrentLatency"),
        ("PT3080-MIB", "pt3080TSoIPRx2CurrentLatency"))
)
if mibBuilder.loadTexts:
    pt3080TSoIPGroup.setStatus("current")

pt3080MonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 12)
)
pt3080MonitorGroup.setObjects(
      *(("PT3080-MIB", "pt3080MonitorSource"),
        ("PT3080-MIB", "pt3080MonitorTSoIPEnable"),
        ("PT3080-MIB", "pt3080MonitorTSoIPSource"),
        ("PT3080-MIB", "pt3080MonitorTSoIPMulticastLanSelect"),
        ("PT3080-MIB", "pt3080MonitorTSoIPDestIPAddress"),
        ("PT3080-MIB", "pt3080MonitorTSoIPDestPort"),
        ("PT3080-MIB", "pt3080MonitorTSoIPProtocol"),
        ("PT3080-MIB", "pt3080MonitorTSoIPEnableFec"),
        ("PT3080-MIB", "pt3080MonitorTSoIPFecColumn"),
        ("PT3080-MIB", "pt3080MonitorTSoIPFecRow"),
        ("PT3080-MIB", "pt3080MonitorTSoIPFecSkew"),
        ("PT3080-MIB", "pt3080MonitorTSoIPKeepNullPackets"),
        ("PT3080-MIB", "pt3080MonitorTSoIPPacketsPerFrame"),
        ("PT3080-MIB", "pt3080MonitorTSoIPUDPChecksum"),
        ("PT3080-MIB", "pt3080MonitorTSoIPDSCP"),
        ("PT3080-MIB", "pt3080MonitorTSoIPTTL"),
        ("PT3080-MIB", "pt3080MonitorTSoIPGenerateError"),
        ("PT3080-MIB", "pt3080MonitorTSoIPIpBitrate"),
        ("PT3080-MIB", "pt3080MonitorTSoIPTSSize"),
        ("PT3080-MIB", "pt3080MonitorTSoIPLostIPFrames"))
)
if mibBuilder.loadTexts:
    pt3080MonitorGroup.setStatus("current")

pt3080TestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 13)
)
pt3080TestGroup.setObjects(
      *(("PT3080-MIB", "pt3080TestEnable"),
        ("PT3080-MIB", "pt3080TestEnableReconnect"),
        ("PT3080-MIB", "pt3080TestScarrierLevel"),
        ("PT3080-MIB", "pt3080TestscarrierFrequencyOffset"))
)
if mibBuilder.loadTexts:
    pt3080TestGroup.setStatus("current")

pt3080AlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 14)
)
pt3080AlarmGroup.setObjects(
      *(("PT3080-MIB", "pt3080GroupAlarmDescription"),
        ("PT3080-MIB", "pt3080GroupAlarmState"),
        ("PT3080-MIB", "pt3080GroupAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080GroupAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080GroupAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080GroupAlarmActionTrap"),
        ("PT3080-MIB", "pt3080GroupAlarmActionEmail"),
        ("PT3080-MIB", "pt3080GroupAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080GroupAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmDescription"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmState"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmActionTrap"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmActionEmail"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080ASITSPrimaryAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmDescription"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmState"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmActionTrap"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmActionEmail"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080ASITSSecondaryAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080SFNAlarmDescription"),
        ("PT3080-MIB", "pt3080SFNAlarmState"),
        ("PT3080-MIB", "pt3080SFNAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080SFNAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080SFNAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080SFNAlarmActionTrap"),
        ("PT3080-MIB", "pt3080SFNAlarmActionEmail"),
        ("PT3080-MIB", "pt3080SFNAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080SFNAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080TSoIPAlarmDescription"),
        ("PT3080-MIB", "pt3080TSoIPAlarmState"),
        ("PT3080-MIB", "pt3080TSoIPAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080TSoIPAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080TSoIPAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080TSoIPAlarmActionTrap"),
        ("PT3080-MIB", "pt3080TSoIPAlarmActionEmail"),
        ("PT3080-MIB", "pt3080TSoIPAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080TSoIPAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmDescription"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmState"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmActionTrap"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmActionEmail"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080DemodulatorAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080ReferenceAlarmDescription"),
        ("PT3080-MIB", "pt3080ReferenceAlarmState"),
        ("PT3080-MIB", "pt3080ReferenceAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080ReferenceAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080ReferenceAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080ReferenceAlarmActionTrap"),
        ("PT3080-MIB", "pt3080ReferenceAlarmActionEmail"),
        ("PT3080-MIB", "pt3080ReferenceAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080ReferenceAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080RFAlarmDescription"),
        ("PT3080-MIB", "pt3080RFAlarmState"),
        ("PT3080-MIB", "pt3080RFAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080RFAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080RFAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080RFAlarmActionTrap"),
        ("PT3080-MIB", "pt3080RFAlarmActionEmail"),
        ("PT3080-MIB", "pt3080RFAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080RFAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080GPSAlarmDescription"),
        ("PT3080-MIB", "pt3080GPSAlarmState"),
        ("PT3080-MIB", "pt3080GPSAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080GPSAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080GPSAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080GPSAlarmActionTrap"),
        ("PT3080-MIB", "pt3080GPSAlarmActionEmail"),
        ("PT3080-MIB", "pt3080GPSAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080GPSAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080ExternalAlarmDescription"),
        ("PT3080-MIB", "pt3080ExternalAlarmState"),
        ("PT3080-MIB", "pt3080ExternalAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080ExternalAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080ExternalAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080ExternalAlarmActionTrap"),
        ("PT3080-MIB", "pt3080ExternalAlarmActionEmail"),
        ("PT3080-MIB", "pt3080ExternalAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080ExternalAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmDescription"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmState"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmActionTrap"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmActionEmail"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080HWMonitorAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080CommsAlarmDescription"),
        ("PT3080-MIB", "pt3080CommsAlarmState"),
        ("PT3080-MIB", "pt3080CommsAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080CommsAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080CommsAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080CommsAlarmActionTrap"),
        ("PT3080-MIB", "pt3080CommsAlarmActionEmail"),
        ("PT3080-MIB", "pt3080CommsAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080CommsAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080InternalAlarmDescription"),
        ("PT3080-MIB", "pt3080InternalAlarmState"),
        ("PT3080-MIB", "pt3080InternalAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080InternalAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080InternalAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080InternalAlarmActionTrap"),
        ("PT3080-MIB", "pt3080InternalAlarmActionEmail"),
        ("PT3080-MIB", "pt3080InternalAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080InternalAlarmActionForceMode"),
        ("PT3080-MIB", "pt3080ASIAlarmDescription"),
        ("PT3080-MIB", "pt3080ASIAlarmState"),
        ("PT3080-MIB", "pt3080ASIAlarmActionEventlog"),
        ("PT3080-MIB", "pt3080ASIAlarmActionRelay1"),
        ("PT3080-MIB", "pt3080ASIAlarmActionRelay2"),
        ("PT3080-MIB", "pt3080ASIAlarmActionTrap"),
        ("PT3080-MIB", "pt3080ASIAlarmActionEmail"),
        ("PT3080-MIB", "pt3080ASIAlarmActionAlarmLED"),
        ("PT3080-MIB", "pt3080ASIAlarmActionForceMode"))
)
if mibBuilder.loadTexts:
    pt3080AlarmGroup.setStatus("current")

pt3080PresetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 15)
)
pt3080PresetGroup.setObjects(
      *(("PT3080-MIB", "pt3080PresetName"),
        ("PT3080-MIB", "pt3080PresetRecall"),
        ("PT3080-MIB", "pt3080PresetStore"))
)
if mibBuilder.loadTexts:
    pt3080PresetGroup.setStatus("current")

pt3080EventlogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 16)
)
pt3080EventlogGroup.setObjects(
      *(("PT3080-MIB", "pt3080EventlogID"),
        ("PT3080-MIB", "pt3080EventlogTimestamp"),
        ("PT3080-MIB", "pt3080EventlogText"),
        ("PT3080-MIB", "pt3080EventlogClear"),
        ("PT3080-MIB", "pt3080EventlogEnable"),
        ("PT3080-MIB", "pt3080EventlogMode"))
)
if mibBuilder.loadTexts:
    pt3080EventlogGroup.setStatus("current")

pt3080CommsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 17)
)
pt3080CommsGroup.setObjects(
      *(("PT3080-MIB", "pt3080CommsAccessPasswordObserver"),
        ("PT3080-MIB", "pt3080CommsAccessPasswordOperator"),
        ("PT3080-MIB", "pt3080CommsAccessPasswordAdministrator"),
        ("PT3080-MIB", "pt3080CommsStaticRouteType"),
        ("PT3080-MIB", "pt3080CommsStaticRoutePrefix"),
        ("PT3080-MIB", "pt3080CommsStaticRoutePrefixSize"),
        ("PT3080-MIB", "pt3080CommsStaticRouteTarget"),
        ("PT3080-MIB", "pt3080CommsStaticRoutePhysicalInterface"),
        ("PT3080-MIB", "pt3080CommsAlarmEmailReceiver"),
        ("PT3080-MIB", "pt3080CommsSeparatedSwitchPorts"),
        ("PT3080-MIB", "pt3080CommsBroadcastStormProtection"),
        ("PT3080-MIB", "pt3080CommsLocalPhysicalInterface"),
        ("PT3080-MIB", "pt3080CommsLocalDhcpMode"),
        ("PT3080-MIB", "pt3080CommsLocalStaticIpAddr"),
        ("PT3080-MIB", "pt3080CommsLocalStaticNetmask"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastAddr"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastSourceFilterMode"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastSourceFilterAddress1"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastSourceFilterAddress2"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastSourceFilterAddress3"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastSourceFilterAddress4"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastSourceFilterAddress5"),
        ("PT3080-MIB", "pt3080CommsLocalIpMulticastSourceFilterAddress6"),
        ("PT3080-MIB", "pt3080CommsLocalVlanEnable"),
        ("PT3080-MIB", "pt3080CommsLocalVlanId"),
        ("PT3080-MIB", "pt3080CommsLocalServiceSNMP"),
        ("PT3080-MIB", "pt3080CommsLocalServiceSCPI"),
        ("PT3080-MIB", "pt3080CommsLocalServiceTSoIP"),
        ("PT3080-MIB", "pt3080CommsLocalServiceRIP"),
        ("PT3080-MIB", "pt3080CommsLocalCurrentIpAddr"),
        ("PT3080-MIB", "pt3080CommsLocalCurrentNetmask"),
        ("PT3080-MIB", "pt3080CommsRemoteEnable"),
        ("PT3080-MIB", "pt3080CommsRemotePhysicalInterface"),
        ("PT3080-MIB", "pt3080CommsRemoteDhcpMode"),
        ("PT3080-MIB", "pt3080CommsRemoteStaticIpAddr"),
        ("PT3080-MIB", "pt3080CommsRemoteStaticNetmask"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastAddr"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastSourceFilterMode"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastSourceFilterAddress1"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastSourceFilterAddress2"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastSourceFilterAddress3"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastSourceFilterAddress4"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastSourceFilterAddress5"),
        ("PT3080-MIB", "pt3080CommsRemoteIpMulticastSourceFilterAddress6"),
        ("PT3080-MIB", "pt3080CommsRemoteVlanEnable"),
        ("PT3080-MIB", "pt3080CommsRemoteVlanId"),
        ("PT3080-MIB", "pt3080CommsRemoteServiceSNMP"),
        ("PT3080-MIB", "pt3080CommsRemoteServiceSCPI"),
        ("PT3080-MIB", "pt3080CommsRemoteServiceTSoIP"),
        ("PT3080-MIB", "pt3080CommsRemoteServiceWeb"),
        ("PT3080-MIB", "pt3080CommsRemoteServiceRIP"),
        ("PT3080-MIB", "pt3080CommsRemoteCurrentIpAddr"),
        ("PT3080-MIB", "pt3080CommsRemoteCurrentNetmask"),
        ("PT3080-MIB", "pt3080CommsGbeAdminEnable"),
        ("PT3080-MIB", "pt3080CommsGbeAdminPhysicalInterface"),
        ("PT3080-MIB", "pt3080CommsGbeAdminDhcpMode"),
        ("PT3080-MIB", "pt3080CommsGbeAdminStaticIpAddr"),
        ("PT3080-MIB", "pt3080CommsGbeAdminStaticNetmask"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastAddr"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastSourceFilterMode"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastSourceFilterAddress1"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastSourceFilterAddress2"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastSourceFilterAddress3"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastSourceFilterAddress4"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastSourceFilterAddress5"),
        ("PT3080-MIB", "pt3080CommsGbeAdminIpMulticastSourceFilterAddress6"),
        ("PT3080-MIB", "pt3080CommsGbeAdminVlanEnable"),
        ("PT3080-MIB", "pt3080CommsGbeAdminVlanId"),
        ("PT3080-MIB", "pt3080CommsGbeAdminServiceSNMP"),
        ("PT3080-MIB", "pt3080CommsGbeAdminServiceSCPI"),
        ("PT3080-MIB", "pt3080CommsGbeAdminServiceTSoIP"),
        ("PT3080-MIB", "pt3080CommsGbeAdminServiceWeb"),
        ("PT3080-MIB", "pt3080CommsGbeAdminServiceRIP"),
        ("PT3080-MIB", "pt3080CommsGbeAdminCurrentIpAddr"),
        ("PT3080-MIB", "pt3080CommsGbeAdminCurrentNetmask"),
        ("PT3080-MIB", "pt3080CommsBackupEnable"),
        ("PT3080-MIB", "pt3080CommsBackupPhysicalInterface"),
        ("PT3080-MIB", "pt3080CommsBackupDhcpMode"),
        ("PT3080-MIB", "pt3080CommsBackupStaticIpAddr"),
        ("PT3080-MIB", "pt3080CommsBackupStaticNetmask"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastAddr"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastSourceFilterMode"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastSourceFilterAddress1"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastSourceFilterAddress2"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastSourceFilterAddress3"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastSourceFilterAddress4"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastSourceFilterAddress5"),
        ("PT3080-MIB", "pt3080CommsBackupIpMulticastSourceFilterAddress6"),
        ("PT3080-MIB", "pt3080CommsBackupVlanEnable"),
        ("PT3080-MIB", "pt3080CommsBackupVlanId"),
        ("PT3080-MIB", "pt3080CommsBackupServiceSNMP"),
        ("PT3080-MIB", "pt3080CommsBackupServiceSCPI"),
        ("PT3080-MIB", "pt3080CommsBackupServiceTSoIP"),
        ("PT3080-MIB", "pt3080CommsBackupServiceWeb"),
        ("PT3080-MIB", "pt3080CommsBackupServiceRIP"),
        ("PT3080-MIB", "pt3080CommsBackupCurrentIpAddr"),
        ("PT3080-MIB", "pt3080CommsBackupCurrentNetmask"),
        ("PT3080-MIB", "pt3080CommsPortEnable"),
        ("PT3080-MIB", "pt3080CommsPortPhysicalInterface"),
        ("PT3080-MIB", "pt3080CommsPortDhcpMode"),
        ("PT3080-MIB", "pt3080CommsPortStaticIpAddr"),
        ("PT3080-MIB", "pt3080CommsPortStaticNetmask"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastAddr"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastSourceFilterMode"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastSourceFilterAddress1"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastSourceFilterAddress2"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastSourceFilterAddress3"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastSourceFilterAddress4"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastSourceFilterAddress5"),
        ("PT3080-MIB", "pt3080CommsPortIpMulticastSourceFilterAddress6"),
        ("PT3080-MIB", "pt3080CommsPortVlanEnable"),
        ("PT3080-MIB", "pt3080CommsPortVlanId"),
        ("PT3080-MIB", "pt3080CommsPortServiceSNMP"),
        ("PT3080-MIB", "pt3080CommsPortServiceSCPI"),
        ("PT3080-MIB", "pt3080CommsPortServiceTSoIP"),
        ("PT3080-MIB", "pt3080CommsPortServiceWeb"),
        ("PT3080-MIB", "pt3080CommsPortServiceRIP"),
        ("PT3080-MIB", "pt3080CommsPortCurrentIpAddr"),
        ("PT3080-MIB", "pt3080CommsPortCurrentNetmask"),
        ("PT3080-MIB", "pt3080CommsSNMPServicePort"),
        ("PT3080-MIB", "pt3080CommsSNMPReadOnlyCommunity"),
        ("PT3080-MIB", "pt3080CommsSNMPReadWriteCommunity"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapCommunity"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestination"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestination2"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestination3"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestination4"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestination5"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestinationPort"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestinationPort2"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestinationPort3"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestinationPort4"),
        ("PT3080-MIB", "pt3080CommsSNMPTrapDestinationPort5"),
        ("PT3080-MIB", "pt3080CommsStaticGateway"),
        ("PT3080-MIB", "pt3080CommsCurrentGateway"),
        ("PT3080-MIB", "pt3080CommsStaticHostname"),
        ("PT3080-MIB", "pt3080CommsCurrentHostname"),
        ("PT3080-MIB", "pt3080CommsStaticDNSDomain"),
        ("PT3080-MIB", "pt3080CommsCurrentDNSDomain"),
        ("PT3080-MIB", "pt3080CommsStaticDNS1ServerAddress"),
        ("PT3080-MIB", "pt3080CommsStaticDNS2ServerAddress"),
        ("PT3080-MIB", "pt3080CommsStaticDNS3ServerAddress"),
        ("PT3080-MIB", "pt3080CommsCurrentDNS1ServerAddress"),
        ("PT3080-MIB", "pt3080CommsCurrentDNS2ServerAddress"),
        ("PT3080-MIB", "pt3080CommsCurrentDNS3ServerAddress"),
        ("PT3080-MIB", "pt3080CommsStaticNtpServerAddress"),
        ("PT3080-MIB", "pt3080CommsCurrentNtpServerAddress"),
        ("PT3080-MIB", "pt3080CommsEmailServerAddress"),
        ("PT3080-MIB", "pt3080CommsWebServicePort"),
        ("PT3080-MIB", "pt3080CommsSCPIServicePort"),
        ("PT3080-MIB", "pt3080CommsSCPIServerBaudrate"),
        ("PT3080-MIB", "pt3080CommsSCPIUartInterface"),
        ("PT3080-MIB", "pt3080CommsRipPort"),
        ("PT3080-MIB", "pt3080CommsIGMPVersion"),
        ("PT3080-MIB", "pt3080CommsIGMPQueryRobustnessCount"),
        ("PT3080-MIB", "pt3080CommsIGMPv3UnsolicitedReportInterval"),
        ("PT3080-MIB", "pt3080CommsIGMPv2UnsolicitedReportInterval"),
        ("PT3080-MIB", "pt3080CommsAccessAllowed"),
        ("PT3080-MIB", "pt3080CommsAccessAllowedTimeout"),
        ("PT3080-MIB", "pt3080CommsAccessAllowedTimeLeft"))
)
if mibBuilder.loadTexts:
    pt3080CommsGroup.setStatus("current")

pt3080DemodulatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 24)
)
pt3080DemodulatorGroup.setObjects(
      *(("PT3080-MIB", "pt3080DemodulatorFollowMode"),
        ("PT3080-MIB", "pt3080Demodulator1Available"),
        ("PT3080-MIB", "pt3080Demodulator2Available"),
        ("PT3080-MIB", "pt3080Demodulator1FWVersion"),
        ("PT3080-MIB", "pt3080Demodulator2FWVersion"),
        ("PT3080-MIB", "pt3080Demodulator1OutputTS"),
        ("PT3080-MIB", "pt3080Demodulator2OutputTS"),
        ("PT3080-MIB", "pt3080Demodulator1MerLimit"),
        ("PT3080-MIB", "pt3080Demodulator2MerLimit"),
        ("PT3080-MIB", "pt3080Demodulator1PreVirterbiErrorRateLimit"),
        ("PT3080-MIB", "pt3080Demodulator2PreVirterbiErrorRateLimit"),
        ("PT3080-MIB", "pt3080Demodulator1PostVirterbiErrorRateLimit"),
        ("PT3080-MIB", "pt3080Demodulator2PostVirterbiErrorRateLimit"),
        ("PT3080-MIB", "pt3080Demodulator1FelStatus"),
        ("PT3080-MIB", "pt3080Demodulator2FelStatus"),
        ("PT3080-MIB", "pt3080Demodulator1UncorrectedPackets"),
        ("PT3080-MIB", "pt3080Demodulator2UncorrectedPackets"),
        ("PT3080-MIB", "pt3080Demodulator1Mer"),
        ("PT3080-MIB", "pt3080Demodulator2Mer"),
        ("PT3080-MIB", "pt3080Demodulator1PreVirterbiErrorRate"),
        ("PT3080-MIB", "pt3080Demodulator2PreVirterbiErrorRate"),
        ("PT3080-MIB", "pt3080Demodulator1PostVirterbiErrorRate"),
        ("PT3080-MIB", "pt3080Demodulator2PostVirterbiErrorRate"),
        ("PT3080-MIB", "pt3080Demodulator1ActualGuardInterval"),
        ("PT3080-MIB", "pt3080Demodulator2ActualGuardInterval"),
        ("PT3080-MIB", "pt3080Demodulator1Actualifft"),
        ("PT3080-MIB", "pt3080Demodulator2Actualifft"),
        ("PT3080-MIB", "pt3080Demodulator1ActualConstellation"),
        ("PT3080-MIB", "pt3080Demodulator2ActualConstellation"),
        ("PT3080-MIB", "pt3080Demodulator1ActualHierarchy"),
        ("PT3080-MIB", "pt3080Demodulator2ActualHierarchy"),
        ("PT3080-MIB", "pt3080Demodulator1ActualCodeRateHighPrio"),
        ("PT3080-MIB", "pt3080Demodulator2ActualCodeRateHighPrio"),
        ("PT3080-MIB", "pt3080Demodulator1ActualCodeRateLowPrio"),
        ("PT3080-MIB", "pt3080Demodulator2ActualCodeRateLowPrio"),
        ("PT3080-MIB", "pt3080Demodulator1ActualDeepInterleaver"),
        ("PT3080-MIB", "pt3080Demodulator2ActualDeepInterleaver"),
        ("PT3080-MIB", "pt3080Demodulator1ActualMpeFecHighPrio"),
        ("PT3080-MIB", "pt3080Demodulator2ActualMpeFecHighPrio"),
        ("PT3080-MIB", "pt3080Demodulator1ActualMpeFecLowPrio"),
        ("PT3080-MIB", "pt3080Demodulator2ActualMpeFecLowPrio"),
        ("PT3080-MIB", "pt3080Demodulator1ActualTimeSlicingHighPrio"),
        ("PT3080-MIB", "pt3080Demodulator2ActualTimeSlicingHighPrio"),
        ("PT3080-MIB", "pt3080Demodulator1ActualTimeSlicingLowPrio"),
        ("PT3080-MIB", "pt3080Demodulator2ActualTimeSlicingLowPrio"),
        ("PT3080-MIB", "pt3080Demodulator1ActualCellID"),
        ("PT3080-MIB", "pt3080Demodulator2ActualCellID"),
        ("PT3080-MIB", "pt3080Demodulator1ActualDVBHMode"),
        ("PT3080-MIB", "pt3080Demodulator2ActualDVBHMode"))
)
if mibBuilder.loadTexts:
    pt3080DemodulatorGroup.setStatus("current")

pt3080PrecorrectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 25)
)
pt3080PrecorrectorGroup.setObjects(
      *(("PT3080-MIB", "pt3080PrecorrectorLastTurnAroundTime"),
        ("PT3080-MIB", "pt3080PrecorrectorSecondsSinceLastUpdate"),
        ("PT3080-MIB", "pt3080PrecorrectorLinCleanrun"),
        ("PT3080-MIB", "pt3080PrecorrectorNlinCleanrun"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearLoadNeutral"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearLoadFactory"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearUpdateFactoryCurve"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearLoadNeutral"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearLoadFactory"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearUpdateFactoryCurve"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptive"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMode"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearSenseEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorStatus"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorSenseLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorSenseValid"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorSenseBadCount"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorAmplitudeRipple"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorAmplitudeRippleValid"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorGroupDelay"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorGroupDelayValid"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorDiscartedIterations"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearMonitorIterations"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptiveMode"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAdaptiveGroupDelayEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorLinearAttenuation"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptive"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMode"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearSenseEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorStatus"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorSenseLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorSenseValid"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorSenseBadCount"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorLowerShoulderValid"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorUpperShoulderValid"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorDiscartedIterations"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorIterations"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorMer"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorMerValid"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorPapr"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearMonitorPaprValid"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAttenuation"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveMode"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveAveraging"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveMerTarget"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveMerEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis"),
        ("PT3080-MIB", "pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorPaprClipping"),
        ("PT3080-MIB", "pt3080PrecorrectorPaprShaping"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMode"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperAdaptive"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperEnable"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperAdaptiveMode"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperAdaptiveShaping"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorStatus"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorShoulderLevelLower"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorShoulderLevelUpper"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorMer"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorMerValid"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorPapr"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorPaprValid"),
        ("PT3080-MIB", "pt3080PrecorrectorClipperMonitorIterations"))
)
if mibBuilder.loadTexts:
    pt3080PrecorrectorGroup.setStatus("current")

pt3080ReceptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 26)
)
pt3080ReceptionGroup.setObjects(
      *(("PT3080-MIB", "pt3080ReceptionGainControl"),
        ("PT3080-MIB", "pt3080ReceptionGainManualValue"),
        ("PT3080-MIB", "pt3080ReceptionGainLimitEnable"),
        ("PT3080-MIB", "pt3080ReceptionGainLimit"),
        ("PT3080-MIB", "pt3080ReceptionGainCurrent"),
        ("PT3080-MIB", "pt3080ReceptionAGCMode"),
        ("PT3080-MIB", "pt3080ReceptionAGCHysteresis"),
        ("PT3080-MIB", "pt3080ReceptionBandwidth"),
        ("PT3080-MIB", "pt3080ReceptionRFFrequency"),
        ("PT3080-MIB", "pt3080ReceptionRFFrequencyOffset"),
        ("PT3080-MIB", "pt3080ReceptionRFPolarity"),
        ("PT3080-MIB", "pt3080ReceptionRFSquelchEnable"),
        ("PT3080-MIB", "pt3080ReceptionRFSquelchThreshold"),
        ("PT3080-MIB", "pt3080ReceptionRFSquelchHysteresis"),
        ("PT3080-MIB", "pt3080ReceptionRFTrackingFilterEnable"),
        ("PT3080-MIB", "pt3080ReceptionRFifLevel"),
        ("PT3080-MIB", "pt3080ReceptionRFNominalInputLevel"),
        ("PT3080-MIB", "pt3080ReceptionRFInputLevel"),
        ("PT3080-MIB", "pt3080ReceptionRFInputLevelThreshold"),
        ("PT3080-MIB", "pt3080ReceptionRFInputLevelHysteresis"),
        ("PT3080-MIB", "pt3080ReceptionIFFrequency"),
        ("PT3080-MIB", "pt3080ReceptionIFPolarity"),
        ("PT3080-MIB", "pt3080ReceptionIFInputLevel"),
        ("PT3080-MIB", "pt3080ReceptionIFInputPolicy"),
        ("PT3080-MIB", "pt3080ReceptionIFInput"),
        ("PT3080-MIB", "pt3080ReceptionIFRFtoIFHoldoverDelay"),
        ("PT3080-MIB", "pt3080ReceptionIFIFtoRFHoldoverDelay"),
        ("PT3080-MIB", "pt3080ReceptionTunerHWVersion"),
        ("PT3080-MIB", "pt3080ReceptionTunerHWType"),
        ("PT3080-MIB", "pt3080ReceptionTunerHWID"),
        ("PT3080-MIB", "pt3080ReceptionTunerHWSerialNumber"),
        ("PT3080-MIB", "pt3080ReceptionTunerHWCalibrationDate"),
        ("PT3080-MIB", "pt3080ReceptionTunerHWCalibrationDataVersion"),
        ("PT3080-MIB", "pt3080ReceptionTunerHWCalibrationSWVersion"))
)
if mibBuilder.loadTexts:
    pt3080ReceptionGroup.setStatus("current")

pt3080BackplaneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 27)
)
pt3080BackplaneGroup.setObjects(
      *(("PT3080-MIB", "pt3080BackplanePolarityHardMute"),
        ("PT3080-MIB", "pt3080BackplanePolarityRFFail"))
)
if mibBuilder.loadTexts:
    pt3080BackplaneGroup.setStatus("current")

pt3080ASIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 30)
)
pt3080ASIGroup.setObjects(
      *(("PT3080-MIB", "pt3080ASIInput1SyncTimeout"),
        ("PT3080-MIB", "pt3080ASIInput2SyncTimeout"),
        ("PT3080-MIB", "pt3080ASIInput1DataErrorLimit"),
        ("PT3080-MIB", "pt3080ASIInput2DataErrorLimit"),
        ("PT3080-MIB", "pt3080ASIInput1SyncStatus"),
        ("PT3080-MIB", "pt3080ASIInput2SyncStatus"),
        ("PT3080-MIB", "pt3080ASIInput1SyncSignal"),
        ("PT3080-MIB", "pt3080ASIInput2SyncSignal"),
        ("PT3080-MIB", "pt3080ASIInput1SyncTSSize"),
        ("PT3080-MIB", "pt3080ASIInput2SyncTSSize"),
        ("PT3080-MIB", "pt3080ASIInput1LineErrors"),
        ("PT3080-MIB", "pt3080ASIInput2LineErrors"),
        ("PT3080-MIB", "pt3080ASIInput1LineRate"),
        ("PT3080-MIB", "pt3080ASIInput2LineRate"),
        ("PT3080-MIB", "pt3080ASIInput1LineErrorRate"),
        ("PT3080-MIB", "pt3080ASIInput2LineErrorRate"),
        ("PT3080-MIB", "pt3080ASIInput1DataErrors"),
        ("PT3080-MIB", "pt3080ASIInput2DataErrors"),
        ("PT3080-MIB", "pt3080ASIInput1DataRate"),
        ("PT3080-MIB", "pt3080ASIInput2DataRate"),
        ("PT3080-MIB", "pt3080ASIInput1DataErrorRate"),
        ("PT3080-MIB", "pt3080ASIInput2DataErrorRate"),
        ("PT3080-MIB", "pt3080ASIInput1ClearErrorCounters"),
        ("PT3080-MIB", "pt3080ASIInput2ClearErrorCounters"))
)
if mibBuilder.loadTexts:
    pt3080ASIGroup.setStatus("current")

pt3080NotifsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 2, 64)
)
pt3080NotifsGroup.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifsGroup.setStatus("current")


# Notification objects

pt3080NotifModulatorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 3)
)
pt3080NotifModulatorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifModulatorAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 5)
)
pt3080NotifTSPrimaryAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 6)
)
pt3080NotifTSSecondaryAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryAlarm.setStatus(
        "current"
    )

pt3080NotifSFNAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 7)
)
pt3080NotifSFNAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNAlarm.setStatus(
        "current"
    )

pt3080NotifRefenceClockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 8)
)
pt3080NotifRefenceClockAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRefenceClockAlarm.setStatus(
        "current"
    )

pt3080NotifRFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 9)
)
pt3080NotifRFAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRFAlarm.setStatus(
        "current"
    )

pt3080NotifGNSSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 10)
)
pt3080NotifGNSSAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifGNSSAlarm.setStatus(
        "current"
    )

pt3080NotifTSoIPAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 12)
)
pt3080NotifTSoIPAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSoIPAlarm.setStatus(
        "current"
    )

pt3080NotifExternalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 13)
)
pt3080NotifExternalAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalAlarm.setStatus(
        "current"
    )

pt3080NotifHWMonitorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 14)
)
pt3080NotifHWMonitorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifHWMonitorAlarm.setStatus(
        "current"
    )

pt3080NotifCommAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 15)
)
pt3080NotifCommAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifCommAlarm.setStatus(
        "current"
    )

pt3080NotifASIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 16)
)
pt3080NotifASIAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifASIAlarm.setStatus(
        "current"
    )

pt3080NotifInternalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 18)
)
pt3080NotifInternalAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimarySyncLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 21)
)
pt3080NotifTSPrimarySyncLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimarySyncLossAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimarySyncErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 22)
)
pt3080NotifTSPrimarySyncErrorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimarySyncErrorAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryPCRErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 23)
)
pt3080NotifTSPrimaryPCRErrorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryPCRErrorAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryPATLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 24)
)
pt3080NotifTSPrimaryPATLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryPATLossAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryTSIDWrongAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 25)
)
pt3080NotifTSPrimaryTSIDWrongAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryTSIDWrongAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryNWIDWrongAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 26)
)
pt3080NotifTSPrimaryNWIDWrongAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryNWIDWrongAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryStuffingRateExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 27)
)
pt3080NotifTSPrimaryStuffingRateExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryStuffingRateExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryBufferPoolExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 28)
)
pt3080NotifTSPrimaryBufferPoolExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryBufferPoolExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimarySTSJitterExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 29)
)
pt3080NotifTSPrimarySTSJitterExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimarySTSJitterExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryMIPDataMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 30)
)
pt3080NotifTSPrimaryMIPDataMissingAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryMIPDataMissingAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryMIPPriorityBadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 31)
)
pt3080NotifTSPrimaryMIPPriorityBadAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryMIPPriorityBadAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondarySyncLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 32)
)
pt3080NotifTSSecondarySyncLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondarySyncLossAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondarySyncErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 33)
)
pt3080NotifTSSecondarySyncErrorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondarySyncErrorAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryPCRErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 34)
)
pt3080NotifTSSecondaryPCRErrorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryPCRErrorAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryPATLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 35)
)
pt3080NotifTSSecondaryPATLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryPATLossAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryTSIDWrongAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 36)
)
pt3080NotifTSSecondaryTSIDWrongAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryTSIDWrongAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryNWIDWrongAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 37)
)
pt3080NotifTSSecondaryNWIDWrongAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryNWIDWrongAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryStuffingRateExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 38)
)
pt3080NotifTSSecondaryStuffingRateExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryStuffingRateExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryBufferPoolExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 39)
)
pt3080NotifTSSecondaryBufferPoolExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryBufferPoolExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondarySTSJitterExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 40)
)
pt3080NotifTSSecondarySTSJitterExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondarySTSJitterExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryMIPDataMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 41)
)
pt3080NotifTSSecondaryMIPDataMissingAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryMIPDataMissingAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryMIPPriorityBadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 42)
)
pt3080NotifTSSecondaryMIPPriorityBadAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryMIPPriorityBadAlarm.setStatus(
        "current"
    )

pt3080NotifRFOverloadProtectionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 44)
)
pt3080NotifRFOverloadProtectionAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRFOverloadProtectionAlarm.setStatus(
        "current"
    )

pt3080NotifCommeth0Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 55)
)
pt3080NotifCommeth0Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifCommeth0Alarm.setStatus(
        "current"
    )

pt3080NotifCommeth1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 56)
)
pt3080NotifCommeth1Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifCommeth1Alarm.setStatus(
        "current"
    )

pt3080NotifCommeth2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 57)
)
pt3080NotifCommeth2Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifCommeth2Alarm.setStatus(
        "current"
    )

pt3080NotifCommeth3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 58)
)
pt3080NotifCommeth3Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifCommeth3Alarm.setStatus(
        "current"
    )

pt3080NotifCommeth4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 59)
)
pt3080NotifCommeth4Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifCommeth4Alarm.setStatus(
        "current"
    )

pt3080NotifExternalInput1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 72)
)
pt3080NotifExternalInput1Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput1Alarm.setStatus(
        "current"
    )

pt3080NotifExternalInput2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 73)
)
pt3080NotifExternalInput2Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput2Alarm.setStatus(
        "current"
    )

pt3080NotifExternalInput3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 74)
)
pt3080NotifExternalInput3Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput3Alarm.setStatus(
        "current"
    )

pt3080NotifExternalInput4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 75)
)
pt3080NotifExternalInput4Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput4Alarm.setStatus(
        "current"
    )

pt3080NotifRefenceClockExtern1PPSLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 76)
)
pt3080NotifRefenceClockExtern1PPSLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRefenceClockExtern1PPSLossAlarm.setStatus(
        "current"
    )

pt3080NotifRefenceClockIntern1PPSLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 77)
)
pt3080NotifRefenceClockIntern1PPSLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRefenceClockIntern1PPSLossAlarm.setStatus(
        "current"
    )

pt3080NotifRefenceClockExtern10MHzLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 78)
)
pt3080NotifRefenceClockExtern10MHzLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRefenceClockExtern10MHzLossAlarm.setStatus(
        "current"
    )

pt3080NotifRFAlcRangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 79)
)
pt3080NotifRFAlcRangeAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRFAlcRangeAlarm.setStatus(
        "current"
    )

pt3080NotifSFNResyncAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 80)
)
pt3080NotifSFNResyncAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNResyncAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 81)
)
pt3080NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSPrimaryNetworkDelayExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 82)
)
pt3080NotifSFNTSPrimaryNetworkDelayExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSPrimaryNetworkDelayExceededAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSSecondaryMaxDelayOffsetExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 84)
)
pt3080NotifSFNTSSecondaryMaxDelayOffsetExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSSecondaryMaxDelayOffsetExceededAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSSecondaryNetworkDelayExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 85)
)
pt3080NotifSFNTSSecondaryNetworkDelayExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSSecondaryNetworkDelayExceededAlarm.setStatus(
        "current"
    )

pt3080NotifRFLevelOutOfRangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 87)
)
pt3080NotifRFLevelOutOfRangeAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRFLevelOutOfRangeAlarm.setStatus(
        "current"
    )

pt3080NotifRefenceClockNTPSyncLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 89)
)
pt3080NotifRefenceClockNTPSyncLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRefenceClockNTPSyncLossAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSPrimarySeamlessDelayTooSmallAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 92)
)
pt3080NotifSFNTSPrimarySeamlessDelayTooSmallAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSPrimarySeamlessDelayTooSmallAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSPrimaryMIPConfigErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 93)
)
pt3080NotifSFNTSPrimaryMIPConfigErrorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSPrimaryMIPConfigErrorAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSSecondarySeamlessDelayTooSmallAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 94)
)
pt3080NotifSFNTSSecondarySeamlessDelayTooSmallAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSSecondarySeamlessDelayTooSmallAlarm.setStatus(
        "current"
    )

pt3080NotifSFNTSSecondaryMIPConfigErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 95)
)
pt3080NotifSFNTSSecondaryMIPConfigErrorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNTSSecondaryMIPConfigErrorAlarm.setStatus(
        "current"
    )

pt3080NotifGNSSUnlockedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 98)
)
pt3080NotifGNSSUnlockedAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifGNSSUnlockedAlarm.setStatus(
        "current"
    )

pt3080NotifGNSSAntennaFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 107)
)
pt3080NotifGNSSAntennaFaultAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifGNSSAntennaFaultAlarm.setStatus(
        "current"
    )

pt3080NotifGNSSHoldOverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 108)
)
pt3080NotifGNSSHoldOverAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifGNSSHoldOverAlarm.setStatus(
        "current"
    )

pt3080NotifRefenceClockExternal10MHzHoldOverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 109)
)
pt3080NotifRefenceClockExternal10MHzHoldOverAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRefenceClockExternal10MHzHoldOverAlarm.setStatus(
        "current"
    )

pt3080NotifRefenceClockExternal1PPSHoldOverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 110)
)
pt3080NotifRefenceClockExternal1PPSHoldOverAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifRefenceClockExternal1PPSHoldOverAlarm.setStatus(
        "current"
    )

pt3080NotifASIASI1ErrorRateEceeededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 113)
)
pt3080NotifASIASI1ErrorRateEceeededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifASIASI1ErrorRateEceeededAlarm.setStatus(
        "current"
    )

pt3080NotifASIASI2ErrorRateEceeededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 114)
)
pt3080NotifASIASI2ErrorRateEceeededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifASIASI2ErrorRateEceeededAlarm.setStatus(
        "current"
    )

pt3080NotifTSoIPRx1PackageErrorRationExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 115)
)
pt3080NotifTSoIPRx1PackageErrorRationExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSoIPRx1PackageErrorRationExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSoIPRx2PackageErrorRationExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 117)
)
pt3080NotifTSoIPRx2PackageErrorRationExceededAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSoIPRx2PackageErrorRationExceededAlarm.setStatus(
        "current"
    )

pt3080NotifTSoIPRx1SyncLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 119)
)
pt3080NotifTSoIPRx1SyncLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSoIPRx1SyncLossAlarm.setStatus(
        "current"
    )

pt3080NotifTSoIPRx2SyncLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 121)
)
pt3080NotifTSoIPRx2SyncLossAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSoIPRx2SyncLossAlarm.setStatus(
        "current"
    )

pt3080NotifInternalBackplaneAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 129)
)
pt3080NotifInternalBackplaneAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalBackplaneAlarm.setStatus(
        "current"
    )

pt3080NotifInternalReferenceClockAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 132)
)
pt3080NotifInternalReferenceClockAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalReferenceClockAlarm.setStatus(
        "current"
    )

pt3080NotifInternalUpConverterAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 134)
)
pt3080NotifInternalUpConverterAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalUpConverterAlarm.setStatus(
        "current"
    )

pt3080NotifInternalDownConverterAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 135)
)
pt3080NotifInternalDownConverterAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalDownConverterAlarm.setStatus(
        "current"
    )

pt3080NotifInternalMainboardAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 136)
)
pt3080NotifInternalMainboardAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalMainboardAlarm.setStatus(
        "current"
    )

pt3080NotifInternalBatteryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 137)
)
pt3080NotifInternalBatteryAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalBatteryAlarm.setStatus(
        "current"
    )

pt3080NotifInternalFirmware1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 139)
)
pt3080NotifInternalFirmware1Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalFirmware1Alarm.setStatus(
        "current"
    )

pt3080NotifInternalGNSSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 142)
)
pt3080NotifInternalGNSSAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalGNSSAlarm.setStatus(
        "current"
    )

pt3080NotifInternalSatelliteAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 143)
)
pt3080NotifInternalSatelliteAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalSatelliteAlarm.setStatus(
        "current"
    )

pt3080NotifInternalEthAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 146)
)
pt3080NotifInternalEthAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalEthAlarm.setStatus(
        "current"
    )

pt3080NotifHWMonitorFPGAAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 156)
)
pt3080NotifHWMonitorFPGAAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifHWMonitorFPGAAlarm.setStatus(
        "current"
    )

pt3080NotifHWMonitorMainBoardCPUTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 157)
)
pt3080NotifHWMonitorMainBoardCPUTemperatureAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifHWMonitorMainBoardCPUTemperatureAlarm.setStatus(
        "current"
    )

pt3080NotifHWMonitorMainBoardTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 158)
)
pt3080NotifHWMonitorMainBoardTemperatureAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifHWMonitorMainBoardTemperatureAlarm.setStatus(
        "current"
    )

pt3080NotifHWMonitorLeftFanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 159)
)
pt3080NotifHWMonitorLeftFanAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifHWMonitorLeftFanAlarm.setStatus(
        "current"
    )

pt3080NotifHWMonitorRightFan2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 160)
)
pt3080NotifHWMonitorRightFan2Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifHWMonitorRightFan2Alarm.setStatus(
        "current"
    )

pt3080NotifHWMonitorBackplaneTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 162)
)
pt3080NotifHWMonitorBackplaneTemperatureAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifHWMonitorBackplaneTemperatureAlarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryInputTSHoldOverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 180)
)
pt3080NotifTSPrimaryInputTSHoldOverAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryInputTSHoldOverAlarm.setStatus(
        "current"
    )

pt3080NotifInternalPLLUnlockedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 182)
)
pt3080NotifInternalPLLUnlockedAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifInternalPLLUnlockedAlarm.setStatus(
        "current"
    )

pt3080NotifExternalInput5Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 183)
)
pt3080NotifExternalInput5Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput5Alarm.setStatus(
        "current"
    )

pt3080NotifSFNUntimedModeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 184)
)
pt3080NotifSFNUntimedModeAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNUntimedModeAlarm.setStatus(
        "current"
    )

pt3080NotifSFNFreeRunningModeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 185)
)
pt3080NotifSFNFreeRunningModeAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifSFNFreeRunningModeAlarm.setStatus(
        "current"
    )

pt3080NotifExternalInput6Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 186)
)
pt3080NotifExternalInput6Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput6Alarm.setStatus(
        "current"
    )

pt3080NotifExternalInput7Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 187)
)
pt3080NotifExternalInput7Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput7Alarm.setStatus(
        "current"
    )

pt3080NotifExternalInput8Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 188)
)
pt3080NotifExternalInput8Alarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifExternalInput8Alarm.setStatus(
        "current"
    )

pt3080NotifTSPrimaryDelayMarginAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 190)
)
pt3080NotifTSPrimaryDelayMarginAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSPrimaryDelayMarginAlarm.setStatus(
        "current"
    )

pt3080NotifTSSecondaryDelayMarginAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 64, 0, 191)
)
pt3080NotifTSSecondaryDelayMarginAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifMessage"),
        ("PT3080-MIB", "pt3080NotifState"),
        ("PT3080-MIB", "pt3080NotifLocalTime"))
)
if mibBuilder.loadTexts:
    pt3080NotifTSSecondaryDelayMarginAlarm.setStatus(
        "current"
    )


# Notifications groups

pt3080NotifGroupModulatorAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 3)
)
pt3080NotifGroupModulatorAlarm.setObjects(
    ("PT3080-MIB", "pt3080NotifModulatorAlarm")
)
if mibBuilder.loadTexts:
    pt3080NotifGroupModulatorAlarm.setStatus(
        "current"
    )

pt3080NotifGroupTSPrimaryAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 5)
)
pt3080NotifGroupTSPrimaryAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifTSPrimaryAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimarySyncLossAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimarySyncErrorAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryPCRErrorAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryPATLossAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryTSIDWrongAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryNWIDWrongAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryStuffingRateExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryBufferPoolExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimarySTSJitterExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryMIPDataMissingAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryMIPPriorityBadAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryInputTSHoldOverAlarm"),
        ("PT3080-MIB", "pt3080NotifTSPrimaryDelayMarginAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupTSPrimaryAlarm.setStatus(
        "current"
    )

pt3080NotifGroupTSSecondaryAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 6)
)
pt3080NotifGroupTSSecondaryAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifTSSecondaryAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondarySyncLossAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondarySyncErrorAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryPCRErrorAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryPATLossAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryTSIDWrongAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryNWIDWrongAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryStuffingRateExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryBufferPoolExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondarySTSJitterExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryMIPDataMissingAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryMIPPriorityBadAlarm"),
        ("PT3080-MIB", "pt3080NotifTSSecondaryDelayMarginAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupTSSecondaryAlarm.setStatus(
        "current"
    )

pt3080NotifGroupSFNAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 7)
)
pt3080NotifGroupSFNAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifSFNAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNResyncAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSPrimaryNetworkDelayExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSSecondaryMaxDelayOffsetExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSSecondaryNetworkDelayExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSPrimarySeamlessDelayTooSmallAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSPrimaryMIPConfigErrorAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSSecondarySeamlessDelayTooSmallAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNTSSecondaryMIPConfigErrorAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNUntimedModeAlarm"),
        ("PT3080-MIB", "pt3080NotifSFNFreeRunningModeAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupSFNAlarm.setStatus(
        "current"
    )

pt3080NotifGroupRefenceClockAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 8)
)
pt3080NotifGroupRefenceClockAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifRefenceClockAlarm"),
        ("PT3080-MIB", "pt3080NotifRefenceClockExtern1PPSLossAlarm"),
        ("PT3080-MIB", "pt3080NotifRefenceClockIntern1PPSLossAlarm"),
        ("PT3080-MIB", "pt3080NotifRefenceClockExtern10MHzLossAlarm"),
        ("PT3080-MIB", "pt3080NotifRefenceClockNTPSyncLossAlarm"),
        ("PT3080-MIB", "pt3080NotifRefenceClockExternal10MHzHoldOverAlarm"),
        ("PT3080-MIB", "pt3080NotifRefenceClockExternal1PPSHoldOverAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupRefenceClockAlarm.setStatus(
        "current"
    )

pt3080NotifGroupRFAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 9)
)
pt3080NotifGroupRFAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifRFAlarm"),
        ("PT3080-MIB", "pt3080NotifRFOverloadProtectionAlarm"),
        ("PT3080-MIB", "pt3080NotifRFAlcRangeAlarm"),
        ("PT3080-MIB", "pt3080NotifRFLevelOutOfRangeAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupRFAlarm.setStatus(
        "current"
    )

pt3080NotifGroupGNSSAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 10)
)
pt3080NotifGroupGNSSAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifGNSSAlarm"),
        ("PT3080-MIB", "pt3080NotifGNSSUnlockedAlarm"),
        ("PT3080-MIB", "pt3080NotifGNSSAntennaFaultAlarm"),
        ("PT3080-MIB", "pt3080NotifGNSSHoldOverAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupGNSSAlarm.setStatus(
        "current"
    )

pt3080NotifGroupTSoIPAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 12)
)
pt3080NotifGroupTSoIPAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifTSoIPAlarm"),
        ("PT3080-MIB", "pt3080NotifTSoIPRx1PackageErrorRationExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSoIPRx2PackageErrorRationExceededAlarm"),
        ("PT3080-MIB", "pt3080NotifTSoIPRx1SyncLossAlarm"),
        ("PT3080-MIB", "pt3080NotifTSoIPRx2SyncLossAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupTSoIPAlarm.setStatus(
        "current"
    )

pt3080NotifGroupExternalAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 13)
)
pt3080NotifGroupExternalAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifExternalAlarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput1Alarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput2Alarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput3Alarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput4Alarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput5Alarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput6Alarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput7Alarm"),
        ("PT3080-MIB", "pt3080NotifExternalInput8Alarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupExternalAlarm.setStatus(
        "current"
    )

pt3080NotifGroupHWMonitorAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 14)
)
pt3080NotifGroupHWMonitorAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifHWMonitorAlarm"),
        ("PT3080-MIB", "pt3080NotifHWMonitorFPGAAlarm"),
        ("PT3080-MIB", "pt3080NotifHWMonitorMainBoardCPUTemperatureAlarm"),
        ("PT3080-MIB", "pt3080NotifHWMonitorMainBoardTemperatureAlarm"),
        ("PT3080-MIB", "pt3080NotifHWMonitorLeftFanAlarm"),
        ("PT3080-MIB", "pt3080NotifHWMonitorRightFan2Alarm"),
        ("PT3080-MIB", "pt3080NotifHWMonitorBackplaneTemperatureAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupHWMonitorAlarm.setStatus(
        "current"
    )

pt3080NotifGroupCommAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 15)
)
pt3080NotifGroupCommAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifCommAlarm"),
        ("PT3080-MIB", "pt3080NotifCommeth0Alarm"),
        ("PT3080-MIB", "pt3080NotifCommeth1Alarm"),
        ("PT3080-MIB", "pt3080NotifCommeth2Alarm"),
        ("PT3080-MIB", "pt3080NotifCommeth3Alarm"),
        ("PT3080-MIB", "pt3080NotifCommeth4Alarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupCommAlarm.setStatus(
        "current"
    )

pt3080NotifGroupASIAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 16)
)
pt3080NotifGroupASIAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifASIAlarm"),
        ("PT3080-MIB", "pt3080NotifASIASI1ErrorRateEceeededAlarm"),
        ("PT3080-MIB", "pt3080NotifASIASI2ErrorRateEceeededAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupASIAlarm.setStatus(
        "current"
    )

pt3080NotifGroupInternalAlarm = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 4, 18)
)
pt3080NotifGroupInternalAlarm.setObjects(
      *(("PT3080-MIB", "pt3080NotifInternalAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalBackplaneAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalReferenceClockAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalUpConverterAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalDownConverterAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalMainboardAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalBatteryAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalFirmware1Alarm"),
        ("PT3080-MIB", "pt3080NotifInternalGNSSAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalSatelliteAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalEthAlarm"),
        ("PT3080-MIB", "pt3080NotifInternalPLLUnlockedAlarm"))
)
if mibBuilder.loadTexts:
    pt3080NotifGroupInternalAlarm.setStatus(
        "current"
    )


# Agent capabilities

pt3080Agent = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 3)
)
if mibBuilder.loadTexts:
    pt3080Agent.setProductRelease("SWPROTELEVISION_P3_1_02_157 build 1441106393")
if mibBuilder.loadTexts:
    pt3080Agent.setStatus(
        "current"
    )


# Module compliance

pt3080Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 223, 2, 3080, 100, 1, 1)
)
pt3080Compliance.setObjects(
      *(("PT3080-MIB", "pt3080SystemGroup"),
        ("PT3080-MIB", "pt3080InputGroup"),
        ("PT3080-MIB", "pt3080OutputGroup"),
        ("PT3080-MIB", "pt3080MonitorGroup"),
        ("PT3080-MIB", "pt3080TestGroup"),
        ("PT3080-MIB", "pt3080AlarmGroup"),
        ("PT3080-MIB", "pt3080PresetGroup"),
        ("PT3080-MIB", "pt3080EventlogGroup"),
        ("PT3080-MIB", "pt3080CommsGroup"),
        ("PT3080-MIB", "pt3080PrecorrectorGroup"),
        ("PT3080-MIB", "pt3080ModeGroup"),
        ("PT3080-MIB", "pt3080GpsGroup"),
        ("PT3080-MIB", "pt3080ChannelFilterGroup"),
        ("PT3080-MIB", "pt3080TSoIPGroup"),
        ("PT3080-MIB", "pt3080DemodulatorGroup"),
        ("PT3080-MIB", "pt3080ReceptionGroup"),
        ("PT3080-MIB", "pt3080ASIGroup"))
)
if mibBuilder.loadTexts:
    pt3080Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PT3080-MIB",
    **{"pt3080": pt3080,
       "pt3080System": pt3080System,
       "pt3080SystemInstrumentKU": pt3080SystemInstrumentKU,
       "pt3080SystemInstrumentType": pt3080SystemInstrumentType,
       "pt3080SystemInstrumentSWRev": pt3080SystemInstrumentSWRev,
       "pt3080SystemInstrumentBootLoaderRev": pt3080SystemInstrumentBootLoaderRev,
       "pt3080SystemInstrumentKernelRev": pt3080SystemInstrumentKernelRev,
       "pt3080SystemInstrumentOptions": pt3080SystemInstrumentOptions,
       "pt3080SystemInstrumentFW1Rev": pt3080SystemInstrumentFW1Rev,
       "pt3080SystemInstrumentFW1RevBL": pt3080SystemInstrumentFW1RevBL,
       "pt3080SystemInstrumentFW2Rev": pt3080SystemInstrumentFW2Rev,
       "pt3080SystemInstrumentFW2RevBL": pt3080SystemInstrumentFW2RevBL,
       "pt3080SystemInstrumentFW3Rev": pt3080SystemInstrumentFW3Rev,
       "pt3080SystemInstrumentFW4Rev": pt3080SystemInstrumentFW4Rev,
       "pt3080SystemInstrumentPCBRev": pt3080SystemInstrumentPCBRev,
       "pt3080SystemInstrumentCalibrationRev": pt3080SystemInstrumentCalibrationRev,
       "pt3080SystemInstrumentCalibrationDate": pt3080SystemInstrumentCalibrationDate,
       "pt3080SystemReboot": pt3080SystemReboot,
       "pt3080SystemRebootDefaultConfig": pt3080SystemRebootDefaultConfig,
       "pt3080SystemDateTimeSync": pt3080SystemDateTimeSync,
       "pt3080SystemTimezone": pt3080SystemTimezone,
       "pt3080SystemDateTime": pt3080SystemDateTime,
       "pt3080SystemCurrentImage": pt3080SystemCurrentImage,
       "pt3080SystemImage0Version": pt3080SystemImage0Version,
       "pt3080SystemImage0InstalledDate": pt3080SystemImage0InstalledDate,
       "pt3080SystemImage1version": pt3080SystemImage1version,
       "pt3080SystemImage1InstalledDate": pt3080SystemImage1InstalledDate,
       "pt3080SystemServiceLED": pt3080SystemServiceLED,
       "pt3080SystemType": pt3080SystemType,
       "pt3080SystemDateTimeSyncActual": pt3080SystemDateTimeSyncActual,
       "pt3080SystemModulationStandard": pt3080SystemModulationStandard,
       "pt3080SystemLanguage": pt3080SystemLanguage,
       "pt3080SystemOperationOnTime": pt3080SystemOperationOnTime,
       "pt3080SystemOperationOnAirTime": pt3080SystemOperationOnAirTime,
       "pt3080SystemOperationNumberOfBoots": pt3080SystemOperationNumberOfBoots,
       "pt3080SystemBackplaneid": pt3080SystemBackplaneid,
       "pt3080SystemBackplaneIdRaw": pt3080SystemBackplaneIdRaw,
       "pt3080SystemBackplaneIdPcb": pt3080SystemBackplaneIdPcb,
       "pt3080SystemBackplaneIdCableOptions": pt3080SystemBackplaneIdCableOptions,
       "pt3080SystemBackplaneIdMAnuf": pt3080SystemBackplaneIdMAnuf,
       "pt3080SystemBackplaneCalibrationDate": pt3080SystemBackplaneCalibrationDate,
       "pt3080SystemBackplaneCalibrationSw": pt3080SystemBackplaneCalibrationSw,
       "pt3080SystemBackplaneIdPartlist": pt3080SystemBackplaneIdPartlist,
       "pt3080SystemScheduledActionTable": pt3080SystemScheduledActionTable,
       "pt3080SystemScheduledActionEntry": pt3080SystemScheduledActionEntry,
       "pt3080SystemScheduledActionID": pt3080SystemScheduledActionID,
       "pt3080SystemScheduledActionRecurrence": pt3080SystemScheduledActionRecurrence,
       "pt3080SystemScheduledActionHour": pt3080SystemScheduledActionHour,
       "pt3080SystemScheduledActionMinute": pt3080SystemScheduledActionMinute,
       "pt3080SystemScheduledActionWeekday": pt3080SystemScheduledActionWeekday,
       "pt3080SystemScheduledActionMonthDay": pt3080SystemScheduledActionMonthDay,
       "pt3080SystemScheduledActionDate": pt3080SystemScheduledActionDate,
       "pt3080SystemScheduledActionRandomDelay": pt3080SystemScheduledActionRandomDelay,
       "pt3080SystemScheduledActionAction": pt3080SystemScheduledActionAction,
       "pt3080SystemScheduledActionRepeaterMode": pt3080SystemScheduledActionRepeaterMode,
       "pt3080SystemScheduledActionPresetNo": pt3080SystemScheduledActionPresetNo,
       "pt3080SystemScheduledActionRebootImage": pt3080SystemScheduledActionRebootImage,
       "pt3080SystemScheduledActionRebootSystemType": pt3080SystemScheduledActionRebootSystemType,
       "pt3080SystemScheduledActionMute": pt3080SystemScheduledActionMute,
       "pt3080SystemScheduledActionSWUpgradeProtocol": pt3080SystemScheduledActionSWUpgradeProtocol,
       "pt3080SystemScheduledActionSWUpgradeUsername": pt3080SystemScheduledActionSWUpgradeUsername,
       "pt3080SystemScheduledActionSWUpgradePassword": pt3080SystemScheduledActionSWUpgradePassword,
       "pt3080SystemScheduledActionSWUpgradeImageServer": pt3080SystemScheduledActionSWUpgradeImageServer,
       "pt3080SystemScheduledActionSWUpgradeImagePath": pt3080SystemScheduledActionSWUpgradeImagePath,
       "pt3080Mode": pt3080Mode,
       "pt3080ModeNetwork": pt3080ModeNetwork,
       "pt3080ModeHierarchy": pt3080ModeHierarchy,
       "pt3080Modeifft": pt3080Modeifft,
       "pt3080ModeCodeRateHighPrio": pt3080ModeCodeRateHighPrio,
       "pt3080ModeCodeRateLowPrio": pt3080ModeCodeRateLowPrio,
       "pt3080ModeConstellation": pt3080ModeConstellation,
       "pt3080ModeGuardInterval": pt3080ModeGuardInterval,
       "pt3080ModeCellID": pt3080ModeCellID,
       "pt3080ModeEnableCellID": pt3080ModeEnableCellID,
       "pt3080ModeDeepInterleaver": pt3080ModeDeepInterleaver,
       "pt3080ModeEnableDVBH": pt3080ModeEnableDVBH,
       "pt3080ModeMpeFecLowPrio": pt3080ModeMpeFecLowPrio,
       "pt3080ModeMpeFecHighPrio": pt3080ModeMpeFecHighPrio,
       "pt3080ModeTimeSlicingLowPrio": pt3080ModeTimeSlicingLowPrio,
       "pt3080ModeTimeSlicingHighPrio": pt3080ModeTimeSlicingHighPrio,
       "pt3080ModeSfnDelayOffset": pt3080ModeSfnDelayOffset,
       "pt3080ModeTxIdent": pt3080ModeTxIdent,
       "pt3080ModeMipControl": pt3080ModeMipControl,
       "pt3080ModeMfnKeepNullPackets": pt3080ModeMfnKeepNullPackets,
       "pt3080ModeNetworkDelayHP": pt3080ModeNetworkDelayHP,
       "pt3080ModeNetworkDelayMinHP": pt3080ModeNetworkDelayMinHP,
       "pt3080ModeNetworkDelayMaxHP": pt3080ModeNetworkDelayMaxHP,
       "pt3080ModeMaxNetworkDelayHP": pt3080ModeMaxNetworkDelayHP,
       "pt3080ModeNetworkDelayMarginHP": pt3080ModeNetworkDelayMarginHP,
       "pt3080ModeNetworkDelayLP": pt3080ModeNetworkDelayLP,
       "pt3080ModeNetworkDelayMinLP": pt3080ModeNetworkDelayMinLP,
       "pt3080ModeNetworkDelayMaxLP": pt3080ModeNetworkDelayMaxLP,
       "pt3080ModeMaxNetworkDelayLP": pt3080ModeMaxNetworkDelayLP,
       "pt3080ModeNetworkDelayMarginLP": pt3080ModeNetworkDelayMarginLP,
       "pt3080ModeNetworkDelayReset": pt3080ModeNetworkDelayReset,
       "pt3080ModeDefaultMIPOutputPower": pt3080ModeDefaultMIPOutputPower,
       "pt3080ModeDefaultMIPOutputTimeOffset": pt3080ModeDefaultMIPOutputTimeOffset,
       "pt3080ModeDefaultMIPOutputCellID": pt3080ModeDefaultMIPOutputCellID,
       "pt3080ModeDefaultMIPOutputFreqOffset": pt3080ModeDefaultMIPOutputFreqOffset,
       "pt3080ModeMIPMaxSFNDelay": pt3080ModeMIPMaxSFNDelay,
       "pt3080ModeMipControlOutputPower": pt3080ModeMipControlOutputPower,
       "pt3080ModeMipControlOutputTimeOffset": pt3080ModeMipControlOutputTimeOffset,
       "pt3080ModeMipControlOutputCellId": pt3080ModeMipControlOutputCellId,
       "pt3080ModeMipControlOutputFreqOffset": pt3080ModeMipControlOutputFreqOffset,
       "pt3080ModeListenBroadcast": pt3080ModeListenBroadcast,
       "pt3080Input": pt3080Input,
       "pt3080InputRefDirection": pt3080InputRefDirection,
       "pt3080InputRefSource": pt3080InputRefSource,
       "pt3080InputRef10MhzImpedance": pt3080InputRef10MhzImpedance,
       "pt3080InputRef1PPSImpedance": pt3080InputRef1PPSImpedance,
       "pt3080InputRef1PPSTrigSlope": pt3080InputRef1PPSTrigSlope,
       "pt3080InputRef1PPSTrigLevel": pt3080InputRef1PPSTrigLevel,
       "pt3080InputRef10MhzHoldoverDelay": pt3080InputRef10MhzHoldoverDelay,
       "pt3080InputRef10MhzHoldoverForever": pt3080InputRef10MhzHoldoverForever,
       "pt3080InputRef1PPSHoldoverDelay": pt3080InputRef1PPSHoldoverDelay,
       "pt3080InputRef1PPSHoldoverForever": pt3080InputRef1PPSHoldoverForever,
       "pt3080InputRefStatus": pt3080InputRefStatus,
       "pt3080InputASITSPrimarySource": pt3080InputASITSPrimarySource,
       "pt3080InputASITSSecondarySource": pt3080InputASITSSecondarySource,
       "pt3080InputASIAutoRoutingPolicy": pt3080InputASIAutoRoutingPolicy,
       "pt3080InputASIAutoRoutingDelayHp2Lp": pt3080InputASIAutoRoutingDelayHp2Lp,
       "pt3080InputASIAutoRoutingDelayLp2Hp": pt3080InputASIAutoRoutingDelayLp2Hp,
       "pt3080InputASIHoldoverTimeout": pt3080InputASIHoldoverTimeout,
       "pt3080InputTSPrimaryMaxPATDelay": pt3080InputTSPrimaryMaxPATDelay,
       "pt3080InputTSPrimaryMaxPATDelayEnable": pt3080InputTSPrimaryMaxPATDelayEnable,
       "pt3080InputTSPrimaryExpectedTSID": pt3080InputTSPrimaryExpectedTSID,
       "pt3080InputTSPrimaryExpectedTSIDEnable": pt3080InputTSPrimaryExpectedTSIDEnable,
       "pt3080InputTSPrimaryExpectedNWID": pt3080InputTSPrimaryExpectedNWID,
       "pt3080InputTSPrimaryExpectedNWIDEnable": pt3080InputTSPrimaryExpectedNWIDEnable,
       "pt3080InputTSPrimaryMaxStuffingrate": pt3080InputTSPrimaryMaxStuffingrate,
       "pt3080InputTSPrimaryMaxStuffingrateEnable": pt3080InputTSPrimaryMaxStuffingrateEnable,
       "pt3080InputTSPrimaryMaxStsJitter": pt3080InputTSPrimaryMaxStsJitter,
       "pt3080InputTSSecondaryMaxPATDelay": pt3080InputTSSecondaryMaxPATDelay,
       "pt3080InputTSSecondaryMaxPATDelayEnable": pt3080InputTSSecondaryMaxPATDelayEnable,
       "pt3080InputTSSecondaryExpectedTSID": pt3080InputTSSecondaryExpectedTSID,
       "pt3080InputTSSecondaryExpectedTSIDEnable": pt3080InputTSSecondaryExpectedTSIDEnable,
       "pt3080InputTSSecondaryExpectedNWID": pt3080InputTSSecondaryExpectedNWID,
       "pt3080InputTSSecondaryExpectedNWIDEnable": pt3080InputTSSecondaryExpectedNWIDEnable,
       "pt3080InputTSSecondaryMaxStuffingrate": pt3080InputTSSecondaryMaxStuffingrate,
       "pt3080InputTSSecondaryMaxStuffingrateEnable": pt3080InputTSSecondaryMaxStuffingrateEnable,
       "pt3080InputTSSecondaryMaxStsJitter": pt3080InputTSSecondaryMaxStsJitter,
       "pt3080InputTSPrimaryStatus": pt3080InputTSPrimaryStatus,
       "pt3080InputTSSecondaryStatus": pt3080InputTSSecondaryStatus,
       "pt3080InputTSHp": pt3080InputTSHp,
       "pt3080InputTSLp": pt3080InputTSLp,
       "pt3080InputEffectiveAutoroutingPolicy": pt3080InputEffectiveAutoroutingPolicy,
       "pt3080InputTSHpBitrate": pt3080InputTSHpBitrate,
       "pt3080InputTSHpPacketsBuffered": pt3080InputTSHpPacketsBuffered,
       "pt3080InputTSHpPacketSize": pt3080InputTSHpPacketSize,
       "pt3080InputTSHpStuffingrate": pt3080InputTSHpStuffingrate,
       "pt3080InputTSHpTSID": pt3080InputTSHpTSID,
       "pt3080InputTSHpNWID": pt3080InputTSHpNWID,
       "pt3080InputTSLpBitrate": pt3080InputTSLpBitrate,
       "pt3080InputTSLpPacketsBuffered": pt3080InputTSLpPacketsBuffered,
       "pt3080InputTSLpPacketSize": pt3080InputTSLpPacketSize,
       "pt3080InputTSLpStuffingrate": pt3080InputTSLpStuffingrate,
       "pt3080InputTSLpTSID": pt3080InputTSLpTSID,
       "pt3080InputTSLpNWID": pt3080InputTSLpNWID,
       "pt3080InputTSPrimaryStsJitter": pt3080InputTSPrimaryStsJitter,
       "pt3080InputTSPrimaryStsJitterMax": pt3080InputTSPrimaryStsJitterMax,
       "pt3080InputTSPrimaryStsJitterMin": pt3080InputTSPrimaryStsJitterMin,
       "pt3080InputTSPrimaryStsJitterReset": pt3080InputTSPrimaryStsJitterReset,
       "pt3080InputTSSecondaryStsJitter": pt3080InputTSSecondaryStsJitter,
       "pt3080InputTSSecondaryStsJitterMax": pt3080InputTSSecondaryStsJitterMax,
       "pt3080InputTSSecondaryStsJitterMin": pt3080InputTSSecondaryStsJitterMin,
       "pt3080InputTSSecondaryStsJitterReset": pt3080InputTSSecondaryStsJitterReset,
       "pt3080InputTSPrimaryMinDelaymargin": pt3080InputTSPrimaryMinDelaymargin,
       "pt3080InputTSPrimaryMinDelaymarginEnable": pt3080InputTSPrimaryMinDelaymarginEnable,
       "pt3080InputTSSecondaryMinDelaymargin": pt3080InputTSSecondaryMinDelaymargin,
       "pt3080InputTSSecondaryMinDelaymarginEnable": pt3080InputTSSecondaryMinDelaymarginEnable,
       "pt3080InputTSPrimaryMaxMissingmip": pt3080InputTSPrimaryMaxMissingmip,
       "pt3080InputTSPrimaryMaxMissingmipEnable": pt3080InputTSPrimaryMaxMissingmipEnable,
       "pt3080InputTSSecondaryMaxMissingmip": pt3080InputTSSecondaryMaxMissingmip,
       "pt3080InputTSSecondaryMaxMissingmipEnable": pt3080InputTSSecondaryMaxMissingmipEnable,
       "pt3080InputRefDevType": pt3080InputRefDevType,
       "pt3080InputRefCalDate": pt3080InputRefCalDate,
       "pt3080InputRefCalVer": pt3080InputRefCalVer,
       "pt3080Output": pt3080Output,
       "pt3080OutputMode": pt3080OutputMode,
       "pt3080OutputRfFrequency": pt3080OutputRfFrequency,
       "pt3080OutputRfLevel": pt3080OutputRfLevel,
       "pt3080OutputBandwidth": pt3080OutputBandwidth,
       "pt3080OutputChannel": pt3080OutputChannel,
       "pt3080OutputSynchronized": pt3080OutputSynchronized,
       "pt3080OutputMute": pt3080OutputMute,
       "pt3080OutputPolarity": pt3080OutputPolarity,
       "pt3080OutputPowerLevel": pt3080OutputPowerLevel,
       "pt3080OutputRfFrequencyOffset": pt3080OutputRfFrequencyOffset,
       "pt3080OutputIfEnable": pt3080OutputIfEnable,
       "pt3080OutputIfFrequency": pt3080OutputIfFrequency,
       "pt3080OutputIfPolarity": pt3080OutputIfPolarity,
       "pt3080OutputIfLevel": pt3080OutputIfLevel,
       "pt3080OutputEffectiveLevel": pt3080OutputEffectiveLevel,
       "pt3080OutputActualLevel": pt3080OutputActualLevel,
       "pt3080OutputRfDetectedActualLevel": pt3080OutputRfDetectedActualLevel,
       "pt3080OutputRfDetectedLowerLevelLimit": pt3080OutputRfDetectedLowerLevelLimit,
       "pt3080OutputRfDetectedLowerLevelcontrol": pt3080OutputRfDetectedLowerLevelcontrol,
       "pt3080OutputRfDetectedHigherLevelLimit": pt3080OutputRfDetectedHigherLevelLimit,
       "pt3080OutputRfDetectedHigherLevelcontrol": pt3080OutputRfDetectedHigherLevelcontrol,
       "pt3080OutputRfAlcControl": pt3080OutputRfAlcControl,
       "pt3080OutputRfAlcSense": pt3080OutputRfAlcSense,
       "pt3080OutputRfAlcSetpointPort1": pt3080OutputRfAlcSetpointPort1,
       "pt3080OutputRfAlcSetpointPort2": pt3080OutputRfAlcSetpointPort2,
       "pt3080OutputRfAlcStatus": pt3080OutputRfAlcStatus,
       "pt3080OutputRfAlcStatusInformation": pt3080OutputRfAlcStatusInformation,
       "pt3080OutputRfCableMode": pt3080OutputRfCableMode,
       "pt3080OutputRfCableConstantLevelOffset": pt3080OutputRfCableConstantLevelOffset,
       "pt3080OutputRfCableFrequencyLevelOffset0": pt3080OutputRfCableFrequencyLevelOffset0,
       "pt3080OutputRfCableFrequencyLevelOffset1": pt3080OutputRfCableFrequencyLevelOffset1,
       "pt3080OutputRfCableFrequencyLevelOffset2": pt3080OutputRfCableFrequencyLevelOffset2,
       "pt3080OutputRfCableFrequencyLevelOffset3": pt3080OutputRfCableFrequencyLevelOffset3,
       "pt3080OutputRfCableFrequencyLevelOffset4": pt3080OutputRfCableFrequencyLevelOffset4,
       "pt3080OutputRfCableFrequencyLevelOffset5": pt3080OutputRfCableFrequencyLevelOffset5,
       "pt3080Gps": pt3080Gps,
       "pt3080Gps1PPSStatus": pt3080Gps1PPSStatus,
       "pt3080GpsVisibleSatellites": pt3080GpsVisibleSatellites,
       "pt3080GpsTrackedSatellites": pt3080GpsTrackedSatellites,
       "pt3080GpsBias": pt3080GpsBias,
       "pt3080GpsLongtitude": pt3080GpsLongtitude,
       "pt3080GpsLatitude": pt3080GpsLatitude,
       "pt3080GpsAltitude": pt3080GpsAltitude,
       "pt3080GpsVersion": pt3080GpsVersion,
       "pt3080GpsHoldoverTime": pt3080GpsHoldoverTime,
       "pt3080GpsHoldoverForever": pt3080GpsHoldoverForever,
       "pt3080GpsCableDelay": pt3080GpsCableDelay,
       "pt3080GpsState": pt3080GpsState,
       "pt3080GpsVisibleSatellitesSnr": pt3080GpsVisibleSatellitesSnr,
       "pt3080GpsbiasVoltage": pt3080GpsbiasVoltage,
       "pt3080GpsSatelliteSystemGPS": pt3080GpsSatelliteSystemGPS,
       "pt3080GpsSatelliteSystemGLONASS": pt3080GpsSatelliteSystemGLONASS,
       "pt3080GpsSatelliteSystemGALILEO": pt3080GpsSatelliteSystemGALILEO,
       "pt3080GpsSatelliteSystemCOMPASS": pt3080GpsSatelliteSystemCOMPASS,
       "pt3080TSoIP": pt3080TSoIP,
       "pt3080TSoIPRx1SyncTimeout": pt3080TSoIPRx1SyncTimeout,
       "pt3080TSoIPRx1MinumimLatency": pt3080TSoIPRx1MinumimLatency,
       "pt3080TSoIPRx1LanSelect": pt3080TSoIPRx1LanSelect,
       "pt3080TSoIPRx1Multicast": pt3080TSoIPRx1Multicast,
       "pt3080TSoIPRx1Protocol": pt3080TSoIPRx1Protocol,
       "pt3080TSoIPRx1Portnumber": pt3080TSoIPRx1Portnumber,
       "pt3080TSoIPRx1ReceiverEnable": pt3080TSoIPRx1ReceiverEnable,
       "pt3080TSoIPRx1PacketErrorRatioLimit": pt3080TSoIPRx1PacketErrorRatioLimit,
       "pt3080TSoIPRx1Status": pt3080TSoIPRx1Status,
       "pt3080TSoIPRx1CurrentIPAddress": pt3080TSoIPRx1CurrentIPAddress,
       "pt3080TSoIPRx1SequenceErrors": pt3080TSoIPRx1SequenceErrors,
       "pt3080TSoIPRx1PacketErrorRatio": pt3080TSoIPRx1PacketErrorRatio,
       "pt3080TSoIPRx1LostIPFrames": pt3080TSoIPRx1LostIPFrames,
       "pt3080TSoIPRx1CorrectedIPFrames": pt3080TSoIPRx1CorrectedIPFrames,
       "pt3080TSoIPRx1FecColumn": pt3080TSoIPRx1FecColumn,
       "pt3080TSoIPRx1FecRow": pt3080TSoIPRx1FecRow,
       "pt3080TSoIPRx1PacketsPerFrame": pt3080TSoIPRx1PacketsPerFrame,
       "pt3080TSoIPRx1IpBitrate": pt3080TSoIPRx1IpBitrate,
       "pt3080TSoIPRx1QueueSize": pt3080TSoIPRx1QueueSize,
       "pt3080TSoIPRx1CurrentLatency": pt3080TSoIPRx1CurrentLatency,
       "pt3080TSoIPRx1TSPacketSize": pt3080TSoIPRx1TSPacketSize,
       "pt3080TSoIPRx1OverrunIPFrames": pt3080TSoIPRx1OverrunIPFrames,
       "pt3080TSoIPRx2SyncTimeout": pt3080TSoIPRx2SyncTimeout,
       "pt3080TSoIPRx2MinumimLatency": pt3080TSoIPRx2MinumimLatency,
       "pt3080TSoIPRx2LanSelect": pt3080TSoIPRx2LanSelect,
       "pt3080TSoIPRx2Multicast": pt3080TSoIPRx2Multicast,
       "pt3080TSoIPRx2Protocol": pt3080TSoIPRx2Protocol,
       "pt3080TSoIPRx2Portnumber": pt3080TSoIPRx2Portnumber,
       "pt3080TSoIPRx2ReceiverEnable": pt3080TSoIPRx2ReceiverEnable,
       "pt3080TSoIPRx2PacketErrorRatioLimit": pt3080TSoIPRx2PacketErrorRatioLimit,
       "pt3080TSoIPRx2Status": pt3080TSoIPRx2Status,
       "pt3080TSoIPRx2CurrentIPAddress": pt3080TSoIPRx2CurrentIPAddress,
       "pt3080TSoIPRx2SequenceErrors": pt3080TSoIPRx2SequenceErrors,
       "pt3080TSoIPRx2PacketErrorRatio": pt3080TSoIPRx2PacketErrorRatio,
       "pt3080TSoIPRx2LostIPFrames": pt3080TSoIPRx2LostIPFrames,
       "pt3080TSoIPRx2CorrectedIPFrames": pt3080TSoIPRx2CorrectedIPFrames,
       "pt3080TSoIPRx2FecColumn": pt3080TSoIPRx2FecColumn,
       "pt3080TSoIPRx2FecRow": pt3080TSoIPRx2FecRow,
       "pt3080TSoIPRx2PacketsPerFrame": pt3080TSoIPRx2PacketsPerFrame,
       "pt3080TSoIPRx2IpBitrate": pt3080TSoIPRx2IpBitrate,
       "pt3080TSoIPRx2QueueSize": pt3080TSoIPRx2QueueSize,
       "pt3080TSoIPRx2CurrentLatency": pt3080TSoIPRx2CurrentLatency,
       "pt3080TSoIPRx2TSPacketSize": pt3080TSoIPRx2TSPacketSize,
       "pt3080TSoIPRx2OverrunIPFrames": pt3080TSoIPRx2OverrunIPFrames,
       "pt3080Monitor": pt3080Monitor,
       "pt3080MonitorSource": pt3080MonitorSource,
       "pt3080MonitorTSoIPEnable": pt3080MonitorTSoIPEnable,
       "pt3080MonitorTSoIPSource": pt3080MonitorTSoIPSource,
       "pt3080MonitorTSoIPDestIPAddress": pt3080MonitorTSoIPDestIPAddress,
       "pt3080MonitorTSoIPDestPort": pt3080MonitorTSoIPDestPort,
       "pt3080MonitorTSoIPProtocol": pt3080MonitorTSoIPProtocol,
       "pt3080MonitorTSoIPEnableFec": pt3080MonitorTSoIPEnableFec,
       "pt3080MonitorTSoIPFecColumn": pt3080MonitorTSoIPFecColumn,
       "pt3080MonitorTSoIPFecRow": pt3080MonitorTSoIPFecRow,
       "pt3080MonitorTSoIPFecSkew": pt3080MonitorTSoIPFecSkew,
       "pt3080MonitorTSoIPKeepNullPackets": pt3080MonitorTSoIPKeepNullPackets,
       "pt3080MonitorTSoIPPacketsPerFrame": pt3080MonitorTSoIPPacketsPerFrame,
       "pt3080MonitorTSoIPUDPChecksum": pt3080MonitorTSoIPUDPChecksum,
       "pt3080MonitorTSoIPDSCP": pt3080MonitorTSoIPDSCP,
       "pt3080MonitorTSoIPTTL": pt3080MonitorTSoIPTTL,
       "pt3080MonitorTSoIPGenerateError": pt3080MonitorTSoIPGenerateError,
       "pt3080MonitorTSoIPMulticastLanSelect": pt3080MonitorTSoIPMulticastLanSelect,
       "pt3080MonitorTSoIPIpBitrate": pt3080MonitorTSoIPIpBitrate,
       "pt3080MonitorTSoIPLostIPFrames": pt3080MonitorTSoIPLostIPFrames,
       "pt3080MonitorTSoIPTSSize": pt3080MonitorTSoIPTSSize,
       "pt3080Test": pt3080Test,
       "pt3080TestEnable": pt3080TestEnable,
       "pt3080TestEnableReconnect": pt3080TestEnableReconnect,
       "pt3080TestScarrierLevel": pt3080TestScarrierLevel,
       "pt3080TestscarrierFrequencyOffset": pt3080TestscarrierFrequencyOffset,
       "pt3080Alarm": pt3080Alarm,
       "pt3080GroupAlarmTable": pt3080GroupAlarmTable,
       "pt3080GroupAlarmEntry": pt3080GroupAlarmEntry,
       "pt3080GroupAlarmID": pt3080GroupAlarmID,
       "pt3080GroupAlarmDescription": pt3080GroupAlarmDescription,
       "pt3080GroupAlarmState": pt3080GroupAlarmState,
       "pt3080GroupAlarmActionEventlog": pt3080GroupAlarmActionEventlog,
       "pt3080GroupAlarmActionRelay1": pt3080GroupAlarmActionRelay1,
       "pt3080GroupAlarmActionRelay2": pt3080GroupAlarmActionRelay2,
       "pt3080GroupAlarmActionTrap": pt3080GroupAlarmActionTrap,
       "pt3080GroupAlarmActionEmail": pt3080GroupAlarmActionEmail,
       "pt3080GroupAlarmActionAlarmLED": pt3080GroupAlarmActionAlarmLED,
       "pt3080GroupAlarmActionForceMode": pt3080GroupAlarmActionForceMode,
       "pt3080ASITSPrimaryAlarmTable": pt3080ASITSPrimaryAlarmTable,
       "pt3080ASITSPrimaryAlarmEntry": pt3080ASITSPrimaryAlarmEntry,
       "pt3080ASITSPrimaryAlarmID": pt3080ASITSPrimaryAlarmID,
       "pt3080ASITSPrimaryAlarmDescription": pt3080ASITSPrimaryAlarmDescription,
       "pt3080ASITSPrimaryAlarmState": pt3080ASITSPrimaryAlarmState,
       "pt3080ASITSPrimaryAlarmActionEventlog": pt3080ASITSPrimaryAlarmActionEventlog,
       "pt3080ASITSPrimaryAlarmActionRelay1": pt3080ASITSPrimaryAlarmActionRelay1,
       "pt3080ASITSPrimaryAlarmActionRelay2": pt3080ASITSPrimaryAlarmActionRelay2,
       "pt3080ASITSPrimaryAlarmActionTrap": pt3080ASITSPrimaryAlarmActionTrap,
       "pt3080ASITSPrimaryAlarmActionEmail": pt3080ASITSPrimaryAlarmActionEmail,
       "pt3080ASITSPrimaryAlarmActionAlarmLED": pt3080ASITSPrimaryAlarmActionAlarmLED,
       "pt3080ASITSPrimaryAlarmActionForceMode": pt3080ASITSPrimaryAlarmActionForceMode,
       "pt3080ASITSSecondaryAlarmTable": pt3080ASITSSecondaryAlarmTable,
       "pt3080ASITSSecondaryAlarmEntry": pt3080ASITSSecondaryAlarmEntry,
       "pt3080ASITSSecondaryAlarmID": pt3080ASITSSecondaryAlarmID,
       "pt3080ASITSSecondaryAlarmDescription": pt3080ASITSSecondaryAlarmDescription,
       "pt3080ASITSSecondaryAlarmState": pt3080ASITSSecondaryAlarmState,
       "pt3080ASITSSecondaryAlarmActionEventlog": pt3080ASITSSecondaryAlarmActionEventlog,
       "pt3080ASITSSecondaryAlarmActionRelay1": pt3080ASITSSecondaryAlarmActionRelay1,
       "pt3080ASITSSecondaryAlarmActionRelay2": pt3080ASITSSecondaryAlarmActionRelay2,
       "pt3080ASITSSecondaryAlarmActionTrap": pt3080ASITSSecondaryAlarmActionTrap,
       "pt3080ASITSSecondaryAlarmActionEmail": pt3080ASITSSecondaryAlarmActionEmail,
       "pt3080ASITSSecondaryAlarmActionAlarmLED": pt3080ASITSSecondaryAlarmActionAlarmLED,
       "pt3080ASITSSecondaryAlarmActionForceMode": pt3080ASITSSecondaryAlarmActionForceMode,
       "pt3080SFNAlarmTable": pt3080SFNAlarmTable,
       "pt3080SFNAlarmEntry": pt3080SFNAlarmEntry,
       "pt3080SFNAlarmID": pt3080SFNAlarmID,
       "pt3080SFNAlarmDescription": pt3080SFNAlarmDescription,
       "pt3080SFNAlarmState": pt3080SFNAlarmState,
       "pt3080SFNAlarmActionEventlog": pt3080SFNAlarmActionEventlog,
       "pt3080SFNAlarmActionRelay1": pt3080SFNAlarmActionRelay1,
       "pt3080SFNAlarmActionRelay2": pt3080SFNAlarmActionRelay2,
       "pt3080SFNAlarmActionTrap": pt3080SFNAlarmActionTrap,
       "pt3080SFNAlarmActionEmail": pt3080SFNAlarmActionEmail,
       "pt3080SFNAlarmActionAlarmLED": pt3080SFNAlarmActionAlarmLED,
       "pt3080SFNAlarmActionForceMode": pt3080SFNAlarmActionForceMode,
       "pt3080ReferenceAlarmTable": pt3080ReferenceAlarmTable,
       "pt3080ReferenceAlarmEntry": pt3080ReferenceAlarmEntry,
       "pt3080ReferenceAlarmID": pt3080ReferenceAlarmID,
       "pt3080ReferenceAlarmDescription": pt3080ReferenceAlarmDescription,
       "pt3080ReferenceAlarmState": pt3080ReferenceAlarmState,
       "pt3080ReferenceAlarmActionEventlog": pt3080ReferenceAlarmActionEventlog,
       "pt3080ReferenceAlarmActionRelay1": pt3080ReferenceAlarmActionRelay1,
       "pt3080ReferenceAlarmActionRelay2": pt3080ReferenceAlarmActionRelay2,
       "pt3080ReferenceAlarmActionTrap": pt3080ReferenceAlarmActionTrap,
       "pt3080ReferenceAlarmActionEmail": pt3080ReferenceAlarmActionEmail,
       "pt3080ReferenceAlarmActionAlarmLED": pt3080ReferenceAlarmActionAlarmLED,
       "pt3080ReferenceAlarmActionForceMode": pt3080ReferenceAlarmActionForceMode,
       "pt3080RFAlarmTable": pt3080RFAlarmTable,
       "pt3080RFAlarmEntry": pt3080RFAlarmEntry,
       "pt3080RFAlarmID": pt3080RFAlarmID,
       "pt3080RFAlarmDescription": pt3080RFAlarmDescription,
       "pt3080RFAlarmState": pt3080RFAlarmState,
       "pt3080RFAlarmActionEventlog": pt3080RFAlarmActionEventlog,
       "pt3080RFAlarmActionRelay1": pt3080RFAlarmActionRelay1,
       "pt3080RFAlarmActionRelay2": pt3080RFAlarmActionRelay2,
       "pt3080RFAlarmActionTrap": pt3080RFAlarmActionTrap,
       "pt3080RFAlarmActionEmail": pt3080RFAlarmActionEmail,
       "pt3080RFAlarmActionAlarmLED": pt3080RFAlarmActionAlarmLED,
       "pt3080RFAlarmActionForceMode": pt3080RFAlarmActionForceMode,
       "pt3080GPSAlarmTable": pt3080GPSAlarmTable,
       "pt3080GPSAlarmEntry": pt3080GPSAlarmEntry,
       "pt3080GPSAlarmID": pt3080GPSAlarmID,
       "pt3080GPSAlarmDescription": pt3080GPSAlarmDescription,
       "pt3080GPSAlarmState": pt3080GPSAlarmState,
       "pt3080GPSAlarmActionEventlog": pt3080GPSAlarmActionEventlog,
       "pt3080GPSAlarmActionRelay1": pt3080GPSAlarmActionRelay1,
       "pt3080GPSAlarmActionRelay2": pt3080GPSAlarmActionRelay2,
       "pt3080GPSAlarmActionTrap": pt3080GPSAlarmActionTrap,
       "pt3080GPSAlarmActionEmail": pt3080GPSAlarmActionEmail,
       "pt3080GPSAlarmActionAlarmLED": pt3080GPSAlarmActionAlarmLED,
       "pt3080GPSAlarmActionForceMode": pt3080GPSAlarmActionForceMode,
       "pt3080TSoIPAlarmTable": pt3080TSoIPAlarmTable,
       "pt3080TSoIPAlarmEntry": pt3080TSoIPAlarmEntry,
       "pt3080TSoIPAlarmID": pt3080TSoIPAlarmID,
       "pt3080TSoIPAlarmDescription": pt3080TSoIPAlarmDescription,
       "pt3080TSoIPAlarmState": pt3080TSoIPAlarmState,
       "pt3080TSoIPAlarmActionEventlog": pt3080TSoIPAlarmActionEventlog,
       "pt3080TSoIPAlarmActionRelay1": pt3080TSoIPAlarmActionRelay1,
       "pt3080TSoIPAlarmActionRelay2": pt3080TSoIPAlarmActionRelay2,
       "pt3080TSoIPAlarmActionTrap": pt3080TSoIPAlarmActionTrap,
       "pt3080TSoIPAlarmActionEmail": pt3080TSoIPAlarmActionEmail,
       "pt3080TSoIPAlarmActionAlarmLED": pt3080TSoIPAlarmActionAlarmLED,
       "pt3080TSoIPAlarmActionForceMode": pt3080TSoIPAlarmActionForceMode,
       "pt3080ExternalAlarmTable": pt3080ExternalAlarmTable,
       "pt3080ExternalAlarmEntry": pt3080ExternalAlarmEntry,
       "pt3080ExternalAlarmID": pt3080ExternalAlarmID,
       "pt3080ExternalAlarmDescription": pt3080ExternalAlarmDescription,
       "pt3080ExternalAlarmState": pt3080ExternalAlarmState,
       "pt3080ExternalAlarmActionEventlog": pt3080ExternalAlarmActionEventlog,
       "pt3080ExternalAlarmActionRelay1": pt3080ExternalAlarmActionRelay1,
       "pt3080ExternalAlarmActionRelay2": pt3080ExternalAlarmActionRelay2,
       "pt3080ExternalAlarmActionTrap": pt3080ExternalAlarmActionTrap,
       "pt3080ExternalAlarmActionEmail": pt3080ExternalAlarmActionEmail,
       "pt3080ExternalAlarmActionAlarmLED": pt3080ExternalAlarmActionAlarmLED,
       "pt3080ExternalAlarmActionForceMode": pt3080ExternalAlarmActionForceMode,
       "pt3080HWMonitorAlarmTable": pt3080HWMonitorAlarmTable,
       "pt3080HWMonitorAlarmEntry": pt3080HWMonitorAlarmEntry,
       "pt3080HWMonitorAlarmID": pt3080HWMonitorAlarmID,
       "pt3080HWMonitorAlarmDescription": pt3080HWMonitorAlarmDescription,
       "pt3080HWMonitorAlarmState": pt3080HWMonitorAlarmState,
       "pt3080HWMonitorAlarmActionEventlog": pt3080HWMonitorAlarmActionEventlog,
       "pt3080HWMonitorAlarmActionRelay1": pt3080HWMonitorAlarmActionRelay1,
       "pt3080HWMonitorAlarmActionRelay2": pt3080HWMonitorAlarmActionRelay2,
       "pt3080HWMonitorAlarmActionTrap": pt3080HWMonitorAlarmActionTrap,
       "pt3080HWMonitorAlarmActionEmail": pt3080HWMonitorAlarmActionEmail,
       "pt3080HWMonitorAlarmActionAlarmLED": pt3080HWMonitorAlarmActionAlarmLED,
       "pt3080HWMonitorAlarmActionForceMode": pt3080HWMonitorAlarmActionForceMode,
       "pt3080CommsAlarmTable": pt3080CommsAlarmTable,
       "pt3080CommsAlarmEntry": pt3080CommsAlarmEntry,
       "pt3080CommsAlarmID": pt3080CommsAlarmID,
       "pt3080CommsAlarmDescription": pt3080CommsAlarmDescription,
       "pt3080CommsAlarmState": pt3080CommsAlarmState,
       "pt3080CommsAlarmActionEventlog": pt3080CommsAlarmActionEventlog,
       "pt3080CommsAlarmActionRelay1": pt3080CommsAlarmActionRelay1,
       "pt3080CommsAlarmActionRelay2": pt3080CommsAlarmActionRelay2,
       "pt3080CommsAlarmActionTrap": pt3080CommsAlarmActionTrap,
       "pt3080CommsAlarmActionEmail": pt3080CommsAlarmActionEmail,
       "pt3080CommsAlarmActionAlarmLED": pt3080CommsAlarmActionAlarmLED,
       "pt3080CommsAlarmActionForceMode": pt3080CommsAlarmActionForceMode,
       "pt3080ASIAlarmTable": pt3080ASIAlarmTable,
       "pt3080ASIAlarmEntry": pt3080ASIAlarmEntry,
       "pt3080ASIAlarmID": pt3080ASIAlarmID,
       "pt3080ASIAlarmDescription": pt3080ASIAlarmDescription,
       "pt3080ASIAlarmState": pt3080ASIAlarmState,
       "pt3080ASIAlarmActionEventlog": pt3080ASIAlarmActionEventlog,
       "pt3080ASIAlarmActionRelay1": pt3080ASIAlarmActionRelay1,
       "pt3080ASIAlarmActionRelay2": pt3080ASIAlarmActionRelay2,
       "pt3080ASIAlarmActionTrap": pt3080ASIAlarmActionTrap,
       "pt3080ASIAlarmActionEmail": pt3080ASIAlarmActionEmail,
       "pt3080ASIAlarmActionAlarmLED": pt3080ASIAlarmActionAlarmLED,
       "pt3080ASIAlarmActionForceMode": pt3080ASIAlarmActionForceMode,
       "pt3080DemodulatorAlarmTable": pt3080DemodulatorAlarmTable,
       "pt3080DemodulatorAlarmEntry": pt3080DemodulatorAlarmEntry,
       "pt3080DemodulatorAlarmID": pt3080DemodulatorAlarmID,
       "pt3080DemodulatorAlarmDescription": pt3080DemodulatorAlarmDescription,
       "pt3080DemodulatorAlarmState": pt3080DemodulatorAlarmState,
       "pt3080DemodulatorAlarmActionEventlog": pt3080DemodulatorAlarmActionEventlog,
       "pt3080DemodulatorAlarmActionRelay1": pt3080DemodulatorAlarmActionRelay1,
       "pt3080DemodulatorAlarmActionRelay2": pt3080DemodulatorAlarmActionRelay2,
       "pt3080DemodulatorAlarmActionTrap": pt3080DemodulatorAlarmActionTrap,
       "pt3080DemodulatorAlarmActionEmail": pt3080DemodulatorAlarmActionEmail,
       "pt3080DemodulatorAlarmActionAlarmLED": pt3080DemodulatorAlarmActionAlarmLED,
       "pt3080DemodulatorAlarmActionForceMode": pt3080DemodulatorAlarmActionForceMode,
       "pt3080InternalAlarmTable": pt3080InternalAlarmTable,
       "pt3080InternalAlarmEntry": pt3080InternalAlarmEntry,
       "pt3080InternalAlarmID": pt3080InternalAlarmID,
       "pt3080InternalAlarmDescription": pt3080InternalAlarmDescription,
       "pt3080InternalAlarmState": pt3080InternalAlarmState,
       "pt3080InternalAlarmActionEventlog": pt3080InternalAlarmActionEventlog,
       "pt3080InternalAlarmActionRelay1": pt3080InternalAlarmActionRelay1,
       "pt3080InternalAlarmActionRelay2": pt3080InternalAlarmActionRelay2,
       "pt3080InternalAlarmActionTrap": pt3080InternalAlarmActionTrap,
       "pt3080InternalAlarmActionEmail": pt3080InternalAlarmActionEmail,
       "pt3080InternalAlarmActionAlarmLED": pt3080InternalAlarmActionAlarmLED,
       "pt3080InternalAlarmActionForceMode": pt3080InternalAlarmActionForceMode,
       "pt3080Preset": pt3080Preset,
       "pt3080PresetTable": pt3080PresetTable,
       "pt3080PresetEntry": pt3080PresetEntry,
       "pt3080PresetNo": pt3080PresetNo,
       "pt3080PresetName": pt3080PresetName,
       "pt3080PresetRecall": pt3080PresetRecall,
       "pt3080PresetStore": pt3080PresetStore,
       "pt3080Eventlog": pt3080Eventlog,
       "pt3080EventlogTable": pt3080EventlogTable,
       "pt3080EventlogEntry": pt3080EventlogEntry,
       "pt3080EventlogNo": pt3080EventlogNo,
       "pt3080EventlogID": pt3080EventlogID,
       "pt3080EventlogTimestamp": pt3080EventlogTimestamp,
       "pt3080EventlogText": pt3080EventlogText,
       "pt3080EventlogClear": pt3080EventlogClear,
       "pt3080EventlogEnable": pt3080EventlogEnable,
       "pt3080EventlogMode": pt3080EventlogMode,
       "pt3080Comms": pt3080Comms,
       "pt3080CommsLocalStaticIpAddr": pt3080CommsLocalStaticIpAddr,
       "pt3080CommsLocalStaticNetmask": pt3080CommsLocalStaticNetmask,
       "pt3080CommsLocalDhcpMode": pt3080CommsLocalDhcpMode,
       "pt3080CommsLocalCurrentIpAddr": pt3080CommsLocalCurrentIpAddr,
       "pt3080CommsLocalCurrentNetmask": pt3080CommsLocalCurrentNetmask,
       "pt3080CommsRemoteStaticIpAddr": pt3080CommsRemoteStaticIpAddr,
       "pt3080CommsRemoteStaticNetmask": pt3080CommsRemoteStaticNetmask,
       "pt3080CommsRemoteCurrentIpAddr": pt3080CommsRemoteCurrentIpAddr,
       "pt3080CommsRemoteCurrentNetmask": pt3080CommsRemoteCurrentNetmask,
       "pt3080CommsGbeAdminStaticIpAddr": pt3080CommsGbeAdminStaticIpAddr,
       "pt3080CommsGbeAdminStaticNetmask": pt3080CommsGbeAdminStaticNetmask,
       "pt3080CommsGbeAdminCurrentIpAddr": pt3080CommsGbeAdminCurrentIpAddr,
       "pt3080CommsGbeAdminCurrentNetmask": pt3080CommsGbeAdminCurrentNetmask,
       "pt3080CommsStaticDNS1ServerAddress": pt3080CommsStaticDNS1ServerAddress,
       "pt3080CommsCurrentDNS1ServerAddress": pt3080CommsCurrentDNS1ServerAddress,
       "pt3080CommsStaticDNS2ServerAddress": pt3080CommsStaticDNS2ServerAddress,
       "pt3080CommsCurrentDNS2ServerAddress": pt3080CommsCurrentDNS2ServerAddress,
       "pt3080CommsStaticDNS3ServerAddress": pt3080CommsStaticDNS3ServerAddress,
       "pt3080CommsCurrentDNS3ServerAddress": pt3080CommsCurrentDNS3ServerAddress,
       "pt3080CommsStaticDNSDomain": pt3080CommsStaticDNSDomain,
       "pt3080CommsCurrentDNSDomain": pt3080CommsCurrentDNSDomain,
       "pt3080CommsStaticHostname": pt3080CommsStaticHostname,
       "pt3080CommsCurrentHostname": pt3080CommsCurrentHostname,
       "pt3080CommsStaticGateway": pt3080CommsStaticGateway,
       "pt3080CommsCurrentGateway": pt3080CommsCurrentGateway,
       "pt3080CommsStaticNtpServerAddress": pt3080CommsStaticNtpServerAddress,
       "pt3080CommsCurrentNtpServerAddress": pt3080CommsCurrentNtpServerAddress,
       "pt3080CommsEmailServerAddress": pt3080CommsEmailServerAddress,
       "pt3080CommsAlarmEmailReceiver": pt3080CommsAlarmEmailReceiver,
       "pt3080CommsWebServicePort": pt3080CommsWebServicePort,
       "pt3080CommsSCPIServicePort": pt3080CommsSCPIServicePort,
       "pt3080CommsSCPIServerBaudrate": pt3080CommsSCPIServerBaudrate,
       "pt3080CommsRipPort": pt3080CommsRipPort,
       "pt3080CommsSCPIUartInterface": pt3080CommsSCPIUartInterface,
       "pt3080CommsAccessAllowed": pt3080CommsAccessAllowed,
       "pt3080CommsAccessAllowedTimeout": pt3080CommsAccessAllowedTimeout,
       "pt3080CommsAccessAllowedTimeLeft": pt3080CommsAccessAllowedTimeLeft,
       "pt3080CommsAccessPasswordObserver": pt3080CommsAccessPasswordObserver,
       "pt3080CommsAccessPasswordOperator": pt3080CommsAccessPasswordOperator,
       "pt3080CommsAccessPasswordAdministrator": pt3080CommsAccessPasswordAdministrator,
       "pt3080CommsSNMPServicePort": pt3080CommsSNMPServicePort,
       "pt3080CommsSNMPReadOnlyCommunity": pt3080CommsSNMPReadOnlyCommunity,
       "pt3080CommsSNMPReadWriteCommunity": pt3080CommsSNMPReadWriteCommunity,
       "pt3080CommsSNMPTrapCommunity": pt3080CommsSNMPTrapCommunity,
       "pt3080CommsSNMPTrapDestination": pt3080CommsSNMPTrapDestination,
       "pt3080CommsSNMPTrapDestinationPort": pt3080CommsSNMPTrapDestinationPort,
       "pt3080CommsRemoteDhcpMode": pt3080CommsRemoteDhcpMode,
       "pt3080CommsGbeAdminDhcpMode": pt3080CommsGbeAdminDhcpMode,
       "pt3080CommsBackupDhcpMode": pt3080CommsBackupDhcpMode,
       "pt3080CommsLocalPhysicalInterface": pt3080CommsLocalPhysicalInterface,
       "pt3080CommsRemotePhysicalInterface": pt3080CommsRemotePhysicalInterface,
       "pt3080CommsGbeAdminPhysicalInterface": pt3080CommsGbeAdminPhysicalInterface,
       "pt3080CommsBroadcastStormProtection": pt3080CommsBroadcastStormProtection,
       "pt3080CommsIGMPv2UnsolicitedReportInterval": pt3080CommsIGMPv2UnsolicitedReportInterval,
       "pt3080CommsIGMPv3UnsolicitedReportInterval": pt3080CommsIGMPv3UnsolicitedReportInterval,
       "pt3080CommsIGMPQueryRobustnessCount": pt3080CommsIGMPQueryRobustnessCount,
       "pt3080CommsSeparatedSwitchPorts": pt3080CommsSeparatedSwitchPorts,
       "pt3080CommsIGMPVersion": pt3080CommsIGMPVersion,
       "pt3080CommsLocalIpMulticastAddr": pt3080CommsLocalIpMulticastAddr,
       "pt3080CommsLocalVlanEnable": pt3080CommsLocalVlanEnable,
       "pt3080CommsLocalVlanId": pt3080CommsLocalVlanId,
       "pt3080CommsLocalServiceSNMP": pt3080CommsLocalServiceSNMP,
       "pt3080CommsLocalServiceSCPI": pt3080CommsLocalServiceSCPI,
       "pt3080CommsLocalServiceTSoIP": pt3080CommsLocalServiceTSoIP,
       "pt3080CommsLocalServiceRIP": pt3080CommsLocalServiceRIP,
       "pt3080CommsRemoteIpMulticastAddr": pt3080CommsRemoteIpMulticastAddr,
       "pt3080CommsRemoteVlanEnable": pt3080CommsRemoteVlanEnable,
       "pt3080CommsRemoteVlanId": pt3080CommsRemoteVlanId,
       "pt3080CommsRemoteServiceSNMP": pt3080CommsRemoteServiceSNMP,
       "pt3080CommsRemoteServiceSCPI": pt3080CommsRemoteServiceSCPI,
       "pt3080CommsRemoteServiceTSoIP": pt3080CommsRemoteServiceTSoIP,
       "pt3080CommsRemoteServiceWeb": pt3080CommsRemoteServiceWeb,
       "pt3080CommsRemoteEnable": pt3080CommsRemoteEnable,
       "pt3080CommsRemoteServiceRIP": pt3080CommsRemoteServiceRIP,
       "pt3080CommsGbeAdminIpMulticastAddr": pt3080CommsGbeAdminIpMulticastAddr,
       "pt3080CommsGbeAdminVlanEnable": pt3080CommsGbeAdminVlanEnable,
       "pt3080CommsGbeAdminVlanId": pt3080CommsGbeAdminVlanId,
       "pt3080CommsGbeAdminServiceSNMP": pt3080CommsGbeAdminServiceSNMP,
       "pt3080CommsGbeAdminServiceSCPI": pt3080CommsGbeAdminServiceSCPI,
       "pt3080CommsGbeAdminServiceTSoIP": pt3080CommsGbeAdminServiceTSoIP,
       "pt3080CommsGbeAdminServiceWeb": pt3080CommsGbeAdminServiceWeb,
       "pt3080CommsGbeAdminEnable": pt3080CommsGbeAdminEnable,
       "pt3080CommsGbeAdminServiceRIP": pt3080CommsGbeAdminServiceRIP,
       "pt3080CommsBackupEnable": pt3080CommsBackupEnable,
       "pt3080CommsBackupPhysicalInterface": pt3080CommsBackupPhysicalInterface,
       "pt3080CommsBackupStaticIpAddr": pt3080CommsBackupStaticIpAddr,
       "pt3080CommsBackupStaticNetmask": pt3080CommsBackupStaticNetmask,
       "pt3080CommsBackupIpMulticastAddr": pt3080CommsBackupIpMulticastAddr,
       "pt3080CommsBackupVlanEnable": pt3080CommsBackupVlanEnable,
       "pt3080CommsBackupVlanId": pt3080CommsBackupVlanId,
       "pt3080CommsBackupServiceSNMP": pt3080CommsBackupServiceSNMP,
       "pt3080CommsBackupServiceSCPI": pt3080CommsBackupServiceSCPI,
       "pt3080CommsBackupServiceTSoIP": pt3080CommsBackupServiceTSoIP,
       "pt3080CommsBackupServiceWeb": pt3080CommsBackupServiceWeb,
       "pt3080CommsBackupServiceRIP": pt3080CommsBackupServiceRIP,
       "pt3080CommsBackupCurrentIpAddr": pt3080CommsBackupCurrentIpAddr,
       "pt3080CommsBackupCurrentNetmask": pt3080CommsBackupCurrentNetmask,
       "pt3080CommsBackupIpMulticastSourceFilterAddress1": pt3080CommsBackupIpMulticastSourceFilterAddress1,
       "pt3080CommsBackupIpMulticastSourceFilterAddress2": pt3080CommsBackupIpMulticastSourceFilterAddress2,
       "pt3080CommsBackupIpMulticastSourceFilterAddress3": pt3080CommsBackupIpMulticastSourceFilterAddress3,
       "pt3080CommsBackupIpMulticastSourceFilterAddress4": pt3080CommsBackupIpMulticastSourceFilterAddress4,
       "pt3080CommsBackupIpMulticastSourceFilterAddress5": pt3080CommsBackupIpMulticastSourceFilterAddress5,
       "pt3080CommsBackupIpMulticastSourceFilterAddress6": pt3080CommsBackupIpMulticastSourceFilterAddress6,
       "pt3080CommsLocalIpMulticastSourceFilterMode": pt3080CommsLocalIpMulticastSourceFilterMode,
       "pt3080CommsRemoteIpMulticastSourceFilterMode": pt3080CommsRemoteIpMulticastSourceFilterMode,
       "pt3080CommsGbeAdminIpMulticastSourceFilterMode": pt3080CommsGbeAdminIpMulticastSourceFilterMode,
       "pt3080CommsBackupIpMulticastSourceFilterMode": pt3080CommsBackupIpMulticastSourceFilterMode,
       "pt3080CommsLocalIpMulticastSourceFilterAddress1": pt3080CommsLocalIpMulticastSourceFilterAddress1,
       "pt3080CommsLocalIpMulticastSourceFilterAddress2": pt3080CommsLocalIpMulticastSourceFilterAddress2,
       "pt3080CommsLocalIpMulticastSourceFilterAddress3": pt3080CommsLocalIpMulticastSourceFilterAddress3,
       "pt3080CommsLocalIpMulticastSourceFilterAddress4": pt3080CommsLocalIpMulticastSourceFilterAddress4,
       "pt3080CommsLocalIpMulticastSourceFilterAddress5": pt3080CommsLocalIpMulticastSourceFilterAddress5,
       "pt3080CommsLocalIpMulticastSourceFilterAddress6": pt3080CommsLocalIpMulticastSourceFilterAddress6,
       "pt3080CommsRemoteIpMulticastSourceFilterAddress1": pt3080CommsRemoteIpMulticastSourceFilterAddress1,
       "pt3080CommsRemoteIpMulticastSourceFilterAddress2": pt3080CommsRemoteIpMulticastSourceFilterAddress2,
       "pt3080CommsRemoteIpMulticastSourceFilterAddress3": pt3080CommsRemoteIpMulticastSourceFilterAddress3,
       "pt3080CommsRemoteIpMulticastSourceFilterAddress4": pt3080CommsRemoteIpMulticastSourceFilterAddress4,
       "pt3080CommsRemoteIpMulticastSourceFilterAddress5": pt3080CommsRemoteIpMulticastSourceFilterAddress5,
       "pt3080CommsRemoteIpMulticastSourceFilterAddress6": pt3080CommsRemoteIpMulticastSourceFilterAddress6,
       "pt3080CommsGbeAdminIpMulticastSourceFilterAddress1": pt3080CommsGbeAdminIpMulticastSourceFilterAddress1,
       "pt3080CommsGbeAdminIpMulticastSourceFilterAddress2": pt3080CommsGbeAdminIpMulticastSourceFilterAddress2,
       "pt3080CommsGbeAdminIpMulticastSourceFilterAddress3": pt3080CommsGbeAdminIpMulticastSourceFilterAddress3,
       "pt3080CommsGbeAdminIpMulticastSourceFilterAddress4": pt3080CommsGbeAdminIpMulticastSourceFilterAddress4,
       "pt3080CommsGbeAdminIpMulticastSourceFilterAddress5": pt3080CommsGbeAdminIpMulticastSourceFilterAddress5,
       "pt3080CommsGbeAdminIpMulticastSourceFilterAddress6": pt3080CommsGbeAdminIpMulticastSourceFilterAddress6,
       "pt3080CommsStaticRouteTable": pt3080CommsStaticRouteTable,
       "pt3080CommsStaticRouteEntry": pt3080CommsStaticRouteEntry,
       "pt3080CommsStaticRouteNO": pt3080CommsStaticRouteNO,
       "pt3080CommsStaticRouteType": pt3080CommsStaticRouteType,
       "pt3080CommsStaticRoutePrefix": pt3080CommsStaticRoutePrefix,
       "pt3080CommsStaticRoutePrefixSize": pt3080CommsStaticRoutePrefixSize,
       "pt3080CommsStaticRouteTarget": pt3080CommsStaticRouteTarget,
       "pt3080CommsStaticRoutePhysicalInterface": pt3080CommsStaticRoutePhysicalInterface,
       "pt3080CommsSNMPTrapDestination2": pt3080CommsSNMPTrapDestination2,
       "pt3080CommsSNMPTrapDestinationPort2": pt3080CommsSNMPTrapDestinationPort2,
       "pt3080CommsSNMPTrapDestination3": pt3080CommsSNMPTrapDestination3,
       "pt3080CommsSNMPTrapDestinationPort3": pt3080CommsSNMPTrapDestinationPort3,
       "pt3080CommsSNMPTrapDestination4": pt3080CommsSNMPTrapDestination4,
       "pt3080CommsSNMPTrapDestinationPort4": pt3080CommsSNMPTrapDestinationPort4,
       "pt3080CommsSNMPTrapDestination5": pt3080CommsSNMPTrapDestination5,
       "pt3080CommsSNMPTrapDestinationPort5": pt3080CommsSNMPTrapDestinationPort5,
       "pt3080CommsPortDhcpMode": pt3080CommsPortDhcpMode,
       "pt3080CommsPortPhysicalInterface": pt3080CommsPortPhysicalInterface,
       "pt3080CommsPortStaticIpAddr": pt3080CommsPortStaticIpAddr,
       "pt3080CommsPortStaticNetmask": pt3080CommsPortStaticNetmask,
       "pt3080CommsPortIpMulticastAddr": pt3080CommsPortIpMulticastAddr,
       "pt3080CommsPortVlanEnable": pt3080CommsPortVlanEnable,
       "pt3080CommsPortVlanId": pt3080CommsPortVlanId,
       "pt3080CommsPortServiceSNMP": pt3080CommsPortServiceSNMP,
       "pt3080CommsPortServiceSCPI": pt3080CommsPortServiceSCPI,
       "pt3080CommsPortServiceTSoIP": pt3080CommsPortServiceTSoIP,
       "pt3080CommsPortServiceWeb": pt3080CommsPortServiceWeb,
       "pt3080CommsPortServiceRIP": pt3080CommsPortServiceRIP,
       "pt3080CommsPortCurrentIpAddr": pt3080CommsPortCurrentIpAddr,
       "pt3080CommsPortCurrentNetmask": pt3080CommsPortCurrentNetmask,
       "pt3080CommsPortIpMulticastSourceFilterAddress1": pt3080CommsPortIpMulticastSourceFilterAddress1,
       "pt3080CommsPortIpMulticastSourceFilterAddress2": pt3080CommsPortIpMulticastSourceFilterAddress2,
       "pt3080CommsPortIpMulticastSourceFilterAddress3": pt3080CommsPortIpMulticastSourceFilterAddress3,
       "pt3080CommsPortIpMulticastSourceFilterAddress4": pt3080CommsPortIpMulticastSourceFilterAddress4,
       "pt3080CommsPortIpMulticastSourceFilterAddress5": pt3080CommsPortIpMulticastSourceFilterAddress5,
       "pt3080CommsPortIpMulticastSourceFilterAddress6": pt3080CommsPortIpMulticastSourceFilterAddress6,
       "pt3080CommsPortIpMulticastSourceFilterMode": pt3080CommsPortIpMulticastSourceFilterMode,
       "pt3080CommsPortEnable": pt3080CommsPortEnable,
       "pt3080Demodulator": pt3080Demodulator,
       "pt3080DemodulatorFollowMode": pt3080DemodulatorFollowMode,
       "pt3080Demodulator1Available": pt3080Demodulator1Available,
       "pt3080Demodulator1FWVersion": pt3080Demodulator1FWVersion,
       "pt3080Demodulator1OutputTS": pt3080Demodulator1OutputTS,
       "pt3080Demodulator1MerLimit": pt3080Demodulator1MerLimit,
       "pt3080Demodulator1PreVirterbiErrorRateLimit": pt3080Demodulator1PreVirterbiErrorRateLimit,
       "pt3080Demodulator1PostVirterbiErrorRateLimit": pt3080Demodulator1PostVirterbiErrorRateLimit,
       "pt3080Demodulator1FelStatus": pt3080Demodulator1FelStatus,
       "pt3080Demodulator1UncorrectedPackets": pt3080Demodulator1UncorrectedPackets,
       "pt3080Demodulator1Mer": pt3080Demodulator1Mer,
       "pt3080Demodulator1PreVirterbiErrorRate": pt3080Demodulator1PreVirterbiErrorRate,
       "pt3080Demodulator1PostVirterbiErrorRate": pt3080Demodulator1PostVirterbiErrorRate,
       "pt3080Demodulator1ActualGuardInterval": pt3080Demodulator1ActualGuardInterval,
       "pt3080Demodulator1Actualifft": pt3080Demodulator1Actualifft,
       "pt3080Demodulator1ActualConstellation": pt3080Demodulator1ActualConstellation,
       "pt3080Demodulator1ActualHierarchy": pt3080Demodulator1ActualHierarchy,
       "pt3080Demodulator1ActualCodeRateHighPrio": pt3080Demodulator1ActualCodeRateHighPrio,
       "pt3080Demodulator1ActualCodeRateLowPrio": pt3080Demodulator1ActualCodeRateLowPrio,
       "pt3080Demodulator1ActualDeepInterleaver": pt3080Demodulator1ActualDeepInterleaver,
       "pt3080Demodulator1ActualMpeFecHighPrio": pt3080Demodulator1ActualMpeFecHighPrio,
       "pt3080Demodulator1ActualMpeFecLowPrio": pt3080Demodulator1ActualMpeFecLowPrio,
       "pt3080Demodulator1ActualTimeSlicingHighPrio": pt3080Demodulator1ActualTimeSlicingHighPrio,
       "pt3080Demodulator1ActualTimeSlicingLowPrio": pt3080Demodulator1ActualTimeSlicingLowPrio,
       "pt3080Demodulator1ActualCellID": pt3080Demodulator1ActualCellID,
       "pt3080Demodulator1ActualDVBHMode": pt3080Demodulator1ActualDVBHMode,
       "pt3080Demodulator2Available": pt3080Demodulator2Available,
       "pt3080Demodulator2FWVersion": pt3080Demodulator2FWVersion,
       "pt3080Demodulator2OutputTS": pt3080Demodulator2OutputTS,
       "pt3080Demodulator2MerLimit": pt3080Demodulator2MerLimit,
       "pt3080Demodulator2PreVirterbiErrorRateLimit": pt3080Demodulator2PreVirterbiErrorRateLimit,
       "pt3080Demodulator2PostVirterbiErrorRateLimit": pt3080Demodulator2PostVirterbiErrorRateLimit,
       "pt3080Demodulator2FelStatus": pt3080Demodulator2FelStatus,
       "pt3080Demodulator2UncorrectedPackets": pt3080Demodulator2UncorrectedPackets,
       "pt3080Demodulator2Mer": pt3080Demodulator2Mer,
       "pt3080Demodulator2PreVirterbiErrorRate": pt3080Demodulator2PreVirterbiErrorRate,
       "pt3080Demodulator2PostVirterbiErrorRate": pt3080Demodulator2PostVirterbiErrorRate,
       "pt3080Demodulator2ActualGuardInterval": pt3080Demodulator2ActualGuardInterval,
       "pt3080Demodulator2Actualifft": pt3080Demodulator2Actualifft,
       "pt3080Demodulator2ActualConstellation": pt3080Demodulator2ActualConstellation,
       "pt3080Demodulator2ActualHierarchy": pt3080Demodulator2ActualHierarchy,
       "pt3080Demodulator2ActualCodeRateHighPrio": pt3080Demodulator2ActualCodeRateHighPrio,
       "pt3080Demodulator2ActualCodeRateLowPrio": pt3080Demodulator2ActualCodeRateLowPrio,
       "pt3080Demodulator2ActualDeepInterleaver": pt3080Demodulator2ActualDeepInterleaver,
       "pt3080Demodulator2ActualMpeFecHighPrio": pt3080Demodulator2ActualMpeFecHighPrio,
       "pt3080Demodulator2ActualMpeFecLowPrio": pt3080Demodulator2ActualMpeFecLowPrio,
       "pt3080Demodulator2ActualTimeSlicingHighPrio": pt3080Demodulator2ActualTimeSlicingHighPrio,
       "pt3080Demodulator2ActualTimeSlicingLowPrio": pt3080Demodulator2ActualTimeSlicingLowPrio,
       "pt3080Demodulator2ActualCellID": pt3080Demodulator2ActualCellID,
       "pt3080Demodulator2ActualDVBHMode": pt3080Demodulator2ActualDVBHMode,
       "pt3080Precorrector": pt3080Precorrector,
       "pt3080PrecorrectorLinearAdaptiveMode": pt3080PrecorrectorLinearAdaptiveMode,
       "pt3080PrecorrectorLinearMode": pt3080PrecorrectorLinearMode,
       "pt3080PrecorrectorNonlinearAdaptiveMode": pt3080PrecorrectorNonlinearAdaptiveMode,
       "pt3080PrecorrectorNonlinearMode": pt3080PrecorrectorNonlinearMode,
       "pt3080PrecorrectorLastTurnAroundTime": pt3080PrecorrectorLastTurnAroundTime,
       "pt3080PrecorrectorSecondsSinceLastUpdate": pt3080PrecorrectorSecondsSinceLastUpdate,
       "pt3080PrecorrectorLinearMonitorSenseBadCount": pt3080PrecorrectorLinearMonitorSenseBadCount,
       "pt3080PrecorrectorNonlinearMonitorSenseBadCount": pt3080PrecorrectorNonlinearMonitorSenseBadCount,
       "pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable": pt3080PrecorrectorLinearAdaptiveAmplitudeRippleEnable,
       "pt3080PrecorrectorLinearAdaptiveGroupDelayEnable": pt3080PrecorrectorLinearAdaptiveGroupDelayEnable,
       "pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable": pt3080PrecorrectorNonlinearAdaptiveLowerShoulderEnable,
       "pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable": pt3080PrecorrectorNonlinearAdaptiveUpperShoulderEnable,
       "pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis": pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetHysteresis,
       "pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis": pt3080PrecorrectorLinearAdaptiveGroupDelayTargetHysteresis,
       "pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis": pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetHysteresis,
       "pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis": pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetHysteresis,
       "pt3080PrecorrectorLinCleanrun": pt3080PrecorrectorLinCleanrun,
       "pt3080PrecorrectorLinearMonitorIterations": pt3080PrecorrectorLinearMonitorIterations,
       "pt3080PrecorrectorLinearLoadNeutral": pt3080PrecorrectorLinearLoadNeutral,
       "pt3080PrecorrectorLinearLoadFactory": pt3080PrecorrectorLinearLoadFactory,
       "pt3080PrecorrectorLinearMonitorSenseLevel": pt3080PrecorrectorLinearMonitorSenseLevel,
       "pt3080PrecorrectorLinearMonitorSenseValid": pt3080PrecorrectorLinearMonitorSenseValid,
       "pt3080PrecorrectorLinearMonitorStatus": pt3080PrecorrectorLinearMonitorStatus,
       "pt3080PrecorrectorLinearUpdateFactoryCurve": pt3080PrecorrectorLinearUpdateFactoryCurve,
       "pt3080PrecorrectorLinearMonitorAmplitudeRipple": pt3080PrecorrectorLinearMonitorAmplitudeRipple,
       "pt3080PrecorrectorLinearMonitorGroupDelay": pt3080PrecorrectorLinearMonitorGroupDelay,
       "pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel": pt3080PrecorrectorNonlinearMonitorLowerShoulderLevel,
       "pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel": pt3080PrecorrectorNonlinearMonitorUpperShoulderLevel,
       "pt3080PrecorrectorLinearMonitorAmplitudeRippleValid": pt3080PrecorrectorLinearMonitorAmplitudeRippleValid,
       "pt3080PrecorrectorLinearMonitorGroupDelayValid": pt3080PrecorrectorLinearMonitorGroupDelayValid,
       "pt3080PrecorrectorNonlinearMonitorLowerShoulderValid": pt3080PrecorrectorNonlinearMonitorLowerShoulderValid,
       "pt3080PrecorrectorNonlinearMonitorUpperShoulderValid": pt3080PrecorrectorNonlinearMonitorUpperShoulderValid,
       "pt3080PrecorrectorNlinCleanrun": pt3080PrecorrectorNlinCleanrun,
       "pt3080PrecorrectorNonlinearMonitorIterations": pt3080PrecorrectorNonlinearMonitorIterations,
       "pt3080PrecorrectorNonlinearLoadNeutral": pt3080PrecorrectorNonlinearLoadNeutral,
       "pt3080PrecorrectorNonlinearLoadFactory": pt3080PrecorrectorNonlinearLoadFactory,
       "pt3080PrecorrectorNonlinearMonitorSenseLevel": pt3080PrecorrectorNonlinearMonitorSenseLevel,
       "pt3080PrecorrectorNonlinearMonitorSenseValid": pt3080PrecorrectorNonlinearMonitorSenseValid,
       "pt3080PrecorrectorNonlinearMonitorStatus": pt3080PrecorrectorNonlinearMonitorStatus,
       "pt3080PrecorrectorNonlinearUpdateFactoryCurve": pt3080PrecorrectorNonlinearUpdateFactoryCurve,
       "pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel": pt3080PrecorrectorLinearAdaptiveAmplitudeRippleTargetLevel,
       "pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel": pt3080PrecorrectorLinearAdaptiveGroupDelayTargetLevel,
       "pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel": pt3080PrecorrectorNonlinearAdaptiveLowerShoulderTargetLevel,
       "pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel": pt3080PrecorrectorNonlinearAdaptiveUpperShoulderTargetLevel,
       "pt3080PrecorrectorLinearSenseEnable": pt3080PrecorrectorLinearSenseEnable,
       "pt3080PrecorrectorLinearMonitorDiscartedIterations": pt3080PrecorrectorLinearMonitorDiscartedIterations,
       "pt3080PrecorrectorNonlinearSenseEnable": pt3080PrecorrectorNonlinearSenseEnable,
       "pt3080PrecorrectorNonlinearMonitorDiscartedIterations": pt3080PrecorrectorNonlinearMonitorDiscartedIterations,
       "pt3080PrecorrectorNonlinearMonitorMer": pt3080PrecorrectorNonlinearMonitorMer,
       "pt3080PrecorrectorNonlinearMonitorMerValid": pt3080PrecorrectorNonlinearMonitorMerValid,
       "pt3080PrecorrectorNonlinearMonitorPapr": pt3080PrecorrectorNonlinearMonitorPapr,
       "pt3080PrecorrectorNonlinearMonitorPaprValid": pt3080PrecorrectorNonlinearMonitorPaprValid,
       "pt3080PrecorrectorNonlinearAdaptiveAveraging": pt3080PrecorrectorNonlinearAdaptiveAveraging,
       "pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable": pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprEnable,
       "pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit": pt3080PrecorrectorNonlinearAdaptiveMaxRfPaprLimit,
       "pt3080PrecorrectorNonlinearAdaptiveMerTarget": pt3080PrecorrectorNonlinearAdaptiveMerTarget,
       "pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis": pt3080PrecorrectorNonlinearAdaptiveMerTargetHysteresis,
       "pt3080PrecorrectorNonlinearAdaptiveMerEnable": pt3080PrecorrectorNonlinearAdaptiveMerEnable,
       "pt3080PrecorrectorPaprClipping": pt3080PrecorrectorPaprClipping,
       "pt3080PrecorrectorPaprShaping": pt3080PrecorrectorPaprShaping,
       "pt3080PrecorrectorClipperAdaptiveMode": pt3080PrecorrectorClipperAdaptiveMode,
       "pt3080PrecorrectorClipperMonitorStatus": pt3080PrecorrectorClipperMonitorStatus,
       "pt3080PrecorrectorClipperMonitorShoulderLevelLower": pt3080PrecorrectorClipperMonitorShoulderLevelLower,
       "pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid": pt3080PrecorrectorClipperMonitorShoulderLevelLowerValid,
       "pt3080PrecorrectorClipperMonitorShoulderLevelUpper": pt3080PrecorrectorClipperMonitorShoulderLevelUpper,
       "pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid": pt3080PrecorrectorClipperMonitorShoulderLevelUpperValid,
       "pt3080PrecorrectorClipperMonitorMer": pt3080PrecorrectorClipperMonitorMer,
       "pt3080PrecorrectorClipperMonitorMerValid": pt3080PrecorrectorClipperMonitorMerValid,
       "pt3080PrecorrectorClipperMonitorPapr": pt3080PrecorrectorClipperMonitorPapr,
       "pt3080PrecorrectorClipperMonitorPaprValid": pt3080PrecorrectorClipperMonitorPaprValid,
       "pt3080PrecorrectorClipperMonitorIterations": pt3080PrecorrectorClipperMonitorIterations,
       "pt3080PrecorrectorClipperMode": pt3080PrecorrectorClipperMode,
       "pt3080PrecorrectorClipperAdaptive": pt3080PrecorrectorClipperAdaptive,
       "pt3080PrecorrectorClipperEnable": pt3080PrecorrectorClipperEnable,
       "pt3080PrecorrectorNonlinearAttenuation": pt3080PrecorrectorNonlinearAttenuation,
       "pt3080PrecorrectorLinearAttenuation": pt3080PrecorrectorLinearAttenuation,
       "pt3080PrecorrectorLinearAdaptive": pt3080PrecorrectorLinearAdaptive,
       "pt3080PrecorrectorNonlinearAdaptive": pt3080PrecorrectorNonlinearAdaptive,
       "pt3080PrecorrectorClipperAdaptiveShaping": pt3080PrecorrectorClipperAdaptiveShaping,
       "pt3080Reception": pt3080Reception,
       "pt3080ReceptionRFFrequency": pt3080ReceptionRFFrequency,
       "pt3080ReceptionRFFrequencyOffset": pt3080ReceptionRFFrequencyOffset,
       "pt3080ReceptionIFInputPolicy": pt3080ReceptionIFInputPolicy,
       "pt3080ReceptionIFFrequency": pt3080ReceptionIFFrequency,
       "pt3080ReceptionIFPolarity": pt3080ReceptionIFPolarity,
       "pt3080ReceptionRFSquelchEnable": pt3080ReceptionRFSquelchEnable,
       "pt3080ReceptionRFSquelchThreshold": pt3080ReceptionRFSquelchThreshold,
       "pt3080ReceptionRFSquelchHysteresis": pt3080ReceptionRFSquelchHysteresis,
       "pt3080ReceptionGainControl": pt3080ReceptionGainControl,
       "pt3080ReceptionGainManualValue": pt3080ReceptionGainManualValue,
       "pt3080ReceptionGainLimitEnable": pt3080ReceptionGainLimitEnable,
       "pt3080ReceptionGainLimit": pt3080ReceptionGainLimit,
       "pt3080ReceptionGainCurrent": pt3080ReceptionGainCurrent,
       "pt3080ReceptionIFRFtoIFHoldoverDelay": pt3080ReceptionIFRFtoIFHoldoverDelay,
       "pt3080ReceptionIFIFtoRFHoldoverDelay": pt3080ReceptionIFIFtoRFHoldoverDelay,
       "pt3080ReceptionIFInput": pt3080ReceptionIFInput,
       "pt3080ReceptionRFInputLevel": pt3080ReceptionRFInputLevel,
       "pt3080ReceptionIFInputLevel": pt3080ReceptionIFInputLevel,
       "pt3080ReceptionBandwidth": pt3080ReceptionBandwidth,
       "pt3080ReceptionRFPolarity": pt3080ReceptionRFPolarity,
       "pt3080ReceptionRFInputLevelHysteresis": pt3080ReceptionRFInputLevelHysteresis,
       "pt3080ReceptionRFInputLevelThreshold": pt3080ReceptionRFInputLevelThreshold,
       "pt3080ReceptionAGCMode": pt3080ReceptionAGCMode,
       "pt3080ReceptionAGCHysteresis": pt3080ReceptionAGCHysteresis,
       "pt3080ReceptionRFTrackingFilterEnable": pt3080ReceptionRFTrackingFilterEnable,
       "pt3080ReceptionRFifLevel": pt3080ReceptionRFifLevel,
       "pt3080ReceptionRFNominalInputLevel": pt3080ReceptionRFNominalInputLevel,
       "pt3080ReceptionTunerHWVersion": pt3080ReceptionTunerHWVersion,
       "pt3080ReceptionTunerHWType": pt3080ReceptionTunerHWType,
       "pt3080ReceptionTunerHWID": pt3080ReceptionTunerHWID,
       "pt3080ReceptionTunerHWSerialNumber": pt3080ReceptionTunerHWSerialNumber,
       "pt3080ReceptionTunerHWCalibrationDate": pt3080ReceptionTunerHWCalibrationDate,
       "pt3080ReceptionTunerHWCalibrationDataVersion": pt3080ReceptionTunerHWCalibrationDataVersion,
       "pt3080ReceptionTunerHWCalibrationSWVersion": pt3080ReceptionTunerHWCalibrationSWVersion,
       "pt3080Backplane": pt3080Backplane,
       "pt3080BackplanePolarityHardMute": pt3080BackplanePolarityHardMute,
       "pt3080BackplanePolarityRFFail": pt3080BackplanePolarityRFFail,
       "pt3080ASI": pt3080ASI,
       "pt3080ASIInput1SyncTimeout": pt3080ASIInput1SyncTimeout,
       "pt3080ASIInput1DataErrorLimit": pt3080ASIInput1DataErrorLimit,
       "pt3080ASIInput1SyncStatus": pt3080ASIInput1SyncStatus,
       "pt3080ASIInput1SyncSignal": pt3080ASIInput1SyncSignal,
       "pt3080ASIInput1SyncTSSize": pt3080ASIInput1SyncTSSize,
       "pt3080ASIInput1LineErrors": pt3080ASIInput1LineErrors,
       "pt3080ASIInput1LineRate": pt3080ASIInput1LineRate,
       "pt3080ASIInput1LineErrorRate": pt3080ASIInput1LineErrorRate,
       "pt3080ASIInput1DataErrors": pt3080ASIInput1DataErrors,
       "pt3080ASIInput1DataRate": pt3080ASIInput1DataRate,
       "pt3080ASIInput1DataErrorRate": pt3080ASIInput1DataErrorRate,
       "pt3080ASIInput1ClearErrorCounters": pt3080ASIInput1ClearErrorCounters,
       "pt3080ASIInput2SyncTimeout": pt3080ASIInput2SyncTimeout,
       "pt3080ASIInput2DataErrorLimit": pt3080ASIInput2DataErrorLimit,
       "pt3080ASIInput2SyncStatus": pt3080ASIInput2SyncStatus,
       "pt3080ASIInput2SyncSignal": pt3080ASIInput2SyncSignal,
       "pt3080ASIInput2SyncTSSize": pt3080ASIInput2SyncTSSize,
       "pt3080ASIInput2LineErrors": pt3080ASIInput2LineErrors,
       "pt3080ASIInput2LineRate": pt3080ASIInput2LineRate,
       "pt3080ASIInput2LineErrorRate": pt3080ASIInput2LineErrorRate,
       "pt3080ASIInput2DataErrors": pt3080ASIInput2DataErrors,
       "pt3080ASIInput2DataRate": pt3080ASIInput2DataRate,
       "pt3080ASIInput2DataErrorRate": pt3080ASIInput2DataErrorRate,
       "pt3080ASIInput2ClearErrorCounters": pt3080ASIInput2ClearErrorCounters,
       "pt3080Notifs": pt3080Notifs,
       "pt3080Notif": pt3080Notif,
       "pt3080NotifModulatorAlarm": pt3080NotifModulatorAlarm,
       "pt3080NotifTSPrimaryAlarm": pt3080NotifTSPrimaryAlarm,
       "pt3080NotifTSSecondaryAlarm": pt3080NotifTSSecondaryAlarm,
       "pt3080NotifSFNAlarm": pt3080NotifSFNAlarm,
       "pt3080NotifRefenceClockAlarm": pt3080NotifRefenceClockAlarm,
       "pt3080NotifRFAlarm": pt3080NotifRFAlarm,
       "pt3080NotifGNSSAlarm": pt3080NotifGNSSAlarm,
       "pt3080NotifTSoIPAlarm": pt3080NotifTSoIPAlarm,
       "pt3080NotifExternalAlarm": pt3080NotifExternalAlarm,
       "pt3080NotifHWMonitorAlarm": pt3080NotifHWMonitorAlarm,
       "pt3080NotifCommAlarm": pt3080NotifCommAlarm,
       "pt3080NotifASIAlarm": pt3080NotifASIAlarm,
       "pt3080NotifInternalAlarm": pt3080NotifInternalAlarm,
       "pt3080NotifTSPrimarySyncLossAlarm": pt3080NotifTSPrimarySyncLossAlarm,
       "pt3080NotifTSPrimarySyncErrorAlarm": pt3080NotifTSPrimarySyncErrorAlarm,
       "pt3080NotifTSPrimaryPCRErrorAlarm": pt3080NotifTSPrimaryPCRErrorAlarm,
       "pt3080NotifTSPrimaryPATLossAlarm": pt3080NotifTSPrimaryPATLossAlarm,
       "pt3080NotifTSPrimaryTSIDWrongAlarm": pt3080NotifTSPrimaryTSIDWrongAlarm,
       "pt3080NotifTSPrimaryNWIDWrongAlarm": pt3080NotifTSPrimaryNWIDWrongAlarm,
       "pt3080NotifTSPrimaryStuffingRateExceededAlarm": pt3080NotifTSPrimaryStuffingRateExceededAlarm,
       "pt3080NotifTSPrimaryBufferPoolExceededAlarm": pt3080NotifTSPrimaryBufferPoolExceededAlarm,
       "pt3080NotifTSPrimarySTSJitterExceededAlarm": pt3080NotifTSPrimarySTSJitterExceededAlarm,
       "pt3080NotifTSPrimaryMIPDataMissingAlarm": pt3080NotifTSPrimaryMIPDataMissingAlarm,
       "pt3080NotifTSPrimaryMIPPriorityBadAlarm": pt3080NotifTSPrimaryMIPPriorityBadAlarm,
       "pt3080NotifTSSecondarySyncLossAlarm": pt3080NotifTSSecondarySyncLossAlarm,
       "pt3080NotifTSSecondarySyncErrorAlarm": pt3080NotifTSSecondarySyncErrorAlarm,
       "pt3080NotifTSSecondaryPCRErrorAlarm": pt3080NotifTSSecondaryPCRErrorAlarm,
       "pt3080NotifTSSecondaryPATLossAlarm": pt3080NotifTSSecondaryPATLossAlarm,
       "pt3080NotifTSSecondaryTSIDWrongAlarm": pt3080NotifTSSecondaryTSIDWrongAlarm,
       "pt3080NotifTSSecondaryNWIDWrongAlarm": pt3080NotifTSSecondaryNWIDWrongAlarm,
       "pt3080NotifTSSecondaryStuffingRateExceededAlarm": pt3080NotifTSSecondaryStuffingRateExceededAlarm,
       "pt3080NotifTSSecondaryBufferPoolExceededAlarm": pt3080NotifTSSecondaryBufferPoolExceededAlarm,
       "pt3080NotifTSSecondarySTSJitterExceededAlarm": pt3080NotifTSSecondarySTSJitterExceededAlarm,
       "pt3080NotifTSSecondaryMIPDataMissingAlarm": pt3080NotifTSSecondaryMIPDataMissingAlarm,
       "pt3080NotifTSSecondaryMIPPriorityBadAlarm": pt3080NotifTSSecondaryMIPPriorityBadAlarm,
       "pt3080NotifRFOverloadProtectionAlarm": pt3080NotifRFOverloadProtectionAlarm,
       "pt3080NotifCommeth0Alarm": pt3080NotifCommeth0Alarm,
       "pt3080NotifCommeth1Alarm": pt3080NotifCommeth1Alarm,
       "pt3080NotifCommeth2Alarm": pt3080NotifCommeth2Alarm,
       "pt3080NotifCommeth3Alarm": pt3080NotifCommeth3Alarm,
       "pt3080NotifCommeth4Alarm": pt3080NotifCommeth4Alarm,
       "pt3080NotifExternalInput1Alarm": pt3080NotifExternalInput1Alarm,
       "pt3080NotifExternalInput2Alarm": pt3080NotifExternalInput2Alarm,
       "pt3080NotifExternalInput3Alarm": pt3080NotifExternalInput3Alarm,
       "pt3080NotifExternalInput4Alarm": pt3080NotifExternalInput4Alarm,
       "pt3080NotifRefenceClockExtern1PPSLossAlarm": pt3080NotifRefenceClockExtern1PPSLossAlarm,
       "pt3080NotifRefenceClockIntern1PPSLossAlarm": pt3080NotifRefenceClockIntern1PPSLossAlarm,
       "pt3080NotifRefenceClockExtern10MHzLossAlarm": pt3080NotifRefenceClockExtern10MHzLossAlarm,
       "pt3080NotifRFAlcRangeAlarm": pt3080NotifRFAlcRangeAlarm,
       "pt3080NotifSFNResyncAlarm": pt3080NotifSFNResyncAlarm,
       "pt3080NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm": pt3080NotifSFNTSPrimaryMaxDelayOffsetExceededAlarm,
       "pt3080NotifSFNTSPrimaryNetworkDelayExceededAlarm": pt3080NotifSFNTSPrimaryNetworkDelayExceededAlarm,
       "pt3080NotifSFNTSSecondaryMaxDelayOffsetExceededAlarm": pt3080NotifSFNTSSecondaryMaxDelayOffsetExceededAlarm,
       "pt3080NotifSFNTSSecondaryNetworkDelayExceededAlarm": pt3080NotifSFNTSSecondaryNetworkDelayExceededAlarm,
       "pt3080NotifRFLevelOutOfRangeAlarm": pt3080NotifRFLevelOutOfRangeAlarm,
       "pt3080NotifRefenceClockNTPSyncLossAlarm": pt3080NotifRefenceClockNTPSyncLossAlarm,
       "pt3080NotifSFNTSPrimarySeamlessDelayTooSmallAlarm": pt3080NotifSFNTSPrimarySeamlessDelayTooSmallAlarm,
       "pt3080NotifSFNTSPrimaryMIPConfigErrorAlarm": pt3080NotifSFNTSPrimaryMIPConfigErrorAlarm,
       "pt3080NotifSFNTSSecondarySeamlessDelayTooSmallAlarm": pt3080NotifSFNTSSecondarySeamlessDelayTooSmallAlarm,
       "pt3080NotifSFNTSSecondaryMIPConfigErrorAlarm": pt3080NotifSFNTSSecondaryMIPConfigErrorAlarm,
       "pt3080NotifGNSSUnlockedAlarm": pt3080NotifGNSSUnlockedAlarm,
       "pt3080NotifGNSSAntennaFaultAlarm": pt3080NotifGNSSAntennaFaultAlarm,
       "pt3080NotifGNSSHoldOverAlarm": pt3080NotifGNSSHoldOverAlarm,
       "pt3080NotifRefenceClockExternal10MHzHoldOverAlarm": pt3080NotifRefenceClockExternal10MHzHoldOverAlarm,
       "pt3080NotifRefenceClockExternal1PPSHoldOverAlarm": pt3080NotifRefenceClockExternal1PPSHoldOverAlarm,
       "pt3080NotifASIASI1ErrorRateEceeededAlarm": pt3080NotifASIASI1ErrorRateEceeededAlarm,
       "pt3080NotifASIASI2ErrorRateEceeededAlarm": pt3080NotifASIASI2ErrorRateEceeededAlarm,
       "pt3080NotifTSoIPRx1PackageErrorRationExceededAlarm": pt3080NotifTSoIPRx1PackageErrorRationExceededAlarm,
       "pt3080NotifTSoIPRx2PackageErrorRationExceededAlarm": pt3080NotifTSoIPRx2PackageErrorRationExceededAlarm,
       "pt3080NotifTSoIPRx1SyncLossAlarm": pt3080NotifTSoIPRx1SyncLossAlarm,
       "pt3080NotifTSoIPRx2SyncLossAlarm": pt3080NotifTSoIPRx2SyncLossAlarm,
       "pt3080NotifInternalBackplaneAlarm": pt3080NotifInternalBackplaneAlarm,
       "pt3080NotifInternalReferenceClockAlarm": pt3080NotifInternalReferenceClockAlarm,
       "pt3080NotifInternalUpConverterAlarm": pt3080NotifInternalUpConverterAlarm,
       "pt3080NotifInternalDownConverterAlarm": pt3080NotifInternalDownConverterAlarm,
       "pt3080NotifInternalMainboardAlarm": pt3080NotifInternalMainboardAlarm,
       "pt3080NotifInternalBatteryAlarm": pt3080NotifInternalBatteryAlarm,
       "pt3080NotifInternalFirmware1Alarm": pt3080NotifInternalFirmware1Alarm,
       "pt3080NotifInternalGNSSAlarm": pt3080NotifInternalGNSSAlarm,
       "pt3080NotifInternalSatelliteAlarm": pt3080NotifInternalSatelliteAlarm,
       "pt3080NotifInternalEthAlarm": pt3080NotifInternalEthAlarm,
       "pt3080NotifHWMonitorFPGAAlarm": pt3080NotifHWMonitorFPGAAlarm,
       "pt3080NotifHWMonitorMainBoardCPUTemperatureAlarm": pt3080NotifHWMonitorMainBoardCPUTemperatureAlarm,
       "pt3080NotifHWMonitorMainBoardTemperatureAlarm": pt3080NotifHWMonitorMainBoardTemperatureAlarm,
       "pt3080NotifHWMonitorLeftFanAlarm": pt3080NotifHWMonitorLeftFanAlarm,
       "pt3080NotifHWMonitorRightFan2Alarm": pt3080NotifHWMonitorRightFan2Alarm,
       "pt3080NotifHWMonitorBackplaneTemperatureAlarm": pt3080NotifHWMonitorBackplaneTemperatureAlarm,
       "pt3080NotifTSPrimaryInputTSHoldOverAlarm": pt3080NotifTSPrimaryInputTSHoldOverAlarm,
       "pt3080NotifInternalPLLUnlockedAlarm": pt3080NotifInternalPLLUnlockedAlarm,
       "pt3080NotifExternalInput5Alarm": pt3080NotifExternalInput5Alarm,
       "pt3080NotifSFNUntimedModeAlarm": pt3080NotifSFNUntimedModeAlarm,
       "pt3080NotifSFNFreeRunningModeAlarm": pt3080NotifSFNFreeRunningModeAlarm,
       "pt3080NotifExternalInput6Alarm": pt3080NotifExternalInput6Alarm,
       "pt3080NotifExternalInput7Alarm": pt3080NotifExternalInput7Alarm,
       "pt3080NotifExternalInput8Alarm": pt3080NotifExternalInput8Alarm,
       "pt3080NotifTSPrimaryDelayMarginAlarm": pt3080NotifTSPrimaryDelayMarginAlarm,
       "pt3080NotifTSSecondaryDelayMarginAlarm": pt3080NotifTSSecondaryDelayMarginAlarm,
       "pt3080NotifMessage": pt3080NotifMessage,
       "pt3080NotifState": pt3080NotifState,
       "pt3080NotifLocalTime": pt3080NotifLocalTime,
       "pt3080Conformance": pt3080Conformance,
       "pt3080Compliances": pt3080Compliances,
       "pt3080Compliance": pt3080Compliance,
       "pt3080Groups": pt3080Groups,
       "pt3080SystemGroup": pt3080SystemGroup,
       "pt3080ModeGroup": pt3080ModeGroup,
       "pt3080InputGroup": pt3080InputGroup,
       "pt3080OutputGroup": pt3080OutputGroup,
       "pt3080GpsGroup": pt3080GpsGroup,
       "pt3080ChannelFilterGroup": pt3080ChannelFilterGroup,
       "pt3080TSoIPGroup": pt3080TSoIPGroup,
       "pt3080MonitorGroup": pt3080MonitorGroup,
       "pt3080TestGroup": pt3080TestGroup,
       "pt3080AlarmGroup": pt3080AlarmGroup,
       "pt3080PresetGroup": pt3080PresetGroup,
       "pt3080EventlogGroup": pt3080EventlogGroup,
       "pt3080CommsGroup": pt3080CommsGroup,
       "pt3080DemodulatorGroup": pt3080DemodulatorGroup,
       "pt3080PrecorrectorGroup": pt3080PrecorrectorGroup,
       "pt3080ReceptionGroup": pt3080ReceptionGroup,
       "pt3080BackplaneGroup": pt3080BackplaneGroup,
       "pt3080ASIGroup": pt3080ASIGroup,
       "pt3080NotifsGroup": pt3080NotifsGroup,
       "pt3080Agent": pt3080Agent,
       "pt3080NotificationsGroups": pt3080NotificationsGroups,
       "pt3080NotifGroupModulatorAlarm": pt3080NotifGroupModulatorAlarm,
       "pt3080NotifGroupTSPrimaryAlarm": pt3080NotifGroupTSPrimaryAlarm,
       "pt3080NotifGroupTSSecondaryAlarm": pt3080NotifGroupTSSecondaryAlarm,
       "pt3080NotifGroupSFNAlarm": pt3080NotifGroupSFNAlarm,
       "pt3080NotifGroupRefenceClockAlarm": pt3080NotifGroupRefenceClockAlarm,
       "pt3080NotifGroupRFAlarm": pt3080NotifGroupRFAlarm,
       "pt3080NotifGroupGNSSAlarm": pt3080NotifGroupGNSSAlarm,
       "pt3080NotifGroupTSoIPAlarm": pt3080NotifGroupTSoIPAlarm,
       "pt3080NotifGroupExternalAlarm": pt3080NotifGroupExternalAlarm,
       "pt3080NotifGroupHWMonitorAlarm": pt3080NotifGroupHWMonitorAlarm,
       "pt3080NotifGroupCommAlarm": pt3080NotifGroupCommAlarm,
       "pt3080NotifGroupASIAlarm": pt3080NotifGroupASIAlarm,
       "pt3080NotifGroupInternalAlarm": pt3080NotifGroupInternalAlarm}
)
