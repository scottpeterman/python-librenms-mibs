# SNMP MIB module (ATEN-IPMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\supermicro\ATEN-IPMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:21 2025
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
    "enterprises",
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

aten = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21317)
)
if mibBuilder.loadTexts:
    aten.setRevisions(
        ("2009-03-20 11:50",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipmi_ObjectIdentity = ObjectIdentity
ipmi = _Ipmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1)
)
_Sel_Type = Integer32
_Sel_Object = MibScalar
sel = _Sel_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 2),
    _Sel_Type()
)
sel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sel.setStatus("current")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1)
)
sensorEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "sensorNumber"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorNumber_Type(Integer32):
    """Custom type sensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SensorNumber_Type.__name__ = "Integer32"
_SensorNumber_Object = MibTableColumn
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 1),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("current")


class _SensorReading_Type(OctetString):
    """Custom type sensorReading based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SensorReading_Type.__name__ = "OctetString"
_SensorReading_Object = MibTableColumn
sensorReading = _SensorReading_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 2),
    _SensorReading_Type()
)
sensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorReading.setStatus("current")
_SensorPositiveHysteresis_Type = Integer32
_SensorPositiveHysteresis_Object = MibTableColumn
sensorPositiveHysteresis = _SensorPositiveHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 3),
    _SensorPositiveHysteresis_Type()
)
sensorPositiveHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorPositiveHysteresis.setStatus("current")
_SensorNegativeHysteresis_Type = Integer32
_SensorNegativeHysteresis_Object = MibTableColumn
sensorNegativeHysteresis = _SensorNegativeHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 4),
    _SensorNegativeHysteresis_Type()
)
sensorNegativeHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNegativeHysteresis.setStatus("current")


class _LncThreshold_Type(OctetString):
    """Custom type lncThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_LncThreshold_Type.__name__ = "OctetString"
_LncThreshold_Object = MibTableColumn
lncThreshold = _LncThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 5),
    _LncThreshold_Type()
)
lncThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lncThreshold.setStatus("current")


class _LcThreshold_Type(OctetString):
    """Custom type lcThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_LcThreshold_Type.__name__ = "OctetString"
_LcThreshold_Object = MibTableColumn
lcThreshold = _LcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 6),
    _LcThreshold_Type()
)
lcThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcThreshold.setStatus("current")


class _LnrThreshold_Type(OctetString):
    """Custom type lnrThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_LnrThreshold_Type.__name__ = "OctetString"
_LnrThreshold_Object = MibTableColumn
lnrThreshold = _LnrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 7),
    _LnrThreshold_Type()
)
lnrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lnrThreshold.setStatus("current")


class _UncThreshold_Type(OctetString):
    """Custom type uncThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_UncThreshold_Type.__name__ = "OctetString"
_UncThreshold_Object = MibTableColumn
uncThreshold = _UncThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 8),
    _UncThreshold_Type()
)
uncThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncThreshold.setStatus("current")


class _UcThreshold_Type(OctetString):
    """Custom type ucThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_UcThreshold_Type.__name__ = "OctetString"
_UcThreshold_Object = MibTableColumn
ucThreshold = _UcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 9),
    _UcThreshold_Type()
)
ucThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucThreshold.setStatus("current")


class _UnrThreshold_Type(OctetString):
    """Custom type unrThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_UnrThreshold_Type.__name__ = "OctetString"
_UnrThreshold_Object = MibTableColumn
unrThreshold = _UnrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 10),
    _UnrThreshold_Type()
)
unrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unrThreshold.setStatus("current")
_EventAssertionEnable_Type = Integer32
_EventAssertionEnable_Object = MibTableColumn
eventAssertionEnable = _EventAssertionEnable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 11),
    _EventAssertionEnable_Type()
)
eventAssertionEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAssertionEnable.setStatus("current")
_EventDeassertionEnable_Type = Integer32
_EventDeassertionEnable_Object = MibTableColumn
eventDeassertionEnable = _EventDeassertionEnable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 12),
    _EventDeassertionEnable_Type()
)
eventDeassertionEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDeassertionEnable.setStatus("current")


class _SensorIDString_Type(OctetString):
    """Custom type sensorIDString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SensorIDString_Type.__name__ = "OctetString"
_SensorIDString_Object = MibTableColumn
sensorIDString = _SensorIDString_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1, 13),
    _SensorIDString_Type()
)
sensorIDString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorIDString.setStatus("current")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("poweroff", 0),
          ("poweron", 1))
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibScalar
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 4),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerStatus.setStatus("current")
_Boardinfo_ObjectIdentity = ObjectIdentity
boardinfo = _Boardinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5)
)


class _BmcMajorVesion_Type(Integer32):
    """Custom type bmcMajorVesion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BmcMajorVesion_Type.__name__ = "Integer32"
_BmcMajorVesion_Object = MibScalar
bmcMajorVesion = _BmcMajorVesion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5, 1),
    _BmcMajorVesion_Type()
)
bmcMajorVesion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcMajorVesion.setStatus("current")


class _BmcMinorVesion_Type(Integer32):
    """Custom type bmcMinorVesion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BmcMinorVesion_Type.__name__ = "Integer32"
_BmcMinorVesion_Object = MibScalar
bmcMinorVesion = _BmcMinorVesion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5, 2),
    _BmcMinorVesion_Type()
)
bmcMinorVesion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcMinorVesion.setStatus("current")


class _BmcBuildDate_Type(OctetString):
    """Custom type bmcBuildDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_BmcBuildDate_Type.__name__ = "OctetString"
_BmcBuildDate_Object = MibScalar
bmcBuildDate = _BmcBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5, 3),
    _BmcBuildDate_Type()
)
bmcBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcBuildDate.setStatus("current")


class _BiosVesion_Type(OctetString):
    """Custom type biosVesion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_BiosVesion_Type.__name__ = "OctetString"
_BiosVesion_Object = MibScalar
biosVesion = _BiosVesion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5, 4),
    _BiosVesion_Type()
)
biosVesion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosVesion.setStatus("current")


class _BiosBuildDate_Type(OctetString):
    """Custom type biosBuildDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_BiosBuildDate_Type.__name__ = "OctetString"
_BiosBuildDate_Object = MibScalar
biosBuildDate = _BiosBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5, 5),
    _BiosBuildDate_Type()
)
biosBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosBuildDate.setStatus("current")


class _HostName_Type(OctetString):
    """Custom type hostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_HostName_Type.__name__ = "OctetString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5, 6),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")


class _BmcBuildVesion_Type(Integer32):
    """Custom type bmcBuildVesion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BmcBuildVesion_Type.__name__ = "Integer32"
_BmcBuildVesion_Object = MibScalar
bmcBuildVesion = _BmcBuildVesion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5, 7),
    _BmcBuildVesion_Type()
)
bmcBuildVesion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcBuildVesion.setStatus("current")
_Hardwareinfo_ObjectIdentity = ObjectIdentity
hardwareinfo = _Hardwareinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6)
)


class _SerialNumber_Type(OctetString):
    """Custom type serialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SerialNumber_Type.__name__ = "OctetString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("current")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2, 1)
)
cpuEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "cpuNumber"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("current")


class _CpuNumber_Type(Integer32):
    """Custom type cpuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpuNumber_Type.__name__ = "Integer32"
_CpuNumber_Object = MibTableColumn
cpuNumber = _CpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2, 1, 1),
    _CpuNumber_Type()
)
cpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuNumber.setStatus("current")


class _Processor_Type(OctetString):
    """Custom type processor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_Processor_Type.__name__ = "OctetString"
_Processor_Object = MibTableColumn
processor = _Processor_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2, 1, 2),
    _Processor_Type()
)
processor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processor.setStatus("current")


class _Speed_Type(Integer32):
    """Custom type speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Speed_Type.__name__ = "Integer32"
_Speed_Object = MibTableColumn
speed = _Speed_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2, 1, 3),
    _Speed_Type()
)
speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speed.setStatus("current")


class _Core_Type(Integer32):
    """Custom type core based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Core_Type.__name__ = "Integer32"
_Core_Object = MibTableColumn
core = _Core_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2, 1, 4),
    _Core_Type()
)
core.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    core.setStatus("current")


class _CoreActive_Type(Integer32):
    """Custom type coreActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoreActive_Type.__name__ = "Integer32"
_CoreActive_Object = MibTableColumn
coreActive = _CoreActive_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2, 1, 5),
    _CoreActive_Type()
)
coreActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coreActive.setStatus("current")


class _Manufacturer_Type(OctetString):
    """Custom type manufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_Manufacturer_Type.__name__ = "OctetString"
_Manufacturer_Object = MibTableColumn
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 2, 1, 6),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")
_DimmTable_Object = MibTable
dimmTable = _DimmTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dimmTable.setStatus("current")
_DimmEntry_Object = MibTableRow
dimmEntry = _DimmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1)
)
dimmEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "dimmNumber"),
)
if mibBuilder.loadTexts:
    dimmEntry.setStatus("current")


class _DimmNumber_Type(Integer32):
    """Custom type dimmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DimmNumber_Type.__name__ = "Integer32"
_DimmNumber_Object = MibTableColumn
dimmNumber = _DimmNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 1),
    _DimmNumber_Type()
)
dimmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmNumber.setStatus("current")


