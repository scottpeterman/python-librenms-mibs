# SNMP MIB module (OG-OMTELEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\opengear\OG-OMTELEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:27 2025
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

(ogMgmt,) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "ogMgmt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ogOmTelem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19)
)
if mibBuilder.loadTexts:
    ogOmTelem.setRevisions(
        ("2023-11-13 09:34",
         "2021-03-12 14:54",
         "2020-08-04 14:54")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgOmSystem_ObjectIdentity = ObjectIdentity
ogOmSystem = _OgOmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 1)
)


class _OgOmSystemHostName_Type(DisplayString):
    """Custom type ogOmSystemHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OgOmSystemHostName_Type.__name__ = "DisplayString"
_OgOmSystemHostName_Object = MibScalar
ogOmSystemHostName = _OgOmSystemHostName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 1, 1),
    _OgOmSystemHostName_Type()
)
ogOmSystemHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSystemHostName.setStatus("current")


class _OgOmSystemSerialNumber_Type(DisplayString):
    """Custom type ogOmSystemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmSystemSerialNumber_Type.__name__ = "DisplayString"
_OgOmSystemSerialNumber_Object = MibScalar
ogOmSystemSerialNumber = _OgOmSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 1, 2),
    _OgOmSystemSerialNumber_Type()
)
ogOmSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSystemSerialNumber.setStatus("current")


class _OgOmSystemFirmwareVersion_Type(DisplayString):
    """Custom type ogOmSystemFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmSystemFirmwareVersion_Type.__name__ = "DisplayString"
_OgOmSystemFirmwareVersion_Object = MibScalar
ogOmSystemFirmwareVersion = _OgOmSystemFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 1, 3),
    _OgOmSystemFirmwareVersion_Type()
)
ogOmSystemFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSystemFirmwareVersion.setStatus("current")


class _OgOmSystemVendor_Type(DisplayString):
    """Custom type ogOmSystemVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmSystemVendor_Type.__name__ = "DisplayString"
_OgOmSystemVendor_Object = MibScalar
ogOmSystemVendor = _OgOmSystemVendor_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 1, 4),
    _OgOmSystemVendor_Type()
)
ogOmSystemVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSystemVendor.setStatus("current")


class _OgOmSystemModel_Type(DisplayString):
    """Custom type ogOmSystemModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OgOmSystemModel_Type.__name__ = "DisplayString"
_OgOmSystemModel_Object = MibScalar
ogOmSystemModel = _OgOmSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 1, 5),
    _OgOmSystemModel_Type()
)
ogOmSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSystemModel.setStatus("current")
_OgOmSerialPort_ObjectIdentity = ObjectIdentity
ogOmSerialPort = _OgOmSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2)
)


class _OgOmSerialPortCount_Type(Integer32):
    """Custom type ogOmSerialPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmSerialPortCount_Type.__name__ = "Integer32"
_OgOmSerialPortCount_Object = MibScalar
ogOmSerialPortCount = _OgOmSerialPortCount_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 1),
    _OgOmSerialPortCount_Type()
)
ogOmSerialPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ogOmSerialPortCount.setStatus("current")
_OgOmSerialPortTable_Object = MibTable
ogOmSerialPortTable = _OgOmSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2)
)
if mibBuilder.loadTexts:
    ogOmSerialPortTable.setStatus("current")
_OgOmSerialPortEntry_Object = MibTableRow
ogOmSerialPortEntry = _OgOmSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1)
)
ogOmSerialPortEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmSerialPortIndex"),
)
if mibBuilder.loadTexts:
    ogOmSerialPortEntry.setStatus("current")


class _OgOmSerialPortIndex_Type(Integer32):
    """Custom type ogOmSerialPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmSerialPortIndex_Type.__name__ = "Integer32"
_OgOmSerialPortIndex_Object = MibTableColumn
ogOmSerialPortIndex = _OgOmSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 1),
    _OgOmSerialPortIndex_Type()
)
ogOmSerialPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmSerialPortIndex.setStatus("current")


class _OgOmSerialPortLabel_Type(DisplayString):
    """Custom type ogOmSerialPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmSerialPortLabel_Type.__name__ = "DisplayString"
_OgOmSerialPortLabel_Object = MibTableColumn
ogOmSerialPortLabel = _OgOmSerialPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 2),
    _OgOmSerialPortLabel_Type()
)
ogOmSerialPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortLabel.setStatus("current")
_OgOmSerialPortSpeed_Type = Integer32
_OgOmSerialPortSpeed_Object = MibTableColumn
ogOmSerialPortSpeed = _OgOmSerialPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 3),
    _OgOmSerialPortSpeed_Type()
)
ogOmSerialPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortSpeed.setStatus("current")
_OgOmSerialPortDataBits_Type = Integer32
_OgOmSerialPortDataBits_Object = MibTableColumn
ogOmSerialPortDataBits = _OgOmSerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 4),
    _OgOmSerialPortDataBits_Type()
)
ogOmSerialPortDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortDataBits.setStatus("current")


class _OgOmSerialPortParity_Type(Integer32):
    """Custom type ogOmSerialPortParity based on Integer32"""
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
        *(("none", 1),
          ("odd", 2),
          ("even", 3),
          ("mark", 4),
          ("space", 5))
    )


_OgOmSerialPortParity_Type.__name__ = "Integer32"
_OgOmSerialPortParity_Object = MibTableColumn
ogOmSerialPortParity = _OgOmSerialPortParity_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 5),
    _OgOmSerialPortParity_Type()
)
ogOmSerialPortParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortParity.setStatus("current")


class _OgOmSerialPortStopBits_Type(Integer32):
    """Custom type ogOmSerialPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2),
          ("oneAndAHalf", 3))
    )


_OgOmSerialPortStopBits_Type.__name__ = "Integer32"
_OgOmSerialPortStopBits_Object = MibTableColumn
ogOmSerialPortStopBits = _OgOmSerialPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 6),
    _OgOmSerialPortStopBits_Type()
)
ogOmSerialPortStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortStopBits.setStatus("current")


class _OgOmSerialPortFlowControl_Type(Integer32):
    """Custom type ogOmSerialPortFlowControl based on Integer32"""
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
          ("hardware", 2),
          ("software", 3))
    )


_OgOmSerialPortFlowControl_Type.__name__ = "Integer32"
_OgOmSerialPortFlowControl_Object = MibTableColumn
ogOmSerialPortFlowControl = _OgOmSerialPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 7),
    _OgOmSerialPortFlowControl_Type()
)
ogOmSerialPortFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortFlowControl.setStatus("current")


class _OgOmSerialPortMode_Type(Integer32):
    """Custom type ogOmSerialPortMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("localConsole", 2),
          ("consoleServer", 3),
          ("bridge", 4),
          ("terminalServer", 5),
          ("reserved", 6),
          ("pduDevice", 7),
          ("unknown", 8))
    )


