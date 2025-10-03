# SNMP MIB module (HP-LASERJET-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hp\HP-LASERJET-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:50:38 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
if mibBuilder.loadTexts:
    hp.setRevisions(
        ("2020-05-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpsystem_ObjectIdentity = ObjectIdentity
hpsystem = _Hpsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_Net_peripheral_ObjectIdentity = ObjectIdentity
net_peripheral = _Net_peripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9)
)
_Net_printer_ObjectIdentity = ObjectIdentity
net_printer = _Net_printer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1)
)
_GeneralDeviceStatus_ObjectIdentity = ObjectIdentity
generalDeviceStatus = _GeneralDeviceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1)
)
_GdStatusBytes_Type = Integer32
_GdStatusBytes_Object = MibScalar
gdStatusBytes = _GdStatusBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 1),
    _GdStatusBytes_Type()
)
gdStatusBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusBytes.setStatus("current")
_GdStatusEntry_ObjectIdentity = ObjectIdentity
gdStatusEntry = _GdStatusEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2)
)


class _GdStatusLineState_Type(Integer32):
    """Custom type gdStatusLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusLineState_Type.__name__ = "Integer32"
_GdStatusLineState_Object = MibScalar
gdStatusLineState = _GdStatusLineState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 1),
    _GdStatusLineState_Type()
)
gdStatusLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusLineState.setStatus("current")


class _GdStatusPaperState_Type(Integer32):
    """Custom type gdStatusPaperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusPaperState_Type.__name__ = "Integer32"
_GdStatusPaperState_Object = MibScalar
gdStatusPaperState = _GdStatusPaperState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 2),
    _GdStatusPaperState_Type()
)
gdStatusPaperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPaperState.setStatus("current")


class _GdStatusInterventionState_Type(Integer32):
    """Custom type gdStatusInterventionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusInterventionState_Type.__name__ = "Integer32"
_GdStatusInterventionState_Object = MibScalar
gdStatusInterventionState = _GdStatusInterventionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 3),
    _GdStatusInterventionState_Type()
)
gdStatusInterventionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusInterventionState.setStatus("current")


class _GdStatusNewMode_Type(Integer32):
    """Custom type gdStatusNewMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusNewMode_Type.__name__ = "Integer32"
_GdStatusNewMode_Object = MibScalar
gdStatusNewMode = _GdStatusNewMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 4),
    _GdStatusNewMode_Type()
)
gdStatusNewMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusNewMode.setStatus("obsolete")


class _GdStatusConnectionTerminationAck_Type(Integer32):
    """Custom type gdStatusConnectionTerminationAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusConnectionTerminationAck_Type.__name__ = "Integer32"
_GdStatusConnectionTerminationAck_Object = MibScalar
gdStatusConnectionTerminationAck = _GdStatusConnectionTerminationAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 5),
    _GdStatusConnectionTerminationAck_Type()
)
gdStatusConnectionTerminationAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusConnectionTerminationAck.setStatus("obsolete")


class _GdStatusPeripheralError_Type(Integer32):
    """Custom type gdStatusPeripheralError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusPeripheralError_Type.__name__ = "Integer32"
_GdStatusPeripheralError_Object = MibScalar
gdStatusPeripheralError = _GdStatusPeripheralError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 6),
    _GdStatusPeripheralError_Type()
)
gdStatusPeripheralError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPeripheralError.setStatus("current")
_GdStatusPaperOut_Type = Integer32
_GdStatusPaperOut_Object = MibScalar
gdStatusPaperOut = _GdStatusPaperOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 8),
    _GdStatusPaperOut_Type()
)
gdStatusPaperOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPaperOut.setStatus("current")
_GdStatusPaperJam_Type = Integer32
_GdStatusPaperJam_Object = MibScalar
gdStatusPaperJam = _GdStatusPaperJam_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 9),
    _GdStatusPaperJam_Type()
)
gdStatusPaperJam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPaperJam.setStatus("current")
_GdStatusTonerLow_Type = Integer32
_GdStatusTonerLow_Object = MibScalar
gdStatusTonerLow = _GdStatusTonerLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 10),
    _GdStatusTonerLow_Type()
)
gdStatusTonerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusTonerLow.setStatus("current")


class _GdStatusPagePunt_Type(Integer32):
    """Custom type gdStatusPagePunt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusPagePunt_Type.__name__ = "Integer32"
_GdStatusPagePunt_Object = MibScalar
gdStatusPagePunt = _GdStatusPagePunt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 11),
    _GdStatusPagePunt_Type()
)
gdStatusPagePunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPagePunt.setStatus("current")


class _GdStatusMemoryOut_Type(Integer32):
    """Custom type gdStatusMemoryOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusMemoryOut_Type.__name__ = "Integer32"
_GdStatusMemoryOut_Object = MibScalar
gdStatusMemoryOut = _GdStatusMemoryOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 12),
    _GdStatusMemoryOut_Type()
)
gdStatusMemoryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusMemoryOut.setStatus("current")


class _GdStatusIoActive_Type(Integer32):
    """Custom type gdStatusIoActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusIoActive_Type.__name__ = "Integer32"
_GdStatusIoActive_Object = MibScalar
gdStatusIoActive = _GdStatusIoActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 13),
    _GdStatusIoActive_Type()
)
gdStatusIoActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusIoActive.setStatus("current")


class _GdStatusBusy_Type(Integer32):
    """Custom type gdStatusBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusBusy_Type.__name__ = "Integer32"
_GdStatusBusy_Object = MibScalar
gdStatusBusy = _GdStatusBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 14),
    _GdStatusBusy_Type()
)
gdStatusBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusBusy.setStatus("current")


class _GdStatusWait_Type(Integer32):
    """Custom type gdStatusWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusWait_Type.__name__ = "Integer32"
_GdStatusWait_Object = MibScalar
gdStatusWait = _GdStatusWait_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 15),
    _GdStatusWait_Type()
)
gdStatusWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusWait.setStatus("current")
_GdStatusInitialize_Type = Integer32
_GdStatusInitialize_Object = MibScalar
gdStatusInitialize = _GdStatusInitialize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 16),
    _GdStatusInitialize_Type()
)
gdStatusInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusInitialize.setStatus("current")


class _GdStatusDoorOpen_Type(Integer32):
    """Custom type gdStatusDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusDoorOpen_Type.__name__ = "Integer32"
_GdStatusDoorOpen_Object = MibScalar
gdStatusDoorOpen = _GdStatusDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 17),
    _GdStatusDoorOpen_Type()
)
gdStatusDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusDoorOpen.setStatus("current")
_GdStatusPrinting_Type = Integer32
_GdStatusPrinting_Object = MibScalar
gdStatusPrinting = _GdStatusPrinting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 18),
    _GdStatusPrinting_Type()
)
gdStatusPrinting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPrinting.setStatus("current")
_GdStatusPaperOutput_Type = Integer32
_GdStatusPaperOutput_Object = MibScalar
gdStatusPaperOutput = _GdStatusPaperOutput_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 19),
    _GdStatusPaperOutput_Type()
)
gdStatusPaperOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPaperOutput.setStatus("current")


class _GdStatusReserved_Type(OctetString):
    """Custom type gdStatusReserved based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_GdStatusReserved_Type.__name__ = "OctetString"
_GdStatusReserved_Object = MibScalar
gdStatusReserved = _GdStatusReserved_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 20),
    _GdStatusReserved_Type()
)
gdStatusReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusReserved.setStatus("obsolete")


class _GdStatusNovBusy_Type(Integer32):
    """Custom type gdStatusNovBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusNovBusy_Type.__name__ = "Integer32"
_GdStatusNovBusy_Object = MibScalar
gdStatusNovBusy = _GdStatusNovBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 21),
    _GdStatusNovBusy_Type()
)
gdStatusNovBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusNovBusy.setStatus("obsolete")


class _GdStatusLlcBusy_Type(Integer32):
    """Custom type gdStatusLlcBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusLlcBusy_Type.__name__ = "Integer32"
_GdStatusLlcBusy_Object = MibScalar
gdStatusLlcBusy = _GdStatusLlcBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 22),
    _GdStatusLlcBusy_Type()
)
gdStatusLlcBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusLlcBusy.setStatus("obsolete")


class _GdStatusTcpBusy_Type(Integer32):
    """Custom type gdStatusTcpBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusTcpBusy_Type.__name__ = "Integer32"
_GdStatusTcpBusy_Object = MibScalar
gdStatusTcpBusy = _GdStatusTcpBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 23),
    _GdStatusTcpBusy_Type()
)
gdStatusTcpBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusTcpBusy.setStatus("obsolete")


class _GdStatusAtBusy_Type(Integer32):
    """Custom type gdStatusAtBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GdStatusAtBusy_Type.__name__ = "Integer32"
_GdStatusAtBusy_Object = MibScalar
gdStatusAtBusy = _GdStatusAtBusy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 2, 24),
    _GdStatusAtBusy_Type()
)
gdStatusAtBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusAtBusy.setStatus("obsolete")
_GdStatusDisplay_Type = DisplayString
_GdStatusDisplay_Object = MibScalar
gdStatusDisplay = _GdStatusDisplay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 3),
    _GdStatusDisplay_Type()
)
gdStatusDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusDisplay.setStatus("current")
_GdStatusJobName_Type = DisplayString
_GdStatusJobName_Object = MibScalar
gdStatusJobName = _GdStatusJobName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 4),
    _GdStatusJobName_Type()
)
gdStatusJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusJobName.setStatus("current")
_GdStatusSource_Type = DisplayString
_GdStatusSource_Object = MibScalar
gdStatusSource = _GdStatusSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 5),
    _GdStatusSource_Type()
)
gdStatusSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusSource.setStatus("current")
_GdStatusPapstatus_Type = DisplayString
_GdStatusPapstatus_Object = MibScalar
gdStatusPapstatus = _GdStatusPapstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 6),
    _GdStatusPapstatus_Type()
)
gdStatusPapstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusPapstatus.setStatus("current")
_GdStatusId_Type = DisplayString
_GdStatusId_Object = MibScalar
gdStatusId = _GdStatusId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 7),
    _GdStatusId_Type()
)
gdStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusId.setStatus("current")
_GdStatusDisplayCode_Type = Integer32
_GdStatusDisplayCode_Object = MibScalar
gdStatusDisplayCode = _GdStatusDisplayCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 8),
    _GdStatusDisplayCode_Type()
)
gdStatusDisplayCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusDisplayCode.setStatus("obsolete")
_GdStatusNlsCode_Type = Integer32
_GdStatusNlsCode_Object = MibScalar
gdStatusNlsCode = _GdStatusNlsCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 9),
    _GdStatusNlsCode_Type()
)
gdStatusNlsCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusNlsCode.setStatus("current")
_GdStatusJobTimeout_Type = Integer32
_GdStatusJobTimeout_Object = MibScalar
gdStatusJobTimeout = _GdStatusJobTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 10),
    _GdStatusJobTimeout_Type()
)
gdStatusJobTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdStatusJobTimeout.setStatus("obsolete")
_GdStatusPjlUstatus_Type = Integer32
_GdStatusPjlUstatus_Object = MibScalar
gdStatusPjlUstatus = _GdStatusPjlUstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 11),
    _GdStatusPjlUstatus_Type()
)
gdStatusPjlUstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdStatusPjlUstatus.setStatus("obsolete")
_GdStatusLaaSupport_Type = Integer32
_GdStatusLaaSupport_Object = MibScalar
gdStatusLaaSupport = _GdStatusLaaSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 12),
    _GdStatusLaaSupport_Type()
)
gdStatusLaaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdStatusLaaSupport.setStatus("current")


class _GdPasswords_Type(OctetString):
    """Custom type gdPasswords based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GdPasswords_Type.__name__ = "OctetString"
_GdPasswords_Object = MibScalar
gdPasswords = _GdPasswords_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 13),
    _GdPasswords_Type()
)
gdPasswords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdPasswords.setStatus("current")


class _GdStatusAtPrinterName_Type(OctetString):
    """Custom type gdStatusAtPrinterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GdStatusAtPrinterName_Type.__name__ = "OctetString"
_GdStatusAtPrinterName_Object = MibScalar
gdStatusAtPrinterName = _GdStatusAtPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 18),
    _GdStatusAtPrinterName_Type()
)
gdStatusAtPrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdStatusAtPrinterName.setStatus("current")


class _GdStatusAtPrinterType_Type(OctetString):
    """Custom type gdStatusAtPrinterType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GdStatusAtPrinterType_Type.__name__ = "OctetString"
_GdStatusAtPrinterType_Object = MibScalar
gdStatusAtPrinterType = _GdStatusAtPrinterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 1, 19),
    _GdStatusAtPrinterType_Type()
)
gdStatusAtPrinterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdStatusAtPrinterType.setStatus("obsolete")
_NetPrinterType_ObjectIdentity = ObjectIdentity
netPrinterType = _NetPrinterType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 1, 2)
)
_Netdm_ObjectIdentity = ObjectIdentity
netdm = _Netdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4)
)
_Dm_ObjectIdentity = ObjectIdentity
dm = _Dm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1)
)
_Device_system_ObjectIdentity = ObjectIdentity
device_system = _Device_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1)
)
_Settings_system_ObjectIdentity = ObjectIdentity
settings_system = _Settings_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1)
)
_Energy_star_Type = Integer32
_Energy_star_Object = MibScalar
energy_star = _Energy_star_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 1),
    _Energy_star_Type()
)
energy_star.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energy_star.setStatus("current")


class _Sleep_mode_Type(Integer32):
    """Custom type sleep_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Sleep_mode_Type.__name__ = "Integer32"
_Sleep_mode_Object = MibScalar
sleep_mode = _Sleep_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 2),
    _Sleep_mode_Type()
)
sleep_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleep_mode.setStatus("current")


class _Control_panel_lock_Type(Integer32):
    """Custom type control_panel_lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Control_panel_lock_Type.__name__ = "Integer32"
_Control_panel_lock_Object = MibScalar
control_panel_lock = _Control_panel_lock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 8),
    _Control_panel_lock_Type()
)
control_panel_lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control_panel_lock.setStatus("current")
_Service_password_Type = Integer32
_Service_password_Object = MibScalar
service_password = _Service_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 9),
    _Service_password_Type()
)
service_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    service_password.setStatus("current")


class _Device_cfg_download_Type(Integer32):
    """Custom type device_cfg_download based on Integer32"""
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
        *(("eCfgDownloadIdle", 1),
          ("eCfgDownloadStart", 2),
          ("eCfgDownloadActive", 3),
          ("eCfgDownloadAborted", 4),
          ("eCfgDownloadDone", 5))
    )


_Device_cfg_download_Type.__name__ = "Integer32"
_Device_cfg_download_Object = MibScalar
device_cfg_download = _Device_cfg_download_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 11),
    _Device_cfg_download_Type()
)
device_cfg_download.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_download.setStatus("current")


class _Device_cfg_download_data_type_Type(Integer32):
    """Custom type device_cfg_download_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eSpeedDials", 5),
          ("eFaxLogs", 6),
          ("eConfigPrams", 7),
          ("eJunkFaxDialStrings", 9))
    )


_Device_cfg_download_data_type_Type.__name__ = "Integer32"
_Device_cfg_download_data_type_Object = MibScalar
device_cfg_download_data_type = _Device_cfg_download_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 12),
    _Device_cfg_download_data_type_Type()
)
device_cfg_download_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_download_data_type.setStatus("current")


class _Device_cfg_upload_Type(Integer32):
    """Custom type device_cfg_upload based on Integer32"""
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
        *(("eCfgUploadIdle", 1),
          ("eCfgUploadStart", 2),
          ("eCfgUploadActive", 3),
          ("eCfgUploadAborted", 4),
          ("eCfgUploadDone", 5))
    )


_Device_cfg_upload_Type.__name__ = "Integer32"
_Device_cfg_upload_Object = MibScalar
device_cfg_upload = _Device_cfg_upload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 13),
    _Device_cfg_upload_Type()
)
device_cfg_upload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_upload.setStatus("current")


class _Device_cfg_upload_data_type_Type(Integer32):
    """Custom type device_cfg_upload_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eSpeedDials", 5),
          ("eFaxLogs", 6),
          ("eConfigPrams", 7),
          ("eJunkFaxDialStrings", 9))
    )


_Device_cfg_upload_data_type_Type.__name__ = "Integer32"
_Device_cfg_upload_data_type_Object = MibScalar
device_cfg_upload_data_type = _Device_cfg_upload_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 14),
    _Device_cfg_upload_data_type_Type()
)
device_cfg_upload_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_upload_data_type.setStatus("current")
_Download_timeout_Type = Integer32
_Download_timeout_Object = MibScalar
download_timeout = _Download_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 17),
    _Download_timeout_Type()
)
download_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    download_timeout.setStatus("current")
_Upload_timeout_Type = Integer32
_Upload_timeout_Object = MibScalar
upload_timeout = _Upload_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 18),
    _Upload_timeout_Type()
)
upload_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upload_timeout.setStatus("current")


class _Run_location_Type(Integer32):
    """Custom type run_location based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Run_location_Type.__name__ = "Integer32"
_Run_location_Object = MibScalar
run_location = _Run_location_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 21),
    _Run_location_Type()
)
run_location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    run_location.setStatus("current")


class _Date_display_Type(Integer32):
    """Custom type date_display based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eDateDisplayMMDDYY", 1),
          ("eDateDisplayDDMMYY", 2),
          ("eDateDisplayYYMMDD", 3))
    )


_Date_display_Type.__name__ = "Integer32"
_Date_display_Object = MibScalar
date_display = _Date_display_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 22),
    _Date_display_Type()
)
date_display.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date_display.setStatus("current")
_Device_cfg_param_command_Type = OctetString
_Device_cfg_param_command_Object = MibScalar
device_cfg_param_command = _Device_cfg_param_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 23),
    _Device_cfg_param_command_Type()
)
device_cfg_param_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_cfg_param_command.setStatus("current")


class _Copier_token_Type(OctetString):
    """Custom type copier_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Copier_token_Type.__name__ = "OctetString"
_Copier_token_Object = MibScalar
copier_token = _Copier_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 24),
    _Copier_token_Type()
)
copier_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    copier_token.setStatus("current")


class _Fax_upload_token_Type(OctetString):
    """Custom type fax_upload_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Fax_upload_token_Type.__name__ = "OctetString"
_Fax_upload_token_Object = MibScalar
fax_upload_token = _Fax_upload_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 26),
    _Fax_upload_token_Type()
)
fax_upload_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_upload_token.setStatus("current")


class _Fax_download_token_Type(OctetString):
    """Custom type fax_download_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Fax_download_token_Type.__name__ = "OctetString"
_Fax_download_token_Object = MibScalar
fax_download_token = _Fax_download_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 27),
    _Fax_download_token_Type()
)
fax_download_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_download_token.setStatus("current")


class _Device_config_token_Type(OctetString):
    """Custom type device_config_token based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_Device_config_token_Type.__name__ = "OctetString"
_Device_config_token_Object = MibScalar
device_config_token = _Device_config_token_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 28),
    _Device_config_token_Type()
)
device_config_token.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_config_token.setStatus("current")


class _Mono_color_switching_mode_Type(Integer32):
    """Custom type mono_color_switching_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eNeverSwitch", 1),
          ("eAlwaysSwitch", 2),
          ("eLookAheadSwitch", 3))
    )


_Mono_color_switching_mode_Type.__name__ = "Integer32"
_Mono_color_switching_mode_Object = MibScalar
mono_color_switching_mode = _Mono_color_switching_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 31),
    _Mono_color_switching_mode_Type()
)
mono_color_switching_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mono_color_switching_mode.setStatus("current")
_Device_configure_ObjectIdentity = ObjectIdentity
device_configure = _Device_configure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32)
)


class _Device_configure_print_engine_speed_Type(Integer32):
    """Custom type device_configure_print_engine_speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNormal", 1),
          ("eSlowDown1", 2))
    )


_Device_configure_print_engine_speed_Type.__name__ = "Integer32"
_Device_configure_print_engine_speed_Object = MibScalar
device_configure_print_engine_speed = _Device_configure_print_engine_speed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 5),
    _Device_configure_print_engine_speed_Type()
)
device_configure_print_engine_speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_print_engine_speed.setStatus("current")


class _Device_configure_duplexer_enabled_Type(Integer32):
    """Custom type device_configure_duplexer_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Device_configure_duplexer_enabled_Type.__name__ = "Integer32"
_Device_configure_duplexer_enabled_Object = MibScalar
device_configure_duplexer_enabled = _Device_configure_duplexer_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 8),
    _Device_configure_duplexer_enabled_Type()
)
device_configure_duplexer_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_duplexer_enabled.setStatus("current")


class _Device_configure_generic_language_prompt_Type(Integer32):
    """Custom type device_configure_generic_language_prompt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Device_configure_generic_language_prompt_Type.__name__ = "Integer32"
_Device_configure_generic_language_prompt_Object = MibScalar
device_configure_generic_language_prompt = _Device_configure_generic_language_prompt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 10),
    _Device_configure_generic_language_prompt_Type()
)
device_configure_generic_language_prompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_generic_language_prompt.setStatus("current")


class _Device_configure_generic_country_prompt_Type(Integer32):
    """Custom type device_configure_generic_country_prompt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Device_configure_generic_country_prompt_Type.__name__ = "Integer32"
_Device_configure_generic_country_prompt_Object = MibScalar
device_configure_generic_country_prompt = _Device_configure_generic_country_prompt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 11),
    _Device_configure_generic_country_prompt_Type()
)
device_configure_generic_country_prompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_generic_country_prompt.setStatus("current")


class _Device_configure_generic_country_Type(Integer32):
    """Custom type device_configure_generic_country based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              13,
              14,
              15,
              16,
              17,
              19,
              21,
              23,
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
              70,
              78,
              79,
              82,
              83,
              85,
              86,
              88,
              94,
              95,
              96,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("eKorea", 4),
          ("eIndonesia", 5),
          ("eChina", 6),
          ("eTaiwan", 7),
          ("ePhilippines", 8),
          ("eThailand", 9),
          ("eSriLanka", 10),
          ("eBrazil", 12),
          ("eCanada", 13),
          ("eMexico", 14),
          ("eUnitedStates", 15),
          ("eArgentina", 16),
          ("eChile", 17),
          ("eNewZealand", 19),
          ("eIsrael", 21),
          ("eAustralia", 23),
          ("eIndia", 25),
          ("ePakistan", 26),
          ("eMalaysia", 27),
          ("eSaudiArabia", 28),
          ("eHongKong", 29),
          ("eSingapore", 30),
          ("eUnitedKingdom", 31),
          ("eTunisia", 32),
          ("eBrunei", 33),
          ("eAustria", 34),
          ("eNetherlands", 35),
          ("eGermany", 39),
          ("eDenmark", 40),
          ("eSweden", 41),
          ("eSouthAfrica", 42),
          ("eNorway", 43),
          ("eIreland", 44),
          ("eBelgium", 45),
          ("eFinland", 46),
          ("eFrance", 47),
          ("eTurkey", 48),
          ("eGreece", 49),
          ("ePortugal", 50),
          ("eItaly", 51),
          ("eLithuania", 52),
          ("eLatvia", 53),
          ("eEstonia", 54),
          ("eSpain", 55),
          ("ePoland", 56),
          ("eBulgaria", 57),
          ("eCroatia", 58),
          ("eRomania", 59),
          ("eSlovakRepublic", 60),
          ("eCzechRepublic", 61),
          ("eHungary", 62),
          ("eUkraine", 63),
          ("eRussia", 64),
          ("eMorocco", 65),
          ("eBelarus", 66),
          ("eEgypt", 67),
          ("ePeru", 70),
          ("eJordan", 78),
          ("eLebanon", 79),
          ("eSwitzerland", 82),
          ("eVietnam", 83),
          ("eLuxemberg", 85),
          ("eNorthAfrica", 86),
          ("eUAE", 88),
          ("eCambodia", 94),
          ("eCyprus", 95),
          ("eIceland", 96),
          ("eLiechtentstein", 98),
          ("eMalta", 99))
    )


_Device_configure_generic_country_Type.__name__ = "Integer32"
_Device_configure_generic_country_Object = MibScalar
device_configure_generic_country = _Device_configure_generic_country_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 16),
    _Device_configure_generic_country_Type()
)
device_configure_generic_country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_generic_country.setStatus("current")
_Device_configure_secure_nvram_items_Type = OctetString
_Device_configure_secure_nvram_items_Object = MibScalar
device_configure_secure_nvram_items = _Device_configure_secure_nvram_items_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 17),
    _Device_configure_secure_nvram_items_Type()
)
device_configure_secure_nvram_items.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_secure_nvram_items.setStatus("current")
_Device_configure_cpe_feature_Type = OctetString
_Device_configure_cpe_feature_Object = MibScalar
device_configure_cpe_feature = _Device_configure_cpe_feature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 18),
    _Device_configure_cpe_feature_Type()
)
device_configure_cpe_feature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_cpe_feature.setStatus("current")
_Device_configure_custom_product_number_Type = OctetString
_Device_configure_custom_product_number_Object = MibScalar
device_configure_custom_product_number = _Device_configure_custom_product_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 19),
    _Device_configure_custom_product_number_Type()
)
device_configure_custom_product_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_configure_custom_product_number.setStatus("current")


class _Device_configure_preferred_boot_localization_language_Type(Integer32):
    """Custom type device_configure_preferred_boot_localization_language based on Integer32"""
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
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              44)
        )
    )
    namedValues = NamedValues(
        *(("eEnglish", 1),
          ("eFrench", 2),
          ("eGerman", 3),
          ("eSpanish", 4),
          ("eItalian", 5),
          ("eSwedish", 6),
          ("eDanish", 7),
          ("eNorwegian", 8),
          ("eDutch", 9),
          ("eFinnish", 10),
          ("ePortuguese", 12),
          ("ePolish", 13),
          ("eTurkish", 14),
          ("eTradChinese", 16),
          ("eSimpChinese", 17),
          ("eRussian", 18),
          ("eCzech", 19),
          ("eHungarian", 20),
          ("eKorean", 21),
          ("eThai", 22),
          ("eUnknownLanguage", 44))
    )


_Device_configure_preferred_boot_localization_language_Type.__name__ = "Integer32"
_Device_configure_preferred_boot_localization_language_Object = MibScalar
device_configure_preferred_boot_localization_language = _Device_configure_preferred_boot_localization_language_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 32, 20),
    _Device_configure_preferred_boot_localization_language_Type()
)
device_configure_preferred_boot_localization_language.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_configure_preferred_boot_localization_language.setStatus("current")
_Control_panel_button_press_delay_Type = Integer32
_Control_panel_button_press_delay_Object = MibScalar
control_panel_button_press_delay = _Control_panel_button_press_delay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 47),
    _Control_panel_button_press_delay_Type()
)
control_panel_button_press_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control_panel_button_press_delay.setStatus("current")
_Low_power_Type = Integer32
_Low_power_Object = MibScalar
low_power = _Low_power_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 49),
    _Low_power_Type()
)
low_power.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    low_power.setStatus("current")


class _Fuser_pressure_release_Type(Integer32):
    """Custom type fuser_pressure_release based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eDisengage", 1)
    )


_Fuser_pressure_release_Type.__name__ = "Integer32"
_Fuser_pressure_release_Object = MibScalar
fuser_pressure_release = _Fuser_pressure_release_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 53),
    _Fuser_pressure_release_Type()
)
fuser_pressure_release.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fuser_pressure_release.setStatus("current")


class _Control_panel_display_contrast_Type(Integer32):
    """Custom type control_panel_display_contrast based on Integer32"""
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
        *(("eLightest", 1),
          ("eLight", 2),
          ("eMedium", 3),
          ("eDark", 4),
          ("eDarkest", 5))
    )


_Control_panel_display_contrast_Type.__name__ = "Integer32"
_Control_panel_display_contrast_Object = MibScalar
control_panel_display_contrast = _Control_panel_display_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 73),
    _Control_panel_display_contrast_Type()
)
control_panel_display_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control_panel_display_contrast.setStatus("current")


class _Calibration_lowspeed_enable_Type(Integer32):
    """Custom type calibration_lowspeed_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisable", 1),
          ("eEnable", 2))
    )


_Calibration_lowspeed_enable_Type.__name__ = "Integer32"
_Calibration_lowspeed_enable_Object = MibScalar
calibration_lowspeed_enable = _Calibration_lowspeed_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 85),
    _Calibration_lowspeed_enable_Type()
)
calibration_lowspeed_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibration_lowspeed_enable.setStatus("current")


class _Start_engine_early_warmup_Type(Integer32):
    """Custom type start_engine_early_warmup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eValue1", 1)
    )


_Start_engine_early_warmup_Type.__name__ = "Integer32"
_Start_engine_early_warmup_Object = MibScalar
start_engine_early_warmup = _Start_engine_early_warmup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 99),
    _Start_engine_early_warmup_Type()
)
start_engine_early_warmup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    start_engine_early_warmup.setStatus("current")


class _Enable_engine_early_warmup_Type(Integer32):
    """Custom type enable_engine_early_warmup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisable", 1),
          ("eEnable", 2))
    )


_Enable_engine_early_warmup_Type.__name__ = "Integer32"
_Enable_engine_early_warmup_Object = MibScalar
enable_engine_early_warmup = _Enable_engine_early_warmup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 1, 101),
    _Enable_engine_early_warmup_Type()
)
enable_engine_early_warmup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable_engine_early_warmup.setStatus("current")
_Status_system_ObjectIdentity = ObjectIdentity
status_system = _Status_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2)
)


class _Localization_language_Type(Integer32):
    """Custom type localization_language based on Integer32"""
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
        *(("eEnglish", 1),
          ("eFrench", 2),
          ("eGerman", 3),
          ("eSpanish", 4),
          ("eItalian", 5),
          ("eSwedish", 6),
          ("eDanish", 7),
          ("eNorwegian", 8),
          ("eDutch", 9),
          ("eFinnish", 10),
          ("eJapanese", 11),
          ("ePortuguese", 12),
          ("ePolish", 13),
          ("eTurkish", 14))
    )


_Localization_language_Type.__name__ = "Integer32"
_Localization_language_Object = MibScalar
localization_language = _Localization_language_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 1),
    _Localization_language_Type()
)
localization_language.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localization_language.setStatus("current")
_Not_ready_printer_Type = OctetString
_Not_ready_printer_Object = MibScalar
not_ready_printer = _Not_ready_printer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 2),
    _Not_ready_printer_Type()
)
not_ready_printer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_printer.setStatus("current")
_Not_ready_controller_Type = OctetString
_Not_ready_controller_Object = MibScalar
not_ready_controller = _Not_ready_controller_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 3),
    _Not_ready_controller_Type()
)
not_ready_controller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_controller.setStatus("current")
_Not_idle_Type = OctetString
_Not_idle_Object = MibScalar
not_idle = _Not_idle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 4),
    _Not_idle_Type()
)
not_idle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_idle.setStatus("current")


class _On_off_line_Type(Integer32):
    """Custom type on_off_line based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOnline", 1),
          ("eOffline", 2),
          ("eOfflineAtEndOfJob", 3))
    )


_On_off_line_Type.__name__ = "Integer32"
_On_off_line_Object = MibScalar
on_off_line = _On_off_line_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 5),
    _On_off_line_Type()
)
on_off_line.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    on_off_line.setStatus("current")


class __pysmi_continue_Type(Integer32):
    """Custom type _pysmi_continue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eInitiateAction", 1)
    )


__pysmi_continue_Type.__name__ = "Integer32"
__pysmi_continue_Object = MibScalar
_pysmi_continue = __pysmi_continue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 6),
    __pysmi_continue_Type()
)
_pysmi_continue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    _pysmi_continue.setStatus("current")


class _Auto_continue_Type(Integer32):
    """Custom type auto_continue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Auto_continue_Type.__name__ = "Integer32"
_Auto_continue_Object = MibScalar
auto_continue = _Auto_continue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 7),
    _Auto_continue_Type()
)
auto_continue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auto_continue.setStatus("current")
_Install_date_Type = DisplayString
_Install_date_Object = MibScalar
install_date = _Install_date_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 8),
    _Install_date_Type()
)
install_date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    install_date.setStatus("current")


class _User_nvram_reset_Type(Integer32):
    """Custom type user_nvram_reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eTrue", 1)
    )


_User_nvram_reset_Type.__name__ = "Integer32"
_User_nvram_reset_Object = MibScalar
user_nvram_reset = _User_nvram_reset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 12),
    _User_nvram_reset_Type()
)
user_nvram_reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    user_nvram_reset.setStatus("current")
_Date_and_time_Type = DisplayString
_Date_and_time_Object = MibScalar
date_and_time = _Date_and_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 17),
    _Date_and_time_Type()
)
date_and_time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date_and_time.setStatus("current")
_Display_ObjectIdentity = ObjectIdentity
display = _Display_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20)
)
_Display_status_ObjectIdentity = ObjectIdentity
display_status = _Display_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 1)
)
_Display_column_size_Type = Integer32
_Display_column_size_Object = MibScalar
display_column_size = _Display_column_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 1, 1),
    _Display_column_size_Type()
)
display_column_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    display_column_size.setStatus("current")
_Display_number_of_rows_Type = Integer32
_Display_number_of_rows_Object = MibScalar
display_number_of_rows = _Display_number_of_rows_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 1, 2),
    _Display_number_of_rows_Type()
)
display_number_of_rows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    display_number_of_rows.setStatus("current")


class _Show_address_Type(Integer32):
    """Custom type show_address based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eAuto", 3))
    )


_Show_address_Type.__name__ = "Integer32"
_Show_address_Object = MibScalar
show_address = _Show_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 1, 3),
    _Show_address_Type()
)
show_address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    show_address.setStatus("current")
_Status_message_ObjectIdentity = ObjectIdentity
status_message = _Status_message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 2)
)
_Status_message1_ObjectIdentity = ObjectIdentity
status_message1 = _Status_message1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 2, 1)
)
_Status_msg_line1_part1_Type = DisplayString
_Status_msg_line1_part1_Object = MibScalar
status_msg_line1_part1 = _Status_msg_line1_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 20, 2, 1, 1),
    _Status_msg_line1_part1_Type()
)
status_msg_line1_part1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_msg_line1_part1.setStatus("current")
_Total_ram_size_Type = Integer32
_Total_ram_size_Object = MibScalar
total_ram_size = _Total_ram_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 21),
    _Total_ram_size_Type()
)
total_ram_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    total_ram_size.setStatus("current")
_Status_printer_Type = OctetString
_Status_printer_Object = MibScalar
status_printer = _Status_printer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 22),
    _Status_printer_Type()
)
status_printer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_printer.setStatus("current")
_Status_controller_Type = OctetString
_Status_controller_Object = MibScalar
status_controller = _Status_controller_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 23),
    _Status_controller_Type()
)
status_controller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_controller.setStatus("current")


class _Time_display_Type(Integer32):
    """Custom type time_display based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eTimeDisplayTwelveHour", 1),
          ("eTimeDisplayTwentyFourHour", 2))
    )


_Time_display_Type.__name__ = "Integer32"
_Time_display_Object = MibScalar
time_display = _Time_display_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 28),
    _Time_display_Type()
)
time_display.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time_display.setStatus("current")


class _Job_input_auto_continue_timeout_Type(Integer32):
    """Custom type job_input_auto_continue_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_Job_input_auto_continue_timeout_Type.__name__ = "Integer32"
_Job_input_auto_continue_timeout_Object = MibScalar
job_input_auto_continue_timeout = _Job_input_auto_continue_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 35),
    _Job_input_auto_continue_timeout_Type()
)
job_input_auto_continue_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_input_auto_continue_timeout.setStatus("current")
_Job_input_auto_continue_mode_Type = OctetString
_Job_input_auto_continue_mode_Object = MibScalar
job_input_auto_continue_mode = _Job_input_auto_continue_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 36),
    _Job_input_auto_continue_mode_Type()
)
job_input_auto_continue_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_input_auto_continue_mode.setStatus("current")
_Background_message_ObjectIdentity = ObjectIdentity
background_message = _Background_message_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37)
)
_Background_message1_ObjectIdentity = ObjectIdentity
background_message1 = _Background_message1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 1)
)


class _Background_status_msg_line1_part1_Type(DisplayString):
    """Custom type background_status_msg_line1_part1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line1_part1_Type.__name__ = "DisplayString"
_Background_status_msg_line1_part1_Object = MibScalar
background_status_msg_line1_part1 = _Background_status_msg_line1_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 1, 1),
    _Background_status_msg_line1_part1_Type()
)
background_status_msg_line1_part1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_line1_part1.setStatus("current")
_Background_message2_ObjectIdentity = ObjectIdentity
background_message2 = _Background_message2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 2)
)


class _Background_status_msg_line2_part1_Type(DisplayString):
    """Custom type background_status_msg_line2_part1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Background_status_msg_line2_part1_Type.__name__ = "DisplayString"
_Background_status_msg_line2_part1_Object = MibScalar
background_status_msg_line2_part1 = _Background_status_msg_line2_part1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 37, 2, 1),
    _Background_status_msg_line2_part1_Type()
)
background_status_msg_line2_part1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    background_status_msg_line2_part1.setStatus("current")


class _Error_log_clear_Type(Integer32):
    """Custom type error_log_clear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eClearErrorLog", 1)
    )


_Error_log_clear_Type.__name__ = "Integer32"
_Error_log_clear_Object = MibScalar
error_log_clear = _Error_log_clear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 38),
    _Error_log_clear_Type()
)
error_log_clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    error_log_clear.setStatus("current")


class _Job_output_auto_continue_timeout_Type(Integer32):
    """Custom type job_output_auto_continue_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_Job_output_auto_continue_timeout_Type.__name__ = "Integer32"
_Job_output_auto_continue_timeout_Object = MibScalar
job_output_auto_continue_timeout = _Job_output_auto_continue_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 40),
    _Job_output_auto_continue_timeout_Type()
)
job_output_auto_continue_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    job_output_auto_continue_timeout.setStatus("current")
_Collated_originals_support_Type = OctetString
_Collated_originals_support_Object = MibScalar
collated_originals_support = _Collated_originals_support_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 42),
    _Collated_originals_support_Type()
)
collated_originals_support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    collated_originals_support.setStatus("current")
_Device_cfg_download_error_Type = Integer32
_Device_cfg_download_error_Object = MibScalar
device_cfg_download_error = _Device_cfg_download_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 43),
    _Device_cfg_download_error_Type()
)
device_cfg_download_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_cfg_download_error.setStatus("current")
_Device_cfg_upload_error_Type = Integer32
_Device_cfg_upload_error_Object = MibScalar
device_cfg_upload_error = _Device_cfg_upload_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 45),
    _Device_cfg_upload_error_Type()
)
device_cfg_upload_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_cfg_upload_error.setStatus("current")
_Localization_languages_supported_Type = DisplayString
_Localization_languages_supported_Object = MibScalar
localization_languages_supported = _Localization_languages_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 52),
    _Localization_languages_supported_Type()
)
localization_languages_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localization_languages_supported.setStatus("current")
_Localization_countries_supported_Type = DisplayString
_Localization_countries_supported_Object = MibScalar
localization_countries_supported = _Localization_countries_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 53),
    _Localization_countries_supported_Type()
)
localization_countries_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localization_countries_supported.setStatus("current")
_Host_application_available_memory_Type = Integer32
_Host_application_available_memory_Object = MibScalar
host_application_available_memory = _Host_application_available_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 59),
    _Host_application_available_memory_Type()
)
host_application_available_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    host_application_available_memory.setStatus("current")


class _Control_panel_button_press_Type(Integer32):
    """Custom type control_panel_button_press based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eGoButton", 1),
          ("eMenuPlusButton", 2),
          ("eMenuMinusButton", 3),
          ("eItemPlusButton", 4),
          ("eItemMinusButton", 5),
          ("eValuePlusButton", 6),
          ("eValueMinusButton", 7),
          ("eSelectButton", 8),
          ("eCancelJobButton", 9))
    )


_Control_panel_button_press_Type.__name__ = "Integer32"
_Control_panel_button_press_Object = MibScalar
control_panel_button_press = _Control_panel_button_press_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 60),
    _Control_panel_button_press_Type()
)
control_panel_button_press.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control_panel_button_press.setStatus("current")
_Control_panel_display_ObjectIdentity = ObjectIdentity
control_panel_display = _Control_panel_display_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 65)
)


class _Ship_cartridge_installed_in_printer_Type(Integer32):
    """Custom type ship_cartridge_installed_in_printer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Ship_cartridge_installed_in_printer_Type.__name__ = "Integer32"
_Ship_cartridge_installed_in_printer_Object = MibScalar
ship_cartridge_installed_in_printer = _Ship_cartridge_installed_in_printer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 97),
    _Ship_cartridge_installed_in_printer_Type()
)
ship_cartridge_installed_in_printer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ship_cartridge_installed_in_printer.setStatus("current")
_Device_mac_address_Type = DisplayString
_Device_mac_address_Object = MibScalar
device_mac_address = _Device_mac_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 120),
    _Device_mac_address_Type()
)
device_mac_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_mac_address.setStatus("current")


class _Extended_print_modes_modified_Type(Integer32):
    """Custom type extended_print_modes_modified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eYes", 1),
          ("eNo", 2))
    )


_Extended_print_modes_modified_Type.__name__ = "Integer32"
_Extended_print_modes_modified_Object = MibScalar
extended_print_modes_modified = _Extended_print_modes_modified_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 2, 121),
    _Extended_print_modes_modified_Type()
)
extended_print_modes_modified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extended_print_modes_modified.setStatus("current")
_Id_ObjectIdentity = ObjectIdentity
id = _Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3)
)
_Model_number_Type = DisplayString
_Model_number_Object = MibScalar
model_number = _Model_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 1),
    _Model_number_Type()
)
model_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_number.setStatus("current")


class _Model_name_Type(DisplayString):
    """Custom type model_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Model_name_Type.__name__ = "DisplayString"
_Model_name_Object = MibScalar
model_name = _Model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 2),
    _Model_name_Type()
)
model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model_name.setStatus("current")


class _Serial_number_Type(DisplayString):
    """Custom type serial_number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Serial_number_Type.__name__ = "DisplayString"
_Serial_number_Object = MibScalar
serial_number = _Serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 3),
    _Serial_number_Type()
)
serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serial_number.setStatus("current")
_Fw_rom_datecode_Type = DisplayString
_Fw_rom_datecode_Object = MibScalar
fw_rom_datecode = _Fw_rom_datecode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 5),
    _Fw_rom_datecode_Type()
)
fw_rom_datecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_datecode.setStatus("current")
_Fw_rom_revision_Type = DisplayString
_Fw_rom_revision_Object = MibScalar
fw_rom_revision = _Fw_rom_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 6),
    _Fw_rom_revision_Type()
)
fw_rom_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fw_rom_revision.setStatus("current")
_Fax_local_phone_num_Type = OctetString
_Fax_local_phone_num_Object = MibScalar
fax_local_phone_num = _Fax_local_phone_num_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 8),
    _Fax_local_phone_num_Type()
)
fax_local_phone_num.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_local_phone_num.setStatus("current")
_Fax_station_name_Type = DisplayString
_Fax_station_name_Object = MibScalar
fax_station_name = _Fax_station_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 9),
    _Fax_station_name_Type()
)
fax_station_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_station_name.setStatus("current")


class _Device_name_Type(DisplayString):
    """Custom type device_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Device_name_Type.__name__ = "DisplayString"
_Device_name_Object = MibScalar
device_name = _Device_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 10),
    _Device_name_Type()
)
device_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_name.setStatus("current")
_Device_location_Type = DisplayString
_Device_location_Object = MibScalar
device_location = _Device_location_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 11),
    _Device_location_Type()
)
device_location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_location.setStatus("current")
_Asset_number_Type = DisplayString
_Asset_number_Object = MibScalar
asset_number = _Asset_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 12),
    _Asset_number_Type()
)
asset_number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asset_number.setStatus("current")
_System_contact_Type = DisplayString
_System_contact_Object = MibScalar
system_contact = _System_contact_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 13),
    _System_contact_Type()
)
system_contact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    system_contact.setStatus("current")


class _Fax_line_interface_unit_id_Type(Integer32):
    """Custom type fax_line_interface_unit_id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Fax_line_interface_unit_id_Type.__name__ = "Integer32"
_Fax_line_interface_unit_id_Object = MibScalar
fax_line_interface_unit_id = _Fax_line_interface_unit_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 3, 18),
    _Fax_line_interface_unit_id_Type()
)
fax_line_interface_unit_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_line_interface_unit_id.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4)
)
_Simm_ObjectIdentity = ObjectIdentity
simm = _Simm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1)
)
_Simm1_ObjectIdentity = ObjectIdentity
simm1 = _Simm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1)
)


class _Simm1_type_Type(Integer32):
    """Custom type simm1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5),
          ("eFlashMemory", 7),
          ("eRamRom", 9))
    )


_Simm1_type_Type.__name__ = "Integer32"
_Simm1_type_Object = MibScalar
simm1_type = _Simm1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 4),
    _Simm1_type_Type()
)
simm1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_type.setStatus("current")
_Simm1_capacity_Type = Integer32
_Simm1_capacity_Object = MibScalar
simm1_capacity = _Simm1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 5),
    _Simm1_capacity_Type()
)
simm1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_capacity.setStatus("current")
_Simm1_bank_ObjectIdentity = ObjectIdentity
simm1_bank = _Simm1_bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6)
)
_Simm1_bank1_ObjectIdentity = ObjectIdentity
simm1_bank1 = _Simm1_bank1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 1)
)


class _Simm1_bank1_type_Type(Integer32):
    """Custom type simm1_bank1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eFlashMemory", 7),
          ("eSDRandomAccessMemory", 14),
          ("eSRandomAccessMemory", 15),
          ("eFPMRandomAccessMemory", 16),
          ("eEDORandomAccessMemory", 17))
    )


_Simm1_bank1_type_Type.__name__ = "Integer32"
_Simm1_bank1_type_Object = MibScalar
simm1_bank1_type = _Simm1_bank1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 1, 1),
    _Simm1_bank1_type_Type()
)
simm1_bank1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank1_type.setStatus("current")
_Simm1_bank1_capacity_Type = Integer32
_Simm1_bank1_capacity_Object = MibScalar
simm1_bank1_capacity = _Simm1_bank1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 1, 2),
    _Simm1_bank1_capacity_Type()
)
simm1_bank1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank1_capacity.setStatus("current")
_Simm1_bank2_ObjectIdentity = ObjectIdentity
simm1_bank2 = _Simm1_bank2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 2)
)


class _Simm1_bank2_type_Type(Integer32):
    """Custom type simm1_bank2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eFlashMemory", 7),
          ("eSDRandomAccessMemory", 14),
          ("eSRandomAccessMemory", 15),
          ("eFPMRandomAccessMemory", 16),
          ("eEDORandomAccessMemory", 17))
    )


_Simm1_bank2_type_Type.__name__ = "Integer32"
_Simm1_bank2_type_Object = MibScalar
simm1_bank2_type = _Simm1_bank2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 2, 1),
    _Simm1_bank2_type_Type()
)
simm1_bank2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank2_type.setStatus("current")
_Simm1_bank2_capacity_Type = Integer32
_Simm1_bank2_capacity_Object = MibScalar
simm1_bank2_capacity = _Simm1_bank2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 1, 6, 2, 2),
    _Simm1_bank2_capacity_Type()
)
simm1_bank2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm1_bank2_capacity.setStatus("current")
_Simm2_ObjectIdentity = ObjectIdentity
simm2 = _Simm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2)
)


class _Simm2_type_Type(Integer32):
    """Custom type simm2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5),
          ("eFlashMemory", 7),
          ("eRamRom", 9))
    )


_Simm2_type_Type.__name__ = "Integer32"
_Simm2_type_Object = MibScalar
simm2_type = _Simm2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 4),
    _Simm2_type_Type()
)
simm2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_type.setStatus("current")
_Simm2_capacity_Type = Integer32
_Simm2_capacity_Object = MibScalar
simm2_capacity = _Simm2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 5),
    _Simm2_capacity_Type()
)
simm2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_capacity.setStatus("current")
_Simm2_bank_ObjectIdentity = ObjectIdentity
simm2_bank = _Simm2_bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6)
)
_Simm2_bank1_ObjectIdentity = ObjectIdentity
simm2_bank1 = _Simm2_bank1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 1)
)


class _Simm2_bank1_type_Type(Integer32):
    """Custom type simm2_bank1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eFlashMemory", 7),
          ("eSDRandomAccessMemory", 14),
          ("eSRandomAccessMemory", 15),
          ("eFPMRandomAccessMemory", 16),
          ("eEDORandomAccessMemory", 17))
    )


_Simm2_bank1_type_Type.__name__ = "Integer32"
_Simm2_bank1_type_Object = MibScalar
simm2_bank1_type = _Simm2_bank1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 1, 1),
    _Simm2_bank1_type_Type()
)
simm2_bank1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank1_type.setStatus("current")
_Simm2_bank1_capacity_Type = Integer32
_Simm2_bank1_capacity_Object = MibScalar
simm2_bank1_capacity = _Simm2_bank1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 1, 2),
    _Simm2_bank1_capacity_Type()
)
simm2_bank1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank1_capacity.setStatus("current")
_Simm2_bank2_ObjectIdentity = ObjectIdentity
simm2_bank2 = _Simm2_bank2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 2)
)


class _Simm2_bank2_type_Type(Integer32):
    """Custom type simm2_bank2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eFlashMemory", 7),
          ("eSDRandomAccessMemory", 14),
          ("eSRandomAccessMemory", 15),
          ("eFPMRandomAccessMemory", 16),
          ("eEDORandomAccessMemory", 17))
    )


_Simm2_bank2_type_Type.__name__ = "Integer32"
_Simm2_bank2_type_Object = MibScalar
simm2_bank2_type = _Simm2_bank2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 2, 1),
    _Simm2_bank2_type_Type()
)
simm2_bank2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank2_type.setStatus("current")
_Simm2_bank2_capacity_Type = Integer32
_Simm2_bank2_capacity_Object = MibScalar
simm2_bank2_capacity = _Simm2_bank2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 2, 6, 2, 2),
    _Simm2_bank2_capacity_Type()
)
simm2_bank2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm2_bank2_capacity.setStatus("current")
_Simm3_ObjectIdentity = ObjectIdentity
simm3 = _Simm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3)
)


class _Simm3_type_Type(Integer32):
    """Custom type simm3_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5),
          ("eFlashMemory", 7),
          ("eRamRom", 9))
    )


_Simm3_type_Type.__name__ = "Integer32"
_Simm3_type_Object = MibScalar
simm3_type = _Simm3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 4),
    _Simm3_type_Type()
)
simm3_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_type.setStatus("current")
_Simm3_capacity_Type = Integer32
_Simm3_capacity_Object = MibScalar
simm3_capacity = _Simm3_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 5),
    _Simm3_capacity_Type()
)
simm3_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_capacity.setStatus("current")
_Simm3_bank_ObjectIdentity = ObjectIdentity
simm3_bank = _Simm3_bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6)
)
_Simm3_bank1_ObjectIdentity = ObjectIdentity
simm3_bank1 = _Simm3_bank1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 1)
)


class _Simm3_bank1_type_Type(Integer32):
    """Custom type simm3_bank1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eFlashMemory", 7),
          ("eSDRandomAccessMemory", 14),
          ("eSRandomAccessMemory", 15),
          ("eFPMRandomAccessMemory", 16),
          ("eEDORandomAccessMemory", 17))
    )


_Simm3_bank1_type_Type.__name__ = "Integer32"
_Simm3_bank1_type_Object = MibScalar
simm3_bank1_type = _Simm3_bank1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 1, 1),
    _Simm3_bank1_type_Type()
)
simm3_bank1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank1_type.setStatus("current")
_Simm3_bank1_capacity_Type = Integer32
_Simm3_bank1_capacity_Object = MibScalar
simm3_bank1_capacity = _Simm3_bank1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 1, 2),
    _Simm3_bank1_capacity_Type()
)
simm3_bank1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank1_capacity.setStatus("current")
_Simm3_bank2_ObjectIdentity = ObjectIdentity
simm3_bank2 = _Simm3_bank2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 2)
)


class _Simm3_bank2_type_Type(Integer32):
    """Custom type simm3_bank2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eFlashMemory", 7),
          ("eSDRandomAccessMemory", 14),
          ("eSRandomAccessMemory", 15),
          ("eFPMRandomAccessMemory", 16),
          ("eEDORandomAccessMemory", 17))
    )


_Simm3_bank2_type_Type.__name__ = "Integer32"
_Simm3_bank2_type_Object = MibScalar
simm3_bank2_type = _Simm3_bank2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 2, 1),
    _Simm3_bank2_type_Type()
)
simm3_bank2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank2_type.setStatus("current")
_Simm3_bank2_capacity_Type = Integer32
_Simm3_bank2_capacity_Object = MibScalar
simm3_bank2_capacity = _Simm3_bank2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 3, 6, 2, 2),
    _Simm3_bank2_capacity_Type()
)
simm3_bank2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm3_bank2_capacity.setStatus("current")
_Simm4_ObjectIdentity = ObjectIdentity
simm4 = _Simm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4)
)


class _Simm4_type_Type(Integer32):
    """Custom type simm4_type based on Integer32"""
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
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm4_type_Type.__name__ = "Integer32"
_Simm4_type_Object = MibScalar
simm4_type = _Simm4_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 4),
    _Simm4_type_Type()
)
simm4_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_type.setStatus("current")
_Simm4_capacity_Type = Integer32
_Simm4_capacity_Object = MibScalar
simm4_capacity = _Simm4_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 4, 5),
    _Simm4_capacity_Type()
)
simm4_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm4_capacity.setStatus("current")
_Simm5_ObjectIdentity = ObjectIdentity
simm5 = _Simm5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 5)
)


class _Simm5_type_Type(Integer32):
    """Custom type simm5_type based on Integer32"""
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
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm5_type_Type.__name__ = "Integer32"
_Simm5_type_Object = MibScalar
simm5_type = _Simm5_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 5, 4),
    _Simm5_type_Type()
)
simm5_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm5_type.setStatus("current")
_Simm5_capacity_Type = Integer32
_Simm5_capacity_Object = MibScalar
simm5_capacity = _Simm5_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 5, 5),
    _Simm5_capacity_Type()
)
simm5_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm5_capacity.setStatus("current")
_Simm6_ObjectIdentity = ObjectIdentity
simm6 = _Simm6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 6)
)


class _Simm6_type_Type(Integer32):
    """Custom type simm6_type based on Integer32"""
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
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm6_type_Type.__name__ = "Integer32"
_Simm6_type_Object = MibScalar
simm6_type = _Simm6_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 6, 4),
    _Simm6_type_Type()
)
simm6_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm6_type.setStatus("current")
_Simm6_capacity_Type = Integer32
_Simm6_capacity_Object = MibScalar
simm6_capacity = _Simm6_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 6, 5),
    _Simm6_capacity_Type()
)
simm6_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm6_capacity.setStatus("current")
_Simm7_ObjectIdentity = ObjectIdentity
simm7 = _Simm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 7)
)


class _Simm7_type_Type(Integer32):
    """Custom type simm7_type based on Integer32"""
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
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm7_type_Type.__name__ = "Integer32"
_Simm7_type_Object = MibScalar
simm7_type = _Simm7_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 7, 4),
    _Simm7_type_Type()
)
simm7_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm7_type.setStatus("current")
_Simm7_capacity_Type = Integer32
_Simm7_capacity_Object = MibScalar
simm7_capacity = _Simm7_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 7, 5),
    _Simm7_capacity_Type()
)
simm7_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm7_capacity.setStatus("current")
_Simm8_ObjectIdentity = ObjectIdentity
simm8 = _Simm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 8)
)


class _Simm8_type_Type(Integer32):
    """Custom type simm8_type based on Integer32"""
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
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5))
    )


_Simm8_type_Type.__name__ = "Integer32"
_Simm8_type_Object = MibScalar
simm8_type = _Simm8_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 8, 4),
    _Simm8_type_Type()
)
simm8_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm8_type.setStatus("current")
_Simm8_capacity_Type = Integer32
_Simm8_capacity_Object = MibScalar
simm8_capacity = _Simm8_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 1, 8, 5),
    _Simm8_capacity_Type()
)
simm8_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    simm8_capacity.setStatus("current")
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 2)
)
_At1_ObjectIdentity = ObjectIdentity
at1 = _At1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 2, 1)
)
_At1_model_number_Type = DisplayString
_At1_model_number_Object = MibScalar
at1_model_number = _At1_model_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 2, 1, 1),
    _At1_model_number_Type()
)
at1_model_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at1_model_number.setStatus("current")
_At1_model_name_Type = DisplayString
_At1_model_name_Object = MibScalar
at1_model_name = _At1_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 2, 1, 2),
    _At1_model_name_Type()
)
at1_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at1_model_name.setStatus("current")
_At1_manufacturing_info_Type = DisplayString
_At1_manufacturing_info_Object = MibScalar
at1_manufacturing_info = _At1_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 2, 1, 3),
    _At1_manufacturing_info_Type()
)
at1_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at1_manufacturing_info.setStatus("current")


class _At1_type_Type(Integer32):
    """Custom type at1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eDiskDrive", 8))
    )


_At1_type_Type.__name__ = "Integer32"
_At1_type_Object = MibScalar
at1_type = _At1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 2, 1, 4),
    _At1_type_Type()
)
at1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at1_type.setStatus("current")
_At1_capacity_Type = Integer32
_At1_capacity_Object = MibScalar
at1_capacity = _At1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 2, 1, 5),
    _At1_capacity_Type()
)
at1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    at1_capacity.setStatus("current")
_Mio_ObjectIdentity = ObjectIdentity
mio = _Mio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3)
)
_Mio1_ObjectIdentity = ObjectIdentity
mio1 = _Mio1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1)
)
_Mio1_model_name_Type = DisplayString
_Mio1_model_name_Object = MibScalar
mio1_model_name = _Mio1_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 2),
    _Mio1_model_name_Type()
)
mio1_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio1_model_name.setStatus("current")
_Mio1_manufacturing_info_Type = DisplayString
_Mio1_manufacturing_info_Object = MibScalar
mio1_manufacturing_info = _Mio1_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 3),
    _Mio1_manufacturing_info_Type()
)
mio1_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio1_manufacturing_info.setStatus("current")


class _Mio1_type_Type(Integer32):
    """Custom type mio1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eDiskDrive", 8),
          ("eIOCard", 12))
    )


_Mio1_type_Type.__name__ = "Integer32"
_Mio1_type_Object = MibScalar
mio1_type = _Mio1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 1, 4),
    _Mio1_type_Type()
)
mio1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio1_type.setStatus("current")
_Mio2_ObjectIdentity = ObjectIdentity
mio2 = _Mio2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2)
)
_Mio2_model_name_Type = DisplayString
_Mio2_model_name_Object = MibScalar
mio2_model_name = _Mio2_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2, 2),
    _Mio2_model_name_Type()
)
mio2_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio2_model_name.setStatus("current")
_Mio2_manufacturing_info_Type = DisplayString
_Mio2_manufacturing_info_Object = MibScalar
mio2_manufacturing_info = _Mio2_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2, 3),
    _Mio2_manufacturing_info_Type()
)
mio2_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio2_manufacturing_info.setStatus("current")


class _Mio2_type_Type(Integer32):
    """Custom type mio2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eDiskDrive", 8),
          ("eIOCard", 12))
    )


_Mio2_type_Type.__name__ = "Integer32"
_Mio2_type_Object = MibScalar
mio2_type = _Mio2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 2, 4),
    _Mio2_type_Type()
)
mio2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio2_type.setStatus("current")
_Mio3_ObjectIdentity = ObjectIdentity
mio3 = _Mio3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3)
)
_Mio3_model_name_Type = DisplayString
_Mio3_model_name_Object = MibScalar
mio3_model_name = _Mio3_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3, 2),
    _Mio3_model_name_Type()
)
mio3_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio3_model_name.setStatus("current")
_Mio3_manufacturing_info_Type = DisplayString
_Mio3_manufacturing_info_Object = MibScalar
mio3_manufacturing_info = _Mio3_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3, 3),
    _Mio3_manufacturing_info_Type()
)
mio3_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio3_manufacturing_info.setStatus("current")


class _Mio3_type_Type(Integer32):
    """Custom type mio3_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eDiskDrive", 8),
          ("eIOCard", 12))
    )


_Mio3_type_Type.__name__ = "Integer32"
_Mio3_type_Object = MibScalar
mio3_type = _Mio3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 3, 4),
    _Mio3_type_Type()
)
mio3_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio3_type.setStatus("current")
_Mio4_ObjectIdentity = ObjectIdentity
mio4 = _Mio4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4)
)
_Mio4_model_name_Type = OctetString
_Mio4_model_name_Object = MibScalar
mio4_model_name = _Mio4_model_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4, 2),
    _Mio4_model_name_Type()
)
mio4_model_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio4_model_name.setStatus("current")
_Mio4_manufacturing_info_Type = OctetString
_Mio4_manufacturing_info_Object = MibScalar
mio4_manufacturing_info = _Mio4_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4, 3),
    _Mio4_manufacturing_info_Type()
)
mio4_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio4_manufacturing_info.setStatus("current")


class _Mio4_type_Type(Integer32):
    """Custom type mio4_type based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eUnknown", 2),
          ("eUnSupported", 3),
          ("eReadOnlyMemory", 4),
          ("eVolatileRandomAccessMemory", 5),
          ("eNonVolatileRandomAccessMemory", 6),
          ("eFlashMemory", 7),
          ("eDiskDrive", 8),
          ("eRamRom", 9),
          ("eInputPHD", 10),
          ("eOutputPHD", 11),
          ("eIOCard", 12),
          ("eBindingPHD", 13),
          ("eSDRandomAccessMemory", 14),
          ("eSRandomAccessMemory", 15),
          ("eFPMRandomAccessMemory", 16),
          ("eEDORandomAccessMemory", 17))
    )


_Mio4_type_Type.__name__ = "Integer32"
_Mio4_type_Object = MibScalar
mio4_type = _Mio4_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 3, 4, 4),
    _Mio4_type_Type()
)
mio4_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mio4_type.setStatus("current")
_Phd_ObjectIdentity = ObjectIdentity
phd = _Phd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5)
)
_Phd1_ObjectIdentity = ObjectIdentity
phd1 = _Phd1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1)
)
_Phd1_model_Type = DisplayString
_Phd1_model_Object = MibScalar
phd1_model = _Phd1_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 1),
    _Phd1_model_Type()
)
phd1_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_model.setStatus("current")
_Phd1_manufacturing_info_Type = DisplayString
_Phd1_manufacturing_info_Object = MibScalar
phd1_manufacturing_info = _Phd1_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 2),
    _Phd1_manufacturing_info_Type()
)
phd1_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_manufacturing_info.setStatus("current")


class _Phd1_type_Type(Integer32):
    """Custom type phd1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eEmpty", 1),
          ("eInputPHD", 10))
    )


_Phd1_type_Type.__name__ = "Integer32"
_Phd1_type_Object = MibScalar
phd1_type = _Phd1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 3),
    _Phd1_type_Type()
)
phd1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_type.setStatus("current")
_Phd1_capacity_Type = Integer32
_Phd1_capacity_Object = MibScalar
phd1_capacity = _Phd1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 1, 4),
    _Phd1_capacity_Type()
)
phd1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd1_capacity.setStatus("current")
_Phd2_ObjectIdentity = ObjectIdentity
phd2 = _Phd2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2)
)
_Phd2_model_Type = DisplayString
_Phd2_model_Object = MibScalar
phd2_model = _Phd2_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 1),
    _Phd2_model_Type()
)
phd2_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_model.setStatus("current")
_Phd2_manufacturing_info_Type = DisplayString
_Phd2_manufacturing_info_Object = MibScalar
phd2_manufacturing_info = _Phd2_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 2),
    _Phd2_manufacturing_info_Type()
)
phd2_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_manufacturing_info.setStatus("current")


class _Phd2_type_Type(Integer32):
    """Custom type phd2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 2),
          ("eInputPHD", 10),
          ("eOutputPHD", 11),
          ("eBindingPHD", 13))
    )


_Phd2_type_Type.__name__ = "Integer32"
_Phd2_type_Object = MibScalar
phd2_type = _Phd2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 3),
    _Phd2_type_Type()
)
phd2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_type.setStatus("current")
_Phd2_capacity_Type = Integer32
_Phd2_capacity_Object = MibScalar
phd2_capacity = _Phd2_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 2, 4),
    _Phd2_capacity_Type()
)
phd2_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_capacity.setStatus("current")
_Phd3_ObjectIdentity = ObjectIdentity
phd3 = _Phd3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3)
)
_Phd3_model_Type = DisplayString
_Phd3_model_Object = MibScalar
phd3_model = _Phd3_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 1),
    _Phd3_model_Type()
)
phd3_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_model.setStatus("current")
_Phd3_manufacturing_info_Type = DisplayString
_Phd3_manufacturing_info_Object = MibScalar
phd3_manufacturing_info = _Phd3_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 2),
    _Phd3_manufacturing_info_Type()
)
phd3_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_manufacturing_info.setStatus("current")


class _Phd3_type_Type(Integer32):
    """Custom type phd3_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 2),
          ("eInputPHD", 10),
          ("eOutputPHD", 11),
          ("eBindingPHD", 13))
    )


_Phd3_type_Type.__name__ = "Integer32"
_Phd3_type_Object = MibScalar
phd3_type = _Phd3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 3),
    _Phd3_type_Type()
)
phd3_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_type.setStatus("current")
_Phd3_capacity_Type = Integer32
_Phd3_capacity_Object = MibScalar
phd3_capacity = _Phd3_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 3, 4),
    _Phd3_capacity_Type()
)
phd3_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_capacity.setStatus("current")
_Phd4_ObjectIdentity = ObjectIdentity
phd4 = _Phd4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4)
)
_Phd4_model_Type = DisplayString
_Phd4_model_Object = MibScalar
phd4_model = _Phd4_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 1),
    _Phd4_model_Type()
)
phd4_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_model.setStatus("current")
_Phd4_manufacturing_info_Type = DisplayString
_Phd4_manufacturing_info_Object = MibScalar
phd4_manufacturing_info = _Phd4_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 2),
    _Phd4_manufacturing_info_Type()
)
phd4_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_manufacturing_info.setStatus("current")


class _Phd4_type_Type(Integer32):
    """Custom type phd4_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 2),
          ("eInputPHD", 10),
          ("eOutputPHD", 11),
          ("eBindingPHD", 13))
    )


_Phd4_type_Type.__name__ = "Integer32"
_Phd4_type_Object = MibScalar
phd4_type = _Phd4_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 3),
    _Phd4_type_Type()
)
phd4_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_type.setStatus("current")
_Phd4_capacity_Type = Integer32
_Phd4_capacity_Object = MibScalar
phd4_capacity = _Phd4_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 4, 4),
    _Phd4_capacity_Type()
)
phd4_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_capacity.setStatus("current")
_Phd5_ObjectIdentity = ObjectIdentity
phd5 = _Phd5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5)
)
_Phd5_model_Type = DisplayString
_Phd5_model_Object = MibScalar
phd5_model = _Phd5_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 1),
    _Phd5_model_Type()
)
phd5_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_model.setStatus("current")
_Phd5_manufacturing_info_Type = DisplayString
_Phd5_manufacturing_info_Object = MibScalar
phd5_manufacturing_info = _Phd5_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 2),
    _Phd5_manufacturing_info_Type()
)
phd5_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_manufacturing_info.setStatus("current")


class _Phd5_type_Type(Integer32):
    """Custom type phd5_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 2),
          ("eInputPHD", 10),
          ("eOutputPHD", 11),
          ("eBindingPHD", 13))
    )


_Phd5_type_Type.__name__ = "Integer32"
_Phd5_type_Object = MibScalar
phd5_type = _Phd5_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 3),
    _Phd5_type_Type()
)
phd5_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_type.setStatus("current")
_Phd5_capacity_Type = Integer32
_Phd5_capacity_Object = MibScalar
phd5_capacity = _Phd5_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 5, 4),
    _Phd5_capacity_Type()
)
phd5_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_capacity.setStatus("current")
_Phd6_ObjectIdentity = ObjectIdentity
phd6 = _Phd6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6)
)
_Phd6_model_Type = DisplayString
_Phd6_model_Object = MibScalar
phd6_model = _Phd6_model_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 1),
    _Phd6_model_Type()
)
phd6_model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_model.setStatus("current")
_Phd6_manufacturing_info_Type = DisplayString
_Phd6_manufacturing_info_Object = MibScalar
phd6_manufacturing_info = _Phd6_manufacturing_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 2),
    _Phd6_manufacturing_info_Type()
)
phd6_manufacturing_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_manufacturing_info.setStatus("current")


class _Phd6_type_Type(Integer32):
    """Custom type phd6_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("eUnknown", 2),
          ("eInputPHD", 10),
          ("eOutputPHD", 11),
          ("eBindingPHD", 13))
    )


_Phd6_type_Type.__name__ = "Integer32"
_Phd6_type_Object = MibScalar
phd6_type = _Phd6_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 3),
    _Phd6_type_Type()
)
phd6_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_type.setStatus("current")
_Phd6_capacity_Type = Integer32
_Phd6_capacity_Object = MibScalar
phd6_capacity = _Phd6_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 5, 6, 4),
    _Phd6_capacity_Type()
)
phd6_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_capacity.setStatus("current")
_Web_server_ObjectIdentity = ObjectIdentity
web_server = _Web_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6)
)
_Settings_web_server_ObjectIdentity = ObjectIdentity
settings_web_server = _Settings_web_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6, 1)
)


class _Web_proxy_config_enable_Type(Integer32):
    """Custom type web_proxy_config_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 0),
          ("eOn", 1))
    )


_Web_proxy_config_enable_Type.__name__ = "Integer32"
_Web_proxy_config_enable_Object = MibScalar
web_proxy_config_enable = _Web_proxy_config_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6, 1, 4),
    _Web_proxy_config_enable_Type()
)
web_proxy_config_enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    web_proxy_config_enable.setStatus("current")


class _Ews_request_control_panel_supplies_status_Type(Integer32):
    """Custom type ews_request_control_panel_supplies_status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Ews_request_control_panel_supplies_status_Type.__name__ = "Integer32"
_Ews_request_control_panel_supplies_status_Object = MibScalar
ews_request_control_panel_supplies_status = _Ews_request_control_panel_supplies_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 6, 1, 5),
    _Ews_request_control_panel_supplies_status_Type()
)
ews_request_control_panel_supplies_status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ews_request_control_panel_supplies_status.setStatus("current")
_Foreign_interface_ObjectIdentity = ObjectIdentity
foreign_interface = _Foreign_interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 8)
)


class _Fih_extra_pulses_feature_Type(Integer32):
    """Custom type fih_extra_pulses_feature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisable", 1),
          ("eEnable", 2))
    )


_Fih_extra_pulses_feature_Type.__name__ = "Integer32"
_Fih_extra_pulses_feature_Object = MibScalar
fih_extra_pulses_feature = _Fih_extra_pulses_feature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 8, 2),
    _Fih_extra_pulses_feature_Type()
)
fih_extra_pulses_feature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fih_extra_pulses_feature.setStatus("current")
_Usb_interface_ObjectIdentity = ObjectIdentity
usb_interface = _Usb_interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9)
)
_Usb_ObjectIdentity = ObjectIdentity
usb = _Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2)
)
_Usb_product_id_Type = Integer32
_Usb_product_id_Object = MibScalar
usb_product_id = _Usb_product_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 4, 9, 2, 5),
    _Usb_product_id_Type()
)
usb_product_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usb_product_id.setStatus("current")
_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5)
)


class _Self_test_Type(Integer32):
    """Custom type self_test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eNotInASelfTest", 1),
          ("eNonDestructiveSelfTest", 4))
    )


_Self_test_Type.__name__ = "Integer32"
_Self_test_Object = MibScalar
self_test = _Self_test_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 1),
    _Self_test_Type()
)
self_test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    self_test.setStatus("current")


class _Print_internal_page_Type(Integer32):
    """Custom type print_internal_page based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7,
              8,
              9,
              10,
              350,
              450)
        )
    )
    namedValues = NamedValues(
        *(("eNotPrintingAnInternalPage", 1),
          ("ePrintingAnUnknownInternalPage", 2),
          ("eDeviceDemoPage1ConfigurationPage", 3),
          ("eDeviceDemoPage5ErrorLog", 7),
          ("eDeviceDemoPage6FileSystemDirectoryListing", 8),
          ("eDeviceDemoPage7MenuMap", 9),
          ("eDeviceUsagePage", 10),
          ("ePCLFontList1", 350),
          ("ePSFontList", 450))
    )


_Print_internal_page_Type.__name__ = "Integer32"
_Print_internal_page_Object = MibScalar
print_internal_page = _Print_internal_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 5, 2),
    _Print_internal_page_Type()
)
print_internal_page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_internal_page.setStatus("current")
_Job_ObjectIdentity = ObjectIdentity
job = _Job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6)
)
_Settings_job_ObjectIdentity = ObjectIdentity
settings_job = _Settings_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1)
)


class _Clearable_warning_Type(Integer32):
    """Custom type clearable_warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOn", 2),
          ("eJob", 3))
    )


_Clearable_warning_Type.__name__ = "Integer32"
_Clearable_warning_Object = MibScalar
clearable_warning = _Clearable_warning_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 1),
    _Clearable_warning_Type()
)
clearable_warning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearable_warning.setStatus("current")


class _Cancel_job_Type(Integer32):
    """Custom type cancel_job based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_Cancel_job_Type.__name__ = "Integer32"
_Cancel_job_Object = MibScalar
cancel_job = _Cancel_job_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 2),
    _Cancel_job_Type()
)
cancel_job.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cancel_job.setStatus("current")


class _Job_info_change_id_Type(OctetString):
    """Custom type job_info_change_id based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Job_info_change_id_Type.__name__ = "OctetString"
_Job_info_change_id_Object = MibScalar
job_info_change_id = _Job_info_change_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 3),
    _Job_info_change_id_Type()
)
job_info_change_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_change_id.setStatus("current")
_Hold_job_timeout_Type = Integer32
_Hold_job_timeout_Object = MibScalar
hold_job_timeout = _Hold_job_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 1, 10),
    _Hold_job_timeout_Type()
)
hold_job_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hold_job_timeout.setStatus("current")
_Active_print_jobs_ObjectIdentity = ObjectIdentity
active_print_jobs = _Active_print_jobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2)
)
_Job_being_parsed_ObjectIdentity = ObjectIdentity
job_being_parsed = _Job_being_parsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2, 1)
)


class _Current_job_parsing_id_Type(Integer32):
    """Custom type current_job_parsing_id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Current_job_parsing_id_Type.__name__ = "Integer32"
_Current_job_parsing_id_Object = MibScalar
current_job_parsing_id = _Current_job_parsing_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 2, 1, 1),
    _Current_job_parsing_id_Type()
)
current_job_parsing_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current_job_parsing_id.setStatus("current")
_Fax_job_control_ObjectIdentity = ObjectIdentity
fax_job_control = _Fax_job_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3)
)
_Settings_fax_job_ObjectIdentity = ObjectIdentity
settings_fax_job = _Settings_fax_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1)
)


class _Faxjob_action_Type(Integer32):
    """Custom type faxjob_action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ePrintFaxToPrinter", 1),
          ("eDeleteFaxFromMemory", 3))
    )


_Faxjob_action_Type.__name__ = "Integer32"
_Faxjob_action_Object = MibScalar
faxjob_action = _Faxjob_action_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1, 1),
    _Faxjob_action_Type()
)
faxjob_action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxjob_action.setStatus("current")
_Faxjob_action_id_Type = Integer32
_Faxjob_action_id_Object = MibScalar
faxjob_action_id = _Faxjob_action_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1, 2),
    _Faxjob_action_id_Type()
)
faxjob_action_id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxjob_action_id.setStatus("current")


class _Faxjob_tx_type_Type(Integer32):
    """Custom type faxjob_tx_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("eSrcHostOnly", 2),
          ("eSrcScannerOnly", 5),
          ("eSrcHostToMemoryOnly", 9))
    )


_Faxjob_tx_type_Type.__name__ = "Integer32"
_Faxjob_tx_type_Object = MibScalar
faxjob_tx_type = _Faxjob_tx_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1, 3),
    _Faxjob_tx_type_Type()
)
faxjob_tx_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxjob_tx_type.setStatus("current")


class _Faxjob_print_duplex_mode_select_Type(Integer32):
    """Custom type faxjob_print_duplex_mode_select based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDuplexerDisabled", 1),
          ("eDuplexerEnabled", 2))
    )


_Faxjob_print_duplex_mode_select_Type.__name__ = "Integer32"
_Faxjob_print_duplex_mode_select_Object = MibScalar
faxjob_print_duplex_mode_select = _Faxjob_print_duplex_mode_select_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 1, 5),
    _Faxjob_print_duplex_mode_select_Type()
)
faxjob_print_duplex_mode_select.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxjob_print_duplex_mode_select.setStatus("current")
_Status_fax_job_ObjectIdentity = ObjectIdentity
status_fax_job = _Status_fax_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2)
)
_Faxjob_download_id_Type = Integer32
_Faxjob_download_id_Object = MibScalar
faxjob_download_id = _Faxjob_download_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 1),
    _Faxjob_download_id_Type()
)
faxjob_download_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_download_id.setStatus("current")
_Faxjob_rx_id_Type = Integer32
_Faxjob_rx_id_Object = MibScalar
faxjob_rx_id = _Faxjob_rx_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 2),
    _Faxjob_rx_id_Type()
)
faxjob_rx_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_id.setStatus("current")
_Faxjob_tx_id_Type = Integer32
_Faxjob_tx_id_Object = MibScalar
faxjob_tx_id = _Faxjob_tx_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 3),
    _Faxjob_tx_id_Type()
)
faxjob_tx_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_id.setStatus("current")
_Faxjob_upload_id_Type = Integer32
_Faxjob_upload_id_Object = MibScalar
faxjob_upload_id = _Faxjob_upload_id_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 2, 4),
    _Faxjob_upload_id_Type()
)
faxjob_upload_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_upload_id.setStatus("current")
_Faxjob_ObjectIdentity = ObjectIdentity
faxjob = _Faxjob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3)
)
_Faxjob_rx_status_ObjectIdentity = ObjectIdentity
faxjob_rx_status = _Faxjob_rx_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 1)
)


class _Faxjob_rx_status_1_Type(Integer32):
    """Custom type faxjob_rx_status_1 based on Integer32"""
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
        *(("eFaxRxIdle", 1),
          ("eFaxRxRinging", 2),
          ("eFaxRxAnswering", 3),
          ("eFaxRxReceiving", 4))
    )


_Faxjob_rx_status_1_Type.__name__ = "Integer32"
_Faxjob_rx_status_1_Object = MibScalar
faxjob_rx_status_1 = _Faxjob_rx_status_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 1, 1),
    _Faxjob_rx_status_1_Type()
)
faxjob_rx_status_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_status_1.setStatus("current")
_Faxjob_tx_status_ObjectIdentity = ObjectIdentity
faxjob_tx_status = _Faxjob_tx_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 3)
)


class _Faxjob_tx_status_1_Type(Integer32):
    """Custom type faxjob_tx_status_1 based on Integer32"""
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
        *(("eFaxTxIdle", 1),
          ("eFaxTxDialing", 2),
          ("eFaxTxConnecting", 3),
          ("eFaxTxTransmitting", 4))
    )


_Faxjob_tx_status_1_Type.__name__ = "Integer32"
_Faxjob_tx_status_1_Object = MibScalar
faxjob_tx_status_1 = _Faxjob_tx_status_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 3, 1),
    _Faxjob_tx_status_1_Type()
)
faxjob_tx_status_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_status_1.setStatus("current")
_Faxjob_tx_error_ObjectIdentity = ObjectIdentity
faxjob_tx_error = _Faxjob_tx_error_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 4)
)
_Faxjob_tx_error_1_Type = Integer32
_Faxjob_tx_error_1_Object = MibScalar
faxjob_tx_error_1 = _Faxjob_tx_error_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 4, 1),
    _Faxjob_tx_error_1_Type()
)
faxjob_tx_error_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_error_1.setStatus("current")
_Faxjob_tx_current_page_ObjectIdentity = ObjectIdentity
faxjob_tx_current_page = _Faxjob_tx_current_page_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 5)
)
_Faxjob_tx_current_page_1_Type = Integer32
_Faxjob_tx_current_page_1_Object = MibScalar
faxjob_tx_current_page_1 = _Faxjob_tx_current_page_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 5, 1),
    _Faxjob_tx_current_page_1_Type()
)
faxjob_tx_current_page_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_current_page_1.setStatus("current")
_Faxjob_rx_current_page_ObjectIdentity = ObjectIdentity
faxjob_rx_current_page = _Faxjob_rx_current_page_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 6)
)
_Faxjob_rx_current_page_1_Type = Integer32
_Faxjob_rx_current_page_1_Object = MibScalar
faxjob_rx_current_page_1 = _Faxjob_rx_current_page_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 6, 1),
    _Faxjob_rx_current_page_1_Type()
)
faxjob_rx_current_page_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_current_page_1.setStatus("current")
_Faxjob_rx_duration_ObjectIdentity = ObjectIdentity
faxjob_rx_duration = _Faxjob_rx_duration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 7)
)
_Faxjob_rx_duration_1_Type = Integer32
_Faxjob_rx_duration_1_Object = MibScalar
faxjob_rx_duration_1 = _Faxjob_rx_duration_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 7, 1),
    _Faxjob_rx_duration_1_Type()
)
faxjob_rx_duration_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_rx_duration_1.setStatus("current")
_Faxjob_tx_duration_ObjectIdentity = ObjectIdentity
faxjob_tx_duration = _Faxjob_tx_duration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 8)
)
_Faxjob_tx_duration_1_Type = Integer32
_Faxjob_tx_duration_1_Object = MibScalar
faxjob_tx_duration_1 = _Faxjob_tx_duration_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 3, 3, 8, 1),
    _Faxjob_tx_duration_1_Type()
)
faxjob_tx_duration_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxjob_tx_duration_1.setStatus("current")
_Fax_activity_log_ObjectIdentity = ObjectIdentity
fax_activity_log = _Fax_activity_log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4)
)
_Settings_faxlog_ObjectIdentity = ObjectIdentity
settings_faxlog = _Settings_faxlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4, 1)
)


class _Fax_log_action_Type(Integer32):
    """Custom type fax_log_action based on Integer32"""
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
        *(("eIdle", 1),
          ("eClear", 2),
          ("ePrintLatest", 3),
          ("ePrintAll", 4))
    )


_Fax_log_action_Type.__name__ = "Integer32"
_Fax_log_action_Object = MibScalar
fax_log_action = _Fax_log_action_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4, 1, 1),
    _Fax_log_action_Type()
)
fax_log_action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_log_action.setStatus("current")


class _Fax_log_reporting_Type(Integer32):
    """Custom type fax_log_reporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eNever", 1),
          ("eErrorOnly", 2),
          ("eSendOnly", 3))
    )


_Fax_log_reporting_Type.__name__ = "Integer32"
_Fax_log_reporting_Object = MibScalar
fax_log_reporting = _Fax_log_reporting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 4, 1, 2),
    _Fax_log_reporting_Type()
)
fax_log_reporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_log_reporting.setStatus("current")
_Job_info_ObjectIdentity = ObjectIdentity
job_info = _Job_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5)
)
_Job_info_name1_Type = DisplayString
_Job_info_name1_Object = MibScalar
job_info_name1 = _Job_info_name1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 1),
    _Job_info_name1_Type()
)
job_info_name1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_name1.setStatus("current")
_Job_info_name2_Type = DisplayString
_Job_info_name2_Object = MibScalar
job_info_name2 = _Job_info_name2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 2),
    _Job_info_name2_Type()
)
job_info_name2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_name2.setStatus("current")
_Job_info_stage_Type = OctetString
_Job_info_stage_Object = MibScalar
job_info_stage = _Job_info_stage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 10),
    _Job_info_stage_Type()
)
job_info_stage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_stage.setStatus("current")
_Job_info_io_source_Type = Integer32
_Job_info_io_source_Object = MibScalar
job_info_io_source = _Job_info_io_source_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 11),
    _Job_info_io_source_Type()
)
job_info_io_source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_io_source.setStatus("current")
_Job_info_pages_processed_Type = Integer32
_Job_info_pages_processed_Object = MibScalar
job_info_pages_processed = _Job_info_pages_processed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 12),
    _Job_info_pages_processed_Type()
)
job_info_pages_processed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_pages_processed.setStatus("current")
_Job_info_pages_printed_Type = Integer32
_Job_info_pages_printed_Object = MibScalar
job_info_pages_printed = _Job_info_pages_printed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 13),
    _Job_info_pages_printed_Type()
)
job_info_pages_printed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_pages_printed.setStatus("current")
_Job_info_size_Type = Integer32
_Job_info_size_Object = MibScalar
job_info_size = _Job_info_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 14),
    _Job_info_size_Type()
)
job_info_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_size.setStatus("current")


class _Job_info_state_Type(Integer32):
    """Custom type job_info_state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              7,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("eAborted", 3),
          ("eWaitingForResources", 4),
          ("ePrinted", 5),
          ("eTerminating", 7),
          ("eCancelled", 10),
          ("eProcessing", 11))
    )


_Job_info_state_Type.__name__ = "Integer32"
_Job_info_state_Object = MibScalar
job_info_state = _Job_info_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 15),
    _Job_info_state_Type()
)
job_info_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_state.setStatus("current")


class _Job_info_outcome_Type(Integer32):
    """Custom type job_info_outcome based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("eOk", 3)
    )


_Job_info_outcome_Type.__name__ = "Integer32"
_Job_info_outcome_Object = MibScalar
job_info_outcome = _Job_info_outcome_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 19),
    _Job_info_outcome_Type()
)
job_info_outcome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_outcome.setStatus("current")
_Job_info_outbins_used_Type = OctetString
_Job_info_outbins_used_Object = MibScalar
job_info_outbins_used = _Job_info_outbins_used_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 20),
    _Job_info_outbins_used_Type()
)
job_info_outbins_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_outbins_used.setStatus("current")
_Job_info_physical_outbins_used_Type = OctetString
_Job_info_physical_outbins_used_Object = MibScalar
job_info_physical_outbins_used = _Job_info_physical_outbins_used_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 22),
    _Job_info_physical_outbins_used_Type()
)
job_info_physical_outbins_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_physical_outbins_used.setStatus("current")
_Job_info_attribute_ObjectIdentity = ObjectIdentity
job_info_attribute = _Job_info_attribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23)
)


class _Job_info_attr_1_Type(OctetString):
    """Custom type job_info_attr_1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_1_Type.__name__ = "OctetString"
_Job_info_attr_1_Object = MibScalar
job_info_attr_1 = _Job_info_attr_1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 1),
    _Job_info_attr_1_Type()
)
job_info_attr_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_1.setStatus("current")


class _Job_info_attr_2_Type(OctetString):
    """Custom type job_info_attr_2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_2_Type.__name__ = "OctetString"
_Job_info_attr_2_Object = MibScalar
job_info_attr_2 = _Job_info_attr_2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 2),
    _Job_info_attr_2_Type()
)
job_info_attr_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_2.setStatus("current")


class _Job_info_attr_3_Type(OctetString):
    """Custom type job_info_attr_3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_3_Type.__name__ = "OctetString"
_Job_info_attr_3_Object = MibScalar
job_info_attr_3 = _Job_info_attr_3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 3),
    _Job_info_attr_3_Type()
)
job_info_attr_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_3.setStatus("current")


class _Job_info_attr_4_Type(OctetString):
    """Custom type job_info_attr_4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_4_Type.__name__ = "OctetString"
_Job_info_attr_4_Object = MibScalar
job_info_attr_4 = _Job_info_attr_4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 4),
    _Job_info_attr_4_Type()
)
job_info_attr_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_4.setStatus("current")


class _Job_info_attr_5_Type(OctetString):
    """Custom type job_info_attr_5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_5_Type.__name__ = "OctetString"
_Job_info_attr_5_Object = MibScalar
job_info_attr_5 = _Job_info_attr_5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 5),
    _Job_info_attr_5_Type()
)
job_info_attr_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_5.setStatus("current")


class _Job_info_attr_6_Type(OctetString):
    """Custom type job_info_attr_6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_6_Type.__name__ = "OctetString"
_Job_info_attr_6_Object = MibScalar
job_info_attr_6 = _Job_info_attr_6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 6),
    _Job_info_attr_6_Type()
)
job_info_attr_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_6.setStatus("current")


class _Job_info_attr_7_Type(OctetString):
    """Custom type job_info_attr_7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_7_Type.__name__ = "OctetString"
_Job_info_attr_7_Object = MibScalar
job_info_attr_7 = _Job_info_attr_7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 7),
    _Job_info_attr_7_Type()
)
job_info_attr_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_7.setStatus("current")


class _Job_info_attr_8_Type(OctetString):
    """Custom type job_info_attr_8 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_8_Type.__name__ = "OctetString"
_Job_info_attr_8_Object = MibScalar
job_info_attr_8 = _Job_info_attr_8_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 8),
    _Job_info_attr_8_Type()
)
job_info_attr_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_8.setStatus("current")


class _Job_info_attr_9_Type(OctetString):
    """Custom type job_info_attr_9 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_9_Type.__name__ = "OctetString"
_Job_info_attr_9_Object = MibScalar
job_info_attr_9 = _Job_info_attr_9_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 9),
    _Job_info_attr_9_Type()
)
job_info_attr_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_9.setStatus("current")


class _Job_info_attr_10_Type(OctetString):
    """Custom type job_info_attr_10 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_10_Type.__name__ = "OctetString"
_Job_info_attr_10_Object = MibScalar
job_info_attr_10 = _Job_info_attr_10_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 10),
    _Job_info_attr_10_Type()
)
job_info_attr_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_10.setStatus("current")


class _Job_info_attr_11_Type(OctetString):
    """Custom type job_info_attr_11 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_11_Type.__name__ = "OctetString"
_Job_info_attr_11_Object = MibScalar
job_info_attr_11 = _Job_info_attr_11_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 11),
    _Job_info_attr_11_Type()
)
job_info_attr_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_11.setStatus("current")


class _Job_info_attr_12_Type(OctetString):
    """Custom type job_info_attr_12 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_12_Type.__name__ = "OctetString"
_Job_info_attr_12_Object = MibScalar
job_info_attr_12 = _Job_info_attr_12_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 12),
    _Job_info_attr_12_Type()
)
job_info_attr_12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_12.setStatus("current")


class _Job_info_attr_13_Type(OctetString):
    """Custom type job_info_attr_13 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_13_Type.__name__ = "OctetString"
_Job_info_attr_13_Object = MibScalar
job_info_attr_13 = _Job_info_attr_13_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 13),
    _Job_info_attr_13_Type()
)
job_info_attr_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_13.setStatus("current")


class _Job_info_attr_14_Type(OctetString):
    """Custom type job_info_attr_14 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_14_Type.__name__ = "OctetString"
_Job_info_attr_14_Object = MibScalar
job_info_attr_14 = _Job_info_attr_14_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 14),
    _Job_info_attr_14_Type()
)
job_info_attr_14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_14.setStatus("current")


class _Job_info_attr_15_Type(OctetString):
    """Custom type job_info_attr_15 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_15_Type.__name__ = "OctetString"
_Job_info_attr_15_Object = MibScalar
job_info_attr_15 = _Job_info_attr_15_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 15),
    _Job_info_attr_15_Type()
)
job_info_attr_15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_15.setStatus("current")


class _Job_info_attr_16_Type(OctetString):
    """Custom type job_info_attr_16 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_16_Type.__name__ = "OctetString"
_Job_info_attr_16_Object = MibScalar
job_info_attr_16 = _Job_info_attr_16_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 16),
    _Job_info_attr_16_Type()
)
job_info_attr_16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_16.setStatus("current")


class _Job_info_attr_17_Type(OctetString):
    """Custom type job_info_attr_17 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_17_Type.__name__ = "OctetString"
_Job_info_attr_17_Object = MibScalar
job_info_attr_17 = _Job_info_attr_17_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 17),
    _Job_info_attr_17_Type()
)
job_info_attr_17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_17.setStatus("current")


class _Job_info_attr_18_Type(OctetString):
    """Custom type job_info_attr_18 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_18_Type.__name__ = "OctetString"
_Job_info_attr_18_Object = MibScalar
job_info_attr_18 = _Job_info_attr_18_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 18),
    _Job_info_attr_18_Type()
)
job_info_attr_18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_18.setStatus("current")


class _Job_info_attr_19_Type(OctetString):
    """Custom type job_info_attr_19 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_19_Type.__name__ = "OctetString"
_Job_info_attr_19_Object = MibScalar
job_info_attr_19 = _Job_info_attr_19_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 19),
    _Job_info_attr_19_Type()
)
job_info_attr_19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_19.setStatus("current")


class _Job_info_attr_20_Type(OctetString):
    """Custom type job_info_attr_20 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_20_Type.__name__ = "OctetString"
_Job_info_attr_20_Object = MibScalar
job_info_attr_20 = _Job_info_attr_20_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 20),
    _Job_info_attr_20_Type()
)
job_info_attr_20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_20.setStatus("current")


class _Job_info_attr_21_Type(OctetString):
    """Custom type job_info_attr_21 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_21_Type.__name__ = "OctetString"
_Job_info_attr_21_Object = MibScalar
job_info_attr_21 = _Job_info_attr_21_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 21),
    _Job_info_attr_21_Type()
)
job_info_attr_21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_21.setStatus("current")


class _Job_info_attr_22_Type(OctetString):
    """Custom type job_info_attr_22 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_22_Type.__name__ = "OctetString"
_Job_info_attr_22_Object = MibScalar
job_info_attr_22 = _Job_info_attr_22_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 22),
    _Job_info_attr_22_Type()
)
job_info_attr_22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_22.setStatus("current")


class _Job_info_attr_23_Type(OctetString):
    """Custom type job_info_attr_23 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_23_Type.__name__ = "OctetString"
_Job_info_attr_23_Object = MibScalar
job_info_attr_23 = _Job_info_attr_23_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 23),
    _Job_info_attr_23_Type()
)
job_info_attr_23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_23.setStatus("current")


class _Job_info_attr_24_Type(OctetString):
    """Custom type job_info_attr_24 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_24_Type.__name__ = "OctetString"
_Job_info_attr_24_Object = MibScalar
job_info_attr_24 = _Job_info_attr_24_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 24),
    _Job_info_attr_24_Type()
)
job_info_attr_24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_24.setStatus("current")


class _Job_info_attr_25_Type(OctetString):
    """Custom type job_info_attr_25 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_25_Type.__name__ = "OctetString"
_Job_info_attr_25_Object = MibScalar
job_info_attr_25 = _Job_info_attr_25_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 25),
    _Job_info_attr_25_Type()
)
job_info_attr_25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_25.setStatus("current")


class _Job_info_attr_26_Type(OctetString):
    """Custom type job_info_attr_26 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_26_Type.__name__ = "OctetString"
_Job_info_attr_26_Object = MibScalar
job_info_attr_26 = _Job_info_attr_26_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 26),
    _Job_info_attr_26_Type()
)
job_info_attr_26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_26.setStatus("current")


class _Job_info_attr_27_Type(OctetString):
    """Custom type job_info_attr_27 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_27_Type.__name__ = "OctetString"
_Job_info_attr_27_Object = MibScalar
job_info_attr_27 = _Job_info_attr_27_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 27),
    _Job_info_attr_27_Type()
)
job_info_attr_27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_27.setStatus("current")


class _Job_info_attr_28_Type(OctetString):
    """Custom type job_info_attr_28 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_28_Type.__name__ = "OctetString"
_Job_info_attr_28_Object = MibScalar
job_info_attr_28 = _Job_info_attr_28_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 28),
    _Job_info_attr_28_Type()
)
job_info_attr_28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_28.setStatus("current")


class _Job_info_attr_29_Type(OctetString):
    """Custom type job_info_attr_29 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_29_Type.__name__ = "OctetString"
_Job_info_attr_29_Object = MibScalar
job_info_attr_29 = _Job_info_attr_29_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 29),
    _Job_info_attr_29_Type()
)
job_info_attr_29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_29.setStatus("current")


class _Job_info_attr_30_Type(OctetString):
    """Custom type job_info_attr_30 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_30_Type.__name__ = "OctetString"
_Job_info_attr_30_Object = MibScalar
job_info_attr_30 = _Job_info_attr_30_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 30),
    _Job_info_attr_30_Type()
)
job_info_attr_30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_30.setStatus("current")


class _Job_info_attr_31_Type(OctetString):
    """Custom type job_info_attr_31 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_31_Type.__name__ = "OctetString"
_Job_info_attr_31_Object = MibScalar
job_info_attr_31 = _Job_info_attr_31_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 31),
    _Job_info_attr_31_Type()
)
job_info_attr_31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_31.setStatus("current")


class _Job_info_attr_32_Type(OctetString):
    """Custom type job_info_attr_32 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Job_info_attr_32_Type.__name__ = "OctetString"
_Job_info_attr_32_Object = MibScalar
job_info_attr_32 = _Job_info_attr_32_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 23, 32),
    _Job_info_attr_32_Type()
)
job_info_attr_32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_attr_32.setStatus("current")
_Job_info_requested_originals_Type = Integer32
_Job_info_requested_originals_Object = MibScalar
job_info_requested_originals = _Job_info_requested_originals_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 24),
    _Job_info_requested_originals_Type()
)
job_info_requested_originals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_requested_originals.setStatus("current")
_Job_info_page_count_current_original_Type = Integer32
_Job_info_page_count_current_original_Object = MibScalar
job_info_page_count_current_original = _Job_info_page_count_current_original_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 25),
    _Job_info_page_count_current_original_Type()
)
job_info_page_count_current_original.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_page_count_current_original.setStatus("current")
_Job_info_pages_in_original_Type = Integer32
_Job_info_pages_in_original_Object = MibScalar
job_info_pages_in_original = _Job_info_pages_in_original_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 26),
    _Job_info_pages_in_original_Type()
)
job_info_pages_in_original.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_pages_in_original.setStatus("current")
_Job_info_printed_originals_Type = Integer32
_Job_info_printed_originals_Object = MibScalar
job_info_printed_originals = _Job_info_printed_originals_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 27),
    _Job_info_printed_originals_Type()
)
job_info_printed_originals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    job_info_printed_originals.setStatus("current")
_Job_info_accounting_ObjectIdentity = ObjectIdentity
job_info_accounting = _Job_info_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 5, 28)
)
_Held_job_ObjectIdentity = ObjectIdentity
held_job = _Held_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7)
)
_Held_job_info_ObjectIdentity = ObjectIdentity
held_job_info = _Held_job_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1)
)


class _Held_job_user_name_Type(DisplayString):
    """Custom type held_job_user_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Held_job_user_name_Type.__name__ = "DisplayString"
_Held_job_user_name_Object = MibScalar
held_job_user_name = _Held_job_user_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 1),
    _Held_job_user_name_Type()
)
held_job_user_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_user_name.setStatus("current")


class _Held_job_job_name_Type(DisplayString):
    """Custom type held_job_job_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Held_job_job_name_Type.__name__ = "DisplayString"
_Held_job_job_name_Object = MibScalar
held_job_job_name = _Held_job_job_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 2),
    _Held_job_job_name_Type()
)
held_job_job_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_job_name.setStatus("current")


class _Held_job_retention_Type(Integer32):
    """Custom type held_job_retention based on Integer32"""
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
        *(("eHoldOff", 1),
          ("eHoldOn", 2),
          ("eHoldStore", 3),
          ("eHoldProof", 4))
    )


_Held_job_retention_Type.__name__ = "Integer32"
_Held_job_retention_Object = MibScalar
held_job_retention = _Held_job_retention_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 3),
    _Held_job_retention_Type()
)
held_job_retention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_retention.setStatus("current")


class _Held_job_security_Type(Integer32):
    """Custom type held_job_security based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eHoldTypePublic", 1),
          ("eHoldTypePrivate", 2))
    )


_Held_job_security_Type.__name__ = "Integer32"
_Held_job_security_Object = MibScalar
held_job_security = _Held_job_security_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 4),
    _Held_job_security_Type()
)
held_job_security.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_security.setStatus("current")


class _Held_job_quantity_Type(Integer32):
    """Custom type held_job_quantity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_Held_job_quantity_Type.__name__ = "Integer32"
_Held_job_quantity_Object = MibScalar
held_job_quantity = _Held_job_quantity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 5),
    _Held_job_quantity_Type()
)
held_job_quantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_quantity.setStatus("current")


class _Held_job_pin_Type(DisplayString):
    """Custom type held_job_pin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Held_job_pin_Type.__name__ = "DisplayString"
_Held_job_pin_Object = MibScalar
held_job_pin = _Held_job_pin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 1, 6),
    _Held_job_pin_Type()
)
held_job_pin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    held_job_pin.setStatus("current")
_Held_job_control_ObjectIdentity = ObjectIdentity
held_job_control = _Held_job_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2)
)


class _Held_job_print_Type(OctetString):
    """Custom type held_job_print based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Held_job_print_Type.__name__ = "OctetString"
_Held_job_print_Object = MibScalar
held_job_print = _Held_job_print_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 1),
    _Held_job_print_Type()
)
held_job_print.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    held_job_print.setStatus("current")


class _Held_job_delete_Type(Integer32):
    """Custom type held_job_delete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_Held_job_delete_Type.__name__ = "Integer32"
_Held_job_delete_Object = MibScalar
held_job_delete = _Held_job_delete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 2),
    _Held_job_delete_Type()
)
held_job_delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    held_job_delete.setStatus("current")


class _Held_job_set_queue_size_Type(Integer32):
    """Custom type held_job_set_queue_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_Held_job_set_queue_size_Type.__name__ = "Integer32"
_Held_job_set_queue_size_Object = MibScalar
held_job_set_queue_size = _Held_job_set_queue_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 3),
    _Held_job_set_queue_size_Type()
)
held_job_set_queue_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    held_job_set_queue_size.setStatus("current")


class _Held_job_enable_Type(Integer32):
    """Custom type held_job_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Held_job_enable_Type.__name__ = "Integer32"
_Held_job_enable_Object = MibScalar
held_job_enable = _Held_job_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 7, 2, 4),
    _Held_job_enable_Type()
)
held_job_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    held_job_enable.setStatus("current")
_Photo_job_ObjectIdentity = ObjectIdentity
photo_job = _Photo_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8)
)


class _Photo_access_card_error_Type(Integer32):
    """Custom type photo_access_card_error based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("ePhotoCardAccessNoError", 0),
          ("ePhotoCardSmartMediaUpsideDown", 1),
          ("ePhotoCardMediaNotFullyInserted", 2),
          ("ePhotoCardMoreThenOneInSlots", 3),
          ("ePhotoCardReadError", 4),
          ("ePhotoCardRemovedWhileReading", 5),
          ("ePhotoCardBadFileWhilePrinting", 6),
          ("ePhotoCardNotInSlot", 7),
          ("ePhotoCardContainsNoPhotos", 8),
          ("ePhotoCardWriteError", 9),
          ("ePhotoCardRemovedWhileWriting", 10),
          ("ePhotoCardUnknownError", 999))
    )


_Photo_access_card_error_Type.__name__ = "Integer32"
_Photo_access_card_error_Object = MibScalar
photo_access_card_error = _Photo_access_card_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 2),
    _Photo_access_card_error_Type()
)
photo_access_card_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    photo_access_card_error.setStatus("current")
_Settings_photo_job_ObjectIdentity = ObjectIdentity
settings_photo_job = _Settings_photo_job_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3)
)


class _Photo_default_num_copies_Type(Integer32):
    """Custom type photo_default_num_copies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Photo_default_num_copies_Type.__name__ = "Integer32"
_Photo_default_num_copies_Object = MibScalar
photo_default_num_copies = _Photo_default_num_copies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 1),
    _Photo_default_num_copies_Type()
)
photo_default_num_copies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_default_num_copies.setStatus("current")


class _Photo_job_num_copies_Type(Integer32):
    """Custom type photo_job_num_copies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Photo_job_num_copies_Type.__name__ = "Integer32"
_Photo_job_num_copies_Object = MibScalar
photo_job_num_copies = _Photo_job_num_copies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 2),
    _Photo_job_num_copies_Type()
)
photo_job_num_copies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_job_num_copies.setStatus("current")


class _Photo_job_media_size_Type(Integer32):
    """Custom type photo_job_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              26,
              76)
        )
    )
    namedValues = NamedValues(
        *(("eUSLetter", 2),
          ("eISOandJISA4", 26),
          ("ePhoto4x6", 76))
    )


_Photo_job_media_size_Type.__name__ = "Integer32"
_Photo_job_media_size_Object = MibScalar
photo_job_media_size = _Photo_job_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 4),
    _Photo_job_media_size_Type()
)
photo_job_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_job_media_size.setStatus("current")
_Photo_job_media_name_Type = DisplayString
_Photo_job_media_name_Object = MibScalar
photo_job_media_name = _Photo_job_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 6),
    _Photo_job_media_name_Type()
)
photo_job_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_job_media_name.setStatus("current")


class _Photo_image_size_Type(Integer32):
    """Custom type photo_image_size based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("eThumbnail", 1),
          ("eWallet", 2),
          ("e3halfx5in", 3),
          ("e3x4in", 4),
          ("e4x6in", 5),
          ("e5x7in", 6),
          ("e6x8in", 7),
          ("e8x10in", 8),
          ("e6x8cm", 9),
          ("e7x10cm", 10),
          ("e9x13cm", 11),
          ("e10x15cm", 12),
          ("e13x18cm", 13),
          ("e15x21cm", 14),
          ("e18x24cm", 15),
          ("e20x25cm", 16),
          ("eFullPage", 17),
          ("ePanoramic", 18))
    )


_Photo_image_size_Type.__name__ = "Integer32"
_Photo_image_size_Object = MibScalar
photo_image_size = _Photo_image_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 7),
    _Photo_image_size_Type()
)
photo_image_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_image_size.setStatus("current")


class _Photo_job_image_size_Type(Integer32):
    """Custom type photo_job_image_size based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("eThumbnail", 1),
          ("eWallet", 2),
          ("e3halfx5in", 3),
          ("e3x4in", 4),
          ("e4x6in", 5),
          ("e5x7in", 6),
          ("e6x8in", 7),
          ("e8x10in", 8),
          ("e6x8cm", 9),
          ("e7x10cm", 10),
          ("e9x13cm", 11),
          ("e10x15cm", 12),
          ("e13x18cm", 13),
          ("e15x21cm", 14),
          ("e18x24cm", 15),
          ("e20x25cm", 16),
          ("eFullPage", 17),
          ("ePanoramic", 18))
    )


_Photo_job_image_size_Type.__name__ = "Integer32"
_Photo_job_image_size_Object = MibScalar
photo_job_image_size = _Photo_job_image_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 8),
    _Photo_job_image_size_Type()
)
photo_job_image_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_job_image_size.setStatus("current")
_Photo_select_images_Type = OctetString
_Photo_select_images_Object = MibScalar
photo_select_images = _Photo_select_images_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 9),
    _Photo_select_images_Type()
)
photo_select_images.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_select_images.setStatus("current")
_Photo_images_on_card_Type = Integer32
_Photo_images_on_card_Object = MibScalar
photo_images_on_card = _Photo_images_on_card_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 10),
    _Photo_images_on_card_Type()
)
photo_images_on_card.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    photo_images_on_card.setStatus("current")


class _Photo_job_source_Type(Integer32):
    """Custom type photo_job_source based on Integer32"""
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
        *(("ePhotoPrintProofSheet", 1),
          ("ePhotoScanProofSheet", 2),
          ("ePhotoPrintColorJob", 3),
          ("ePhotoPrintMonochromeJob", 4),
          ("ePhotoPrintIndexPrint", 5))
    )


_Photo_job_source_Type.__name__ = "Integer32"
_Photo_job_source_Object = MibScalar
photo_job_source = _Photo_job_source_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 11),
    _Photo_job_source_Type()
)
photo_job_source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_job_source.setStatus("current")
_Photo_color_page_count_Type = Integer32
_Photo_color_page_count_Object = MibScalar
photo_color_page_count = _Photo_color_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 12),
    _Photo_color_page_count_Type()
)
photo_color_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_color_page_count.setStatus("current")
_Photo_mono_page_count_Type = Integer32
_Photo_mono_page_count_Object = MibScalar
photo_mono_page_count = _Photo_mono_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 13),
    _Photo_mono_page_count_Type()
)
photo_mono_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_mono_page_count.setStatus("current")


class _Photo_image_size_set_Type(Integer32):
    """Custom type photo_image_size_set based on Integer32"""
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
        *(("eImageSizeSetInch1", 1),
          ("eImageSizeSetInch2", 2),
          ("eImageSizeSetCentimeter1", 3),
          ("eImageSizeSetCentimeter2", 4),
          ("eImageSizeSetCentimeter3", 5))
    )


_Photo_image_size_set_Type.__name__ = "Integer32"
_Photo_image_size_set_Object = MibScalar
photo_image_size_set = _Photo_image_size_set_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 15),
    _Photo_image_size_set_Type()
)
photo_image_size_set.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_image_size_set.setStatus("current")


class _Photo_clear_counts_Type(Integer32):
    """Custom type photo_clear_counts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eClearPageCounts", 1),
          ("eClearInsertCounts", 2),
          ("eClearAllCounts", 3))
    )


_Photo_clear_counts_Type.__name__ = "Integer32"
_Photo_clear_counts_Object = MibScalar
photo_clear_counts = _Photo_clear_counts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 18),
    _Photo_clear_counts_Type()
)
photo_clear_counts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_clear_counts.setStatus("current")
_Photo_compact_flash_insert_count_Type = Integer32
_Photo_compact_flash_insert_count_Object = MibScalar
photo_compact_flash_insert_count = _Photo_compact_flash_insert_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 19),
    _Photo_compact_flash_insert_count_Type()
)
photo_compact_flash_insert_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_compact_flash_insert_count.setStatus("current")
_Photo_memory_stick_insert_count_Type = Integer32
_Photo_memory_stick_insert_count_Object = MibScalar
photo_memory_stick_insert_count = _Photo_memory_stick_insert_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 20),
    _Photo_memory_stick_insert_count_Type()
)
photo_memory_stick_insert_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_memory_stick_insert_count.setStatus("current")
_Photo_memory_stick_pro_insert_count_Type = Integer32
_Photo_memory_stick_pro_insert_count_Object = MibScalar
photo_memory_stick_pro_insert_count = _Photo_memory_stick_pro_insert_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 21),
    _Photo_memory_stick_pro_insert_count_Type()
)
photo_memory_stick_pro_insert_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_memory_stick_pro_insert_count.setStatus("current")
_Photo_smart_media_insert_count_Type = Integer32
_Photo_smart_media_insert_count_Object = MibScalar
photo_smart_media_insert_count = _Photo_smart_media_insert_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 22),
    _Photo_smart_media_insert_count_Type()
)
photo_smart_media_insert_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_smart_media_insert_count.setStatus("current")
_Photo_secure_digital_insert_count_Type = Integer32
_Photo_secure_digital_insert_count_Object = MibScalar
photo_secure_digital_insert_count = _Photo_secure_digital_insert_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 23),
    _Photo_secure_digital_insert_count_Type()
)
photo_secure_digital_insert_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_secure_digital_insert_count.setStatus("current")
_Photo_mmc_insert_count_Type = Integer32
_Photo_mmc_insert_count_Object = MibScalar
photo_mmc_insert_count = _Photo_mmc_insert_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 24),
    _Photo_mmc_insert_count_Type()
)
photo_mmc_insert_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_mmc_insert_count.setStatus("current")
_Photo_xd_insert_count_Type = Integer32
_Photo_xd_insert_count_Object = MibScalar
photo_xd_insert_count = _Photo_xd_insert_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 6, 8, 3, 25),
    _Photo_xd_insert_count_Type()
)
photo_xd_insert_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    photo_xd_insert_count.setStatus("current")
_Phone_ObjectIdentity = ObjectIdentity
phone = _Phone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9)
)
_Dial_ObjectIdentity = ObjectIdentity
dial = _Dial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1)
)
_Dial_all_lines_ObjectIdentity = ObjectIdentity
dial_all_lines = _Dial_all_lines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1, 1)
)


class _Fax_dial_mode_Type(Integer32):
    """Custom type fax_dial_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eToneDial", 1),
          ("ePulseDial", 2))
    )


_Fax_dial_mode_Type.__name__ = "Integer32"
_Fax_dial_mode_Object = MibScalar
fax_dial_mode = _Fax_dial_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1, 1, 1),
    _Fax_dial_mode_Type()
)
fax_dial_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_dial_mode.setStatus("current")
_Device_redial_Type = OctetString
_Device_redial_Object = MibScalar
device_redial = _Device_redial_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 1, 1, 2),
    _Device_redial_Type()
)
device_redial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_redial.setStatus("current")
_Answer_ObjectIdentity = ObjectIdentity
answer = _Answer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2)
)
_Answer_all_lines_ObjectIdentity = ObjectIdentity
answer_all_lines = _Answer_all_lines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1)
)


class _Fax_answer_mode_Type(Integer32):
    """Custom type fax_answer_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eManualAnswer", 1),
          ("eFaxAnswer", 2))
    )


_Fax_answer_mode_Type.__name__ = "Integer32"
_Fax_answer_mode_Object = MibScalar
fax_answer_mode = _Fax_answer_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1, 1),
    _Fax_answer_mode_Type()
)
fax_answer_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_answer_mode.setStatus("current")


class _Fax_num_rings_pickup_Type(Integer32):
    """Custom type fax_num_rings_pickup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Fax_num_rings_pickup_Type.__name__ = "Integer32"
_Fax_num_rings_pickup_Object = MibScalar
fax_num_rings_pickup = _Fax_num_rings_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1, 2),
    _Fax_num_rings_pickup_Type()
)
fax_num_rings_pickup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_num_rings_pickup.setStatus("current")
_Device_ring_type_pickup_Type = OctetString
_Device_ring_type_pickup_Object = MibScalar
device_ring_type_pickup = _Device_ring_type_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 9, 2, 1, 3),
    _Device_ring_type_pickup_Type()
)
device_ring_type_pickup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    device_ring_type_pickup.setStatus("current")
_File_system_ObjectIdentity = ObjectIdentity
file_system = _File_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10)
)
_Settings_file_system_ObjectIdentity = ObjectIdentity
settings_file_system = _Settings_file_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1)
)
_File_system_memory_Type = Integer32
_File_system_memory_Object = MibScalar
file_system_memory = _File_system_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 1),
    _File_system_memory_Type()
)
file_system_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_memory.setStatus("current")


class _File_system_max_open_files_Type(Integer32):
    """Custom type file_system_max_open_files based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 512),
    )


_File_system_max_open_files_Type.__name__ = "Integer32"
_File_system_max_open_files_Object = MibScalar
file_system_max_open_files = _File_system_max_open_files_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 2),
    _File_system_max_open_files_Type()
)
file_system_max_open_files.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_max_open_files.setStatus("current")
_File_system_test_return_code_Type = OctetString
_File_system_test_return_code_Object = MibScalar
file_system_test_return_code = _File_system_test_return_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 3),
    _File_system_test_return_code_Type()
)
file_system_test_return_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_test_return_code.setStatus("current")
_File_system_set_system_partition_writeable_Type = OctetString
_File_system_set_system_partition_writeable_Object = MibScalar
file_system_set_system_partition_writeable = _File_system_set_system_partition_writeable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 6),
    _File_system_set_system_partition_writeable_Type()
)
file_system_set_system_partition_writeable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_set_system_partition_writeable.setStatus("current")
_File_system_set_system_partition_readonly_Type = Integer32
_File_system_set_system_partition_readonly_Object = MibScalar
file_system_set_system_partition_readonly = _File_system_set_system_partition_readonly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 7),
    _File_system_set_system_partition_readonly_Type()
)
file_system_set_system_partition_readonly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_set_system_partition_readonly.setStatus("current")
_File_system_delete_files_Type = OctetString
_File_system_delete_files_Object = MibScalar
file_system_delete_files = _File_system_delete_files_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 8),
    _File_system_delete_files_Type()
)
file_system_delete_files.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_delete_files.setStatus("current")
_File_system_security_access_password_Type = DisplayString
_File_system_security_access_password_Object = MibScalar
file_system_security_access_password = _File_system_security_access_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 9),
    _File_system_security_access_password_Type()
)
file_system_security_access_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_security_access_password.setStatus("current")
_File_system_external_access_capabilities_Type = OctetString
_File_system_external_access_capabilities_Object = MibScalar
file_system_external_access_capabilities = _File_system_external_access_capabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 10),
    _File_system_external_access_capabilities_Type()
)
file_system_external_access_capabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_external_access_capabilities.setStatus("current")
_File_system_erase_mode_Type = OctetString
_File_system_erase_mode_Object = MibScalar
file_system_erase_mode = _File_system_erase_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 11),
    _File_system_erase_mode_Type()
)
file_system_erase_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_erase_mode.setStatus("current")
_File_system_wipe_disk_Type = Integer32
_File_system_wipe_disk_Object = MibScalar
file_system_wipe_disk = _File_system_wipe_disk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 12),
    _File_system_wipe_disk_Type()
)
file_system_wipe_disk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system_wipe_disk.setStatus("current")
_File_system_wipe_disk_status_Type = Integer32
_File_system_wipe_disk_status_Object = MibScalar
file_system_wipe_disk_status = _File_system_wipe_disk_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 1, 13),
    _File_system_wipe_disk_status_Type()
)
file_system_wipe_disk_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_wipe_disk_status.setStatus("current")
_Status_file_system_ObjectIdentity = ObjectIdentity
status_file_system = _Status_file_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 2)
)
_File_system_statistic_read_open_Type = Integer32
_File_system_statistic_read_open_Object = MibScalar
file_system_statistic_read_open = _File_system_statistic_read_open_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 2, 1),
    _File_system_statistic_read_open_Type()
)
file_system_statistic_read_open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_statistic_read_open.setStatus("current")
_File_system_statistic_write_open_Type = Integer32
_File_system_statistic_write_open_Object = MibScalar
file_system_statistic_write_open = _File_system_statistic_write_open_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 2, 2),
    _File_system_statistic_write_open_Type()
)
file_system_statistic_write_open.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_statistic_write_open.setStatus("current")
_File_system_statistic_successful_Type = Integer32
_File_system_statistic_successful_Object = MibScalar
file_system_statistic_successful = _File_system_statistic_successful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 2, 3),
    _File_system_statistic_successful_Type()
)
file_system_statistic_successful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_statistic_successful.setStatus("current")
_File_system_statistic_unsuccessful_Type = Integer32
_File_system_statistic_unsuccessful_Object = MibScalar
file_system_statistic_unsuccessful = _File_system_statistic_unsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 2, 4),
    _File_system_statistic_unsuccessful_Type()
)
file_system_statistic_unsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_statistic_unsuccessful.setStatus("current")
_File_system_statistic_current_memory_usage_Type = Integer32
_File_system_statistic_current_memory_usage_Object = MibScalar
file_system_statistic_current_memory_usage = _File_system_statistic_current_memory_usage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 2, 5),
    _File_system_statistic_current_memory_usage_Type()
)
file_system_statistic_current_memory_usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_statistic_current_memory_usage.setStatus("current")
_File_system_statistic_max_memory_usage_Type = Integer32
_File_system_statistic_max_memory_usage_Object = MibScalar
file_system_statistic_max_memory_usage = _File_system_statistic_max_memory_usage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 2, 6),
    _File_system_statistic_max_memory_usage_Type()
)
file_system_statistic_max_memory_usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system_statistic_max_memory_usage.setStatus("current")
_File_systems_ObjectIdentity = ObjectIdentity
file_systems = _File_systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3)
)
_File_system1_ObjectIdentity = ObjectIdentity
file_system1 = _File_system1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 1)
)


class _File_system1_initialized_Type(Integer32):
    """Custom type file_system1_initialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_File_system1_initialized_Type.__name__ = "Integer32"
_File_system1_initialized_Object = MibScalar
file_system1_initialized = _File_system1_initialized_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 1, 1),
    _File_system1_initialized_Type()
)
file_system1_initialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system1_initialized.setStatus("current")
_File_system1_capacity_Type = Integer32
_File_system1_capacity_Object = MibScalar
file_system1_capacity = _File_system1_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 1, 2),
    _File_system1_capacity_Type()
)
file_system1_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system1_capacity.setStatus("current")
_File_system1_free_space_Type = Integer32
_File_system1_free_space_Object = MibScalar
file_system1_free_space = _File_system1_free_space_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 1, 3),
    _File_system1_free_space_Type()
)
file_system1_free_space.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    file_system1_free_space.setStatus("current")


class _File_system1_write_protect_Type(Integer32):
    """Custom type file_system1_write_protect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_File_system1_write_protect_Type.__name__ = "Integer32"
_File_system1_write_protect_Object = MibScalar
file_system1_write_protect = _File_system1_write_protect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 1, 4),
    _File_system1_write_protect_Type()
)
file_system1_write_protect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system1_write_protect.setStatus("current")
_File_system2_ObjectIdentity = ObjectIdentity
file_system2 = _File_system2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 2)
)


class _File_system2_initialize_volume_Type(Integer32):
    """Custom type file_system2_initialize_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eInitializing", 2)
    )


_File_system2_initialize_volume_Type.__name__ = "Integer32"
_File_system2_initialize_volume_Object = MibScalar
file_system2_initialize_volume = _File_system2_initialize_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 2, 6),
    _File_system2_initialize_volume_Type()
)
file_system2_initialize_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system2_initialize_volume.setStatus("current")
_File_system3_ObjectIdentity = ObjectIdentity
file_system3 = _File_system3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 3)
)


class _File_system3_initialize_volume_Type(Integer32):
    """Custom type file_system3_initialize_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eInitializing", 2)
    )


_File_system3_initialize_volume_Type.__name__ = "Integer32"
_File_system3_initialize_volume_Object = MibScalar
file_system3_initialize_volume = _File_system3_initialize_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 3, 6),
    _File_system3_initialize_volume_Type()
)
file_system3_initialize_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system3_initialize_volume.setStatus("current")
_File_system4_ObjectIdentity = ObjectIdentity
file_system4 = _File_system4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 4)
)


class _File_system4_initialize_volume_Type(Integer32):
    """Custom type file_system4_initialize_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eInitializing", 2)
    )


_File_system4_initialize_volume_Type.__name__ = "Integer32"
_File_system4_initialize_volume_Object = MibScalar
file_system4_initialize_volume = _File_system4_initialize_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 10, 3, 4, 6),
    _File_system4_initialize_volume_Type()
)
file_system4_initialize_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    file_system4_initialize_volume.setStatus("current")
_Errorlog_ObjectIdentity = ObjectIdentity
errorlog = _Errorlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11)
)
_Error1_ObjectIdentity = ObjectIdentity
error1 = _Error1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1)
)
_Error1_time_stamp_Type = Integer32
_Error1_time_stamp_Object = MibScalar
error1_time_stamp = _Error1_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 1),
    _Error1_time_stamp_Type()
)
error1_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_time_stamp.setStatus("current")
_Error1_code_Type = Integer32
_Error1_code_Object = MibScalar
error1_code = _Error1_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 1, 2),
    _Error1_code_Type()
)
error1_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error1_code.setStatus("current")
_Error2_ObjectIdentity = ObjectIdentity
error2 = _Error2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2)
)
_Error2_time_stamp_Type = Integer32
_Error2_time_stamp_Object = MibScalar
error2_time_stamp = _Error2_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 1),
    _Error2_time_stamp_Type()
)
error2_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_time_stamp.setStatus("current")
_Error2_code_Type = Integer32
_Error2_code_Object = MibScalar
error2_code = _Error2_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 2, 2),
    _Error2_code_Type()
)
error2_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error2_code.setStatus("current")
_Error3_ObjectIdentity = ObjectIdentity
error3 = _Error3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3)
)
_Error3_time_stamp_Type = Integer32
_Error3_time_stamp_Object = MibScalar
error3_time_stamp = _Error3_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 1),
    _Error3_time_stamp_Type()
)
error3_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_time_stamp.setStatus("current")
_Error3_code_Type = Integer32
_Error3_code_Object = MibScalar
error3_code = _Error3_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 3, 2),
    _Error3_code_Type()
)
error3_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error3_code.setStatus("current")
_Error4_ObjectIdentity = ObjectIdentity
error4 = _Error4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4)
)
_Error4_time_stamp_Type = Integer32
_Error4_time_stamp_Object = MibScalar
error4_time_stamp = _Error4_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 1),
    _Error4_time_stamp_Type()
)
error4_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_time_stamp.setStatus("current")
_Error4_code_Type = Integer32
_Error4_code_Object = MibScalar
error4_code = _Error4_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 4, 2),
    _Error4_code_Type()
)
error4_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error4_code.setStatus("current")
_Error5_ObjectIdentity = ObjectIdentity
error5 = _Error5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5)
)
_Error5_time_stamp_Type = Integer32
_Error5_time_stamp_Object = MibScalar
error5_time_stamp = _Error5_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 1),
    _Error5_time_stamp_Type()
)
error5_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_time_stamp.setStatus("current")
_Error5_code_Type = Integer32
_Error5_code_Object = MibScalar
error5_code = _Error5_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 5, 2),
    _Error5_code_Type()
)
error5_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error5_code.setStatus("current")
_Error6_ObjectIdentity = ObjectIdentity
error6 = _Error6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6)
)
_Error6_time_stamp_Type = Integer32
_Error6_time_stamp_Object = MibScalar
error6_time_stamp = _Error6_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 1),
    _Error6_time_stamp_Type()
)
error6_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_time_stamp.setStatus("current")
_Error6_code_Type = Integer32
_Error6_code_Object = MibScalar
error6_code = _Error6_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 6, 2),
    _Error6_code_Type()
)
error6_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error6_code.setStatus("current")
_Error7_ObjectIdentity = ObjectIdentity
error7 = _Error7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7)
)
_Error7_time_stamp_Type = Integer32
_Error7_time_stamp_Object = MibScalar
error7_time_stamp = _Error7_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 1),
    _Error7_time_stamp_Type()
)
error7_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_time_stamp.setStatus("current")
_Error7_code_Type = Integer32
_Error7_code_Object = MibScalar
error7_code = _Error7_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 7, 2),
    _Error7_code_Type()
)
error7_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error7_code.setStatus("current")
_Error8_ObjectIdentity = ObjectIdentity
error8 = _Error8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8)
)
_Error8_time_stamp_Type = Integer32
_Error8_time_stamp_Object = MibScalar
error8_time_stamp = _Error8_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 1),
    _Error8_time_stamp_Type()
)
error8_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_time_stamp.setStatus("current")
_Error8_code_Type = Integer32
_Error8_code_Object = MibScalar
error8_code = _Error8_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 8, 2),
    _Error8_code_Type()
)
error8_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error8_code.setStatus("current")
_Error9_ObjectIdentity = ObjectIdentity
error9 = _Error9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9)
)
_Error9_time_stamp_Type = Integer32
_Error9_time_stamp_Object = MibScalar
error9_time_stamp = _Error9_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 1),
    _Error9_time_stamp_Type()
)
error9_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_time_stamp.setStatus("current")
_Error9_code_Type = Integer32
_Error9_code_Object = MibScalar
error9_code = _Error9_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 9, 2),
    _Error9_code_Type()
)
error9_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error9_code.setStatus("current")
_Error10_ObjectIdentity = ObjectIdentity
error10 = _Error10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10)
)
_Error10_time_stamp_Type = Integer32
_Error10_time_stamp_Object = MibScalar
error10_time_stamp = _Error10_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 1),
    _Error10_time_stamp_Type()
)
error10_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_time_stamp.setStatus("current")
_Error10_code_Type = Integer32
_Error10_code_Object = MibScalar
error10_code = _Error10_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 10, 2),
    _Error10_code_Type()
)
error10_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error10_code.setStatus("current")
_Error11_ObjectIdentity = ObjectIdentity
error11 = _Error11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11)
)
_Error11_time_stamp_Type = Integer32
_Error11_time_stamp_Object = MibScalar
error11_time_stamp = _Error11_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 1),
    _Error11_time_stamp_Type()
)
error11_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_time_stamp.setStatus("current")
_Error11_code_Type = Integer32
_Error11_code_Object = MibScalar
error11_code = _Error11_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 11, 2),
    _Error11_code_Type()
)
error11_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error11_code.setStatus("current")
_Error12_ObjectIdentity = ObjectIdentity
error12 = _Error12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12)
)
_Error12_time_stamp_Type = Integer32
_Error12_time_stamp_Object = MibScalar
error12_time_stamp = _Error12_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 1),
    _Error12_time_stamp_Type()
)
error12_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_time_stamp.setStatus("current")
_Error12_code_Type = Integer32
_Error12_code_Object = MibScalar
error12_code = _Error12_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 12, 2),
    _Error12_code_Type()
)
error12_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error12_code.setStatus("current")
_Error13_ObjectIdentity = ObjectIdentity
error13 = _Error13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13)
)
_Error13_time_stamp_Type = Integer32
_Error13_time_stamp_Object = MibScalar
error13_time_stamp = _Error13_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 1),
    _Error13_time_stamp_Type()
)
error13_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_time_stamp.setStatus("current")
_Error13_code_Type = Integer32
_Error13_code_Object = MibScalar
error13_code = _Error13_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 13, 2),
    _Error13_code_Type()
)
error13_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error13_code.setStatus("current")
_Error14_ObjectIdentity = ObjectIdentity
error14 = _Error14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14)
)
_Error14_time_stamp_Type = Integer32
_Error14_time_stamp_Object = MibScalar
error14_time_stamp = _Error14_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 1),
    _Error14_time_stamp_Type()
)
error14_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_time_stamp.setStatus("current")
_Error14_code_Type = Integer32
_Error14_code_Object = MibScalar
error14_code = _Error14_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 14, 2),
    _Error14_code_Type()
)
error14_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error14_code.setStatus("current")
_Error15_ObjectIdentity = ObjectIdentity
error15 = _Error15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15)
)
_Error15_time_stamp_Type = Integer32
_Error15_time_stamp_Object = MibScalar
error15_time_stamp = _Error15_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 1),
    _Error15_time_stamp_Type()
)
error15_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_time_stamp.setStatus("current")
_Error15_code_Type = Integer32
_Error15_code_Object = MibScalar
error15_code = _Error15_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 15, 2),
    _Error15_code_Type()
)
error15_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error15_code.setStatus("current")
_Error16_ObjectIdentity = ObjectIdentity
error16 = _Error16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 16)
)
_Error16_time_stamp_Type = Integer32
_Error16_time_stamp_Object = MibScalar
error16_time_stamp = _Error16_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 16, 1),
    _Error16_time_stamp_Type()
)
error16_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error16_time_stamp.setStatus("current")
_Error16_code_Type = Integer32
_Error16_code_Object = MibScalar
error16_code = _Error16_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 16, 2),
    _Error16_code_Type()
)
error16_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error16_code.setStatus("current")
_Error17_ObjectIdentity = ObjectIdentity
error17 = _Error17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 17)
)
_Error17_time_stamp_Type = Integer32
_Error17_time_stamp_Object = MibScalar
error17_time_stamp = _Error17_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 17, 1),
    _Error17_time_stamp_Type()
)
error17_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error17_time_stamp.setStatus("current")
_Error17_code_Type = Integer32
_Error17_code_Object = MibScalar
error17_code = _Error17_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 17, 2),
    _Error17_code_Type()
)
error17_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error17_code.setStatus("current")
_Error18_ObjectIdentity = ObjectIdentity
error18 = _Error18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 18)
)
_Error18_time_stamp_Type = Integer32
_Error18_time_stamp_Object = MibScalar
error18_time_stamp = _Error18_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 18, 1),
    _Error18_time_stamp_Type()
)
error18_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error18_time_stamp.setStatus("current")
_Error18_code_Type = Integer32
_Error18_code_Object = MibScalar
error18_code = _Error18_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 18, 2),
    _Error18_code_Type()
)
error18_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error18_code.setStatus("current")
_Error19_ObjectIdentity = ObjectIdentity
error19 = _Error19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 19)
)
_Error19_time_stamp_Type = Integer32
_Error19_time_stamp_Object = MibScalar
error19_time_stamp = _Error19_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 19, 1),
    _Error19_time_stamp_Type()
)
error19_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error19_time_stamp.setStatus("current")
_Error19_code_Type = Integer32
_Error19_code_Object = MibScalar
error19_code = _Error19_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 19, 2),
    _Error19_code_Type()
)
error19_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error19_code.setStatus("current")
_Error20_ObjectIdentity = ObjectIdentity
error20 = _Error20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 20)
)
_Error20_time_stamp_Type = Integer32
_Error20_time_stamp_Object = MibScalar
error20_time_stamp = _Error20_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 20, 1),
    _Error20_time_stamp_Type()
)
error20_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error20_time_stamp.setStatus("current")
_Error20_code_Type = Integer32
_Error20_code_Object = MibScalar
error20_code = _Error20_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 20, 2),
    _Error20_code_Type()
)
error20_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error20_code.setStatus("current")
_Error21_ObjectIdentity = ObjectIdentity
error21 = _Error21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 21)
)
_Error21_time_stamp_Type = Integer32
_Error21_time_stamp_Object = MibScalar
error21_time_stamp = _Error21_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 21, 1),
    _Error21_time_stamp_Type()
)
error21_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error21_time_stamp.setStatus("current")
_Error21_code_Type = Integer32
_Error21_code_Object = MibScalar
error21_code = _Error21_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 21, 2),
    _Error21_code_Type()
)
error21_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error21_code.setStatus("current")
_Error22_ObjectIdentity = ObjectIdentity
error22 = _Error22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 22)
)
_Error22_time_stamp_Type = Integer32
_Error22_time_stamp_Object = MibScalar
error22_time_stamp = _Error22_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 22, 1),
    _Error22_time_stamp_Type()
)
error22_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error22_time_stamp.setStatus("current")
_Error22_code_Type = Integer32
_Error22_code_Object = MibScalar
error22_code = _Error22_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 22, 2),
    _Error22_code_Type()
)
error22_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error22_code.setStatus("current")
_Error23_ObjectIdentity = ObjectIdentity
error23 = _Error23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 23)
)
_Error23_time_stamp_Type = Integer32
_Error23_time_stamp_Object = MibScalar
error23_time_stamp = _Error23_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 23, 1),
    _Error23_time_stamp_Type()
)
error23_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error23_time_stamp.setStatus("current")
_Error23_code_Type = Integer32
_Error23_code_Object = MibScalar
error23_code = _Error23_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 23, 2),
    _Error23_code_Type()
)
error23_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error23_code.setStatus("current")
_Error24_ObjectIdentity = ObjectIdentity
error24 = _Error24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 24)
)
_Error24_time_stamp_Type = Integer32
_Error24_time_stamp_Object = MibScalar
error24_time_stamp = _Error24_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 24, 1),
    _Error24_time_stamp_Type()
)
error24_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error24_time_stamp.setStatus("current")
_Error24_code_Type = Integer32
_Error24_code_Object = MibScalar
error24_code = _Error24_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 24, 2),
    _Error24_code_Type()
)
error24_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error24_code.setStatus("current")
_Error25_ObjectIdentity = ObjectIdentity
error25 = _Error25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 25)
)
_Error25_time_stamp_Type = Integer32
_Error25_time_stamp_Object = MibScalar
error25_time_stamp = _Error25_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 25, 1),
    _Error25_time_stamp_Type()
)
error25_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error25_time_stamp.setStatus("current")
_Error25_code_Type = Integer32
_Error25_code_Object = MibScalar
error25_code = _Error25_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 25, 2),
    _Error25_code_Type()
)
error25_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error25_code.setStatus("current")
_Error26_ObjectIdentity = ObjectIdentity
error26 = _Error26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 26)
)
_Error26_time_stamp_Type = Integer32
_Error26_time_stamp_Object = MibScalar
error26_time_stamp = _Error26_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 26, 1),
    _Error26_time_stamp_Type()
)
error26_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error26_time_stamp.setStatus("current")
_Error26_code_Type = Integer32
_Error26_code_Object = MibScalar
error26_code = _Error26_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 26, 2),
    _Error26_code_Type()
)
error26_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error26_code.setStatus("current")
_Error27_ObjectIdentity = ObjectIdentity
error27 = _Error27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 27)
)
_Error27_time_stamp_Type = Integer32
_Error27_time_stamp_Object = MibScalar
error27_time_stamp = _Error27_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 27, 1),
    _Error27_time_stamp_Type()
)
error27_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error27_time_stamp.setStatus("current")
_Error27_code_Type = Integer32
_Error27_code_Object = MibScalar
error27_code = _Error27_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 27, 2),
    _Error27_code_Type()
)
error27_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error27_code.setStatus("current")
_Error28_ObjectIdentity = ObjectIdentity
error28 = _Error28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 28)
)
_Error28_time_stamp_Type = Integer32
_Error28_time_stamp_Object = MibScalar
error28_time_stamp = _Error28_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 28, 1),
    _Error28_time_stamp_Type()
)
error28_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error28_time_stamp.setStatus("current")
_Error28_code_Type = Integer32
_Error28_code_Object = MibScalar
error28_code = _Error28_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 28, 2),
    _Error28_code_Type()
)
error28_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error28_code.setStatus("current")
_Error29_ObjectIdentity = ObjectIdentity
error29 = _Error29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 29)
)
_Error29_time_stamp_Type = Integer32
_Error29_time_stamp_Object = MibScalar
error29_time_stamp = _Error29_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 29, 1),
    _Error29_time_stamp_Type()
)
error29_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error29_time_stamp.setStatus("current")
_Error29_code_Type = Integer32
_Error29_code_Object = MibScalar
error29_code = _Error29_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 29, 2),
    _Error29_code_Type()
)
error29_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error29_code.setStatus("current")
_Error30_ObjectIdentity = ObjectIdentity
error30 = _Error30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 30)
)
_Error30_time_stamp_Type = Integer32
_Error30_time_stamp_Object = MibScalar
error30_time_stamp = _Error30_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 30, 1),
    _Error30_time_stamp_Type()
)
error30_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error30_time_stamp.setStatus("current")
_Error30_code_Type = Integer32
_Error30_code_Object = MibScalar
error30_code = _Error30_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 30, 2),
    _Error30_code_Type()
)
error30_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error30_code.setStatus("current")
_Error31_ObjectIdentity = ObjectIdentity
error31 = _Error31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 31)
)
_Error31_time_stamp_Type = Integer32
_Error31_time_stamp_Object = MibScalar
error31_time_stamp = _Error31_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 31, 1),
    _Error31_time_stamp_Type()
)
error31_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error31_time_stamp.setStatus("current")
_Error31_code_Type = Integer32
_Error31_code_Object = MibScalar
error31_code = _Error31_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 31, 2),
    _Error31_code_Type()
)
error31_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error31_code.setStatus("current")
_Error32_ObjectIdentity = ObjectIdentity
error32 = _Error32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 32)
)
_Error32_time_stamp_Type = Integer32
_Error32_time_stamp_Object = MibScalar
error32_time_stamp = _Error32_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 32, 1),
    _Error32_time_stamp_Type()
)
error32_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error32_time_stamp.setStatus("current")
_Error32_code_Type = Integer32
_Error32_code_Object = MibScalar
error32_code = _Error32_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 32, 2),
    _Error32_code_Type()
)
error32_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error32_code.setStatus("current")
_Error33_ObjectIdentity = ObjectIdentity
error33 = _Error33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 33)
)
_Error33_time_stamp_Type = Integer32
_Error33_time_stamp_Object = MibScalar
error33_time_stamp = _Error33_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 33, 1),
    _Error33_time_stamp_Type()
)
error33_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error33_time_stamp.setStatus("current")
_Error33_code_Type = Integer32
_Error33_code_Object = MibScalar
error33_code = _Error33_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 33, 2),
    _Error33_code_Type()
)
error33_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error33_code.setStatus("current")
_Error34_ObjectIdentity = ObjectIdentity
error34 = _Error34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 34)
)
_Error34_time_stamp_Type = Integer32
_Error34_time_stamp_Object = MibScalar
error34_time_stamp = _Error34_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 34, 1),
    _Error34_time_stamp_Type()
)
error34_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error34_time_stamp.setStatus("current")
_Error34_code_Type = Integer32
_Error34_code_Object = MibScalar
error34_code = _Error34_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 34, 2),
    _Error34_code_Type()
)
error34_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error34_code.setStatus("current")
_Error35_ObjectIdentity = ObjectIdentity
error35 = _Error35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 35)
)
_Error35_time_stamp_Type = Integer32
_Error35_time_stamp_Object = MibScalar
error35_time_stamp = _Error35_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 35, 1),
    _Error35_time_stamp_Type()
)
error35_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error35_time_stamp.setStatus("current")
_Error35_code_Type = Integer32
_Error35_code_Object = MibScalar
error35_code = _Error35_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 35, 2),
    _Error35_code_Type()
)
error35_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error35_code.setStatus("current")
_Error36_ObjectIdentity = ObjectIdentity
error36 = _Error36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 36)
)
_Error36_time_stamp_Type = Integer32
_Error36_time_stamp_Object = MibScalar
error36_time_stamp = _Error36_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 36, 1),
    _Error36_time_stamp_Type()
)
error36_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error36_time_stamp.setStatus("current")
_Error36_code_Type = Integer32
_Error36_code_Object = MibScalar
error36_code = _Error36_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 36, 2),
    _Error36_code_Type()
)
error36_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error36_code.setStatus("current")
_Error37_ObjectIdentity = ObjectIdentity
error37 = _Error37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 37)
)
_Error37_time_stamp_Type = Integer32
_Error37_time_stamp_Object = MibScalar
error37_time_stamp = _Error37_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 37, 1),
    _Error37_time_stamp_Type()
)
error37_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error37_time_stamp.setStatus("current")
_Error37_code_Type = Integer32
_Error37_code_Object = MibScalar
error37_code = _Error37_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 37, 2),
    _Error37_code_Type()
)
error37_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error37_code.setStatus("current")
_Error38_ObjectIdentity = ObjectIdentity
error38 = _Error38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 38)
)
_Error38_time_stamp_Type = Integer32
_Error38_time_stamp_Object = MibScalar
error38_time_stamp = _Error38_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 38, 1),
    _Error38_time_stamp_Type()
)
error38_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error38_time_stamp.setStatus("current")
_Error38_code_Type = Integer32
_Error38_code_Object = MibScalar
error38_code = _Error38_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 38, 2),
    _Error38_code_Type()
)
error38_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error38_code.setStatus("current")
_Error39_ObjectIdentity = ObjectIdentity
error39 = _Error39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 39)
)
_Error39_time_stamp_Type = Integer32
_Error39_time_stamp_Object = MibScalar
error39_time_stamp = _Error39_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 39, 1),
    _Error39_time_stamp_Type()
)
error39_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error39_time_stamp.setStatus("current")
_Error39_code_Type = Integer32
_Error39_code_Object = MibScalar
error39_code = _Error39_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 39, 2),
    _Error39_code_Type()
)
error39_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error39_code.setStatus("current")
_Error40_ObjectIdentity = ObjectIdentity
error40 = _Error40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 40)
)
_Error40_time_stamp_Type = Integer32
_Error40_time_stamp_Object = MibScalar
error40_time_stamp = _Error40_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 40, 1),
    _Error40_time_stamp_Type()
)
error40_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error40_time_stamp.setStatus("current")
_Error40_code_Type = Integer32
_Error40_code_Object = MibScalar
error40_code = _Error40_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 40, 2),
    _Error40_code_Type()
)
error40_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error40_code.setStatus("current")
_Error41_ObjectIdentity = ObjectIdentity
error41 = _Error41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 41)
)
_Error41_time_stamp_Type = Integer32
_Error41_time_stamp_Object = MibScalar
error41_time_stamp = _Error41_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 41, 1),
    _Error41_time_stamp_Type()
)
error41_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error41_time_stamp.setStatus("current")
_Error41_code_Type = Integer32
_Error41_code_Object = MibScalar
error41_code = _Error41_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 41, 2),
    _Error41_code_Type()
)
error41_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error41_code.setStatus("current")
_Error42_ObjectIdentity = ObjectIdentity
error42 = _Error42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 42)
)
_Error42_time_stamp_Type = Integer32
_Error42_time_stamp_Object = MibScalar
error42_time_stamp = _Error42_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 42, 1),
    _Error42_time_stamp_Type()
)
error42_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error42_time_stamp.setStatus("current")
_Error42_code_Type = Integer32
_Error42_code_Object = MibScalar
error42_code = _Error42_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 42, 2),
    _Error42_code_Type()
)
error42_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error42_code.setStatus("current")
_Error43_ObjectIdentity = ObjectIdentity
error43 = _Error43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 43)
)
_Error43_time_stamp_Type = Integer32
_Error43_time_stamp_Object = MibScalar
error43_time_stamp = _Error43_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 43, 1),
    _Error43_time_stamp_Type()
)
error43_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error43_time_stamp.setStatus("current")
_Error43_code_Type = Integer32
_Error43_code_Object = MibScalar
error43_code = _Error43_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 43, 2),
    _Error43_code_Type()
)
error43_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error43_code.setStatus("current")
_Error44_ObjectIdentity = ObjectIdentity
error44 = _Error44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 44)
)
_Error44_time_stamp_Type = Integer32
_Error44_time_stamp_Object = MibScalar
error44_time_stamp = _Error44_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 44, 1),
    _Error44_time_stamp_Type()
)
error44_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error44_time_stamp.setStatus("current")
_Error44_code_Type = Integer32
_Error44_code_Object = MibScalar
error44_code = _Error44_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 44, 2),
    _Error44_code_Type()
)
error44_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error44_code.setStatus("current")
_Error45_ObjectIdentity = ObjectIdentity
error45 = _Error45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 45)
)
_Error45_time_stamp_Type = Integer32
_Error45_time_stamp_Object = MibScalar
error45_time_stamp = _Error45_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 45, 1),
    _Error45_time_stamp_Type()
)
error45_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error45_time_stamp.setStatus("current")
_Error45_code_Type = Integer32
_Error45_code_Object = MibScalar
error45_code = _Error45_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 45, 2),
    _Error45_code_Type()
)
error45_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error45_code.setStatus("current")
_Error46_ObjectIdentity = ObjectIdentity
error46 = _Error46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 46)
)
_Error46_time_stamp_Type = Integer32
_Error46_time_stamp_Object = MibScalar
error46_time_stamp = _Error46_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 46, 1),
    _Error46_time_stamp_Type()
)
error46_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error46_time_stamp.setStatus("current")
_Error46_code_Type = Integer32
_Error46_code_Object = MibScalar
error46_code = _Error46_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 46, 2),
    _Error46_code_Type()
)
error46_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error46_code.setStatus("current")
_Error47_ObjectIdentity = ObjectIdentity
error47 = _Error47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 47)
)
_Error47_time_stamp_Type = Integer32
_Error47_time_stamp_Object = MibScalar
error47_time_stamp = _Error47_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 47, 1),
    _Error47_time_stamp_Type()
)
error47_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error47_time_stamp.setStatus("current")
_Error47_code_Type = Integer32
_Error47_code_Object = MibScalar
error47_code = _Error47_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 47, 2),
    _Error47_code_Type()
)
error47_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error47_code.setStatus("current")
_Error48_ObjectIdentity = ObjectIdentity
error48 = _Error48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 48)
)
_Error48_time_stamp_Type = Integer32
_Error48_time_stamp_Object = MibScalar
error48_time_stamp = _Error48_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 48, 1),
    _Error48_time_stamp_Type()
)
error48_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error48_time_stamp.setStatus("current")
_Error48_code_Type = Integer32
_Error48_code_Object = MibScalar
error48_code = _Error48_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 48, 2),
    _Error48_code_Type()
)
error48_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error48_code.setStatus("current")
_Error49_ObjectIdentity = ObjectIdentity
error49 = _Error49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 49)
)
_Error49_time_stamp_Type = Integer32
_Error49_time_stamp_Object = MibScalar
error49_time_stamp = _Error49_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 49, 1),
    _Error49_time_stamp_Type()
)
error49_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error49_time_stamp.setStatus("current")
_Error49_code_Type = Integer32
_Error49_code_Object = MibScalar
error49_code = _Error49_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 49, 2),
    _Error49_code_Type()
)
error49_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error49_code.setStatus("current")
_Error50_ObjectIdentity = ObjectIdentity
error50 = _Error50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 50)
)
_Error50_time_stamp_Type = Integer32
_Error50_time_stamp_Object = MibScalar
error50_time_stamp = _Error50_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 50, 1),
    _Error50_time_stamp_Type()
)
error50_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error50_time_stamp.setStatus("current")
_Error50_code_Type = Integer32
_Error50_code_Object = MibScalar
error50_code = _Error50_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 50, 2),
    _Error50_code_Type()
)
error50_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    error50_code.setStatus("current")
_Error51_ObjectIdentity = ObjectIdentity
error51 = _Error51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 51)
)
_Error52_ObjectIdentity = ObjectIdentity
error52 = _Error52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 52)
)
_Error53_ObjectIdentity = ObjectIdentity
error53 = _Error53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 53)
)
_Error54_ObjectIdentity = ObjectIdentity
error54 = _Error54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 54)
)
_Error55_ObjectIdentity = ObjectIdentity
error55 = _Error55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 55)
)
_Error56_ObjectIdentity = ObjectIdentity
error56 = _Error56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 56)
)
_Error57_ObjectIdentity = ObjectIdentity
error57 = _Error57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 57)
)
_Error58_ObjectIdentity = ObjectIdentity
error58 = _Error58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 58)
)
_Error59_ObjectIdentity = ObjectIdentity
error59 = _Error59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 59)
)
_Error60_ObjectIdentity = ObjectIdentity
error60 = _Error60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 60)
)
_Error61_ObjectIdentity = ObjectIdentity
error61 = _Error61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 61)
)
_Error62_ObjectIdentity = ObjectIdentity
error62 = _Error62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 62)
)
_Error63_ObjectIdentity = ObjectIdentity
error63 = _Error63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 63)
)
_Error64_ObjectIdentity = ObjectIdentity
error64 = _Error64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 64)
)
_Error65_ObjectIdentity = ObjectIdentity
error65 = _Error65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 65)
)
_Error66_ObjectIdentity = ObjectIdentity
error66 = _Error66_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 66)
)
_Error67_ObjectIdentity = ObjectIdentity
error67 = _Error67_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 67)
)
_Error68_ObjectIdentity = ObjectIdentity
error68 = _Error68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 68)
)
_Error69_ObjectIdentity = ObjectIdentity
error69 = _Error69_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 69)
)
_Error70_ObjectIdentity = ObjectIdentity
error70 = _Error70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 70)
)
_Error71_ObjectIdentity = ObjectIdentity
error71 = _Error71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 71)
)
_Error72_ObjectIdentity = ObjectIdentity
error72 = _Error72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 72)
)
_Error73_ObjectIdentity = ObjectIdentity
error73 = _Error73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 73)
)
_Error74_ObjectIdentity = ObjectIdentity
error74 = _Error74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 74)
)
_Error75_ObjectIdentity = ObjectIdentity
error75 = _Error75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 75)
)
_Error76_ObjectIdentity = ObjectIdentity
error76 = _Error76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 76)
)
_Error77_ObjectIdentity = ObjectIdentity
error77 = _Error77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 77)
)
_Error78_ObjectIdentity = ObjectIdentity
error78 = _Error78_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 78)
)
_Error79_ObjectIdentity = ObjectIdentity
error79 = _Error79_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 79)
)
_Error80_ObjectIdentity = ObjectIdentity
error80 = _Error80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 80)
)
_Error81_ObjectIdentity = ObjectIdentity
error81 = _Error81_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 81)
)
_Error82_ObjectIdentity = ObjectIdentity
error82 = _Error82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 82)
)
_Error83_ObjectIdentity = ObjectIdentity
error83 = _Error83_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 83)
)
_Error84_ObjectIdentity = ObjectIdentity
error84 = _Error84_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 84)
)
_Error85_ObjectIdentity = ObjectIdentity
error85 = _Error85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 85)
)
_Error86_ObjectIdentity = ObjectIdentity
error86 = _Error86_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 86)
)
_Error87_ObjectIdentity = ObjectIdentity
error87 = _Error87_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 87)
)
_Error88_ObjectIdentity = ObjectIdentity
error88 = _Error88_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 88)
)
_Error89_ObjectIdentity = ObjectIdentity
error89 = _Error89_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 89)
)
_Error90_ObjectIdentity = ObjectIdentity
error90 = _Error90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 11, 90)
)
_Resource_manager_ObjectIdentity = ObjectIdentity
resource_manager = _Resource_manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12)
)
_Mass_storage_resources_ObjectIdentity = ObjectIdentity
mass_storage_resources = _Mass_storage_resources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12, 3)
)
_Mass_storage_resource_change_counter_Type = Integer32
_Mass_storage_resource_change_counter_Object = MibScalar
mass_storage_resource_change_counter = _Mass_storage_resource_change_counter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12, 3, 1),
    _Mass_storage_resource_change_counter_Type()
)
mass_storage_resource_change_counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mass_storage_resource_change_counter.setStatus("current")


class _Mass_storage_resource_changed_Type(Integer32):
    """Custom type mass_storage_resource_changed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eTrue", 2)
    )


_Mass_storage_resource_changed_Type.__name__ = "Integer32"
_Mass_storage_resource_changed_Object = MibScalar
mass_storage_resource_changed = _Mass_storage_resource_changed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 12, 3, 2),
    _Mass_storage_resource_changed_Type()
)
mass_storage_resource_changed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mass_storage_resource_changed.setStatus("current")
_Remote_procedure_call_ObjectIdentity = ObjectIdentity
remote_procedure_call = _Remote_procedure_call_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13)
)
_Settings_rpc_ObjectIdentity = ObjectIdentity
settings_rpc = _Settings_rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 1)
)
_Rpc_test_return_code_Type = OctetString
_Rpc_test_return_code_Object = MibScalar
rpc_test_return_code = _Rpc_test_return_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 1, 1),
    _Rpc_test_return_code_Type()
)
rpc_test_return_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpc_test_return_code.setStatus("current")
_Rpc_bind_protocol_address_Type = OctetString
_Rpc_bind_protocol_address_Object = MibScalar
rpc_bind_protocol_address = _Rpc_bind_protocol_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 1, 2),
    _Rpc_bind_protocol_address_Type()
)
rpc_bind_protocol_address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpc_bind_protocol_address.setStatus("current")
_Status_rpc_ObjectIdentity = ObjectIdentity
status_rpc = _Status_rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 2)
)
_Rpc_statistic_successful_Type = Integer32
_Rpc_statistic_successful_Object = MibScalar
rpc_statistic_successful = _Rpc_statistic_successful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 2, 1),
    _Rpc_statistic_successful_Type()
)
rpc_statistic_successful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpc_statistic_successful.setStatus("current")
_Rpc_statistic_unsuccessful_Type = Integer32
_Rpc_statistic_unsuccessful_Object = MibScalar
rpc_statistic_unsuccessful = _Rpc_statistic_unsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 2, 2),
    _Rpc_statistic_unsuccessful_Type()
)
rpc_statistic_unsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpc_statistic_unsuccessful.setStatus("current")
_Rpc_bound_protocol_address_Type = OctetString
_Rpc_bound_protocol_address_Object = MibScalar
rpc_bound_protocol_address = _Rpc_bound_protocol_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 2, 3),
    _Rpc_bound_protocol_address_Type()
)
rpc_bound_protocol_address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpc_bound_protocol_address.setStatus("current")
_Rpc_services_ObjectIdentity = ObjectIdentity
rpc_services = _Rpc_services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3)
)
_Mount_ObjectIdentity = ObjectIdentity
mount = _Mount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 1)
)
_Settings_mount_ObjectIdentity = ObjectIdentity
settings_mount = _Settings_mount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 1, 1)
)
_Mount_test_return_code_Type = OctetString
_Mount_test_return_code_Object = MibScalar
mount_test_return_code = _Mount_test_return_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 1, 1, 1),
    _Mount_test_return_code_Type()
)
mount_test_return_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mount_test_return_code.setStatus("current")
_Nfs_server_ObjectIdentity = ObjectIdentity
nfs_server = _Nfs_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2)
)
_Settings_nfs_server_ObjectIdentity = ObjectIdentity
settings_nfs_server = _Settings_nfs_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 1)
)
_Nfs_server_memory_Type = Integer32
_Nfs_server_memory_Object = MibScalar
nfs_server_memory = _Nfs_server_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 1, 1),
    _Nfs_server_memory_Type()
)
nfs_server_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfs_server_memory.setStatus("current")


class _Nfs_server_read_size_Type(Integer32):
    """Custom type nfs_server_read_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_Nfs_server_read_size_Type.__name__ = "Integer32"
_Nfs_server_read_size_Object = MibScalar
nfs_server_read_size = _Nfs_server_read_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 1, 2),
    _Nfs_server_read_size_Type()
)
nfs_server_read_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfs_server_read_size.setStatus("current")


class _Nfs_server_write_size_Type(Integer32):
    """Custom type nfs_server_write_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_Nfs_server_write_size_Type.__name__ = "Integer32"
_Nfs_server_write_size_Object = MibScalar
nfs_server_write_size = _Nfs_server_write_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 1, 3),
    _Nfs_server_write_size_Type()
)
nfs_server_write_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfs_server_write_size.setStatus("current")
_Nfs_server_test_return_code_Type = OctetString
_Nfs_server_test_return_code_Object = MibScalar
nfs_server_test_return_code = _Nfs_server_test_return_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 1, 4),
    _Nfs_server_test_return_code_Type()
)
nfs_server_test_return_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nfs_server_test_return_code.setStatus("current")
_Status_nfs_server_ObjectIdentity = ObjectIdentity
status_nfs_server = _Status_nfs_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 2)
)
_Nfs_server_statistic_successful_Type = Integer32
_Nfs_server_statistic_successful_Object = MibScalar
nfs_server_statistic_successful = _Nfs_server_statistic_successful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 2, 1),
    _Nfs_server_statistic_successful_Type()
)
nfs_server_statistic_successful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfs_server_statistic_successful.setStatus("current")
_Nfs_server_statistic_unsuccessful_Type = Integer32
_Nfs_server_statistic_unsuccessful_Object = MibScalar
nfs_server_statistic_unsuccessful = _Nfs_server_statistic_unsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 2, 2),
    _Nfs_server_statistic_unsuccessful_Type()
)
nfs_server_statistic_unsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfs_server_statistic_unsuccessful.setStatus("current")
_Nfs_server_statistic_current_memory_usage_Type = Integer32
_Nfs_server_statistic_current_memory_usage_Object = MibScalar
nfs_server_statistic_current_memory_usage = _Nfs_server_statistic_current_memory_usage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 2, 4),
    _Nfs_server_statistic_current_memory_usage_Type()
)
nfs_server_statistic_current_memory_usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfs_server_statistic_current_memory_usage.setStatus("current")
_Nfs_server_statistic_max_memory_usage_Type = Integer32
_Nfs_server_statistic_max_memory_usage_Object = MibScalar
nfs_server_statistic_max_memory_usage = _Nfs_server_statistic_max_memory_usage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 2, 2, 5),
    _Nfs_server_statistic_max_memory_usage_Type()
)
nfs_server_statistic_max_memory_usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfs_server_statistic_max_memory_usage.setStatus("current")
_Rpc_bind_ObjectIdentity = ObjectIdentity
rpc_bind = _Rpc_bind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 3)
)
_Settings_rpc_bind_ObjectIdentity = ObjectIdentity
settings_rpc_bind = _Settings_rpc_bind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 3, 1)
)
_Rpc_bind_test_return_code_Type = OctetString
_Rpc_bind_test_return_code_Object = MibScalar
rpc_bind_test_return_code = _Rpc_bind_test_return_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 3, 1, 1),
    _Rpc_bind_test_return_code_Type()
)
rpc_bind_test_return_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpc_bind_test_return_code.setStatus("current")
_Status_rpc_bind_ObjectIdentity = ObjectIdentity
status_rpc_bind = _Status_rpc_bind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 3, 2)
)
_Rpc_bind_statistic_successful_Type = Integer32
_Rpc_bind_statistic_successful_Object = MibScalar
rpc_bind_statistic_successful = _Rpc_bind_statistic_successful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 3, 2, 1),
    _Rpc_bind_statistic_successful_Type()
)
rpc_bind_statistic_successful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpc_bind_statistic_successful.setStatus("current")
_Rpc_bind_statistic_unsuccessful_Type = Integer32
_Rpc_bind_statistic_unsuccessful_Object = MibScalar
rpc_bind_statistic_unsuccessful = _Rpc_bind_statistic_unsuccessful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 13, 3, 3, 2, 2),
    _Rpc_bind_statistic_unsuccessful_Type()
)
rpc_bind_statistic_unsuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpc_bind_statistic_unsuccessful.setStatus("current")
_Xport_interface_ObjectIdentity = ObjectIdentity
xport_interface = _Xport_interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 14)
)
_Status_xip_ObjectIdentity = ObjectIdentity
status_xip = _Status_xip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 14, 2)
)
_Xip_statistic_processed_Type = Integer32
_Xip_statistic_processed_Object = MibScalar
xip_statistic_processed = _Xip_statistic_processed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 14, 2, 1),
    _Xip_statistic_processed_Type()
)
xip_statistic_processed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xip_statistic_processed.setStatus("current")
_Xip_statistic_data_in_dropped_Type = Integer32
_Xip_statistic_data_in_dropped_Object = MibScalar
xip_statistic_data_in_dropped = _Xip_statistic_data_in_dropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 14, 2, 2),
    _Xip_statistic_data_in_dropped_Type()
)
xip_statistic_data_in_dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xip_statistic_data_in_dropped.setStatus("current")
_Mass_storage_block_driver_ObjectIdentity = ObjectIdentity
mass_storage_block_driver = _Mass_storage_block_driver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15)
)
_Settings_mass_storage_bd_ObjectIdentity = ObjectIdentity
settings_mass_storage_bd = _Settings_mass_storage_bd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 1)
)


class _Ram_disk_mode_Type(Integer32):
    """Custom type ram_disk_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2),
          ("eAuto", 3))
    )


_Ram_disk_mode_Type.__name__ = "Integer32"
_Ram_disk_mode_Object = MibScalar
ram_disk_mode = _Ram_disk_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 1, 1),
    _Ram_disk_mode_Type()
)
ram_disk_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ram_disk_mode.setStatus("current")
_Ram_disk_size_Type = Integer32
_Ram_disk_size_Object = MibScalar
ram_disk_size = _Ram_disk_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 1, 2),
    _Ram_disk_size_Type()
)
ram_disk_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ram_disk_size.setStatus("current")
_Status_mass_storage_bd_ObjectIdentity = ObjectIdentity
status_mass_storage_bd = _Status_mass_storage_bd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 2)
)
_Maximum_ram_disk_memory_Type = Integer32
_Maximum_ram_disk_memory_Object = MibScalar
maximum_ram_disk_memory = _Maximum_ram_disk_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 2, 1),
    _Maximum_ram_disk_memory_Type()
)
maximum_ram_disk_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximum_ram_disk_memory.setStatus("current")
_Mass_storage_block_drivers_ObjectIdentity = ObjectIdentity
mass_storage_block_drivers = _Mass_storage_block_drivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 3)
)
_Mass_storage_bd2_ObjectIdentity = ObjectIdentity
mass_storage_bd2 = _Mass_storage_bd2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 3, 2)
)
_Settings_msbd2_ObjectIdentity = ObjectIdentity
settings_msbd2 = _Settings_msbd2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 3, 2, 1)
)
_Disk_storage_block_driver2_test_return_code_Type = OctetString
_Disk_storage_block_driver2_test_return_code_Object = MibScalar
disk_storage_block_driver2_test_return_code = _Disk_storage_block_driver2_test_return_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 15, 3, 2, 1, 1),
    _Disk_storage_block_driver2_test_return_code_Type()
)
disk_storage_block_driver2_test_return_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disk_storage_block_driver2_test_return_code.setStatus("current")
_Accounting_ObjectIdentity = ObjectIdentity
accounting = _Accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16)
)
_Printer_accounting_ObjectIdentity = ObjectIdentity
printer_accounting = _Printer_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1)
)
_Printed_media_usage_ObjectIdentity = ObjectIdentity
printed_media_usage = _Printed_media_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1)
)


class _Printed_media_simplex_count_Type(Integer32):
    """Custom type printed_media_simplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Printed_media_simplex_count_Type.__name__ = "Integer32"
_Printed_media_simplex_count_Object = MibScalar
printed_media_simplex_count = _Printed_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 1),
    _Printed_media_simplex_count_Type()
)
printed_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_simplex_count.setStatus("current")
_Printed_media_simplex_charge_Type = Integer32
_Printed_media_simplex_charge_Object = MibScalar
printed_media_simplex_charge = _Printed_media_simplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 2),
    _Printed_media_simplex_charge_Type()
)
printed_media_simplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printed_media_simplex_charge.setStatus("current")


class _Printed_media_duplex_count_Type(Integer32):
    """Custom type printed_media_duplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Printed_media_duplex_count_Type.__name__ = "Integer32"
_Printed_media_duplex_count_Object = MibScalar
printed_media_duplex_count = _Printed_media_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 3),
    _Printed_media_duplex_count_Type()
)
printed_media_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_duplex_count.setStatus("current")
_Printed_media_duplex_charge_Type = Integer32
_Printed_media_duplex_charge_Object = MibScalar
printed_media_duplex_charge = _Printed_media_duplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 4),
    _Printed_media_duplex_charge_Type()
)
printed_media_duplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printed_media_duplex_charge.setStatus("current")
_Printed_media_total_charge_Type = Integer32
_Printed_media_total_charge_Object = MibScalar
printed_media_total_charge = _Printed_media_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 5),
    _Printed_media_total_charge_Type()
)
printed_media_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_total_charge.setStatus("current")
_Printed_media_combined_total_Type = Integer32
_Printed_media_combined_total_Object = MibScalar
printed_media_combined_total = _Printed_media_combined_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 7),
    _Printed_media_combined_total_Type()
)
printed_media_combined_total.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    printed_media_combined_total.setStatus("current")
_Printed_media_dimplex_count_Type = Integer32
_Printed_media_dimplex_count_Object = MibScalar
printed_media_dimplex_count = _Printed_media_dimplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 10),
    _Printed_media_dimplex_count_Type()
)
printed_media_dimplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_dimplex_count.setStatus("current")
_Printed_media_combined_simplex_count_Type = Integer32
_Printed_media_combined_simplex_count_Object = MibScalar
printed_media_combined_simplex_count = _Printed_media_combined_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 11),
    _Printed_media_combined_simplex_count_Type()
)
printed_media_combined_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_combined_simplex_count.setStatus("current")
_Printed_media_combined_duplex_count_Type = Integer32
_Printed_media_combined_duplex_count_Object = MibScalar
printed_media_combined_duplex_count = _Printed_media_combined_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 12),
    _Printed_media_combined_duplex_count_Type()
)
printed_media_combined_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_combined_duplex_count.setStatus("current")


class _Impression_based_duplex_count_supported_Type(Integer32):
    """Custom type impression_based_duplex_count_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Impression_based_duplex_count_supported_Type.__name__ = "Integer32"
_Impression_based_duplex_count_supported_Object = MibScalar
impression_based_duplex_count_supported = _Impression_based_duplex_count_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 1, 15),
    _Impression_based_duplex_count_supported_Type()
)
impression_based_duplex_count_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    impression_based_duplex_count_supported.setStatus("current")
_Usage_printer_total_charge_Type = Integer32
_Usage_printer_total_charge_Object = MibScalar
usage_printer_total_charge = _Usage_printer_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 2),
    _Usage_printer_total_charge_Type()
)
usage_printer_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_printer_total_charge.setStatus("current")
_Usage_average_toner_coverage_Type = Integer32
_Usage_average_toner_coverage_Object = MibScalar
usage_average_toner_coverage = _Usage_average_toner_coverage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 3),
    _Usage_average_toner_coverage_Type()
)
usage_average_toner_coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_average_toner_coverage.setStatus("current")


class _Usage_staple_count_Type(Integer32):
    """Custom type usage_staple_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Usage_staple_count_Type.__name__ = "Integer32"
_Usage_staple_count_Object = MibScalar
usage_staple_count = _Usage_staple_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 4),
    _Usage_staple_count_Type()
)
usage_staple_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_staple_count.setStatus("current")


class _Usage_instructions_line1_Type(DisplayString):
    """Custom type usage_instructions_line1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line1_Type.__name__ = "DisplayString"
_Usage_instructions_line1_Object = MibScalar
usage_instructions_line1 = _Usage_instructions_line1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 5),
    _Usage_instructions_line1_Type()
)
usage_instructions_line1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line1.setStatus("current")


class _Usage_instructions_line2_Type(DisplayString):
    """Custom type usage_instructions_line2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line2_Type.__name__ = "DisplayString"
_Usage_instructions_line2_Object = MibScalar
usage_instructions_line2 = _Usage_instructions_line2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 6),
    _Usage_instructions_line2_Type()
)
usage_instructions_line2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line2.setStatus("current")


class _Usage_instructions_line3_Type(DisplayString):
    """Custom type usage_instructions_line3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line3_Type.__name__ = "DisplayString"
_Usage_instructions_line3_Object = MibScalar
usage_instructions_line3 = _Usage_instructions_line3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 7),
    _Usage_instructions_line3_Type()
)
usage_instructions_line3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line3.setStatus("current")


class _Usage_instructions_line4_Type(DisplayString):
    """Custom type usage_instructions_line4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Usage_instructions_line4_Type.__name__ = "DisplayString"
_Usage_instructions_line4_Object = MibScalar
usage_instructions_line4 = _Usage_instructions_line4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 8),
    _Usage_instructions_line4_Type()
)
usage_instructions_line4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usage_instructions_line4.setStatus("current")
_Print_meter_usage_ObjectIdentity = ObjectIdentity
print_meter_usage = _Print_meter_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14)
)
_Print_meter_usage_threshold_Type = Integer32
_Print_meter_usage_threshold_Object = MibScalar
print_meter_usage_threshold = _Print_meter_usage_threshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 2),
    _Print_meter_usage_threshold_Type()
)
print_meter_usage_threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_usage_threshold.setStatus("current")


class _Print_meter_print_quality_Type(Integer32):
    """Custom type print_meter_print_quality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ePrintQualityMono", 1),
          ("ePrintQualityGood", 2),
          ("ePrintQualityBest", 3))
    )


_Print_meter_print_quality_Type.__name__ = "Integer32"
_Print_meter_print_quality_Object = MibScalar
print_meter_print_quality = _Print_meter_print_quality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 3),
    _Print_meter_print_quality_Type()
)
print_meter_print_quality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_print_quality.setStatus("current")
_Print_meter_simplex_count_Type = Integer32
_Print_meter_simplex_count_Object = MibScalar
print_meter_simplex_count = _Print_meter_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 4),
    _Print_meter_simplex_count_Type()
)
print_meter_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_simplex_count.setStatus("current")
_Print_meter_duplex_count_Type = Integer32
_Print_meter_duplex_count_Object = MibScalar
print_meter_duplex_count = _Print_meter_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 5),
    _Print_meter_duplex_count_Type()
)
print_meter_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_duplex_count.setStatus("current")
_Print_meter_total_charge_Type = Integer32
_Print_meter_total_charge_Object = MibScalar
print_meter_total_charge = _Print_meter_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 6),
    _Print_meter_total_charge_Type()
)
print_meter_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_total_charge.setStatus("current")
_Print_meter_dimplex_count_Type = Integer32
_Print_meter_dimplex_count_Object = MibScalar
print_meter_dimplex_count = _Print_meter_dimplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 7),
    _Print_meter_dimplex_count_Type()
)
print_meter_dimplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_dimplex_count.setStatus("current")
_Print_meter_simplex_total_Type = Integer32
_Print_meter_simplex_total_Object = MibScalar
print_meter_simplex_total = _Print_meter_simplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 8),
    _Print_meter_simplex_total_Type()
)
print_meter_simplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_simplex_total.setStatus("current")
_Print_meter_duplex_total_Type = Integer32
_Print_meter_duplex_total_Object = MibScalar
print_meter_duplex_total = _Print_meter_duplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 9),
    _Print_meter_duplex_total_Type()
)
print_meter_duplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_duplex_total.setStatus("current")
_Print_meter_category_total_Type = Integer32
_Print_meter_category_total_Object = MibScalar
print_meter_category_total = _Print_meter_category_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 10),
    _Print_meter_category_total_Type()
)
print_meter_category_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_category_total.setStatus("current")
_Print_meter_dimplex_total_Type = Integer32
_Print_meter_dimplex_total_Object = MibScalar
print_meter_dimplex_total = _Print_meter_dimplex_total_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 1, 14, 11),
    _Print_meter_dimplex_total_Type()
)
print_meter_dimplex_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_meter_dimplex_total.setStatus("current")
_Scanner_accounting_ObjectIdentity = ObjectIdentity
scanner_accounting = _Scanner_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2)
)
_Scanned_media_usage_ObjectIdentity = ObjectIdentity
scanned_media_usage = _Scanned_media_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1)
)


class _Scanned_media_simplex_count_Type(Integer32):
    """Custom type scanned_media_simplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Scanned_media_simplex_count_Type.__name__ = "Integer32"
_Scanned_media_simplex_count_Object = MibScalar
scanned_media_simplex_count = _Scanned_media_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 1),
    _Scanned_media_simplex_count_Type()
)
scanned_media_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanned_media_simplex_count.setStatus("current")
_Scanned_media_simplex_charge_Type = Integer32
_Scanned_media_simplex_charge_Object = MibScalar
scanned_media_simplex_charge = _Scanned_media_simplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 2),
    _Scanned_media_simplex_charge_Type()
)
scanned_media_simplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanned_media_simplex_charge.setStatus("current")


class _Scanned_media_duplex_count_Type(Integer32):
    """Custom type scanned_media_duplex_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 930576247),
    )


_Scanned_media_duplex_count_Type.__name__ = "Integer32"
_Scanned_media_duplex_count_Object = MibScalar
scanned_media_duplex_count = _Scanned_media_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 3),
    _Scanned_media_duplex_count_Type()
)
scanned_media_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanned_media_duplex_count.setStatus("current")
_Scanned_media_duplex_charge_Type = Integer32
_Scanned_media_duplex_charge_Object = MibScalar
scanned_media_duplex_charge = _Scanned_media_duplex_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 4),
    _Scanned_media_duplex_charge_Type()
)
scanned_media_duplex_charge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanned_media_duplex_charge.setStatus("current")
_Scanned_media_total_charge_Type = Integer32
_Scanned_media_total_charge_Object = MibScalar
scanned_media_total_charge = _Scanned_media_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 1, 5),
    _Scanned_media_total_charge_Type()
)
scanned_media_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanned_media_total_charge.setStatus("current")
_Usage_scanner_total_charge_Type = Integer32
_Usage_scanner_total_charge_Object = MibScalar
usage_scanner_total_charge = _Usage_scanner_total_charge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 2, 2),
    _Usage_scanner_total_charge_Type()
)
usage_scanner_total_charge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usage_scanner_total_charge.setStatus("current")
_Printer_color_accounting_ObjectIdentity = ObjectIdentity
printer_color_accounting = _Printer_color_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3)
)
_Printed_media_color_usage_ObjectIdentity = ObjectIdentity
printed_media_color_usage = _Printed_media_color_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1)
)
_Printed_media_color_simplex_count_Type = Integer32
_Printed_media_color_simplex_count_Object = MibScalar
printed_media_color_simplex_count = _Printed_media_color_simplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 1),
    _Printed_media_color_simplex_count_Type()
)
printed_media_color_simplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_simplex_count.setStatus("current")
_Printed_media_color_duplex_count_Type = Integer32
_Printed_media_color_duplex_count_Object = MibScalar
printed_media_color_duplex_count = _Printed_media_color_duplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 3),
    _Printed_media_color_duplex_count_Type()
)
printed_media_color_duplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_duplex_count.setStatus("current")
_Printed_media_color_total_count_Type = Integer32
_Printed_media_color_total_count_Object = MibScalar
printed_media_color_total_count = _Printed_media_color_total_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 5),
    _Printed_media_color_total_count_Type()
)
printed_media_color_total_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_total_count.setStatus("current")
_Printed_media_color_dimplex_count_Type = Integer32
_Printed_media_color_dimplex_count_Object = MibScalar
printed_media_color_dimplex_count = _Printed_media_color_dimplex_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 3, 1, 6),
    _Printed_media_color_dimplex_count_Type()
)
printed_media_color_dimplex_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_media_color_dimplex_count.setStatus("current")
_Printed_modes_accounting_ObjectIdentity = ObjectIdentity
printed_modes_accounting = _Printed_modes_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4)
)
_Printed_modes_usage_ObjectIdentity = ObjectIdentity
printed_modes_usage = _Printed_modes_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1)
)
_Printed_modes_mono_count_Type = Integer32
_Printed_modes_mono_count_Object = MibScalar
printed_modes_mono_count = _Printed_modes_mono_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1, 1),
    _Printed_modes_mono_count_Type()
)
printed_modes_mono_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_modes_mono_count.setStatus("current")
_Printed_modes_color_count_Type = Integer32
_Printed_modes_color_count_Object = MibScalar
printed_modes_color_count = _Printed_modes_color_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1, 3),
    _Printed_modes_color_count_Type()
)
printed_modes_color_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_modes_color_count.setStatus("current")
_Printed_modes_total_count_Type = Integer32
_Printed_modes_total_count_Object = MibScalar
printed_modes_total_count = _Printed_modes_total_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 4, 1, 5),
    _Printed_modes_total_count_Type()
)
printed_modes_total_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printed_modes_total_count.setStatus("current")
_Source_tray_accounting_ObjectIdentity = ObjectIdentity
source_tray_accounting = _Source_tray_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 5)
)
_Source_tray_usage_ObjectIdentity = ObjectIdentity
source_tray_usage = _Source_tray_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 5, 1)
)
_Source_tray_usage_count_Type = Integer32
_Source_tray_usage_count_Object = MibScalar
source_tray_usage_count = _Source_tray_usage_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 5, 1, 1),
    _Source_tray_usage_count_Type()
)
source_tray_usage_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    source_tray_usage_count.setStatus("current")
_Destination_bin_accounting_ObjectIdentity = ObjectIdentity
destination_bin_accounting = _Destination_bin_accounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 6)
)
_Destination_bin_usage_ObjectIdentity = ObjectIdentity
destination_bin_usage = _Destination_bin_usage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 6, 1)
)
_Destination_bin_usage_count_Type = Integer32
_Destination_bin_usage_count_Object = MibScalar
destination_bin_usage_count = _Destination_bin_usage_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 16, 6, 1, 1),
    _Destination_bin_usage_count_Type()
)
destination_bin_usage_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destination_bin_usage_count.setStatus("current")
_Firmware_download_ObjectIdentity = ObjectIdentity
firmware_download = _Firmware_download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18)
)


class _Firmware_download_write_status_supported_Type(Integer32):
    """Custom type firmware_download_write_status_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Firmware_download_write_status_supported_Type.__name__ = "Integer32"
_Firmware_download_write_status_supported_Object = MibScalar
firmware_download_write_status_supported = _Firmware_download_write_status_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 1),
    _Firmware_download_write_status_supported_Type()
)
firmware_download_write_status_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_write_status_supported.setStatus("current")
_Firmware_download_write_time_Type = Integer32
_Firmware_download_write_time_Object = MibScalar
firmware_download_write_time = _Firmware_download_write_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 2),
    _Firmware_download_write_time_Type()
)
firmware_download_write_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_write_time.setStatus("current")
_Firmware_download_write_count_Type = Integer32
_Firmware_download_write_count_Object = MibScalar
firmware_download_write_count = _Firmware_download_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 3),
    _Firmware_download_write_count_Type()
)
firmware_download_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_write_count.setStatus("current")


class _Firmware_download_current_state_Type(Integer32):
    """Custom type firmware_download_current_state based on Integer32"""
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
        *(("eIdle", 1),
          ("eReceivingImage", 2),
          ("eReceivedImageError", 3),
          ("eVerifyingImage", 4),
          ("eVerifiedImageError", 5),
          ("eWritingImage", 6),
          ("eWritingImageError", 7),
          ("eDownloadComplete", 8),
          ("eOKtoShutDown", 9),
          ("eCancelDownload", 10),
          ("eShuttingDown", 11))
    )


_Firmware_download_current_state_Type.__name__ = "Integer32"
_Firmware_download_current_state_Object = MibScalar
firmware_download_current_state = _Firmware_download_current_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 4),
    _Firmware_download_current_state_Type()
)
firmware_download_current_state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmware_download_current_state.setStatus("current")
_Firmware_download_maximum_write_count_Type = Integer32
_Firmware_download_maximum_write_count_Object = MibScalar
firmware_download_maximum_write_count = _Firmware_download_maximum_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 5),
    _Firmware_download_maximum_write_count_Type()
)
firmware_download_maximum_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_maximum_write_count.setStatus("current")
_Firmware_download_name_Type = DisplayString
_Firmware_download_name_Object = MibScalar
firmware_download_name = _Firmware_download_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 6),
    _Firmware_download_name_Type()
)
firmware_download_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_name.setStatus("current")
_Firmware_download_version_Type = DisplayString
_Firmware_download_version_Object = MibScalar
firmware_download_version = _Firmware_download_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 18, 7),
    _Firmware_download_version_Type()
)
firmware_download_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_download_version.setStatus("current")
_Operating_system_ObjectIdentity = ObjectIdentity
operating_system = _Operating_system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 19)
)
_Upgradable_devices_ObjectIdentity = ObjectIdentity
upgradable_devices = _Upgradable_devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20)
)


class _Upgradable_devices_write_status_supported_Type(Integer32):
    """Custom type upgradable_devices_write_status_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Upgradable_devices_write_status_supported_Type.__name__ = "Integer32"
_Upgradable_devices_write_status_supported_Object = MibScalar
upgradable_devices_write_status_supported = _Upgradable_devices_write_status_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 1),
    _Upgradable_devices_write_status_supported_Type()
)
upgradable_devices_write_status_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_write_status_supported.setStatus("current")
_Upgradable_devices_write_time_Type = Integer32
_Upgradable_devices_write_time_Object = MibScalar
upgradable_devices_write_time = _Upgradable_devices_write_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 2),
    _Upgradable_devices_write_time_Type()
)
upgradable_devices_write_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_write_time.setStatus("current")
_Upgradable_devices_write_count_Type = Integer32
_Upgradable_devices_write_count_Object = MibScalar
upgradable_devices_write_count = _Upgradable_devices_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 3),
    _Upgradable_devices_write_count_Type()
)
upgradable_devices_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_write_count.setStatus("current")


class _Upgradable_devices_current_state_Type(Integer32):
    """Custom type upgradable_devices_current_state based on Integer32"""
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
        *(("eIdle", 1),
          ("eReceivedImage", 2),
          ("eReceivedImageError", 3),
          ("eVerifiedImage", 4),
          ("eVerifiedImageError", 5),
          ("eWritingImage", 6),
          ("eWritingImageError", 7),
          ("eUpgradeComplete", 8))
    )


_Upgradable_devices_current_state_Type.__name__ = "Integer32"
_Upgradable_devices_current_state_Object = MibScalar
upgradable_devices_current_state = _Upgradable_devices_current_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 4),
    _Upgradable_devices_current_state_Type()
)
upgradable_devices_current_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_current_state.setStatus("current")
_Upgradable_devices_max_write_count_Type = Integer32
_Upgradable_devices_max_write_count_Object = MibScalar
upgradable_devices_max_write_count = _Upgradable_devices_max_write_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 5),
    _Upgradable_devices_max_write_count_Type()
)
upgradable_devices_max_write_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_max_write_count.setStatus("current")
_Upgradable_devices_name_Type = DisplayString
_Upgradable_devices_name_Object = MibScalar
upgradable_devices_name = _Upgradable_devices_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 6),
    _Upgradable_devices_name_Type()
)
upgradable_devices_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_name.setStatus("current")
_Upgradable_devices_version_Type = DisplayString
_Upgradable_devices_version_Object = MibScalar
upgradable_devices_version = _Upgradable_devices_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 7),
    _Upgradable_devices_version_Type()
)
upgradable_devices_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradable_devices_version.setStatus("current")


class _Remote_upgrade_enable_Type(Integer32):
    """Custom type remote_upgrade_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Remote_upgrade_enable_Type.__name__ = "Integer32"
_Remote_upgrade_enable_Object = MibScalar
remote_upgrade_enable = _Remote_upgrade_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 20, 8),
    _Remote_upgrade_enable_Type()
)
remote_upgrade_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remote_upgrade_enable.setStatus("current")
_Warninglog_ObjectIdentity = ObjectIdentity
warninglog = _Warninglog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22)
)
_Warning1_ObjectIdentity = ObjectIdentity
warning1 = _Warning1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 1)
)
_Warning2_ObjectIdentity = ObjectIdentity
warning2 = _Warning2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 2)
)
_Warning3_ObjectIdentity = ObjectIdentity
warning3 = _Warning3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 3)
)
_Warning4_ObjectIdentity = ObjectIdentity
warning4 = _Warning4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 4)
)
_Warning5_ObjectIdentity = ObjectIdentity
warning5 = _Warning5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 5)
)
_Warning6_ObjectIdentity = ObjectIdentity
warning6 = _Warning6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 6)
)
_Warning7_ObjectIdentity = ObjectIdentity
warning7 = _Warning7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 7)
)
_Warning8_ObjectIdentity = ObjectIdentity
warning8 = _Warning8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 8)
)
_Warning9_ObjectIdentity = ObjectIdentity
warning9 = _Warning9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 9)
)
_Warning10_ObjectIdentity = ObjectIdentity
warning10 = _Warning10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 10)
)
_Warning11_ObjectIdentity = ObjectIdentity
warning11 = _Warning11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 11)
)
_Warning12_ObjectIdentity = ObjectIdentity
warning12 = _Warning12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 12)
)
_Warning13_ObjectIdentity = ObjectIdentity
warning13 = _Warning13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 13)
)
_Warning14_ObjectIdentity = ObjectIdentity
warning14 = _Warning14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 14)
)
_Warning15_ObjectIdentity = ObjectIdentity
warning15 = _Warning15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 15)
)
_Warning16_ObjectIdentity = ObjectIdentity
warning16 = _Warning16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 16)
)
_Warning17_ObjectIdentity = ObjectIdentity
warning17 = _Warning17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 17)
)
_Warning18_ObjectIdentity = ObjectIdentity
warning18 = _Warning18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 18)
)
_Warning19_ObjectIdentity = ObjectIdentity
warning19 = _Warning19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 19)
)
_Warning20_ObjectIdentity = ObjectIdentity
warning20 = _Warning20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 20)
)
_Warning21_ObjectIdentity = ObjectIdentity
warning21 = _Warning21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 21)
)
_Warning22_ObjectIdentity = ObjectIdentity
warning22 = _Warning22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 22)
)
_Warning23_ObjectIdentity = ObjectIdentity
warning23 = _Warning23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 23)
)
_Warning24_ObjectIdentity = ObjectIdentity
warning24 = _Warning24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 24)
)
_Warning25_ObjectIdentity = ObjectIdentity
warning25 = _Warning25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 25)
)
_Warning26_ObjectIdentity = ObjectIdentity
warning26 = _Warning26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 26)
)
_Warning27_ObjectIdentity = ObjectIdentity
warning27 = _Warning27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 27)
)
_Warning28_ObjectIdentity = ObjectIdentity
warning28 = _Warning28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 28)
)
_Warning29_ObjectIdentity = ObjectIdentity
warning29 = _Warning29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 29)
)
_Warning30_ObjectIdentity = ObjectIdentity
warning30 = _Warning30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 30)
)
_Warning31_ObjectIdentity = ObjectIdentity
warning31 = _Warning31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 31)
)
_Warning32_ObjectIdentity = ObjectIdentity
warning32 = _Warning32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 32)
)
_Warning33_ObjectIdentity = ObjectIdentity
warning33 = _Warning33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 33)
)
_Warning34_ObjectIdentity = ObjectIdentity
warning34 = _Warning34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 34)
)
_Warning35_ObjectIdentity = ObjectIdentity
warning35 = _Warning35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 35)
)
_Warning36_ObjectIdentity = ObjectIdentity
warning36 = _Warning36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 36)
)
_Warning37_ObjectIdentity = ObjectIdentity
warning37 = _Warning37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 37)
)
_Warning38_ObjectIdentity = ObjectIdentity
warning38 = _Warning38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 38)
)
_Warning39_ObjectIdentity = ObjectIdentity
warning39 = _Warning39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 39)
)
_Warning40_ObjectIdentity = ObjectIdentity
warning40 = _Warning40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 40)
)
_Warning41_ObjectIdentity = ObjectIdentity
warning41 = _Warning41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 41)
)
_Warning42_ObjectIdentity = ObjectIdentity
warning42 = _Warning42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 42)
)
_Warning43_ObjectIdentity = ObjectIdentity
warning43 = _Warning43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 43)
)
_Warning44_ObjectIdentity = ObjectIdentity
warning44 = _Warning44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 44)
)
_Warning45_ObjectIdentity = ObjectIdentity
warning45 = _Warning45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 45)
)
_Warning46_ObjectIdentity = ObjectIdentity
warning46 = _Warning46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 46)
)
_Warning47_ObjectIdentity = ObjectIdentity
warning47 = _Warning47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 47)
)
_Warning48_ObjectIdentity = ObjectIdentity
warning48 = _Warning48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 48)
)
_Warning49_ObjectIdentity = ObjectIdentity
warning49 = _Warning49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 49)
)
_Warning50_ObjectIdentity = ObjectIdentity
warning50 = _Warning50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 22, 50)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 23)
)
_Settings_security_ObjectIdentity = ObjectIdentity
settings_security = _Settings_security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 23, 1)
)


class _Supports_pjl_user_groups_Type(Integer32):
    """Custom type supports_pjl_user_groups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Supports_pjl_user_groups_Type.__name__ = "Integer32"
_Supports_pjl_user_groups_Object = MibScalar
supports_pjl_user_groups = _Supports_pjl_user_groups_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 23, 1, 1),
    _Supports_pjl_user_groups_Type()
)
supports_pjl_user_groups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supports_pjl_user_groups.setStatus("current")
_Settings_system2_ObjectIdentity = ObjectIdentity
settings_system2 = _Settings_system2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25)
)
_Toner_miser_plus_value_Type = OctetString
_Toner_miser_plus_value_Object = MibScalar
toner_miser_plus_value = _Toner_miser_plus_value_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 1),
    _Toner_miser_plus_value_Type()
)
toner_miser_plus_value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    toner_miser_plus_value.setStatus("current")


class _Toner_miser_plus_supported_Type(Integer32):
    """Custom type toner_miser_plus_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Toner_miser_plus_supported_Type.__name__ = "Integer32"
_Toner_miser_plus_supported_Object = MibScalar
toner_miser_plus_supported = _Toner_miser_plus_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 2),
    _Toner_miser_plus_supported_Type()
)
toner_miser_plus_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toner_miser_plus_supported.setStatus("current")


class _Protect_ews_info_tab_Type(Integer32):
    """Custom type protect_ews_info_tab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Protect_ews_info_tab_Type.__name__ = "Integer32"
_Protect_ews_info_tab_Object = MibScalar
protect_ews_info_tab = _Protect_ews_info_tab_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 17),
    _Protect_ews_info_tab_Type()
)
protect_ews_info_tab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protect_ews_info_tab.setStatus("current")


class _Eprint_opt_in_Type(Integer32):
    """Custom type eprint_opt_in based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Eprint_opt_in_Type.__name__ = "Integer32"
_Eprint_opt_in_Object = MibScalar
eprint_opt_in = _Eprint_opt_in_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 19),
    _Eprint_opt_in_Type()
)
eprint_opt_in.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_opt_in.setStatus("current")


class _Eprint_enabled_Type(Integer32):
    """Custom type eprint_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Eprint_enabled_Type.__name__ = "Integer32"
_Eprint_enabled_Object = MibScalar
eprint_enabled = _Eprint_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 20),
    _Eprint_enabled_Type()
)
eprint_enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_enabled.setStatus("current")
_Eprint_email_address_Type = OctetString
_Eprint_email_address_Object = MibScalar
eprint_email_address = _Eprint_email_address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 21),
    _Eprint_email_address_Type()
)
eprint_email_address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_email_address.setStatus("current")


class _Eprint_email_Type(Integer32):
    """Custom type eprint_email based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Eprint_email_Type.__name__ = "Integer32"
_Eprint_email_Object = MibScalar
eprint_email = _Eprint_email_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 22),
    _Eprint_email_Type()
)
eprint_email.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_email.setStatus("current")
_Eprint_printer_code_Type = OctetString
_Eprint_printer_code_Object = MibScalar
eprint_printer_code = _Eprint_printer_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 23),
    _Eprint_printer_code_Type()
)
eprint_printer_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_printer_code.setStatus("current")


class _Eprint_hp_web_services_Type(Integer32):
    """Custom type eprint_hp_web_services based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Eprint_hp_web_services_Type.__name__ = "Integer32"
_Eprint_hp_web_services_Object = MibScalar
eprint_hp_web_services = _Eprint_hp_web_services_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 24),
    _Eprint_hp_web_services_Type()
)
eprint_hp_web_services.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_hp_web_services.setStatus("current")


class _Eprint_jdi_interface_Type(Integer32):
    """Custom type eprint_jdi_interface based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("eJDIInterface1", 1),
          ("eJDIInterface2", 2),
          ("eJDIInterface3", 3),
          ("eJDIInterface4", 4),
          ("eJDIInterface5", 5),
          ("eJDIInterface6", 6),
          ("eJDIInterface7", 7),
          ("eJDIInterface8", 8),
          ("eJDIInterface9", 9),
          ("eJDIInterface10", 10))
    )


_Eprint_jdi_interface_Type.__name__ = "Integer32"
_Eprint_jdi_interface_Object = MibScalar
eprint_jdi_interface = _Eprint_jdi_interface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 25),
    _Eprint_jdi_interface_Type()
)
eprint_jdi_interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_jdi_interface.setStatus("current")


class _Eprint_supported_Type(Integer32):
    """Custom type eprint_supported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Eprint_supported_Type.__name__ = "Integer32"
_Eprint_supported_Object = MibScalar
eprint_supported = _Eprint_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 31),
    _Eprint_supported_Type()
)
eprint_supported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_supported.setStatus("current")


class _Eprint_supported_jdi_Type(Integer32):
    """Custom type eprint_supported_jdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Eprint_supported_jdi_Type.__name__ = "Integer32"
_Eprint_supported_jdi_Object = MibScalar
eprint_supported_jdi = _Eprint_supported_jdi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 32),
    _Eprint_supported_jdi_Type()
)
eprint_supported_jdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eprint_supported_jdi.setStatus("current")
_Fax_init_at_command_Type = OctetString
_Fax_init_at_command_Object = MibScalar
fax_init_at_command = _Fax_init_at_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 47),
    _Fax_init_at_command_Type()
)
fax_init_at_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_init_at_command.setStatus("current")
_Set_primary_interface_index_Type = Integer32
_Set_primary_interface_index_Object = MibScalar
set_primary_interface_index = _Set_primary_interface_index_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 59),
    _Set_primary_interface_index_Type()
)
set_primary_interface_index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set_primary_interface_index.setStatus("current")


class _Wireless_direct_print_setting_Type(Integer32):
    """Custom type wireless_direct_print_setting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Wireless_direct_print_setting_Type.__name__ = "Integer32"
_Wireless_direct_print_setting_Object = MibScalar
wireless_direct_print_setting = _Wireless_direct_print_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 1, 25, 60),
    _Wireless_direct_print_setting_Type()
)
wireless_direct_print_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireless_direct_print_setting.setStatus("current")
_Source_subsystem_ObjectIdentity = ObjectIdentity
source_subsystem = _Source_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2)
)
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1)
)
_Settings_io_ObjectIdentity = ObjectIdentity
settings_io = _Settings_io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1)
)


class _Io_timeout_Type(Integer32):
    """Custom type io_timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_Io_timeout_Type.__name__ = "Integer32"
_Io_timeout_Object = MibScalar
io_timeout = _Io_timeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1, 1),
    _Io_timeout_Type()
)
io_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    io_timeout.setStatus("current")


class _Io_switch_Type(Integer32):
    """Custom type io_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eYes", 1)
    )


_Io_switch_Type.__name__ = "Integer32"
_Io_switch_Object = MibScalar
io_switch = _Io_switch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1, 2),
    _Io_switch_Type()
)
io_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    io_switch.setStatus("current")


class _Io_buffering_Type(Integer32):
    """Custom type io_buffering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2),
          ("eAuto", 3))
    )


_Io_buffering_Type.__name__ = "Integer32"
_Io_buffering_Object = MibScalar
io_buffering = _Io_buffering_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1, 5),
    _Io_buffering_Type()
)
io_buffering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    io_buffering.setStatus("current")
_Io_buffer_size_Type = Integer32
_Io_buffer_size_Object = MibScalar
io_buffer_size = _Io_buffer_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1, 6),
    _Io_buffer_size_Type()
)
io_buffer_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    io_buffer_size.setStatus("current")
_Maximum_io_buffering_memory_Type = Integer32
_Maximum_io_buffering_memory_Object = MibScalar
maximum_io_buffering_memory = _Maximum_io_buffering_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 1, 7),
    _Maximum_io_buffering_memory_Type()
)
maximum_io_buffering_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximum_io_buffering_memory.setStatus("current")
_Status_io_ObjectIdentity = ObjectIdentity
status_io = _Status_io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 2)
)
_Not_ready_source_io_Type = OctetString
_Not_ready_source_io_Object = MibScalar
not_ready_source_io = _Not_ready_source_io_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 2, 1),
    _Not_ready_source_io_Type()
)
not_ready_source_io.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_source_io.setStatus("current")
_Status_source_io_Type = OctetString
_Status_source_io_Object = MibScalar
status_source_io = _Status_source_io_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 2, 2),
    _Status_source_io_Type()
)
status_source_io.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_source_io.setStatus("current")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3)
)
_Port1_ObjectIdentity = ObjectIdentity
port1 = _Port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1)
)
_Parallel_ObjectIdentity = ObjectIdentity
parallel = _Parallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1, 1)
)


class _Parallel_speed_Type(Integer32):
    """Custom type parallel_speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eSlow", 1),
          ("eFast", 2))
    )


_Parallel_speed_Type.__name__ = "Integer32"
_Parallel_speed_Object = MibScalar
parallel_speed = _Parallel_speed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1, 1, 4),
    _Parallel_speed_Type()
)
parallel_speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parallel_speed.setStatus("current")


class _Parallel_bidirectionality_Type(Integer32):
    """Custom type parallel_bidirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eUnidirectional", 1),
          ("eBidirectional", 2))
    )


_Parallel_bidirectionality_Type.__name__ = "Integer32"
_Parallel_bidirectionality_Object = MibScalar
parallel_bidirectionality = _Parallel_bidirectionality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1, 1, 5),
    _Parallel_bidirectionality_Type()
)
parallel_bidirectionality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parallel_bidirectionality.setStatus("current")


class _Port1_parallel_speed_Type(Integer32):
    """Custom type port1_parallel_speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eSlow", 1),
          ("eFast", 2))
    )


_Port1_parallel_speed_Type.__name__ = "Integer32"
_Port1_parallel_speed_Object = MibScalar
port1_parallel_speed = _Port1_parallel_speed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1, 4),
    _Port1_parallel_speed_Type()
)
port1_parallel_speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1_parallel_speed.setStatus("current")


class _Port1_parallel_bidirectionality_Type(Integer32):
    """Custom type port1_parallel_bidirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eUnidirectional", 1),
          ("eBidirectional", 2))
    )


_Port1_parallel_bidirectionality_Type.__name__ = "Integer32"
_Port1_parallel_bidirectionality_Object = MibScalar
port1_parallel_bidirectionality = _Port1_parallel_bidirectionality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 1, 3, 1, 5),
    _Port1_parallel_bidirectionality_Type()
)
port1_parallel_bidirectionality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1_parallel_bidirectionality.setStatus("current")
_Scanner_ObjectIdentity = ObjectIdentity
scanner = _Scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2)
)
_Settings_scanner_ObjectIdentity = ObjectIdentity
settings_scanner = _Settings_scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1)
)


class _Scan_contrast_Type(Integer32):
    """Custom type scan_contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_Scan_contrast_Type.__name__ = "Integer32"
_Scan_contrast_Object = MibScalar
scan_contrast = _Scan_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 1),
    _Scan_contrast_Type()
)
scan_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_contrast.setStatus("current")


class _Scan_resolution_Type(OctetString):
    """Custom type scan_resolution based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Scan_resolution_Type.__name__ = "OctetString"
_Scan_resolution_Object = MibScalar
scan_resolution = _Scan_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 2),
    _Scan_resolution_Type()
)
scan_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_resolution.setStatus("current")


class _Scan_pixel_data_type_Type(Integer32):
    """Custom type scan_pixel_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              24)
        )
    )
    namedValues = NamedValues(
        *(("eBiLevelThesholded", 1),
          ("eGrey256", 8),
          ("e24BitColor", 24))
    )


_Scan_pixel_data_type_Type.__name__ = "Integer32"
_Scan_pixel_data_type_Object = MibScalar
scan_pixel_data_type = _Scan_pixel_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 3),
    _Scan_pixel_data_type_Type()
)
scan_pixel_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_pixel_data_type.setStatus("current")


class _Scan_compression_Type(Integer32):
    """Custom type scan_compression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("eCompressNone", 1),
          ("eCompressDefault", 2),
          ("eCompressionMMR", 5),
          ("eCompressionJPEG", 6))
    )


_Scan_compression_Type.__name__ = "Integer32"
_Scan_compression_Object = MibScalar
scan_compression = _Scan_compression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 4),
    _Scan_compression_Type()
)
scan_compression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_compression.setStatus("current")


class _Scan_compression_factor_Type(Integer32):
    """Custom type scan_compression_factor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Scan_compression_factor_Type.__name__ = "Integer32"
_Scan_compression_factor_Object = MibScalar
scan_compression_factor = _Scan_compression_factor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 5),
    _Scan_compression_factor_Type()
)
scan_compression_factor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_compression_factor.setStatus("current")
_Scan_upload_error_Type = Integer32
_Scan_upload_error_Object = MibScalar
scan_upload_error = _Scan_upload_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 6),
    _Scan_upload_error_Type()
)
scan_upload_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_upload_error.setStatus("current")


class _Scan_upload_Type(Integer32):
    """Custom type scan_upload based on Integer32"""
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
        *(("eScanUploadIdle", 1),
          ("eScanUploadStart", 2),
          ("eScanUploadActive", 3),
          ("eScanUploadAborted", 4),
          ("eScanUploadDone", 5),
          ("eScanUploadNewPage", 6))
    )


_Scan_upload_Type.__name__ = "Integer32"
_Scan_upload_Object = MibScalar
scan_upload = _Scan_upload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 12),
    _Scan_upload_Type()
)
scan_upload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_upload.setStatus("current")


class _Default_scanner_margin_left_Type(Integer32):
    """Custom type default_scanner_margin_left based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5088),
    )


_Default_scanner_margin_left_Type.__name__ = "Integer32"
_Default_scanner_margin_left_Object = MibScalar
default_scanner_margin_left = _Default_scanner_margin_left_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 16),
    _Default_scanner_margin_left_Type()
)
default_scanner_margin_left.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scanner_margin_left.setStatus("current")


class _Default_scanner_margin_right_Type(Integer32):
    """Custom type default_scanner_margin_right based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 5120),
    )


_Default_scanner_margin_right_Type.__name__ = "Integer32"
_Default_scanner_margin_right_Object = MibScalar
default_scanner_margin_right = _Default_scanner_margin_right_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 17),
    _Default_scanner_margin_right_Type()
)
default_scanner_margin_right.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_scanner_margin_right.setStatus("current")


class _Scanner_accessory_serial_number_Type(Integer32):
    """Custom type scanner_accessory_serial_number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Scanner_accessory_serial_number_Type.__name__ = "Integer32"
_Scanner_accessory_serial_number_Object = MibScalar
scanner_accessory_serial_number = _Scanner_accessory_serial_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 18),
    _Scanner_accessory_serial_number_Type()
)
scanner_accessory_serial_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_serial_number.setStatus("current")


class _Scanner_accessory_model_number_Type(DisplayString):
    """Custom type scanner_accessory_model_number based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Scanner_accessory_model_number_Type.__name__ = "DisplayString"
_Scanner_accessory_model_number_Object = MibScalar
scanner_accessory_model_number = _Scanner_accessory_model_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 19),
    _Scanner_accessory_model_number_Type()
)
scanner_accessory_model_number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_model_number.setStatus("current")


class _Scanner_accessory_adf_sheet_count_Type(Integer32):
    """Custom type scanner_accessory_adf_sheet_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_adf_sheet_count_Type.__name__ = "Integer32"
_Scanner_accessory_adf_sheet_count_Object = MibScalar
scanner_accessory_adf_sheet_count = _Scanner_accessory_adf_sheet_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 20),
    _Scanner_accessory_adf_sheet_count_Type()
)
scanner_accessory_adf_sheet_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_adf_sheet_count.setStatus("current")


class _Scanner_accessory_flatbed_scan_count_Type(Integer32):
    """Custom type scanner_accessory_flatbed_scan_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_flatbed_scan_count_Type.__name__ = "Integer32"
_Scanner_accessory_flatbed_scan_count_Object = MibScalar
scanner_accessory_flatbed_scan_count = _Scanner_accessory_flatbed_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 21),
    _Scanner_accessory_flatbed_scan_count_Type()
)
scanner_accessory_flatbed_scan_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_flatbed_scan_count.setStatus("current")


class _Scanner_accessory_cleaning_interval_Type(Integer32):
    """Custom type scanner_accessory_cleaning_interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_cleaning_interval_Type.__name__ = "Integer32"
_Scanner_accessory_cleaning_interval_Object = MibScalar
scanner_accessory_cleaning_interval = _Scanner_accessory_cleaning_interval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 22),
    _Scanner_accessory_cleaning_interval_Type()
)
scanner_accessory_cleaning_interval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_cleaning_interval.setStatus("current")


class _Scanner_accessory_cleaning_count_Type(Integer32):
    """Custom type scanner_accessory_cleaning_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_cleaning_count_Type.__name__ = "Integer32"
_Scanner_accessory_cleaning_count_Object = MibScalar
scanner_accessory_cleaning_count = _Scanner_accessory_cleaning_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 23),
    _Scanner_accessory_cleaning_count_Type()
)
scanner_accessory_cleaning_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_cleaning_count.setStatus("current")


class _Scanner_accessory_maintenance_interval_Type(Integer32):
    """Custom type scanner_accessory_maintenance_interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_maintenance_interval_Type.__name__ = "Integer32"
_Scanner_accessory_maintenance_interval_Object = MibScalar
scanner_accessory_maintenance_interval = _Scanner_accessory_maintenance_interval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 24),
    _Scanner_accessory_maintenance_interval_Type()
)
scanner_accessory_maintenance_interval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_maintenance_interval.setStatus("current")


class _Scanner_accessory_maintenance_count_Type(Integer32):
    """Custom type scanner_accessory_maintenance_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Scanner_accessory_maintenance_count_Type.__name__ = "Integer32"
_Scanner_accessory_maintenance_count_Object = MibScalar
scanner_accessory_maintenance_count = _Scanner_accessory_maintenance_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 25),
    _Scanner_accessory_maintenance_count_Type()
)
scanner_accessory_maintenance_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_maintenance_count.setStatus("current")


class _Scanner_accessory_rom_revision_Type(DisplayString):
    """Custom type scanner_accessory_rom_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Scanner_accessory_rom_revision_Type.__name__ = "DisplayString"
_Scanner_accessory_rom_revision_Object = MibScalar
scanner_accessory_rom_revision = _Scanner_accessory_rom_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 26),
    _Scanner_accessory_rom_revision_Type()
)
scanner_accessory_rom_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_rom_revision.setStatus("current")


class _Scanner_accessory_copy_processor_boot_revision_Type(DisplayString):
    """Custom type scanner_accessory_copy_processor_boot_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Scanner_accessory_copy_processor_boot_revision_Type.__name__ = "DisplayString"
_Scanner_accessory_copy_processor_boot_revision_Object = MibScalar
scanner_accessory_copy_processor_boot_revision = _Scanner_accessory_copy_processor_boot_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 27),
    _Scanner_accessory_copy_processor_boot_revision_Type()
)
scanner_accessory_copy_processor_boot_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_copy_processor_boot_revision.setStatus("current")


class _Scanner_accessory_copy_processor_runtime_revision_Type(DisplayString):
    """Custom type scanner_accessory_copy_processor_runtime_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Scanner_accessory_copy_processor_runtime_revision_Type.__name__ = "DisplayString"
_Scanner_accessory_copy_processor_runtime_revision_Object = MibScalar
scanner_accessory_copy_processor_runtime_revision = _Scanner_accessory_copy_processor_runtime_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 28),
    _Scanner_accessory_copy_processor_runtime_revision_Type()
)
scanner_accessory_copy_processor_runtime_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_copy_processor_runtime_revision.setStatus("current")


class _Scanner_accessory_service_agent_revision_Type(DisplayString):
    """Custom type scanner_accessory_service_agent_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Scanner_accessory_service_agent_revision_Type.__name__ = "DisplayString"
_Scanner_accessory_service_agent_revision_Object = MibScalar
scanner_accessory_service_agent_revision = _Scanner_accessory_service_agent_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 29),
    _Scanner_accessory_service_agent_revision_Type()
)
scanner_accessory_service_agent_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_service_agent_revision.setStatus("current")


class _Scanner_accessory_control_panel_user_interface_revision_Type(DisplayString):
    """Custom type scanner_accessory_control_panel_user_interface_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Scanner_accessory_control_panel_user_interface_revision_Type.__name__ = "DisplayString"
_Scanner_accessory_control_panel_user_interface_revision_Object = MibScalar
scanner_accessory_control_panel_user_interface_revision = _Scanner_accessory_control_panel_user_interface_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 30),
    _Scanner_accessory_control_panel_user_interface_revision_Type()
)
scanner_accessory_control_panel_user_interface_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_control_panel_user_interface_revision.setStatus("current")
_Scan_calibration_ObjectIdentity = ObjectIdentity
scan_calibration = _Scan_calibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 32)
)


class _Scan_calibration_target_Type(Integer32):
    """Custom type scan_calibration_target based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eWhiteSheet", 1),
          ("ePlaten", 2))
    )


_Scan_calibration_target_Type.__name__ = "Integer32"
_Scan_calibration_target_Object = MibScalar
scan_calibration_target = _Scan_calibration_target_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 32, 18),
    _Scan_calibration_target_Type()
)
scan_calibration_target.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_calibration_target.setStatus("current")


class _Scanner_accessory_nvram_Type(OctetString):
    """Custom type scanner_accessory_nvram based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_Scanner_accessory_nvram_Type.__name__ = "OctetString"
_Scanner_accessory_nvram_Object = MibScalar
scanner_accessory_nvram = _Scanner_accessory_nvram_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 33),
    _Scanner_accessory_nvram_Type()
)
scanner_accessory_nvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_nvram.setStatus("current")


class _Scanner_accessory_nvram2_Type(OctetString):
    """Custom type scanner_accessory_nvram2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_Scanner_accessory_nvram2_Type.__name__ = "OctetString"
_Scanner_accessory_nvram2_Object = MibScalar
scanner_accessory_nvram2 = _Scanner_accessory_nvram2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 34),
    _Scanner_accessory_nvram2_Type()
)
scanner_accessory_nvram2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_nvram2.setStatus("current")


class _Scanner_accessory_nvram3_Type(OctetString):
    """Custom type scanner_accessory_nvram3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_Scanner_accessory_nvram3_Type.__name__ = "OctetString"
_Scanner_accessory_nvram3_Object = MibScalar
scanner_accessory_nvram3 = _Scanner_accessory_nvram3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 35),
    _Scanner_accessory_nvram3_Type()
)
scanner_accessory_nvram3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_nvram3.setStatus("current")


class _Scanner_accessory_nvram4_Type(OctetString):
    """Custom type scanner_accessory_nvram4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Scanner_accessory_nvram4_Type.__name__ = "OctetString"
_Scanner_accessory_nvram4_Object = MibScalar
scanner_accessory_nvram4 = _Scanner_accessory_nvram4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 36),
    _Scanner_accessory_nvram4_Type()
)
scanner_accessory_nvram4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_nvram4.setStatus("current")
_Ui_add_option_Type = DisplayString
_Ui_add_option_Object = MibScalar
ui_add_option = _Ui_add_option_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 37),
    _Ui_add_option_Type()
)
ui_add_option.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ui_add_option.setStatus("current")
_Ui_select_option_Type = DisplayString
_Ui_select_option_Object = MibScalar
ui_select_option = _Ui_select_option_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 38),
    _Ui_select_option_Type()
)
ui_select_option.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ui_select_option.setStatus("current")
_Ui_delete_option_Type = DisplayString
_Ui_delete_option_Object = MibScalar
ui_delete_option = _Ui_delete_option_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 42),
    _Ui_delete_option_Type()
)
ui_delete_option.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ui_delete_option.setStatus("current")
_Scanner_jam_page_count_Type = Integer32
_Scanner_jam_page_count_Object = MibScalar
scanner_jam_page_count = _Scanner_jam_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 43),
    _Scanner_jam_page_count_Type()
)
scanner_jam_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_jam_page_count.setStatus("current")
_Scanner_adf_page_count_Type = Integer32
_Scanner_adf_page_count_Object = MibScalar
scanner_adf_page_count = _Scanner_adf_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 44),
    _Scanner_adf_page_count_Type()
)
scanner_adf_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_adf_page_count.setStatus("current")
_Scan_adf_page_count_Type = Integer32
_Scan_adf_page_count_Object = MibScalar
scan_adf_page_count = _Scan_adf_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 45),
    _Scan_adf_page_count_Type()
)
scan_adf_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_adf_page_count.setStatus("current")


class _Scan_image_type_Type(Integer32):
    """Custom type scan_image_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eText", 1),
          ("ePhoto", 2),
          ("eMixed", 3))
    )


_Scan_image_type_Type.__name__ = "Integer32"
_Scan_image_type_Object = MibScalar
scan_image_type = _Scan_image_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 46),
    _Scan_image_type_Type()
)
scan_image_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_image_type.setStatus("current")


class _Scan_subsample_Type(Integer32):
    """Custom type scan_subsample based on Integer32"""
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
        *(("eFourToOneToOne", 1),
          ("eFourToTwoToTwo", 2),
          ("eFourToThreeToThree", 3),
          ("eFourToFourToFour", 4))
    )


_Scan_subsample_Type.__name__ = "Integer32"
_Scan_subsample_Object = MibScalar
scan_subsample = _Scan_subsample_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 47),
    _Scan_subsample_Type()
)
scan_subsample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_subsample.setStatus("current")
_Scanner_retrieve_scanline_Type = OctetString
_Scanner_retrieve_scanline_Object = MibScalar
scanner_retrieve_scanline = _Scanner_retrieve_scanline_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 48),
    _Scanner_retrieve_scanline_Type()
)
scanner_retrieve_scanline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_retrieve_scanline.setStatus("current")
_Scanner_motor_control_Type = Integer32
_Scanner_motor_control_Object = MibScalar
scanner_motor_control = _Scanner_motor_control_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 49),
    _Scanner_motor_control_Type()
)
scanner_motor_control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_motor_control.setStatus("current")


class _Scan_height_Type(Integer32):
    """Custom type scan_height based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25200),
    )


_Scan_height_Type.__name__ = "Integer32"
_Scan_height_Object = MibScalar
scan_height = _Scan_height_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 50),
    _Scan_height_Type()
)
scan_height.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_height.setStatus("current")
_Scanner_scanline_statistics_Type = DisplayString
_Scanner_scanline_statistics_Object = MibScalar
scanner_scanline_statistics = _Scanner_scanline_statistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 51),
    _Scanner_scanline_statistics_Type()
)
scanner_scanline_statistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_scanline_statistics.setStatus("current")
_Scan_control_descriptor_Type = DisplayString
_Scan_control_descriptor_Object = MibScalar
scan_control_descriptor = _Scan_control_descriptor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 52),
    _Scan_control_descriptor_Type()
)
scan_control_descriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_control_descriptor.setStatus("current")


class _Scan_gamma_correction_Type(OctetString):
    """Custom type scan_gamma_correction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Scan_gamma_correction_Type.__name__ = "OctetString"
_Scan_gamma_correction_Object = MibScalar
scan_gamma_correction = _Scan_gamma_correction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 53),
    _Scan_gamma_correction_Type()
)
scan_gamma_correction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_gamma_correction.setStatus("current")


class _Scan_pad_image_Type(Integer32):
    """Custom type scan_pad_image based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Scan_pad_image_Type.__name__ = "Integer32"
_Scan_pad_image_Object = MibScalar
scan_pad_image = _Scan_pad_image_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 54),
    _Scan_pad_image_Type()
)
scan_pad_image.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_pad_image.setStatus("current")
_Scanner_accessory_total_copy_pages_printed_Type = Integer32
_Scanner_accessory_total_copy_pages_printed_Object = MibScalar
scanner_accessory_total_copy_pages_printed = _Scanner_accessory_total_copy_pages_printed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 63),
    _Scanner_accessory_total_copy_pages_printed_Type()
)
scanner_accessory_total_copy_pages_printed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_accessory_total_copy_pages_printed.setStatus("current")
_Scan_flatbed_page_count_Type = Integer32
_Scan_flatbed_page_count_Object = MibScalar
scan_flatbed_page_count = _Scan_flatbed_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 73),
    _Scan_flatbed_page_count_Type()
)
scan_flatbed_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_flatbed_page_count.setStatus("current")
_Scanner_flatbed_page_count_Type = Integer32
_Scanner_flatbed_page_count_Object = MibScalar
scanner_flatbed_page_count = _Scanner_flatbed_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 74),
    _Scanner_flatbed_page_count_Type()
)
scanner_flatbed_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_flatbed_page_count.setStatus("current")
_Scanner_modular_hardware_Type = OctetString
_Scanner_modular_hardware_Object = MibScalar
scanner_modular_hardware = _Scanner_modular_hardware_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 75),
    _Scanner_modular_hardware_Type()
)
scanner_modular_hardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_modular_hardware.setStatus("current")
_Scanner_clock_edge_modifiers_Type = OctetString
_Scanner_clock_edge_modifiers_Object = MibScalar
scanner_clock_edge_modifiers = _Scanner_clock_edge_modifiers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 84),
    _Scanner_clock_edge_modifiers_Type()
)
scanner_clock_edge_modifiers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_clock_edge_modifiers.setStatus("current")
_Scan_clock_edges_Type = OctetString
_Scan_clock_edges_Object = MibScalar
scan_clock_edges = _Scan_clock_edges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 85),
    _Scan_clock_edges_Type()
)
scan_clock_edges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_clock_edges.setStatus("current")


class _Scan_emulate_copy_Type(Integer32):
    """Custom type scan_emulate_copy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eYes", 1),
          ("eNo", 2))
    )


_Scan_emulate_copy_Type.__name__ = "Integer32"
_Scan_emulate_copy_Object = MibScalar
scan_emulate_copy = _Scan_emulate_copy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 1, 86),
    _Scan_emulate_copy_Type()
)
scan_emulate_copy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_emulate_copy.setStatus("current")
_Status_scanner_ObjectIdentity = ObjectIdentity
status_scanner = _Status_scanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2)
)
_Not_ready_source_scanner_Type = OctetString
_Not_ready_source_scanner_Object = MibScalar
not_ready_source_scanner = _Not_ready_source_scanner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 1),
    _Not_ready_source_scanner_Type()
)
not_ready_source_scanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_source_scanner.setStatus("current")
_Scan_resolution_range_Type = DisplayString
_Scan_resolution_range_Object = MibScalar
scan_resolution_range = _Scan_resolution_range_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 3),
    _Scan_resolution_range_Type()
)
scan_resolution_range.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_resolution_range.setStatus("current")
_Scan_calibration_download_Type = OctetString
_Scan_calibration_download_Object = MibScalar
scan_calibration_download = _Scan_calibration_download_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 5),
    _Scan_calibration_download_Type()
)
scan_calibration_download.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_calibration_download.setStatus("current")


class _Scan_calibration_error_Type(Integer32):
    """Custom type scan_calibration_error based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eNoError", 1),
          ("eUnknownCalibrationError", 2),
          ("eScannerFeederEmpty", 3),
          ("eLowMemory", 4),
          ("eWriteFailed", 5),
          ("eScannerBusy", 6),
          ("eADFMispick", 7),
          ("eADFJam", 8),
          ("eUncorrectablePixels", 9))
    )


_Scan_calibration_error_Type.__name__ = "Integer32"
_Scan_calibration_error_Object = MibScalar
scan_calibration_error = _Scan_calibration_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 6),
    _Scan_calibration_error_Type()
)
scan_calibration_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scan_calibration_error.setStatus("current")


class _Scanner_button_status_Type(Integer32):
    """Custom type scanner_button_status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Scanner_button_status_Type.__name__ = "Integer32"
_Scanner_button_status_Object = MibScalar
scanner_button_status = _Scanner_button_status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 7),
    _Scanner_button_status_Type()
)
scanner_button_status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanner_button_status.setStatus("current")
_Scanner_lamp_gain_value_Type = DisplayString
_Scanner_lamp_gain_value_Object = MibScalar
scanner_lamp_gain_value = _Scanner_lamp_gain_value_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 8),
    _Scanner_lamp_gain_value_Type()
)
scanner_lamp_gain_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_lamp_gain_value.setStatus("current")
_Scanner_light_monitor_window_Type = OctetString
_Scanner_light_monitor_window_Object = MibScalar
scanner_light_monitor_window = _Scanner_light_monitor_window_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 9),
    _Scanner_light_monitor_window_Type()
)
scanner_light_monitor_window.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_light_monitor_window.setStatus("current")
_Scanner_reference_position_Type = DisplayString
_Scanner_reference_position_Object = MibScalar
scanner_reference_position = _Scanner_reference_position_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 10),
    _Scanner_reference_position_Type()
)
scanner_reference_position.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_reference_position.setStatus("current")
_Scanner_sensor_manufacturer_Type = DisplayString
_Scanner_sensor_manufacturer_Object = MibScalar
scanner_sensor_manufacturer = _Scanner_sensor_manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 11),
    _Scanner_sensor_manufacturer_Type()
)
scanner_sensor_manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanner_sensor_manufacturer.setStatus("current")
_Copy_scanner_dimensions_Type = DisplayString
_Copy_scanner_dimensions_Object = MibScalar
copy_scanner_dimensions = _Copy_scanner_dimensions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 2, 2, 13),
    _Copy_scanner_dimensions_Type()
)
copy_scanner_dimensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copy_scanner_dimensions.setStatus("current")
_Fax_receive_ObjectIdentity = ObjectIdentity
fax_receive = _Fax_receive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3)
)
_Settings_fax_receive_ObjectIdentity = ObjectIdentity
settings_fax_receive = _Settings_fax_receive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 1)
)


class _Fax_receive_stamping_enable_Type(Integer32):
    """Custom type fax_receive_stamping_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_receive_stamping_enable_Type.__name__ = "Integer32"
_Fax_receive_stamping_enable_Object = MibScalar
fax_receive_stamping_enable = _Fax_receive_stamping_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 1, 1),
    _Fax_receive_stamping_enable_Type()
)
fax_receive_stamping_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_receive_stamping_enable.setStatus("current")
_Status_fax_receive_ObjectIdentity = ObjectIdentity
status_fax_receive = _Status_fax_receive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 2)
)
_Not_ready_fax_receive_Type = OctetString
_Not_ready_fax_receive_Object = MibScalar
not_ready_fax_receive = _Not_ready_fax_receive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 3, 2, 1),
    _Not_ready_fax_receive_Type()
)
not_ready_fax_receive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_fax_receive.setStatus("current")
_Spooler_ObjectIdentity = ObjectIdentity
spooler = _Spooler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 4)
)
_Settings_spooler_ObjectIdentity = ObjectIdentity
settings_spooler = _Settings_spooler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 4, 1)
)


class _Mopy_mode_Type(Integer32):
    """Custom type mopy_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eStandard", 4),
          ("eEnhanced", 5))
    )


_Mopy_mode_Type.__name__ = "Integer32"
_Mopy_mode_Object = MibScalar
mopy_mode = _Mopy_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 2, 4, 1, 1),
    _Mopy_mode_Type()
)
mopy_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mopy_mode.setStatus("current")
_Processing_subsystem_ObjectIdentity = ObjectIdentity
processing_subsystem = _Processing_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3)
)
_Pdl_ObjectIdentity = ObjectIdentity
pdl = _Pdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3)
)
_Settings_pdl_ObjectIdentity = ObjectIdentity
settings_pdl = _Settings_pdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1)
)


class _Default_orientation_Type(Integer32):
    """Custom type default_orientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ePortrait", 1),
          ("eLandscape", 2))
    )


_Default_orientation_Type.__name__ = "Integer32"
_Default_orientation_Object = MibScalar
default_orientation = _Default_orientation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 2),
    _Default_orientation_Type()
)
default_orientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_orientation.setStatus("current")


class _Default_copies_Type(Integer32):
    """Custom type default_copies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_Default_copies_Type.__name__ = "Integer32"
_Default_copies_Object = MibScalar
default_copies = _Default_copies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 4),
    _Default_copies_Type()
)
default_copies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_copies.setStatus("current")


class _Form_feed_Type(Integer32):
    """Custom type form_feed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eInitiateAction", 1)
    )


_Form_feed_Type.__name__ = "Integer32"
_Form_feed_Object = MibScalar
form_feed = _Form_feed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 5),
    _Form_feed_Type()
)
form_feed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    form_feed.setStatus("current")


class _Resource_saving_Type(Integer32):
    """Custom type resource_saving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2),
          ("eAuto", 3))
    )


_Resource_saving_Type.__name__ = "Integer32"
_Resource_saving_Object = MibScalar
resource_saving = _Resource_saving_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 6),
    _Resource_saving_Type()
)
resource_saving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resource_saving.setStatus("current")
_Maximum_resource_saving_memory_Type = Integer32
_Maximum_resource_saving_memory_Object = MibScalar
maximum_resource_saving_memory = _Maximum_resource_saving_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 7),
    _Maximum_resource_saving_memory_Type()
)
maximum_resource_saving_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximum_resource_saving_memory.setStatus("current")
_Default_vertical_black_resolution_Type = Integer32
_Default_vertical_black_resolution_Object = MibScalar
default_vertical_black_resolution = _Default_vertical_black_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 8),
    _Default_vertical_black_resolution_Type()
)
default_vertical_black_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_vertical_black_resolution.setStatus("current")
_Default_horizontal_black_resolution_Type = Integer32
_Default_horizontal_black_resolution_Object = MibScalar
default_horizontal_black_resolution = _Default_horizontal_black_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 9),
    _Default_horizontal_black_resolution_Type()
)
default_horizontal_black_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_horizontal_black_resolution.setStatus("current")


class _Default_page_protect_Type(Integer32):
    """Custom type default_page_protect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOn", 2),
          ("eAuto", 3))
    )


_Default_page_protect_Type.__name__ = "Integer32"
_Default_page_protect_Object = MibScalar
default_page_protect = _Default_page_protect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 10),
    _Default_page_protect_Type()
)
default_page_protect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_page_protect.setStatus("current")
_Default_lines_per_page_Type = Integer32
_Default_lines_per_page_Object = MibScalar
default_lines_per_page = _Default_lines_per_page_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 11),
    _Default_lines_per_page_Type()
)
default_lines_per_page.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_lines_per_page.setStatus("current")
_Default_vmi_Type = Integer32
_Default_vmi_Object = MibScalar
default_vmi = _Default_vmi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 12),
    _Default_vmi_Type()
)
default_vmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_vmi.setStatus("current")


class _Default_media_size_Type(Integer32):
    """Custom type default_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18,
              25,
              26,
              80,
              81,
              90,
              91,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eROC16K", 17),
          ("eJISExecutive", 18),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("eMonarch", 80),
          ("eCommercial10", 81),
          ("eInternationalDL", 90),
          ("eInternationalC5", 91),
          ("eInternationalB5", 100),
          ("eCustom", 101))
    )


_Default_media_size_Type.__name__ = "Integer32"
_Default_media_size_Object = MibScalar
default_media_size = _Default_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 13),
    _Default_media_size_Type()
)
default_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_media_size.setStatus("current")


class _Cold_reset_media_size_Type(Integer32):
    """Custom type cold_reset_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              26)
        )
    )
    namedValues = NamedValues(
        *(("eUSLetter", 2),
          ("eISOandJISA4", 26))
    )


_Cold_reset_media_size_Type.__name__ = "Integer32"
_Cold_reset_media_size_Object = MibScalar
cold_reset_media_size = _Cold_reset_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 19),
    _Cold_reset_media_size_Type()
)
cold_reset_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cold_reset_media_size.setStatus("current")
_Default_media_name_Type = DisplayString
_Default_media_name_Object = MibScalar
default_media_name = _Default_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 22),
    _Default_media_name_Type()
)
default_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_media_name.setStatus("current")


class _Reprint_Type(Integer32):
    """Custom type reprint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2),
          ("eAuto", 3))
    )


_Reprint_Type.__name__ = "Integer32"
_Reprint_Object = MibScalar
reprint = _Reprint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 36),
    _Reprint_Type()
)
reprint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reprint.setStatus("current")


class _Wide_a4_Type(Integer32):
    """Custom type wide_a4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Wide_a4_Type.__name__ = "Integer32"
_Wide_a4_Object = MibScalar
wide_a4 = _Wide_a4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 37),
    _Wide_a4_Type()
)
wide_a4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wide_a4.setStatus("current")


class _Dark_courier_Type(Integer32):
    """Custom type dark_courier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Dark_courier_Type.__name__ = "Integer32"
_Dark_courier_Object = MibScalar
dark_courier = _Dark_courier_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 38),
    _Dark_courier_Type()
)
dark_courier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dark_courier.setStatus("current")
_Default_bits_per_pixel_Type = Integer32
_Default_bits_per_pixel_Object = MibScalar
default_bits_per_pixel = _Default_bits_per_pixel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 1, 39),
    _Default_bits_per_pixel_Type()
)
default_bits_per_pixel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_bits_per_pixel.setStatus("current")
_Status_pdl_ObjectIdentity = ObjectIdentity
status_pdl = _Status_pdl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 2)
)
_Not_ready_processing_pdl_Type = OctetString
_Not_ready_processing_pdl_Object = MibScalar
not_ready_processing_pdl = _Not_ready_processing_pdl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 2, 1),
    _Not_ready_processing_pdl_Type()
)
not_ready_processing_pdl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_processing_pdl.setStatus("current")


class _Form_feed_needed_Type(Integer32):
    """Custom type form_feed_needed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Form_feed_needed_Type.__name__ = "Integer32"
_Form_feed_needed_Object = MibScalar
form_feed_needed = _Form_feed_needed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 2, 2),
    _Form_feed_needed_Type()
)
form_feed_needed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    form_feed_needed.setStatus("current")
_Pdl_pcl_ObjectIdentity = ObjectIdentity
pdl_pcl = _Pdl_pcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3)
)
_Pcl_datecode_Type = DisplayString
_Pcl_datecode_Object = MibScalar
pcl_datecode = _Pcl_datecode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 1),
    _Pcl_datecode_Type()
)
pcl_datecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcl_datecode.setStatus("current")
_Pcl_resource_saving_memory_size_Type = Integer32
_Pcl_resource_saving_memory_size_Object = MibScalar
pcl_resource_saving_memory_size = _Pcl_resource_saving_memory_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 2),
    _Pcl_resource_saving_memory_size_Type()
)
pcl_resource_saving_memory_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_resource_saving_memory_size.setStatus("current")
_Pcl_name_Type = DisplayString
_Pcl_name_Object = MibScalar
pcl_name = _Pcl_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 3),
    _Pcl_name_Type()
)
pcl_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcl_name.setStatus("current")
_Pcl_version_Type = DisplayString
_Pcl_version_Object = MibScalar
pcl_version = _Pcl_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 4),
    _Pcl_version_Type()
)
pcl_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcl_version.setStatus("current")
_Pcl_total_page_count_Type = Integer32
_Pcl_total_page_count_Object = MibScalar
pcl_total_page_count = _Pcl_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 5),
    _Pcl_total_page_count_Type()
)
pcl_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcl_total_page_count.setStatus("current")


class _Pcl_default_symbol_set_Type(Integer32):
    """Custom type pcl_default_symbol_set based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              9,
              14,
              19,
              21,
              37,
              38,
              39,
              53,
              78,
              83,
              173,
              174,
              180,
              202,
              205,
              234,
              269,
              277,
              293,
              308,
              309,
              330,
              341,
              373,
              405,
              426,
              458,
              501,
              565,
              619,
              629)
        )
    )
    namedValues = NamedValues(
        *(("eISO60DanishNorwegian", 4),
          ("eISO15Italian", 9),
          ("eISO88591Latin1ECMA94", 14),
          ("eISO11SwedishforNames", 19),
          ("eISO6ASCII", 21),
          ("eISO4UnitedKingdom", 37),
          ("eISO69French", 38),
          ("eISO21German", 39),
          ("eLegal", 53),
          ("eISO88592Latin2ECMA94", 78),
          ("eISO17Spanish", 83),
          ("ePSMath", 173),
          ("eISO88599Latin5ECMA128", 174),
          ("eWindows31Latin5", 180),
          ("eMicrosoftPublishing", 202),
          ("eVenturaMath", 205),
          ("eDeskTop", 234),
          ("eMath8", 269),
          ("eRoman8", 277),
          ("eWindows31Latin2", 293),
          ("ePC8Turkish", 308),
          ("eWindows30Latin1", 309),
          ("ePSText", 330),
          ("ePC8CodePage437", 341),
          ("ePC8DNDanishNorwegian", 373),
          ("ePC850Multilingual", 405),
          ("eVenturaInternational", 426),
          ("eVenturaUS", 458),
          ("ePiFont", 501),
          ("ePC852Latin2", 565),
          ("eWindows31J", 619),
          ("eWindows31Latin1", 629))
    )


_Pcl_default_symbol_set_Type.__name__ = "Integer32"
_Pcl_default_symbol_set_Object = MibScalar
pcl_default_symbol_set = _Pcl_default_symbol_set_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 11),
    _Pcl_default_symbol_set_Type()
)
pcl_default_symbol_set.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_symbol_set.setStatus("current")
_Pcl_default_font_height_Type = Integer32
_Pcl_default_font_height_Object = MibScalar
pcl_default_font_height = _Pcl_default_font_height_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 13),
    _Pcl_default_font_height_Type()
)
pcl_default_font_height.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_height.setStatus("current")


class _Pcl_default_font_source_Type(Integer32):
    """Custom type pcl_default_font_source based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("eInternal", 1),
          ("ePermanentSoft", 2),
          ("eRomSimm1", 10),
          ("eRomSimm2", 11),
          ("eRomSimm3", 12),
          ("eRomSimm4", 13),
          ("eRomSimm5", 14),
          ("eUsb1", 15),
          ("eUsb2", 16),
          ("eUsb3", 17),
          ("eUsb4", 18))
    )


_Pcl_default_font_source_Type.__name__ = "Integer32"
_Pcl_default_font_source_Object = MibScalar
pcl_default_font_source = _Pcl_default_font_source_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 14),
    _Pcl_default_font_source_Type()
)
pcl_default_font_source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_source.setStatus("current")


class _Pcl_default_font_number_Type(Integer32):
    """Custom type pcl_default_font_number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pcl_default_font_number_Type.__name__ = "Integer32"
_Pcl_default_font_number_Object = MibScalar
pcl_default_font_number = _Pcl_default_font_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 15),
    _Pcl_default_font_number_Type()
)
pcl_default_font_number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_number.setStatus("current")
_Pcl_default_font_width_Type = Integer32
_Pcl_default_font_width_Object = MibScalar
pcl_default_font_width = _Pcl_default_font_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 3, 16),
    _Pcl_default_font_width_Type()
)
pcl_default_font_width.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcl_default_font_width.setStatus("current")
_Pdl_postscript_ObjectIdentity = ObjectIdentity
pdl_postscript = _Pdl_postscript_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4)
)
_Postscript_datecode_Type = DisplayString
_Postscript_datecode_Object = MibScalar
postscript_datecode = _Postscript_datecode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 1),
    _Postscript_datecode_Type()
)
postscript_datecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postscript_datecode.setStatus("current")
_Postscript_resource_saving_memory_size_Type = Integer32
_Postscript_resource_saving_memory_size_Object = MibScalar
postscript_resource_saving_memory_size = _Postscript_resource_saving_memory_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 2),
    _Postscript_resource_saving_memory_size_Type()
)
postscript_resource_saving_memory_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postscript_resource_saving_memory_size.setStatus("current")
_Postscript_name_Type = DisplayString
_Postscript_name_Object = MibScalar
postscript_name = _Postscript_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 3),
    _Postscript_name_Type()
)
postscript_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postscript_name.setStatus("current")
_Postscript_version_Type = DisplayString
_Postscript_version_Object = MibScalar
postscript_version = _Postscript_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 4),
    _Postscript_version_Type()
)
postscript_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postscript_version.setStatus("current")
_Postscript_total_page_count_Type = Integer32
_Postscript_total_page_count_Object = MibScalar
postscript_total_page_count = _Postscript_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 5),
    _Postscript_total_page_count_Type()
)
postscript_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postscript_total_page_count.setStatus("current")


class _Postscript_print_errors_Type(Integer32):
    """Custom type postscript_print_errors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Postscript_print_errors_Type.__name__ = "Integer32"
_Postscript_print_errors_Object = MibScalar
postscript_print_errors = _Postscript_print_errors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 11),
    _Postscript_print_errors_Type()
)
postscript_print_errors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postscript_print_errors.setStatus("current")


class _Postscript_jam_recovery_Type(Integer32):
    """Custom type postscript_jam_recovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Postscript_jam_recovery_Type.__name__ = "Integer32"
_Postscript_jam_recovery_Object = MibScalar
postscript_jam_recovery = _Postscript_jam_recovery_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 12),
    _Postscript_jam_recovery_Type()
)
postscript_jam_recovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postscript_jam_recovery.setStatus("current")


class _Postscript_defer_media_Type(Integer32):
    """Custom type postscript_defer_media based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Postscript_defer_media_Type.__name__ = "Integer32"
_Postscript_defer_media_Object = MibScalar
postscript_defer_media = _Postscript_defer_media_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 4, 14),
    _Postscript_defer_media_Type()
)
postscript_defer_media.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postscript_defer_media.setStatus("current")
_Pdl_esc_p_ObjectIdentity = ObjectIdentity
pdl_esc_p = _Pdl_esc_p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 5)
)
_Esc_p_datecode_Type = DisplayString
_Esc_p_datecode_Object = MibScalar
esc_p_datecode = _Esc_p_datecode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 5, 1),
    _Esc_p_datecode_Type()
)
esc_p_datecode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esc_p_datecode.setStatus("current")
_Esc_p_name_Type = DisplayString
_Esc_p_name_Object = MibScalar
esc_p_name = _Esc_p_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 5, 3),
    _Esc_p_name_Type()
)
esc_p_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esc_p_name.setStatus("current")
_Esc_p_version_Type = DisplayString
_Esc_p_version_Object = MibScalar
esc_p_version = _Esc_p_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 5, 4),
    _Esc_p_version_Type()
)
esc_p_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esc_p_version.setStatus("current")
_Pdl_pdf_ObjectIdentity = ObjectIdentity
pdl_pdf = _Pdl_pdf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15)
)
_Pdf_version_Type = OctetString
_Pdf_version_Object = MibScalar
pdf_version = _Pdf_version_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 1),
    _Pdf_version_Type()
)
pdf_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdf_version.setStatus("current")
_Pdf_total_page_count_Type = Integer32
_Pdf_total_page_count_Object = MibScalar
pdf_total_page_count = _Pdf_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 2),
    _Pdf_total_page_count_Type()
)
pdf_total_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdf_total_page_count.setStatus("current")


class _Pdf_enabled_Type(Integer32):
    """Custom type pdf_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ePDFNotEnabled", 1),
          ("ePDFEnabled", 2))
    )


_Pdf_enabled_Type.__name__ = "Integer32"
_Pdf_enabled_Object = MibScalar
pdf_enabled = _Pdf_enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 3),
    _Pdf_enabled_Type()
)
pdf_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdf_enabled.setStatus("current")


class _Pdf_print_errors_Type(Integer32):
    """Custom type pdf_print_errors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Pdf_print_errors_Type.__name__ = "Integer32"
_Pdf_print_errors_Object = MibScalar
pdf_print_errors = _Pdf_print_errors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 15, 4),
    _Pdf_print_errors_Type()
)
pdf_print_errors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdf_print_errors.setStatus("current")
_Pdl_pclxl_ObjectIdentity = ObjectIdentity
pdl_pclxl = _Pdl_pclxl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 16)
)
_Pclxl_total_page_count_Type = Integer32
_Pclxl_total_page_count_Object = MibScalar
pclxl_total_page_count = _Pclxl_total_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 3, 16, 1),
    _Pclxl_total_page_count_Type()
)
pclxl_total_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pclxl_total_page_count.setStatus("current")
_Pml_ObjectIdentity = ObjectIdentity
pml = _Pml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 4)
)
_Pjl_ObjectIdentity = ObjectIdentity
pjl = _Pjl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 5)
)
_Pjl_password_Type = Integer32
_Pjl_password_Object = MibScalar
pjl_password = _Pjl_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 5, 1),
    _Pjl_password_Type()
)
pjl_password.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pjl_password.setStatus("current")
_Fax_proc_sub_ObjectIdentity = ObjectIdentity
fax_proc_sub = _Fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7)
)
_Settings_fax_proc_sub_ObjectIdentity = ObjectIdentity
settings_fax_proc_sub = _Settings_fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1)
)
_Fax_rxscale_Type = Integer32
_Fax_rxscale_Object = MibScalar
fax_rxscale = _Fax_rxscale_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 1),
    _Fax_rxscale_Type()
)
fax_rxscale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_rxscale.setStatus("current")


class _Fax_noise_volume_Type(Integer32):
    """Custom type fax_noise_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Fax_noise_volume_Type.__name__ = "Integer32"
_Fax_noise_volume_Object = MibScalar
fax_noise_volume = _Fax_noise_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 3),
    _Fax_noise_volume_Type()
)
fax_noise_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_noise_volume.setStatus("current")


class _Fax_download_Type(Integer32):
    """Custom type fax_download based on Integer32"""
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
        *(("eFaxDownloadIdle", 1),
          ("eFaxDownloadStart", 2),
          ("eFaxDownloadActive", 3),
          ("eFaxDownloadAborted", 4),
          ("eFaxDownloadDone", 5))
    )


_Fax_download_Type.__name__ = "Integer32"
_Fax_download_Object = MibScalar
fax_download = _Fax_download_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 6),
    _Fax_download_Type()
)
fax_download.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_download.setStatus("current")


class _Fax_silent_detection_Type(Integer32):
    """Custom type fax_silent_detection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_silent_detection_Type.__name__ = "Integer32"
_Fax_silent_detection_Object = MibScalar
fax_silent_detection = _Fax_silent_detection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 7),
    _Fax_silent_detection_Type()
)
fax_silent_detection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_silent_detection.setStatus("current")


class _Fax_ring_enable_Type(Integer32):
    """Custom type fax_ring_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_ring_enable_Type.__name__ = "Integer32"
_Fax_ring_enable_Object = MibScalar
fax_ring_enable = _Fax_ring_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 8),
    _Fax_ring_enable_Type()
)
fax_ring_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_ring_enable.setStatus("current")


class _Fax_country_Type(Integer32):
    """Custom type fax_country based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              13,
              14,
              15,
              19,
              21,
              23,
              27,
              29,
              30,
              31,
              34,
              35,
              37,
              39,
              40,
              41,
              43,
              44,
              45,
              46,
              47,
              51,
              55,
              56,
              62,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("eChina", 6),
          ("eMexicoAndLatinAmerica", 13),
          ("eCanadaFrench", 14),
          ("eUnitedStatesAndCanadaEnglish", 15),
          ("eNewZealand", 19),
          ("eIsrael", 21),
          ("eAustralia", 23),
          ("eMalaysia", 27),
          ("eHongKong", 29),
          ("eSingapore", 30),
          ("eUnitedKingdom", 31),
          ("eAustria", 34),
          ("eNetherlands", 35),
          ("eSwitzerlandFrench", 37),
          ("eGermany", 39),
          ("eDenmark", 40),
          ("eSweden", 41),
          ("eNorway", 43),
          ("eIreland", 44),
          ("eBelgium", 45),
          ("eFinland", 46),
          ("eFrance", 47),
          ("eItaly", 51),
          ("eSpain", 55),
          ("ePoland", 56),
          ("eHungary", 62),
          ("eUkraine", 63),
          ("eRussia", 64))
    )


_Fax_country_Type.__name__ = "Integer32"
_Fax_country_Object = MibScalar
fax_country = _Fax_country_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 9),
    _Fax_country_Type()
)
fax_country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_country.setStatus("current")
_Fax_tx_phone_number_Type = DisplayString
_Fax_tx_phone_number_Object = MibScalar
fax_tx_phone_number = _Fax_tx_phone_number_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 10),
    _Fax_tx_phone_number_Type()
)
fax_tx_phone_number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_tx_phone_number.setStatus("current")
_Fax_redial_time_Type = Integer32
_Fax_redial_time_Object = MibScalar
fax_redial_time = _Fax_redial_time_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 14),
    _Fax_redial_time_Type()
)
fax_redial_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_redial_time.setStatus("current")
_Fax_pstn_access_code_Type = DisplayString
_Fax_pstn_access_code_Object = MibScalar
fax_pstn_access_code = _Fax_pstn_access_code_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 18),
    _Fax_pstn_access_code_Type()
)
fax_pstn_access_code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_pstn_access_code.setStatus("current")


class _Fax_rx_disposition_Type(Integer32):
    """Custom type fax_rx_disposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ePrintOnly", 1),
          ("eUploadOnly", 2),
          ("eUploadElsePrint", 4),
          ("eForwardElsePrint", 6))
    )


_Fax_rx_disposition_Type.__name__ = "Integer32"
_Fax_rx_disposition_Object = MibScalar
fax_rx_disposition = _Fax_rx_disposition_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 19),
    _Fax_rx_disposition_Type()
)
fax_rx_disposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_rx_disposition.setStatus("current")


class _Fax_error_correction_mode_Type(Integer32):
    """Custom type fax_error_correction_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_error_correction_mode_Type.__name__ = "Integer32"
_Fax_error_correction_mode_Object = MibScalar
fax_error_correction_mode = _Fax_error_correction_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 21),
    _Fax_error_correction_mode_Type()
)
fax_error_correction_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_error_correction_mode.setStatus("current")


class _Fax_report_transmission_Type(Integer32):
    """Custom type fax_report_transmission based on Integer32"""
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
        *(("eNone", 1),
          ("ePrintReport", 2),
          ("ePrintReportOnSend", 3),
          ("ePrintReportOnError", 4),
          ("ePrintReportOnSendError", 5),
          ("ePrintReportOnReceiveError", 6))
    )


_Fax_report_transmission_Type.__name__ = "Integer32"
_Fax_report_transmission_Object = MibScalar
fax_report_transmission = _Fax_report_transmission_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 22),
    _Fax_report_transmission_Type()
)
fax_report_transmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_report_transmission.setStatus("current")


class _Fax_report_activity_log_Type(Integer32):
    """Custom type fax_report_activity_log based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNever", 1),
          ("eThreshold", 2))
    )


_Fax_report_activity_log_Type.__name__ = "Integer32"
_Fax_report_activity_log_Object = MibScalar
fax_report_activity_log = _Fax_report_activity_log_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 23),
    _Fax_report_activity_log_Type()
)
fax_report_activity_log.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_report_activity_log.setStatus("current")


class _Fax_dial_tone_detection_Type(Integer32):
    """Custom type fax_dial_tone_detection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_dial_tone_detection_Type.__name__ = "Integer32"
_Fax_dial_tone_detection_Object = MibScalar
fax_dial_tone_detection = _Fax_dial_tone_detection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 24),
    _Fax_dial_tone_detection_Type()
)
fax_dial_tone_detection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_dial_tone_detection.setStatus("current")


class _Fax_alarm_volume_Type(Integer32):
    """Custom type fax_alarm_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fax_alarm_volume_Type.__name__ = "Integer32"
_Fax_alarm_volume_Object = MibScalar
fax_alarm_volume = _Fax_alarm_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 25),
    _Fax_alarm_volume_Type()
)
fax_alarm_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_alarm_volume.setStatus("current")


class _Fax_beep_volume_Type(Integer32):
    """Custom type fax_beep_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fax_beep_volume_Type.__name__ = "Integer32"
_Fax_beep_volume_Object = MibScalar
fax_beep_volume = _Fax_beep_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 26),
    _Fax_beep_volume_Type()
)
fax_beep_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_beep_volume.setStatus("current")


class _Fax_ring_volume_Type(Integer32):
    """Custom type fax_ring_volume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Fax_ring_volume_Type.__name__ = "Integer32"
_Fax_ring_volume_Object = MibScalar
fax_ring_volume = _Fax_ring_volume_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 27),
    _Fax_ring_volume_Type()
)
fax_ring_volume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_ring_volume.setStatus("current")
_Fax_master_host_Type = DisplayString
_Fax_master_host_Object = MibScalar
fax_master_host = _Fax_master_host_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 28),
    _Fax_master_host_Type()
)
fax_master_host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_master_host.setStatus("current")


class _Fax_thumbnail_enable_Type(Integer32):
    """Custom type fax_thumbnail_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_thumbnail_enable_Type.__name__ = "Integer32"
_Fax_thumbnail_enable_Object = MibScalar
fax_thumbnail_enable = _Fax_thumbnail_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 29),
    _Fax_thumbnail_enable_Type()
)
fax_thumbnail_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_thumbnail_enable.setStatus("current")


class _Fax_phone_pickup_enable_Type(Integer32):
    """Custom type fax_phone_pickup_enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Fax_phone_pickup_enable_Type.__name__ = "Integer32"
_Fax_phone_pickup_enable_Object = MibScalar
fax_phone_pickup_enable = _Fax_phone_pickup_enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 30),
    _Fax_phone_pickup_enable_Type()
)
fax_phone_pickup_enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_phone_pickup_enable.setStatus("current")
_Fax_adf_scan_count_Type = Integer32
_Fax_adf_scan_count_Object = MibScalar
fax_adf_scan_count = _Fax_adf_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 31),
    _Fax_adf_scan_count_Type()
)
fax_adf_scan_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_adf_scan_count.setStatus("current")
_Fax_print_page_count_Type = Integer32
_Fax_print_page_count_Object = MibScalar
fax_print_page_count = _Fax_print_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 32),
    _Fax_print_page_count_Type()
)
fax_print_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_print_page_count.setStatus("current")
_Fax_download_page_count_Type = Integer32
_Fax_download_page_count_Object = MibScalar
fax_download_page_count = _Fax_download_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 33),
    _Fax_download_page_count_Type()
)
fax_download_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_download_page_count.setStatus("current")
_Fax_upload_page_count_Type = Integer32
_Fax_upload_page_count_Object = MibScalar
fax_upload_page_count = _Fax_upload_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 34),
    _Fax_upload_page_count_Type()
)
fax_upload_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_upload_page_count.setStatus("current")
_Fax_flatbed_scan_count_Type = Integer32
_Fax_flatbed_scan_count_Object = MibScalar
fax_flatbed_scan_count = _Fax_flatbed_scan_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 36),
    _Fax_flatbed_scan_count_Type()
)
fax_flatbed_scan_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_flatbed_scan_count.setStatus("current")


class _Default_fax_glass_size_Type(Integer32):
    """Custom type default_fax_glass_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              26)
        )
    )
    namedValues = NamedValues(
        *(("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eISOandJISA4", 26))
    )


_Default_fax_glass_size_Type.__name__ = "Integer32"
_Default_fax_glass_size_Object = MibScalar
default_fax_glass_size = _Default_fax_glass_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 37),
    _Default_fax_glass_size_Type()
)
default_fax_glass_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_fax_glass_size.setStatus("current")


class _Fax_cold_reset_fax_glass_size_Type(Integer32):
    """Custom type fax_cold_reset_fax_glass_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              26)
        )
    )
    namedValues = NamedValues(
        *(("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eISOandJISA4", 26))
    )


_Fax_cold_reset_fax_glass_size_Type.__name__ = "Integer32"
_Fax_cold_reset_fax_glass_size_Object = MibScalar
fax_cold_reset_fax_glass_size = _Fax_cold_reset_fax_glass_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 1, 38),
    _Fax_cold_reset_fax_glass_size_Type()
)
fax_cold_reset_fax_glass_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_cold_reset_fax_glass_size.setStatus("current")
_Status_fax_proc_sub_ObjectIdentity = ObjectIdentity
status_fax_proc_sub = _Status_fax_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2)
)


class _Fax_upload_Type(Integer32):
    """Custom type fax_upload based on Integer32"""
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
        *(("eFaxUploadIdle", 1),
          ("eFaxUploadStart", 2),
          ("eFaxUploadActive", 3),
          ("eFaxUploadAborted", 4),
          ("eFaxUploadDone", 5),
          ("eFaxUploadNeeded", 6))
    )


_Fax_upload_Type.__name__ = "Integer32"
_Fax_upload_Object = MibScalar
fax_upload = _Fax_upload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 1),
    _Fax_upload_Type()
)
fax_upload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_upload.setStatus("current")


class _Fax_min_rings_pickup_Type(Integer32):
    """Custom type fax_min_rings_pickup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Fax_min_rings_pickup_Type.__name__ = "Integer32"
_Fax_min_rings_pickup_Object = MibScalar
fax_min_rings_pickup = _Fax_min_rings_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 2),
    _Fax_min_rings_pickup_Type()
)
fax_min_rings_pickup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_min_rings_pickup.setStatus("current")


class _Fax_max_rings_pickup_Type(Integer32):
    """Custom type fax_max_rings_pickup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fax_max_rings_pickup_Type.__name__ = "Integer32"
_Fax_max_rings_pickup_Object = MibScalar
fax_max_rings_pickup = _Fax_max_rings_pickup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 3),
    _Fax_max_rings_pickup_Type()
)
fax_max_rings_pickup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_max_rings_pickup.setStatus("current")
_Fax_max_redials_Type = Integer32
_Fax_max_redials_Object = MibScalar
fax_max_redials = _Fax_max_redials_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 4),
    _Fax_max_redials_Type()
)
fax_max_redials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_max_redials.setStatus("current")
_Fax_additional_wait_Type = Integer32
_Fax_additional_wait_Object = MibScalar
fax_additional_wait = _Fax_additional_wait_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 5),
    _Fax_additional_wait_Type()
)
fax_additional_wait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_additional_wait.setStatus("current")
_Fax_download_error_Type = Integer32
_Fax_download_error_Object = MibScalar
fax_download_error = _Fax_download_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 6),
    _Fax_download_error_Type()
)
fax_download_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_download_error.setStatus("current")
_Fax_upload_error_Type = Integer32
_Fax_upload_error_Object = MibScalar
fax_upload_error = _Fax_upload_error_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 7),
    _Fax_upload_error_Type()
)
fax_upload_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_upload_error.setStatus("current")


class _Fax_firmware_revision_Type(DisplayString):
    """Custom type fax_firmware_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Fax_firmware_revision_Type.__name__ = "DisplayString"
_Fax_firmware_revision_Object = MibScalar
fax_firmware_revision = _Fax_firmware_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 2, 8),
    _Fax_firmware_revision_Type()
)
fax_firmware_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fax_firmware_revision.setStatus("current")
_Fax_forwarding_ObjectIdentity = ObjectIdentity
fax_forwarding = _Fax_forwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 3)
)
_Fax_forwarding_phone_num_Type = DisplayString
_Fax_forwarding_phone_num_Object = MibScalar
fax_forwarding_phone_num = _Fax_forwarding_phone_num_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 7, 3, 3),
    _Fax_forwarding_phone_num_Type()
)
fax_forwarding_phone_num.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_forwarding_phone_num.setStatus("current")
_Jetsend_proc_sub_ObjectIdentity = ObjectIdentity
jetsend_proc_sub = _Jetsend_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 8)
)
_Settings_jetsend_ObjectIdentity = ObjectIdentity
settings_jetsend = _Settings_jetsend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 8, 1)
)


class _Jetsend_mode_Type(Integer32):
    """Custom type jetsend_mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Jetsend_mode_Type.__name__ = "Integer32"
_Jetsend_mode_Object = MibScalar
jetsend_mode = _Jetsend_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 8, 1, 1),
    _Jetsend_mode_Type()
)
jetsend_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jetsend_mode.setStatus("current")
_Jetsend_contact_ObjectIdentity = ObjectIdentity
jetsend_contact = _Jetsend_contact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 8, 3)
)
_Settings_jetsend_contact_ObjectIdentity = ObjectIdentity
settings_jetsend_contact = _Settings_jetsend_contact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 8, 3, 1)
)


class _Jetsend_contact_password_Type(OctetString):
    """Custom type jetsend_contact_password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Jetsend_contact_password_Type.__name__ = "OctetString"
_Jetsend_contact_password_Object = MibScalar
jetsend_contact_password = _Jetsend_contact_password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 8, 3, 1, 1),
    _Jetsend_contact_password_Type()
)
jetsend_contact_password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jetsend_contact_password.setStatus("current")


class _Jetsend_contact_ip_address_security_Type(OctetString):
    """Custom type jetsend_contact_ip_address_security based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Jetsend_contact_ip_address_security_Type.__name__ = "OctetString"
_Jetsend_contact_ip_address_security_Object = MibScalar
jetsend_contact_ip_address_security = _Jetsend_contact_ip_address_security_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 8, 3, 1, 2),
    _Jetsend_contact_ip_address_security_Type()
)
jetsend_contact_ip_address_security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jetsend_contact_ip_address_security.setStatus("current")
_Webserver_proc_sub_ObjectIdentity = ObjectIdentity
webserver_proc_sub = _Webserver_proc_sub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9)
)
_Settings_webserver_ObjectIdentity = ObjectIdentity
settings_webserver = _Settings_webserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 3, 9, 1)
)
_Destination_subsystem_ObjectIdentity = ObjectIdentity
destination_subsystem = _Destination_subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4)
)
_Print_engine_ObjectIdentity = ObjectIdentity
print_engine = _Print_engine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1)
)
_Settings_prt_eng_ObjectIdentity = ObjectIdentity
settings_prt_eng = _Settings_prt_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1)
)
_Override_media_name_Type = DisplayString
_Override_media_name_Object = MibScalar
override_media_name = _Override_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 2),
    _Override_media_name_Type()
)
override_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    override_media_name.setStatus("current")


class _Override_media_size_Type(Integer32):
    """Custom type override_media_size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              25,
              26,
              45,
              80,
              81,
              90,
              91,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("eJISB5", 45),
          ("eMonarch", 80),
          ("eCommercial10", 81),
          ("eInternationalDL", 90),
          ("eInternationalC5", 91),
          ("eInternationalB5", 100),
          ("eCustom", 101))
    )


_Override_media_size_Type.__name__ = "Integer32"
_Override_media_size_Object = MibScalar
override_media_size = _Override_media_size_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 3),
    _Override_media_size_Type()
)
override_media_size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    override_media_size.setStatus("current")


class _Print_density_Type(Integer32):
    """Custom type print_density based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Print_density_Type.__name__ = "Integer32"
_Print_density_Object = MibScalar
print_density = _Print_density_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 5),
    _Print_density_Type()
)
print_density.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_density.setStatus("current")


class _Transfer_setting_Type(Integer32):
    """Custom type transfer_setting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_Transfer_setting_Type.__name__ = "Integer32"
_Transfer_setting_Object = MibScalar
transfer_setting = _Transfer_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 8),
    _Transfer_setting_Type()
)
transfer_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transfer_setting.setStatus("current")
_Marking_agent_density_ObjectIdentity = ObjectIdentity
marking_agent_density = _Marking_agent_density_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 9)
)


class _Separation_setting_Type(Integer32):
    """Custom type separation_setting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_Separation_setting_Type.__name__ = "Integer32"
_Separation_setting_Object = MibScalar
separation_setting = _Separation_setting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 1, 13),
    _Separation_setting_Type()
)
separation_setting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    separation_setting.setStatus("current")
_Status_prt_eng_ObjectIdentity = ObjectIdentity
status_prt_eng = _Status_prt_eng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2)
)
_Not_ready_destination_print_engine_Type = OctetString
_Not_ready_destination_print_engine_Object = MibScalar
not_ready_destination_print_engine = _Not_ready_destination_print_engine_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 1),
    _Not_ready_destination_print_engine_Type()
)
not_ready_destination_print_engine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_destination_print_engine.setStatus("current")
_Not_ready_laser_print_engine_Type = OctetString
_Not_ready_laser_print_engine_Object = MibScalar
not_ready_laser_print_engine = _Not_ready_laser_print_engine_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 3),
    _Not_ready_laser_print_engine_Type()
)
not_ready_laser_print_engine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_laser_print_engine.setStatus("current")
_Total_engine_page_count_Type = Integer32
_Total_engine_page_count_Object = MibScalar
total_engine_page_count = _Total_engine_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 5),
    _Total_engine_page_count_Type()
)
total_engine_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    total_engine_page_count.setStatus("current")
_Total_mono_page_count_Type = Integer32
_Total_mono_page_count_Object = MibScalar
total_mono_page_count = _Total_mono_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 6),
    _Total_mono_page_count_Type()
)
total_mono_page_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    total_mono_page_count.setStatus("current")


class _Total_color_page_count_Type(Integer32):
    """Custom type total_color_page_count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967296),
    )


_Total_color_page_count_Type.__name__ = "Integer32"
_Total_color_page_count_Object = MibScalar
total_color_page_count = _Total_color_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 7),
    _Total_color_page_count_Type()
)
total_color_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    total_color_page_count.setStatus("current")
_Status_destination_print_engine_Type = OctetString
_Status_destination_print_engine_Object = MibScalar
status_destination_print_engine = _Status_destination_print_engine_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 8),
    _Status_destination_print_engine_Type()
)
status_destination_print_engine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_destination_print_engine.setStatus("current")
_Duplex_page_count_Type = Integer32
_Duplex_page_count_Object = MibScalar
duplex_page_count = _Duplex_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 22),
    _Duplex_page_count_Type()
)
duplex_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplex_page_count.setStatus("current")


class _Print_engine_revision_Type(DisplayString):
    """Custom type print_engine_revision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Print_engine_revision_Type.__name__ = "DisplayString"
_Print_engine_revision_Object = MibScalar
print_engine_revision = _Print_engine_revision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 26),
    _Print_engine_revision_Type()
)
print_engine_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    print_engine_revision.setStatus("current")
_Print_engine_jam_count_Type = Integer32
_Print_engine_jam_count_Object = MibScalar
print_engine_jam_count = _Print_engine_jam_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 34),
    _Print_engine_jam_count_Type()
)
print_engine_jam_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_engine_jam_count.setStatus("current")
_Print_engine_mispick_count_Type = Integer32
_Print_engine_mispick_count_Object = MibScalar
print_engine_mispick_count = _Print_engine_mispick_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 35),
    _Print_engine_mispick_count_Type()
)
print_engine_mispick_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    print_engine_mispick_count.setStatus("current")
_Printer_calibration_dhalf_ObjectIdentity = ObjectIdentity
printer_calibration_dhalf = _Printer_calibration_dhalf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37)
)
_Printer_cal_dhalf_data_ObjectIdentity = ObjectIdentity
printer_cal_dhalf_data = _Printer_cal_dhalf_data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 3)
)
_Printer_cal_grayaxis_ObjectIdentity = ObjectIdentity
printer_cal_grayaxis = _Printer_cal_grayaxis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 6)
)
_Printer_cal_grayaxis_data_ObjectIdentity = ObjectIdentity
printer_cal_grayaxis_data = _Printer_cal_grayaxis_data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 37, 7)
)
_Printer_calibration_cpr_ObjectIdentity = ObjectIdentity
printer_calibration_cpr = _Printer_calibration_cpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 2, 38)
)
_Intray_ObjectIdentity = ObjectIdentity
intray = _Intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3)
)
_Settings_intray_ObjectIdentity = ObjectIdentity
settings_intray = _Settings_intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1)
)


class _Default_manual_feed_Type(Integer32):
    """Custom type default_manual_feed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eOff", 1),
          ("eOn", 2))
    )


_Default_manual_feed_Type.__name__ = "Integer32"
_Default_manual_feed_Object = MibScalar
default_manual_feed = _Default_manual_feed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 4),
    _Default_manual_feed_Type()
)
default_manual_feed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_manual_feed.setStatus("current")


class _Mp_tray_Type(Integer32):
    """Custom type mp_tray based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eCassette", 2),
          ("eFirst", 3))
    )


_Mp_tray_Type.__name__ = "Integer32"
_Mp_tray_Object = MibScalar
mp_tray = _Mp_tray_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 5),
    _Mp_tray_Type()
)
mp_tray.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp_tray.setStatus("current")
_Tray_lock_Type = OctetString
_Tray_lock_Object = MibScalar
tray_lock = _Tray_lock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 6),
    _Tray_lock_Type()
)
tray_lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray_lock.setStatus("current")


class _Custom_paper_dim_unit_Type(Integer32):
    """Custom type custom_paper_dim_unit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eTenThousandthsOfInches", 3),
          ("eMicrometers", 4))
    )


_Custom_paper_dim_unit_Type.__name__ = "Integer32"
_Custom_paper_dim_unit_Object = MibScalar
custom_paper_dim_unit = _Custom_paper_dim_unit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 7),
    _Custom_paper_dim_unit_Type()
)
custom_paper_dim_unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    custom_paper_dim_unit.setStatus("current")
_Custom_paper_feed_dim_Type = Integer32
_Custom_paper_feed_dim_Object = MibScalar
custom_paper_feed_dim = _Custom_paper_feed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 8),
    _Custom_paper_feed_dim_Type()
)
custom_paper_feed_dim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    custom_paper_feed_dim.setStatus("current")
_Custom_paper_xfeed_dim_Type = Integer32
_Custom_paper_xfeed_dim_Object = MibScalar
custom_paper_xfeed_dim = _Custom_paper_xfeed_dim_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 1, 9),
    _Custom_paper_xfeed_dim_Type()
)
custom_paper_xfeed_dim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    custom_paper_xfeed_dim.setStatus("current")
_Status_intray_ObjectIdentity = ObjectIdentity
status_intray = _Status_intray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 2)
)
_Not_ready_tray_missing_Type = OctetString
_Not_ready_tray_missing_Object = MibScalar
not_ready_tray_missing = _Not_ready_tray_missing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 2, 1),
    _Not_ready_tray_missing_Type()
)
not_ready_tray_missing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_tray_missing.setStatus("current")
_Not_ready_tray_empty_Type = OctetString
_Not_ready_tray_empty_Object = MibScalar
not_ready_tray_empty = _Not_ready_tray_empty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 2, 2),
    _Not_ready_tray_empty_Type()
)
not_ready_tray_empty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_tray_empty.setStatus("current")
_Status_tray_missing_Type = OctetString
_Status_tray_missing_Object = MibScalar
status_tray_missing = _Status_tray_missing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 2, 3),
    _Status_tray_missing_Type()
)
status_tray_missing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_tray_missing.setStatus("current")
_Status_tray_empty_Type = OctetString
_Status_tray_empty_Object = MibScalar
status_tray_empty = _Status_tray_empty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 2, 4),
    _Status_tray_empty_Type()
)
status_tray_empty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_tray_empty.setStatus("current")
_Intrays_ObjectIdentity = ObjectIdentity
intrays = _Intrays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3)
)
_Intray1_ObjectIdentity = ObjectIdentity
intray1 = _Intray1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1)
)


class _Tray1_media_size_loaded_Type(Integer32):
    """Custom type tray1_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              15,
              17,
              24,
              25,
              26,
              27,
              34,
              44,
              45,
              46,
              71,
              72,
              74,
              75,
              78,
              80,
              81,
              89,
              90,
              91,
              92,
              100,
              101,
              110,
              111,
              118,
              121,
              122,
              127,
              328,
              32765)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eFoolscap", 10),
          ("eLedger", 11),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA6", 24),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("eISOandJISA3", 27),
          ("ePRC16K195X270", 34),
          ("eJISB6", 44),
          ("eJISB5", 45),
          ("eJISB4", 46),
          ("eJapanesePostcardSingle", 71),
          ("eJapanesePostcardDouble", 72),
          ("eIndexCard4x6", 74),
          ("eIndexCard5x8", 75),
          ("eIndexCard3x5", 78),
          ("eMonarch", 80),
          ("eCommercial10", 81),
          ("ePRC16K184X260", 89),
          ("eInternationalDL", 90),
          ("eInternationalC5", 91),
          ("eInternationalC6", 92),
          ("eInternationalB5", 100),
          ("eCustom", 101),
          ("eJapanseEnvLong3", 110),
          ("eJapanseEnvLong4", 111),
          ("ePhoto10x15", 118),
          ("ePhotoLSizeCard", 121),
          ("eIndexCard5x7", 122),
          ("eLegal216x340", 127),
          ("eJapaneseOufuku148x200", 328),
          ("eAnySize", 32765))
    )


_Tray1_media_size_loaded_Type.__name__ = "Integer32"
_Tray1_media_size_loaded_Object = MibScalar
tray1_media_size_loaded = _Tray1_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 1),
    _Tray1_media_size_loaded_Type()
)
tray1_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_media_size_loaded.setStatus("current")


class _Tray1_media_available_Type(Integer32):
    """Custom type tray1_media_available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_Tray1_media_available_Type.__name__ = "Integer32"
_Tray1_media_available_Object = MibScalar
tray1_media_available = _Tray1_media_available_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 2),
    _Tray1_media_available_Type()
)
tray1_media_available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_media_available.setStatus("current")
_Tray1_name_Type = DisplayString
_Tray1_name_Object = MibScalar
tray1_name = _Tray1_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 3),
    _Tray1_name_Type()
)
tray1_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_name.setStatus("current")
_Tray1_media_name_Type = DisplayString
_Tray1_media_name_Object = MibScalar
tray1_media_name = _Tray1_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 4),
    _Tray1_media_name_Type()
)
tray1_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_media_name.setStatus("current")
_Tray1_custom_media_width_Type = Integer32
_Tray1_custom_media_width_Object = MibScalar
tray1_custom_media_width = _Tray1_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 10),
    _Tray1_custom_media_width_Type()
)
tray1_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_custom_media_width.setStatus("current")
_Tray1_custom_media_length_Type = Integer32
_Tray1_custom_media_length_Object = MibScalar
tray1_custom_media_length = _Tray1_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 11),
    _Tray1_custom_media_length_Type()
)
tray1_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_custom_media_length.setStatus("current")
_Tray1_phd_Type = Integer32
_Tray1_phd_Object = MibScalar
tray1_phd = _Tray1_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 12),
    _Tray1_phd_Type()
)
tray1_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_phd.setStatus("current")


class _Tray1_fuser_temperature_Type(Integer32):
    """Custom type tray1_fuser_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_Tray1_fuser_temperature_Type.__name__ = "Integer32"
_Tray1_fuser_temperature_Object = MibScalar
tray1_fuser_temperature = _Tray1_fuser_temperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 13),
    _Tray1_fuser_temperature_Type()
)
tray1_fuser_temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_fuser_temperature.setStatus("current")


class _Tray1_type_Type(Integer32):
    """Custom type tray1_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray1_type_Type.__name__ = "Integer32"
_Tray1_type_Object = MibScalar
tray1_type = _Tray1_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 17),
    _Tray1_type_Type()
)
tray1_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray1_type.setStatus("current")
_Tray1_media_key_Type = OctetString
_Tray1_media_key_Object = MibScalar
tray1_media_key = _Tray1_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 1, 20),
    _Tray1_media_key_Type()
)
tray1_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray1_media_key.setStatus("current")
_Intray2_ObjectIdentity = ObjectIdentity
intray2 = _Intray2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2)
)


class _Tray2_media_size_loaded_Type(Integer32):
    """Custom type tray2_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              15,
              17,
              25,
              26,
              27,
              34,
              45,
              46,
              81,
              89,
              90,
              91,
              100,
              101,
              110,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eLedger", 11),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("eISOandJISA3", 27),
          ("ePRC16K195X270", 34),
          ("eJISB5", 45),
          ("eJISB4", 46),
          ("eCommercial10", 81),
          ("ePRC16K184X260", 89),
          ("eInternationalDL", 90),
          ("eInternationalC5", 91),
          ("eInternationalB5", 100),
          ("eCustom", 101),
          ("eJapanseEnvLong3", 110),
          ("eUnknownMediaSize", 32767))
    )


_Tray2_media_size_loaded_Type.__name__ = "Integer32"
_Tray2_media_size_loaded_Object = MibScalar
tray2_media_size_loaded = _Tray2_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 1),
    _Tray2_media_size_loaded_Type()
)
tray2_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_media_size_loaded.setStatus("current")


class _Tray2_media_available_Type(Integer32):
    """Custom type tray2_media_available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_Tray2_media_available_Type.__name__ = "Integer32"
_Tray2_media_available_Object = MibScalar
tray2_media_available = _Tray2_media_available_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 2),
    _Tray2_media_available_Type()
)
tray2_media_available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_media_available.setStatus("current")
_Tray2_name_Type = DisplayString
_Tray2_name_Object = MibScalar
tray2_name = _Tray2_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 3),
    _Tray2_name_Type()
)
tray2_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_name.setStatus("current")
_Tray2_media_name_Type = DisplayString
_Tray2_media_name_Object = MibScalar
tray2_media_name = _Tray2_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 4),
    _Tray2_media_name_Type()
)
tray2_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_media_name.setStatus("current")
_Tray2_custom_media_width_Type = Integer32
_Tray2_custom_media_width_Object = MibScalar
tray2_custom_media_width = _Tray2_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 10),
    _Tray2_custom_media_width_Type()
)
tray2_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_custom_media_width.setStatus("current")
_Tray2_custom_media_length_Type = Integer32
_Tray2_custom_media_length_Object = MibScalar
tray2_custom_media_length = _Tray2_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 11),
    _Tray2_custom_media_length_Type()
)
tray2_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_custom_media_length.setStatus("current")
_Tray2_phd_Type = Integer32
_Tray2_phd_Object = MibScalar
tray2_phd = _Tray2_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 12),
    _Tray2_phd_Type()
)
tray2_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_phd.setStatus("current")


class _Tray2_fuser_temperature_Type(Integer32):
    """Custom type tray2_fuser_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_Tray2_fuser_temperature_Type.__name__ = "Integer32"
_Tray2_fuser_temperature_Object = MibScalar
tray2_fuser_temperature = _Tray2_fuser_temperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 13),
    _Tray2_fuser_temperature_Type()
)
tray2_fuser_temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_fuser_temperature.setStatus("current")


class _Tray2_type_Type(Integer32):
    """Custom type tray2_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray2_type_Type.__name__ = "Integer32"
_Tray2_type_Object = MibScalar
tray2_type = _Tray2_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 17),
    _Tray2_type_Type()
)
tray2_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray2_type.setStatus("current")
_Tray2_media_key_Type = OctetString
_Tray2_media_key_Object = MibScalar
tray2_media_key = _Tray2_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 2, 20),
    _Tray2_media_key_Type()
)
tray2_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray2_media_key.setStatus("current")
_Intray3_ObjectIdentity = ObjectIdentity
intray3 = _Intray3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3)
)


class _Tray3_media_size_loaded_Type(Integer32):
    """Custom type tray3_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11,
              15,
              17,
              25,
              26,
              27,
              34,
              45,
              46,
              89,
              101,
              127,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eFoolscap", 10),
          ("eLedger", 11),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("eISOandJISA3", 27),
          ("ePRC16K195X270", 34),
          ("eJISB5", 45),
          ("eJISB4", 46),
          ("ePRC16K184X260", 89),
          ("eCustom", 101),
          ("eLegal216x340", 127),
          ("eUnknownMediaSize", 32767))
    )


_Tray3_media_size_loaded_Type.__name__ = "Integer32"
_Tray3_media_size_loaded_Object = MibScalar
tray3_media_size_loaded = _Tray3_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 1),
    _Tray3_media_size_loaded_Type()
)
tray3_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_media_size_loaded.setStatus("current")


class _Tray3_media_available_Type(Integer32):
    """Custom type tray3_media_available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_Tray3_media_available_Type.__name__ = "Integer32"
_Tray3_media_available_Object = MibScalar
tray3_media_available = _Tray3_media_available_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 2),
    _Tray3_media_available_Type()
)
tray3_media_available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_media_available.setStatus("current")
_Tray3_name_Type = DisplayString
_Tray3_name_Object = MibScalar
tray3_name = _Tray3_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 3),
    _Tray3_name_Type()
)
tray3_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_name.setStatus("current")
_Tray3_media_name_Type = OctetString
_Tray3_media_name_Object = MibScalar
tray3_media_name = _Tray3_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 4),
    _Tray3_media_name_Type()
)
tray3_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_media_name.setStatus("current")
_Tray3_custom_media_width_Type = Integer32
_Tray3_custom_media_width_Object = MibScalar
tray3_custom_media_width = _Tray3_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 10),
    _Tray3_custom_media_width_Type()
)
tray3_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_custom_media_width.setStatus("current")
_Tray3_custom_media_length_Type = Integer32
_Tray3_custom_media_length_Object = MibScalar
tray3_custom_media_length = _Tray3_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 11),
    _Tray3_custom_media_length_Type()
)
tray3_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_custom_media_length.setStatus("current")
_Tray3_phd_Type = Integer32
_Tray3_phd_Object = MibScalar
tray3_phd = _Tray3_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 12),
    _Tray3_phd_Type()
)
tray3_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_phd.setStatus("current")


class _Tray3_fuser_temperature_Type(Integer32):
    """Custom type tray3_fuser_temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_Tray3_fuser_temperature_Type.__name__ = "Integer32"
_Tray3_fuser_temperature_Object = MibScalar
tray3_fuser_temperature = _Tray3_fuser_temperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 13),
    _Tray3_fuser_temperature_Type()
)
tray3_fuser_temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_fuser_temperature.setStatus("current")


class _Tray3_type_Type(Integer32):
    """Custom type tray3_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray3_type_Type.__name__ = "Integer32"
_Tray3_type_Object = MibScalar
tray3_type = _Tray3_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 17),
    _Tray3_type_Type()
)
tray3_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray3_type.setStatus("current")
_Tray3_media_key_Type = OctetString
_Tray3_media_key_Object = MibScalar
tray3_media_key = _Tray3_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 3, 20),
    _Tray3_media_key_Type()
)
tray3_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray3_media_key.setStatus("current")
_Intray4_ObjectIdentity = ObjectIdentity
intray4 = _Intray4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4)
)


class _Tray4_media_size_loaded_Type(Integer32):
    """Custom type tray4_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              11,
              26,
              27,
              46)
        )
    )
    namedValues = NamedValues(
        *(("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eLedger", 11),
          ("eISOandJISA4", 26),
          ("eISOandJISA3", 27),
          ("eJISB4", 46))
    )


_Tray4_media_size_loaded_Type.__name__ = "Integer32"
_Tray4_media_size_loaded_Object = MibScalar
tray4_media_size_loaded = _Tray4_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4, 1),
    _Tray4_media_size_loaded_Type()
)
tray4_media_size_loaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray4_media_size_loaded.setStatus("current")
_Tray4_phd_Type = Integer32
_Tray4_phd_Object = MibScalar
tray4_phd = _Tray4_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 4, 12),
    _Tray4_phd_Type()
)
tray4_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray4_phd.setStatus("current")
_Intray5_ObjectIdentity = ObjectIdentity
intray5 = _Intray5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5)
)


class _Tray5_media_size_loaded_Type(Integer32):
    """Custom type tray5_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              15,
              17,
              25,
              26,
              34,
              45,
              89,
              101,
              127,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("eUSExecutive", 1),
          ("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eFoolscap", 10),
          ("eStatement", 15),
          ("eROC16K", 17),
          ("eISOandJISA5", 25),
          ("eISOandJISA4", 26),
          ("ePRC16K195X270", 34),
          ("eJISB5", 45),
          ("ePRC16K184X260", 89),
          ("eCustom", 101),
          ("eLegal216x340", 127),
          ("eUnknownMediaSize", 32767))
    )


_Tray5_media_size_loaded_Type.__name__ = "Integer32"
_Tray5_media_size_loaded_Object = MibScalar
tray5_media_size_loaded = _Tray5_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 1),
    _Tray5_media_size_loaded_Type()
)
tray5_media_size_loaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray5_media_size_loaded.setStatus("current")
_Tray5_media_name_Type = OctetString
_Tray5_media_name_Object = MibScalar
tray5_media_name = _Tray5_media_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 4),
    _Tray5_media_name_Type()
)
tray5_media_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray5_media_name.setStatus("current")
_Tray5_custom_media_width_Type = Integer32
_Tray5_custom_media_width_Object = MibScalar
tray5_custom_media_width = _Tray5_custom_media_width_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 10),
    _Tray5_custom_media_width_Type()
)
tray5_custom_media_width.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_custom_media_width.setStatus("current")
_Tray5_custom_media_length_Type = Integer32
_Tray5_custom_media_length_Object = MibScalar
tray5_custom_media_length = _Tray5_custom_media_length_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 11),
    _Tray5_custom_media_length_Type()
)
tray5_custom_media_length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_custom_media_length.setStatus("current")
_Tray5_phd_Type = Integer32
_Tray5_phd_Object = MibScalar
tray5_phd = _Tray5_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 12),
    _Tray5_phd_Type()
)
tray5_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_phd.setStatus("current")


class _Tray5_type_Type(Integer32):
    """Custom type tray5_type based on Integer32"""
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
        *(("eTray", 1),
          ("eManualRoll", 2),
          ("eArss", 3),
          ("eManualSheet", 4))
    )


_Tray5_type_Type.__name__ = "Integer32"
_Tray5_type_Object = MibScalar
tray5_type = _Tray5_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 17),
    _Tray5_type_Type()
)
tray5_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tray5_type.setStatus("current")
_Tray5_media_key_Type = OctetString
_Tray5_media_key_Object = MibScalar
tray5_media_key = _Tray5_media_key_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 5, 20),
    _Tray5_media_key_Type()
)
tray5_media_key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray5_media_key.setStatus("current")
_Intray6_ObjectIdentity = ObjectIdentity
intray6 = _Intray6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 6)
)


class _Tray6_media_size_loaded_Type(Integer32):
    """Custom type tray6_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              26,
              46)
        )
    )
    namedValues = NamedValues(
        *(("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eISOandJISA4", 26),
          ("eJISB4", 46))
    )


_Tray6_media_size_loaded_Type.__name__ = "Integer32"
_Tray6_media_size_loaded_Object = MibScalar
tray6_media_size_loaded = _Tray6_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 6, 1),
    _Tray6_media_size_loaded_Type()
)
tray6_media_size_loaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray6_media_size_loaded.setStatus("current")
_Tray6_phd_Type = Integer32
_Tray6_phd_Object = MibScalar
tray6_phd = _Tray6_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 6, 12),
    _Tray6_phd_Type()
)
tray6_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray6_phd.setStatus("current")
_Intray7_ObjectIdentity = ObjectIdentity
intray7 = _Intray7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 7)
)


class _Tray7_media_size_loaded_Type(Integer32):
    """Custom type tray7_media_size_loaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              11,
              26,
              27,
              46)
        )
    )
    namedValues = NamedValues(
        *(("eUSLetter", 2),
          ("eUSLegal", 3),
          ("eLedger", 11),
          ("eISOandJISA4", 26),
          ("eISOandJISA3", 27),
          ("eJISB4", 46))
    )


_Tray7_media_size_loaded_Type.__name__ = "Integer32"
_Tray7_media_size_loaded_Object = MibScalar
tray7_media_size_loaded = _Tray7_media_size_loaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 7, 1),
    _Tray7_media_size_loaded_Type()
)
tray7_media_size_loaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray7_media_size_loaded.setStatus("current")
_Tray7_phd_Type = Integer32
_Tray7_phd_Object = MibScalar
tray7_phd = _Tray7_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 3, 3, 7, 12),
    _Tray7_phd_Type()
)
tray7_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tray7_phd.setStatus("current")
_Outbin_ObjectIdentity = ObjectIdentity
outbin = _Outbin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4)
)
_Settings_outbin_ObjectIdentity = ObjectIdentity
settings_outbin = _Settings_outbin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 1)
)
_Overflow_bin_Type = Integer32
_Overflow_bin_Object = MibScalar
overflow_bin = _Overflow_bin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 1, 4),
    _Overflow_bin_Type()
)
overflow_bin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overflow_bin.setStatus("current")
_Outbins_ObjectIdentity = ObjectIdentity
outbins = _Outbins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3)
)
_Outbin1_ObjectIdentity = ObjectIdentity
outbin1 = _Outbin1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1)
)
_Outbin1_maximum_capacity_Type = Integer32
_Outbin1_maximum_capacity_Object = MibScalar
outbin1_maximum_capacity = _Outbin1_maximum_capacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1, 1),
    _Outbin1_maximum_capacity_Type()
)
outbin1_maximum_capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin1_maximum_capacity.setStatus("current")
_Outbin1_override_mode_Type = OctetString
_Outbin1_override_mode_Object = MibScalar
outbin1_override_mode = _Outbin1_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 1, 9),
    _Outbin1_override_mode_Type()
)
outbin1_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin1_override_mode.setStatus("current")
_Outbin2_ObjectIdentity = ObjectIdentity
outbin2 = _Outbin2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 2)
)
_Outbin2_override_mode_Type = OctetString
_Outbin2_override_mode_Object = MibScalar
outbin2_override_mode = _Outbin2_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 2, 9),
    _Outbin2_override_mode_Type()
)
outbin2_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin2_override_mode.setStatus("current")
_Outbin3_ObjectIdentity = ObjectIdentity
outbin3 = _Outbin3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3)
)
_Outbin3_override_mode_Type = OctetString
_Outbin3_override_mode_Object = MibScalar
outbin3_override_mode = _Outbin3_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 9),
    _Outbin3_override_mode_Type()
)
outbin3_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin3_override_mode.setStatus("current")
_Outbin3_maximum_binding_Type = Integer32
_Outbin3_maximum_binding_Object = MibScalar
outbin3_maximum_binding = _Outbin3_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 10),
    _Outbin3_maximum_binding_Type()
)
outbin3_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin3_maximum_binding.setStatus("current")
_Outbin3_phd_Type = Integer32
_Outbin3_phd_Object = MibScalar
outbin3_phd = _Outbin3_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 11),
    _Outbin3_phd_Type()
)
outbin3_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin3_phd.setStatus("current")


class _Outbin3_error_info_Type(OctetString):
    """Custom type outbin3_error_info based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Outbin3_error_info_Type.__name__ = "OctetString"
_Outbin3_error_info_Object = MibScalar
outbin3_error_info = _Outbin3_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 3, 12),
    _Outbin3_error_info_Type()
)
outbin3_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin3_error_info.setStatus("current")
_Outbin4_ObjectIdentity = ObjectIdentity
outbin4 = _Outbin4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4)
)
_Outbin4_override_mode_Type = OctetString
_Outbin4_override_mode_Object = MibScalar
outbin4_override_mode = _Outbin4_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4, 9),
    _Outbin4_override_mode_Type()
)
outbin4_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin4_override_mode.setStatus("current")
_Outbin4_maximum_binding_Type = Integer32
_Outbin4_maximum_binding_Object = MibScalar
outbin4_maximum_binding = _Outbin4_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4, 10),
    _Outbin4_maximum_binding_Type()
)
outbin4_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin4_maximum_binding.setStatus("current")
_Outbin4_phd_Type = Integer32
_Outbin4_phd_Object = MibScalar
outbin4_phd = _Outbin4_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 4, 11),
    _Outbin4_phd_Type()
)
outbin4_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin4_phd.setStatus("current")
_Outbin5_ObjectIdentity = ObjectIdentity
outbin5 = _Outbin5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5)
)
_Outbin5_override_mode_Type = OctetString
_Outbin5_override_mode_Object = MibScalar
outbin5_override_mode = _Outbin5_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5, 9),
    _Outbin5_override_mode_Type()
)
outbin5_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin5_override_mode.setStatus("current")
_Outbin5_maximum_binding_Type = Integer32
_Outbin5_maximum_binding_Object = MibScalar
outbin5_maximum_binding = _Outbin5_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5, 10),
    _Outbin5_maximum_binding_Type()
)
outbin5_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin5_maximum_binding.setStatus("current")
_Outbin5_phd_Type = Integer32
_Outbin5_phd_Object = MibScalar
outbin5_phd = _Outbin5_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 5, 11),
    _Outbin5_phd_Type()
)
outbin5_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin5_phd.setStatus("current")
_Outbin6_ObjectIdentity = ObjectIdentity
outbin6 = _Outbin6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6)
)
_Outbin6_override_mode_Type = OctetString
_Outbin6_override_mode_Object = MibScalar
outbin6_override_mode = _Outbin6_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6, 9),
    _Outbin6_override_mode_Type()
)
outbin6_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin6_override_mode.setStatus("current")
_Outbin6_maximum_binding_Type = Integer32
_Outbin6_maximum_binding_Object = MibScalar
outbin6_maximum_binding = _Outbin6_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6, 10),
    _Outbin6_maximum_binding_Type()
)
outbin6_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin6_maximum_binding.setStatus("current")
_Outbin6_phd_Type = Integer32
_Outbin6_phd_Object = MibScalar
outbin6_phd = _Outbin6_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 6, 11),
    _Outbin6_phd_Type()
)
outbin6_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin6_phd.setStatus("current")
_Outbin7_ObjectIdentity = ObjectIdentity
outbin7 = _Outbin7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7)
)
_Outbin7_override_mode_Type = OctetString
_Outbin7_override_mode_Object = MibScalar
outbin7_override_mode = _Outbin7_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7, 9),
    _Outbin7_override_mode_Type()
)
outbin7_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin7_override_mode.setStatus("current")
_Outbin7_maximum_binding_Type = Integer32
_Outbin7_maximum_binding_Object = MibScalar
outbin7_maximum_binding = _Outbin7_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7, 10),
    _Outbin7_maximum_binding_Type()
)
outbin7_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin7_maximum_binding.setStatus("current")
_Outbin7_phd_Type = Integer32
_Outbin7_phd_Object = MibScalar
outbin7_phd = _Outbin7_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 7, 11),
    _Outbin7_phd_Type()
)
outbin7_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin7_phd.setStatus("current")
_Outbin8_ObjectIdentity = ObjectIdentity
outbin8 = _Outbin8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8)
)
_Outbin8_override_mode_Type = OctetString
_Outbin8_override_mode_Object = MibScalar
outbin8_override_mode = _Outbin8_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8, 9),
    _Outbin8_override_mode_Type()
)
outbin8_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin8_override_mode.setStatus("current")
_Outbin8_maximum_binding_Type = Integer32
_Outbin8_maximum_binding_Object = MibScalar
outbin8_maximum_binding = _Outbin8_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8, 10),
    _Outbin8_maximum_binding_Type()
)
outbin8_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin8_maximum_binding.setStatus("current")
_Outbin8_phd_Type = Integer32
_Outbin8_phd_Object = MibScalar
outbin8_phd = _Outbin8_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 8, 11),
    _Outbin8_phd_Type()
)
outbin8_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin8_phd.setStatus("current")
_Outbin9_ObjectIdentity = ObjectIdentity
outbin9 = _Outbin9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9)
)
_Outbin9_override_mode_Type = OctetString
_Outbin9_override_mode_Object = MibScalar
outbin9_override_mode = _Outbin9_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 9),
    _Outbin9_override_mode_Type()
)
outbin9_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin9_override_mode.setStatus("current")
_Outbin9_maximum_binding_Type = Integer32
_Outbin9_maximum_binding_Object = MibScalar
outbin9_maximum_binding = _Outbin9_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 10),
    _Outbin9_maximum_binding_Type()
)
outbin9_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin9_maximum_binding.setStatus("current")
_Outbin9_phd_Type = Integer32
_Outbin9_phd_Object = MibScalar
outbin9_phd = _Outbin9_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 11),
    _Outbin9_phd_Type()
)
outbin9_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin9_phd.setStatus("current")


class _Outbin9_error_info_Type(OctetString):
    """Custom type outbin9_error_info based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Outbin9_error_info_Type.__name__ = "OctetString"
_Outbin9_error_info_Object = MibScalar
outbin9_error_info = _Outbin9_error_info_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 9, 12),
    _Outbin9_error_info_Type()
)
outbin9_error_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin9_error_info.setStatus("current")
_Outbin10_ObjectIdentity = ObjectIdentity
outbin10 = _Outbin10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10)
)
_Outbin10_override_mode_Type = OctetString
_Outbin10_override_mode_Object = MibScalar
outbin10_override_mode = _Outbin10_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10, 9),
    _Outbin10_override_mode_Type()
)
outbin10_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin10_override_mode.setStatus("current")
_Outbin10_maximum_binding_Type = Integer32
_Outbin10_maximum_binding_Object = MibScalar
outbin10_maximum_binding = _Outbin10_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10, 10),
    _Outbin10_maximum_binding_Type()
)
outbin10_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin10_maximum_binding.setStatus("current")
_Outbin10_phd_Type = Integer32
_Outbin10_phd_Object = MibScalar
outbin10_phd = _Outbin10_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 10, 11),
    _Outbin10_phd_Type()
)
outbin10_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin10_phd.setStatus("current")
_Outbin11_ObjectIdentity = ObjectIdentity
outbin11 = _Outbin11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11)
)
_Outbin11_override_mode_Type = OctetString
_Outbin11_override_mode_Object = MibScalar
outbin11_override_mode = _Outbin11_override_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11, 9),
    _Outbin11_override_mode_Type()
)
outbin11_override_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbin11_override_mode.setStatus("current")
_Outbin11_maximum_binding_Type = Integer32
_Outbin11_maximum_binding_Object = MibScalar
outbin11_maximum_binding = _Outbin11_maximum_binding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11, 10),
    _Outbin11_maximum_binding_Type()
)
outbin11_maximum_binding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin11_maximum_binding.setStatus("current")
_Outbin11_phd_Type = Integer32
_Outbin11_phd_Object = MibScalar
outbin11_phd = _Outbin11_phd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 4, 3, 11, 11),
    _Outbin11_phd_Type()
)
outbin11_phd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbin11_phd.setStatus("current")
_Marking_agent_ObjectIdentity = ObjectIdentity
marking_agent = _Marking_agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5)
)
_Settings_marking_agent_ObjectIdentity = ObjectIdentity
settings_marking_agent = _Settings_marking_agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5, 1)
)


class _Low_marking_agent_processing_Type(Integer32):
    """Custom type low_marking_agent_processing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eStop", 1),
          ("eCont", 2))
    )


_Low_marking_agent_processing_Type.__name__ = "Integer32"
_Low_marking_agent_processing_Object = MibScalar
low_marking_agent_processing = _Low_marking_agent_processing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 5, 1, 3),
    _Low_marking_agent_processing_Type()
)
low_marking_agent_processing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    low_marking_agent_processing.setStatus("current")
_Imaging_ObjectIdentity = ObjectIdentity
imaging = _Imaging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6)
)


class _Default_ret_Type(Integer32):
    """Custom type default_ret based on Integer32"""
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
        *(("eOff", 1),
          ("eLight", 2),
          ("eMedium", 3),
          ("eDark", 4))
    )


_Default_ret_Type.__name__ = "Integer32"
_Default_ret_Object = MibScalar
default_ret = _Default_ret_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6, 5),
    _Default_ret_Type()
)
default_ret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_ret.setStatus("current")


class _Default_print_quality_Type(Integer32):
    """Custom type default_print_quality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Default_print_quality_Type.__name__ = "Integer32"
_Default_print_quality_Object = MibScalar
default_print_quality = _Default_print_quality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 6, 7),
    _Default_print_quality_Type()
)
default_print_quality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    default_print_quality.setStatus("current")
_Ph_ObjectIdentity = ObjectIdentity
ph = _Ph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7)
)
_Settings_ph_ObjectIdentity = ObjectIdentity
settings_ph = _Settings_ph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 1)
)
_Ph_devices_ObjectIdentity = ObjectIdentity
ph_devices = _Ph_devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3)
)
_Ph2_ObjectIdentity = ObjectIdentity
ph2 = _Ph2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 2)
)
_Phd2_device_specific_command_Type = OctetString
_Phd2_device_specific_command_Object = MibScalar
phd2_device_specific_command = _Phd2_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 2, 2),
    _Phd2_device_specific_command_Type()
)
phd2_device_specific_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phd2_device_specific_command.setStatus("current")
_Phd2_device_memory_Type = OctetString
_Phd2_device_memory_Object = MibScalar
phd2_device_memory = _Phd2_device_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 2, 4),
    _Phd2_device_memory_Type()
)
phd2_device_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd2_device_memory.setStatus("current")
_Ph3_ObjectIdentity = ObjectIdentity
ph3 = _Ph3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 3)
)
_Phd3_device_specific_command_Type = OctetString
_Phd3_device_specific_command_Object = MibScalar
phd3_device_specific_command = _Phd3_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 3, 2),
    _Phd3_device_specific_command_Type()
)
phd3_device_specific_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phd3_device_specific_command.setStatus("current")
_Phd3_device_memory_Type = OctetString
_Phd3_device_memory_Object = MibScalar
phd3_device_memory = _Phd3_device_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 3, 4),
    _Phd3_device_memory_Type()
)
phd3_device_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd3_device_memory.setStatus("current")
_Ph4_ObjectIdentity = ObjectIdentity
ph4 = _Ph4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 4)
)
_Phd4_device_specific_command_Type = OctetString
_Phd4_device_specific_command_Object = MibScalar
phd4_device_specific_command = _Phd4_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 4, 2),
    _Phd4_device_specific_command_Type()
)
phd4_device_specific_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phd4_device_specific_command.setStatus("current")
_Phd4_device_memory_Type = OctetString
_Phd4_device_memory_Object = MibScalar
phd4_device_memory = _Phd4_device_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 4, 4),
    _Phd4_device_memory_Type()
)
phd4_device_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd4_device_memory.setStatus("current")
_Ph5_ObjectIdentity = ObjectIdentity
ph5 = _Ph5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 5)
)
_Phd5_device_specific_command_Type = OctetString
_Phd5_device_specific_command_Object = MibScalar
phd5_device_specific_command = _Phd5_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 5, 2),
    _Phd5_device_specific_command_Type()
)
phd5_device_specific_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phd5_device_specific_command.setStatus("current")
_Phd5_device_memory_Type = OctetString
_Phd5_device_memory_Object = MibScalar
phd5_device_memory = _Phd5_device_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 5, 4),
    _Phd5_device_memory_Type()
)
phd5_device_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd5_device_memory.setStatus("current")
_Ph6_ObjectIdentity = ObjectIdentity
ph6 = _Ph6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 6)
)
_Phd6_device_specific_command_Type = OctetString
_Phd6_device_specific_command_Object = MibScalar
phd6_device_specific_command = _Phd6_device_specific_command_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 6, 2),
    _Phd6_device_specific_command_Type()
)
phd6_device_specific_command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phd6_device_specific_command.setStatus("current")
_Phd6_device_memory_Type = OctetString
_Phd6_device_memory_Object = MibScalar
phd6_device_memory = _Phd6_device_memory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 7, 3, 6, 4),
    _Phd6_device_memory_Type()
)
phd6_device_memory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phd6_device_memory.setStatus("current")
_Print_media_ObjectIdentity = ObjectIdentity
print_media = _Print_media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8)
)
_Settings_print_media_ObjectIdentity = ObjectIdentity
settings_print_media = _Settings_print_media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1)
)
_Media_names_available_Type = OctetString
_Media_names_available_Object = MibScalar
media_names_available = _Media_names_available_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1, 1),
    _Media_names_available_Type()
)
media_names_available.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_names_available.setStatus("current")
_North_edge_offset_Type = Integer32
_North_edge_offset_Object = MibScalar
north_edge_offset = _North_edge_offset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 1, 2),
    _North_edge_offset_Type()
)
north_edge_offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    north_edge_offset.setStatus("current")
_Media_info_ObjectIdentity = ObjectIdentity
media_info = _Media_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3)
)
_Media1_ObjectIdentity = ObjectIdentity
media1 = _Media1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1)
)


class _Media1_name_Type(DisplayString):
    """Custom type media1_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media1_name_Type.__name__ = "DisplayString"
_Media1_name_Object = MibScalar
media1_name = _Media1_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 1),
    _Media1_name_Type()
)
media1_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media1_name.setStatus("current")


class _Media1_short_name_Type(DisplayString):
    """Custom type media1_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media1_short_name_Type.__name__ = "DisplayString"
_Media1_short_name_Object = MibScalar
media1_short_name = _Media1_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 2),
    _Media1_short_name_Type()
)
media1_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media1_short_name.setStatus("current")
_Media1_page_count_Type = Integer32
_Media1_page_count_Object = MibScalar
media1_page_count = _Media1_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 3),
    _Media1_page_count_Type()
)
media1_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media1_page_count.setStatus("current")
_Media1_engine_media_mode_Type = Integer32
_Media1_engine_media_mode_Object = MibScalar
media1_engine_media_mode = _Media1_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 1, 4),
    _Media1_engine_media_mode_Type()
)
media1_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media1_engine_media_mode.setStatus("current")
_Media2_ObjectIdentity = ObjectIdentity
media2 = _Media2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2)
)


class _Media2_name_Type(DisplayString):
    """Custom type media2_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media2_name_Type.__name__ = "DisplayString"
_Media2_name_Object = MibScalar
media2_name = _Media2_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 1),
    _Media2_name_Type()
)
media2_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media2_name.setStatus("current")


class _Media2_short_name_Type(DisplayString):
    """Custom type media2_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media2_short_name_Type.__name__ = "DisplayString"
_Media2_short_name_Object = MibScalar
media2_short_name = _Media2_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 2),
    _Media2_short_name_Type()
)
media2_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media2_short_name.setStatus("current")
_Media2_page_count_Type = Integer32
_Media2_page_count_Object = MibScalar
media2_page_count = _Media2_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 3),
    _Media2_page_count_Type()
)
media2_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media2_page_count.setStatus("current")
_Media2_engine_media_mode_Type = Integer32
_Media2_engine_media_mode_Object = MibScalar
media2_engine_media_mode = _Media2_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 2, 4),
    _Media2_engine_media_mode_Type()
)
media2_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media2_engine_media_mode.setStatus("current")
_Media3_ObjectIdentity = ObjectIdentity
media3 = _Media3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3)
)


class _Media3_name_Type(DisplayString):
    """Custom type media3_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media3_name_Type.__name__ = "DisplayString"
_Media3_name_Object = MibScalar
media3_name = _Media3_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 1),
    _Media3_name_Type()
)
media3_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media3_name.setStatus("current")


class _Media3_short_name_Type(DisplayString):
    """Custom type media3_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media3_short_name_Type.__name__ = "DisplayString"
_Media3_short_name_Object = MibScalar
media3_short_name = _Media3_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 2),
    _Media3_short_name_Type()
)
media3_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media3_short_name.setStatus("current")
_Media3_page_count_Type = Integer32
_Media3_page_count_Object = MibScalar
media3_page_count = _Media3_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 3),
    _Media3_page_count_Type()
)
media3_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media3_page_count.setStatus("current")
_Media3_engine_media_mode_Type = Integer32
_Media3_engine_media_mode_Object = MibScalar
media3_engine_media_mode = _Media3_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 3, 4),
    _Media3_engine_media_mode_Type()
)
media3_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media3_engine_media_mode.setStatus("current")
_Media4_ObjectIdentity = ObjectIdentity
media4 = _Media4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4)
)


class _Media4_name_Type(DisplayString):
    """Custom type media4_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media4_name_Type.__name__ = "DisplayString"
_Media4_name_Object = MibScalar
media4_name = _Media4_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 1),
    _Media4_name_Type()
)
media4_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media4_name.setStatus("current")


class _Media4_short_name_Type(DisplayString):
    """Custom type media4_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media4_short_name_Type.__name__ = "DisplayString"
_Media4_short_name_Object = MibScalar
media4_short_name = _Media4_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 2),
    _Media4_short_name_Type()
)
media4_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media4_short_name.setStatus("current")
_Media4_page_count_Type = Integer32
_Media4_page_count_Object = MibScalar
media4_page_count = _Media4_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 3),
    _Media4_page_count_Type()
)
media4_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media4_page_count.setStatus("current")
_Media4_engine_media_mode_Type = Integer32
_Media4_engine_media_mode_Object = MibScalar
media4_engine_media_mode = _Media4_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 4, 4),
    _Media4_engine_media_mode_Type()
)
media4_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media4_engine_media_mode.setStatus("current")
_Media5_ObjectIdentity = ObjectIdentity
media5 = _Media5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5)
)


class _Media5_name_Type(DisplayString):
    """Custom type media5_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media5_name_Type.__name__ = "DisplayString"
_Media5_name_Object = MibScalar
media5_name = _Media5_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 1),
    _Media5_name_Type()
)
media5_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media5_name.setStatus("current")


class _Media5_short_name_Type(DisplayString):
    """Custom type media5_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media5_short_name_Type.__name__ = "DisplayString"
_Media5_short_name_Object = MibScalar
media5_short_name = _Media5_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 2),
    _Media5_short_name_Type()
)
media5_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media5_short_name.setStatus("current")
_Media5_page_count_Type = Integer32
_Media5_page_count_Object = MibScalar
media5_page_count = _Media5_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 3),
    _Media5_page_count_Type()
)
media5_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media5_page_count.setStatus("current")
_Media5_engine_media_mode_Type = Integer32
_Media5_engine_media_mode_Object = MibScalar
media5_engine_media_mode = _Media5_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 5, 4),
    _Media5_engine_media_mode_Type()
)
media5_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media5_engine_media_mode.setStatus("current")
_Media6_ObjectIdentity = ObjectIdentity
media6 = _Media6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6)
)


class _Media6_name_Type(DisplayString):
    """Custom type media6_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media6_name_Type.__name__ = "DisplayString"
_Media6_name_Object = MibScalar
media6_name = _Media6_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 1),
    _Media6_name_Type()
)
media6_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media6_name.setStatus("current")


class _Media6_short_name_Type(DisplayString):
    """Custom type media6_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media6_short_name_Type.__name__ = "DisplayString"
_Media6_short_name_Object = MibScalar
media6_short_name = _Media6_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 2),
    _Media6_short_name_Type()
)
media6_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media6_short_name.setStatus("current")
_Media6_page_count_Type = Integer32
_Media6_page_count_Object = MibScalar
media6_page_count = _Media6_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 3),
    _Media6_page_count_Type()
)
media6_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media6_page_count.setStatus("current")
_Media6_engine_media_mode_Type = Integer32
_Media6_engine_media_mode_Object = MibScalar
media6_engine_media_mode = _Media6_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 6, 4),
    _Media6_engine_media_mode_Type()
)
media6_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media6_engine_media_mode.setStatus("current")
_Media7_ObjectIdentity = ObjectIdentity
media7 = _Media7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7)
)


class _Media7_name_Type(DisplayString):
    """Custom type media7_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media7_name_Type.__name__ = "DisplayString"
_Media7_name_Object = MibScalar
media7_name = _Media7_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 1),
    _Media7_name_Type()
)
media7_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media7_name.setStatus("current")


class _Media7_short_name_Type(DisplayString):
    """Custom type media7_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media7_short_name_Type.__name__ = "DisplayString"
_Media7_short_name_Object = MibScalar
media7_short_name = _Media7_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 2),
    _Media7_short_name_Type()
)
media7_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media7_short_name.setStatus("current")
_Media7_page_count_Type = Integer32
_Media7_page_count_Object = MibScalar
media7_page_count = _Media7_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 3),
    _Media7_page_count_Type()
)
media7_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media7_page_count.setStatus("current")
_Media7_engine_media_mode_Type = Integer32
_Media7_engine_media_mode_Object = MibScalar
media7_engine_media_mode = _Media7_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 7, 4),
    _Media7_engine_media_mode_Type()
)
media7_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media7_engine_media_mode.setStatus("current")
_Media8_ObjectIdentity = ObjectIdentity
media8 = _Media8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8)
)


class _Media8_name_Type(DisplayString):
    """Custom type media8_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media8_name_Type.__name__ = "DisplayString"
_Media8_name_Object = MibScalar
media8_name = _Media8_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 1),
    _Media8_name_Type()
)
media8_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media8_name.setStatus("current")


class _Media8_short_name_Type(DisplayString):
    """Custom type media8_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media8_short_name_Type.__name__ = "DisplayString"
_Media8_short_name_Object = MibScalar
media8_short_name = _Media8_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 2),
    _Media8_short_name_Type()
)
media8_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media8_short_name.setStatus("current")
_Media8_page_count_Type = Integer32
_Media8_page_count_Object = MibScalar
media8_page_count = _Media8_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 3),
    _Media8_page_count_Type()
)
media8_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media8_page_count.setStatus("current")
_Media8_engine_media_mode_Type = Integer32
_Media8_engine_media_mode_Object = MibScalar
media8_engine_media_mode = _Media8_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 8, 4),
    _Media8_engine_media_mode_Type()
)
media8_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media8_engine_media_mode.setStatus("current")
_Media9_ObjectIdentity = ObjectIdentity
media9 = _Media9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9)
)


class _Media9_name_Type(DisplayString):
    """Custom type media9_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media9_name_Type.__name__ = "DisplayString"
_Media9_name_Object = MibScalar
media9_name = _Media9_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 1),
    _Media9_name_Type()
)
media9_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media9_name.setStatus("current")


class _Media9_short_name_Type(DisplayString):
    """Custom type media9_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media9_short_name_Type.__name__ = "DisplayString"
_Media9_short_name_Object = MibScalar
media9_short_name = _Media9_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 2),
    _Media9_short_name_Type()
)
media9_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media9_short_name.setStatus("current")
_Media9_page_count_Type = Integer32
_Media9_page_count_Object = MibScalar
media9_page_count = _Media9_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 3),
    _Media9_page_count_Type()
)
media9_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media9_page_count.setStatus("current")
_Media9_engine_media_mode_Type = Integer32
_Media9_engine_media_mode_Object = MibScalar
media9_engine_media_mode = _Media9_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 9, 4),
    _Media9_engine_media_mode_Type()
)
media9_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media9_engine_media_mode.setStatus("current")
_Media10_ObjectIdentity = ObjectIdentity
media10 = _Media10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10)
)


class _Media10_name_Type(DisplayString):
    """Custom type media10_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media10_name_Type.__name__ = "DisplayString"
_Media10_name_Object = MibScalar
media10_name = _Media10_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 1),
    _Media10_name_Type()
)
media10_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media10_name.setStatus("current")


class _Media10_short_name_Type(DisplayString):
    """Custom type media10_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media10_short_name_Type.__name__ = "DisplayString"
_Media10_short_name_Object = MibScalar
media10_short_name = _Media10_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 2),
    _Media10_short_name_Type()
)
media10_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media10_short_name.setStatus("current")
_Media10_page_count_Type = Integer32
_Media10_page_count_Object = MibScalar
media10_page_count = _Media10_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 3),
    _Media10_page_count_Type()
)
media10_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media10_page_count.setStatus("current")
_Media10_engine_media_mode_Type = Integer32
_Media10_engine_media_mode_Object = MibScalar
media10_engine_media_mode = _Media10_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 10, 4),
    _Media10_engine_media_mode_Type()
)
media10_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media10_engine_media_mode.setStatus("current")
_Media11_ObjectIdentity = ObjectIdentity
media11 = _Media11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11)
)


class _Media11_name_Type(DisplayString):
    """Custom type media11_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media11_name_Type.__name__ = "DisplayString"
_Media11_name_Object = MibScalar
media11_name = _Media11_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 1),
    _Media11_name_Type()
)
media11_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media11_name.setStatus("current")


class _Media11_short_name_Type(DisplayString):
    """Custom type media11_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media11_short_name_Type.__name__ = "DisplayString"
_Media11_short_name_Object = MibScalar
media11_short_name = _Media11_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 2),
    _Media11_short_name_Type()
)
media11_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media11_short_name.setStatus("current")
_Media11_page_count_Type = Integer32
_Media11_page_count_Object = MibScalar
media11_page_count = _Media11_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 3),
    _Media11_page_count_Type()
)
media11_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media11_page_count.setStatus("current")
_Media11_engine_media_mode_Type = Integer32
_Media11_engine_media_mode_Object = MibScalar
media11_engine_media_mode = _Media11_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 11, 4),
    _Media11_engine_media_mode_Type()
)
media11_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media11_engine_media_mode.setStatus("current")
_Media12_ObjectIdentity = ObjectIdentity
media12 = _Media12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12)
)


class _Media12_name_Type(DisplayString):
    """Custom type media12_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media12_name_Type.__name__ = "DisplayString"
_Media12_name_Object = MibScalar
media12_name = _Media12_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 1),
    _Media12_name_Type()
)
media12_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media12_name.setStatus("current")


class _Media12_short_name_Type(DisplayString):
    """Custom type media12_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media12_short_name_Type.__name__ = "DisplayString"
_Media12_short_name_Object = MibScalar
media12_short_name = _Media12_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 2),
    _Media12_short_name_Type()
)
media12_short_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media12_short_name.setStatus("current")
_Media12_page_count_Type = Integer32
_Media12_page_count_Object = MibScalar
media12_page_count = _Media12_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 3),
    _Media12_page_count_Type()
)
media12_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media12_page_count.setStatus("current")
_Media12_engine_media_mode_Type = Integer32
_Media12_engine_media_mode_Object = MibScalar
media12_engine_media_mode = _Media12_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 12, 4),
    _Media12_engine_media_mode_Type()
)
media12_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media12_engine_media_mode.setStatus("current")
_Media13_ObjectIdentity = ObjectIdentity
media13 = _Media13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13)
)


class _Media13_name_Type(DisplayString):
    """Custom type media13_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media13_name_Type.__name__ = "DisplayString"
_Media13_name_Object = MibScalar
media13_name = _Media13_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 1),
    _Media13_name_Type()
)
media13_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media13_name.setStatus("current")


class _Media13_short_name_Type(DisplayString):
    """Custom type media13_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media13_short_name_Type.__name__ = "DisplayString"
_Media13_short_name_Object = MibScalar
media13_short_name = _Media13_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 2),
    _Media13_short_name_Type()
)
media13_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media13_short_name.setStatus("current")
_Media13_page_count_Type = Integer32
_Media13_page_count_Object = MibScalar
media13_page_count = _Media13_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 3),
    _Media13_page_count_Type()
)
media13_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media13_page_count.setStatus("current")
_Media13_engine_media_mode_Type = Integer32
_Media13_engine_media_mode_Object = MibScalar
media13_engine_media_mode = _Media13_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 13, 4),
    _Media13_engine_media_mode_Type()
)
media13_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media13_engine_media_mode.setStatus("current")
_Media14_ObjectIdentity = ObjectIdentity
media14 = _Media14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14)
)


class _Media14_name_Type(DisplayString):
    """Custom type media14_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media14_name_Type.__name__ = "DisplayString"
_Media14_name_Object = MibScalar
media14_name = _Media14_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 1),
    _Media14_name_Type()
)
media14_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media14_name.setStatus("current")


class _Media14_short_name_Type(DisplayString):
    """Custom type media14_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media14_short_name_Type.__name__ = "DisplayString"
_Media14_short_name_Object = MibScalar
media14_short_name = _Media14_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 2),
    _Media14_short_name_Type()
)
media14_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media14_short_name.setStatus("current")
_Media14_page_count_Type = Integer32
_Media14_page_count_Object = MibScalar
media14_page_count = _Media14_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 3),
    _Media14_page_count_Type()
)
media14_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media14_page_count.setStatus("current")
_Media14_engine_media_mode_Type = Integer32
_Media14_engine_media_mode_Object = MibScalar
media14_engine_media_mode = _Media14_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 14, 4),
    _Media14_engine_media_mode_Type()
)
media14_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media14_engine_media_mode.setStatus("current")
_Media15_ObjectIdentity = ObjectIdentity
media15 = _Media15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15)
)


class _Media15_name_Type(DisplayString):
    """Custom type media15_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media15_name_Type.__name__ = "DisplayString"
_Media15_name_Object = MibScalar
media15_name = _Media15_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 1),
    _Media15_name_Type()
)
media15_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media15_name.setStatus("current")


class _Media15_short_name_Type(DisplayString):
    """Custom type media15_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media15_short_name_Type.__name__ = "DisplayString"
_Media15_short_name_Object = MibScalar
media15_short_name = _Media15_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 2),
    _Media15_short_name_Type()
)
media15_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media15_short_name.setStatus("current")
_Media15_page_count_Type = Integer32
_Media15_page_count_Object = MibScalar
media15_page_count = _Media15_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 3),
    _Media15_page_count_Type()
)
media15_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media15_page_count.setStatus("current")
_Media15_engine_media_mode_Type = Integer32
_Media15_engine_media_mode_Object = MibScalar
media15_engine_media_mode = _Media15_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 15, 4),
    _Media15_engine_media_mode_Type()
)
media15_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media15_engine_media_mode.setStatus("current")
_Media16_ObjectIdentity = ObjectIdentity
media16 = _Media16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16)
)


class _Media16_name_Type(DisplayString):
    """Custom type media16_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media16_name_Type.__name__ = "DisplayString"
_Media16_name_Object = MibScalar
media16_name = _Media16_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 1),
    _Media16_name_Type()
)
media16_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media16_name.setStatus("current")


class _Media16_short_name_Type(DisplayString):
    """Custom type media16_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media16_short_name_Type.__name__ = "DisplayString"
_Media16_short_name_Object = MibScalar
media16_short_name = _Media16_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 2),
    _Media16_short_name_Type()
)
media16_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media16_short_name.setStatus("current")
_Media16_page_count_Type = Integer32
_Media16_page_count_Object = MibScalar
media16_page_count = _Media16_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 3),
    _Media16_page_count_Type()
)
media16_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media16_page_count.setStatus("current")
_Media16_engine_media_mode_Type = Integer32
_Media16_engine_media_mode_Object = MibScalar
media16_engine_media_mode = _Media16_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 16, 4),
    _Media16_engine_media_mode_Type()
)
media16_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media16_engine_media_mode.setStatus("current")
_Media17_ObjectIdentity = ObjectIdentity
media17 = _Media17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17)
)


class _Media17_name_Type(DisplayString):
    """Custom type media17_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Media17_name_Type.__name__ = "DisplayString"
_Media17_name_Object = MibScalar
media17_name = _Media17_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 1),
    _Media17_name_Type()
)
media17_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media17_name.setStatus("current")


class _Media17_short_name_Type(DisplayString):
    """Custom type media17_short_name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_Media17_short_name_Type.__name__ = "DisplayString"
_Media17_short_name_Object = MibScalar
media17_short_name = _Media17_short_name_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 2),
    _Media17_short_name_Type()
)
media17_short_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media17_short_name.setStatus("current")
_Media17_page_count_Type = Integer32
_Media17_page_count_Object = MibScalar
media17_page_count = _Media17_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 3),
    _Media17_page_count_Type()
)
media17_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media17_page_count.setStatus("current")
_Media17_engine_media_mode_Type = Integer32
_Media17_engine_media_mode_Object = MibScalar
media17_engine_media_mode = _Media17_engine_media_mode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 17, 4),
    _Media17_engine_media_mode_Type()
)
media17_engine_media_mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media17_engine_media_mode.setStatus("current")
_Media18_ObjectIdentity = ObjectIdentity
media18 = _Media18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 18)
)
_Media19_ObjectIdentity = ObjectIdentity
media19 = _Media19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 19)
)
_Media20_ObjectIdentity = ObjectIdentity
media20 = _Media20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 20)
)
_Media21_ObjectIdentity = ObjectIdentity
media21 = _Media21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 21)
)
_Media22_ObjectIdentity = ObjectIdentity
media22 = _Media22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 22)
)
_Media23_ObjectIdentity = ObjectIdentity
media23 = _Media23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 23)
)
_Media24_ObjectIdentity = ObjectIdentity
media24 = _Media24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 24)
)
_Media25_ObjectIdentity = ObjectIdentity
media25 = _Media25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 25)
)
_Media26_ObjectIdentity = ObjectIdentity
media26 = _Media26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 26)
)
_Media27_ObjectIdentity = ObjectIdentity
media27 = _Media27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 27)
)
_Media28_ObjectIdentity = ObjectIdentity
media28 = _Media28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 28)
)
_Media29_ObjectIdentity = ObjectIdentity
media29 = _Media29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 29)
)
_Media30_ObjectIdentity = ObjectIdentity
media30 = _Media30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 30)
)
_Media31_ObjectIdentity = ObjectIdentity
media31 = _Media31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 31)
)
_Media32_ObjectIdentity = ObjectIdentity
media32 = _Media32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 32)
)
_Media33_ObjectIdentity = ObjectIdentity
media33 = _Media33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 33)
)
_Media34_ObjectIdentity = ObjectIdentity
media34 = _Media34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 34)
)
_Media35_ObjectIdentity = ObjectIdentity
media35 = _Media35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 35)
)
_Media36_ObjectIdentity = ObjectIdentity
media36 = _Media36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 36)
)
_Media37_ObjectIdentity = ObjectIdentity
media37 = _Media37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 37)
)
_Media38_ObjectIdentity = ObjectIdentity
media38 = _Media38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 3, 38)
)
_Media_modes_ObjectIdentity = ObjectIdentity
media_modes = _Media_modes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 4)
)
_Engine_media_modes_supported1_Type = DisplayString
_Engine_media_modes_supported1_Object = MibScalar
engine_media_modes_supported1 = _Engine_media_modes_supported1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 4, 1),
    _Engine_media_modes_supported1_Type()
)
engine_media_modes_supported1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_media_modes_supported1.setStatus("current")
_Media_size_ObjectIdentity = ObjectIdentity
media_size = _Media_size_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5)
)
_Media_size_count_Type = Integer32
_Media_size_count_Object = MibScalar
media_size_count = _Media_size_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5, 1),
    _Media_size_count_Type()
)
media_size_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media_size_count.setStatus("current")
_Media_size_west_edge_first_side_offset_Type = Integer32
_Media_size_west_edge_first_side_offset_Object = MibScalar
media_size_west_edge_first_side_offset = _Media_size_west_edge_first_side_offset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5, 2),
    _Media_size_west_edge_first_side_offset_Type()
)
media_size_west_edge_first_side_offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_size_west_edge_first_side_offset.setStatus("current")
_Media_size_west_edge_second_side_offset_Type = Integer32
_Media_size_west_edge_second_side_offset_Object = MibScalar
media_size_west_edge_second_side_offset = _Media_size_west_edge_second_side_offset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 5, 3),
    _Media_size_west_edge_second_side_offset_Type()
)
media_size_west_edge_second_side_offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    media_size_west_edge_second_side_offset.setStatus("current")
_Media_mode_details_ObjectIdentity = ObjectIdentity
media_mode_details = _Media_mode_details_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6)
)
_Media_mode1_ObjectIdentity = ObjectIdentity
media_mode1 = _Media_mode1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 1)
)
_Engine_media_mode1_page_count_Type = Integer32
_Engine_media_mode1_page_count_Object = MibScalar
engine_media_mode1_page_count = _Engine_media_mode1_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 1, 2),
    _Engine_media_mode1_page_count_Type()
)
engine_media_mode1_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_media_mode1_page_count.setStatus("current")
_Media_mode2_ObjectIdentity = ObjectIdentity
media_mode2 = _Media_mode2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 2)
)
_Engine_media_mode2_page_count_Type = Integer32
_Engine_media_mode2_page_count_Object = MibScalar
engine_media_mode2_page_count = _Engine_media_mode2_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 2, 2),
    _Engine_media_mode2_page_count_Type()
)
engine_media_mode2_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_media_mode2_page_count.setStatus("current")
_Media_mode3_ObjectIdentity = ObjectIdentity
media_mode3 = _Media_mode3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 3)
)
_Engine_media_mode3_page_count_Type = Integer32
_Engine_media_mode3_page_count_Object = MibScalar
engine_media_mode3_page_count = _Engine_media_mode3_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 3, 2),
    _Engine_media_mode3_page_count_Type()
)
engine_media_mode3_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_media_mode3_page_count.setStatus("current")
_Media_mode4_ObjectIdentity = ObjectIdentity
media_mode4 = _Media_mode4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 4)
)
_Engine_media_mode4_page_count_Type = Integer32
_Engine_media_mode4_page_count_Object = MibScalar
engine_media_mode4_page_count = _Engine_media_mode4_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 4, 2),
    _Engine_media_mode4_page_count_Type()
)
engine_media_mode4_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_media_mode4_page_count.setStatus("current")
_Media_mode5_ObjectIdentity = ObjectIdentity
media_mode5 = _Media_mode5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 5)
)
_Engine_media_mode5_page_count_Type = Integer32
_Engine_media_mode5_page_count_Object = MibScalar
engine_media_mode5_page_count = _Engine_media_mode5_page_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 6, 5, 2),
    _Engine_media_mode5_page_count_Type()
)
engine_media_mode5_page_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engine_media_mode5_page_count.setStatus("current")
_Media_counts_ObjectIdentity = ObjectIdentity
media_counts = _Media_counts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 7)
)
_Media_types_ObjectIdentity = ObjectIdentity
media_types = _Media_types_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 8)
)
_Media_number_of_type_supported_Type = Integer32
_Media_number_of_type_supported_Object = MibScalar
media_number_of_type_supported = _Media_number_of_type_supported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 8, 8, 1),
    _Media_number_of_type_supported_Type()
)
media_number_of_type_supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media_number_of_type_supported.setStatus("current")
_Consumables_ObjectIdentity = ObjectIdentity
consumables = _Consumables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10)
)
_Consumables_1_ObjectIdentity = ObjectIdentity
consumables_1 = _Consumables_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1)
)
_Consumable_status_ObjectIdentity = ObjectIdentity
consumable_status = _Consumable_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 1, 1)
)
_Consumables_status_ObjectIdentity = ObjectIdentity
consumables_status = _Consumables_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5)
)
_Consumables_life_ObjectIdentity = ObjectIdentity
consumables_life = _Consumables_life_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1)
)
_Consumable_life_usage_units_remaining_Type = Integer32
_Consumable_life_usage_units_remaining_Object = MibScalar
consumable_life_usage_units_remaining = _Consumable_life_usage_units_remaining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 1),
    _Consumable_life_usage_units_remaining_Type()
)
consumable_life_usage_units_remaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_life_usage_units_remaining.setStatus("current")


class _Consumable_life_usage_units_Type(Integer32):
    """Custom type consumable_life_usage_units based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ePagesRemaining", 1),
          ("eEstimatedPagesRemaining", 2),
          ("eUnknownUnits", 3),
          ("ePagesSinceLow", 4),
          ("ePagesSinceOut", 5),
          ("ePagesPicked", 6),
          ("ePercentLifeRemaining", 7),
          ("e4X6ImagesPrinted", 8),
          ("eEngineDropCount", 9),
          ("eEngineWebAdvances", 10))
    )


_Consumable_life_usage_units_Type.__name__ = "Integer32"
_Consumable_life_usage_units_Object = MibScalar
consumable_life_usage_units = _Consumable_life_usage_units_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 2),
    _Consumable_life_usage_units_Type()
)
consumable_life_usage_units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_life_usage_units.setStatus("current")
_Consumable_life_low_threshold_Type = Integer32
_Consumable_life_low_threshold_Object = MibScalar
consumable_life_low_threshold = _Consumable_life_low_threshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 3),
    _Consumable_life_low_threshold_Type()
)
consumable_life_low_threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_life_low_threshold.setStatus("current")
_Estimated_page_yield_Type = Integer32
_Estimated_page_yield_Object = MibScalar
estimated_page_yield = _Estimated_page_yield_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 4),
    _Estimated_page_yield_Type()
)
estimated_page_yield.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estimated_page_yield.setStatus("current")


class _Estimated_page_yield_unit_Type(Integer32):
    """Custom type estimated_page_yield_unit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e5PercentPages", 1),
          ("eISOPages", 2))
    )


_Estimated_page_yield_unit_Type.__name__ = "Integer32"
_Estimated_page_yield_unit_Object = MibScalar
estimated_page_yield_unit = _Estimated_page_yield_unit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 5),
    _Estimated_page_yield_unit_Type()
)
estimated_page_yield_unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    estimated_page_yield_unit.setStatus("current")
_Supplies_at_very_low_delay_limit_Type = Integer32
_Supplies_at_very_low_delay_limit_Object = MibScalar
supplies_at_very_low_delay_limit = _Supplies_at_very_low_delay_limit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 1, 6),
    _Supplies_at_very_low_delay_limit_Type()
)
supplies_at_very_low_delay_limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplies_at_very_low_delay_limit.setStatus("current")


class _Supplies_at_very_low_delay_Type(Integer32):
    """Custom type supplies_at_very_low_delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eDisabled", 1),
          ("eEnabled", 2))
    )


_Supplies_at_very_low_delay_Type.__name__ = "Integer32"
_Supplies_at_very_low_delay_Object = MibScalar
supplies_at_very_low_delay = _Supplies_at_very_low_delay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 5, 2),
    _Supplies_at_very_low_delay_Type()
)
supplies_at_very_low_delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplies_at_very_low_delay.setStatus("current")


class _Consumable_current_state_Type(Integer32):
    """Custom type consumable_current_state based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("cAuthLevel1", 0),
          ("cAuthLevel2", 1),
          ("cAuthLevel3", 2),
          ("cAuthLevel4", 3),
          ("cAuthLevel5", 4),
          ("cAuthLevel6", 5),
          ("cAuthLevel7", 6),
          ("cGenuineHPUnsupported", 8),
          ("cELabelDefective", 9),
          ("cELabelMissing", 10),
          ("cLowCondition", 11),
          ("cOutCondition", 12),
          ("cIncorrect", 13),
          ("cMissing", 14),
          ("cPastOutCondition", 15),
          ("cConfigurableLow", 16),
          ("cExpired", 17),
          ("cFailure", 18),
          ("cLeak", 19),
          ("cUnknownManufacturer", 20),
          ("cUnsupported", 21),
          ("cUnavailable", 22),
          ("cIncompatible", 23),
          ("cStatusAreValid", 31))
    )


_Consumable_current_state_Type.__name__ = "Integer32"
_Consumable_current_state_Object = MibScalar
consumable_current_state = _Consumable_current_state_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 7),
    _Consumable_current_state_Type()
)
consumable_current_state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_current_state.setStatus("current")
_Consumable_string_ObjectIdentity = ObjectIdentity
consumable_string = _Consumable_string_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 8)
)


class _Device_used_while_cartridge_out_override_active_Type(Integer32):
    """Custom type device_used_while_cartridge_out_override_active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eNotUsed", 1),
          ("eUsed", 2))
    )


_Device_used_while_cartridge_out_override_active_Type.__name__ = "Integer32"
_Device_used_while_cartridge_out_override_active_Object = MibScalar
device_used_while_cartridge_out_override_active = _Device_used_while_cartridge_out_override_active_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 9),
    _Device_used_while_cartridge_out_override_active_Type()
)
device_used_while_cartridge_out_override_active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_used_while_cartridge_out_override_active.setStatus("current")
_Consumable_pages_printed_with_supply_Type = Integer32
_Consumable_pages_printed_with_supply_Object = MibScalar
consumable_pages_printed_with_supply = _Consumable_pages_printed_with_supply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 11),
    _Consumable_pages_printed_with_supply_Type()
)
consumable_pages_printed_with_supply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consumable_pages_printed_with_supply.setStatus("current")
_Total_kilo_pixels_per_cartridge_Type = Integer32
_Total_kilo_pixels_per_cartridge_Object = MibScalar
total_kilo_pixels_per_cartridge = _Total_kilo_pixels_per_cartridge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 15),
    _Total_kilo_pixels_per_cartridge_Type()
)
total_kilo_pixels_per_cartridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    total_kilo_pixels_per_cartridge.setStatus("current")
_Consumable_replacement_count_Type = Integer32
_Consumable_replacement_count_Object = MibScalar
consumable_replacement_count = _Consumable_replacement_count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 16),
    _Consumable_replacement_count_Type()
)
consumable_replacement_count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_replacement_count.setStatus("current")
_Consumable_pages_since_replacement_Type = Integer32
_Consumable_pages_since_replacement_Object = MibScalar
consumable_pages_since_replacement = _Consumable_pages_since_replacement_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 10, 18),
    _Consumable_pages_since_replacement_Type()
)
consumable_pages_since_replacement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consumable_pages_since_replacement.setStatus("current")
_Print_meter_ObjectIdentity = ObjectIdentity
print_meter = _Print_meter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11)
)
_Printer_average_ObjectIdentity = ObjectIdentity
printer_average = _Printer_average_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1)
)
_Printer_average_marking_agent_units_per_gram_Type = OctetString
_Printer_average_marking_agent_units_per_gram_Object = MibScalar
printer_average_marking_agent_units_per_gram = _Printer_average_marking_agent_units_per_gram_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1, 4),
    _Printer_average_marking_agent_units_per_gram_Type()
)
printer_average_marking_agent_units_per_gram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_average_marking_agent_units_per_gram.setStatus("current")
_Printer_average_marking_agent_coverage_actual_Type = OctetString
_Printer_average_marking_agent_coverage_actual_Object = MibScalar
printer_average_marking_agent_coverage_actual = _Printer_average_marking_agent_coverage_actual_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 11, 1, 5),
    _Printer_average_marking_agent_coverage_actual_Type()
)
printer_average_marking_agent_coverage_actual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    printer_average_marking_agent_coverage_actual.setStatus("current")
_Menus_ObjectIdentity = ObjectIdentity
menus = _Menus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 13)
)
_Media_sizes_ObjectIdentity = ObjectIdentity
media_sizes = _Media_sizes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 15)
)
_Media_size_supported_driver_n_string_Type = OctetString
_Media_size_supported_driver_n_string_Object = MibScalar
media_size_supported_driver_n_string = _Media_size_supported_driver_n_string_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 1, 15, 1),
    _Media_size_supported_driver_n_string_Type()
)
media_size_supported_driver_n_string.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    media_size_supported_driver_n_string.setStatus("current")
_Fax_send_ObjectIdentity = ObjectIdentity
fax_send = _Fax_send_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2)
)
_Settings_fax_send_ObjectIdentity = ObjectIdentity
settings_fax_send = _Settings_fax_send_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1)
)


class _Fax_resolution_Type(OctetString):
    """Custom type fax_resolution based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Fax_resolution_Type.__name__ = "OctetString"
_Fax_resolution_Object = MibScalar
fax_resolution = _Fax_resolution_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1, 1),
    _Fax_resolution_Type()
)
fax_resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_resolution.setStatus("current")


class _Fax_contrast_Type(Integer32):
    """Custom type fax_contrast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_Fax_contrast_Type.__name__ = "Integer32"
_Fax_contrast_Object = MibScalar
fax_contrast = _Fax_contrast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1, 2),
    _Fax_contrast_Type()
)
fax_contrast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_contrast.setStatus("current")


class _Fax_pixel_data_type_Type(Integer32):
    """Custom type fax_pixel_data_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eBiLevelThesholded", 1),
          ("eBiLevelHalfToned", 2))
    )


_Fax_pixel_data_type_Type.__name__ = "Integer32"
_Fax_pixel_data_type_Object = MibScalar
fax_pixel_data_type = _Fax_pixel_data_type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 1, 3),
    _Fax_pixel_data_type_Type()
)
fax_pixel_data_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_pixel_data_type.setStatus("current")
_Status_fax_send_ObjectIdentity = ObjectIdentity
status_fax_send = _Status_fax_send_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 2)
)
_Not_ready_fax_send_Type = OctetString
_Not_ready_fax_send_Object = MibScalar
not_ready_fax_send = _Not_ready_fax_send_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 2, 1),
    _Not_ready_fax_send_Type()
)
not_ready_fax_send.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    not_ready_fax_send.setStatus("current")
_Transmit_fax_ObjectIdentity = ObjectIdentity
transmit_fax = _Transmit_fax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 5)
)


class _Fax_allow_redials_Type(Integer32):
    """Custom type fax_allow_redials based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eFalse", 1),
          ("eTrue", 2))
    )


_Fax_allow_redials_Type.__name__ = "Integer32"
_Fax_allow_redials_Object = MibScalar
fax_allow_redials = _Fax_allow_redials_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 4, 2, 5, 3),
    _Fax_allow_redials_Type()
)
fax_allow_redials.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fax_allow_redials.setStatus("current")
_Channel_ObjectIdentity = ObjectIdentity
channel = _Channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6)
)
_Channelnumberofchannels_Type = Integer32
_Channelnumberofchannels_Object = MibScalar
channelnumberofchannels = _Channelnumberofchannels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 1),
    _Channelnumberofchannels_Type()
)
channelnumberofchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelnumberofchannels.setStatus("current")
_Channelprinteralert_Type = OctetString
_Channelprinteralert_Object = MibScalar
channelprinteralert = _Channelprinteralert_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 2),
    _Channelprinteralert_Type()
)
channelprinteralert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelprinteralert.setStatus("current")
_ChannelTable_ObjectIdentity = ObjectIdentity
channelTable = _ChannelTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3)
)
_ChannelEntry_ObjectIdentity = ObjectIdentity
channelEntry = _ChannelEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1)
)


class _Channeltype_Type(Integer32):
    """Custom type channeltype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              9,
              10,
              11,
              15,
              38)
        )
    )
    namedValues = NamedValues(
        *(("eChOther", 1),
          ("eChAppleTalkPAP", 7),
          ("eChLPDServer", 8),
          ("eChNetwareRPrinter", 9),
          ("eChNetwarePServer", 10),
          ("eChPort9100", 11),
          ("eChDLCLLCPort", 15),
          ("eChBidirPortTCP", 38))
    )


_Channeltype_Type.__name__ = "Integer32"
_Channeltype_Object = MibScalar
channeltype = _Channeltype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 2),
    _Channeltype_Type()
)
channeltype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channeltype.setStatus("current")
_Channelprotocolversion_Type = OctetString
_Channelprotocolversion_Object = MibScalar
channelprotocolversion = _Channelprotocolversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 3),
    _Channelprotocolversion_Type()
)
channelprotocolversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelprotocolversion.setStatus("current")


class _Channelstate_Type(Integer32):
    """Custom type channelstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eChOther", 1),
          ("eChPrintDataAccecped", 3),
          ("eChNoDataAccepted", 4))
    )


_Channelstate_Type.__name__ = "Integer32"
_Channelstate_Object = MibScalar
channelstate = _Channelstate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 4),
    _Channelstate_Type()
)
channelstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelstate.setStatus("current")
_Channelifindex_Type = Integer32
_Channelifindex_Object = MibScalar
channelifindex = _Channelifindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 5),
    _Channelifindex_Type()
)
channelifindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelifindex.setStatus("current")
_Channelstatus_Type = Integer32
_Channelstatus_Object = MibScalar
channelstatus = _Channelstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 6),
    _Channelstatus_Type()
)
channelstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelstatus.setStatus("current")
_Channelinformation_Type = OctetString
_Channelinformation_Object = MibScalar
channelinformation = _Channelinformation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 6, 3, 1, 7),
    _Channelinformation_Type()
)
channelinformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelinformation.setStatus("current")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7)
)
_Channel_table_ObjectIdentity = ObjectIdentity
channel_table = _Channel_table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2)
)
_Channel_entry_ObjectIdentity = ObjectIdentity
channel_entry = _Channel_entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1)
)
_Channel_bytes_sent_Type = Integer32
_Channel_bytes_sent_Object = MibScalar
channel_bytes_sent = _Channel_bytes_sent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 2),
    _Channel_bytes_sent_Type()
)
channel_bytes_sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_bytes_sent.setStatus("current")
_Channel_bytes_received_Type = Integer32
_Channel_bytes_received_Object = MibScalar
channel_bytes_received = _Channel_bytes_received_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 3),
    _Channel_bytes_received_Type()
)
channel_bytes_received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_bytes_received.setStatus("current")
_Channel_io_errors_Type = Integer32
_Channel_io_errors_Object = MibScalar
channel_io_errors = _Channel_io_errors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 4),
    _Channel_io_errors_Type()
)
channel_io_errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_io_errors.setStatus("current")
_Channel_jobs_received_Type = Integer32
_Channel_jobs_received_Object = MibScalar
channel_jobs_received = _Channel_jobs_received_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 5),
    _Channel_jobs_received_Type()
)
channel_jobs_received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_jobs_received.setStatus("current")
_Channel_mio_Type = Integer32
_Channel_mio_Object = MibScalar
channel_mio = _Channel_mio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 1, 7, 2, 1, 6),
    _Channel_mio_Type()
)
channel_mio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_mio.setStatus("current")
_Printmib_ObjectIdentity = ObjectIdentity
printmib = _Printmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2)
)
_PrtGeneral_ObjectIdentity = ObjectIdentity
prtGeneral = _PrtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5)
)
_PrtGeneralTable_ObjectIdentity = ObjectIdentity
prtGeneralTable = _PrtGeneralTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1)
)
_PrtGeneralEntry_ObjectIdentity = ObjectIdentity
prtGeneralEntry = _PrtGeneralEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1)
)


class _Prtgeneralconfigchanges_Type(Integer32):
    """Custom type prtgeneralconfigchanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_Prtgeneralconfigchanges_Type.__name__ = "Integer32"
_Prtgeneralconfigchanges_Object = MibScalar
prtgeneralconfigchanges = _Prtgeneralconfigchanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 1),
    _Prtgeneralconfigchanges_Type()
)
prtgeneralconfigchanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralconfigchanges.setStatus("current")


class _Prtgeneralcurrentlocalization_Type(Integer32):
    """Custom type prtgeneralcurrentlocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_Prtgeneralcurrentlocalization_Type.__name__ = "Integer32"
_Prtgeneralcurrentlocalization_Object = MibScalar
prtgeneralcurrentlocalization = _Prtgeneralcurrentlocalization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 2),
    _Prtgeneralcurrentlocalization_Type()
)
prtgeneralcurrentlocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralcurrentlocalization.setStatus("current")


class _Prtgeneralreset_Type(Integer32):
    """Custom type prtgeneralreset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ePnotResetting", 3),
          ("ePpowerCycleReset", 4),
          ("ePresetToNVRAM", 5),
          ("ePresetToFactoryDefaults", 6))
    )


_Prtgeneralreset_Type.__name__ = "Integer32"
_Prtgeneralreset_Object = MibScalar
prtgeneralreset = _Prtgeneralreset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 3),
    _Prtgeneralreset_Type()
)
prtgeneralreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralreset.setStatus("current")


class _Prtgeneralcurrentoperator_Type(OctetString):
    """Custom type prtgeneralcurrentoperator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Prtgeneralcurrentoperator_Type.__name__ = "OctetString"
_Prtgeneralcurrentoperator_Object = MibScalar
prtgeneralcurrentoperator = _Prtgeneralcurrentoperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 4),
    _Prtgeneralcurrentoperator_Type()
)
prtgeneralcurrentoperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralcurrentoperator.setStatus("current")


class _Prtgeneralserviceperson_Type(OctetString):
    """Custom type prtgeneralserviceperson based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Prtgeneralserviceperson_Type.__name__ = "OctetString"
_Prtgeneralserviceperson_Object = MibScalar
prtgeneralserviceperson = _Prtgeneralserviceperson_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 5),
    _Prtgeneralserviceperson_Type()
)
prtgeneralserviceperson.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralserviceperson.setStatus("current")
_Prtinputdefaultindex_Type = Integer32
_Prtinputdefaultindex_Object = MibScalar
prtinputdefaultindex = _Prtinputdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 6),
    _Prtinputdefaultindex_Type()
)
prtinputdefaultindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputdefaultindex.setStatus("current")
_Prtoutputdefaultindex_Type = Integer32
_Prtoutputdefaultindex_Object = MibScalar
prtoutputdefaultindex = _Prtoutputdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 7),
    _Prtoutputdefaultindex_Type()
)
prtoutputdefaultindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtoutputdefaultindex.setStatus("current")


class _Prtmarkerdefaultindex_Type(Integer32):
    """Custom type prtmarkerdefaultindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Prtmarkerdefaultindex_Type.__name__ = "Integer32"
_Prtmarkerdefaultindex_Object = MibScalar
prtmarkerdefaultindex = _Prtmarkerdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 8),
    _Prtmarkerdefaultindex_Type()
)
prtmarkerdefaultindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerdefaultindex.setStatus("current")


class _Prtmediapathdefaultindex_Type(Integer32):
    """Custom type prtmediapathdefaultindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Prtmediapathdefaultindex_Type.__name__ = "Integer32"
_Prtmediapathdefaultindex_Object = MibScalar
prtmediapathdefaultindex = _Prtmediapathdefaultindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 9),
    _Prtmediapathdefaultindex_Type()
)
prtmediapathdefaultindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtmediapathdefaultindex.setStatus("current")


class _Prtconsolelocalization_Type(Integer32):
    """Custom type prtconsolelocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_Prtconsolelocalization_Type.__name__ = "Integer32"
_Prtconsolelocalization_Object = MibScalar
prtconsolelocalization = _Prtconsolelocalization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 10),
    _Prtconsolelocalization_Type()
)
prtconsolelocalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtconsolelocalization.setStatus("current")


class _Prtconsolenumberofdisplaylines_Type(Integer32):
    """Custom type prtconsolenumberofdisplaylines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtconsolenumberofdisplaylines_Type.__name__ = "Integer32"
_Prtconsolenumberofdisplaylines_Object = MibScalar
prtconsolenumberofdisplaylines = _Prtconsolenumberofdisplaylines_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 11),
    _Prtconsolenumberofdisplaylines_Type()
)
prtconsolenumberofdisplaylines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsolenumberofdisplaylines.setStatus("current")


class _Prtconsolenumberofdisplaychars_Type(Integer32):
    """Custom type prtconsolenumberofdisplaychars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtconsolenumberofdisplaychars_Type.__name__ = "Integer32"
_Prtconsolenumberofdisplaychars_Object = MibScalar
prtconsolenumberofdisplaychars = _Prtconsolenumberofdisplaychars_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 12),
    _Prtconsolenumberofdisplaychars_Type()
)
prtconsolenumberofdisplaychars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsolenumberofdisplaychars.setStatus("current")


class _Prtconsoledisable_Type(Integer32):
    """Custom type prtconsoledisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ePoperatorConsoleEnabled", 3),
          ("ePoperatorConsoleDisabled", 4),
          ("ePoperatorConsoleEnabledLevel1", 5),
          ("ePoperatorConsoleEnabledLevel2", 6))
    )


_Prtconsoledisable_Type.__name__ = "Integer32"
_Prtconsoledisable_Object = MibScalar
prtconsoledisable = _Prtconsoledisable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 13),
    _Prtconsoledisable_Type()
)
prtconsoledisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtconsoledisable.setStatus("current")


class _Prtgeneralstartuppage_Type(Integer32):
    """Custom type prtgeneralstartuppage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("ePnotPresent", 5)
    )


_Prtgeneralstartuppage_Type.__name__ = "Integer32"
_Prtgeneralstartuppage_Object = MibScalar
prtgeneralstartuppage = _Prtgeneralstartuppage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 14),
    _Prtgeneralstartuppage_Type()
)
prtgeneralstartuppage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralstartuppage.setStatus("current")


class _Prtgeneralbannerpage_Type(Integer32):
    """Custom type prtgeneralbannerpage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("ePnotPresent", 5)
    )


_Prtgeneralbannerpage_Type.__name__ = "Integer32"
_Prtgeneralbannerpage_Object = MibScalar
prtgeneralbannerpage = _Prtgeneralbannerpage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 15),
    _Prtgeneralbannerpage_Type()
)
prtgeneralbannerpage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralbannerpage.setStatus("current")


class _Prtgeneralprintername_Type(OctetString):
    """Custom type prtgeneralprintername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Prtgeneralprintername_Type.__name__ = "OctetString"
_Prtgeneralprintername_Object = MibScalar
prtgeneralprintername = _Prtgeneralprintername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 16),
    _Prtgeneralprintername_Type()
)
prtgeneralprintername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtgeneralprintername.setStatus("current")


class _Prtgeneralserialnumber_Type(OctetString):
    """Custom type prtgeneralserialnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Prtgeneralserialnumber_Type.__name__ = "OctetString"
_Prtgeneralserialnumber_Object = MibScalar
prtgeneralserialnumber = _Prtgeneralserialnumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 17),
    _Prtgeneralserialnumber_Type()
)
prtgeneralserialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtgeneralserialnumber.setStatus("current")
_Prtalertcriticalevents_Type = Integer32
_Prtalertcriticalevents_Object = MibScalar
prtalertcriticalevents = _Prtalertcriticalevents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 18),
    _Prtalertcriticalevents_Type()
)
prtalertcriticalevents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertcriticalevents.setStatus("current")
_Prtalertallevents_Type = Integer32
_Prtalertallevents_Object = MibScalar
prtalertallevents = _Prtalertallevents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 1, 1, 19),
    _Prtalertallevents_Type()
)
prtalertallevents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertallevents.setStatus("current")
_PrtStorageRefTable_ObjectIdentity = ObjectIdentity
prtStorageRefTable = _PrtStorageRefTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 2)
)
_PrtStorageRefEntry_ObjectIdentity = ObjectIdentity
prtStorageRefEntry = _PrtStorageRefEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 2, 1)
)


class _Prtstoragerefindex_Type(Integer32):
    """Custom type prtstoragerefindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Prtstoragerefindex_Type.__name__ = "Integer32"
_Prtstoragerefindex_Object = MibScalar
prtstoragerefindex = _Prtstoragerefindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 2, 1, 2),
    _Prtstoragerefindex_Type()
)
prtstoragerefindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtstoragerefindex.setStatus("current")
_PrtDeviceRefTable_ObjectIdentity = ObjectIdentity
prtDeviceRefTable = _PrtDeviceRefTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 3)
)
_PrtDeviceRefEntry_ObjectIdentity = ObjectIdentity
prtDeviceRefEntry = _PrtDeviceRefEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 3, 1)
)


class _Prtdevicerefindex_Type(Integer32):
    """Custom type prtdevicerefindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Prtdevicerefindex_Type.__name__ = "Integer32"
_Prtdevicerefindex_Object = MibScalar
prtdevicerefindex = _Prtdevicerefindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 5, 3, 1, 2),
    _Prtdevicerefindex_Type()
)
prtdevicerefindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtdevicerefindex.setStatus("current")
_PrtCover_ObjectIdentity = ObjectIdentity
prtCover = _PrtCover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6)
)
_PrtCoverTable_ObjectIdentity = ObjectIdentity
prtCoverTable = _PrtCoverTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1)
)
_PrtCoverEntry_ObjectIdentity = ObjectIdentity
prtCoverEntry = _PrtCoverEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1, 1)
)


class _Prtcoverdescription_Type(OctetString):
    """Custom type prtcoverdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtcoverdescription_Type.__name__ = "OctetString"
_Prtcoverdescription_Object = MibScalar
prtcoverdescription = _Prtcoverdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1, 1, 2),
    _Prtcoverdescription_Type()
)
prtcoverdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtcoverdescription.setStatus("current")


class _Prtcoverstatus_Type(Integer32):
    """Custom type prtcoverstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePdoorOpen", 3),
          ("ePdoorClosed", 4))
    )


_Prtcoverstatus_Type.__name__ = "Integer32"
_Prtcoverstatus_Object = MibScalar
prtcoverstatus = _Prtcoverstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 6, 1, 1, 3),
    _Prtcoverstatus_Type()
)
prtcoverstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtcoverstatus.setStatus("current")
_PrtLocalization_ObjectIdentity = ObjectIdentity
prtLocalization = _PrtLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7)
)
_PrtLocalizationTable_ObjectIdentity = ObjectIdentity
prtLocalizationTable = _PrtLocalizationTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1)
)
_PrtLocalizationEntry_ObjectIdentity = ObjectIdentity
prtLocalizationEntry = _PrtLocalizationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1)
)


class _Prtlocalizationlanguage_Type(OctetString):
    """Custom type prtlocalizationlanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Prtlocalizationlanguage_Type.__name__ = "OctetString"
_Prtlocalizationlanguage_Object = MibScalar
prtlocalizationlanguage = _Prtlocalizationlanguage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1, 2),
    _Prtlocalizationlanguage_Type()
)
prtlocalizationlanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtlocalizationlanguage.setStatus("current")


class _Prtlocalizationcountry_Type(OctetString):
    """Custom type prtlocalizationcountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Prtlocalizationcountry_Type.__name__ = "OctetString"
_Prtlocalizationcountry_Object = MibScalar
prtlocalizationcountry = _Prtlocalizationcountry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1, 3),
    _Prtlocalizationcountry_Type()
)
prtlocalizationcountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtlocalizationcountry.setStatus("current")


class _Prtlocalizationcharacterset_Type(Integer32):
    """Custom type prtlocalizationcharacterset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              8,
              12,
              2004,
              2024)
        )
    )
    namedValues = NamedValues(
        *(("ePcsISOLatin2", 5),
          ("ePcsISOLatinCyrillic", 8),
          ("ePcsISOLatin5", 12),
          ("ePcsHPRoman8", 2004),
          ("ePcsWindows31J", 2024))
    )


_Prtlocalizationcharacterset_Type.__name__ = "Integer32"
_Prtlocalizationcharacterset_Object = MibScalar
prtlocalizationcharacterset = _Prtlocalizationcharacterset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 7, 1, 1, 4),
    _Prtlocalizationcharacterset_Type()
)
prtlocalizationcharacterset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtlocalizationcharacterset.setStatus("current")
_PrtInput_ObjectIdentity = ObjectIdentity
prtInput = _PrtInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8)
)
_PrtInputTable_ObjectIdentity = ObjectIdentity
prtInputTable = _PrtInputTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2)
)
_PrtInputEntry_ObjectIdentity = ObjectIdentity
prtInputEntry = _PrtInputEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1)
)


class _Prtinputtype_Type(Integer32):
    """Custom type prtinputtype based on Integer32"""
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
        *(("ePother", 1),
          ("ePunknown", 2),
          ("ePsheetFeedAutoRemovableTray", 3),
          ("ePsheetFeedAutoNonRemovableTray", 4),
          ("ePsheetFeedManual", 5),
          ("ePcontinuousRoll", 6),
          ("ePcontinuousFanFold", 7))
    )


_Prtinputtype_Type.__name__ = "Integer32"
_Prtinputtype_Object = MibScalar
prtinputtype = _Prtinputtype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 2),
    _Prtinputtype_Type()
)
prtinputtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputtype.setStatus("current")


class _Prtinputdimunit_Type(Integer32):
    """Custom type prtinputdimunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePtenThousandthsOfInches", 3),
          ("ePmicrometers", 4))
    )


_Prtinputdimunit_Type.__name__ = "Integer32"
_Prtinputdimunit_Object = MibScalar
prtinputdimunit = _Prtinputdimunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 3),
    _Prtinputdimunit_Type()
)
prtinputdimunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputdimunit.setStatus("current")
_Prtinputmediadimfeeddirdeclared_Type = Integer32
_Prtinputmediadimfeeddirdeclared_Object = MibScalar
prtinputmediadimfeeddirdeclared = _Prtinputmediadimfeeddirdeclared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 4),
    _Prtinputmediadimfeeddirdeclared_Type()
)
prtinputmediadimfeeddirdeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinputmediadimfeeddirdeclared.setStatus("current")
_Prtinputmediadimxfeeddirdeclared_Type = Integer32
_Prtinputmediadimxfeeddirdeclared_Object = MibScalar
prtinputmediadimxfeeddirdeclared = _Prtinputmediadimxfeeddirdeclared_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 5),
    _Prtinputmediadimxfeeddirdeclared_Type()
)
prtinputmediadimxfeeddirdeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinputmediadimxfeeddirdeclared.setStatus("current")
_Prtinputmediadimfeeddirchosen_Type = Integer32
_Prtinputmediadimfeeddirchosen_Object = MibScalar
prtinputmediadimfeeddirchosen = _Prtinputmediadimfeeddirchosen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 6),
    _Prtinputmediadimfeeddirchosen_Type()
)
prtinputmediadimfeeddirchosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmediadimfeeddirchosen.setStatus("current")
_Prtinputmediadimxfeeddirchosen_Type = Integer32
_Prtinputmediadimxfeeddirchosen_Object = MibScalar
prtinputmediadimxfeeddirchosen = _Prtinputmediadimxfeeddirchosen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 7),
    _Prtinputmediadimxfeeddirchosen_Type()
)
prtinputmediadimxfeeddirchosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmediadimxfeeddirchosen.setStatus("current")


class _Prtinputcapacityunit_Type(Integer32):
    """Custom type prtinputcapacityunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              8,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ePtenThousandthsOfInches", 3),
          ("ePmicrometers", 4),
          ("ePsheets", 8),
          ("ePfeet", 16),
          ("ePmeters", 17))
    )


_Prtinputcapacityunit_Type.__name__ = "Integer32"
_Prtinputcapacityunit_Object = MibScalar
prtinputcapacityunit = _Prtinputcapacityunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 8),
    _Prtinputcapacityunit_Type()
)
prtinputcapacityunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputcapacityunit.setStatus("current")
_Prtinputmaxcapacity_Type = Integer32
_Prtinputmaxcapacity_Object = MibScalar
prtinputmaxcapacity = _Prtinputmaxcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 9),
    _Prtinputmaxcapacity_Type()
)
prtinputmaxcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmaxcapacity.setStatus("current")
_Prtinputcurrentlevel_Type = Integer32
_Prtinputcurrentlevel_Object = MibScalar
prtinputcurrentlevel = _Prtinputcurrentlevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 10),
    _Prtinputcurrentlevel_Type()
)
prtinputcurrentlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputcurrentlevel.setStatus("current")
_Prtinputstatus_Type = Integer32
_Prtinputstatus_Object = MibScalar
prtinputstatus = _Prtinputstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 11),
    _Prtinputstatus_Type()
)
prtinputstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputstatus.setStatus("current")


class _Prtinputmedianame_Type(OctetString):
    """Custom type prtinputmedianame based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputmedianame_Type.__name__ = "OctetString"
_Prtinputmedianame_Object = MibScalar
prtinputmedianame = _Prtinputmedianame_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 12),
    _Prtinputmedianame_Type()
)
prtinputmedianame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinputmedianame.setStatus("current")


class _Prtinputname_Type(OctetString):
    """Custom type prtinputname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputname_Type.__name__ = "OctetString"
_Prtinputname_Object = MibScalar
prtinputname = _Prtinputname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 13),
    _Prtinputname_Type()
)
prtinputname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputname.setStatus("current")


class _Prtinputvendorname_Type(OctetString):
    """Custom type prtinputvendorname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputvendorname_Type.__name__ = "OctetString"
_Prtinputvendorname_Object = MibScalar
prtinputvendorname = _Prtinputvendorname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 14),
    _Prtinputvendorname_Type()
)
prtinputvendorname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputvendorname.setStatus("current")


class _Prtinputmodel_Type(OctetString):
    """Custom type prtinputmodel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputmodel_Type.__name__ = "OctetString"
_Prtinputmodel_Object = MibScalar
prtinputmodel = _Prtinputmodel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 15),
    _Prtinputmodel_Type()
)
prtinputmodel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmodel.setStatus("current")


class _Prtinputversion_Type(OctetString):
    """Custom type prtinputversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputversion_Type.__name__ = "OctetString"
_Prtinputversion_Object = MibScalar
prtinputversion = _Prtinputversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 16),
    _Prtinputversion_Type()
)
prtinputversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputversion.setStatus("current")


class _Prtinputserialnumber_Type(OctetString):
    """Custom type prtinputserialnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtinputserialnumber_Type.__name__ = "OctetString"
_Prtinputserialnumber_Object = MibScalar
prtinputserialnumber = _Prtinputserialnumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 17),
    _Prtinputserialnumber_Type()
)
prtinputserialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputserialnumber.setStatus("current")


class _Prtinputdescription_Type(OctetString):
    """Custom type prtinputdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtinputdescription_Type.__name__ = "OctetString"
_Prtinputdescription_Object = MibScalar
prtinputdescription = _Prtinputdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 18),
    _Prtinputdescription_Type()
)
prtinputdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputdescription.setStatus("current")


class _Prtinputsecurity_Type(Integer32):
    """Custom type prtinputsecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePon", 3),
          ("ePoff", 4),
          ("ePnotPresent", 5))
    )


_Prtinputsecurity_Type.__name__ = "Integer32"
_Prtinputsecurity_Object = MibScalar
prtinputsecurity = _Prtinputsecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 19),
    _Prtinputsecurity_Type()
)
prtinputsecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputsecurity.setStatus("current")
_Prtinputmedialoadtimeout_Type = Integer32
_Prtinputmedialoadtimeout_Object = MibScalar
prtinputmedialoadtimeout = _Prtinputmedialoadtimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 24),
    _Prtinputmedialoadtimeout_Type()
)
prtinputmedialoadtimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputmedialoadtimeout.setStatus("current")
_Prtinputnextindex_Type = Integer32
_Prtinputnextindex_Object = MibScalar
prtinputnextindex = _Prtinputnextindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 8, 2, 1, 26),
    _Prtinputnextindex_Type()
)
prtinputnextindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinputnextindex.setStatus("current")
_PrtOutput_ObjectIdentity = ObjectIdentity
prtOutput = _PrtOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9)
)
_PrtOutputTable_ObjectIdentity = ObjectIdentity
prtOutputTable = _PrtOutputTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2)
)
_PrtOutputEntry_ObjectIdentity = ObjectIdentity
prtOutputEntry = _PrtOutputEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1)
)


class _Prtoutputtype_Type(Integer32):
    """Custom type prtoutputtype based on Integer32"""
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
        *(("ePother", 1),
          ("ePunknown", 2),
          ("ePremovableBin", 3),
          ("ePunRemovableBin", 4),
          ("ePcontinuousRollDevice", 5),
          ("ePmailBox", 6),
          ("ePcontinousFanFold", 7))
    )


_Prtoutputtype_Type.__name__ = "Integer32"
_Prtoutputtype_Object = MibScalar
prtoutputtype = _Prtoutputtype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 2),
    _Prtoutputtype_Type()
)
prtoutputtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputtype.setStatus("current")


class _Prtoutputcapacityunit_Type(Integer32):
    """Custom type prtoutputcapacityunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              8,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ePtenThousandthsOfInches", 3),
          ("ePmicrometers", 4),
          ("ePsheets", 8),
          ("ePfeet", 16),
          ("ePmeters", 17))
    )


_Prtoutputcapacityunit_Type.__name__ = "Integer32"
_Prtoutputcapacityunit_Object = MibScalar
prtoutputcapacityunit = _Prtoutputcapacityunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 3),
    _Prtoutputcapacityunit_Type()
)
prtoutputcapacityunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputcapacityunit.setStatus("current")
_Prtoutputmaxcapacity_Type = Integer32
_Prtoutputmaxcapacity_Object = MibScalar
prtoutputmaxcapacity = _Prtoutputmaxcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 4),
    _Prtoutputmaxcapacity_Type()
)
prtoutputmaxcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmaxcapacity.setStatus("current")
_Prtoutputremainingcapacity_Type = Integer32
_Prtoutputremainingcapacity_Object = MibScalar
prtoutputremainingcapacity = _Prtoutputremainingcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 5),
    _Prtoutputremainingcapacity_Type()
)
prtoutputremainingcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputremainingcapacity.setStatus("current")
_Prtoutputstatus_Type = Integer32
_Prtoutputstatus_Object = MibScalar
prtoutputstatus = _Prtoutputstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 6),
    _Prtoutputstatus_Type()
)
prtoutputstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputstatus.setStatus("current")


class _Prtoutputname_Type(OctetString):
    """Custom type prtoutputname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Prtoutputname_Type.__name__ = "OctetString"
_Prtoutputname_Object = MibScalar
prtoutputname = _Prtoutputname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 7),
    _Prtoutputname_Type()
)
prtoutputname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputname.setStatus("current")


class _Prtoutputvendorname_Type(OctetString):
    """Custom type prtoutputvendorname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputvendorname_Type.__name__ = "OctetString"
_Prtoutputvendorname_Object = MibScalar
prtoutputvendorname = _Prtoutputvendorname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 8),
    _Prtoutputvendorname_Type()
)
prtoutputvendorname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputvendorname.setStatus("current")


class _Prtoutputmodel_Type(OctetString):
    """Custom type prtoutputmodel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputmodel_Type.__name__ = "OctetString"
_Prtoutputmodel_Object = MibScalar
prtoutputmodel = _Prtoutputmodel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 9),
    _Prtoutputmodel_Type()
)
prtoutputmodel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmodel.setStatus("current")


class _Prtoutputversion_Type(OctetString):
    """Custom type prtoutputversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputversion_Type.__name__ = "OctetString"
_Prtoutputversion_Object = MibScalar
prtoutputversion = _Prtoutputversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 10),
    _Prtoutputversion_Type()
)
prtoutputversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputversion.setStatus("current")


class _Prtoutputserialnumber_Type(OctetString):
    """Custom type prtoutputserialnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtoutputserialnumber_Type.__name__ = "OctetString"
_Prtoutputserialnumber_Object = MibScalar
prtoutputserialnumber = _Prtoutputserialnumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 11),
    _Prtoutputserialnumber_Type()
)
prtoutputserialnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputserialnumber.setStatus("current")


class _Prtoutputdescription_Type(OctetString):
    """Custom type prtoutputdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtoutputdescription_Type.__name__ = "OctetString"
_Prtoutputdescription_Object = MibScalar
prtoutputdescription = _Prtoutputdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 12),
    _Prtoutputdescription_Type()
)
prtoutputdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputdescription.setStatus("current")


class _Prtoutputsecurity_Type(Integer32):
    """Custom type prtoutputsecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePon", 3),
          ("ePoff", 4),
          ("ePnotPresent", 5))
    )


_Prtoutputsecurity_Type.__name__ = "Integer32"
_Prtoutputsecurity_Object = MibScalar
prtoutputsecurity = _Prtoutputsecurity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 13),
    _Prtoutputsecurity_Type()
)
prtoutputsecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputsecurity.setStatus("current")


class _Prtoutputdimunit_Type(Integer32):
    """Custom type prtoutputdimunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePtenThousandthsOfInches", 3),
          ("ePmicrometers", 4))
    )


_Prtoutputdimunit_Type.__name__ = "Integer32"
_Prtoutputdimunit_Object = MibScalar
prtoutputdimunit = _Prtoutputdimunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 14),
    _Prtoutputdimunit_Type()
)
prtoutputdimunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputdimunit.setStatus("current")
_Prtoutputmaxdimfeeddir_Type = Integer32
_Prtoutputmaxdimfeeddir_Object = MibScalar
prtoutputmaxdimfeeddir = _Prtoutputmaxdimfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 15),
    _Prtoutputmaxdimfeeddir_Type()
)
prtoutputmaxdimfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmaxdimfeeddir.setStatus("current")
_Prtoutputmaxdimxfeeddir_Type = Integer32
_Prtoutputmaxdimxfeeddir_Object = MibScalar
prtoutputmaxdimxfeeddir = _Prtoutputmaxdimxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 16),
    _Prtoutputmaxdimxfeeddir_Type()
)
prtoutputmaxdimxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmaxdimxfeeddir.setStatus("current")
_Prtoutputmindimfeeddir_Type = Integer32
_Prtoutputmindimfeeddir_Object = MibScalar
prtoutputmindimfeeddir = _Prtoutputmindimfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 17),
    _Prtoutputmindimfeeddir_Type()
)
prtoutputmindimfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmindimfeeddir.setStatus("current")
_Prtoutputmindimxfeeddir_Type = Integer32
_Prtoutputmindimxfeeddir_Object = MibScalar
prtoutputmindimxfeeddir = _Prtoutputmindimxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 18),
    _Prtoutputmindimxfeeddir_Type()
)
prtoutputmindimxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputmindimxfeeddir.setStatus("current")


class _Prtoutputstackingorder_Type(Integer32):
    """Custom type prtoutputstackingorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePunknown", 2),
          ("ePfirstToLast", 3),
          ("ePlastToFirst", 4))
    )


_Prtoutputstackingorder_Type.__name__ = "Integer32"
_Prtoutputstackingorder_Object = MibScalar
prtoutputstackingorder = _Prtoutputstackingorder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 19),
    _Prtoutputstackingorder_Type()
)
prtoutputstackingorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputstackingorder.setStatus("current")


class _Prtoutputpagedeliveryorientation_Type(Integer32):
    """Custom type prtoutputpagedeliveryorientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePfaceUp", 3),
          ("ePfaceDown", 4))
    )


_Prtoutputpagedeliveryorientation_Type.__name__ = "Integer32"
_Prtoutputpagedeliveryorientation_Object = MibScalar
prtoutputpagedeliveryorientation = _Prtoutputpagedeliveryorientation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 20),
    _Prtoutputpagedeliveryorientation_Type()
)
prtoutputpagedeliveryorientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputpagedeliveryorientation.setStatus("current")


class _Prtoutputbursting_Type(Integer32):
    """Custom type prtoutputbursting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePon", 3),
          ("ePoff", 4),
          ("ePnotPresent", 5))
    )


_Prtoutputbursting_Type.__name__ = "Integer32"
_Prtoutputbursting_Object = MibScalar
prtoutputbursting = _Prtoutputbursting_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 21),
    _Prtoutputbursting_Type()
)
prtoutputbursting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputbursting.setStatus("current")


class _Prtoutputdecollating_Type(Integer32):
    """Custom type prtoutputdecollating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePon", 3),
          ("ePoff", 4),
          ("ePnotPresent", 5))
    )


_Prtoutputdecollating_Type.__name__ = "Integer32"
_Prtoutputdecollating_Object = MibScalar
prtoutputdecollating = _Prtoutputdecollating_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 22),
    _Prtoutputdecollating_Type()
)
prtoutputdecollating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputdecollating.setStatus("current")


class _Prtoutputpagecollated_Type(Integer32):
    """Custom type prtoutputpagecollated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePon", 3),
          ("ePoff", 4),
          ("ePnotPresent", 5))
    )


_Prtoutputpagecollated_Type.__name__ = "Integer32"
_Prtoutputpagecollated_Object = MibScalar
prtoutputpagecollated = _Prtoutputpagecollated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 23),
    _Prtoutputpagecollated_Type()
)
prtoutputpagecollated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputpagecollated.setStatus("current")


class _Prtoutputoffsetstacking_Type(Integer32):
    """Custom type prtoutputoffsetstacking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePon", 3),
          ("ePoff", 4),
          ("ePnotPresent", 5))
    )


_Prtoutputoffsetstacking_Type.__name__ = "Integer32"
_Prtoutputoffsetstacking_Object = MibScalar
prtoutputoffsetstacking = _Prtoutputoffsetstacking_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 9, 2, 1, 24),
    _Prtoutputoffsetstacking_Type()
)
prtoutputoffsetstacking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtoutputoffsetstacking.setStatus("current")
_PrtMarker_ObjectIdentity = ObjectIdentity
prtMarker = _PrtMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10)
)
_PrtMarkerTable_ObjectIdentity = ObjectIdentity
prtMarkerTable = _PrtMarkerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2)
)
_PrtMarkerEntry_ObjectIdentity = ObjectIdentity
prtMarkerEntry = _PrtMarkerEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1)
)


class _Prtmarkermarktech_Type(Integer32):
    """Custom type prtmarkermarktech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("ePelectrophotographicLaser", 4)
    )


_Prtmarkermarktech_Type.__name__ = "Integer32"
_Prtmarkermarktech_Object = MibScalar
prtmarkermarktech = _Prtmarkermarktech_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 2),
    _Prtmarkermarktech_Type()
)
prtmarkermarktech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkermarktech.setStatus("current")


class _Prtmarkercounterunit_Type(Integer32):
    """Custom type prtmarkercounterunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("ePimpressions", 7)
    )


_Prtmarkercounterunit_Type.__name__ = "Integer32"
_Prtmarkercounterunit_Object = MibScalar
prtmarkercounterunit = _Prtmarkercounterunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 3),
    _Prtmarkercounterunit_Type()
)
prtmarkercounterunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercounterunit.setStatus("current")
_Prtmarkerlifecount_Type = Integer32
_Prtmarkerlifecount_Object = MibScalar
prtmarkerlifecount = _Prtmarkerlifecount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 4),
    _Prtmarkerlifecount_Type()
)
prtmarkerlifecount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerlifecount.setStatus("current")
_Prtmarkerpoweroncount_Type = Integer32
_Prtmarkerpoweroncount_Object = MibScalar
prtmarkerpoweroncount = _Prtmarkerpoweroncount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 5),
    _Prtmarkerpoweroncount_Type()
)
prtmarkerpoweroncount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerpoweroncount.setStatus("current")


class _Prtmarkerprocesscolorants_Type(Integer32):
    """Custom type prtmarkerprocesscolorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkerprocesscolorants_Type.__name__ = "Integer32"
_Prtmarkerprocesscolorants_Object = MibScalar
prtmarkerprocesscolorants = _Prtmarkerprocesscolorants_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 6),
    _Prtmarkerprocesscolorants_Type()
)
prtmarkerprocesscolorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerprocesscolorants.setStatus("current")


class _Prtmarkerspotcolorants_Type(Integer32):
    """Custom type prtmarkerspotcolorants based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkerspotcolorants_Type.__name__ = "Integer32"
_Prtmarkerspotcolorants_Object = MibScalar
prtmarkerspotcolorants = _Prtmarkerspotcolorants_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 7),
    _Prtmarkerspotcolorants_Type()
)
prtmarkerspotcolorants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerspotcolorants.setStatus("current")


class _Prtmarkeraddressabilityunit_Type(Integer32):
    """Custom type prtmarkeraddressabilityunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("ePtenThousandthsOfInches", 3)
    )


_Prtmarkeraddressabilityunit_Type.__name__ = "Integer32"
_Prtmarkeraddressabilityunit_Object = MibScalar
prtmarkeraddressabilityunit = _Prtmarkeraddressabilityunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 8),
    _Prtmarkeraddressabilityunit_Type()
)
prtmarkeraddressabilityunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkeraddressabilityunit.setStatus("current")
_Prtmarkeraddressabilityfeeddir_Type = Integer32
_Prtmarkeraddressabilityfeeddir_Object = MibScalar
prtmarkeraddressabilityfeeddir = _Prtmarkeraddressabilityfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 9),
    _Prtmarkeraddressabilityfeeddir_Type()
)
prtmarkeraddressabilityfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkeraddressabilityfeeddir.setStatus("current")
_Prtmarkeraddressabilityxfeeddir_Type = Integer32
_Prtmarkeraddressabilityxfeeddir_Object = MibScalar
prtmarkeraddressabilityxfeeddir = _Prtmarkeraddressabilityxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 10),
    _Prtmarkeraddressabilityxfeeddir_Type()
)
prtmarkeraddressabilityxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkeraddressabilityxfeeddir.setStatus("current")
_Prtmarkernorthmargin_Type = Integer32
_Prtmarkernorthmargin_Object = MibScalar
prtmarkernorthmargin = _Prtmarkernorthmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 11),
    _Prtmarkernorthmargin_Type()
)
prtmarkernorthmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkernorthmargin.setStatus("current")
_Prtmarkersouthmargin_Type = Integer32
_Prtmarkersouthmargin_Object = MibScalar
prtmarkersouthmargin = _Prtmarkersouthmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 12),
    _Prtmarkersouthmargin_Type()
)
prtmarkersouthmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersouthmargin.setStatus("current")
_Prtmarkerwestmargin_Type = Integer32
_Prtmarkerwestmargin_Object = MibScalar
prtmarkerwestmargin = _Prtmarkerwestmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 13),
    _Prtmarkerwestmargin_Type()
)
prtmarkerwestmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerwestmargin.setStatus("current")
_Prtmarkereastmargin_Type = Integer32
_Prtmarkereastmargin_Object = MibScalar
prtmarkereastmargin = _Prtmarkereastmargin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 14),
    _Prtmarkereastmargin_Type()
)
prtmarkereastmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkereastmargin.setStatus("current")
_Prtmarkerstatus_Type = Integer32
_Prtmarkerstatus_Object = MibScalar
prtmarkerstatus = _Prtmarkerstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 10, 2, 1, 15),
    _Prtmarkerstatus_Type()
)
prtmarkerstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkerstatus.setStatus("current")
_PrtMarkerSupplies_ObjectIdentity = ObjectIdentity
prtMarkerSupplies = _PrtMarkerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11)
)
_PrtMarkerSuppliesTable_ObjectIdentity = ObjectIdentity
prtMarkerSuppliesTable = _PrtMarkerSuppliesTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1)
)
_PrtMarkerSuppliesEntry_ObjectIdentity = ObjectIdentity
prtMarkerSuppliesEntry = _PrtMarkerSuppliesEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1)
)


class _Prtmarkersuppliesmarkerindex_Type(Integer32):
    """Custom type prtmarkersuppliesmarkerindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkersuppliesmarkerindex_Type.__name__ = "Integer32"
_Prtmarkersuppliesmarkerindex_Object = MibScalar
prtmarkersuppliesmarkerindex = _Prtmarkersuppliesmarkerindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 2),
    _Prtmarkersuppliesmarkerindex_Type()
)
prtmarkersuppliesmarkerindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesmarkerindex.setStatus("current")


class _Prtmarkersuppliescolorantindex_Type(Integer32):
    """Custom type prtmarkersuppliescolorantindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkersuppliescolorantindex_Type.__name__ = "Integer32"
_Prtmarkersuppliescolorantindex_Object = MibScalar
prtmarkersuppliescolorantindex = _Prtmarkersuppliescolorantindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 3),
    _Prtmarkersuppliescolorantindex_Type()
)
prtmarkersuppliescolorantindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliescolorantindex.setStatus("current")


class _Prtmarkersuppliesclass_Type(Integer32):
    """Custom type prtmarkersuppliesclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("ePsupplyThatIsConsumed", 3)
    )


_Prtmarkersuppliesclass_Type.__name__ = "Integer32"
_Prtmarkersuppliesclass_Object = MibScalar
prtmarkersuppliesclass = _Prtmarkersuppliesclass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 4),
    _Prtmarkersuppliesclass_Type()
)
prtmarkersuppliesclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesclass.setStatus("current")


class _Prtmarkersuppliestype_Type(Integer32):
    """Custom type prtmarkersuppliestype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("ePtoner", 3)
    )


_Prtmarkersuppliestype_Type.__name__ = "Integer32"
_Prtmarkersuppliestype_Object = MibScalar
prtmarkersuppliestype = _Prtmarkersuppliestype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 5),
    _Prtmarkersuppliestype_Type()
)
prtmarkersuppliestype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliestype.setStatus("current")


class _Prtmarkersuppliesdescription_Type(OctetString):
    """Custom type prtmarkersuppliesdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtmarkersuppliesdescription_Type.__name__ = "OctetString"
_Prtmarkersuppliesdescription_Object = MibScalar
prtmarkersuppliesdescription = _Prtmarkersuppliesdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 6),
    _Prtmarkersuppliesdescription_Type()
)
prtmarkersuppliesdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesdescription.setStatus("current")


class _Prtmarkersuppliessupplyunit_Type(Integer32):
    """Custom type prtmarkersuppliessupplyunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            13
        )
    )
    namedValues = NamedValues(
        ("ePtenthsOfGrams", 13)
    )


_Prtmarkersuppliessupplyunit_Type.__name__ = "Integer32"
_Prtmarkersuppliessupplyunit_Object = MibScalar
prtmarkersuppliessupplyunit = _Prtmarkersuppliessupplyunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 7),
    _Prtmarkersuppliessupplyunit_Type()
)
prtmarkersuppliessupplyunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliessupplyunit.setStatus("current")
_Prtmarkersuppliesmaxcapacity_Type = Integer32
_Prtmarkersuppliesmaxcapacity_Object = MibScalar
prtmarkersuppliesmaxcapacity = _Prtmarkersuppliesmaxcapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 8),
    _Prtmarkersuppliesmaxcapacity_Type()
)
prtmarkersuppliesmaxcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersuppliesmaxcapacity.setStatus("current")
_Prtmarkersupplieslevel_Type = Integer32
_Prtmarkersupplieslevel_Object = MibScalar
prtmarkersupplieslevel = _Prtmarkersupplieslevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 11, 1, 1, 9),
    _Prtmarkersupplieslevel_Type()
)
prtmarkersupplieslevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkersupplieslevel.setStatus("current")
_PrtMarkerColorant_ObjectIdentity = ObjectIdentity
prtMarkerColorant = _PrtMarkerColorant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12)
)
_PrtMarkerColorantTable_ObjectIdentity = ObjectIdentity
prtMarkerColorantTable = _PrtMarkerColorantTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1)
)
_PrtMarkerColorantEntry_ObjectIdentity = ObjectIdentity
prtMarkerColorantEntry = _PrtMarkerColorantEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1)
)


class _Prtmarkercolorantmarkerindex_Type(Integer32):
    """Custom type prtmarkercolorantmarkerindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Prtmarkercolorantmarkerindex_Type.__name__ = "Integer32"
_Prtmarkercolorantmarkerindex_Object = MibScalar
prtmarkercolorantmarkerindex = _Prtmarkercolorantmarkerindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 2),
    _Prtmarkercolorantmarkerindex_Type()
)
prtmarkercolorantmarkerindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercolorantmarkerindex.setStatus("current")


class _Prtmarkercolorantrole_Type(Integer32):
    """Custom type prtmarkercolorantrole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePprocess", 3),
          ("ePspot", 4))
    )


_Prtmarkercolorantrole_Type.__name__ = "Integer32"
_Prtmarkercolorantrole_Object = MibScalar
prtmarkercolorantrole = _Prtmarkercolorantrole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 3),
    _Prtmarkercolorantrole_Type()
)
prtmarkercolorantrole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercolorantrole.setStatus("current")


class _Prtmarkercolorantvalue_Type(OctetString):
    """Custom type prtmarkercolorantvalue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtmarkercolorantvalue_Type.__name__ = "OctetString"
_Prtmarkercolorantvalue_Object = MibScalar
prtmarkercolorantvalue = _Prtmarkercolorantvalue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 4),
    _Prtmarkercolorantvalue_Type()
)
prtmarkercolorantvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercolorantvalue.setStatus("current")
_Prtmarkercoloranttonality_Type = Integer32
_Prtmarkercoloranttonality_Object = MibScalar
prtmarkercoloranttonality = _Prtmarkercoloranttonality_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 12, 1, 1, 5),
    _Prtmarkercoloranttonality_Type()
)
prtmarkercoloranttonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmarkercoloranttonality.setStatus("current")
_PrtMediaPath_ObjectIdentity = ObjectIdentity
prtMediaPath = _PrtMediaPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13)
)
_PrtMediaPathTable_ObjectIdentity = ObjectIdentity
prtMediaPathTable = _PrtMediaPathTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4)
)
_PrtMediaPathEntry_ObjectIdentity = ObjectIdentity
prtMediaPathEntry = _PrtMediaPathEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1)
)


class _Prtmediapathmaxspeedprintunit_Type(Integer32):
    """Custom type prtmediapathmaxspeedprintunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("ePimpressionsPerHour", 7)
    )


_Prtmediapathmaxspeedprintunit_Type.__name__ = "Integer32"
_Prtmediapathmaxspeedprintunit_Object = MibScalar
prtmediapathmaxspeedprintunit = _Prtmediapathmaxspeedprintunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 2),
    _Prtmediapathmaxspeedprintunit_Type()
)
prtmediapathmaxspeedprintunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxspeedprintunit.setStatus("current")


class _Prtmediapathmediasizeunit_Type(Integer32):
    """Custom type prtmediapathmediasizeunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePtenThousandthsOfInches", 3),
          ("ePmicrometers", 4))
    )


_Prtmediapathmediasizeunit_Type.__name__ = "Integer32"
_Prtmediapathmediasizeunit_Object = MibScalar
prtmediapathmediasizeunit = _Prtmediapathmediasizeunit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 3),
    _Prtmediapathmediasizeunit_Type()
)
prtmediapathmediasizeunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmediasizeunit.setStatus("current")
_Prtmediapathmaxspeed_Type = Integer32
_Prtmediapathmaxspeed_Object = MibScalar
prtmediapathmaxspeed = _Prtmediapathmaxspeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 4),
    _Prtmediapathmaxspeed_Type()
)
prtmediapathmaxspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxspeed.setStatus("current")
_Prtmediapathmaxmediafeeddir_Type = Integer32
_Prtmediapathmaxmediafeeddir_Object = MibScalar
prtmediapathmaxmediafeeddir = _Prtmediapathmaxmediafeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 5),
    _Prtmediapathmaxmediafeeddir_Type()
)
prtmediapathmaxmediafeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxmediafeeddir.setStatus("current")
_Prtmediapathmaxmediaxfeeddir_Type = Integer32
_Prtmediapathmaxmediaxfeeddir_Object = MibScalar
prtmediapathmaxmediaxfeeddir = _Prtmediapathmaxmediaxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 6),
    _Prtmediapathmaxmediaxfeeddir_Type()
)
prtmediapathmaxmediaxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathmaxmediaxfeeddir.setStatus("current")
_Prtmediapathminmediafeeddir_Type = Integer32
_Prtmediapathminmediafeeddir_Object = MibScalar
prtmediapathminmediafeeddir = _Prtmediapathminmediafeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 7),
    _Prtmediapathminmediafeeddir_Type()
)
prtmediapathminmediafeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathminmediafeeddir.setStatus("current")
_Prtmediapathminmediaxfeeddir_Type = Integer32
_Prtmediapathminmediaxfeeddir_Object = MibScalar
prtmediapathminmediaxfeeddir = _Prtmediapathminmediaxfeeddir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 8),
    _Prtmediapathminmediaxfeeddir_Type()
)
prtmediapathminmediaxfeeddir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathminmediaxfeeddir.setStatus("current")


class _Prtmediapathtype_Type(Integer32):
    """Custom type prtmediapathtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePlongEdgeBindingDuplex", 3),
          ("ePshortEdgeBindingDuplex", 4),
          ("ePsimplex", 5))
    )


_Prtmediapathtype_Type.__name__ = "Integer32"
_Prtmediapathtype_Object = MibScalar
prtmediapathtype = _Prtmediapathtype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 9),
    _Prtmediapathtype_Type()
)
prtmediapathtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathtype.setStatus("current")


class _Prtmediapathdescription_Type(OctetString):
    """Custom type prtmediapathdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtmediapathdescription_Type.__name__ = "OctetString"
_Prtmediapathdescription_Object = MibScalar
prtmediapathdescription = _Prtmediapathdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 10),
    _Prtmediapathdescription_Type()
)
prtmediapathdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathdescription.setStatus("current")
_Prtmediapathstatus_Type = Integer32
_Prtmediapathstatus_Object = MibScalar
prtmediapathstatus = _Prtmediapathstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 13, 4, 1, 11),
    _Prtmediapathstatus_Type()
)
prtmediapathstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtmediapathstatus.setStatus("current")
_PrtChannel_ObjectIdentity = ObjectIdentity
prtChannel = _PrtChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14)
)
_PrtChannelTable_ObjectIdentity = ObjectIdentity
prtChannelTable = _PrtChannelTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1)
)
_PrtChannelEntry_ObjectIdentity = ObjectIdentity
prtChannelEntry = _PrtChannelEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1)
)


class _Prtchanneltype_Type(Integer32):
    """Custom type prtchanneltype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7,
              9,
              10,
              15,
              38)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePchSerialPort", 3),
          ("ePchIEEE1284Port", 5),
          ("ePchAppleTalkPAP", 7),
          ("ePchNetwareRPrinter", 9),
          ("ePchNetwarePServer", 10),
          ("ePchDLCLLCPort", 15),
          ("ePchBidirPortTCP", 38))
    )


_Prtchanneltype_Type.__name__ = "Integer32"
_Prtchanneltype_Object = MibScalar
prtchanneltype = _Prtchanneltype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 2),
    _Prtchanneltype_Type()
)
prtchanneltype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchanneltype.setStatus("current")


class _Prtchannelprotocolversion_Type(OctetString):
    """Custom type prtchannelprotocolversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Prtchannelprotocolversion_Type.__name__ = "OctetString"
_Prtchannelprotocolversion_Object = MibScalar
prtchannelprotocolversion = _Prtchannelprotocolversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 3),
    _Prtchannelprotocolversion_Type()
)
prtchannelprotocolversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelprotocolversion.setStatus("current")
_Prtchannelcurrentjobcntllangindex_Type = Integer32
_Prtchannelcurrentjobcntllangindex_Object = MibScalar
prtchannelcurrentjobcntllangindex = _Prtchannelcurrentjobcntllangindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 4),
    _Prtchannelcurrentjobcntllangindex_Type()
)
prtchannelcurrentjobcntllangindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelcurrentjobcntllangindex.setStatus("current")
_Prtchanneldefaultpagedesclangindex_Type = Integer32
_Prtchanneldefaultpagedesclangindex_Object = MibScalar
prtchanneldefaultpagedesclangindex = _Prtchanneldefaultpagedesclangindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 5),
    _Prtchanneldefaultpagedesclangindex_Type()
)
prtchanneldefaultpagedesclangindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtchanneldefaultpagedesclangindex.setStatus("current")


class _Prtchannelstate_Type(Integer32):
    """Custom type prtchannelstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePprintDataAccepted", 3),
          ("ePnoDataAccepted", 4))
    )


_Prtchannelstate_Type.__name__ = "Integer32"
_Prtchannelstate_Object = MibScalar
prtchannelstate = _Prtchannelstate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 6),
    _Prtchannelstate_Type()
)
prtchannelstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelstate.setStatus("current")
_Prtchannelifindex_Type = Integer32
_Prtchannelifindex_Object = MibScalar
prtchannelifindex = _Prtchannelifindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 7),
    _Prtchannelifindex_Type()
)
prtchannelifindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelifindex.setStatus("current")
_Prtchannelstatus_Type = Integer32
_Prtchannelstatus_Object = MibScalar
prtchannelstatus = _Prtchannelstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 8),
    _Prtchannelstatus_Type()
)
prtchannelstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelstatus.setStatus("current")


class _Prtchannelinformation_Type(OctetString):
    """Custom type prtchannelinformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtchannelinformation_Type.__name__ = "OctetString"
_Prtchannelinformation_Object = MibScalar
prtchannelinformation = _Prtchannelinformation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 14, 1, 1, 9),
    _Prtchannelinformation_Type()
)
prtchannelinformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtchannelinformation.setStatus("current")
_PrtInterpreter_ObjectIdentity = ObjectIdentity
prtInterpreter = _PrtInterpreter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15)
)
_PrtInterpreterTable_ObjectIdentity = ObjectIdentity
prtInterpreterTable = _PrtInterpreterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1)
)
_PrtInterpreterEntry_ObjectIdentity = ObjectIdentity
prtInterpreterEntry = _PrtInterpreterEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1)
)


class _Prtinterpreterlangfamily_Type(Integer32):
    """Custom type prtinterpreterlangfamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              37,
              47)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePlangPCL", 3),
          ("ePlangPJL", 5),
          ("ePlangPS", 6),
          ("ePlangAutomatic", 37),
          ("ePlangPCLXL", 47))
    )


_Prtinterpreterlangfamily_Type.__name__ = "Integer32"
_Prtinterpreterlangfamily_Object = MibScalar
prtinterpreterlangfamily = _Prtinterpreterlangfamily_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 2),
    _Prtinterpreterlangfamily_Type()
)
prtinterpreterlangfamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterlangfamily.setStatus("current")


class _Prtinterpreterlanglevel_Type(OctetString):
    """Custom type prtinterpreterlanglevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Prtinterpreterlanglevel_Type.__name__ = "OctetString"
_Prtinterpreterlanglevel_Object = MibScalar
prtinterpreterlanglevel = _Prtinterpreterlanglevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 3),
    _Prtinterpreterlanglevel_Type()
)
prtinterpreterlanglevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterlanglevel.setStatus("current")


class _Prtinterpreterlangversion_Type(OctetString):
    """Custom type prtinterpreterlangversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Prtinterpreterlangversion_Type.__name__ = "OctetString"
_Prtinterpreterlangversion_Object = MibScalar
prtinterpreterlangversion = _Prtinterpreterlangversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 4),
    _Prtinterpreterlangversion_Type()
)
prtinterpreterlangversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterlangversion.setStatus("current")


class _Prtinterpreterdescription_Type(OctetString):
    """Custom type prtinterpreterdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtinterpreterdescription_Type.__name__ = "OctetString"
_Prtinterpreterdescription_Object = MibScalar
prtinterpreterdescription = _Prtinterpreterdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 5),
    _Prtinterpreterdescription_Type()
)
prtinterpreterdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterdescription.setStatus("current")


class _Prtinterpreterversion_Type(OctetString):
    """Custom type prtinterpreterversion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Prtinterpreterversion_Type.__name__ = "OctetString"
_Prtinterpreterversion_Object = MibScalar
prtinterpreterversion = _Prtinterpreterversion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 6),
    _Prtinterpreterversion_Type()
)
prtinterpreterversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterversion.setStatus("current")


class _Prtinterpreterdefaultorientation_Type(Integer32):
    """Custom type prtinterpreterdefaultorientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePportrait", 3),
          ("ePlandscape", 4))
    )


_Prtinterpreterdefaultorientation_Type.__name__ = "Integer32"
_Prtinterpreterdefaultorientation_Object = MibScalar
prtinterpreterdefaultorientation = _Prtinterpreterdefaultorientation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 7),
    _Prtinterpreterdefaultorientation_Type()
)
prtinterpreterdefaultorientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinterpreterdefaultorientation.setStatus("current")
_Prtinterpreterfeedaddressability_Type = Integer32
_Prtinterpreterfeedaddressability_Object = MibScalar
prtinterpreterfeedaddressability = _Prtinterpreterfeedaddressability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 8),
    _Prtinterpreterfeedaddressability_Type()
)
prtinterpreterfeedaddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterfeedaddressability.setStatus("current")
_Prtinterpreterxfeedaddressability_Type = Integer32
_Prtinterpreterxfeedaddressability_Object = MibScalar
prtinterpreterxfeedaddressability = _Prtinterpreterxfeedaddressability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 9),
    _Prtinterpreterxfeedaddressability_Type()
)
prtinterpreterxfeedaddressability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterxfeedaddressability.setStatus("current")


class _Prtinterpreterdefaultcharsetin_Type(Integer32):
    """Custom type prtinterpreterdefaultcharsetin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              12,
              13,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              1004,
              2000,
              2001,
              2002,
              2003,
              2004,
              2005,
              2009,
              2010,
              2011,
              2012,
              2014,
              2017,
              2021,
              2027,
              2087,
              2257)
        )
    )
    namedValues = NamedValues(
        *(("ePcsASCII", 3),
          ("ePcsISOLatin1", 4),
          ("ePcsISOLatin2", 5),
          ("ePcsISOLatin5", 12),
          ("ePcsISOLatin6", 13),
          ("ePcsISO4UnitedKingdom", 20),
          ("ePcsISO11SwedishforNames", 21),
          ("ePcsISO15Italian", 22),
          ("ePcsISO17Spanish", 23),
          ("ePcsISO21German", 24),
          ("ePcsISO60DanishNorwegian", 25),
          ("ePcsISO69French", 26),
          ("ePcsUnicodeIBM2039", 1004),
          ("ePcsWindows30Latin1", 2000),
          ("ePcsWindows31Latin1", 2001),
          ("ePcsWindows31Latin2", 2002),
          ("ePcsWindows31Latin5", 2003),
          ("ePcsHPRoman8", 2004),
          ("ePcsAdobeStandardEncoding", 2005),
          ("ePcsPC850Multilingual", 2009),
          ("ePcsPCp852", 2010),
          ("ePcsPC8CodePage437", 2011),
          ("ePcsPC8DNDanishNorwegian", 2012),
          ("ePcsHPPC8Turkish", 2014),
          ("ePcsHPLegal", 2017),
          ("ePcsHPDeskTop", 2021),
          ("ePcsMacintosh", 2027),
          ("ePcsPC775Baltic", 2087),
          ("ePcsWindows1257Baltic", 2257))
    )


_Prtinterpreterdefaultcharsetin_Type.__name__ = "Integer32"
_Prtinterpreterdefaultcharsetin_Object = MibScalar
prtinterpreterdefaultcharsetin = _Prtinterpreterdefaultcharsetin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 10),
    _Prtinterpreterdefaultcharsetin_Type()
)
prtinterpreterdefaultcharsetin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtinterpreterdefaultcharsetin.setStatus("current")


class _Prtinterpreterdefaultcharsetout_Type(Integer32):
    """Custom type prtinterpreterdefaultcharsetout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              2004,
              2005)
        )
    )
    namedValues = NamedValues(
        *(("ePcsNoDefault", 2),
          ("ePcsASCII", 3),
          ("ePcsHPRoman8", 2004),
          ("ePcsAdobeStandardEncoding", 2005))
    )


_Prtinterpreterdefaultcharsetout_Type.__name__ = "Integer32"
_Prtinterpreterdefaultcharsetout_Object = MibScalar
prtinterpreterdefaultcharsetout = _Prtinterpreterdefaultcharsetout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 11),
    _Prtinterpreterdefaultcharsetout_Type()
)
prtinterpreterdefaultcharsetout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpreterdefaultcharsetout.setStatus("current")


class _Prtinterpretertwoway_Type(Integer32):
    """Custom type prtinterpretertwoway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ePyes", 3),
          ("ePno", 4))
    )


_Prtinterpretertwoway_Type.__name__ = "Integer32"
_Prtinterpretertwoway_Object = MibScalar
prtinterpretertwoway = _Prtinterpretertwoway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 15, 1, 1, 12),
    _Prtinterpretertwoway_Type()
)
prtinterpretertwoway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtinterpretertwoway.setStatus("current")
_PrtConsoleDisplayBuffer_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBuffer = _PrtConsoleDisplayBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16)
)
_PrtConsoleDisplayBufferTable_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBufferTable = _PrtConsoleDisplayBufferTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16, 5)
)
_PrtConsoleDisplayBufferEntry_ObjectIdentity = ObjectIdentity
prtConsoleDisplayBufferEntry = _PrtConsoleDisplayBufferEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16, 5, 1)
)


class _Prtconsoledisplaybuffertext_Type(OctetString):
    """Custom type prtconsoledisplaybuffertext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtconsoledisplaybuffertext_Type.__name__ = "OctetString"
_Prtconsoledisplaybuffertext_Object = MibScalar
prtconsoledisplaybuffertext = _Prtconsoledisplaybuffertext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 16, 5, 1, 2),
    _Prtconsoledisplaybuffertext_Type()
)
prtconsoledisplaybuffertext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoledisplaybuffertext.setStatus("current")
_PrtConsoleLights_ObjectIdentity = ObjectIdentity
prtConsoleLights = _PrtConsoleLights_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17)
)
_PrtConsoleLightTable_ObjectIdentity = ObjectIdentity
prtConsoleLightTable = _PrtConsoleLightTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6)
)
_PrtConsoleLightEntry_ObjectIdentity = ObjectIdentity
prtConsoleLightEntry = _PrtConsoleLightEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1)
)
_Prtconsoleontime_Type = Integer32
_Prtconsoleontime_Object = MibScalar
prtconsoleontime = _Prtconsoleontime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 2),
    _Prtconsoleontime_Type()
)
prtconsoleontime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoleontime.setStatus("current")
_Prtconsoleofftime_Type = Integer32
_Prtconsoleofftime_Object = MibScalar
prtconsoleofftime = _Prtconsoleofftime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 3),
    _Prtconsoleofftime_Type()
)
prtconsoleofftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoleofftime.setStatus("current")


class _Prtconsolecolor_Type(Integer32):
    """Custom type prtconsolecolor based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePunknown", 2),
          ("ePwhite", 3),
          ("ePred", 4),
          ("ePgreen", 5),
          ("ePblue", 6),
          ("ePcyan", 7),
          ("ePmagenta", 8),
          ("ePyellow", 9),
          ("ePorange", 10))
    )


_Prtconsolecolor_Type.__name__ = "Integer32"
_Prtconsolecolor_Object = MibScalar
prtconsolecolor = _Prtconsolecolor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 4),
    _Prtconsolecolor_Type()
)
prtconsolecolor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsolecolor.setStatus("current")


class _Prtconsoledescription_Type(OctetString):
    """Custom type prtconsoledescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtconsoledescription_Type.__name__ = "OctetString"
_Prtconsoledescription_Object = MibScalar
prtconsoledescription = _Prtconsoledescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 17, 6, 1, 5),
    _Prtconsoledescription_Type()
)
prtconsoledescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtconsoledescription.setStatus("current")
_PrtAlert_ObjectIdentity = ObjectIdentity
prtAlert = _PrtAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18)
)
_PrtAlertTable_ObjectIdentity = ObjectIdentity
prtAlertTable = _PrtAlertTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1)
)
_PrtAlertEntry_ObjectIdentity = ObjectIdentity
prtAlertEntry = _PrtAlertEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1)
)


class _Prtalertseveritylevel_Type(Integer32):
    """Custom type prtalertseveritylevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePcriticalBinaryChangeEvent", 3),
          ("ePwarningUnaryChangeEvent", 4),
          ("ePwarningBinaryChangeEvent", 5))
    )


_Prtalertseveritylevel_Type.__name__ = "Integer32"
_Prtalertseveritylevel_Object = MibScalar
prtalertseveritylevel = _Prtalertseveritylevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 2),
    _Prtalertseveritylevel_Type()
)
prtalertseveritylevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertseveritylevel.setStatus("current")


class _Prtalerttraininglevel_Type(Integer32):
    """Custom type prtalerttraininglevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePuntrained", 3),
          ("ePtrained", 4),
          ("ePfieldService", 5),
          ("ePmanagement", 6),
          ("ePnoInterventionRequired", 7))
    )


_Prtalerttraininglevel_Type.__name__ = "Integer32"
_Prtalerttraininglevel_Object = MibScalar
prtalerttraininglevel = _Prtalerttraininglevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 3),
    _Prtalerttraininglevel_Type()
)
prtalerttraininglevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalerttraininglevel.setStatus("current")


class _Prtalertgroup_Type(Integer32):
    """Custom type prtalertgroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              8,
              9,
              10,
              11,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ePgeneralPrinter", 5),
          ("ePcover", 6),
          ("ePinput", 8),
          ("ePoutput", 9),
          ("ePmarker", 10),
          ("ePmarkerSupplies", 11),
          ("ePchannel", 14))
    )


_Prtalertgroup_Type.__name__ = "Integer32"
_Prtalertgroup_Object = MibScalar
prtalertgroup = _Prtalertgroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 4),
    _Prtalertgroup_Type()
)
prtalertgroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertgroup.setStatus("current")
_Prtalertgroupindex_Type = Integer32
_Prtalertgroupindex_Object = MibScalar
prtalertgroupindex = _Prtalertgroupindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 5),
    _Prtalertgroupindex_Type()
)
prtalertgroupindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertgroupindex.setStatus("current")
_Prtalertlocation_Type = Integer32
_Prtalertlocation_Object = MibScalar
prtalertlocation = _Prtalertlocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 6),
    _Prtalertlocation_Type()
)
prtalertlocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertlocation.setStatus("current")


class _Prtalertcode_Type(Integer32):
    """Custom type prtalertcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              8,
              9,
              12,
              13,
              14,
              15,
              22,
              23,
              33,
              34,
              1001,
              1002,
              1101,
              1104)
        )
    )
    namedValues = NamedValues(
        *(("ePother", 1),
          ("ePcoverOpened", 3),
          ("ePjam", 8),
          ("ePsubunitMissing", 9),
          ("ePsubunitAlmostEmpty", 12),
          ("ePsubunitEmpty", 13),
          ("ePsubunitAlmostFull", 14),
          ("ePsubunitFull", 15),
          ("ePsubunitOffline", 22),
          ("ePsubunitPowerSaver", 23),
          ("ePsubunitMotorFailure", 33),
          ("ePsubunitMemoryExhausted", 34),
          ("ePmarkerFuserUnderTemperature", 1001),
          ("ePmarkerFuserOverTemperature", 1002),
          ("ePmarkerTonerEmpty", 1101),
          ("ePmarkerTonerAlmostEmpty", 1104))
    )


_Prtalertcode_Type.__name__ = "Integer32"
_Prtalertcode_Object = MibScalar
prtalertcode = _Prtalertcode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 7),
    _Prtalertcode_Type()
)
prtalertcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertcode.setStatus("current")


class _Prtalertdescription_Type(OctetString):
    """Custom type prtalertdescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Prtalertdescription_Type.__name__ = "OctetString"
_Prtalertdescription_Object = MibScalar
prtalertdescription = _Prtalertdescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 8),
    _Prtalertdescription_Type()
)
prtalertdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalertdescription.setStatus("current")
_Prtalerttime_Type = Integer32
_Prtalerttime_Object = MibScalar
prtalerttime = _Prtalerttime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 2, 18, 1, 1, 9),
    _Prtalerttime_Type()
)
prtalerttime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtalerttime.setStatus("current")
_Hrm_ObjectIdentity = ObjectIdentity
hrm = _Hrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3)
)
_HrStorage_ObjectIdentity = ObjectIdentity
hrStorage = _HrStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2)
)
_Hrmemorysize_Type = Integer32
_Hrmemorysize_Object = MibScalar
hrmemorysize = _Hrmemorysize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 2),
    _Hrmemorysize_Type()
)
hrmemorysize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrmemorysize.setStatus("current")
_HrStorageTable_ObjectIdentity = ObjectIdentity
hrStorageTable = _HrStorageTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3)
)
_HrStorageEntry_ObjectIdentity = ObjectIdentity
hrStorageEntry = _HrStorageEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1)
)


class _Hrstorageindex_Type(Integer32):
    """Custom type hrstorageindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrstorageindex_Type.__name__ = "Integer32"
_Hrstorageindex_Object = MibScalar
hrstorageindex = _Hrstorageindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 1),
    _Hrstorageindex_Type()
)
hrstorageindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageindex.setStatus("current")
_Hrstoragetype_Type = ObjectIdentifier
_Hrstoragetype_Object = MibScalar
hrstoragetype = _Hrstoragetype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 2),
    _Hrstoragetype_Type()
)
hrstoragetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstoragetype.setStatus("current")
_Hrstoragedescr_Type = OctetString
_Hrstoragedescr_Object = MibScalar
hrstoragedescr = _Hrstoragedescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 3),
    _Hrstoragedescr_Type()
)
hrstoragedescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstoragedescr.setStatus("current")


class _Hrstorageallocationunits_Type(Integer32):
    """Custom type hrstorageallocationunits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrstorageallocationunits_Type.__name__ = "Integer32"
_Hrstorageallocationunits_Object = MibScalar
hrstorageallocationunits = _Hrstorageallocationunits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 4),
    _Hrstorageallocationunits_Type()
)
hrstorageallocationunits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageallocationunits.setStatus("current")


class _Hrstoragesize_Type(Integer32):
    """Custom type hrstoragesize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrstoragesize_Type.__name__ = "Integer32"
_Hrstoragesize_Object = MibScalar
hrstoragesize = _Hrstoragesize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 5),
    _Hrstoragesize_Type()
)
hrstoragesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstoragesize.setStatus("current")


class _Hrstorageused_Type(Integer32):
    """Custom type hrstorageused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrstorageused_Type.__name__ = "Integer32"
_Hrstorageused_Object = MibScalar
hrstorageused = _Hrstorageused_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 6),
    _Hrstorageused_Type()
)
hrstorageused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageused.setStatus("current")
_Hrstorageallocationfailures_Type = Integer32
_Hrstorageallocationfailures_Object = MibScalar
hrstorageallocationfailures = _Hrstorageallocationfailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 2, 3, 1, 7),
    _Hrstorageallocationfailures_Type()
)
hrstorageallocationfailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrstorageallocationfailures.setStatus("current")
_HrDevice_ObjectIdentity = ObjectIdentity
hrDevice = _HrDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3)
)
_HrDeviceTable_ObjectIdentity = ObjectIdentity
hrDeviceTable = _HrDeviceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2)
)
_HrDeviceEntry_ObjectIdentity = ObjectIdentity
hrDeviceEntry = _HrDeviceEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1)
)


class _Hrdeviceindex_Type(Integer32):
    """Custom type hrdeviceindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrdeviceindex_Type.__name__ = "Integer32"
_Hrdeviceindex_Object = MibScalar
hrdeviceindex = _Hrdeviceindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 1),
    _Hrdeviceindex_Type()
)
hrdeviceindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdeviceindex.setStatus("current")
_Hrdevicetype_Type = ObjectIdentifier
_Hrdevicetype_Object = MibScalar
hrdevicetype = _Hrdevicetype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 2),
    _Hrdevicetype_Type()
)
hrdevicetype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdevicetype.setStatus("current")


class _Hrdevicedescr_Type(OctetString):
    """Custom type hrdevicedescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hrdevicedescr_Type.__name__ = "OctetString"
_Hrdevicedescr_Object = MibScalar
hrdevicedescr = _Hrdevicedescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 3),
    _Hrdevicedescr_Type()
)
hrdevicedescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdevicedescr.setStatus("current")
_Hrdeviceid_Type = ObjectIdentifier
_Hrdeviceid_Object = MibScalar
hrdeviceid = _Hrdeviceid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 4),
    _Hrdeviceid_Type()
)
hrdeviceid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdeviceid.setStatus("current")


class _Hrdevicestatus_Type(Integer32):
    """Custom type hrdevicestatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eHrunning", 2),
          ("eHwarning", 3),
          ("eHdown", 5))
    )


_Hrdevicestatus_Type.__name__ = "Integer32"
_Hrdevicestatus_Object = MibScalar
hrdevicestatus = _Hrdevicestatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 5),
    _Hrdevicestatus_Type()
)
hrdevicestatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdevicestatus.setStatus("current")
_Hrdeviceerrors_Type = Integer32
_Hrdeviceerrors_Object = MibScalar
hrdeviceerrors = _Hrdeviceerrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 2, 1, 6),
    _Hrdeviceerrors_Type()
)
hrdeviceerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdeviceerrors.setStatus("current")
_HrPrinterTable_ObjectIdentity = ObjectIdentity
hrPrinterTable = _HrPrinterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5)
)
_HrPrinterEntry_ObjectIdentity = ObjectIdentity
hrPrinterEntry = _HrPrinterEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5, 1)
)


class _Hrprinterstatus_Type(Integer32):
    """Custom type hrprinterstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eHother", 1),
          ("eHidle", 3),
          ("eHprinting", 4),
          ("eHwarmup", 5))
    )


_Hrprinterstatus_Type.__name__ = "Integer32"
_Hrprinterstatus_Object = MibScalar
hrprinterstatus = _Hrprinterstatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5, 1, 1),
    _Hrprinterstatus_Type()
)
hrprinterstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrprinterstatus.setStatus("current")
_Hrprinterdetectederrorstate_Type = OctetString
_Hrprinterdetectederrorstate_Object = MibScalar
hrprinterdetectederrorstate = _Hrprinterdetectederrorstate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 5, 1, 2),
    _Hrprinterdetectederrorstate_Type()
)
hrprinterdetectederrorstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrprinterdetectederrorstate.setStatus("current")
_HrDiskStorageTable_ObjectIdentity = ObjectIdentity
hrDiskStorageTable = _HrDiskStorageTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6)
)
_HrDiskStorageEntry_ObjectIdentity = ObjectIdentity
hrDiskStorageEntry = _HrDiskStorageEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1)
)


class _Hrdiskstorageaccess_Type(Integer32):
    """Custom type hrdiskstorageaccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eHreadWrite", 1),
          ("eHreadOnly", 2))
    )


_Hrdiskstorageaccess_Type.__name__ = "Integer32"
_Hrdiskstorageaccess_Object = MibScalar
hrdiskstorageaccess = _Hrdiskstorageaccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 1),
    _Hrdiskstorageaccess_Type()
)
hrdiskstorageaccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrdiskstorageaccess.setStatus("current")


class _Hrdiskstoragemedia_Type(Integer32):
    """Custom type hrdiskstoragemedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eHother", 1),
          ("eHhardDisk", 3),
          ("eHramDisk", 8))
    )


_Hrdiskstoragemedia_Type.__name__ = "Integer32"
_Hrdiskstoragemedia_Object = MibScalar
hrdiskstoragemedia = _Hrdiskstoragemedia_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 2),
    _Hrdiskstoragemedia_Type()
)
hrdiskstoragemedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdiskstoragemedia.setStatus("current")


class _Hrdiskstorageremoveble_Type(Integer32):
    """Custom type hrdiskstorageremoveble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eHfalse", 2)
    )


_Hrdiskstorageremoveble_Type.__name__ = "Integer32"
_Hrdiskstorageremoveble_Object = MibScalar
hrdiskstorageremoveble = _Hrdiskstorageremoveble_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 3),
    _Hrdiskstorageremoveble_Type()
)
hrdiskstorageremoveble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdiskstorageremoveble.setStatus("current")
_Hrdiskstoragecapacity_Type = Integer32
_Hrdiskstoragecapacity_Object = MibScalar
hrdiskstoragecapacity = _Hrdiskstoragecapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 6, 1, 4),
    _Hrdiskstoragecapacity_Type()
)
hrdiskstoragecapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrdiskstoragecapacity.setStatus("current")
_HrPartitionTable_ObjectIdentity = ObjectIdentity
hrPartitionTable = _HrPartitionTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7)
)
_HrPartitionEntry_ObjectIdentity = ObjectIdentity
hrPartitionEntry = _HrPartitionEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1)
)


class _Hrpartitionindex_Type(Integer32):
    """Custom type hrpartitionindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrpartitionindex_Type.__name__ = "Integer32"
_Hrpartitionindex_Object = MibScalar
hrpartitionindex = _Hrpartitionindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 1),
    _Hrpartitionindex_Type()
)
hrpartitionindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionindex.setStatus("current")


class _Hrpartitionlabel_Type(OctetString):
    """Custom type hrpartitionlabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Hrpartitionlabel_Type.__name__ = "OctetString"
_Hrpartitionlabel_Object = MibScalar
hrpartitionlabel = _Hrpartitionlabel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 2),
    _Hrpartitionlabel_Type()
)
hrpartitionlabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrpartitionlabel.setStatus("current")
_Hrpartitionid_Type = OctetString
_Hrpartitionid_Object = MibScalar
hrpartitionid = _Hrpartitionid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 3),
    _Hrpartitionid_Type()
)
hrpartitionid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionid.setStatus("current")
_Hrpartitionsize_Type = Integer32
_Hrpartitionsize_Object = MibScalar
hrpartitionsize = _Hrpartitionsize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 4),
    _Hrpartitionsize_Type()
)
hrpartitionsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionsize.setStatus("current")


class _Hrpartitionfsindex_Type(Integer32):
    """Custom type hrpartitionfsindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrpartitionfsindex_Type.__name__ = "Integer32"
_Hrpartitionfsindex_Object = MibScalar
hrpartitionfsindex = _Hrpartitionfsindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 7, 1, 5),
    _Hrpartitionfsindex_Type()
)
hrpartitionfsindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrpartitionfsindex.setStatus("current")
_HrFSTable_ObjectIdentity = ObjectIdentity
hrFSTable = _HrFSTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8)
)
_HrFSEntry_ObjectIdentity = ObjectIdentity
hrFSEntry = _HrFSEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1)
)


class _Hrfsindex_Type(Integer32):
    """Custom type hrfsindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hrfsindex_Type.__name__ = "Integer32"
_Hrfsindex_Object = MibScalar
hrfsindex = _Hrfsindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 1),
    _Hrfsindex_Type()
)
hrfsindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsindex.setStatus("current")
_Hrfsmountpoint_Type = OctetString
_Hrfsmountpoint_Object = MibScalar
hrfsmountpoint = _Hrfsmountpoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 2),
    _Hrfsmountpoint_Type()
)
hrfsmountpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsmountpoint.setStatus("current")
_Hrfsremotemountpoint_Type = OctetString
_Hrfsremotemountpoint_Object = MibScalar
hrfsremotemountpoint = _Hrfsremotemountpoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 3),
    _Hrfsremotemountpoint_Type()
)
hrfsremotemountpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsremotemountpoint.setStatus("current")
_Hrfstype_Type = ObjectIdentifier
_Hrfstype_Object = MibScalar
hrfstype = _Hrfstype_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 4),
    _Hrfstype_Type()
)
hrfstype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfstype.setStatus("current")


class _Hrfsaccess_Type(Integer32):
    """Custom type hrfsaccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eHreadWrite", 1),
          ("eHreadOnly", 2))
    )


_Hrfsaccess_Type.__name__ = "Integer32"
_Hrfsaccess_Object = MibScalar
hrfsaccess = _Hrfsaccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 5),
    _Hrfsaccess_Type()
)
hrfsaccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hrfsaccess.setStatus("current")


class _Hrfsbootable_Type(Integer32):
    """Custom type hrfsbootable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("eHfalse", 2)
    )


_Hrfsbootable_Type.__name__ = "Integer32"
_Hrfsbootable_Object = MibScalar
hrfsbootable = _Hrfsbootable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 6),
    _Hrfsbootable_Type()
)
hrfsbootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsbootable.setStatus("current")


class _Hrfsstorageindex_Type(Integer32):
    """Custom type hrfsstorageindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hrfsstorageindex_Type.__name__ = "Integer32"
_Hrfsstorageindex_Object = MibScalar
hrfsstorageindex = _Hrfsstorageindex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 7),
    _Hrfsstorageindex_Type()
)
hrfsstorageindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfsstorageindex.setStatus("current")
_Hrfslastfullbackupdate_Type = OctetString
_Hrfslastfullbackupdate_Object = MibScalar
hrfslastfullbackupdate = _Hrfslastfullbackupdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 8),
    _Hrfslastfullbackupdate_Type()
)
hrfslastfullbackupdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfslastfullbackupdate.setStatus("current")
_Hrfslastpartialbackupdate_Type = OctetString
_Hrfslastpartialbackupdate_Object = MibScalar
hrfslastpartialbackupdate = _Hrfslastpartialbackupdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 4, 2, 3, 3, 8, 1, 9),
    _Hrfslastpartialbackupdate_Type()
)
hrfslastpartialbackupdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hrfslastpartialbackupdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-LASERJET-COMMON-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpsystem": hpsystem,
       "net-peripheral": net_peripheral,
       "net-printer": net_printer,
       "generalDeviceStatus": generalDeviceStatus,
       "gdStatusBytes": gdStatusBytes,
       "gdStatusEntry": gdStatusEntry,
       "gdStatusLineState": gdStatusLineState,
       "gdStatusPaperState": gdStatusPaperState,
       "gdStatusInterventionState": gdStatusInterventionState,
       "gdStatusNewMode": gdStatusNewMode,
       "gdStatusConnectionTerminationAck": gdStatusConnectionTerminationAck,
       "gdStatusPeripheralError": gdStatusPeripheralError,
       "gdStatusPaperOut": gdStatusPaperOut,
       "gdStatusPaperJam": gdStatusPaperJam,
       "gdStatusTonerLow": gdStatusTonerLow,
       "gdStatusPagePunt": gdStatusPagePunt,
       "gdStatusMemoryOut": gdStatusMemoryOut,
       "gdStatusIoActive": gdStatusIoActive,
       "gdStatusBusy": gdStatusBusy,
       "gdStatusWait": gdStatusWait,
       "gdStatusInitialize": gdStatusInitialize,
       "gdStatusDoorOpen": gdStatusDoorOpen,
       "gdStatusPrinting": gdStatusPrinting,
       "gdStatusPaperOutput": gdStatusPaperOutput,
       "gdStatusReserved": gdStatusReserved,
       "gdStatusNovBusy": gdStatusNovBusy,
       "gdStatusLlcBusy": gdStatusLlcBusy,
       "gdStatusTcpBusy": gdStatusTcpBusy,
       "gdStatusAtBusy": gdStatusAtBusy,
       "gdStatusDisplay": gdStatusDisplay,
       "gdStatusJobName": gdStatusJobName,
       "gdStatusSource": gdStatusSource,
       "gdStatusPapstatus": gdStatusPapstatus,
       "gdStatusId": gdStatusId,
       "gdStatusDisplayCode": gdStatusDisplayCode,
       "gdStatusNlsCode": gdStatusNlsCode,
       "gdStatusJobTimeout": gdStatusJobTimeout,
       "gdStatusPjlUstatus": gdStatusPjlUstatus,
       "gdStatusLaaSupport": gdStatusLaaSupport,
       "gdPasswords": gdPasswords,
       "gdStatusAtPrinterName": gdStatusAtPrinterName,
       "gdStatusAtPrinterType": gdStatusAtPrinterType,
       "netPrinterType": netPrinterType,
       "netdm": netdm,
       "dm": dm,
       "device": device,
       "device-system": device_system,
       "settings-system": settings_system,
       "energy-star": energy_star,
       "sleep-mode": sleep_mode,
       "control-panel-lock": control_panel_lock,
       "service-password": service_password,
       "device-cfg-download": device_cfg_download,
       "device-cfg-download-data-type": device_cfg_download_data_type,
       "device-cfg-upload": device_cfg_upload,
       "device-cfg-upload-data-type": device_cfg_upload_data_type,
       "download-timeout": download_timeout,
       "upload-timeout": upload_timeout,
       "run-location": run_location,
       "date-display": date_display,
       "device-cfg-param-command": device_cfg_param_command,
       "copier-token": copier_token,
       "fax-upload-token": fax_upload_token,
       "fax-download-token": fax_download_token,
       "device-config-token": device_config_token,
       "mono-color-switching-mode": mono_color_switching_mode,
       "device-configure": device_configure,
       "device-configure-print-engine-speed": device_configure_print_engine_speed,
       "device-configure-duplexer-enabled": device_configure_duplexer_enabled,
       "device-configure-generic-language-prompt": device_configure_generic_language_prompt,
       "device-configure-generic-country-prompt": device_configure_generic_country_prompt,
       "device-configure-generic-country": device_configure_generic_country,
       "device-configure-secure-nvram-items": device_configure_secure_nvram_items,
       "device-configure-cpe-feature": device_configure_cpe_feature,
       "device-configure-custom-product-number": device_configure_custom_product_number,
       "device-configure-preferred-boot-localization-language": device_configure_preferred_boot_localization_language,
       "control-panel-button-press-delay": control_panel_button_press_delay,
       "low-power": low_power,
       "fuser-pressure-release": fuser_pressure_release,
       "control-panel-display-contrast": control_panel_display_contrast,
       "calibration-lowspeed-enable": calibration_lowspeed_enable,
       "start-engine-early-warmup": start_engine_early_warmup,
       "enable-engine-early-warmup": enable_engine_early_warmup,
       "status-system": status_system,
       "localization-language": localization_language,
       "not-ready-printer": not_ready_printer,
       "not-ready-controller": not_ready_controller,
       "not-idle": not_idle,
       "on-off-line": on_off_line,
       "continue": _pysmi_continue,
       "auto-continue": auto_continue,
       "install-date": install_date,
       "user-nvram-reset": user_nvram_reset,
       "date-and-time": date_and_time,
       "display": display,
       "display-status": display_status,
       "display-column-size": display_column_size,
       "display-number-of-rows": display_number_of_rows,
       "show-address": show_address,
       "status-message": status_message,
       "status-message1": status_message1,
       "status-msg-line1-part1": status_msg_line1_part1,
       "total-ram-size": total_ram_size,
       "status-printer": status_printer,
       "status-controller": status_controller,
       "time-display": time_display,
       "job-input-auto-continue-timeout": job_input_auto_continue_timeout,
       "job-input-auto-continue-mode": job_input_auto_continue_mode,
       "background-message": background_message,
       "background-message1": background_message1,
       "background-status-msg-line1-part1": background_status_msg_line1_part1,
       "background-message2": background_message2,
       "background-status-msg-line2-part1": background_status_msg_line2_part1,
       "error-log-clear": error_log_clear,
       "job-output-auto-continue-timeout": job_output_auto_continue_timeout,
       "collated-originals-support": collated_originals_support,
       "device-cfg-download-error": device_cfg_download_error,
       "device-cfg-upload-error": device_cfg_upload_error,
       "localization-languages-supported": localization_languages_supported,
       "localization-countries-supported": localization_countries_supported,
       "host-application-available-memory": host_application_available_memory,
       "control-panel-button-press": control_panel_button_press,
       "control-panel-display": control_panel_display,
       "ship-cartridge-installed-in-printer": ship_cartridge_installed_in_printer,
       "device-mac-address": device_mac_address,
       "extended-print-modes-modified": extended_print_modes_modified,
       "id": id,
       "model-number": model_number,
       "model-name": model_name,
       "serial-number": serial_number,
       "fw-rom-datecode": fw_rom_datecode,
       "fw-rom-revision": fw_rom_revision,
       "fax-local-phone-num": fax_local_phone_num,
       "fax-station-name": fax_station_name,
       "device-name": device_name,
       "device-location": device_location,
       "asset-number": asset_number,
       "system-contact": system_contact,
       "fax-line-interface-unit-id": fax_line_interface_unit_id,
       "interface": interface,
       "simm": simm,
       "simm1": simm1,
       "simm1-type": simm1_type,
       "simm1-capacity": simm1_capacity,
       "simm1-bank": simm1_bank,
       "simm1-bank1": simm1_bank1,
       "simm1-bank1-type": simm1_bank1_type,
       "simm1-bank1-capacity": simm1_bank1_capacity,
       "simm1-bank2": simm1_bank2,
       "simm1-bank2-type": simm1_bank2_type,
       "simm1-bank2-capacity": simm1_bank2_capacity,
       "simm2": simm2,
       "simm2-type": simm2_type,
       "simm2-capacity": simm2_capacity,
       "simm2-bank": simm2_bank,
       "simm2-bank1": simm2_bank1,
       "simm2-bank1-type": simm2_bank1_type,
       "simm2-bank1-capacity": simm2_bank1_capacity,
       "simm2-bank2": simm2_bank2,
       "simm2-bank2-type": simm2_bank2_type,
       "simm2-bank2-capacity": simm2_bank2_capacity,
       "simm3": simm3,
       "simm3-type": simm3_type,
       "simm3-capacity": simm3_capacity,
       "simm3-bank": simm3_bank,
       "simm3-bank1": simm3_bank1,
       "simm3-bank1-type": simm3_bank1_type,
       "simm3-bank1-capacity": simm3_bank1_capacity,
       "simm3-bank2": simm3_bank2,
       "simm3-bank2-type": simm3_bank2_type,
       "simm3-bank2-capacity": simm3_bank2_capacity,
       "simm4": simm4,
       "simm4-type": simm4_type,
       "simm4-capacity": simm4_capacity,
       "simm5": simm5,
       "simm5-type": simm5_type,
       "simm5-capacity": simm5_capacity,
       "simm6": simm6,
       "simm6-type": simm6_type,
       "simm6-capacity": simm6_capacity,
       "simm7": simm7,
       "simm7-type": simm7_type,
       "simm7-capacity": simm7_capacity,
       "simm8": simm8,
       "simm8-type": simm8_type,
       "simm8-capacity": simm8_capacity,
       "at": at,
       "at1": at1,
       "at1-model-number": at1_model_number,
       "at1-model-name": at1_model_name,
       "at1-manufacturing-info": at1_manufacturing_info,
       "at1-type": at1_type,
       "at1-capacity": at1_capacity,
       "mio": mio,
       "mio1": mio1,
       "mio1-model-name": mio1_model_name,
       "mio1-manufacturing-info": mio1_manufacturing_info,
       "mio1-type": mio1_type,
       "mio2": mio2,
       "mio2-model-name": mio2_model_name,
       "mio2-manufacturing-info": mio2_manufacturing_info,
       "mio2-type": mio2_type,
       "mio3": mio3,
       "mio3-model-name": mio3_model_name,
       "mio3-manufacturing-info": mio3_manufacturing_info,
       "mio3-type": mio3_type,
       "mio4": mio4,
       "mio4-model-name": mio4_model_name,
       "mio4-manufacturing-info": mio4_manufacturing_info,
       "mio4-type": mio4_type,
       "phd": phd,
       "phd1": phd1,
       "phd1-model": phd1_model,
       "phd1-manufacturing-info": phd1_manufacturing_info,
       "phd1-type": phd1_type,
       "phd1-capacity": phd1_capacity,
       "phd2": phd2,
       "phd2-model": phd2_model,
       "phd2-manufacturing-info": phd2_manufacturing_info,
       "phd2-type": phd2_type,
       "phd2-capacity": phd2_capacity,
       "phd3": phd3,
       "phd3-model": phd3_model,
       "phd3-manufacturing-info": phd3_manufacturing_info,
       "phd3-type": phd3_type,
       "phd3-capacity": phd3_capacity,
       "phd4": phd4,
       "phd4-model": phd4_model,
       "phd4-manufacturing-info": phd4_manufacturing_info,
       "phd4-type": phd4_type,
       "phd4-capacity": phd4_capacity,
       "phd5": phd5,
       "phd5-model": phd5_model,
       "phd5-manufacturing-info": phd5_manufacturing_info,
       "phd5-type": phd5_type,
       "phd5-capacity": phd5_capacity,
       "phd6": phd6,
       "phd6-model": phd6_model,
       "phd6-manufacturing-info": phd6_manufacturing_info,
       "phd6-type": phd6_type,
       "phd6-capacity": phd6_capacity,
       "web-server": web_server,
       "settings-web-server": settings_web_server,
       "web-proxy-config-enable": web_proxy_config_enable,
       "ews-request-control-panel-supplies-status": ews_request_control_panel_supplies_status,
       "foreign-interface": foreign_interface,
       "fih-extra-pulses-feature": fih_extra_pulses_feature,
       "usb-interface": usb_interface,
       "usb": usb,
       "usb-product-id": usb_product_id,
       "test": test,
       "self-test": self_test,
       "print-internal-page": print_internal_page,
       "job": job,
       "settings-job": settings_job,
       "clearable-warning": clearable_warning,
       "cancel-job": cancel_job,
       "job-info-change-id": job_info_change_id,
       "hold-job-timeout": hold_job_timeout,
       "active-print-jobs": active_print_jobs,
       "job-being-parsed": job_being_parsed,
       "current-job-parsing-id": current_job_parsing_id,
       "fax-job-control": fax_job_control,
       "settings-fax-job": settings_fax_job,
       "faxjob-action": faxjob_action,
       "faxjob-action-id": faxjob_action_id,
       "faxjob-tx-type": faxjob_tx_type,
       "faxjob-print-duplex-mode-select": faxjob_print_duplex_mode_select,
       "status-fax-job": status_fax_job,
       "faxjob-download-id": faxjob_download_id,
       "faxjob-rx-id": faxjob_rx_id,
       "faxjob-tx-id": faxjob_tx_id,
       "faxjob-upload-id": faxjob_upload_id,
       "faxjob": faxjob,
       "faxjob-rx-status": faxjob_rx_status,
       "faxjob-rx-status-1": faxjob_rx_status_1,
       "faxjob-tx-status": faxjob_tx_status,
       "faxjob-tx-status-1": faxjob_tx_status_1,
       "faxjob-tx-error": faxjob_tx_error,
       "faxjob-tx-error-1": faxjob_tx_error_1,
       "faxjob-tx-current-page": faxjob_tx_current_page,
       "faxjob-tx-current-page-1": faxjob_tx_current_page_1,
       "faxjob-rx-current-page": faxjob_rx_current_page,
       "faxjob-rx-current-page-1": faxjob_rx_current_page_1,
       "faxjob-rx-duration": faxjob_rx_duration,
       "faxjob-rx-duration-1": faxjob_rx_duration_1,
       "faxjob-tx-duration": faxjob_tx_duration,
       "faxjob-tx-duration-1": faxjob_tx_duration_1,
       "fax-activity-log": fax_activity_log,
       "settings-faxlog": settings_faxlog,
       "fax-log-action": fax_log_action,
       "fax-log-reporting": fax_log_reporting,
       "job-info": job_info,
       "job-info-name1": job_info_name1,
       "job-info-name2": job_info_name2,
       "job-info-stage": job_info_stage,
       "job-info-io-source": job_info_io_source,
       "job-info-pages-processed": job_info_pages_processed,
       "job-info-pages-printed": job_info_pages_printed,
       "job-info-size": job_info_size,
       "job-info-state": job_info_state,
       "job-info-outcome": job_info_outcome,
       "job-info-outbins-used": job_info_outbins_used,
       "job-info-physical-outbins-used": job_info_physical_outbins_used,
       "job-info-attribute": job_info_attribute,
       "job-info-attr-1": job_info_attr_1,
       "job-info-attr-2": job_info_attr_2,
       "job-info-attr-3": job_info_attr_3,
       "job-info-attr-4": job_info_attr_4,
       "job-info-attr-5": job_info_attr_5,
       "job-info-attr-6": job_info_attr_6,
       "job-info-attr-7": job_info_attr_7,
       "job-info-attr-8": job_info_attr_8,
       "job-info-attr-9": job_info_attr_9,
       "job-info-attr-10": job_info_attr_10,
       "job-info-attr-11": job_info_attr_11,
       "job-info-attr-12": job_info_attr_12,
       "job-info-attr-13": job_info_attr_13,
       "job-info-attr-14": job_info_attr_14,
       "job-info-attr-15": job_info_attr_15,
       "job-info-attr-16": job_info_attr_16,
       "job-info-attr-17": job_info_attr_17,
       "job-info-attr-18": job_info_attr_18,
       "job-info-attr-19": job_info_attr_19,
       "job-info-attr-20": job_info_attr_20,
       "job-info-attr-21": job_info_attr_21,
       "job-info-attr-22": job_info_attr_22,
       "job-info-attr-23": job_info_attr_23,
       "job-info-attr-24": job_info_attr_24,
       "job-info-attr-25": job_info_attr_25,
       "job-info-attr-26": job_info_attr_26,
       "job-info-attr-27": job_info_attr_27,
       "job-info-attr-28": job_info_attr_28,
       "job-info-attr-29": job_info_attr_29,
       "job-info-attr-30": job_info_attr_30,
       "job-info-attr-31": job_info_attr_31,
       "job-info-attr-32": job_info_attr_32,
       "job-info-requested-originals": job_info_requested_originals,
       "job-info-page-count-current-original": job_info_page_count_current_original,
       "job-info-pages-in-original": job_info_pages_in_original,
       "job-info-printed-originals": job_info_printed_originals,
       "job-info-accounting": job_info_accounting,
       "held-job": held_job,
       "held-job-info": held_job_info,
       "held-job-user-name": held_job_user_name,
       "held-job-job-name": held_job_job_name,
       "held-job-retention": held_job_retention,
       "held-job-security": held_job_security,
       "held-job-quantity": held_job_quantity,
       "held-job-pin": held_job_pin,
       "held-job-control": held_job_control,
       "held-job-print": held_job_print,
       "held-job-delete": held_job_delete,
       "held-job-set-queue-size": held_job_set_queue_size,
       "held-job-enable": held_job_enable,
       "photo-job": photo_job,
       "photo-access-card-error": photo_access_card_error,
       "settings-photo-job": settings_photo_job,
       "photo-default-num-copies": photo_default_num_copies,
       "photo-job-num-copies": photo_job_num_copies,
       "photo-job-media-size": photo_job_media_size,
       "photo-job-media-name": photo_job_media_name,
       "photo-image-size": photo_image_size,
       "photo-job-image-size": photo_job_image_size,
       "photo-select-images": photo_select_images,
       "photo-images-on-card": photo_images_on_card,
       "photo-job-source": photo_job_source,
       "photo-color-page-count": photo_color_page_count,
       "photo-mono-page-count": photo_mono_page_count,
       "photo-image-size-set": photo_image_size_set,
       "photo-clear-counts": photo_clear_counts,
       "photo-compact-flash-insert-count": photo_compact_flash_insert_count,
       "photo-memory-stick-insert-count": photo_memory_stick_insert_count,
       "photo-memory-stick-pro-insert-count": photo_memory_stick_pro_insert_count,
       "photo-smart-media-insert-count": photo_smart_media_insert_count,
       "photo-secure-digital-insert-count": photo_secure_digital_insert_count,
       "photo-mmc-insert-count": photo_mmc_insert_count,
       "photo-xd-insert-count": photo_xd_insert_count,
       "phone": phone,
       "dial": dial,
       "dial-all-lines": dial_all_lines,
       "fax-dial-mode": fax_dial_mode,
       "device-redial": device_redial,
       "answer": answer,
       "answer-all-lines": answer_all_lines,
       "fax-answer-mode": fax_answer_mode,
       "fax-num-rings-pickup": fax_num_rings_pickup,
       "device-ring-type-pickup": device_ring_type_pickup,
       "file-system": file_system,
       "settings-file-system": settings_file_system,
       "file-system-memory": file_system_memory,
       "file-system-max-open-files": file_system_max_open_files,
       "file-system-test-return-code": file_system_test_return_code,
       "file-system-set-system-partition-writeable": file_system_set_system_partition_writeable,
       "file-system-set-system-partition-readonly": file_system_set_system_partition_readonly,
       "file-system-delete-files": file_system_delete_files,
       "file-system-security-access-password": file_system_security_access_password,
       "file-system-external-access-capabilities": file_system_external_access_capabilities,
       "file-system-erase-mode": file_system_erase_mode,
       "file-system-wipe-disk": file_system_wipe_disk,
       "file-system-wipe-disk-status": file_system_wipe_disk_status,
       "status-file-system": status_file_system,
       "file-system-statistic-read-open": file_system_statistic_read_open,
       "file-system-statistic-write-open": file_system_statistic_write_open,
       "file-system-statistic-successful": file_system_statistic_successful,
       "file-system-statistic-unsuccessful": file_system_statistic_unsuccessful,
       "file-system-statistic-current-memory-usage": file_system_statistic_current_memory_usage,
       "file-system-statistic-max-memory-usage": file_system_statistic_max_memory_usage,
       "file-systems": file_systems,
       "file-system1": file_system1,
       "file-system1-initialized": file_system1_initialized,
       "file-system1-capacity": file_system1_capacity,
       "file-system1-free-space": file_system1_free_space,
       "file-system1-write-protect": file_system1_write_protect,
       "file-system2": file_system2,
       "file-system2-initialize-volume": file_system2_initialize_volume,
       "file-system3": file_system3,
       "file-system3-initialize-volume": file_system3_initialize_volume,
       "file-system4": file_system4,
       "file-system4-initialize-volume": file_system4_initialize_volume,
       "errorlog": errorlog,
       "error1": error1,
       "error1-time-stamp": error1_time_stamp,
       "error1-code": error1_code,
       "error2": error2,
       "error2-time-stamp": error2_time_stamp,
       "error2-code": error2_code,
       "error3": error3,
       "error3-time-stamp": error3_time_stamp,
       "error3-code": error3_code,
       "error4": error4,
       "error4-time-stamp": error4_time_stamp,
       "error4-code": error4_code,
       "error5": error5,
       "error5-time-stamp": error5_time_stamp,
       "error5-code": error5_code,
       "error6": error6,
       "error6-time-stamp": error6_time_stamp,
       "error6-code": error6_code,
       "error7": error7,
       "error7-time-stamp": error7_time_stamp,
       "error7-code": error7_code,
       "error8": error8,
       "error8-time-stamp": error8_time_stamp,
       "error8-code": error8_code,
       "error9": error9,
       "error9-time-stamp": error9_time_stamp,
       "error9-code": error9_code,
       "error10": error10,
       "error10-time-stamp": error10_time_stamp,
       "error10-code": error10_code,
       "error11": error11,
       "error11-time-stamp": error11_time_stamp,
       "error11-code": error11_code,
       "error12": error12,
       "error12-time-stamp": error12_time_stamp,
       "error12-code": error12_code,
       "error13": error13,
       "error13-time-stamp": error13_time_stamp,
       "error13-code": error13_code,
       "error14": error14,
       "error14-time-stamp": error14_time_stamp,
       "error14-code": error14_code,
       "error15": error15,
       "error15-time-stamp": error15_time_stamp,
       "error15-code": error15_code,
       "error16": error16,
       "error16-time-stamp": error16_time_stamp,
       "error16-code": error16_code,
       "error17": error17,
       "error17-time-stamp": error17_time_stamp,
       "error17-code": error17_code,
       "error18": error18,
       "error18-time-stamp": error18_time_stamp,
       "error18-code": error18_code,
       "error19": error19,
       "error19-time-stamp": error19_time_stamp,
       "error19-code": error19_code,
       "error20": error20,
       "error20-time-stamp": error20_time_stamp,
       "error20-code": error20_code,
       "error21": error21,
       "error21-time-stamp": error21_time_stamp,
       "error21-code": error21_code,
       "error22": error22,
       "error22-time-stamp": error22_time_stamp,
       "error22-code": error22_code,
       "error23": error23,
       "error23-time-stamp": error23_time_stamp,
       "error23-code": error23_code,
       "error24": error24,
       "error24-time-stamp": error24_time_stamp,
       "error24-code": error24_code,
       "error25": error25,
       "error25-time-stamp": error25_time_stamp,
       "error25-code": error25_code,
       "error26": error26,
       "error26-time-stamp": error26_time_stamp,
       "error26-code": error26_code,
       "error27": error27,
       "error27-time-stamp": error27_time_stamp,
       "error27-code": error27_code,
       "error28": error28,
       "error28-time-stamp": error28_time_stamp,
       "error28-code": error28_code,
       "error29": error29,
       "error29-time-stamp": error29_time_stamp,
       "error29-code": error29_code,
       "error30": error30,
       "error30-time-stamp": error30_time_stamp,
       "error30-code": error30_code,
       "error31": error31,
       "error31-time-stamp": error31_time_stamp,
       "error31-code": error31_code,
       "error32": error32,
       "error32-time-stamp": error32_time_stamp,
       "error32-code": error32_code,
       "error33": error33,
       "error33-time-stamp": error33_time_stamp,
       "error33-code": error33_code,
       "error34": error34,
       "error34-time-stamp": error34_time_stamp,
       "error34-code": error34_code,
       "error35": error35,
       "error35-time-stamp": error35_time_stamp,
       "error35-code": error35_code,
       "error36": error36,
       "error36-time-stamp": error36_time_stamp,
       "error36-code": error36_code,
       "error37": error37,
       "error37-time-stamp": error37_time_stamp,
       "error37-code": error37_code,
       "error38": error38,
       "error38-time-stamp": error38_time_stamp,
       "error38-code": error38_code,
       "error39": error39,
       "error39-time-stamp": error39_time_stamp,
       "error39-code": error39_code,
       "error40": error40,
       "error40-time-stamp": error40_time_stamp,
       "error40-code": error40_code,
       "error41": error41,
       "error41-time-stamp": error41_time_stamp,
       "error41-code": error41_code,
       "error42": error42,
       "error42-time-stamp": error42_time_stamp,
       "error42-code": error42_code,
       "error43": error43,
       "error43-time-stamp": error43_time_stamp,
       "error43-code": error43_code,
       "error44": error44,
       "error44-time-stamp": error44_time_stamp,
       "error44-code": error44_code,
       "error45": error45,
       "error45-time-stamp": error45_time_stamp,
       "error45-code": error45_code,
       "error46": error46,
       "error46-time-stamp": error46_time_stamp,
       "error46-code": error46_code,
       "error47": error47,
       "error47-time-stamp": error47_time_stamp,
       "error47-code": error47_code,
       "error48": error48,
       "error48-time-stamp": error48_time_stamp,
       "error48-code": error48_code,
       "error49": error49,
       "error49-time-stamp": error49_time_stamp,
       "error49-code": error49_code,
       "error50": error50,
       "error50-time-stamp": error50_time_stamp,
       "error50-code": error50_code,
       "error51": error51,
       "error52": error52,
       "error53": error53,
       "error54": error54,
       "error55": error55,
       "error56": error56,
       "error57": error57,
       "error58": error58,
       "error59": error59,
       "error60": error60,
       "error61": error61,
       "error62": error62,
       "error63": error63,
       "error64": error64,
       "error65": error65,
       "error66": error66,
       "error67": error67,
       "error68": error68,
       "error69": error69,
       "error70": error70,
       "error71": error71,
       "error72": error72,
       "error73": error73,
       "error74": error74,
       "error75": error75,
       "error76": error76,
       "error77": error77,
       "error78": error78,
       "error79": error79,
       "error80": error80,
       "error81": error81,
       "error82": error82,
       "error83": error83,
       "error84": error84,
       "error85": error85,
       "error86": error86,
       "error87": error87,
       "error88": error88,
       "error89": error89,
       "error90": error90,
       "resource-manager": resource_manager,
       "mass-storage-resources": mass_storage_resources,
       "mass-storage-resource-change-counter": mass_storage_resource_change_counter,
       "mass-storage-resource-changed": mass_storage_resource_changed,
       "remote-procedure-call": remote_procedure_call,
       "settings-rpc": settings_rpc,
       "rpc-test-return-code": rpc_test_return_code,
       "rpc-bind-protocol-address": rpc_bind_protocol_address,
       "status-rpc": status_rpc,
       "rpc-statistic-successful": rpc_statistic_successful,
       "rpc-statistic-unsuccessful": rpc_statistic_unsuccessful,
       "rpc-bound-protocol-address": rpc_bound_protocol_address,
       "rpc-services": rpc_services,
       "mount": mount,
       "settings-mount": settings_mount,
       "mount-test-return-code": mount_test_return_code,
       "nfs-server": nfs_server,
       "settings-nfs-server": settings_nfs_server,
       "nfs-server-memory": nfs_server_memory,
       "nfs-server-read-size": nfs_server_read_size,
       "nfs-server-write-size": nfs_server_write_size,
       "nfs-server-test-return-code": nfs_server_test_return_code,
       "status-nfs-server": status_nfs_server,
       "nfs-server-statistic-successful": nfs_server_statistic_successful,
       "nfs-server-statistic-unsuccessful": nfs_server_statistic_unsuccessful,
       "nfs-server-statistic-current-memory-usage": nfs_server_statistic_current_memory_usage,
       "nfs-server-statistic-max-memory-usage": nfs_server_statistic_max_memory_usage,
       "rpc-bind": rpc_bind,
       "settings-rpc-bind": settings_rpc_bind,
       "rpc-bind-test-return-code": rpc_bind_test_return_code,
       "status-rpc-bind": status_rpc_bind,
       "rpc-bind-statistic-successful": rpc_bind_statistic_successful,
       "rpc-bind-statistic-unsuccessful": rpc_bind_statistic_unsuccessful,
       "xport-interface": xport_interface,
       "status-xip": status_xip,
       "xip-statistic-processed": xip_statistic_processed,
       "xip-statistic-data-in-dropped": xip_statistic_data_in_dropped,
       "mass-storage-block-driver": mass_storage_block_driver,
       "settings-mass-storage-bd": settings_mass_storage_bd,
       "ram-disk-mode": ram_disk_mode,
       "ram-disk-size": ram_disk_size,
       "status-mass-storage-bd": status_mass_storage_bd,
       "maximum-ram-disk-memory": maximum_ram_disk_memory,
       "mass-storage-block-drivers": mass_storage_block_drivers,
       "mass-storage-bd2": mass_storage_bd2,
       "settings-msbd2": settings_msbd2,
       "disk-storage-block-driver2-test-return-code": disk_storage_block_driver2_test_return_code,
       "accounting": accounting,
       "printer-accounting": printer_accounting,
       "printed-media-usage": printed_media_usage,
       "printed-media-simplex-count": printed_media_simplex_count,
       "printed-media-simplex-charge": printed_media_simplex_charge,
       "printed-media-duplex-count": printed_media_duplex_count,
       "printed-media-duplex-charge": printed_media_duplex_charge,
       "printed-media-total-charge": printed_media_total_charge,
       "printed-media-combined-total": printed_media_combined_total,
       "printed-media-dimplex-count": printed_media_dimplex_count,
       "printed-media-combined-simplex-count": printed_media_combined_simplex_count,
       "printed-media-combined-duplex-count": printed_media_combined_duplex_count,
       "impression-based-duplex-count-supported": impression_based_duplex_count_supported,
       "usage-printer-total-charge": usage_printer_total_charge,
       "usage-average-toner-coverage": usage_average_toner_coverage,
       "usage-staple-count": usage_staple_count,
       "usage-instructions-line1": usage_instructions_line1,
       "usage-instructions-line2": usage_instructions_line2,
       "usage-instructions-line3": usage_instructions_line3,
       "usage-instructions-line4": usage_instructions_line4,
       "print-meter-usage": print_meter_usage,
       "print-meter-usage-threshold": print_meter_usage_threshold,
       "print-meter-print-quality": print_meter_print_quality,
       "print-meter-simplex-count": print_meter_simplex_count,
       "print-meter-duplex-count": print_meter_duplex_count,
       "print-meter-total-charge": print_meter_total_charge,
       "print-meter-dimplex-count": print_meter_dimplex_count,
       "print-meter-simplex-total": print_meter_simplex_total,
       "print-meter-duplex-total": print_meter_duplex_total,
       "print-meter-category-total": print_meter_category_total,
       "print-meter-dimplex-total": print_meter_dimplex_total,
       "scanner-accounting": scanner_accounting,
       "scanned-media-usage": scanned_media_usage,
       "scanned-media-simplex-count": scanned_media_simplex_count,
       "scanned-media-simplex-charge": scanned_media_simplex_charge,
       "scanned-media-duplex-count": scanned_media_duplex_count,
       "scanned-media-duplex-charge": scanned_media_duplex_charge,
       "scanned-media-total-charge": scanned_media_total_charge,
       "usage-scanner-total-charge": usage_scanner_total_charge,
       "printer-color-accounting": printer_color_accounting,
       "printed-media-color-usage": printed_media_color_usage,
       "printed-media-color-simplex-count": printed_media_color_simplex_count,
       "printed-media-color-duplex-count": printed_media_color_duplex_count,
       "printed-media-color-total-count": printed_media_color_total_count,
       "printed-media-color-dimplex-count": printed_media_color_dimplex_count,
       "printed-modes-accounting": printed_modes_accounting,
       "printed-modes-usage": printed_modes_usage,
       "printed-modes-mono-count": printed_modes_mono_count,
       "printed-modes-color-count": printed_modes_color_count,
       "printed-modes-total-count": printed_modes_total_count,
       "source-tray-accounting": source_tray_accounting,
       "source-tray-usage": source_tray_usage,
       "source-tray-usage-count": source_tray_usage_count,
       "destination-bin-accounting": destination_bin_accounting,
       "destination-bin-usage": destination_bin_usage,
       "destination-bin-usage-count": destination_bin_usage_count,
       "firmware-download": firmware_download,
       "firmware-download-write-status-supported": firmware_download_write_status_supported,
       "firmware-download-write-time": firmware_download_write_time,
       "firmware-download-write-count": firmware_download_write_count,
       "firmware-download-current-state": firmware_download_current_state,
       "firmware-download-maximum-write-count": firmware_download_maximum_write_count,
       "firmware-download-name": firmware_download_name,
       "firmware-download-version": firmware_download_version,
       "operating-system": operating_system,
       "upgradable-devices": upgradable_devices,
       "upgradable-devices-write-status-supported": upgradable_devices_write_status_supported,
       "upgradable-devices-write-time": upgradable_devices_write_time,
       "upgradable-devices-write-count": upgradable_devices_write_count,
       "upgradable-devices-current-state": upgradable_devices_current_state,
       "upgradable-devices-max-write-count": upgradable_devices_max_write_count,
       "upgradable-devices-name": upgradable_devices_name,
       "upgradable-devices-version": upgradable_devices_version,
       "remote-upgrade-enable": remote_upgrade_enable,
       "warninglog": warninglog,
       "warning1": warning1,
       "warning2": warning2,
       "warning3": warning3,
       "warning4": warning4,
       "warning5": warning5,
       "warning6": warning6,
       "warning7": warning7,
       "warning8": warning8,
       "warning9": warning9,
       "warning10": warning10,
       "warning11": warning11,
       "warning12": warning12,
       "warning13": warning13,
       "warning14": warning14,
       "warning15": warning15,
       "warning16": warning16,
       "warning17": warning17,
       "warning18": warning18,
       "warning19": warning19,
       "warning20": warning20,
       "warning21": warning21,
       "warning22": warning22,
       "warning23": warning23,
       "warning24": warning24,
       "warning25": warning25,
       "warning26": warning26,
       "warning27": warning27,
       "warning28": warning28,
       "warning29": warning29,
       "warning30": warning30,
       "warning31": warning31,
       "warning32": warning32,
       "warning33": warning33,
       "warning34": warning34,
       "warning35": warning35,
       "warning36": warning36,
       "warning37": warning37,
       "warning38": warning38,
       "warning39": warning39,
       "warning40": warning40,
       "warning41": warning41,
       "warning42": warning42,
       "warning43": warning43,
       "warning44": warning44,
       "warning45": warning45,
       "warning46": warning46,
       "warning47": warning47,
       "warning48": warning48,
       "warning49": warning49,
       "warning50": warning50,
       "security": security,
       "settings-security": settings_security,
       "supports-pjl-user-groups": supports_pjl_user_groups,
       "settings-system2": settings_system2,
       "toner-miser-plus-value": toner_miser_plus_value,
       "toner-miser-plus-supported": toner_miser_plus_supported,
       "protect-ews-info-tab": protect_ews_info_tab,
       "eprint-opt-in": eprint_opt_in,
       "eprint-enabled": eprint_enabled,
       "eprint-email-address": eprint_email_address,
       "eprint-email": eprint_email,
       "eprint-printer-code": eprint_printer_code,
       "eprint-hp-web-services": eprint_hp_web_services,
       "eprint-jdi-interface": eprint_jdi_interface,
       "eprint-supported": eprint_supported,
       "eprint-supported-jdi": eprint_supported_jdi,
       "fax-init-at-command": fax_init_at_command,
       "set-primary-interface-index": set_primary_interface_index,
       "wireless-direct-print-setting": wireless_direct_print_setting,
       "source-subsystem": source_subsystem,
       "io": io,
       "settings-io": settings_io,
       "io-timeout": io_timeout,
       "io-switch": io_switch,
       "io-buffering": io_buffering,
       "io-buffer-size": io_buffer_size,
       "maximum-io-buffering-memory": maximum_io_buffering_memory,
       "status-io": status_io,
       "not-ready-source-io": not_ready_source_io,
       "status-source-io": status_source_io,
       "ports": ports,
       "port1": port1,
       "parallel": parallel,
       "parallel-speed": parallel_speed,
       "parallel-bidirectionality": parallel_bidirectionality,
       "port1-parallel-speed": port1_parallel_speed,
       "port1-parallel-bidirectionality": port1_parallel_bidirectionality,
       "scanner": scanner,
       "settings-scanner": settings_scanner,
       "scan-contrast": scan_contrast,
       "scan-resolution": scan_resolution,
       "scan-pixel-data-type": scan_pixel_data_type,
       "scan-compression": scan_compression,
       "scan-compression-factor": scan_compression_factor,
       "scan-upload-error": scan_upload_error,
       "scan-upload": scan_upload,
       "default-scanner-margin-left": default_scanner_margin_left,
       "default-scanner-margin-right": default_scanner_margin_right,
       "scanner-accessory-serial-number": scanner_accessory_serial_number,
       "scanner-accessory-model-number": scanner_accessory_model_number,
       "scanner-accessory-adf-sheet-count": scanner_accessory_adf_sheet_count,
       "scanner-accessory-flatbed-scan-count": scanner_accessory_flatbed_scan_count,
       "scanner-accessory-cleaning-interval": scanner_accessory_cleaning_interval,
       "scanner-accessory-cleaning-count": scanner_accessory_cleaning_count,
       "scanner-accessory-maintenance-interval": scanner_accessory_maintenance_interval,
       "scanner-accessory-maintenance-count": scanner_accessory_maintenance_count,
       "scanner-accessory-rom-revision": scanner_accessory_rom_revision,
       "scanner-accessory-copy-processor-boot-revision": scanner_accessory_copy_processor_boot_revision,
       "scanner-accessory-copy-processor-runtime-revision": scanner_accessory_copy_processor_runtime_revision,
       "scanner-accessory-service-agent-revision": scanner_accessory_service_agent_revision,
       "scanner-accessory-control-panel-user-interface-revision": scanner_accessory_control_panel_user_interface_revision,
       "scan-calibration": scan_calibration,
       "scan-calibration-target": scan_calibration_target,
       "scanner-accessory-nvram": scanner_accessory_nvram,
       "scanner-accessory-nvram2": scanner_accessory_nvram2,
       "scanner-accessory-nvram3": scanner_accessory_nvram3,
       "scanner-accessory-nvram4": scanner_accessory_nvram4,
       "ui-add-option": ui_add_option,
       "ui-select-option": ui_select_option,
       "ui-delete-option": ui_delete_option,
       "scanner-jam-page-count": scanner_jam_page_count,
       "scanner-adf-page-count": scanner_adf_page_count,
       "scan-adf-page-count": scan_adf_page_count,
       "scan-image-type": scan_image_type,
       "scan-subsample": scan_subsample,
       "scanner-retrieve-scanline": scanner_retrieve_scanline,
       "scanner-motor-control": scanner_motor_control,
       "scan-height": scan_height,
       "scanner-scanline-statistics": scanner_scanline_statistics,
       "scan-control-descriptor": scan_control_descriptor,
       "scan-gamma-correction": scan_gamma_correction,
       "scan-pad-image": scan_pad_image,
       "scanner-accessory-total-copy-pages-printed": scanner_accessory_total_copy_pages_printed,
       "scan-flatbed-page-count": scan_flatbed_page_count,
       "scanner-flatbed-page-count": scanner_flatbed_page_count,
       "scanner-modular-hardware": scanner_modular_hardware,
       "scanner-clock-edge-modifiers": scanner_clock_edge_modifiers,
       "scan-clock-edges": scan_clock_edges,
       "scan-emulate-copy": scan_emulate_copy,
       "status-scanner": status_scanner,
       "not-ready-source-scanner": not_ready_source_scanner,
       "scan-resolution-range": scan_resolution_range,
       "scan-calibration-download": scan_calibration_download,
       "scan-calibration-error": scan_calibration_error,
       "scanner-button-status": scanner_button_status,
       "scanner-lamp-gain-value": scanner_lamp_gain_value,
       "scanner-light-monitor-window": scanner_light_monitor_window,
       "scanner-reference-position": scanner_reference_position,
       "scanner-sensor-manufacturer": scanner_sensor_manufacturer,
       "copy-scanner-dimensions": copy_scanner_dimensions,
       "fax-receive": fax_receive,
       "settings-fax-receive": settings_fax_receive,
       "fax-receive-stamping-enable": fax_receive_stamping_enable,
       "status-fax-receive": status_fax_receive,
       "not-ready-fax-receive": not_ready_fax_receive,
       "spooler": spooler,
       "settings-spooler": settings_spooler,
       "mopy-mode": mopy_mode,
       "processing-subsystem": processing_subsystem,
       "pdl": pdl,
       "settings-pdl": settings_pdl,
       "default-orientation": default_orientation,
       "default-copies": default_copies,
       "form-feed": form_feed,
       "resource-saving": resource_saving,
       "maximum-resource-saving-memory": maximum_resource_saving_memory,
       "default-vertical-black-resolution": default_vertical_black_resolution,
       "default-horizontal-black-resolution": default_horizontal_black_resolution,
       "default-page-protect": default_page_protect,
       "default-lines-per-page": default_lines_per_page,
       "default-vmi": default_vmi,
       "default-media-size": default_media_size,
       "cold-reset-media-size": cold_reset_media_size,
       "default-media-name": default_media_name,
       "reprint": reprint,
       "wide-a4": wide_a4,
       "dark-courier": dark_courier,
       "default-bits-per-pixel": default_bits_per_pixel,
       "status-pdl": status_pdl,
       "not-ready-processing-pdl": not_ready_processing_pdl,
       "form-feed-needed": form_feed_needed,
       "pdl-pcl": pdl_pcl,
       "pcl-datecode": pcl_datecode,
       "pcl-resource-saving-memory-size": pcl_resource_saving_memory_size,
       "pcl-name": pcl_name,
       "pcl-version": pcl_version,
       "pcl-total-page-count": pcl_total_page_count,
       "pcl-default-symbol-set": pcl_default_symbol_set,
       "pcl-default-font-height": pcl_default_font_height,
       "pcl-default-font-source": pcl_default_font_source,
       "pcl-default-font-number": pcl_default_font_number,
       "pcl-default-font-width": pcl_default_font_width,
       "pdl-postscript": pdl_postscript,
       "postscript-datecode": postscript_datecode,
       "postscript-resource-saving-memory-size": postscript_resource_saving_memory_size,
       "postscript-name": postscript_name,
       "postscript-version": postscript_version,
       "postscript-total-page-count": postscript_total_page_count,
       "postscript-print-errors": postscript_print_errors,
       "postscript-jam-recovery": postscript_jam_recovery,
       "postscript-defer-media": postscript_defer_media,
       "pdl-esc-p": pdl_esc_p,
       "esc-p-datecode": esc_p_datecode,
       "esc-p-name": esc_p_name,
       "esc-p-version": esc_p_version,
       "pdl-pdf": pdl_pdf,
       "pdf-version": pdf_version,
       "pdf-total-page-count": pdf_total_page_count,
       "pdf-enabled": pdf_enabled,
       "pdf-print-errors": pdf_print_errors,
       "pdl-pclxl": pdl_pclxl,
       "pclxl-total-page-count": pclxl_total_page_count,
       "pml": pml,
       "pjl": pjl,
       "pjl-password": pjl_password,
       "fax-proc-sub": fax_proc_sub,
       "settings-fax-proc-sub": settings_fax_proc_sub,
       "fax-rxscale": fax_rxscale,
       "fax-noise-volume": fax_noise_volume,
       "fax-download": fax_download,
       "fax-silent-detection": fax_silent_detection,
       "fax-ring-enable": fax_ring_enable,
       "fax-country": fax_country,
       "fax-tx-phone-number": fax_tx_phone_number,
       "fax-redial-time": fax_redial_time,
       "fax-pstn-access-code": fax_pstn_access_code,
       "fax-rx-disposition": fax_rx_disposition,
       "fax-error-correction-mode": fax_error_correction_mode,
       "fax-report-transmission": fax_report_transmission,
       "fax-report-activity-log": fax_report_activity_log,
       "fax-dial-tone-detection": fax_dial_tone_detection,
       "fax-alarm-volume": fax_alarm_volume,
       "fax-beep-volume": fax_beep_volume,
       "fax-ring-volume": fax_ring_volume,
       "fax-master-host": fax_master_host,
       "fax-thumbnail-enable": fax_thumbnail_enable,
       "fax-phone-pickup-enable": fax_phone_pickup_enable,
       "fax-adf-scan-count": fax_adf_scan_count,
       "fax-print-page-count": fax_print_page_count,
       "fax-download-page-count": fax_download_page_count,
       "fax-upload-page-count": fax_upload_page_count,
       "fax-flatbed-scan-count": fax_flatbed_scan_count,
       "default-fax-glass-size": default_fax_glass_size,
       "fax-cold-reset-fax-glass-size": fax_cold_reset_fax_glass_size,
       "status-fax-proc-sub": status_fax_proc_sub,
       "fax-upload": fax_upload,
       "fax-min-rings-pickup": fax_min_rings_pickup,
       "fax-max-rings-pickup": fax_max_rings_pickup,
       "fax-max-redials": fax_max_redials,
       "fax-additional-wait": fax_additional_wait,
       "fax-download-error": fax_download_error,
       "fax-upload-error": fax_upload_error,
       "fax-firmware-revision": fax_firmware_revision,
       "fax-forwarding": fax_forwarding,
       "fax-forwarding-phone-num": fax_forwarding_phone_num,
       "jetsend-proc-sub": jetsend_proc_sub,
       "settings-jetsend": settings_jetsend,
       "jetsend-mode": jetsend_mode,
       "jetsend-contact": jetsend_contact,
       "settings-jetsend-contact": settings_jetsend_contact,
       "jetsend-contact-password": jetsend_contact_password,
       "jetsend-contact-ip-address-security": jetsend_contact_ip_address_security,
       "webserver-proc-sub": webserver_proc_sub,
       "settings-webserver": settings_webserver,
       "destination-subsystem": destination_subsystem,
       "print-engine": print_engine,
       "settings-prt-eng": settings_prt_eng,
       "override-media-name": override_media_name,
       "override-media-size": override_media_size,
       "print-density": print_density,
       "transfer-setting": transfer_setting,
       "marking-agent-density": marking_agent_density,
       "separation-setting": separation_setting,
       "status-prt-eng": status_prt_eng,
       "not-ready-destination-print-engine": not_ready_destination_print_engine,
       "not-ready-laser-print-engine": not_ready_laser_print_engine,
       "total-engine-page-count": total_engine_page_count,
       "total-mono-page-count": total_mono_page_count,
       "total-color-page-count": total_color_page_count,
       "status-destination-print-engine": status_destination_print_engine,
       "duplex-page-count": duplex_page_count,
       "print-engine-revision": print_engine_revision,
       "print-engine-jam-count": print_engine_jam_count,
       "print-engine-mispick-count": print_engine_mispick_count,
       "printer-calibration-dhalf": printer_calibration_dhalf,
       "printer-cal-dhalf-data": printer_cal_dhalf_data,
       "printer-cal-grayaxis": printer_cal_grayaxis,
       "printer-cal-grayaxis-data": printer_cal_grayaxis_data,
       "printer-calibration-cpr": printer_calibration_cpr,
       "intray": intray,
       "settings-intray": settings_intray,
       "default-manual-feed": default_manual_feed,
       "mp-tray": mp_tray,
       "tray-lock": tray_lock,
       "custom-paper-dim-unit": custom_paper_dim_unit,
       "custom-paper-feed-dim": custom_paper_feed_dim,
       "custom-paper-xfeed-dim": custom_paper_xfeed_dim,
       "status-intray": status_intray,
       "not-ready-tray-missing": not_ready_tray_missing,
       "not-ready-tray-empty": not_ready_tray_empty,
       "status-tray-missing": status_tray_missing,
       "status-tray-empty": status_tray_empty,
       "intrays": intrays,
       "intray1": intray1,
       "tray1-media-size-loaded": tray1_media_size_loaded,
       "tray1-media-available": tray1_media_available,
       "tray1-name": tray1_name,
       "tray1-media-name": tray1_media_name,
       "tray1-custom-media-width": tray1_custom_media_width,
       "tray1-custom-media-length": tray1_custom_media_length,
       "tray1-phd": tray1_phd,
       "tray1-fuser-temperature": tray1_fuser_temperature,
       "tray1-type": tray1_type,
       "tray1-media-key": tray1_media_key,
       "intray2": intray2,
       "tray2-media-size-loaded": tray2_media_size_loaded,
       "tray2-media-available": tray2_media_available,
       "tray2-name": tray2_name,
       "tray2-media-name": tray2_media_name,
       "tray2-custom-media-width": tray2_custom_media_width,
       "tray2-custom-media-length": tray2_custom_media_length,
       "tray2-phd": tray2_phd,
       "tray2-fuser-temperature": tray2_fuser_temperature,
       "tray2-type": tray2_type,
       "tray2-media-key": tray2_media_key,
       "intray3": intray3,
       "tray3-media-size-loaded": tray3_media_size_loaded,
       "tray3-media-available": tray3_media_available,
       "tray3-name": tray3_name,
       "tray3-media-name": tray3_media_name,
       "tray3-custom-media-width": tray3_custom_media_width,
       "tray3-custom-media-length": tray3_custom_media_length,
       "tray3-phd": tray3_phd,
       "tray3-fuser-temperature": tray3_fuser_temperature,
       "tray3-type": tray3_type,
       "tray3-media-key": tray3_media_key,
       "intray4": intray4,
       "tray4-media-size-loaded": tray4_media_size_loaded,
       "tray4-phd": tray4_phd,
       "intray5": intray5,
       "tray5-media-size-loaded": tray5_media_size_loaded,
       "tray5-media-name": tray5_media_name,
       "tray5-custom-media-width": tray5_custom_media_width,
       "tray5-custom-media-length": tray5_custom_media_length,
       "tray5-phd": tray5_phd,
       "tray5-type": tray5_type,
       "tray5-media-key": tray5_media_key,
       "intray6": intray6,
       "tray6-media-size-loaded": tray6_media_size_loaded,
       "tray6-phd": tray6_phd,
       "intray7": intray7,
       "tray7-media-size-loaded": tray7_media_size_loaded,
       "tray7-phd": tray7_phd,
       "outbin": outbin,
       "settings-outbin": settings_outbin,
       "overflow-bin": overflow_bin,
       "outbins": outbins,
       "outbin1": outbin1,
       "outbin1-maximum-capacity": outbin1_maximum_capacity,
       "outbin1-override-mode": outbin1_override_mode,
       "outbin2": outbin2,
       "outbin2-override-mode": outbin2_override_mode,
       "outbin3": outbin3,
       "outbin3-override-mode": outbin3_override_mode,
       "outbin3-maximum-binding": outbin3_maximum_binding,
       "outbin3-phd": outbin3_phd,
       "outbin3-error-info": outbin3_error_info,
       "outbin4": outbin4,
       "outbin4-override-mode": outbin4_override_mode,
       "outbin4-maximum-binding": outbin4_maximum_binding,
       "outbin4-phd": outbin4_phd,
       "outbin5": outbin5,
       "outbin5-override-mode": outbin5_override_mode,
       "outbin5-maximum-binding": outbin5_maximum_binding,
       "outbin5-phd": outbin5_phd,
       "outbin6": outbin6,
       "outbin6-override-mode": outbin6_override_mode,
       "outbin6-maximum-binding": outbin6_maximum_binding,
       "outbin6-phd": outbin6_phd,
       "outbin7": outbin7,
       "outbin7-override-mode": outbin7_override_mode,
       "outbin7-maximum-binding": outbin7_maximum_binding,
       "outbin7-phd": outbin7_phd,
       "outbin8": outbin8,
       "outbin8-override-mode": outbin8_override_mode,
       "outbin8-maximum-binding": outbin8_maximum_binding,
       "outbin8-phd": outbin8_phd,
       "outbin9": outbin9,
       "outbin9-override-mode": outbin9_override_mode,
       "outbin9-maximum-binding": outbin9_maximum_binding,
       "outbin9-phd": outbin9_phd,
       "outbin9-error-info": outbin9_error_info,
       "outbin10": outbin10,
       "outbin10-override-mode": outbin10_override_mode,
       "outbin10-maximum-binding": outbin10_maximum_binding,
       "outbin10-phd": outbin10_phd,
       "outbin11": outbin11,
       "outbin11-override-mode": outbin11_override_mode,
       "outbin11-maximum-binding": outbin11_maximum_binding,
       "outbin11-phd": outbin11_phd,
       "marking-agent": marking_agent,
       "settings-marking-agent": settings_marking_agent,
       "low-marking-agent-processing": low_marking_agent_processing,
       "imaging": imaging,
       "default-ret": default_ret,
       "default-print-quality": default_print_quality,
       "ph": ph,
       "settings-ph": settings_ph,
       "ph-devices": ph_devices,
       "ph2": ph2,
       "phd2-device-specific-command": phd2_device_specific_command,
       "phd2-device-memory": phd2_device_memory,
       "ph3": ph3,
       "phd3-device-specific-command": phd3_device_specific_command,
       "phd3-device-memory": phd3_device_memory,
       "ph4": ph4,
       "phd4-device-specific-command": phd4_device_specific_command,
       "phd4-device-memory": phd4_device_memory,
       "ph5": ph5,
       "phd5-device-specific-command": phd5_device_specific_command,
       "phd5-device-memory": phd5_device_memory,
       "ph6": ph6,
       "phd6-device-specific-command": phd6_device_specific_command,
       "phd6-device-memory": phd6_device_memory,
       "print-media": print_media,
       "settings-print-media": settings_print_media,
       "media-names-available": media_names_available,
       "north-edge-offset": north_edge_offset,
       "media-info": media_info,
       "media1": media1,
       "media1-name": media1_name,
       "media1-short-name": media1_short_name,
       "media1-page-count": media1_page_count,
       "media1-engine-media-mode": media1_engine_media_mode,
       "media2": media2,
       "media2-name": media2_name,
       "media2-short-name": media2_short_name,
       "media2-page-count": media2_page_count,
       "media2-engine-media-mode": media2_engine_media_mode,
       "media3": media3,
       "media3-name": media3_name,
       "media3-short-name": media3_short_name,
       "media3-page-count": media3_page_count,
       "media3-engine-media-mode": media3_engine_media_mode,
       "media4": media4,
       "media4-name": media4_name,
       "media4-short-name": media4_short_name,
       "media4-page-count": media4_page_count,
       "media4-engine-media-mode": media4_engine_media_mode,
       "media5": media5,
       "media5-name": media5_name,
       "media5-short-name": media5_short_name,
       "media5-page-count": media5_page_count,
       "media5-engine-media-mode": media5_engine_media_mode,
       "media6": media6,
       "media6-name": media6_name,
       "media6-short-name": media6_short_name,
       "media6-page-count": media6_page_count,
       "media6-engine-media-mode": media6_engine_media_mode,
       "media7": media7,
       "media7-name": media7_name,
       "media7-short-name": media7_short_name,
       "media7-page-count": media7_page_count,
       "media7-engine-media-mode": media7_engine_media_mode,
       "media8": media8,
       "media8-name": media8_name,
       "media8-short-name": media8_short_name,
       "media8-page-count": media8_page_count,
       "media8-engine-media-mode": media8_engine_media_mode,
       "media9": media9,
       "media9-name": media9_name,
       "media9-short-name": media9_short_name,
       "media9-page-count": media9_page_count,
       "media9-engine-media-mode": media9_engine_media_mode,
       "media10": media10,
       "media10-name": media10_name,
       "media10-short-name": media10_short_name,
       "media10-page-count": media10_page_count,
       "media10-engine-media-mode": media10_engine_media_mode,
       "media11": media11,
       "media11-name": media11_name,
       "media11-short-name": media11_short_name,
       "media11-page-count": media11_page_count,
       "media11-engine-media-mode": media11_engine_media_mode,
       "media12": media12,
       "media12-name": media12_name,
       "media12-short-name": media12_short_name,
       "media12-page-count": media12_page_count,
       "media12-engine-media-mode": media12_engine_media_mode,
       "media13": media13,
       "media13-name": media13_name,
       "media13-short-name": media13_short_name,
       "media13-page-count": media13_page_count,
       "media13-engine-media-mode": media13_engine_media_mode,
       "media14": media14,
       "media14-name": media14_name,
       "media14-short-name": media14_short_name,
       "media14-page-count": media14_page_count,
       "media14-engine-media-mode": media14_engine_media_mode,
       "media15": media15,
       "media15-name": media15_name,
       "media15-short-name": media15_short_name,
       "media15-page-count": media15_page_count,
       "media15-engine-media-mode": media15_engine_media_mode,
       "media16": media16,
       "media16-name": media16_name,
       "media16-short-name": media16_short_name,
       "media16-page-count": media16_page_count,
       "media16-engine-media-mode": media16_engine_media_mode,
       "media17": media17,
       "media17-name": media17_name,
       "media17-short-name": media17_short_name,
       "media17-page-count": media17_page_count,
       "media17-engine-media-mode": media17_engine_media_mode,
       "media18": media18,
       "media19": media19,
       "media20": media20,
       "media21": media21,
       "media22": media22,
       "media23": media23,
       "media24": media24,
       "media25": media25,
       "media26": media26,
       "media27": media27,
       "media28": media28,
       "media29": media29,
       "media30": media30,
       "media31": media31,
       "media32": media32,
       "media33": media33,
       "media34": media34,
       "media35": media35,
       "media36": media36,
       "media37": media37,
       "media38": media38,
       "media-modes": media_modes,
       "engine-media-modes-supported1": engine_media_modes_supported1,
       "media-size": media_size,
       "media-size-count": media_size_count,
       "media-size-west-edge-first-side-offset": media_size_west_edge_first_side_offset,
       "media-size-west-edge-second-side-offset": media_size_west_edge_second_side_offset,
       "media-mode-details": media_mode_details,
       "media-mode1": media_mode1,
       "engine-media-mode1-page-count": engine_media_mode1_page_count,
       "media-mode2": media_mode2,
       "engine-media-mode2-page-count": engine_media_mode2_page_count,
       "media-mode3": media_mode3,
       "engine-media-mode3-page-count": engine_media_mode3_page_count,
       "media-mode4": media_mode4,
       "engine-media-mode4-page-count": engine_media_mode4_page_count,
       "media-mode5": media_mode5,
       "engine-media-mode5-page-count": engine_media_mode5_page_count,
       "media-counts": media_counts,
       "media-types": media_types,
       "media-number-of-type-supported": media_number_of_type_supported,
       "consumables": consumables,
       "consumables-1": consumables_1,
       "consumable-status": consumable_status,
       "consumables-status": consumables_status,
       "consumables-life": consumables_life,
       "consumable-life-usage-units-remaining": consumable_life_usage_units_remaining,
       "consumable-life-usage-units": consumable_life_usage_units,
       "consumable-life-low-threshold": consumable_life_low_threshold,
       "estimated-page-yield": estimated_page_yield,
       "estimated-page-yield-unit": estimated_page_yield_unit,
       "supplies-at-very-low-delay-limit": supplies_at_very_low_delay_limit,
       "supplies-at-very-low-delay": supplies_at_very_low_delay,
       "consumable-current-state": consumable_current_state,
       "consumable-string": consumable_string,
       "device-used-while-cartridge-out-override-active": device_used_while_cartridge_out_override_active,
       "consumable-pages-printed-with-supply": consumable_pages_printed_with_supply,
       "total-kilo-pixels-per-cartridge": total_kilo_pixels_per_cartridge,
       "consumable-replacement-count": consumable_replacement_count,
       "consumable-pages-since-replacement": consumable_pages_since_replacement,
       "print-meter": print_meter,
       "printer-average": printer_average,
       "printer-average-marking-agent-units-per-gram": printer_average_marking_agent_units_per_gram,
       "printer-average-marking-agent-coverage-actual": printer_average_marking_agent_coverage_actual,
       "menus": menus,
       "media-sizes": media_sizes,
       "media-size-supported-driver-n-string": media_size_supported_driver_n_string,
       "fax-send": fax_send,
       "settings-fax-send": settings_fax_send,
       "fax-resolution": fax_resolution,
       "fax-contrast": fax_contrast,
       "fax-pixel-data-type": fax_pixel_data_type,
       "status-fax-send": status_fax_send,
       "not-ready-fax-send": not_ready_fax_send,
       "transmit-fax": transmit_fax,
       "fax-allow-redials": fax_allow_redials,
       "channel": channel,
       "channelnumberofchannels": channelnumberofchannels,
       "channelprinteralert": channelprinteralert,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channeltype": channeltype,
       "channelprotocolversion": channelprotocolversion,
       "channelstate": channelstate,
       "channelifindex": channelifindex,
       "channelstatus": channelstatus,
       "channelinformation": channelinformation,
       "tables": tables,
       "channel-table": channel_table,
       "channel-entry": channel_entry,
       "channel-bytes-sent": channel_bytes_sent,
       "channel-bytes-received": channel_bytes_received,
       "channel-io-errors": channel_io_errors,
       "channel-jobs-received": channel_jobs_received,
       "channel-mio": channel_mio,
       "printmib": printmib,
       "prtGeneral": prtGeneral,
       "prtGeneralTable": prtGeneralTable,
       "prtGeneralEntry": prtGeneralEntry,
       "prtgeneralconfigchanges": prtgeneralconfigchanges,
       "prtgeneralcurrentlocalization": prtgeneralcurrentlocalization,
       "prtgeneralreset": prtgeneralreset,
       "prtgeneralcurrentoperator": prtgeneralcurrentoperator,
       "prtgeneralserviceperson": prtgeneralserviceperson,
       "prtinputdefaultindex": prtinputdefaultindex,
       "prtoutputdefaultindex": prtoutputdefaultindex,
       "prtmarkerdefaultindex": prtmarkerdefaultindex,
       "prtmediapathdefaultindex": prtmediapathdefaultindex,
       "prtconsolelocalization": prtconsolelocalization,
       "prtconsolenumberofdisplaylines": prtconsolenumberofdisplaylines,
       "prtconsolenumberofdisplaychars": prtconsolenumberofdisplaychars,
       "prtconsoledisable": prtconsoledisable,
       "prtgeneralstartuppage": prtgeneralstartuppage,
       "prtgeneralbannerpage": prtgeneralbannerpage,
       "prtgeneralprintername": prtgeneralprintername,
       "prtgeneralserialnumber": prtgeneralserialnumber,
       "prtalertcriticalevents": prtalertcriticalevents,
       "prtalertallevents": prtalertallevents,
       "prtStorageRefTable": prtStorageRefTable,
       "prtStorageRefEntry": prtStorageRefEntry,
       "prtstoragerefindex": prtstoragerefindex,
       "prtDeviceRefTable": prtDeviceRefTable,
       "prtDeviceRefEntry": prtDeviceRefEntry,
       "prtdevicerefindex": prtdevicerefindex,
       "prtCover": prtCover,
       "prtCoverTable": prtCoverTable,
       "prtCoverEntry": prtCoverEntry,
       "prtcoverdescription": prtcoverdescription,
       "prtcoverstatus": prtcoverstatus,
       "prtLocalization": prtLocalization,
       "prtLocalizationTable": prtLocalizationTable,
       "prtLocalizationEntry": prtLocalizationEntry,
       "prtlocalizationlanguage": prtlocalizationlanguage,
       "prtlocalizationcountry": prtlocalizationcountry,
       "prtlocalizationcharacterset": prtlocalizationcharacterset,
       "prtInput": prtInput,
       "prtInputTable": prtInputTable,
       "prtInputEntry": prtInputEntry,
       "prtinputtype": prtinputtype,
       "prtinputdimunit": prtinputdimunit,
       "prtinputmediadimfeeddirdeclared": prtinputmediadimfeeddirdeclared,
       "prtinputmediadimxfeeddirdeclared": prtinputmediadimxfeeddirdeclared,
       "prtinputmediadimfeeddirchosen": prtinputmediadimfeeddirchosen,
       "prtinputmediadimxfeeddirchosen": prtinputmediadimxfeeddirchosen,
       "prtinputcapacityunit": prtinputcapacityunit,
       "prtinputmaxcapacity": prtinputmaxcapacity,
       "prtinputcurrentlevel": prtinputcurrentlevel,
       "prtinputstatus": prtinputstatus,
       "prtinputmedianame": prtinputmedianame,
       "prtinputname": prtinputname,
       "prtinputvendorname": prtinputvendorname,
       "prtinputmodel": prtinputmodel,
       "prtinputversion": prtinputversion,
       "prtinputserialnumber": prtinputserialnumber,
       "prtinputdescription": prtinputdescription,
       "prtinputsecurity": prtinputsecurity,
       "prtinputmedialoadtimeout": prtinputmedialoadtimeout,
       "prtinputnextindex": prtinputnextindex,
       "prtOutput": prtOutput,
       "prtOutputTable": prtOutputTable,
       "prtOutputEntry": prtOutputEntry,
       "prtoutputtype": prtoutputtype,
       "prtoutputcapacityunit": prtoutputcapacityunit,
       "prtoutputmaxcapacity": prtoutputmaxcapacity,
       "prtoutputremainingcapacity": prtoutputremainingcapacity,
       "prtoutputstatus": prtoutputstatus,
       "prtoutputname": prtoutputname,
       "prtoutputvendorname": prtoutputvendorname,
       "prtoutputmodel": prtoutputmodel,
       "prtoutputversion": prtoutputversion,
       "prtoutputserialnumber": prtoutputserialnumber,
       "prtoutputdescription": prtoutputdescription,
       "prtoutputsecurity": prtoutputsecurity,
       "prtoutputdimunit": prtoutputdimunit,
       "prtoutputmaxdimfeeddir": prtoutputmaxdimfeeddir,
       "prtoutputmaxdimxfeeddir": prtoutputmaxdimxfeeddir,
       "prtoutputmindimfeeddir": prtoutputmindimfeeddir,
       "prtoutputmindimxfeeddir": prtoutputmindimxfeeddir,
       "prtoutputstackingorder": prtoutputstackingorder,
       "prtoutputpagedeliveryorientation": prtoutputpagedeliveryorientation,
       "prtoutputbursting": prtoutputbursting,
       "prtoutputdecollating": prtoutputdecollating,
       "prtoutputpagecollated": prtoutputpagecollated,
       "prtoutputoffsetstacking": prtoutputoffsetstacking,
       "prtMarker": prtMarker,
       "prtMarkerTable": prtMarkerTable,
       "prtMarkerEntry": prtMarkerEntry,
       "prtmarkermarktech": prtmarkermarktech,
       "prtmarkercounterunit": prtmarkercounterunit,
       "prtmarkerlifecount": prtmarkerlifecount,
       "prtmarkerpoweroncount": prtmarkerpoweroncount,
       "prtmarkerprocesscolorants": prtmarkerprocesscolorants,
       "prtmarkerspotcolorants": prtmarkerspotcolorants,
       "prtmarkeraddressabilityunit": prtmarkeraddressabilityunit,
       "prtmarkeraddressabilityfeeddir": prtmarkeraddressabilityfeeddir,
       "prtmarkeraddressabilityxfeeddir": prtmarkeraddressabilityxfeeddir,
       "prtmarkernorthmargin": prtmarkernorthmargin,
       "prtmarkersouthmargin": prtmarkersouthmargin,
       "prtmarkerwestmargin": prtmarkerwestmargin,
       "prtmarkereastmargin": prtmarkereastmargin,
       "prtmarkerstatus": prtmarkerstatus,
       "prtMarkerSupplies": prtMarkerSupplies,
       "prtMarkerSuppliesTable": prtMarkerSuppliesTable,
       "prtMarkerSuppliesEntry": prtMarkerSuppliesEntry,
       "prtmarkersuppliesmarkerindex": prtmarkersuppliesmarkerindex,
       "prtmarkersuppliescolorantindex": prtmarkersuppliescolorantindex,
       "prtmarkersuppliesclass": prtmarkersuppliesclass,
       "prtmarkersuppliestype": prtmarkersuppliestype,
       "prtmarkersuppliesdescription": prtmarkersuppliesdescription,
       "prtmarkersuppliessupplyunit": prtmarkersuppliessupplyunit,
       "prtmarkersuppliesmaxcapacity": prtmarkersuppliesmaxcapacity,
       "prtmarkersupplieslevel": prtmarkersupplieslevel,
       "prtMarkerColorant": prtMarkerColorant,
       "prtMarkerColorantTable": prtMarkerColorantTable,
       "prtMarkerColorantEntry": prtMarkerColorantEntry,
       "prtmarkercolorantmarkerindex": prtmarkercolorantmarkerindex,
       "prtmarkercolorantrole": prtmarkercolorantrole,
       "prtmarkercolorantvalue": prtmarkercolorantvalue,
       "prtmarkercoloranttonality": prtmarkercoloranttonality,
       "prtMediaPath": prtMediaPath,
       "prtMediaPathTable": prtMediaPathTable,
       "prtMediaPathEntry": prtMediaPathEntry,
       "prtmediapathmaxspeedprintunit": prtmediapathmaxspeedprintunit,
       "prtmediapathmediasizeunit": prtmediapathmediasizeunit,
       "prtmediapathmaxspeed": prtmediapathmaxspeed,
       "prtmediapathmaxmediafeeddir": prtmediapathmaxmediafeeddir,
       "prtmediapathmaxmediaxfeeddir": prtmediapathmaxmediaxfeeddir,
       "prtmediapathminmediafeeddir": prtmediapathminmediafeeddir,
       "prtmediapathminmediaxfeeddir": prtmediapathminmediaxfeeddir,
       "prtmediapathtype": prtmediapathtype,
       "prtmediapathdescription": prtmediapathdescription,
       "prtmediapathstatus": prtmediapathstatus,
       "prtChannel": prtChannel,
       "prtChannelTable": prtChannelTable,
       "prtChannelEntry": prtChannelEntry,
       "prtchanneltype": prtchanneltype,
       "prtchannelprotocolversion": prtchannelprotocolversion,
       "prtchannelcurrentjobcntllangindex": prtchannelcurrentjobcntllangindex,
       "prtchanneldefaultpagedesclangindex": prtchanneldefaultpagedesclangindex,
       "prtchannelstate": prtchannelstate,
       "prtchannelifindex": prtchannelifindex,
       "prtchannelstatus": prtchannelstatus,
       "prtchannelinformation": prtchannelinformation,
       "prtInterpreter": prtInterpreter,
       "prtInterpreterTable": prtInterpreterTable,
       "prtInterpreterEntry": prtInterpreterEntry,
       "prtinterpreterlangfamily": prtinterpreterlangfamily,
       "prtinterpreterlanglevel": prtinterpreterlanglevel,
       "prtinterpreterlangversion": prtinterpreterlangversion,
       "prtinterpreterdescription": prtinterpreterdescription,
       "prtinterpreterversion": prtinterpreterversion,
       "prtinterpreterdefaultorientation": prtinterpreterdefaultorientation,
       "prtinterpreterfeedaddressability": prtinterpreterfeedaddressability,
       "prtinterpreterxfeedaddressability": prtinterpreterxfeedaddressability,
       "prtinterpreterdefaultcharsetin": prtinterpreterdefaultcharsetin,
       "prtinterpreterdefaultcharsetout": prtinterpreterdefaultcharsetout,
       "prtinterpretertwoway": prtinterpretertwoway,
       "prtConsoleDisplayBuffer": prtConsoleDisplayBuffer,
       "prtConsoleDisplayBufferTable": prtConsoleDisplayBufferTable,
       "prtConsoleDisplayBufferEntry": prtConsoleDisplayBufferEntry,
       "prtconsoledisplaybuffertext": prtconsoledisplaybuffertext,
       "prtConsoleLights": prtConsoleLights,
       "prtConsoleLightTable": prtConsoleLightTable,
       "prtConsoleLightEntry": prtConsoleLightEntry,
       "prtconsoleontime": prtconsoleontime,
       "prtconsoleofftime": prtconsoleofftime,
       "prtconsolecolor": prtconsolecolor,
       "prtconsoledescription": prtconsoledescription,
       "prtAlert": prtAlert,
       "prtAlertTable": prtAlertTable,
       "prtAlertEntry": prtAlertEntry,
       "prtalertseveritylevel": prtalertseveritylevel,
       "prtalerttraininglevel": prtalerttraininglevel,
       "prtalertgroup": prtalertgroup,
       "prtalertgroupindex": prtalertgroupindex,
       "prtalertlocation": prtalertlocation,
       "prtalertcode": prtalertcode,
       "prtalertdescription": prtalertdescription,
       "prtalerttime": prtalerttime,
       "hrm": hrm,
       "hrStorage": hrStorage,
       "hrmemorysize": hrmemorysize,
       "hrStorageTable": hrStorageTable,
       "hrStorageEntry": hrStorageEntry,
       "hrstorageindex": hrstorageindex,
       "hrstoragetype": hrstoragetype,
       "hrstoragedescr": hrstoragedescr,
       "hrstorageallocationunits": hrstorageallocationunits,
       "hrstoragesize": hrstoragesize,
       "hrstorageused": hrstorageused,
       "hrstorageallocationfailures": hrstorageallocationfailures,
       "hrDevice": hrDevice,
       "hrDeviceTable": hrDeviceTable,
       "hrDeviceEntry": hrDeviceEntry,
       "hrdeviceindex": hrdeviceindex,
       "hrdevicetype": hrdevicetype,
       "hrdevicedescr": hrdevicedescr,
       "hrdeviceid": hrdeviceid,
       "hrdevicestatus": hrdevicestatus,
       "hrdeviceerrors": hrdeviceerrors,
       "hrPrinterTable": hrPrinterTable,
       "hrPrinterEntry": hrPrinterEntry,
       "hrprinterstatus": hrprinterstatus,
       "hrprinterdetectederrorstate": hrprinterdetectederrorstate,
       "hrDiskStorageTable": hrDiskStorageTable,
       "hrDiskStorageEntry": hrDiskStorageEntry,
       "hrdiskstorageaccess": hrdiskstorageaccess,
       "hrdiskstoragemedia": hrdiskstoragemedia,
       "hrdiskstorageremoveble": hrdiskstorageremoveble,
       "hrdiskstoragecapacity": hrdiskstoragecapacity,
       "hrPartitionTable": hrPartitionTable,
       "hrPartitionEntry": hrPartitionEntry,
       "hrpartitionindex": hrpartitionindex,
       "hrpartitionlabel": hrpartitionlabel,
       "hrpartitionid": hrpartitionid,
       "hrpartitionsize": hrpartitionsize,
       "hrpartitionfsindex": hrpartitionfsindex,
       "hrFSTable": hrFSTable,
       "hrFSEntry": hrFSEntry,
       "hrfsindex": hrfsindex,
       "hrfsmountpoint": hrfsmountpoint,
       "hrfsremotemountpoint": hrfsremotemountpoint,
       "hrfstype": hrfstype,
       "hrfsaccess": hrfsaccess,
       "hrfsbootable": hrfsbootable,
       "hrfsstorageindex": hrfsstorageindex,
       "hrfslastfullbackupdate": hrfslastfullbackupdate,
       "hrfslastpartialbackupdate": hrfslastpartialbackupdate}
)