class _DimmLocation_Type(OctetString):
    """Custom type dimmLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_DimmLocation_Type.__name__ = "OctetString"
_DimmLocation_Object = MibTableColumn
dimmLocation = _DimmLocation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 2),
    _DimmLocation_Type()
)
dimmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmLocation.setStatus("current")


class _DimmMaxCapSpeed_Type(Integer32):
    """Custom type dimmMaxCapSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DimmMaxCapSpeed_Type.__name__ = "Integer32"
_DimmMaxCapSpeed_Object = MibTableColumn
dimmMaxCapSpeed = _DimmMaxCapSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 3),
    _DimmMaxCapSpeed_Type()
)
dimmMaxCapSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmMaxCapSpeed.setStatus("current")


class _DimmOpSpeed_Type(Integer32):
    """Custom type dimmOpSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DimmOpSpeed_Type.__name__ = "Integer32"
_DimmOpSpeed_Object = MibTableColumn
dimmOpSpeed = _DimmOpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 4),
    _DimmOpSpeed_Type()
)
dimmOpSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmOpSpeed.setStatus("current")


class _DimmSize_Type(Integer32):
    """Custom type dimmSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DimmSize_Type.__name__ = "Integer32"
_DimmSize_Object = MibTableColumn
dimmSize = _DimmSize_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 5),
    _DimmSize_Type()
)
dimmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmSize.setStatus("current")


class _DimmSerialNo_Type(OctetString):
    """Custom type dimmSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_DimmSerialNo_Type.__name__ = "OctetString"
_DimmSerialNo_Object = MibTableColumn
dimmSerialNo = _DimmSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 6),
    _DimmSerialNo_Type()
)
dimmSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmSerialNo.setStatus("current")


class _DimmPartNo_Type(OctetString):
    """Custom type dimmPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_DimmPartNo_Type.__name__ = "OctetString"
_DimmPartNo_Object = MibTableColumn
dimmPartNo = _DimmPartNo_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 7),
    _DimmPartNo_Type()
)
dimmPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmPartNo.setStatus("current")


class _DimmManufacturer_Type(OctetString):
    """Custom type dimmManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_DimmManufacturer_Type.__name__ = "OctetString"
_DimmManufacturer_Object = MibTableColumn
dimmManufacturer = _DimmManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6, 3, 1, 8),
    _DimmManufacturer_Type()
)
dimmManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dimmManufacturer.setStatus("current")
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7)
)
_ControllerTable_Object = MibTable
controllerTable = _ControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1)
)
if mibBuilder.loadTexts:
    controllerTable.setStatus("current")
_ControllerEntry_Object = MibTableRow
controllerEntry = _ControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1)
)
controllerEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "controllerNumber"),
)
if mibBuilder.loadTexts:
    controllerEntry.setStatus("current")


class _ControllerNumber_Type(Integer32):
    """Custom type controllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ControllerNumber_Type.__name__ = "Integer32"
_ControllerNumber_Object = MibTableColumn
controllerNumber = _ControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 1),
    _ControllerNumber_Type()
)
controllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerNumber.setStatus("current")


class _ControllerProductName_Type(OctetString):
    """Custom type controllerProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )
    fixed_length = 96


_ControllerProductName_Type.__name__ = "OctetString"
_ControllerProductName_Object = MibTableColumn
controllerProductName = _ControllerProductName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 2),
    _ControllerProductName_Type()
)
controllerProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerProductName.setStatus("current")


class _Serial_Type(OctetString):
    """Custom type serial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_Serial_Type.__name__ = "OctetString"
_Serial_Object = MibTableColumn
serial = _Serial_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 3),
    _Serial_Type()
)
serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial.setStatus("current")


class _Package_Type(OctetString):
    """Custom type package based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(96, 96),
    )
    fixed_length = 96


_Package_Type.__name__ = "OctetString"
_Package_Object = MibTableColumn
package = _Package_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 4),
    _Package_Type()
)
package.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    package.setStatus("current")


class _FwVersion_Type(OctetString):
    """Custom type fwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_FwVersion_Type.__name__ = "OctetString"
_FwVersion_Object = MibTableColumn
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 5),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")


class _BiosVersion_Type(OctetString):
    """Custom type biosVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_BiosVersion_Type.__name__ = "OctetString"
_BiosVersion_Object = MibTableColumn
biosVersion = _BiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 6),
    _BiosVersion_Type()
)
biosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosVersion.setStatus("current")


class _BootBlockVersion_Type(OctetString):
    """Custom type bootBlockVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_BootBlockVersion_Type.__name__ = "OctetString"
_BootBlockVersion_Object = MibTableColumn
bootBlockVersion = _BootBlockVersion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 7),
    _BootBlockVersion_Type()
)
bootBlockVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootBlockVersion.setStatus("current")


class _BatteryStatus_Type(Integer32):
    """Custom type batteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BatteryStatus_Type.__name__ = "Integer32"
_BatteryStatus_Object = MibTableColumn
batteryStatus = _BatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 8),
    _BatteryStatus_Type()
)
batteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStatus.setStatus("current")


class _PcieLocation_Type(Integer32):
    """Custom type pcieLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PcieLocation_Type.__name__ = "Integer32"
_PcieLocation_Object = MibTableColumn
pcieLocation = _PcieLocation_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 9),
    _PcieLocation_Type()
)
pcieLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcieLocation.setStatus("current")


class _PcieSlot_Type(Integer32):
    """Custom type pcieSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PcieSlot_Type.__name__ = "Integer32"
_PcieSlot_Object = MibTableColumn
pcieSlot = _PcieSlot_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 1, 1, 10),
    _PcieSlot_Type()
)
pcieSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcieSlot.setStatus("current")
_PhyHddTable_Object = MibTable
phyHddTable = _PhyHddTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2)
)
if mibBuilder.loadTexts:
    phyHddTable.setStatus("current")
_HddEntry_Object = MibTableRow
hddEntry = _HddEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1)
)
hddEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "hddNumber"),
)
if mibBuilder.loadTexts:
    hddEntry.setStatus("current")


class _HddNumber_Type(Integer32):
    """Custom type hddNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HddNumber_Type.__name__ = "Integer32"
_HddNumber_Object = MibTableColumn
hddNumber = _HddNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 1),
    _HddNumber_Type()
)
hddNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddNumber.setStatus("current")


class _HddControllerNumber_Type(Integer32):
    """Custom type hddControllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HddControllerNumber_Type.__name__ = "Integer32"
_HddControllerNumber_Object = MibTableColumn
hddControllerNumber = _HddControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 2),
    _HddControllerNumber_Type()
)
hddControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddControllerNumber.setStatus("current")


class _EnclosureNumber_Type(Integer32):
    """Custom type enclosureNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EnclosureNumber_Type.__name__ = "Integer32"
_EnclosureNumber_Object = MibTableColumn
enclosureNumber = _EnclosureNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 3),
    _EnclosureNumber_Type()
)
enclosureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureNumber.setStatus("current")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 4),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _Temperature_Type(Integer32):
    """Custom type temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Temperature_Type.__name__ = "Integer32"
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 5),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")


class _Capacity_Type(Integer32):
    """Custom type capacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Capacity_Type.__name__ = "Integer32"
_Capacity_Object = MibTableColumn
capacity = _Capacity_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 6),
    _Capacity_Type()
)
capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacity.setStatus("current")


class _Vendor_Type(OctetString):
    """Custom type vendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vendor_Type.__name__ = "OctetString"
_Vendor_Object = MibTableColumn
vendor = _Vendor_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 7),
    _Vendor_Type()
)
vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendor.setStatus("current")


class _ModelName_Type(OctetString):
    """Custom type modelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_ModelName_Type.__name__ = "OctetString"
_ModelName_Object = MibTableColumn
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 8),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")


class _Revision_Type(OctetString):
    """Custom type revision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Revision_Type.__name__ = "OctetString"
_Revision_Object = MibTableColumn
revision = _Revision_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 9),
    _Revision_Type()
)
revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revision.setStatus("current")


class _Sn_Type(OctetString):
    """Custom type sn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_Sn_Type.__name__ = "OctetString"
_Sn_Object = MibTableColumn
sn = _Sn_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 10),
    _Sn_Type()
)
sn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sn.setStatus("current")


class _LinkSpeed_Type(Integer32):
    """Custom type linkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LinkSpeed_Type.__name__ = "Integer32"
_LinkSpeed_Object = MibTableColumn
linkSpeed = _LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 11),
    _LinkSpeed_Type()
)
linkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSpeed.setStatus("current")


class _FwState_Type(Integer32):
    """Custom type fwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FwState_Type.__name__ = "Integer32"
_FwState_Object = MibTableColumn
fwState = _FwState_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 12),
    _FwState_Type()
)
fwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwState.setStatus("current")


class _OtherErrCount_Type(Integer32):
    """Custom type otherErrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OtherErrCount_Type.__name__ = "Integer32"
_OtherErrCount_Object = MibTableColumn
otherErrCount = _OtherErrCount_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 13),
    _OtherErrCount_Type()
)
otherErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherErrCount.setStatus("current")


class _PredictedFailCount_Type(Integer32):
    """Custom type predictedFailCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PredictedFailCount_Type.__name__ = "Integer32"
_PredictedFailCount_Object = MibTableColumn
predictedFailCount = _PredictedFailCount_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 14),
    _PredictedFailCount_Type()
)
predictedFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    predictedFailCount.setStatus("current")