_OgOmSerialPortMode_Type.__name__ = "Integer32"
_OgOmSerialPortMode_Object = MibTableColumn
ogOmSerialPortMode = _OgOmSerialPortMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 8),
    _OgOmSerialPortMode_Type()
)
ogOmSerialPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortMode.setStatus("current")


class _OgOmSerialPortPinout_Type(Integer32):
    """Custom type ogOmSerialPortPinout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("x1", 1),
          ("x2", 2),
          ("usb", 3))
    )


_OgOmSerialPortPinout_Type.__name__ = "Integer32"
_OgOmSerialPortPinout_Object = MibTableColumn
ogOmSerialPortPinout = _OgOmSerialPortPinout_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 9),
    _OgOmSerialPortPinout_Type()
)
ogOmSerialPortPinout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortPinout.setStatus("current")


class _OgOmSerialPortLogLevel_Type(Integer32):
    """Custom type ogOmSerialPortLogLevel based on Integer32"""
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
        *(("disabled", 1),
          ("connect", 2),
          ("inputAndOutput", 3),
          ("inputOnly", 4))
    )


_OgOmSerialPortLogLevel_Type.__name__ = "Integer32"
_OgOmSerialPortLogLevel_Object = MibTableColumn
ogOmSerialPortLogLevel = _OgOmSerialPortLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 10),
    _OgOmSerialPortLogLevel_Type()
)
ogOmSerialPortLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortLogLevel.setStatus("current")
_OgOmSerialPortRxBytes_Type = Counter64
_OgOmSerialPortRxBytes_Object = MibTableColumn
ogOmSerialPortRxBytes = _OgOmSerialPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 11),
    _OgOmSerialPortRxBytes_Type()
)
ogOmSerialPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortRxBytes.setStatus("current")
_OgOmSerialPortTxBytes_Type = Counter64
_OgOmSerialPortTxBytes_Object = MibTableColumn
ogOmSerialPortTxBytes = _OgOmSerialPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 12),
    _OgOmSerialPortTxBytes_Type()
)
ogOmSerialPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortTxBytes.setStatus("current")
_OgOmSerialPortFramingErrors_Type = Counter64
_OgOmSerialPortFramingErrors_Object = MibTableColumn
ogOmSerialPortFramingErrors = _OgOmSerialPortFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 13),
    _OgOmSerialPortFramingErrors_Type()
)
ogOmSerialPortFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortFramingErrors.setStatus("current")
_OgOmSerialPortParityErrors_Type = Counter64
_OgOmSerialPortParityErrors_Object = MibTableColumn
ogOmSerialPortParityErrors = _OgOmSerialPortParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 14),
    _OgOmSerialPortParityErrors_Type()
)
ogOmSerialPortParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortParityErrors.setStatus("current")
_OgOmSerialPortOverrunErrors_Type = Counter64
_OgOmSerialPortOverrunErrors_Object = MibTableColumn
ogOmSerialPortOverrunErrors = _OgOmSerialPortOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 15),
    _OgOmSerialPortOverrunErrors_Type()
)
ogOmSerialPortOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortOverrunErrors.setStatus("current")
_OgOmSerialPortBreaks_Type = Counter64
_OgOmSerialPortBreaks_Object = MibTableColumn
ogOmSerialPortBreaks = _OgOmSerialPortBreaks_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 16),
    _OgOmSerialPortBreaks_Type()
)
ogOmSerialPortBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortBreaks.setStatus("current")


class _OgOmSerialPortDCD_Type(Integer32):
    """Custom type ogOmSerialPortDCD based on Integer32"""
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
          ("on", 1),
          ("off", 2))
    )


_OgOmSerialPortDCD_Type.__name__ = "Integer32"
_OgOmSerialPortDCD_Object = MibTableColumn
ogOmSerialPortDCD = _OgOmSerialPortDCD_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 17),
    _OgOmSerialPortDCD_Type()
)
ogOmSerialPortDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortDCD.setStatus("current")


class _OgOmSerialPortDTR_Type(Integer32):
    """Custom type ogOmSerialPortDTR based on Integer32"""
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
          ("on", 1),
          ("off", 2))
    )


_OgOmSerialPortDTR_Type.__name__ = "Integer32"
_OgOmSerialPortDTR_Object = MibTableColumn
ogOmSerialPortDTR = _OgOmSerialPortDTR_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 18),
    _OgOmSerialPortDTR_Type()
)
ogOmSerialPortDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortDTR.setStatus("current")


class _OgOmSerialPortDSR_Type(Integer32):
    """Custom type ogOmSerialPortDSR based on Integer32"""
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
          ("on", 1),
          ("off", 2))
    )


_OgOmSerialPortDSR_Type.__name__ = "Integer32"
_OgOmSerialPortDSR_Object = MibTableColumn
ogOmSerialPortDSR = _OgOmSerialPortDSR_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 19),
    _OgOmSerialPortDSR_Type()
)
ogOmSerialPortDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortDSR.setStatus("current")


class _OgOmSerialPortCTS_Type(Integer32):
    """Custom type ogOmSerialPortCTS based on Integer32"""
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
          ("on", 1),
          ("off", 2))
    )


_OgOmSerialPortCTS_Type.__name__ = "Integer32"
_OgOmSerialPortCTS_Object = MibTableColumn
ogOmSerialPortCTS = _OgOmSerialPortCTS_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 20),
    _OgOmSerialPortCTS_Type()
)
ogOmSerialPortCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortCTS.setStatus("current")


class _OgOmSerialPortRTS_Type(Integer32):
    """Custom type ogOmSerialPortRTS based on Integer32"""
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
          ("on", 1),
          ("off", 2))
    )


_OgOmSerialPortRTS_Type.__name__ = "Integer32"
_OgOmSerialPortRTS_Object = MibTableColumn
ogOmSerialPortRTS = _OgOmSerialPortRTS_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 2, 2, 1, 21),
    _OgOmSerialPortRTS_Type()
)
ogOmSerialPortRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialPortRTS.setStatus("current")
_OgOmSerialUser_ObjectIdentity = ObjectIdentity
ogOmSerialUser = _OgOmSerialUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3)
)
_OgOmSerialUserTable_Object = MibTable
ogOmSerialUserTable = _OgOmSerialUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3, 1)
)
if mibBuilder.loadTexts:
    ogOmSerialUserTable.setStatus("current")
_OgOmSerialUserEntry_Object = MibTableRow
ogOmSerialUserEntry = _OgOmSerialUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3, 1, 1)
)
ogOmSerialUserEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmSerialUserIndex"),
)
if mibBuilder.loadTexts:
    ogOmSerialUserEntry.setStatus("current")


class _OgOmSerialUserIndex_Type(Integer32):
    """Custom type ogOmSerialUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmSerialUserIndex_Type.__name__ = "Integer32"