class _MediaErrCount_Type(Integer32):
    """Custom type mediaErrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MediaErrCount_Type.__name__ = "Integer32"
_MediaErrCount_Object = MibTableColumn
mediaErrCount = _MediaErrCount_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 2, 1, 15),
    _MediaErrCount_Type()
)
mediaErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaErrCount.setStatus("current")
_LogHddTable_Object = MibTable
logHddTable = _LogHddTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3)
)
if mibBuilder.loadTexts:
    logHddTable.setStatus("current")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1)
)
volumeEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "volNumber"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("current")


class _VolNumber_Type(Integer32):
    """Custom type volNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VolNumber_Type.__name__ = "Integer32"
_VolNumber_Object = MibTableColumn
volNumber = _VolNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 1),
    _VolNumber_Type()
)
volNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volNumber.setStatus("current")


class _VolControllerNumber_Type(Integer32):
    """Custom type volControllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VolControllerNumber_Type.__name__ = "Integer32"
_VolControllerNumber_Object = MibTableColumn
volControllerNumber = _VolControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 2),
    _VolControllerNumber_Type()
)
volControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volControllerNumber.setStatus("current")


class _VolStatus_Type(Integer32):
    """Custom type volStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VolStatus_Type.__name__ = "Integer32"
_VolStatus_Object = MibTableColumn
volStatus = _VolStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 3),
    _VolStatus_Type()
)
volStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volStatus.setStatus("current")


class _VolCapacity_Type(Integer32):
    """Custom type volCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VolCapacity_Type.__name__ = "Integer32"
_VolCapacity_Object = MibTableColumn
volCapacity = _VolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 4),
    _VolCapacity_Type()
)
volCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCapacity.setStatus("current")


class _PriRaidLevel_Type(Integer32):
    """Custom type priRaidLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PriRaidLevel_Type.__name__ = "Integer32"
_PriRaidLevel_Object = MibTableColumn
priRaidLevel = _PriRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 5),
    _PriRaidLevel_Type()
)
priRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priRaidLevel.setStatus("current")


class _RaidLevelQualifier_Type(Integer32):
    """Custom type raidLevelQualifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaidLevelQualifier_Type.__name__ = "Integer32"
_RaidLevelQualifier_Object = MibTableColumn
raidLevelQualifier = _RaidLevelQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 6),
    _RaidLevelQualifier_Type()
)
raidLevelQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidLevelQualifier.setStatus("current")


class _SecRaidLevel_Type(Integer32):
    """Custom type secRaidLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SecRaidLevel_Type.__name__ = "Integer32"
_SecRaidLevel_Object = MibTableColumn
secRaidLevel = _SecRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 7),
    _SecRaidLevel_Type()
)
secRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secRaidLevel.setStatus("current")


class _LdStripSize_Type(Integer32):
    """Custom type ldStripSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LdStripSize_Type.__name__ = "Integer32"
_LdStripSize_Object = MibTableColumn
ldStripSize = _LdStripSize_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 8),
    _LdStripSize_Type()
)
ldStripSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldStripSize.setStatus("current")


class _NumDevices_Type(Integer32):
    """Custom type numDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NumDevices_Type.__name__ = "Integer32"
_NumDevices_Object = MibTableColumn
numDevices = _NumDevices_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 9),
    _NumDevices_Type()
)
numDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDevices.setStatus("current")


class _SpanDepth_Type(Integer32):
    """Custom type spanDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpanDepth_Type.__name__ = "Integer32"
_SpanDepth_Object = MibTableColumn
spanDepth = _SpanDepth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 10),
    _SpanDepth_Type()
)
spanDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanDepth.setStatus("current")


class _State_Type(Integer32):
    """Custom type state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_State_Type.__name__ = "Integer32"
_State_Object = MibTableColumn
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 11),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("current")


class _VolName_Type(OctetString):
    """Custom type volName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_VolName_Type.__name__ = "OctetString"
_VolName_Object = MibTableColumn
volName = _VolName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7, 3, 1, 12),
    _VolName_Type()
)
volName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volName.setStatus("current")


class _ColdResetBMC_Type(Integer32):
    """Custom type coldResetBMC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ColdResetBMC_Type.__name__ = "Integer32"
_ColdResetBMC_Object = MibScalar
coldResetBMC = _ColdResetBMC_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 8),
    _ColdResetBMC_Type()
)
coldResetBMC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coldResetBMC.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 9)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserInfo_Object = MibTableRow
userInfo = _UserInfo_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 9, 1)
)
userInfo.setIndexNames(
    (0, "ATEN-IPMI-MIB", "id"),
)
if mibBuilder.loadTexts:
    userInfo.setStatus("current")


class _Id_Type(Integer32):
    """Custom type id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Id_Type.__name__ = "Integer32"
_Id_Object = MibTableColumn
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 9, 1, 1),
    _Id_Type()
)
id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    id.setStatus("current")


class _Username_Type(OctetString):
    """Custom type username based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Username_Type.__name__ = "OctetString"
_Username_Object = MibTableColumn
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 9, 1, 2),
    _Username_Type()
)
username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    username.setStatus("current")


class _Password_Type(OctetString):
    """Custom type password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_Password_Type.__name__ = "OctetString"
_Password_Object = MibTableColumn
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 9, 1, 3),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("current")


class _Privilege_Type(Integer32):
    """Custom type privilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_Privilege_Type.__name__ = "Integer32"
_Privilege_Object = MibTableColumn
privilege = _Privilege_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 9, 1, 4),
    _Privilege_Type()
)
privilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privilege.setStatus("current")


class _Uid_Type(Integer32):
    """Custom type uid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Uid_Type.__name__ = "Integer32"
_Uid_Object = MibScalar
uid = _Uid_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 10),
    _Uid_Type()
)
uid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uid.setStatus("current")
_AlertTable_Object = MibTable
alertTable = _AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 11)
)
if mibBuilder.loadTexts:
    alertTable.setStatus("current")
_AlertInfo_Object = MibTableRow
alertInfo = _AlertInfo_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 11, 1)
)
alertInfo.setIndexNames(
    (0, "ATEN-IPMI-MIB", "id"),
)
if mibBuilder.loadTexts:
    alertInfo.setStatus("current")


class _AlertNo_Type(Integer32):
    """Custom type alertNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlertNo_Type.__name__ = "Integer32"
_AlertNo_Object = MibTableColumn
alertNo = _AlertNo_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 11, 1, 1),
    _AlertNo_Type()
)
alertNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertNo.setStatus("current")


class _AlertLevel_Type(OctetString):
    """Custom type alertLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )
    fixed_length = 25


_AlertLevel_Type.__name__ = "OctetString"
_AlertLevel_Object = MibTableColumn
alertLevel = _AlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 11, 1, 2),
    _AlertLevel_Type()
)
alertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertLevel.setStatus("current")


class _DestinationAddress_Type(OctetString):
    """Custom type destinationAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(270, 270),
    )
    fixed_length = 270


_DestinationAddress_Type.__name__ = "OctetString"
_DestinationAddress_Object = MibTableColumn
destinationAddress = _DestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 11, 1, 3),
    _DestinationAddress_Type()
)
destinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destinationAddress.setStatus("current")
_Powerinfo_ObjectIdentity = ObjectIdentity
powerinfo = _Powerinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14)
)


class _PsuNumber_Type(Integer32):
    """Custom type psuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PsuNumber_Type.__name__ = "Integer32"
_PsuNumber_Object = MibScalar
psuNumber = _PsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 1),
    _PsuNumber_Type()
)
psuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuNumber.setStatus("current")
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("current")
_PsuEntry_Object = MibTableRow
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1)
)
psuEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "psuIndex"),
)
if mibBuilder.loadTexts:
    psuEntry.setStatus("current")


class _PsuIndex_Type(Integer32):
    """Custom type psuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PsuIndex_Type.__name__ = "Integer32"
_PsuIndex_Object = MibTableColumn
psuIndex = _PsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 1),
    _PsuIndex_Type()
)
psuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuIndex.setStatus("current")


class _PsuStatus_Type(Integer32):
    """Custom type psuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("good", 1))
    )


_PsuStatus_Type.__name__ = "Integer32"
_PsuStatus_Object = MibTableColumn
psuStatus = _PsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 2),
    _PsuStatus_Type()
)
psuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuStatus.setStatus("current")


class _InputVoltage_Type(OctetString):
    """Custom type inputVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_InputVoltage_Type.__name__ = "OctetString"
_InputVoltage_Object = MibTableColumn
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 3),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("current")


class _InputCurrent_Type(OctetString):
    """Custom type inputCurrent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_InputCurrent_Type.__name__ = "OctetString"
_InputCurrent_Object = MibTableColumn
inputCurrent = _InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 4),
    _InputCurrent_Type()
)
inputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrent.setStatus("current")


class _InputPower_Type(Integer32):
    """Custom type inputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048576),
    )


_InputPower_Type.__name__ = "Integer32"
_InputPower_Object = MibTableColumn
inputPower = _InputPower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 5),
    _InputPower_Type()
)
inputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPower.setStatus("current")


class _OutputVoltage_Type(OctetString):
    """Custom type outputVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_OutputVoltage_Type.__name__ = "OctetString"
_OutputVoltage_Object = MibTableColumn
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 6),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("current")


class _OutputCurrent_Type(OctetString):
    """Custom type outputCurrent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_OutputCurrent_Type.__name__ = "OctetString"
_OutputCurrent_Object = MibTableColumn
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 7),
    _OutputCurrent_Type()
)
outputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrent.setStatus("current")


class _OutputPower_Type(Integer32):
    """Custom type outputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048576),
    )


_OutputPower_Type.__name__ = "Integer32"
_OutputPower_Object = MibTableColumn
outputPower = _OutputPower_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 8),
    _OutputPower_Type()
)
outputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPower.setStatus("current")


class _Temperature1_Type(Integer32):
    """Custom type temperature1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Temperature1_Type.__name__ = "Integer32"
_Temperature1_Object = MibTableColumn
temperature1 = _Temperature1_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 9),
    _Temperature1_Type()
)
temperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature1.setStatus("current")


class _Temperature2_Type(Integer32):
    """Custom type temperature2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Temperature2_Type.__name__ = "Integer32"
_Temperature2_Object = MibTableColumn
temperature2 = _Temperature2_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 10),
    _Temperature2_Type()
)
temperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature2.setStatus("current")


class _FanRPM1_Type(Integer32):
    """Custom type fanRPM1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanRPM1_Type.__name__ = "Integer32"
_FanRPM1_Object = MibTableColumn
fanRPM1 = _FanRPM1_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 11),
    _FanRPM1_Type()
)
fanRPM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRPM1.setStatus("current")


class _FanRPM2_Type(Integer32):
    """Custom type fanRPM2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanRPM2_Type.__name__ = "Integer32"
_FanRPM2_Object = MibTableColumn
fanRPM2 = _FanRPM2_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 12),
    _FanRPM2_Type()
)
fanRPM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRPM2.setStatus("current")


class _PsuSerialNumber_Type(OctetString):
    """Custom type psuSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_PsuSerialNumber_Type.__name__ = "OctetString"
_PsuSerialNumber_Object = MibTableColumn
psuSerialNumber = _PsuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 14, 2, 1, 13),
    _PsuSerialNumber_Type()
)
psuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuSerialNumber.setStatus("current")


class _FanMode_Type(Integer32):
    """Custom type fanMode based on Integer32"""
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
        *(("standard", 0),
          ("fullspeed", 1),
          ("optimal", 2),
          ("pue2optimal", 3),
          ("heavyIO", 4))
    )


_FanMode_Type.__name__ = "Integer32"
_FanMode_Object = MibScalar
fanMode = _FanMode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 15),
    _FanMode_Type()
)
fanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanMode.setStatus("current")
_Fruinfo_ObjectIdentity = ObjectIdentity
fruinfo = _Fruinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 1)
)
_ChassisType_Type = Integer32
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 1, 1),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("current")


class _ChassisPartNumber_Type(OctetString):
    """Custom type chassisPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_ChassisPartNumber_Type.__name__ = "OctetString"
_ChassisPartNumber_Object = MibScalar
chassisPartNumber = _ChassisPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 1, 2),
    _ChassisPartNumber_Type()
)
chassisPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPartNumber.setStatus("current")


class _ChassisSerialNumber_Type(OctetString):
    """Custom type chassisSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_ChassisSerialNumber_Type.__name__ = "OctetString"
_ChassisSerialNumber_Object = MibScalar
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 1, 3),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("current")
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 2)
)


class _BoardLanguage_Type(Integer32):
    """Custom type boardLanguage based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136)
        )
    )
    namedValues = NamedValues(
        *(("afar", 1),
          ("abkhazian", 2),
          ("afrikaans", 3),
          ("amharic", 4),
          ("arabic", 5),
          ("assamese", 6),
          ("aymara", 7),
          ("azerbaijani", 8),
          ("bashkir", 9),
          ("byelorussian", 10),
          ("bulgarian", 11),
          ("bihari", 12),
          ("bislama", 13),
          ("bengali", 14),
          ("tibetan", 15),
          ("breton", 16),
          ("catalan", 17),
          ("corsican", 18),
          ("czech", 19),
          ("welsh", 20),
          ("danish", 21),
          ("german", 22),
          ("bhutani", 23),
          ("greek", 24),
          ("english", 25),
          ("esperanto", 26),
          ("spanish", 27),
          ("estonian", 28),
          ("basque", 29),
          ("persian", 30),
          ("finnish", 31),
          ("fiji", 32),
          ("faeroese", 33),
          ("french", 34),
          ("frisian", 35),
          ("irish", 36),
          ("gaelic", 37),
          ("galician", 38),
          ("guarani", 39),
          ("gujarati", 40),
          ("hausa", 41),
          ("hindi", 42),
          ("croatian", 43),
          ("hungarian", 44),
          ("armenian", 45),
          ("interlingua", 46),
          ("interlingue", 47),
          ("inupiak", 48),
          ("indonesian", 49),
          ("icelandic", 50),
          ("italian", 51),
          ("hebrew", 52),
          ("japanese", 53),
          ("yiddish", 54),
          ("javanese", 55),
          ("georgian", 56),
          ("kazakh", 57),
          ("greenlandic", 58),
          ("cambodian", 59),
          ("kannada", 60),
          ("korean", 61),
          ("kashmiri", 62),
          ("kurdish", 63),
          ("kirghiz", 64),
          ("latin", 65),
          ("lingala", 66),
          ("laothian", 67),
          ("lithuanian", 68),
          ("lettish", 69),
          ("malagasy", 70),
          ("maori", 71),
          ("macedonian", 72),
          ("malayalam", 73),
          ("mongolian", 74),
          ("moldavian", 75),
          ("marathi", 76),
          ("malay", 77),
          ("maltese", 78),
          ("burmese", 79),
          ("nauru", 80),
          ("nepali", 81),
          ("dutch", 82),
          ("norwegian", 83),
          ("occitan", 84),
          ("oromo", 85),
          ("oriya", 86),
          ("punjabi", 87),
          ("polish", 88),
          ("pushto", 89),
          ("portuguese", 90),
          ("quechua", 91),
          ("rhaeto-romance", 92),
          ("kirundi", 93),
          ("romanian", 94),
          ("russian", 95),
          ("kinyarwanda", 96),
          ("sanskrit", 97),
          ("sindhi", 98),
          ("sangro", 99),
          ("serbo-croatian", 100),
          ("singhalese", 101),
          ("slovak", 102),
          ("slovenian", 103),
          ("samoan", 104),
          ("shona", 105),
          ("somali", 106),
          ("albanian", 107),
          ("serbian", 108),
          ("siswati", 109),
          ("sesotho", 110),
          ("sudanese", 111),
          ("swedish", 112),
          ("swahili", 113),
          ("tamil", 114),
          ("tegulu", 115),
          ("tajik", 116),
          ("thai", 117),
          ("tigrinya", 118),
          ("turkmen", 119),
          ("tagalog", 120),
          ("setswana", 121),
          ("tonga", 122),
          ("turkish", 123),
          ("tsonga", 124),
          ("tatar", 125),
          ("twi", 126),
          ("ukrainian", 127),
          ("urdu", 128),
          ("uzbek", 129),
          ("vietnamese", 130),
          ("volapuk", 131),
          ("wolof", 132),
          ("xhosa", 133),
          ("yoruba", 134),
          ("chinese", 135),
          ("zulu", 136))
    )


_BoardLanguage_Type.__name__ = "Integer32"
_BoardLanguage_Object = MibScalar
boardLanguage = _BoardLanguage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 2, 1),
    _BoardLanguage_Type()
)
boardLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardLanguage.setStatus("current")


class _BoardManufacturer_Type(OctetString):
    """Custom type boardManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_BoardManufacturer_Type.__name__ = "OctetString"
_BoardManufacturer_Object = MibScalar
boardManufacturer = _BoardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 2, 2),
    _BoardManufacturer_Type()
)
boardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardManufacturer.setStatus("current")


class _BoardProductName_Type(OctetString):
    """Custom type boardProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_BoardProductName_Type.__name__ = "OctetString"
_BoardProductName_Object = MibScalar
boardProductName = _BoardProductName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 2, 3),
    _BoardProductName_Type()
)
boardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardProductName.setStatus("current")


class _BoardSerialNumber_Type(OctetString):
    """Custom type boardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_BoardSerialNumber_Type.__name__ = "OctetString"
_BoardSerialNumber_Object = MibScalar
boardSerialNumber = _BoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 2, 4),
    _BoardSerialNumber_Type()
)
boardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSerialNumber.setStatus("current")