_OgOmSerialUserIndex_Object = MibTableColumn
ogOmSerialUserIndex = _OgOmSerialUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3, 1, 1, 1),
    _OgOmSerialUserIndex_Type()
)
ogOmSerialUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmSerialUserIndex.setStatus("current")
_OgOmSerialUserStartTime_Type = DateAndTime
_OgOmSerialUserStartTime_Object = MibTableColumn
ogOmSerialUserStartTime = _OgOmSerialUserStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3, 1, 1, 2),
    _OgOmSerialUserStartTime_Type()
)
ogOmSerialUserStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialUserStartTime.setStatus("current")
_OgOmSerialUserPortNumber_Type = Integer32
_OgOmSerialUserPortNumber_Object = MibTableColumn
ogOmSerialUserPortNumber = _OgOmSerialUserPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3, 1, 1, 3),
    _OgOmSerialUserPortNumber_Type()
)
ogOmSerialUserPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialUserPortNumber.setStatus("current")


class _OgOmSerialUserPortLabel_Type(DisplayString):
    """Custom type ogOmSerialUserPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmSerialUserPortLabel_Type.__name__ = "DisplayString"
_OgOmSerialUserPortLabel_Object = MibTableColumn
ogOmSerialUserPortLabel = _OgOmSerialUserPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3, 1, 1, 4),
    _OgOmSerialUserPortLabel_Type()
)
ogOmSerialUserPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialUserPortLabel.setStatus("current")


class _OgOmSerialUserName_Type(DisplayString):
    """Custom type ogOmSerialUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmSerialUserName_Type.__name__ = "DisplayString"
_OgOmSerialUserName_Object = MibTableColumn
ogOmSerialUserName = _OgOmSerialUserName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 3, 1, 1, 5),
    _OgOmSerialUserName_Type()
)
ogOmSerialUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmSerialUserName.setStatus("current")
_OgOmWebUser_ObjectIdentity = ObjectIdentity
ogOmWebUser = _OgOmWebUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4)
)
_OgOmWebUserTable_Object = MibTable
ogOmWebUserTable = _OgOmWebUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4, 1)
)
if mibBuilder.loadTexts:
    ogOmWebUserTable.setStatus("current")
_OgOmWebUserEntry_Object = MibTableRow
ogOmWebUserEntry = _OgOmWebUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4, 1, 1)
)
ogOmWebUserEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmWebUserIndex"),
)
if mibBuilder.loadTexts:
    ogOmWebUserEntry.setStatus("current")


class _OgOmWebUserIndex_Type(Integer32):
    """Custom type ogOmWebUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmWebUserIndex_Type.__name__ = "Integer32"
_OgOmWebUserIndex_Object = MibTableColumn
ogOmWebUserIndex = _OgOmWebUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4, 1, 1, 1),
    _OgOmWebUserIndex_Type()
)
ogOmWebUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmWebUserIndex.setStatus("current")
_OgOmWebUserStartTime_Type = DateAndTime
_OgOmWebUserStartTime_Object = MibTableColumn
ogOmWebUserStartTime = _OgOmWebUserStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4, 1, 1, 2),
    _OgOmWebUserStartTime_Type()
)
ogOmWebUserStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmWebUserStartTime.setStatus("current")


class _OgOmWebUserName_Type(DisplayString):
    """Custom type ogOmWebUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmWebUserName_Type.__name__ = "DisplayString"
_OgOmWebUserName_Object = MibTableColumn
ogOmWebUserName = _OgOmWebUserName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4, 1, 1, 3),
    _OgOmWebUserName_Type()
)
ogOmWebUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmWebUserName.setStatus("current")


class _OgOmWebUserSourceAddress_Type(DisplayString):
    """Custom type ogOmWebUserSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmWebUserSourceAddress_Type.__name__ = "DisplayString"
_OgOmWebUserSourceAddress_Object = MibTableColumn
ogOmWebUserSourceAddress = _OgOmWebUserSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4, 1, 1, 4),
    _OgOmWebUserSourceAddress_Type()
)
ogOmWebUserSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmWebUserSourceAddress.setStatus("current")


class _OgOmWebUserSourcePort_Type(Integer32):
    """Custom type ogOmWebUserSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmWebUserSourcePort_Type.__name__ = "Integer32"
_OgOmWebUserSourcePort_Object = MibTableColumn
ogOmWebUserSourcePort = _OgOmWebUserSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 4, 1, 1, 5),
    _OgOmWebUserSourcePort_Type()
)
ogOmWebUserSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmWebUserSourcePort.setStatus("current")
_OgOmCellular_ObjectIdentity = ObjectIdentity
ogOmCellular = _OgOmCellular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5)
)
_OgOmCellularTable_Object = MibTable
ogOmCellularTable = _OgOmCellularTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1)
)
if mibBuilder.loadTexts:
    ogOmCellularTable.setStatus("current")
_OgOmCellularEntry_Object = MibTableRow
ogOmCellularEntry = _OgOmCellularEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1)
)
ogOmCellularEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmCellularIndex"),
)
if mibBuilder.loadTexts:
    ogOmCellularEntry.setStatus("current")


class _OgOmCellularIndex_Type(Integer32):
    """Custom type ogOmCellularIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmCellularIndex_Type.__name__ = "Integer32"
_OgOmCellularIndex_Object = MibTableColumn
ogOmCellularIndex = _OgOmCellularIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 1),
    _OgOmCellularIndex_Type()
)
ogOmCellularIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmCellularIndex.setStatus("current")


class _OgOmCellularVendor_Type(DisplayString):
    """Custom type ogOmCellularVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellularVendor_Type.__name__ = "DisplayString"
_OgOmCellularVendor_Object = MibTableColumn
ogOmCellularVendor = _OgOmCellularVendor_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 2),
    _OgOmCellularVendor_Type()
)
ogOmCellularVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularVendor.setStatus("current")