class _BoardPartNumber_Type(OctetString):
    """Custom type boardPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_BoardPartNumber_Type.__name__ = "OctetString"
_BoardPartNumber_Object = MibScalar
boardPartNumber = _BoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 2, 5),
    _BoardPartNumber_Type()
)
boardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPartNumber.setStatus("current")
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3)
)


class _ProductLanguage_Type(Integer32):
    """Custom type productLanguage based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136)
        )
    )
    namedValues = NamedValues(
        *(("afar", 1),
          ("abkhazian", 2),
          ("afrikaans", 3),
          ("amharic", 4),
          ("arabic", 5),
          ("assamese", 6),
          ("aymara", 7),
          ("azerbaijani", 8),
          ("bashkir", 9),
          ("byelorussian", 10),
          ("bulgarian", 11),
          ("bihari", 12),
          ("bislama", 13),
          ("bengali", 14),
          ("tibetan", 15),
          ("breton", 16),
          ("catalan", 17),
          ("corsican", 18),
          ("czech", 19),
          ("welsh", 20),
          ("danish", 21),
          ("german", 22),
          ("bhutani", 23),
          ("greek", 24),
          ("english", 25),
          ("esperanto", 26),
          ("spanish", 27),
          ("estonian", 28),
          ("basque", 29),
          ("persian", 30),
          ("finnish", 31),
          ("fiji", 32),
          ("faeroese", 33),
          ("french", 34),
          ("frisian", 35),
          ("irish", 36),
          ("gaelic", 37),
          ("galician", 38),
          ("guarani", 39),
          ("gujarati", 40),
          ("hausa", 41),
          ("hindi", 42),
          ("croatian", 43),
          ("hungarian", 44),
          ("armenian", 45),
          ("interlingua", 46),
          ("interlingue", 47),
          ("inupiak", 48),
          ("indonesian", 49),
          ("icelandic", 50),
          ("italian", 51),
          ("hebrew", 52),
          ("japanese", 53),
          ("yiddish", 54),
          ("javanese", 55),
          ("georgian", 56),
          ("kazakh", 57),
          ("greenlandic", 58),
          ("cambodian", 59),
          ("kannada", 60),
          ("korean", 61),
          ("kashmiri", 62),
          ("kurdish", 63),
          ("kirghiz", 64),
          ("latin", 65),
          ("lingala", 66),
          ("laothian", 67),
          ("lithuanian", 68),
          ("lettish", 69),
          ("malagasy", 70),
          ("maori", 71),
          ("macedonian", 72),
          ("malayalam", 73),
          ("mongolian", 74),
          ("moldavian", 75),
          ("marathi", 76),
          ("malay", 77),
          ("maltese", 78),
          ("burmese", 79),
          ("nauru", 80),
          ("nepali", 81),
          ("dutch", 82),
          ("norwegian", 83),
          ("occitan", 84),
          ("oromo", 85),
          ("oriya", 86),
          ("punjabi", 87),
          ("polish", 88),
          ("pushto", 89),
          ("portuguese", 90),
          ("quechua", 91),
          ("rhaeto-romance", 92),
          ("kirundi", 93),
          ("romanian", 94),
          ("russian", 95),
          ("kinyarwanda", 96),
          ("sanskrit", 97),
          ("sindhi", 98),
          ("sangro", 99),
          ("serbo-croatian", 100),
          ("singhalese", 101),
          ("slovak", 102),
          ("slovenian", 103),
          ("samoan", 104),
          ("shona", 105),
          ("somali", 106),
          ("albanian", 107),
          ("serbian", 108),
          ("siswati", 109),
          ("sesotho", 110),
          ("sudanese", 111),
          ("swedish", 112),
          ("swahili", 113),
          ("tamil", 114),
          ("tegulu", 115),
          ("tajik", 116),
          ("thai", 117),
          ("tigrinya", 118),
          ("turkmen", 119),
          ("tagalog", 120),
          ("setswana", 121),
          ("tonga", 122),
          ("turkish", 123),
          ("tsonga", 124),
          ("tatar", 125),
          ("twi", 126),
          ("ukrainian", 127),
          ("urdu", 128),
          ("uzbek", 129),
          ("vietnamese", 130),
          ("volapuk", 131),
          ("wolof", 132),
          ("xhosa", 133),
          ("yoruba", 134),
          ("chinese", 135),
          ("zulu", 136))
    )


_ProductLanguage_Type.__name__ = "Integer32"
_ProductLanguage_Object = MibScalar
productLanguage = _ProductLanguage_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3, 1),
    _ProductLanguage_Type()
)
productLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productLanguage.setStatus("current")


class _ProductManufacturer_Type(OctetString):
    """Custom type productManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_ProductManufacturer_Type.__name__ = "OctetString"
_ProductManufacturer_Object = MibScalar
productManufacturer = _ProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3, 2),
    _ProductManufacturer_Type()
)
productManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productManufacturer.setStatus("current")


class _ProductName_Type(OctetString):
    """Custom type productName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_ProductName_Type.__name__ = "OctetString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")


class _ProductPartNumber_Type(OctetString):
    """Custom type productPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_ProductPartNumber_Type.__name__ = "OctetString"
_ProductPartNumber_Object = MibScalar
productPartNumber = _ProductPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3, 4),
    _ProductPartNumber_Type()
)
productPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productPartNumber.setStatus("current")
_ProductVersion_Type = Integer32
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3, 5),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")


class _ProductSerialNumber_Type(OctetString):
    """Custom type productSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_ProductSerialNumber_Type.__name__ = "OctetString"
_ProductSerialNumber_Object = MibScalar
productSerialNumber = _ProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3, 6),
    _ProductSerialNumber_Type()
)
productSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSerialNumber.setStatus("current")


class _ProductAssetTag_Type(OctetString):
    """Custom type productAssetTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_ProductAssetTag_Type.__name__ = "OctetString"
_ProductAssetTag_Object = MibScalar
productAssetTag = _ProductAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 16, 3, 7),
    _ProductAssetTag_Type()
)
productAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productAssetTag.setStatus("current")
_Ntpinfo_ObjectIdentity = ObjectIdentity
ntpinfo = _Ntpinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 17)
)


class _TimeZone_Type(OctetString):
    """Custom type timeZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_TimeZone_Type.__name__ = "OctetString"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 17, 1),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _NtpEnable_Type(Integer32):
    """Custom type ntpEnable based on Integer32"""
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


_NtpEnable_Type.__name__ = "Integer32"
_NtpEnable_Object = MibScalar
ntpEnable = _NtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 17, 2),
    _NtpEnable_Type()
)
ntpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpEnable.setStatus("current")


class _PrimaryNTPServer_Type(OctetString):
    """Custom type primaryNTPServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )
    fixed_length = 127


_PrimaryNTPServer_Type.__name__ = "OctetString"
_PrimaryNTPServer_Object = MibScalar
primaryNTPServer = _PrimaryNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 17, 3),
    _PrimaryNTPServer_Type()
)
primaryNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryNTPServer.setStatus("current")


class _SecondaryNTPServer_Type(OctetString):
    """Custom type secondaryNTPServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )
    fixed_length = 127


_SecondaryNTPServer_Type.__name__ = "OctetString"
_SecondaryNTPServer_Object = MibScalar
secondaryNTPServer = _SecondaryNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 17, 4),
    _SecondaryNTPServer_Type()
)
secondaryNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryNTPServer.setStatus("current")


class _Dst_Type(Integer32):
    """Custom type dst based on Integer32"""
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


_Dst_Type.__name__ = "Integer32"
_Dst_Object = MibScalar
dst = _Dst_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 17, 5),
    _Dst_Type()
)
dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dst.setStatus("current")
_SelTable_Object = MibTable
selTable = _SelTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18)
)
if mibBuilder.loadTexts:
    selTable.setStatus("current")
_SelEntry_Object = MibTableRow
selEntry = _SelEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18, 1)
)
selEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "selEid"),
)
if mibBuilder.loadTexts:
    selEntry.setStatus("current")


class _SelEid_Type(Integer32):
    """Custom type selEid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SelEid_Type.__name__ = "Integer32"
_SelEid_Object = MibTableColumn
selEid = _SelEid_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18, 1, 1),
    _SelEid_Type()
)
selEid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selEid.setStatus("current")
_SelTimeStamp_Type = DateAndTime
_SelTimeStamp_Object = MibTableColumn
selTimeStamp = _SelTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18, 1, 2),
    _SelTimeStamp_Type()
)
selTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selTimeStamp.setStatus("current")


class _SelSensorName_Type(OctetString):
    """Custom type selSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SelSensorName_Type.__name__ = "OctetString"
_SelSensorName_Object = MibTableColumn
selSensorName = _SelSensorName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18, 1, 3),
    _SelSensorName_Type()
)
selSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selSensorName.setStatus("current")


class _SelSensorType_Type(OctetString):
    """Custom type selSensorType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SelSensorType_Type.__name__ = "OctetString"
_SelSensorType_Object = MibTableColumn
selSensorType = _SelSensorType_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18, 1, 4),
    _SelSensorType_Type()
)
selSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selSensorType.setStatus("current")


class _SelDescription_Type(OctetString):
    """Custom type selDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_SelDescription_Type.__name__ = "OctetString"
_SelDescription_Object = MibTableColumn
selDescription = _SelDescription_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18, 1, 5),
    _SelDescription_Type()
)
selDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selDescription.setStatus("current")


class _SelRawData_Type(OctetString):
    """Custom type selRawData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SelRawData_Type.__name__ = "OctetString"
_SelRawData_Object = MibTableColumn
selRawData = _SelRawData_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 18, 1, 6),
    _SelRawData_Type()
)
selRawData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selRawData.setStatus("current")
_Nvme_ObjectIdentity = ObjectIdentity
nvme = _Nvme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19)
)
_NvmeCtrlTbl_Object = MibTable
nvmeCtrlTbl = _NvmeCtrlTbl_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1)
)
if mibBuilder.loadTexts:
    nvmeCtrlTbl.setStatus("current")
_NvmeCtrlEntry_Object = MibTableRow
nvmeCtrlEntry = _NvmeCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1, 1)
)
nvmeCtrlEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "nvmeCtrlPresent"),
)
if mibBuilder.loadTexts:
    nvmeCtrlEntry.setStatus("current")


class _NvmeCtrlPresent_Type(Integer32):
    """Custom type nvmeCtrlPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_NvmeCtrlPresent_Type.__name__ = "Integer32"