class _OgOmCellularModel_Type(DisplayString):
    """Custom type ogOmCellularModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellularModel_Type.__name__ = "DisplayString"
_OgOmCellularModel_Object = MibTableColumn
ogOmCellularModel = _OgOmCellularModel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 3),
    _OgOmCellularModel_Type()
)
ogOmCellularModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularModel.setStatus("current")


class _OgOmCellularEquipmentId_Type(DisplayString):
    """Custom type ogOmCellularEquipmentId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellularEquipmentId_Type.__name__ = "DisplayString"
_OgOmCellularEquipmentId_Object = MibTableColumn
ogOmCellularEquipmentId = _OgOmCellularEquipmentId_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 4),
    _OgOmCellularEquipmentId_Type()
)
ogOmCellularEquipmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularEquipmentId.setStatus("current")


class _OgOmCellularFirmware_Type(DisplayString):
    """Custom type ogOmCellularFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellularFirmware_Type.__name__ = "DisplayString"
_OgOmCellularFirmware_Object = MibTableColumn
ogOmCellularFirmware = _OgOmCellularFirmware_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 5),
    _OgOmCellularFirmware_Type()
)
ogOmCellularFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularFirmware.setStatus("current")


class _OgOmCellularState_Type(Integer32):
    """Custom type ogOmCellularState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("unknown", 2),
          ("initializing", 3),
          ("locked", 4),
          ("disabled", 5),
          ("disabling", 6),
          ("enabling", 7),
          ("enabled", 8),
          ("searching", 9),
          ("registered", 10),
          ("disconnecting", 11),
          ("connecting", 12),
          ("connected", 13))
    )


_OgOmCellularState_Type.__name__ = "Integer32"
_OgOmCellularState_Object = MibTableColumn
ogOmCellularState = _OgOmCellularState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 6),
    _OgOmCellularState_Type()
)
ogOmCellularState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularState.setStatus("current")


class _OgOmCellularAccessTechnology_Type(Integer32):
    """Custom type ogOmCellularAccessTechnology based on Integer32"""
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
        *(("unavailable", 1),
          ("cdma", 2),
          ("evdo", 3),
          ("gsm", 4),
          ("umts", 5),
          ("lte", 6),
          ("gsmUmts", 7),
          ("gsmUmtsLte", 8),
          ("cdmaEvdo", 9),
          ("cdmaEvdoLte", 10),
          ("lteNr5g", 11),
          ("nr5g", 12))
    )


_OgOmCellularAccessTechnology_Type.__name__ = "Integer32"
_OgOmCellularAccessTechnology_Object = MibTableColumn
ogOmCellularAccessTechnology = _OgOmCellularAccessTechnology_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 7),
    _OgOmCellularAccessTechnology_Type()
)
ogOmCellularAccessTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularAccessTechnology.setStatus("current")
_OgOmCellularActiveUim_Type = Counter32
_OgOmCellularActiveUim_Object = MibTableColumn
ogOmCellularActiveUim = _OgOmCellularActiveUim_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 8),
    _OgOmCellularActiveUim_Type()
)
ogOmCellularActiveUim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularActiveUim.setStatus("current")


class _OgOmCellularUimFailoverState_Type(Integer32):
    """Custom type ogOmCellularUimFailoverState based on Integer32"""
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
        *(("unavailable", 1),
          ("disabled", 2),
          ("enabled", 3),
          ("failingOver", 4),
          ("failedOver", 5),
          ("failingBack", 6))
    )


_OgOmCellularUimFailoverState_Type.__name__ = "Integer32"
_OgOmCellularUimFailoverState_Object = MibTableColumn
ogOmCellularUimFailoverState = _OgOmCellularUimFailoverState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 5, 1, 1, 9),
    _OgOmCellularUimFailoverState_Type()
)
ogOmCellularUimFailoverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellularUimFailoverState.setStatus("current")
_OgOmCellUim_ObjectIdentity = ObjectIdentity
ogOmCellUim = _OgOmCellUim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6)
)
_OgOmCellUimTable_Object = MibTable
ogOmCellUimTable = _OgOmCellUimTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1)
)
if mibBuilder.loadTexts:
    ogOmCellUimTable.setStatus("current")
_OgOmCellUimEntry_Object = MibTableRow
ogOmCellUimEntry = _OgOmCellUimEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1)
)
ogOmCellUimEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmCellUimIndex"),
)
if mibBuilder.loadTexts:
    ogOmCellUimEntry.setStatus("current")


class _OgOmCellUimIndex_Type(Integer32):
    """Custom type ogOmCellUimIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmCellUimIndex_Type.__name__ = "Integer32"
_OgOmCellUimIndex_Object = MibTableColumn
ogOmCellUimIndex = _OgOmCellUimIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 1),
    _OgOmCellUimIndex_Type()
)
ogOmCellUimIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmCellUimIndex.setStatus("current")
_OgOmCellUimPhysicalSlot_Type = Counter32
_OgOmCellUimPhysicalSlot_Object = MibTableColumn
ogOmCellUimPhysicalSlot = _OgOmCellUimPhysicalSlot_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 2),
    _OgOmCellUimPhysicalSlot_Type()
)
ogOmCellUimPhysicalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimPhysicalSlot.setStatus("current")


class _OgOmCellUimSlotState_Type(Integer32):
    """Custom type ogOmCellUimSlotState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("inactive", 2),
          ("active", 3))
    )


_OgOmCellUimSlotState_Type.__name__ = "Integer32"
_OgOmCellUimSlotState_Object = MibTableColumn
ogOmCellUimSlotState = _OgOmCellUimSlotState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 3),
    _OgOmCellUimSlotState_Type()
)
ogOmCellUimSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimSlotState.setStatus("current")


class _OgOmCellUimCardState_Type(Integer32):
    """Custom type ogOmCellUimCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("absent", 2),
          ("present", 3))
    )


_OgOmCellUimCardState_Type.__name__ = "Integer32"
_OgOmCellUimCardState_Object = MibTableColumn
ogOmCellUimCardState = _OgOmCellUimCardState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 4),
    _OgOmCellUimCardState_Type()
)
ogOmCellUimCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimCardState.setStatus("current")


class _OgOmCellUimIccid_Type(DisplayString):
    """Custom type ogOmCellUimIccid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellUimIccid_Type.__name__ = "DisplayString"
_OgOmCellUimIccid_Object = MibTableColumn
ogOmCellUimIccid = _OgOmCellUimIccid_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 5),
    _OgOmCellUimIccid_Type()
)
ogOmCellUimIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimIccid.setStatus("current")