_NvmeCtrlPresent_Object = MibTableColumn
nvmeCtrlPresent = _NvmeCtrlPresent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1, 1, 1),
    _NvmeCtrlPresent_Type()
)
nvmeCtrlPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmeCtrlPresent.setStatus("current")


class _MaxTemp_Type(Integer32):
    """Custom type maxTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MaxTemp_Type.__name__ = "Integer32"
_MaxTemp_Object = MibTableColumn
maxTemp = _MaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1, 1, 2),
    _MaxTemp_Type()
)
maxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTemp.setStatus("current")


class _MaxSlotNum_Type(Integer32):
    """Custom type maxSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MaxSlotNum_Type.__name__ = "Integer32"
_MaxSlotNum_Object = MibTableColumn
maxSlotNum = _MaxSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1, 1, 3),
    _MaxSlotNum_Type()
)
maxSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSlotNum.setStatus("current")


class _Onboard_Type(Integer32):
    """Custom type onboard based on Integer32"""
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


_Onboard_Type.__name__ = "Integer32"
_Onboard_Object = MibTableColumn
onboard = _Onboard_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1, 1, 4),
    _Onboard_Type()
)
onboard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onboard.setStatus("current")


class _DriverIndex_Type(Integer32):
    """Custom type driverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DriverIndex_Type.__name__ = "Integer32"
_DriverIndex_Object = MibTableColumn
driverIndex = _DriverIndex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1, 1, 5),
    _DriverIndex_Type()
)
driverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverIndex.setStatus("current")


class _CpldVer_Type(OctetString):
    """Custom type cpldVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CpldVer_Type.__name__ = "OctetString"
_CpldVer_Object = MibTableColumn
cpldVer = _CpldVer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 1, 1, 6),
    _CpldVer_Type()
)
cpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpldVer.setStatus("current")
_NvmeDriveTbl_Object = MibTable
nvmeDriveTbl = _NvmeDriveTbl_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2)
)
if mibBuilder.loadTexts:
    nvmeDriveTbl.setStatus("current")
_NvmeDriveEntry_Object = MibTableRow
nvmeDriveEntry = _NvmeDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1)
)
nvmeDriveEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "slotId"),
)
if mibBuilder.loadTexts:
    nvmeDriveEntry.setStatus("current")


class _SlotId_Type(Integer32):
    """Custom type slotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SlotId_Type.__name__ = "Integer32"
_SlotId_Object = MibTableColumn
slotId = _SlotId_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 1),
    _SlotId_Type()
)
slotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotId.setStatus("current")


class _GroupId_Type(Integer32):
    """Custom type groupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GroupId_Type.__name__ = "Integer32"
_GroupId_Object = MibTableColumn
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 2),
    _GroupId_Type()
)
groupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupId.setStatus("current")


class _NvmeDrivePresent_Type(Integer32):
    """Custom type nvmeDrivePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_NvmeDrivePresent_Type.__name__ = "Integer32"
_NvmeDrivePresent_Object = MibTableColumn
nvmeDrivePresent = _NvmeDrivePresent_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 3),
    _NvmeDrivePresent_Type()
)
nvmeDrivePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmeDrivePresent.setStatus("current")


class _Locate_Type(Integer32):
    """Custom type locate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dislocate", 0),
          ("locate", 1))
    )


_Locate_Type.__name__ = "Integer32"
_Locate_Object = MibTableColumn
locate = _Locate_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 4),
    _Locate_Type()
)
locate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locate.setStatus("current")


class _Save2Remove_Type(Integer32):
    """Custom type save2Remove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 0),
          ("ready", 1))
    )


_Save2Remove_Type.__name__ = "Integer32"
_Save2Remove_Object = MibTableColumn
save2Remove = _Save2Remove_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 5),
    _Save2Remove_Type()
)
save2Remove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    save2Remove.setStatus("current")


class _VmdMode_Type(Integer32):
    """Custom type vmdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vmd-off", 0),
          ("vmd-on", 1))
    )


_VmdMode_Type.__name__ = "Integer32"
_VmdMode_Object = MibTableColumn
vmdMode = _VmdMode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 6),
    _VmdMode_Type()
)
vmdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmdMode.setStatus("current")


class _Temp_Type(Integer32):
    """Custom type temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Temp_Type.__name__ = "Integer32"
_Temp_Object = MibTableColumn
temp = _Temp_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 7),
    _Temp_Type()
)
temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp.setStatus("current")


class _ClassCode_Type(OctetString):
    """Custom type classCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ClassCode_Type.__name__ = "OctetString"
_ClassCode_Object = MibTableColumn
classCode = _ClassCode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 8),
    _ClassCode_Type()
)
classCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classCode.setStatus("current")


class _VendorID_Type(OctetString):
    """Custom type vendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_VendorID_Type.__name__ = "OctetString"
_VendorID_Object = MibTableColumn
vendorID = _VendorID_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 9),
    _VendorID_Type()
)
vendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorID.setStatus("current")


class _SerialNum_Type(OctetString):
    """Custom type serialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SerialNum_Type.__name__ = "OctetString"
_SerialNum_Object = MibTableColumn
serialNum = _SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 10),
    _SerialNum_Type()
)
serialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNum.setStatus("current")


class _ModelNum_Type(OctetString):
    """Custom type modelNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_ModelNum_Type.__name__ = "OctetString"
_ModelNum_Object = MibTableColumn
modelNum = _ModelNum_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 11),
    _ModelNum_Type()
)
modelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelNum.setStatus("current")


class _Port0MaxLinkSpd_Type(OctetString):
    """Custom type port0MaxLinkSpd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Port0MaxLinkSpd_Type.__name__ = "OctetString"
_Port0MaxLinkSpd_Object = MibTableColumn
port0MaxLinkSpd = _Port0MaxLinkSpd_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 12),
    _Port0MaxLinkSpd_Type()
)
port0MaxLinkSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port0MaxLinkSpd.setStatus("current")


class _Port0MaxLinkWidth_Type(OctetString):
    """Custom type port0MaxLinkWidth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Port0MaxLinkWidth_Type.__name__ = "OctetString"
_Port0MaxLinkWidth_Object = MibTableColumn
port0MaxLinkWidth = _Port0MaxLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 13),
    _Port0MaxLinkWidth_Type()
)
port0MaxLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port0MaxLinkWidth.setStatus("current")


class _Port1MaxLinkSpd_Type(OctetString):
    """Custom type port1MaxLinkSpd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Port1MaxLinkSpd_Type.__name__ = "OctetString"
_Port1MaxLinkSpd_Object = MibTableColumn
port1MaxLinkSpd = _Port1MaxLinkSpd_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 14),
    _Port1MaxLinkSpd_Type()
)
port1MaxLinkSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port1MaxLinkSpd.setStatus("current")


class _Port1MaxLinkWidth_Type(OctetString):
    """Custom type port1MaxLinkWidth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Port1MaxLinkWidth_Type.__name__ = "OctetString"
_Port1MaxLinkWidth_Object = MibTableColumn
port1MaxLinkWidth = _Port1MaxLinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 15),
    _Port1MaxLinkWidth_Type()
)
port1MaxLinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port1MaxLinkWidth.setStatus("current")


class _InitPowerRequirement_Type(Integer32):
    """Custom type initPowerRequirement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InitPowerRequirement_Type.__name__ = "Integer32"
_InitPowerRequirement_Object = MibTableColumn
initPowerRequirement = _InitPowerRequirement_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 16),
    _InitPowerRequirement_Type()
)
initPowerRequirement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initPowerRequirement.setStatus("current")


class _MaxPowerRequirement_Type(Integer32):
    """Custom type maxPowerRequirement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaxPowerRequirement_Type.__name__ = "Integer32"
_MaxPowerRequirement_Object = MibTableColumn
maxPowerRequirement = _MaxPowerRequirement_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 19, 2, 1, 17),
    _MaxPowerRequirement_Type()
)
maxPowerRequirement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPowerRequirement.setStatus("current")
_NicTable_Object = MibTable
nicTable = _NicTable_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20)
)
if mibBuilder.loadTexts:
    nicTable.setStatus("current")
_NicEntry_Object = MibTableRow
nicEntry = _NicEntry_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1)
)
nicEntry.setIndexNames(
    (0, "ATEN-IPMI-MIB", "nicNumber"),
)
if mibBuilder.loadTexts:
    nicEntry.setStatus("current")


class _NicNumber_Type(Integer32):
    """Custom type nicNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NicNumber_Type.__name__ = "Integer32"
_NicNumber_Object = MibTableColumn
nicNumber = _NicNumber_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 1),
    _NicNumber_Type()
)
nicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicNumber.setStatus("current")


class _NicName_Type(OctetString):
    """Custom type nicName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_NicName_Type.__name__ = "OctetString"
_NicName_Object = MibTableColumn
nicName = _NicName_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 2),
    _NicName_Type()
)
nicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicName.setStatus("current")


class _NicMac_Type(OctetString):
    """Custom type nicMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_NicMac_Type.__name__ = "OctetString"
_NicMac_Object = MibTableColumn
nicMac = _NicMac_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 3),
    _NicMac_Type()
)
nicMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicMac.setStatus("current")
_NicIpv4Addr_Type = IpAddress
_NicIpv4Addr_Object = MibTableColumn
nicIpv4Addr = _NicIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 4),
    _NicIpv4Addr_Type()
)
nicIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicIpv4Addr.setStatus("current")


class _NicIpv6Addr_Type(OctetString):
    """Custom type nicIpv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(45, 45),
    )
    fixed_length = 45


_NicIpv6Addr_Type.__name__ = "OctetString"
_NicIpv6Addr_Object = MibTableColumn
nicIpv6Addr = _NicIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 5),
    _NicIpv6Addr_Type()
)
nicIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicIpv6Addr.setStatus("current")


class _NicGateway_Type(OctetString):
    """Custom type nicGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(45, 45),
    )
    fixed_length = 45


_NicGateway_Type.__name__ = "OctetString"
_NicGateway_Object = MibTableColumn
nicGateway = _NicGateway_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 6),
    _NicGateway_Type()
)
nicGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicGateway.setStatus("current")


class _NicNetmask_Type(OctetString):
    """Custom type nicNetmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(45, 45),
    )
    fixed_length = 45


_NicNetmask_Type.__name__ = "OctetString"
_NicNetmask_Object = MibTableColumn
nicNetmask = _NicNetmask_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 7),
    _NicNetmask_Type()
)
nicNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicNetmask.setStatus("current")


class _NicFqdn_Type(OctetString):
    """Custom type nicFqdn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_NicFqdn_Type.__name__ = "OctetString"
_NicFqdn_Object = MibTableColumn
nicFqdn = _NicFqdn_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 8),
    _NicFqdn_Type()
)
nicFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicFqdn.setStatus("current")


class _NicDns_Type(OctetString):
    """Custom type nicDns based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(91, 91),
    )
    fixed_length = 91


_NicDns_Type.__name__ = "OctetString"
_NicDns_Object = MibTableColumn
nicDns = _NicDns_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 9),
    _NicDns_Type()
)
nicDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDns.setStatus("current")


class _NicSpeed_Type(Integer32):
    """Custom type nicSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NicSpeed_Type.__name__ = "Integer32"
_NicSpeed_Object = MibTableColumn
nicSpeed = _NicSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 10),
    _NicSpeed_Type()
)
nicSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicSpeed.setStatus("current")


class _NicDescript_Type(OctetString):
    """Custom type nicDescript based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_NicDescript_Type.__name__ = "OctetString"
_NicDescript_Object = MibTableColumn
nicDescript = _NicDescript_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 11),
    _NicDescript_Type()
)
nicDescript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicDescript.setStatus("current")


class _NicStatus_Type(OctetString):
    """Custom type nicStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NicStatus_Type.__name__ = "OctetString"
_NicStatus_Object = MibTableColumn
nicStatus = _NicStatus_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 20, 1, 12),
    _NicStatus_Type()
)
nicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicStatus.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21)
)
_Ipv4DNSServer_Type = IpAddress
_Ipv4DNSServer_Object = MibScalar
ipv4DNSServer = _Ipv4DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 1),
    _Ipv4DNSServer_Type()
)
ipv4DNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4DNSServer.setStatus("current")
_Ipv4Gateway_Type = IpAddress
_Ipv4Gateway_Object = MibScalar
ipv4Gateway = _Ipv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 2),
    _Ipv4Gateway_Type()
)
ipv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4Gateway.setStatus("current")


class _Ipv6DNSServer_Type(OctetString):
    """Custom type ipv6DNSServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(45, 45),
    )
    fixed_length = 45


_Ipv6DNSServer_Type.__name__ = "OctetString"
_Ipv6DNSServer_Object = MibScalar
ipv6DNSServer = _Ipv6DNSServer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 3),
    _Ipv6DNSServer_Type()
)
ipv6DNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DNSServer.setStatus("current")


class _Ipv6DUID_Type(OctetString):
    """Custom type ipv6DUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_Ipv6DUID_Type.__name__ = "OctetString"
_Ipv6DUID_Object = MibScalar
ipv6DUID = _Ipv6DUID_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 4),
    _Ipv6DUID_Type()
)
ipv6DUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DUID.setStatus("current")


class _Dhcpv6State_Type(Integer32):
    """Custom type dhcpv6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stateless", 0),
          ("stateful", 1))
    )


_Dhcpv6State_Type.__name__ = "Integer32"
_Dhcpv6State_Object = MibScalar
dhcpv6State = _Dhcpv6State_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 5),
    _Dhcpv6State_Type()
)
dhcpv6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6State.setStatus("current")


class _Hostname_Type(OctetString):
    """Custom type hostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_Hostname_Type.__name__ = "OctetString"
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 6),
    _Hostname_Type()
)
hostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostname.setStatus("current")


class _DhcpEnabled_Type(Integer32):
    """Custom type dhcpEnabled based on Integer32"""
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


_DhcpEnabled_Type.__name__ = "Integer32"
_DhcpEnabled_Object = MibScalar
dhcpEnabled = _DhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 7),
    _DhcpEnabled_Type()
)
dhcpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpEnabled.setStatus("current")


class _VlanIDEnabled_Type(Integer32):
    """Custom type vlanIDEnabled based on Integer32"""
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


_VlanIDEnabled_Type.__name__ = "Integer32"
_VlanIDEnabled_Object = MibScalar
vlanIDEnabled = _VlanIDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 8),
    _VlanIDEnabled_Type()
)
vlanIDEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIDEnabled.setStatus("current")


class _VlanID_Type(Integer32):
    """Custom type vlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanID_Type.__name__ = "Integer32"
_VlanID_Object = MibScalar
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 9),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")


class _LanInterface_Type(Integer32):
    """Custom type lanInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 0),
          ("shared", 1),
          ("failover", 2))
    )


_LanInterface_Type.__name__ = "Integer32"
_LanInterface_Object = MibScalar
lanInterface = _LanInterface_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 10),
    _LanInterface_Type()
)
lanInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanInterface.setStatus("current")


class _RmcpPort_Type(Integer32):
    """Custom type rmcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RmcpPort_Type.__name__ = "Integer32"
_RmcpPort_Object = MibScalar
rmcpPort = _RmcpPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 11),
    _RmcpPort_Type()
)
rmcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcpPort.setStatus("current")


class _ActiveLanInterface_Type(Integer32):
    """Custom type activeLanInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 0),
          ("shared", 1),
          ("failover", 2))
    )


_ActiveLanInterface_Type.__name__ = "Integer32"
_ActiveLanInterface_Object = MibScalar
activeLanInterface = _ActiveLanInterface_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 12),
    _ActiveLanInterface_Type()
)
activeLanInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeLanInterface.setStatus("current")


class _DedicatedLanDuplex_Type(Integer32):
    """Custom type dedicatedLanDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("fullduplex", 1),
          ("halfduplex", 2))
    )


_DedicatedLanDuplex_Type.__name__ = "Integer32"
_DedicatedLanDuplex_Object = MibScalar
dedicatedLanDuplex = _DedicatedLanDuplex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 13),
    _DedicatedLanDuplex_Type()
)
dedicatedLanDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dedicatedLanDuplex.setStatus("current")


class _SharedLanDuplex_Type(Integer32):
    """Custom type sharedLanDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("fullduplex", 1),
          ("halfduplex", 2))
    )


_SharedLanDuplex_Type.__name__ = "Integer32"
_SharedLanDuplex_Object = MibScalar
sharedLanDuplex = _SharedLanDuplex_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 21, 14),
    _SharedLanDuplex_Type()
)
sharedLanDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedLanDuplex.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 22)
)


class _SmtpEnabled_Type(Integer32):
    """Custom type smtpEnabled based on Integer32"""
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


_SmtpEnabled_Type.__name__ = "Integer32"
_SmtpEnabled_Object = MibScalar
smtpEnabled = _SmtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 22, 1),
    _SmtpEnabled_Type()
)
smtpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpEnabled.setStatus("current")


class _SmtpServer_Type(OctetString):
    """Custom type smtpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_SmtpServer_Type.__name__ = "OctetString"
_SmtpServer_Object = MibScalar
smtpServer = _SmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 22, 2),
    _SmtpServer_Type()
)
smtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServer.setStatus("current")


class _SmtpPort_Type(Integer32):
    """Custom type smtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SmtpPort_Type.__name__ = "Integer32"
_SmtpPort_Object = MibScalar
smtpPort = _SmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 22, 3),
    _SmtpPort_Type()
)
smtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpPort.setStatus("current")


class _SmtpUsername_Type(OctetString):
    """Custom type smtpUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_SmtpUsername_Type.__name__ = "OctetString"
_SmtpUsername_Object = MibScalar
smtpUsername = _SmtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 22, 4),
    _SmtpUsername_Type()
)
smtpUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpUsername.setStatus("current")


class _SmtpSenderEmail_Type(OctetString):
    """Custom type smtpSenderEmail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(63, 63),
    )
    fixed_length = 63


_SmtpSenderEmail_Type.__name__ = "OctetString"
_SmtpSenderEmail_Object = MibScalar
smtpSenderEmail = _SmtpSenderEmail_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 22, 5),
    _SmtpSenderEmail_Type()
)
smtpSenderEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpSenderEmail.setStatus("current")


class _MouseMode_Type(Integer32):
    """Custom type mouseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("relative", 2),
          ("single", 3))
    )


_MouseMode_Type.__name__ = "Integer32"
_MouseMode_Object = MibScalar
mouseMode = _MouseMode_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 23),
    _MouseMode_Type()
)
mouseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mouseMode.setStatus("current")


class _SysBootOrder_Type(Integer32):
    """Custom type sysBootOrder based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pxe", 1),
          ("hdd", 2),
          ("diags", 3),
          ("cdDvd", 4),
          ("biosSetup", 5),
          ("floppy", 6),
          ("usbKey", 7),
          ("usbHdd", 8),
          ("usbFloppy", 9),
          ("usbCD", 10),
          ("uefiUsbKey", 11),
          ("uefiCD", 12),
          ("uefiHdd", 13),
          ("uefiUsbHdd", 14),
          ("uefiUsbCD", 15))
    )