class _OgOmCellUimImsi_Type(DisplayString):
    """Custom type ogOmCellUimImsi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellUimImsi_Type.__name__ = "DisplayString"
_OgOmCellUimImsi_Object = MibTableColumn
ogOmCellUimImsi = _OgOmCellUimImsi_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 6),
    _OgOmCellUimImsi_Type()
)
ogOmCellUimImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimImsi.setStatus("current")


class _OgOmCellUimOperatorName_Type(DisplayString):
    """Custom type ogOmCellUimOperatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellUimOperatorName_Type.__name__ = "DisplayString"
_OgOmCellUimOperatorName_Object = MibTableColumn
ogOmCellUimOperatorName = _OgOmCellUimOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 7),
    _OgOmCellUimOperatorName_Type()
)
ogOmCellUimOperatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimOperatorName.setStatus("current")


class _OgOmCellUimApn_Type(DisplayString):
    """Custom type ogOmCellUimApn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellUimApn_Type.__name__ = "DisplayString"
_OgOmCellUimApn_Object = MibTableColumn
ogOmCellUimApn = _OgOmCellUimApn_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 8),
    _OgOmCellUimApn_Type()
)
ogOmCellUimApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimApn.setStatus("current")


class _OgOmCellUimSignalQuality_Type(Integer32):
    """Custom type ogOmCellUimSignalQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OgOmCellUimSignalQuality_Type.__name__ = "Integer32"
_OgOmCellUimSignalQuality_Object = MibTableColumn
ogOmCellUimSignalQuality = _OgOmCellUimSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 9),
    _OgOmCellUimSignalQuality_Type()
)
ogOmCellUimSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimSignalQuality.setStatus("current")


class _OgOmCellUimRssi_Type(Integer32):
    """Custom type ogOmCellUimRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 99),
    )


_OgOmCellUimRssi_Type.__name__ = "Integer32"
_OgOmCellUimRssi_Object = MibTableColumn
ogOmCellUimRssi = _OgOmCellUimRssi_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 10),
    _OgOmCellUimRssi_Type()
)
ogOmCellUimRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimRssi.setStatus("current")


class _OgOmCellUimConnectivityHealth_Type(Integer32):
    """Custom type ogOmCellUimConnectivityHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("bad", 2),
          ("good", 3))
    )


_OgOmCellUimConnectivityHealth_Type.__name__ = "Integer32"
_OgOmCellUimConnectivityHealth_Object = MibTableColumn
ogOmCellUimConnectivityHealth = _OgOmCellUimConnectivityHealth_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 11),
    _OgOmCellUimConnectivityHealth_Type()
)
ogOmCellUimConnectivityHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimConnectivityHealth.setStatus("current")


class _OgOmCellUimSignalHealth_Type(Integer32):
    """Custom type ogOmCellUimSignalHealth based on Integer32"""
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
        *(("unavailable", 1),
          ("bad", 2),
          ("moderate", 3),
          ("good", 4))
    )


_OgOmCellUimSignalHealth_Type.__name__ = "Integer32"
_OgOmCellUimSignalHealth_Object = MibTableColumn
ogOmCellUimSignalHealth = _OgOmCellUimSignalHealth_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 12),
    _OgOmCellUimSignalHealth_Type()
)
ogOmCellUimSignalHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimSignalHealth.setStatus("current")
_OgOmCellUimLastUpdateTime_Type = DateAndTime
_OgOmCellUimLastUpdateTime_Object = MibTableColumn
ogOmCellUimLastUpdateTime = _OgOmCellUimLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 13),
    _OgOmCellUimLastUpdateTime_Type()
)
ogOmCellUimLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimLastUpdateTime.setStatus("current")
_OgOmCellUimLastActiveTime_Type = DateAndTime
_OgOmCellUimLastActiveTime_Object = MibTableColumn
ogOmCellUimLastActiveTime = _OgOmCellUimLastActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 14),
    _OgOmCellUimLastActiveTime_Type()
)
ogOmCellUimLastActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimLastActiveTime.setStatus("current")


class _OgOmCellUimRoamingOperatorName_Type(DisplayString):
    """Custom type ogOmCellUimRoamingOperatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmCellUimRoamingOperatorName_Type.__name__ = "DisplayString"
_OgOmCellUimRoamingOperatorName_Object = MibTableColumn
ogOmCellUimRoamingOperatorName = _OgOmCellUimRoamingOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 6, 1, 1, 15),
    _OgOmCellUimRoamingOperatorName_Type()
)
ogOmCellUimRoamingOperatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmCellUimRoamingOperatorName.setStatus("current")
_OgOmEnrollment_ObjectIdentity = ObjectIdentity
ogOmEnrollment = _OgOmEnrollment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7)
)
_OgOmEnrollmentTable_Object = MibTable
ogOmEnrollmentTable = _OgOmEnrollmentTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7, 1)
)
if mibBuilder.loadTexts:
    ogOmEnrollmentTable.setStatus("current")
_OgOmEnrollmentEntry_Object = MibTableRow
ogOmEnrollmentEntry = _OgOmEnrollmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7, 1, 1)
)
ogOmEnrollmentEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmEnrollmentIndex"),
)
if mibBuilder.loadTexts:
    ogOmEnrollmentEntry.setStatus("current")


class _OgOmEnrollmentIndex_Type(Integer32):
    """Custom type ogOmEnrollmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmEnrollmentIndex_Type.__name__ = "Integer32"
_OgOmEnrollmentIndex_Object = MibTableColumn
ogOmEnrollmentIndex = _OgOmEnrollmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7, 1, 1, 1),
    _OgOmEnrollmentIndex_Type()
)
ogOmEnrollmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmEnrollmentIndex.setStatus("current")


class _OgOmEnrollmentAddress_Type(DisplayString):
    """Custom type ogOmEnrollmentAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmEnrollmentAddress_Type.__name__ = "DisplayString"
_OgOmEnrollmentAddress_Object = MibTableColumn
ogOmEnrollmentAddress = _OgOmEnrollmentAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7, 1, 1, 2),
    _OgOmEnrollmentAddress_Type()
)
ogOmEnrollmentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmEnrollmentAddress.setStatus("current")


class _OgOmEnrollmentPort_Type(Integer32):
    """Custom type ogOmEnrollmentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmEnrollmentPort_Type.__name__ = "Integer32"
_OgOmEnrollmentPort_Object = MibTableColumn
ogOmEnrollmentPort = _OgOmEnrollmentPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7, 1, 1, 3),
    _OgOmEnrollmentPort_Type()
)
ogOmEnrollmentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmEnrollmentPort.setStatus("current")