_SysBootOrder_Type.__name__ = "Integer32"
_SysBootOrder_Object = MibScalar
sysBootOrder = _SysBootOrder_Object(
    (1, 3, 6, 1, 4, 1, 21317, 1, 24),
    _SysBootOrder_Type()
)
sysBootOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBootOrder.setStatus("current")

# Managed Objects groups


# Notification objects

guid = NotificationType(
    (1, 3, 6, 1, 4, 1, 21317, 1, 30)
)
if mibBuilder.loadTexts:
    guid.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATEN-IPMI-MIB",
    **{"aten": aten,
       "ipmi": ipmi,
       "sel": sel,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorNumber": sensorNumber,
       "sensorReading": sensorReading,
       "sensorPositiveHysteresis": sensorPositiveHysteresis,
       "sensorNegativeHysteresis": sensorNegativeHysteresis,
       "lncThreshold": lncThreshold,
       "lcThreshold": lcThreshold,
       "lnrThreshold": lnrThreshold,
       "uncThreshold": uncThreshold,
       "ucThreshold": ucThreshold,
       "unrThreshold": unrThreshold,
       "eventAssertionEnable": eventAssertionEnable,
       "eventDeassertionEnable": eventDeassertionEnable,
       "sensorIDString": sensorIDString,
       "powerStatus": powerStatus,
       "boardinfo": boardinfo,
       "bmcMajorVesion": bmcMajorVesion,
       "bmcMinorVesion": bmcMinorVesion,
       "bmcBuildDate": bmcBuildDate,
       "biosVesion": biosVesion,
       "biosBuildDate": biosBuildDate,
       "hostName": hostName,
       "bmcBuildVesion": bmcBuildVesion,
       "hardwareinfo": hardwareinfo,
       "serialNumber": serialNumber,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuNumber": cpuNumber,
       "processor": processor,
       "speed": speed,
       "core": core,
       "coreActive": coreActive,
       "manufacturer": manufacturer,
       "dimmTable": dimmTable,
       "dimmEntry": dimmEntry,
       "dimmNumber": dimmNumber,
       "dimmLocation": dimmLocation,
       "dimmMaxCapSpeed": dimmMaxCapSpeed,
       "dimmOpSpeed": dimmOpSpeed,
       "dimmSize": dimmSize,
       "dimmSerialNo": dimmSerialNo,
       "dimmPartNo": dimmPartNo,
       "dimmManufacturer": dimmManufacturer,
       "storage": storage,
       "controllerTable": controllerTable,
       "controllerEntry": controllerEntry,
       "controllerNumber": controllerNumber,
       "controllerProductName": controllerProductName,
       "serial": serial,
       "package": package,
       "fwVersion": fwVersion,
       "biosVersion": biosVersion,
       "bootBlockVersion": bootBlockVersion,
       "batteryStatus": batteryStatus,
       "pcieLocation": pcieLocation,
       "pcieSlot": pcieSlot,
       "phyHddTable": phyHddTable,
       "hddEntry": hddEntry,
       "hddNumber": hddNumber,
       "hddControllerNumber": hddControllerNumber,
       "enclosureNumber": enclosureNumber,
       "status": status,
       "temperature": temperature,
       "capacity": capacity,
       "vendor": vendor,
       "modelName": modelName,
       "revision": revision,
       "sn": sn,
       "linkSpeed": linkSpeed,
       "fwState": fwState,
       "otherErrCount": otherErrCount,
       "predictedFailCount": predictedFailCount,
       "mediaErrCount": mediaErrCount,
       "logHddTable": logHddTable,
       "volumeEntry": volumeEntry,
       "volNumber": volNumber,
       "volControllerNumber": volControllerNumber,
       "volStatus": volStatus,
       "volCapacity": volCapacity,
       "priRaidLevel": priRaidLevel,
       "raidLevelQualifier": raidLevelQualifier,
       "secRaidLevel": secRaidLevel,
       "ldStripSize": ldStripSize,
       "numDevices": numDevices,
       "spanDepth": spanDepth,
       "state": state,
       "volName": volName,
       "coldResetBMC": coldResetBMC,
       "userTable": userTable,
       "userInfo": userInfo,
       "id": id,
       "username": username,
       "password": password,
       "privilege": privilege,
       "uid": uid,
       "alertTable": alertTable,
       "alertInfo": alertInfo,
       "alertNo": alertNo,
       "alertLevel": alertLevel,
       "destinationAddress": destinationAddress,
       "powerinfo": powerinfo,
       "psuNumber": psuNumber,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuIndex": psuIndex,
       "psuStatus": psuStatus,
       "inputVoltage": inputVoltage,
       "inputCurrent": inputCurrent,
       "inputPower": inputPower,
       "outputVoltage": outputVoltage,
       "outputCurrent": outputCurrent,
       "outputPower": outputPower,
       "temperature1": temperature1,
       "temperature2": temperature2,
       "fanRPM1": fanRPM1,
       "fanRPM2": fanRPM2,
       "psuSerialNumber": psuSerialNumber,
       "fanMode": fanMode,
       "fruinfo": fruinfo,
       "chassis": chassis,
       "chassisType": chassisType,
       "chassisPartNumber": chassisPartNumber,
       "chassisSerialNumber": chassisSerialNumber,
       "board": board,
       "boardLanguage": boardLanguage,
       "boardManufacturer": boardManufacturer,
       "boardProductName": boardProductName,
       "boardSerialNumber": boardSerialNumber,
       "boardPartNumber": boardPartNumber,
       "product": product,
       "productLanguage": productLanguage,
       "productManufacturer": productManufacturer,
       "productName": productName,
       "productPartNumber": productPartNumber,
       "productVersion": productVersion,
       "productSerialNumber": productSerialNumber,
       "productAssetTag": productAssetTag,
       "ntpinfo": ntpinfo,
       "timeZone": timeZone,
       "ntpEnable": ntpEnable,
       "primaryNTPServer": primaryNTPServer,
       "secondaryNTPServer": secondaryNTPServer,
       "dst": dst,
       "selTable": selTable,
       "selEntry": selEntry,
       "selEid": selEid,
       "selTimeStamp": selTimeStamp,
       "selSensorName": selSensorName,
       "selSensorType": selSensorType,
       "selDescription": selDescription,
       "selRawData": selRawData,
       "nvme": nvme,
       "nvmeCtrlTbl": nvmeCtrlTbl,
       "nvmeCtrlEntry": nvmeCtrlEntry,
       "nvmeCtrlPresent": nvmeCtrlPresent,
       "maxTemp": maxTemp,
       "maxSlotNum": maxSlotNum,
       "onboard": onboard,
       "driverIndex": driverIndex,
       "cpldVer": cpldVer,
       "nvmeDriveTbl": nvmeDriveTbl,
       "nvmeDriveEntry": nvmeDriveEntry,
       "slotId": slotId,
       "groupId": groupId,
       "nvmeDrivePresent": nvmeDrivePresent,
       "locate": locate,
       "save2Remove": save2Remove,
       "vmdMode": vmdMode,
       "temp": temp,
       "classCode": classCode,
       "vendorID": vendorID,
       "serialNum": serialNum,
       "modelNum": modelNum,
       "port0MaxLinkSpd": port0MaxLinkSpd,
       "port0MaxLinkWidth": port0MaxLinkWidth,
       "port1MaxLinkSpd": port1MaxLinkSpd,
       "port1MaxLinkWidth": port1MaxLinkWidth,
       "initPowerRequirement": initPowerRequirement,
       "maxPowerRequirement": maxPowerRequirement,
       "nicTable": nicTable,
       "nicEntry": nicEntry,
       "nicNumber": nicNumber,
       "nicName": nicName,
       "nicMac": nicMac,
       "nicIpv4Addr": nicIpv4Addr,
       "nicIpv6Addr": nicIpv6Addr,
       "nicGateway": nicGateway,
       "nicNetmask": nicNetmask,
       "nicFqdn": nicFqdn,
       "nicDns": nicDns,
       "nicSpeed": nicSpeed,
       "nicDescript": nicDescript,
       "nicStatus": nicStatus,
       "network": network,
       "ipv4DNSServer": ipv4DNSServer,
       "ipv4Gateway": ipv4Gateway,
       "ipv6DNSServer": ipv6DNSServer,
       "ipv6DUID": ipv6DUID,
       "dhcpv6State": dhcpv6State,
       "hostname": hostname,
       "dhcpEnabled": dhcpEnabled,
       "vlanIDEnabled": vlanIDEnabled,
       "vlanID": vlanID,
       "lanInterface": lanInterface,
       "rmcpPort": rmcpPort,
       "activeLanInterface": activeLanInterface,
       "dedicatedLanDuplex": dedicatedLanDuplex,
       "sharedLanDuplex": sharedLanDuplex,
       "smtp": smtp,
       "smtpEnabled": smtpEnabled,
       "smtpServer": smtpServer,
       "smtpPort": smtpPort,
       "smtpUsername": smtpUsername,
       "smtpSenderEmail": smtpSenderEmail,
       "mouseMode": mouseMode,
       "sysBootOrder": sysBootOrder,
       "guid": guid}
)