class _OgOmEnrollmentBundle_Type(DisplayString):
    """Custom type ogOmEnrollmentBundle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgOmEnrollmentBundle_Type.__name__ = "DisplayString"
_OgOmEnrollmentBundle_Object = MibTableColumn
ogOmEnrollmentBundle = _OgOmEnrollmentBundle_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7, 1, 1, 4),
    _OgOmEnrollmentBundle_Type()
)
ogOmEnrollmentBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmEnrollmentBundle.setStatus("current")


class _OgOmEnrollmentStatus_Type(Integer32):
    """Custom type ogOmEnrollmentStatus based on Integer32"""
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
        *(("unknown", 1),
          ("enrolling", 2),
          ("connected", 3),
          ("disconnected", 4),
          ("registered", 5),
          ("failed", 6))
    )


_OgOmEnrollmentStatus_Type.__name__ = "Integer32"
_OgOmEnrollmentStatus_Object = MibTableColumn
ogOmEnrollmentStatus = _OgOmEnrollmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 7, 1, 1, 5),
    _OgOmEnrollmentStatus_Type()
)
ogOmEnrollmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmEnrollmentStatus.setStatus("current")
_OgOmPowerSupply_ObjectIdentity = ObjectIdentity
ogOmPowerSupply = _OgOmPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8)
)
_OgOmPowerSupplyTable_Object = MibTable
ogOmPowerSupplyTable = _OgOmPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1)
)
if mibBuilder.loadTexts:
    ogOmPowerSupplyTable.setStatus("current")
_OgOmPowerSupplyEntry_Object = MibTableRow
ogOmPowerSupplyEntry = _OgOmPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1, 1)
)
ogOmPowerSupplyEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    ogOmPowerSupplyEntry.setStatus("current")


class _OgOmPowerSupplyIndex_Type(Integer32):
    """Custom type ogOmPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmPowerSupplyIndex_Type.__name__ = "Integer32"
_OgOmPowerSupplyIndex_Object = MibTableColumn
ogOmPowerSupplyIndex = _OgOmPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1, 1, 1),
    _OgOmPowerSupplyIndex_Type()
)
ogOmPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmPowerSupplyIndex.setStatus("current")


class _OgOmPowerSupplyName_Type(DisplayString):
    """Custom type ogOmPowerSupplyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmPowerSupplyName_Type.__name__ = "DisplayString"
_OgOmPowerSupplyName_Object = MibTableColumn
ogOmPowerSupplyName = _OgOmPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1, 1, 2),
    _OgOmPowerSupplyName_Type()
)
ogOmPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmPowerSupplyName.setStatus("current")


class _OgOmPowerSupplyDevice_Type(DisplayString):
    """Custom type ogOmPowerSupplyDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmPowerSupplyDevice_Type.__name__ = "DisplayString"
_OgOmPowerSupplyDevice_Object = MibTableColumn
ogOmPowerSupplyDevice = _OgOmPowerSupplyDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1, 1, 3),
    _OgOmPowerSupplyDevice_Type()
)
ogOmPowerSupplyDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmPowerSupplyDevice.setStatus("current")
_OgOmPowerSupplyInputVoltage_Type = Integer32
_OgOmPowerSupplyInputVoltage_Object = MibTableColumn
ogOmPowerSupplyInputVoltage = _OgOmPowerSupplyInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1, 1, 4),
    _OgOmPowerSupplyInputVoltage_Type()
)
ogOmPowerSupplyInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmPowerSupplyInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogOmPowerSupplyInputVoltage.setUnits("0.001 volts")
_OgOmPowerSupplyOutputCurrent_Type = Integer32
_OgOmPowerSupplyOutputCurrent_Object = MibTableColumn
ogOmPowerSupplyOutputCurrent = _OgOmPowerSupplyOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1, 1, 5),
    _OgOmPowerSupplyOutputCurrent_Type()
)
ogOmPowerSupplyOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmPowerSupplyOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ogOmPowerSupplyOutputCurrent.setUnits("0.001 Amps")
_OgOmPowerSupplyOutputPower_Type = Integer32
_OgOmPowerSupplyOutputPower_Object = MibTableColumn
ogOmPowerSupplyOutputPower = _OgOmPowerSupplyOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 8, 1, 1, 6),
    _OgOmPowerSupplyOutputPower_Type()
)
ogOmPowerSupplyOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmPowerSupplyOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    ogOmPowerSupplyOutputPower.setUnits("Watts")
_OgOmTempSensor_ObjectIdentity = ObjectIdentity
ogOmTempSensor = _OgOmTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 9)
)
_OgOmTempSensorTable_Object = MibTable
ogOmTempSensorTable = _OgOmTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 9, 1)
)
if mibBuilder.loadTexts:
    ogOmTempSensorTable.setStatus("current")
_OgOmTempSensorEntry_Object = MibTableRow
ogOmTempSensorEntry = _OgOmTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 9, 1, 1)
)
ogOmTempSensorEntry.setIndexNames(
    (0, "OG-OMTELEM-MIB", "ogOmTempSensorIndex"),
)
if mibBuilder.loadTexts:
    ogOmTempSensorEntry.setStatus("current")


class _OgOmTempSensorIndex_Type(Integer32):
    """Custom type ogOmTempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgOmTempSensorIndex_Type.__name__ = "Integer32"
_OgOmTempSensorIndex_Object = MibTableColumn
ogOmTempSensorIndex = _OgOmTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 9, 1, 1, 1),
    _OgOmTempSensorIndex_Type()
)
ogOmTempSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogOmTempSensorIndex.setStatus("current")


class _OgOmTempSensorName_Type(DisplayString):
    """Custom type ogOmTempSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmTempSensorName_Type.__name__ = "DisplayString"
_OgOmTempSensorName_Object = MibTableColumn
ogOmTempSensorName = _OgOmTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 9, 1, 1, 2),
    _OgOmTempSensorName_Type()
)
ogOmTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmTempSensorName.setStatus("current")


class _OgOmTempSensorDevice_Type(DisplayString):
    """Custom type ogOmTempSensorDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OgOmTempSensorDevice_Type.__name__ = "DisplayString"
_OgOmTempSensorDevice_Object = MibTableColumn
ogOmTempSensorDevice = _OgOmTempSensorDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 9, 1, 1, 3),
    _OgOmTempSensorDevice_Type()
)
ogOmTempSensorDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmTempSensorDevice.setStatus("current")
_OgOmTempSensorValue_Type = Integer32
_OgOmTempSensorValue_Object = MibTableColumn
ogOmTempSensorValue = _OgOmTempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 9, 1, 1, 4),
    _OgOmTempSensorValue_Type()
)
ogOmTempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOmTempSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    ogOmTempSensorValue.setUnits("millidegrees Celsius")
_OgOmConformance_ObjectIdentity = ObjectIdentity
ogOmConformance = _OgOmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 65535)
)
_OgOmCompliances_ObjectIdentity = ObjectIdentity
ogOmCompliances = _OgOmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 65535, 1)
)
_OgOmGroups_ObjectIdentity = ObjectIdentity
ogOmGroups = _OgOmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 65535, 2)
)

# Managed Objects groups

ogOmBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 65535, 2, 1)
)
ogOmBasicGroup.setObjects(
      *(("OG-OMTELEM-MIB", "ogOmSystemHostName"),
        ("OG-OMTELEM-MIB", "ogOmSystemSerialNumber"),
        ("OG-OMTELEM-MIB", "ogOmSystemFirmwareVersion"),
        ("OG-OMTELEM-MIB", "ogOmSystemVendor"),
        ("OG-OMTELEM-MIB", "ogOmSystemModel"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortCount"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortLabel"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortSpeed"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortDataBits"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortParity"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortStopBits"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortFlowControl"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortMode"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortPinout"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortLogLevel"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortRxBytes"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortTxBytes"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortFramingErrors"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortParityErrors"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortOverrunErrors"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortBreaks"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortDCD"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortDTR"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortDSR"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortCTS"),
        ("OG-OMTELEM-MIB", "ogOmSerialPortRTS"),
        ("OG-OMTELEM-MIB", "ogOmSerialUserStartTime"),
        ("OG-OMTELEM-MIB", "ogOmSerialUserPortNumber"),
        ("OG-OMTELEM-MIB", "ogOmSerialUserPortLabel"),
        ("OG-OMTELEM-MIB", "ogOmSerialUserName"),
        ("OG-OMTELEM-MIB", "ogOmWebUserStartTime"),
        ("OG-OMTELEM-MIB", "ogOmWebUserName"),
        ("OG-OMTELEM-MIB", "ogOmWebUserSourceAddress"),
        ("OG-OMTELEM-MIB", "ogOmWebUserSourcePort"),
        ("OG-OMTELEM-MIB", "ogOmCellularVendor"),
        ("OG-OMTELEM-MIB", "ogOmCellularModel"),
        ("OG-OMTELEM-MIB", "ogOmCellularEquipmentId"),
        ("OG-OMTELEM-MIB", "ogOmCellularFirmware"),
        ("OG-OMTELEM-MIB", "ogOmCellularState"),
        ("OG-OMTELEM-MIB", "ogOmCellularAccessTechnology"),
        ("OG-OMTELEM-MIB", "ogOmCellularActiveUim"),
        ("OG-OMTELEM-MIB", "ogOmCellularUimFailoverState"),
        ("OG-OMTELEM-MIB", "ogOmCellUimPhysicalSlot"),
        ("OG-OMTELEM-MIB", "ogOmCellUimSlotState"),
        ("OG-OMTELEM-MIB", "ogOmCellUimCardState"),
        ("OG-OMTELEM-MIB", "ogOmCellUimIccid"),
        ("OG-OMTELEM-MIB", "ogOmCellUimImsi"),
        ("OG-OMTELEM-MIB", "ogOmCellUimOperatorName"),
        ("OG-OMTELEM-MIB", "ogOmCellUimApn"),
        ("OG-OMTELEM-MIB", "ogOmCellUimSignalQuality"),
        ("OG-OMTELEM-MIB", "ogOmCellUimRssi"),
        ("OG-OMTELEM-MIB", "ogOmCellUimConnectivityHealth"),
        ("OG-OMTELEM-MIB", "ogOmCellUimSignalHealth"),
        ("OG-OMTELEM-MIB", "ogOmCellUimLastUpdateTime"),
        ("OG-OMTELEM-MIB", "ogOmCellUimLastActiveTime"),
        ("OG-OMTELEM-MIB", "ogOmCellUimRoamingOperatorName"),
        ("OG-OMTELEM-MIB", "ogOmEnrollmentAddress"),
        ("OG-OMTELEM-MIB", "ogOmEnrollmentPort"),
        ("OG-OMTELEM-MIB", "ogOmEnrollmentBundle"),
        ("OG-OMTELEM-MIB", "ogOmEnrollmentStatus"),
        ("OG-OMTELEM-MIB", "ogOmPowerSupplyName"),
        ("OG-OMTELEM-MIB", "ogOmPowerSupplyDevice"),
        ("OG-OMTELEM-MIB", "ogOmPowerSupplyInputVoltage"),
        ("OG-OMTELEM-MIB", "ogOmPowerSupplyOutputCurrent"),
        ("OG-OMTELEM-MIB", "ogOmPowerSupplyOutputPower"),
        ("OG-OMTELEM-MIB", "ogOmTempSensorName"),
        ("OG-OMTELEM-MIB", "ogOmTempSensorDevice"),
        ("OG-OMTELEM-MIB", "ogOmTempSensorValue"))
)
if mibBuilder.loadTexts:
    ogOmBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ogOmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 19, 65535, 1, 1)
)
ogOmCompliance.setObjects(
    ("OG-OMTELEM-MIB", "ogOmBasicGroup")
)
if mibBuilder.loadTexts:
    ogOmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-OMTELEM-MIB",
    **{"ogOmTelem": ogOmTelem,
       "ogOmSystem": ogOmSystem,
       "ogOmSystemHostName": ogOmSystemHostName,
       "ogOmSystemSerialNumber": ogOmSystemSerialNumber,
       "ogOmSystemFirmwareVersion": ogOmSystemFirmwareVersion,
       "ogOmSystemVendor": ogOmSystemVendor,
       "ogOmSystemModel": ogOmSystemModel,
       "ogOmSerialPort": ogOmSerialPort,
       "ogOmSerialPortCount": ogOmSerialPortCount,
       "ogOmSerialPortTable": ogOmSerialPortTable,
       "ogOmSerialPortEntry": ogOmSerialPortEntry,
       "ogOmSerialPortIndex": ogOmSerialPortIndex,
       "ogOmSerialPortLabel": ogOmSerialPortLabel,
       "ogOmSerialPortSpeed": ogOmSerialPortSpeed,
       "ogOmSerialPortDataBits": ogOmSerialPortDataBits,
       "ogOmSerialPortParity": ogOmSerialPortParity,
       "ogOmSerialPortStopBits": ogOmSerialPortStopBits,
       "ogOmSerialPortFlowControl": ogOmSerialPortFlowControl,
       "ogOmSerialPortMode": ogOmSerialPortMode,
       "ogOmSerialPortPinout": ogOmSerialPortPinout,
       "ogOmSerialPortLogLevel": ogOmSerialPortLogLevel,
       "ogOmSerialPortRxBytes": ogOmSerialPortRxBytes,
       "ogOmSerialPortTxBytes": ogOmSerialPortTxBytes,
       "ogOmSerialPortFramingErrors": ogOmSerialPortFramingErrors,
       "ogOmSerialPortParityErrors": ogOmSerialPortParityErrors,
       "ogOmSerialPortOverrunErrors": ogOmSerialPortOverrunErrors,
       "ogOmSerialPortBreaks": ogOmSerialPortBreaks,
       "ogOmSerialPortDCD": ogOmSerialPortDCD,
       "ogOmSerialPortDTR": ogOmSerialPortDTR,
       "ogOmSerialPortDSR": ogOmSerialPortDSR,
       "ogOmSerialPortCTS": ogOmSerialPortCTS,
       "ogOmSerialPortRTS": ogOmSerialPortRTS,
       "ogOmSerialUser": ogOmSerialUser,
       "ogOmSerialUserTable": ogOmSerialUserTable,
       "ogOmSerialUserEntry": ogOmSerialUserEntry,
       "ogOmSerialUserIndex": ogOmSerialUserIndex,
       "ogOmSerialUserStartTime": ogOmSerialUserStartTime,
       "ogOmSerialUserPortNumber": ogOmSerialUserPortNumber,
       "ogOmSerialUserPortLabel": ogOmSerialUserPortLabel,
       "ogOmSerialUserName": ogOmSerialUserName,
       "ogOmWebUser": ogOmWebUser,
       "ogOmWebUserTable": ogOmWebUserTable,
       "ogOmWebUserEntry": ogOmWebUserEntry,
       "ogOmWebUserIndex": ogOmWebUserIndex,
       "ogOmWebUserStartTime": ogOmWebUserStartTime,
       "ogOmWebUserName": ogOmWebUserName,
       "ogOmWebUserSourceAddress": ogOmWebUserSourceAddress,
       "ogOmWebUserSourcePort": ogOmWebUserSourcePort,
       "ogOmCellular": ogOmCellular,
       "ogOmCellularTable": ogOmCellularTable,
       "ogOmCellularEntry": ogOmCellularEntry,
       "ogOmCellularIndex": ogOmCellularIndex,
       "ogOmCellularVendor": ogOmCellularVendor,
       "ogOmCellularModel": ogOmCellularModel,
       "ogOmCellularEquipmentId": ogOmCellularEquipmentId,
       "ogOmCellularFirmware": ogOmCellularFirmware,
       "ogOmCellularState": ogOmCellularState,
       "ogOmCellularAccessTechnology": ogOmCellularAccessTechnology,
       "ogOmCellularActiveUim": ogOmCellularActiveUim,
       "ogOmCellularUimFailoverState": ogOmCellularUimFailoverState,
       "ogOmCellUim": ogOmCellUim,
       "ogOmCellUimTable": ogOmCellUimTable,
       "ogOmCellUimEntry": ogOmCellUimEntry,
       "ogOmCellUimIndex": ogOmCellUimIndex,
       "ogOmCellUimPhysicalSlot": ogOmCellUimPhysicalSlot,
       "ogOmCellUimSlotState": ogOmCellUimSlotState,
       "ogOmCellUimCardState": ogOmCellUimCardState,
       "ogOmCellUimIccid": ogOmCellUimIccid,
       "ogOmCellUimImsi": ogOmCellUimImsi,
       "ogOmCellUimOperatorName": ogOmCellUimOperatorName,
       "ogOmCellUimApn": ogOmCellUimApn,
       "ogOmCellUimSignalQuality": ogOmCellUimSignalQuality,
       "ogOmCellUimRssi": ogOmCellUimRssi,
       "ogOmCellUimConnectivityHealth": ogOmCellUimConnectivityHealth,
       "ogOmCellUimSignalHealth": ogOmCellUimSignalHealth,
       "ogOmCellUimLastUpdateTime": ogOmCellUimLastUpdateTime,
       "ogOmCellUimLastActiveTime": ogOmCellUimLastActiveTime,
       "ogOmCellUimRoamingOperatorName": ogOmCellUimRoamingOperatorName,
       "ogOmEnrollment": ogOmEnrollment,
       "ogOmEnrollmentTable": ogOmEnrollmentTable,
       "ogOmEnrollmentEntry": ogOmEnrollmentEntry,
       "ogOmEnrollmentIndex": ogOmEnrollmentIndex,
       "ogOmEnrollmentAddress": ogOmEnrollmentAddress,
       "ogOmEnrollmentPort": ogOmEnrollmentPort,
       "ogOmEnrollmentBundle": ogOmEnrollmentBundle,
       "ogOmEnrollmentStatus": ogOmEnrollmentStatus,
       "ogOmPowerSupply": ogOmPowerSupply,
       "ogOmPowerSupplyTable": ogOmPowerSupplyTable,
       "ogOmPowerSupplyEntry": ogOmPowerSupplyEntry,
       "ogOmPowerSupplyIndex": ogOmPowerSupplyIndex,
       "ogOmPowerSupplyName": ogOmPowerSupplyName,
       "ogOmPowerSupplyDevice": ogOmPowerSupplyDevice,
       "ogOmPowerSupplyInputVoltage": ogOmPowerSupplyInputVoltage,
       "ogOmPowerSupplyOutputCurrent": ogOmPowerSupplyOutputCurrent,
       "ogOmPowerSupplyOutputPower": ogOmPowerSupplyOutputPower,
       "ogOmTempSensor": ogOmTempSensor,
       "ogOmTempSensorTable": ogOmTempSensorTable,
       "ogOmTempSensorEntry": ogOmTempSensorEntry,
       "ogOmTempSensorIndex": ogOmTempSensorIndex,
       "ogOmTempSensorName": ogOmTempSensorName,
       "ogOmTempSensorDevice": ogOmTempSensorDevice,
       "ogOmTempSensorValue": ogOmTempSensorValue,
       "ogOmConformance": ogOmConformance,
       "ogOmCompliances": ogOmCompliances,
       "ogOmCompliance": ogOmCompliance,
       "ogOmGroups": ogOmGroups,
       "ogOmBasicGroup": ogOmBasicGroup}
)
