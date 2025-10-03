# SNMP MIB module (SAF-MPMUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\saf\SAF-MPMUX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:24:54 2025
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Saf_ObjectIdentity = ObjectIdentity
saf = _Saf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571)
)
_Tehnika_ObjectIdentity = ObjectIdentity
tehnika = _Tehnika_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100)
)
_MicrowaveRadio_ObjectIdentity = ObjectIdentity
microwaveRadio = _MicrowaveRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1)
)
_PointToPoint_ObjectIdentity = ObjectIdentity
pointToPoint = _PointToPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1)
)
_Cfm22_ObjectIdentity = ObjectIdentity
cfm22 = _Cfm22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2)
)
_Mpmux_ObjectIdentity = ObjectIdentity
mpmux = _Mpmux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22)
)
_Terminal_ObjectIdentity = ObjectIdentity
terminal = _Terminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1)
)


class _TermProduct_Type(DisplayString):
    """Custom type termProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TermProduct_Type.__name__ = "DisplayString"
_TermProduct_Object = MibScalar
termProduct = _TermProduct_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 1),
    _TermProduct_Type()
)
termProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termProduct.setStatus("mandatory")


class _TermDescription_Type(DisplayString):
    """Custom type termDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TermDescription_Type.__name__ = "DisplayString"
_TermDescription_Object = MibScalar
termDescription = _TermDescription_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 2),
    _TermDescription_Type()
)
termDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termDescription.setStatus("mandatory")


class _TermLocation_Type(DisplayString):
    """Custom type termLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TermLocation_Type.__name__ = "DisplayString"
_TermLocation_Object = MibScalar
termLocation = _TermLocation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 3),
    _TermLocation_Type()
)
termLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termLocation.setStatus("mandatory")


class _TermVersion_Type(DisplayString):
    """Custom type termVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TermVersion_Type.__name__ = "DisplayString"
_TermVersion_Object = MibScalar
termVersion = _TermVersion_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 4),
    _TermVersion_Type()
)
termVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termVersion.setStatus("mandatory")


class _TermOperation_Type(Integer32):
    """Custom type termOperation based on Integer32"""
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
        *(("none", 0),
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("error", 4))
    )


_TermOperation_Type.__name__ = "Integer32"
_TermOperation_Object = MibScalar
termOperation = _TermOperation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 5),
    _TermOperation_Type()
)
termOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termOperation.setStatus("mandatory")


class _TermIduTemperature_Type(Integer32):
    """Custom type termIduTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TermIduTemperature_Type.__name__ = "Integer32"
_TermIduTemperature_Object = MibScalar
termIduTemperature = _TermIduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 6),
    _TermIduTemperature_Type()
)
termIduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termIduTemperature.setStatus("mandatory")
_TermFrameErrors_Type = Integer32
_TermFrameErrors_Object = MibScalar
termFrameErrors = _TermFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 10),
    _TermFrameErrors_Type()
)
termFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termFrameErrors.setStatus("mandatory")
_WriteConfig_Type = Integer32
_WriteConfig_Object = MibScalar
writeConfig = _WriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 11),
    _WriteConfig_Type()
)
writeConfig.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    writeConfig.setStatus("mandatory")
_RestartCPU_Type = Integer32
_RestartCPU_Object = MibScalar
restartCPU = _RestartCPU_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 12),
    _RestartCPU_Type()
)
restartCPU.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartCPU.setStatus("mandatory")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 13),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")


class _TermRf1CablePowerStatus_Type(Integer32):
    """Custom type termRf1CablePowerStatus based on Integer32"""
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
          ("ok", 1),
          ("short", 2),
          ("error", 3),
          ("power-off", 4))
    )


_TermRf1CablePowerStatus_Type.__name__ = "Integer32"
_TermRf1CablePowerStatus_Object = MibScalar
termRf1CablePowerStatus = _TermRf1CablePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 14),
    _TermRf1CablePowerStatus_Type()
)
termRf1CablePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRf1CablePowerStatus.setStatus("mandatory")


class _TermRf2CablePowerStatus_Type(Integer32):
    """Custom type termRf2CablePowerStatus based on Integer32"""
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
          ("ok", 1),
          ("short", 2),
          ("error", 3),
          ("power-off", 4))
    )


_TermRf2CablePowerStatus_Type.__name__ = "Integer32"
_TermRf2CablePowerStatus_Object = MibScalar
termRf2CablePowerStatus = _TermRf2CablePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 15),
    _TermRf2CablePowerStatus_Type()
)
termRf2CablePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRf2CablePowerStatus.setStatus("mandatory")


class _Power3V3PS1_Type(DisplayString):
    """Custom type power3V3PS1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Power3V3PS1_Type.__name__ = "DisplayString"
_Power3V3PS1_Object = MibScalar
power3V3PS1 = _Power3V3PS1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 16),
    _Power3V3PS1_Type()
)
power3V3PS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power3V3PS1.setStatus("mandatory")


class _Power5VPS1_Type(DisplayString):
    """Custom type power5VPS1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Power5VPS1_Type.__name__ = "DisplayString"
_Power5VPS1_Object = MibScalar
power5VPS1 = _Power5VPS1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 17),
    _Power5VPS1_Type()
)
power5VPS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power5VPS1.setStatus("mandatory")


class _PowerM5VPS1_Type(DisplayString):
    """Custom type powerM5VPS1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerM5VPS1_Type.__name__ = "DisplayString"
_PowerM5VPS1_Object = MibScalar
powerM5VPS1 = _PowerM5VPS1_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 18),
    _PowerM5VPS1_Type()
)
powerM5VPS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerM5VPS1.setStatus("mandatory")


class _PowerODU1V_Type(DisplayString):
    """Custom type powerODU1V based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerODU1V_Type.__name__ = "DisplayString"
_PowerODU1V_Object = MibScalar
powerODU1V = _PowerODU1V_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 19),
    _PowerODU1V_Type()
)
powerODU1V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerODU1V.setStatus("mandatory")


class _PowerODU1I_Type(DisplayString):
    """Custom type powerODU1I based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerODU1I_Type.__name__ = "DisplayString"
_PowerODU1I_Object = MibScalar
powerODU1I = _PowerODU1I_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 20),
    _PowerODU1I_Type()
)
powerODU1I.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerODU1I.setStatus("mandatory")


class _PowerODU1W_Type(DisplayString):
    """Custom type powerODU1W based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerODU1W_Type.__name__ = "DisplayString"
_PowerODU1W_Object = MibScalar
powerODU1W = _PowerODU1W_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 21),
    _PowerODU1W_Type()
)
powerODU1W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerODU1W.setStatus("mandatory")


class _Power3V3PS2_Type(DisplayString):
    """Custom type power3V3PS2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Power3V3PS2_Type.__name__ = "DisplayString"
_Power3V3PS2_Object = MibScalar
power3V3PS2 = _Power3V3PS2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 22),
    _Power3V3PS2_Type()
)
power3V3PS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power3V3PS2.setStatus("mandatory")


class _Power5VPS2_Type(DisplayString):
    """Custom type power5VPS2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Power5VPS2_Type.__name__ = "DisplayString"
_Power5VPS2_Object = MibScalar
power5VPS2 = _Power5VPS2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 23),
    _Power5VPS2_Type()
)
power5VPS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power5VPS2.setStatus("mandatory")


class _PowerM5VPS2_Type(DisplayString):
    """Custom type powerM5VPS2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerM5VPS2_Type.__name__ = "DisplayString"
_PowerM5VPS2_Object = MibScalar
powerM5VPS2 = _PowerM5VPS2_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 24),
    _PowerM5VPS2_Type()
)
powerM5VPS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerM5VPS2.setStatus("mandatory")


class _PowerODU2V_Type(DisplayString):
    """Custom type powerODU2V based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerODU2V_Type.__name__ = "DisplayString"
_PowerODU2V_Object = MibScalar
powerODU2V = _PowerODU2V_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 25),
    _PowerODU2V_Type()
)
powerODU2V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerODU2V.setStatus("mandatory")


class _PowerODU2I_Type(DisplayString):
    """Custom type powerODU2I based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerODU2I_Type.__name__ = "DisplayString"
_PowerODU2I_Object = MibScalar
powerODU2I = _PowerODU2I_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 26),
    _PowerODU2I_Type()
)
powerODU2I.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerODU2I.setStatus("mandatory")


class _PowerODU2W_Type(DisplayString):
    """Custom type powerODU2W based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PowerODU2W_Type.__name__ = "DisplayString"
_PowerODU2W_Object = MibScalar
powerODU2W = _PowerODU2W_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 27),
    _PowerODU2W_Type()
)
powerODU2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerODU2W.setStatus("mandatory")
_CpuUsage_Type = Integer32
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 28),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("mandatory")
_TermBFrameErr_Type = Counter32
_TermBFrameErr_Object = MibScalar
termBFrameErr = _TermBFrameErr_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 29),
    _TermBFrameErr_Type()
)
termBFrameErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termBFrameErr.setStatus("mandatory")
_TermStatCountTime_Type = Gauge32
_TermStatCountTime_Object = MibScalar
termStatCountTime = _TermStatCountTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 30),
    _TermStatCountTime_Type()
)
termStatCountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termStatCountTime.setStatus("mandatory")
_TermErroredSecond_Type = Gauge32
_TermErroredSecond_Object = MibScalar
termErroredSecond = _TermErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 31),
    _TermErroredSecond_Type()
)
termErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termErroredSecond.setStatus("mandatory")
_TermSeverelyErroredSecond_Type = Gauge32
_TermSeverelyErroredSecond_Object = MibScalar
termSeverelyErroredSecond = _TermSeverelyErroredSecond_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 32),
    _TermSeverelyErroredSecond_Type()
)
termSeverelyErroredSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termSeverelyErroredSecond.setStatus("mandatory")
_TermSyncLostTime_Type = Gauge32
_TermSyncLostTime_Object = MibScalar
termSyncLostTime = _TermSyncLostTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 33),
    _TermSyncLostTime_Type()
)
termSyncLostTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termSyncLostTime.setStatus("mandatory")
_TermAvailableTime_Type = Gauge32
_TermAvailableTime_Object = MibScalar
termAvailableTime = _TermAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 34),
    _TermAvailableTime_Type()
)
termAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termAvailableTime.setStatus("mandatory")
_TermUnAvailableTime_Type = Gauge32
_TermUnAvailableTime_Object = MibScalar
termUnAvailableTime = _TermUnAvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 35),
    _TermUnAvailableTime_Type()
)
termUnAvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termUnAvailableTime.setStatus("mandatory")


class _TermBer_Type(DisplayString):
    """Custom type termBer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TermBer_Type.__name__ = "DisplayString"
_TermBer_Object = MibScalar
termBer = _TermBer_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 36),
    _TermBer_Type()
)
termBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termBer.setStatus("mandatory")
_BerAlarm_Type = Integer32
_BerAlarm_Object = MibScalar
berAlarm = _BerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 37),
    _BerAlarm_Type()
)
berAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    berAlarm.setStatus("mandatory")
_RemoteAlarm_Type = Integer32
_RemoteAlarm_Object = MibScalar
remoteAlarm = _RemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 38),
    _RemoteAlarm_Type()
)
remoteAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlarm.setStatus("mandatory")
_SystemAlarm_Type = Integer32
_SystemAlarm_Object = MibScalar
systemAlarm = _SystemAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 39),
    _SystemAlarm_Type()
)
systemAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarm.setStatus("mandatory")
_InputABCD_Type = Integer32
_InputABCD_Object = MibScalar
inputABCD = _InputABCD_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 40),
    _InputABCD_Type()
)
inputABCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputABCD.setStatus("mandatory")
_OutputABCD_Type = Integer32
_OutputABCD_Object = MibScalar
outputABCD = _OutputABCD_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 41),
    _OutputABCD_Type()
)
outputABCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputABCD.setStatus("mandatory")
_TermBerInPwOf10_Type = Integer32
_TermBerInPwOf10_Object = MibScalar
termBerInPwOf10 = _TermBerInPwOf10_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 42),
    _TermBerInPwOf10_Type()
)
termBerInPwOf10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termBerInPwOf10.setStatus("optional")
_OutputMaskABCD_Type = Integer32
_OutputMaskABCD_Object = MibScalar
outputMaskABCD = _OutputMaskABCD_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 1, 43),
    _OutputMaskABCD_Type()
)
outputMaskABCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputMaskABCD.setStatus("mandatory")
_Baseband_ObjectIdentity = ObjectIdentity
baseband = _Baseband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 2)
)


class _BbVersion_Type(DisplayString):
    """Custom type bbVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BbVersion_Type.__name__ = "DisplayString"
_BbVersion_Object = MibScalar
bbVersion = _BbVersion_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 2, 1),
    _BbVersion_Type()
)
bbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbVersion.setStatus("mandatory")


class _BbOperation_Type(Integer32):
    """Custom type bbOperation based on Integer32"""
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
        *(("none", 0),
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("loopback", 4),
          ("illegalSpeed", 5),
          ("error", 6))
    )


_BbOperation_Type.__name__ = "Integer32"
_BbOperation_Object = MibScalar
bbOperation = _BbOperation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 2, 2),
    _BbOperation_Type()
)
bbOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbOperation.setStatus("mandatory")
_BbLinkCapacity_Type = Integer32
_BbLinkCapacity_Object = MibScalar
bbLinkCapacity = _BbLinkCapacity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 2, 3),
    _BbLinkCapacity_Type()
)
bbLinkCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbLinkCapacity.setStatus("mandatory")


class _BbLinkCapacityDescription_Type(DisplayString):
    """Custom type bbLinkCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BbLinkCapacityDescription_Type.__name__ = "DisplayString"
_BbLinkCapacityDescription_Object = MibScalar
bbLinkCapacityDescription = _BbLinkCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 2, 4),
    _BbLinkCapacityDescription_Type()
)
bbLinkCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbLinkCapacityDescription.setStatus("mandatory")


class _BbLoopback_Type(Integer32):
    """Custom type bbLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("digital", 1),
          ("analog", 2))
    )


_BbLoopback_Type.__name__ = "Integer32"
_BbLoopback_Object = MibScalar
bbLoopback = _BbLoopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 2, 5),
    _BbLoopback_Type()
)
bbLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bbLoopback.setStatus("mandatory")


class _BbSyncLostAlarm_Type(Integer32):
    """Custom type bbSyncLostAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("on", 1))
    )


_BbSyncLostAlarm_Type.__name__ = "Integer32"
_BbSyncLostAlarm_Object = MibScalar
bbSyncLostAlarm = _BbSyncLostAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 2, 6),
    _BbSyncLostAlarm_Type()
)
bbSyncLostAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bbSyncLostAlarm.setStatus("mandatory")
_Radio1_ObjectIdentity = ObjectIdentity
radio1 = _Radio1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3)
)


class _Rf1Operation_Type(Integer32):
    """Custom type rf1Operation based on Integer32"""
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
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("error", 4),
          ("noDataFromODU", 5))
    )


_Rf1Operation_Type.__name__ = "Integer32"
_Rf1Operation_Object = MibScalar
rf1Operation = _Rf1Operation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 1),
    _Rf1Operation_Type()
)
rf1Operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1Operation.setStatus("mandatory")


class _Rf1Alarm_Type(Integer32):
    """Custom type rf1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("on", 1))
    )


_Rf1Alarm_Type.__name__ = "Integer32"
_Rf1Alarm_Object = MibScalar
rf1Alarm = _Rf1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 2),
    _Rf1Alarm_Type()
)
rf1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1Alarm.setStatus("mandatory")


class _Rf1Version_Type(DisplayString):
    """Custom type rf1Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rf1Version_Type.__name__ = "DisplayString"
_Rf1Version_Object = MibScalar
rf1Version = _Rf1Version_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 3),
    _Rf1Version_Type()
)
rf1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1Version.setStatus("mandatory")


class _Rf1Side_Type(Integer32):
    """Custom type rf1Side based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_Rf1Side_Type.__name__ = "Integer32"
_Rf1Side_Object = MibScalar
rf1Side = _Rf1Side_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 4),
    _Rf1Side_Type()
)
rf1Side.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1Side.setStatus("mandatory")
_Rf1Channel_Type = Integer32
_Rf1Channel_Object = MibScalar
rf1Channel = _Rf1Channel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 5),
    _Rf1Channel_Type()
)
rf1Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf1Channel.setStatus("mandatory")


class _Rf1TxFrequency_Type(DisplayString):
    """Custom type rf1TxFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rf1TxFrequency_Type.__name__ = "DisplayString"
_Rf1TxFrequency_Object = MibScalar
rf1TxFrequency = _Rf1TxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 6),
    _Rf1TxFrequency_Type()
)
rf1TxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1TxFrequency.setStatus("mandatory")


class _Rf1RxFrequency_Type(DisplayString):
    """Custom type rf1RxFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rf1RxFrequency_Type.__name__ = "DisplayString"
_Rf1RxFrequency_Object = MibScalar
rf1RxFrequency = _Rf1RxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 7),
    _Rf1RxFrequency_Type()
)
rf1RxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1RxFrequency.setStatus("mandatory")
_Rf1TxPower_Type = Integer32
_Rf1TxPower_Object = MibScalar
rf1TxPower = _Rf1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 8),
    _Rf1TxPower_Type()
)
rf1TxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf1TxPower.setStatus("mandatory")


class _Rf1RxState_Type(Integer32):
    """Custom type rf1RxState based on Integer32"""
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
        *(("low", 0),
          ("ok", 1),
          ("error", 2),
          ("loopback", 3))
    )


_Rf1RxState_Type.__name__ = "Integer32"
_Rf1RxState_Object = MibScalar
rf1RxState = _Rf1RxState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 9),
    _Rf1RxState_Type()
)
rf1RxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1RxState.setStatus("mandatory")
_Rf1RxLevel_Type = Integer32
_Rf1RxLevel_Object = MibScalar
rf1RxLevel = _Rf1RxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 10),
    _Rf1RxLevel_Type()
)
rf1RxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1RxLevel.setStatus("mandatory")
_Rf1CableAttenuation_Type = Integer32
_Rf1CableAttenuation_Object = MibScalar
rf1CableAttenuation = _Rf1CableAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 11),
    _Rf1CableAttenuation_Type()
)
rf1CableAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1CableAttenuation.setStatus("mandatory")


class _Rf1TxOut_Type(Integer32):
    """Custom type rf1TxOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1),
          ("off", 2))
    )


_Rf1TxOut_Type.__name__ = "Integer32"
_Rf1TxOut_Object = MibScalar
rf1TxOut = _Rf1TxOut_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 12),
    _Rf1TxOut_Type()
)
rf1TxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1TxOut.setStatus("mandatory")


class _Rf1TxPLL_Type(Integer32):
    """Custom type rf1TxPLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1))
    )


_Rf1TxPLL_Type.__name__ = "Integer32"
_Rf1TxPLL_Object = MibScalar
rf1TxPLL = _Rf1TxPLL_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 13),
    _Rf1TxPLL_Type()
)
rf1TxPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1TxPLL.setStatus("mandatory")


class _Rf1RxPLL_Type(Integer32):
    """Custom type rf1RxPLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1))
    )


_Rf1RxPLL_Type.__name__ = "Integer32"
_Rf1RxPLL_Object = MibScalar
rf1RxPLL = _Rf1RxPLL_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 14),
    _Rf1RxPLL_Type()
)
rf1RxPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1RxPLL.setStatus("mandatory")
_Rf1OduTemperature_Type = Integer32
_Rf1OduTemperature_Object = MibScalar
rf1OduTemperature = _Rf1OduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 15),
    _Rf1OduTemperature_Type()
)
rf1OduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1OduTemperature.setStatus("mandatory")


class _Rf1OduHumidity_Type(Integer32):
    """Custom type rf1OduHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_Rf1OduHumidity_Type.__name__ = "Integer32"
_Rf1OduHumidity_Object = MibScalar
rf1OduHumidity = _Rf1OduHumidity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 16),
    _Rf1OduHumidity_Type()
)
rf1OduHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1OduHumidity.setStatus("mandatory")


class _Rf1Loopback_Type(Integer32):
    """Custom type rf1Loopback based on Integer32"""
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


_Rf1Loopback_Type.__name__ = "Integer32"
_Rf1Loopback_Object = MibScalar
rf1Loopback = _Rf1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 17),
    _Rf1Loopback_Type()
)
rf1Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf1Loopback.setStatus("mandatory")
_Rf1RxAlarmLevel_Type = Integer32
_Rf1RxAlarmLevel_Object = MibScalar
rf1RxAlarmLevel = _Rf1RxAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 18),
    _Rf1RxAlarmLevel_Type()
)
rf1RxAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf1RxAlarmLevel.setStatus("mandatory")
_Rf1txfstart_Type = Integer32
_Rf1txfstart_Object = MibScalar
rf1txfstart = _Rf1txfstart_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 19),
    _Rf1txfstart_Type()
)
rf1txfstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1txfstart.setStatus("optional")
_Rf1duplexshift_Type = Integer32
_Rf1duplexshift_Object = MibScalar
rf1duplexshift = _Rf1duplexshift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 20),
    _Rf1duplexshift_Type()
)
rf1duplexshift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1duplexshift.setStatus("optional")
_Rf1chstep_Type = Integer32
_Rf1chstep_Object = MibScalar
rf1chstep = _Rf1chstep_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 21),
    _Rf1chstep_Type()
)
rf1chstep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1chstep.setStatus("optional")
_Rf1chstart_Type = Integer32
_Rf1chstart_Object = MibScalar
rf1chstart = _Rf1chstart_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 22),
    _Rf1chstart_Type()
)
rf1chstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1chstart.setStatus("optional")
_Rf1chend_Type = Integer32
_Rf1chend_Object = MibScalar
rf1chend = _Rf1chend_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 23),
    _Rf1chend_Type()
)
rf1chend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1chend.setStatus("optional")
_Rf1txpwmin_Type = Integer32
_Rf1txpwmin_Object = MibScalar
rf1txpwmin = _Rf1txpwmin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 24),
    _Rf1txpwmin_Type()
)
rf1txpwmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1txpwmin.setStatus("optional")
_Rf1txpwmax_Type = Integer32
_Rf1txpwmax_Object = MibScalar
rf1txpwmax = _Rf1txpwmax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 25),
    _Rf1txpwmax_Type()
)
rf1txpwmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1txpwmax.setStatus("optional")
_Rf1txpwstep_Type = Integer32
_Rf1txpwstep_Object = MibScalar
rf1txpwstep = _Rf1txpwstep_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 3, 26),
    _Rf1txpwstep_Type()
)
rf1txpwstep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf1txpwstep.setStatus("optional")
_Radio2_ObjectIdentity = ObjectIdentity
radio2 = _Radio2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4)
)


class _Rf2Operation_Type(Integer32):
    """Custom type rf2Operation based on Integer32"""
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
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("error", 4),
          ("noDataFromODU", 5))
    )


_Rf2Operation_Type.__name__ = "Integer32"
_Rf2Operation_Object = MibScalar
rf2Operation = _Rf2Operation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 1),
    _Rf2Operation_Type()
)
rf2Operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2Operation.setStatus("mandatory")


class _Rf2Alarm_Type(Integer32):
    """Custom type rf2Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("on", 1))
    )


_Rf2Alarm_Type.__name__ = "Integer32"
_Rf2Alarm_Object = MibScalar
rf2Alarm = _Rf2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 2),
    _Rf2Alarm_Type()
)
rf2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2Alarm.setStatus("optional")


class _Rf2Version_Type(DisplayString):
    """Custom type rf2Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rf2Version_Type.__name__ = "DisplayString"
_Rf2Version_Object = MibScalar
rf2Version = _Rf2Version_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 3),
    _Rf2Version_Type()
)
rf2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2Version.setStatus("mandatory")


class _Rf2Side_Type(Integer32):
    """Custom type rf2Side based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_Rf2Side_Type.__name__ = "Integer32"
_Rf2Side_Object = MibScalar
rf2Side = _Rf2Side_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 4),
    _Rf2Side_Type()
)
rf2Side.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2Side.setStatus("mandatory")
_Rf2Channel_Type = Integer32
_Rf2Channel_Object = MibScalar
rf2Channel = _Rf2Channel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 5),
    _Rf2Channel_Type()
)
rf2Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf2Channel.setStatus("mandatory")


class _Rf2TxFrequency_Type(DisplayString):
    """Custom type rf2TxFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rf2TxFrequency_Type.__name__ = "DisplayString"
_Rf2TxFrequency_Object = MibScalar
rf2TxFrequency = _Rf2TxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 6),
    _Rf2TxFrequency_Type()
)
rf2TxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2TxFrequency.setStatus("mandatory")


class _Rf2RxFrequency_Type(DisplayString):
    """Custom type rf2RxFrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rf2RxFrequency_Type.__name__ = "DisplayString"
_Rf2RxFrequency_Object = MibScalar
rf2RxFrequency = _Rf2RxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 7),
    _Rf2RxFrequency_Type()
)
rf2RxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2RxFrequency.setStatus("mandatory")
_Rf2TxPower_Type = Integer32
_Rf2TxPower_Object = MibScalar
rf2TxPower = _Rf2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 8),
    _Rf2TxPower_Type()
)
rf2TxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf2TxPower.setStatus("mandatory")


class _Rf2RxState_Type(Integer32):
    """Custom type rf2RxState based on Integer32"""
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
        *(("low", 0),
          ("ok", 1),
          ("error", 2),
          ("loopback", 3))
    )


_Rf2RxState_Type.__name__ = "Integer32"
_Rf2RxState_Object = MibScalar
rf2RxState = _Rf2RxState_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 9),
    _Rf2RxState_Type()
)
rf2RxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2RxState.setStatus("mandatory")
_Rf2RxLevel_Type = Integer32
_Rf2RxLevel_Object = MibScalar
rf2RxLevel = _Rf2RxLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 10),
    _Rf2RxLevel_Type()
)
rf2RxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2RxLevel.setStatus("mandatory")
_Rf2CableAttenuation_Type = Integer32
_Rf2CableAttenuation_Object = MibScalar
rf2CableAttenuation = _Rf2CableAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 11),
    _Rf2CableAttenuation_Type()
)
rf2CableAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2CableAttenuation.setStatus("mandatory")


class _Rf2TxOut_Type(Integer32):
    """Custom type rf2TxOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1),
          ("off", 2))
    )


_Rf2TxOut_Type.__name__ = "Integer32"
_Rf2TxOut_Object = MibScalar
rf2TxOut = _Rf2TxOut_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 12),
    _Rf2TxOut_Type()
)
rf2TxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2TxOut.setStatus("mandatory")


class _Rf2TxPLL_Type(Integer32):
    """Custom type rf2TxPLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1))
    )


_Rf2TxPLL_Type.__name__ = "Integer32"
_Rf2TxPLL_Object = MibScalar
rf2TxPLL = _Rf2TxPLL_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 13),
    _Rf2TxPLL_Type()
)
rf2TxPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2TxPLL.setStatus("mandatory")


class _Rf2RxPLL_Type(Integer32):
    """Custom type rf2RxPLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1))
    )


_Rf2RxPLL_Type.__name__ = "Integer32"
_Rf2RxPLL_Object = MibScalar
rf2RxPLL = _Rf2RxPLL_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 14),
    _Rf2RxPLL_Type()
)
rf2RxPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2RxPLL.setStatus("mandatory")
_Rf2OduTemperature_Type = Integer32
_Rf2OduTemperature_Object = MibScalar
rf2OduTemperature = _Rf2OduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 15),
    _Rf2OduTemperature_Type()
)
rf2OduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2OduTemperature.setStatus("mandatory")


class _Rf2OduHumidity_Type(Integer32):
    """Custom type rf2OduHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_Rf2OduHumidity_Type.__name__ = "Integer32"
_Rf2OduHumidity_Object = MibScalar
rf2OduHumidity = _Rf2OduHumidity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 16),
    _Rf2OduHumidity_Type()
)
rf2OduHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2OduHumidity.setStatus("mandatory")


class _Rf2Loopback_Type(Integer32):
    """Custom type rf2Loopback based on Integer32"""
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


_Rf2Loopback_Type.__name__ = "Integer32"
_Rf2Loopback_Object = MibScalar
rf2Loopback = _Rf2Loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 17),
    _Rf2Loopback_Type()
)
rf2Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf2Loopback.setStatus("mandatory")
_Rf2RxAlarmLevel_Type = Integer32
_Rf2RxAlarmLevel_Object = MibScalar
rf2RxAlarmLevel = _Rf2RxAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 18),
    _Rf2RxAlarmLevel_Type()
)
rf2RxAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rf2RxAlarmLevel.setStatus("mandatory")
_Rf2txfstart_Type = Integer32
_Rf2txfstart_Object = MibScalar
rf2txfstart = _Rf2txfstart_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 19),
    _Rf2txfstart_Type()
)
rf2txfstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2txfstart.setStatus("optional")
_Rf2duplexshift_Type = Integer32
_Rf2duplexshift_Object = MibScalar
rf2duplexshift = _Rf2duplexshift_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 20),
    _Rf2duplexshift_Type()
)
rf2duplexshift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2duplexshift.setStatus("optional")
_Rf2chstep_Type = Integer32
_Rf2chstep_Object = MibScalar
rf2chstep = _Rf2chstep_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 21),
    _Rf2chstep_Type()
)
rf2chstep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2chstep.setStatus("optional")
_Rf2chstart_Type = Integer32
_Rf2chstart_Object = MibScalar
rf2chstart = _Rf2chstart_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 22),
    _Rf2chstart_Type()
)
rf2chstart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2chstart.setStatus("optional")
_Rf2chend_Type = Integer32
_Rf2chend_Object = MibScalar
rf2chend = _Rf2chend_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 23),
    _Rf2chend_Type()
)
rf2chend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2chend.setStatus("optional")
_Rf2txpwmin_Type = Integer32
_Rf2txpwmin_Object = MibScalar
rf2txpwmin = _Rf2txpwmin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 24),
    _Rf2txpwmin_Type()
)
rf2txpwmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2txpwmin.setStatus("optional")
_Rf2txpwmax_Type = Integer32
_Rf2txpwmax_Object = MibScalar
rf2txpwmax = _Rf2txpwmax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 25),
    _Rf2txpwmax_Type()
)
rf2txpwmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2txpwmax.setStatus("optional")
_Rf2txpwstep_Type = Integer32
_Rf2txpwstep_Object = MibScalar
rf2txpwstep = _Rf2txpwstep_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 4, 26),
    _Rf2txpwstep_Type()
)
rf2txpwstep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rf2txpwstep.setStatus("optional")
_SwitchCtrl_ObjectIdentity = ObjectIdentity
switchCtrl = _SwitchCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5)
)


class _ActiveLink_Type(Integer32):
    """Custom type activeLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("link1", 1),
          ("link2", 2),
          ("error", 255))
    )


_ActiveLink_Type.__name__ = "Integer32"
_ActiveLink_Object = MibScalar
activeLink = _ActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 1),
    _ActiveLink_Type()
)
activeLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeLink.setStatus("mandatory")


class _ActiveTx_Type(Integer32):
    """Custom type activeTx based on Integer32"""
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
          ("link1", 1),
          ("link2", 2),
          ("both", 3))
    )


_ActiveTx_Type.__name__ = "Integer32"
_ActiveTx_Object = MibScalar
activeTx = _ActiveTx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 2),
    _ActiveTx_Type()
)
activeTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeTx.setStatus("mandatory")


class _PreferedLink_Type(Integer32):
    """Custom type preferedLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("link1", 1),
          ("link2", 2),
          ("error", 255))
    )


_PreferedLink_Type.__name__ = "Integer32"
_PreferedLink_Object = MibScalar
preferedLink = _PreferedLink_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 3),
    _PreferedLink_Type()
)
preferedLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferedLink.setStatus("optional")


class _ForcedLink_Type(Integer32):
    """Custom type forcedLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("link1", 1),
          ("link2", 2),
          ("error", 255))
    )


_ForcedLink_Type.__name__ = "Integer32"
_ForcedLink_Object = MibScalar
forcedLink = _ForcedLink_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 4),
    _ForcedLink_Type()
)
forcedLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forcedLink.setStatus("mandatory")


class _SwitchMode_Type(Integer32):
    """Custom type switchMode based on Integer32"""
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
        *(("unknown", 0),
          ("freqDiv", 1),
          ("hotStandby", 2),
          ("independent", 3))
    )


_SwitchMode_Type.__name__ = "Integer32"
_SwitchMode_Object = MibScalar
switchMode = _SwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 5),
    _SwitchMode_Type()
)
switchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchMode.setStatus("mandatory")
_Odu1RxMax_Type = Integer32
_Odu1RxMax_Object = MibScalar
odu1RxMax = _Odu1RxMax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 6),
    _Odu1RxMax_Type()
)
odu1RxMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    odu1RxMax.setStatus("mandatory")
_Odu2RxMax_Type = Integer32
_Odu2RxMax_Object = MibScalar
odu2RxMax = _Odu2RxMax_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 7),
    _Odu2RxMax_Type()
)
odu2RxMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    odu2RxMax.setStatus("mandatory")
_Odu1RxMin_Type = Integer32
_Odu1RxMin_Object = MibScalar
odu1RxMin = _Odu1RxMin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 8),
    _Odu1RxMin_Type()
)
odu1RxMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    odu1RxMin.setStatus("mandatory")
_Odu2RxMin_Type = Integer32
_Odu2RxMin_Object = MibScalar
odu2RxMin = _Odu2RxMin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 9),
    _Odu2RxMin_Type()
)
odu2RxMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    odu2RxMin.setStatus("mandatory")
_RxDelta_Type = Integer32
_RxDelta_Object = MibScalar
rxDelta = _RxDelta_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 10),
    _RxDelta_Type()
)
rxDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxDelta.setStatus("mandatory")


class _RxBER_Type(DisplayString):
    """Custom type rxBER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RxBER_Type.__name__ = "DisplayString"
_RxBER_Object = MibScalar
rxBER = _RxBER_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 11),
    _RxBER_Type()
)
rxBER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rxBER.setStatus("mandatory")
_SwitchDelay_Type = Integer32
_SwitchDelay_Object = MibScalar
switchDelay = _SwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 12),
    _SwitchDelay_Type()
)
switchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchDelay.setStatus("mandatory")


class _SwitchEnabledForRxBer_Type(Integer32):
    """Custom type switchEnabledForRxBer based on Integer32"""
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


_SwitchEnabledForRxBer_Type.__name__ = "Integer32"
_SwitchEnabledForRxBer_Object = MibScalar
switchEnabledForRxBer = _SwitchEnabledForRxBer_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 13),
    _SwitchEnabledForRxBer_Type()
)
switchEnabledForRxBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEnabledForRxBer.setStatus("mandatory")
_SwitchReason_Type = Integer32
_SwitchReason_Object = MibScalar
switchReason = _SwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 5, 14),
    _SwitchReason_Type()
)
switchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchReason.setStatus("mandatory")
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6)
)
_M1_ObjectIdentity = ObjectIdentity
m1 = _M1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1)
)


class _M1Type_Type(Integer32):
    """Custom type m1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              33,
              37,
              43,
              74,
              78,
              100,
              227,
              241,
              242,
              255)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("e1x1", 30),
          ("e1", 33),
          ("v35", 37),
          ("bridge", 43),
          ("t1x4", 74),
          ("e1x4", 78),
          ("eow64", 100),
          ("e3", 227),
          ("f1bridge", 241),
          ("f2bridge", 242),
          ("none", 255))
    )


_M1Type_Type.__name__ = "Integer32"
_M1Type_Object = MibScalar
m1Type = _M1Type_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 1),
    _M1Type_Type()
)
m1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1Type.setStatus("mandatory")


class _M1Description_Type(DisplayString):
    """Custom type m1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M1Description_Type.__name__ = "DisplayString"
_M1Description_Object = MibScalar
m1Description = _M1Description_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 2),
    _M1Description_Type()
)
m1Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1Description.setStatus("mandatory")


class _M1Version_Type(DisplayString):
    """Custom type m1Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M1Version_Type.__name__ = "DisplayString"
_M1Version_Object = MibScalar
m1Version = _M1Version_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 3),
    _M1Version_Type()
)
m1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1Version.setStatus("mandatory")
_M1Speed_Type = Integer32
_M1Speed_Object = MibScalar
m1Speed = _M1Speed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 4),
    _M1Speed_Type()
)
m1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1Speed.setStatus("mandatory")


class _M1Operation_Type(Integer32):
    """Custom type m1Operation based on Integer32"""
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
        *(("none", 0),
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("loopback", 4),
          ("illegalSpeed", 5),
          ("error", 6))
    )


_M1Operation_Type.__name__ = "Integer32"
_M1Operation_Object = MibScalar
m1Operation = _M1Operation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 5),
    _M1Operation_Type()
)
m1Operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1Operation.setStatus("mandatory")


class _M1Rx_Type(Integer32):
    """Custom type m1Rx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("rxAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M1Rx_Type.__name__ = "Integer32"
_M1Rx_Object = MibScalar
m1Rx = _M1Rx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 6),
    _M1Rx_Type()
)
m1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1Rx.setStatus("mandatory")


class _M1Tx_Type(Integer32):
    """Custom type m1Tx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("txAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M1Tx_Type.__name__ = "Integer32"
_M1Tx_Object = MibScalar
m1Tx = _M1Tx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 7),
    _M1Tx_Type()
)
m1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1Tx.setStatus("mandatory")


class _M1Loopback_Type(Integer32):
    """Custom type m1Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("analog", 2))
    )


_M1Loopback_Type.__name__ = "Integer32"
_M1Loopback_Object = MibScalar
m1Loopback = _M1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 8),
    _M1Loopback_Type()
)
m1Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1Loopback.setStatus("mandatory")


class _M1RxInput_Type(Integer32):
    """Custom type m1RxInput based on Integer32"""
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
        *(("other", 0),
          ("coax", 1),
          ("rj45", 2),
          ("v35", 3),
          ("e3", 4),
          ("db25unbalanced", 5),
          ("db25balanced", 6))
    )


_M1RxInput_Type.__name__ = "Integer32"
_M1RxInput_Object = MibScalar
m1RxInput = _M1RxInput_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 9),
    _M1RxInput_Type()
)
m1RxInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1RxInput.setStatus("mandatory")


class _M1TxMode_Type(Integer32):
    """Custom type m1TxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_M1TxMode_Type.__name__ = "Integer32"
_M1TxMode_Object = MibScalar
m1TxMode = _M1TxMode_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 10),
    _M1TxMode_Type()
)
m1TxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1TxMode.setStatus("mandatory")


class _M1TxClockSource_Type(Integer32):
    """Custom type m1TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("master", 1),
          ("slave", 2))
    )


_M1TxClockSource_Type.__name__ = "Integer32"
_M1TxClockSource_Object = MibScalar
m1TxClockSource = _M1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 11),
    _M1TxClockSource_Type()
)
m1TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1TxClockSource.setStatus("mandatory")


class _M1TxClockPhase_Type(Integer32):
    """Custom type m1TxClockPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M1TxClockPhase_Type.__name__ = "Integer32"
_M1TxClockPhase_Object = MibScalar
m1TxClockPhase = _M1TxClockPhase_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 12),
    _M1TxClockPhase_Type()
)
m1TxClockPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1TxClockPhase.setStatus("mandatory")


class _M1DataPolarity_Type(Integer32):
    """Custom type m1DataPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M1DataPolarity_Type.__name__ = "Integer32"
_M1DataPolarity_Object = MibScalar
m1DataPolarity = _M1DataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 13),
    _M1DataPolarity_Type()
)
m1DataPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1DataPolarity.setStatus("mandatory")
_M1ChanCount_Type = Integer32
_M1ChanCount_Object = MibScalar
m1ChanCount = _M1ChanCount_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 14),
    _M1ChanCount_Type()
)
m1ChanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1ChanCount.setStatus("mandatory")
_M1port1_ObjectIdentity = ObjectIdentity
m1port1 = _M1port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 21)
)
_M1p1statbin_Type = Integer32
_M1p1statbin_Object = MibScalar
m1p1statbin = _M1p1statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 21, 1),
    _M1p1statbin_Type()
)
m1p1statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1p1statbin.setStatus("mandatory")


class _M1p1connection_Type(Integer32):
    """Custom type m1p1connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M1p1connection_Type.__name__ = "Integer32"
_M1p1connection_Object = MibScalar
m1p1connection = _M1p1connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 21, 2),
    _M1p1connection_Type()
)
m1p1connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p1connection.setStatus("mandatory")


class _M1p1flowcntrl_Type(Integer32):
    """Custom type m1p1flowcntrl based on Integer32"""
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


_M1p1flowcntrl_Type.__name__ = "Integer32"
_M1p1flowcntrl_Object = MibScalar
m1p1flowcntrl = _M1p1flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 21, 3),
    _M1p1flowcntrl_Type()
)
m1p1flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p1flowcntrl.setStatus("mandatory")


class _M1p1priority_Type(Integer32):
    """Custom type m1p1priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M1p1priority_Type.__name__ = "Integer32"
_M1p1priority_Object = MibScalar
m1p1priority = _M1p1priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 21, 4),
    _M1p1priority_Type()
)
m1p1priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p1priority.setStatus("mandatory")


class _M1p1loopback_Type(Integer32):
    """Custom type m1p1loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M1p1loopback_Type.__name__ = "Integer32"
_M1p1loopback_Object = MibScalar
m1p1loopback = _M1p1loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 21, 5),
    _M1p1loopback_Type()
)
m1p1loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p1loopback.setStatus("mandatory")
_M1port2_ObjectIdentity = ObjectIdentity
m1port2 = _M1port2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 22)
)
_M1p2statbin_Type = Integer32
_M1p2statbin_Object = MibScalar
m1p2statbin = _M1p2statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 22, 1),
    _M1p2statbin_Type()
)
m1p2statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1p2statbin.setStatus("mandatory")


class _M1p2connection_Type(Integer32):
    """Custom type m1p2connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M1p2connection_Type.__name__ = "Integer32"
_M1p2connection_Object = MibScalar
m1p2connection = _M1p2connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 22, 2),
    _M1p2connection_Type()
)
m1p2connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p2connection.setStatus("mandatory")


class _M1p2flowcntrl_Type(Integer32):
    """Custom type m1p2flowcntrl based on Integer32"""
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


_M1p2flowcntrl_Type.__name__ = "Integer32"
_M1p2flowcntrl_Object = MibScalar
m1p2flowcntrl = _M1p2flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 22, 3),
    _M1p2flowcntrl_Type()
)
m1p2flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p2flowcntrl.setStatus("mandatory")


class _M1p2priority_Type(Integer32):
    """Custom type m1p2priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M1p2priority_Type.__name__ = "Integer32"
_M1p2priority_Object = MibScalar
m1p2priority = _M1p2priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 22, 4),
    _M1p2priority_Type()
)
m1p2priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p2priority.setStatus("mandatory")


class _M1p2loopback_Type(Integer32):
    """Custom type m1p2loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M1p2loopback_Type.__name__ = "Integer32"
_M1p2loopback_Object = MibScalar
m1p2loopback = _M1p2loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 22, 5),
    _M1p2loopback_Type()
)
m1p2loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p2loopback.setStatus("mandatory")
_M1port3_ObjectIdentity = ObjectIdentity
m1port3 = _M1port3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 23)
)
_M1p3statbin_Type = Integer32
_M1p3statbin_Object = MibScalar
m1p3statbin = _M1p3statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 23, 1),
    _M1p3statbin_Type()
)
m1p3statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1p3statbin.setStatus("mandatory")


class _M1p3connection_Type(Integer32):
    """Custom type m1p3connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M1p3connection_Type.__name__ = "Integer32"
_M1p3connection_Object = MibScalar
m1p3connection = _M1p3connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 23, 2),
    _M1p3connection_Type()
)
m1p3connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p3connection.setStatus("mandatory")


class _M1p3flowcntrl_Type(Integer32):
    """Custom type m1p3flowcntrl based on Integer32"""
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


_M1p3flowcntrl_Type.__name__ = "Integer32"
_M1p3flowcntrl_Object = MibScalar
m1p3flowcntrl = _M1p3flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 23, 3),
    _M1p3flowcntrl_Type()
)
m1p3flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p3flowcntrl.setStatus("mandatory")


class _M1p3priority_Type(Integer32):
    """Custom type m1p3priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M1p3priority_Type.__name__ = "Integer32"
_M1p3priority_Object = MibScalar
m1p3priority = _M1p3priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 23, 4),
    _M1p3priority_Type()
)
m1p3priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p3priority.setStatus("mandatory")


class _M1p3loopback_Type(Integer32):
    """Custom type m1p3loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M1p3loopback_Type.__name__ = "Integer32"
_M1p3loopback_Object = MibScalar
m1p3loopback = _M1p3loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 23, 5),
    _M1p3loopback_Type()
)
m1p3loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p3loopback.setStatus("mandatory")
_M1port4_ObjectIdentity = ObjectIdentity
m1port4 = _M1port4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 24)
)
_M1p4statbin_Type = Integer32
_M1p4statbin_Object = MibScalar
m1p4statbin = _M1p4statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 24, 1),
    _M1p4statbin_Type()
)
m1p4statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m1p4statbin.setStatus("mandatory")


class _M1p4connection_Type(Integer32):
    """Custom type m1p4connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M1p4connection_Type.__name__ = "Integer32"
_M1p4connection_Object = MibScalar
m1p4connection = _M1p4connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 24, 2),
    _M1p4connection_Type()
)
m1p4connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p4connection.setStatus("mandatory")


class _M1p4flowcntrl_Type(Integer32):
    """Custom type m1p4flowcntrl based on Integer32"""
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


_M1p4flowcntrl_Type.__name__ = "Integer32"
_M1p4flowcntrl_Object = MibScalar
m1p4flowcntrl = _M1p4flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 24, 3),
    _M1p4flowcntrl_Type()
)
m1p4flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p4flowcntrl.setStatus("mandatory")


class _M1p4priority_Type(Integer32):
    """Custom type m1p4priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M1p4priority_Type.__name__ = "Integer32"
_M1p4priority_Object = MibScalar
m1p4priority = _M1p4priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 24, 4),
    _M1p4priority_Type()
)
m1p4priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p4priority.setStatus("mandatory")


class _M1p4loopback_Type(Integer32):
    """Custom type m1p4loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M1p4loopback_Type.__name__ = "Integer32"
_M1p4loopback_Object = MibScalar
m1p4loopback = _M1p4loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 1, 24, 5),
    _M1p4loopback_Type()
)
m1p4loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m1p4loopback.setStatus("mandatory")
_M2_ObjectIdentity = ObjectIdentity
m2 = _M2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2)
)


class _M2Type_Type(Integer32):
    """Custom type m2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              33,
              37,
              43,
              74,
              78,
              100,
              227,
              241,
              242,
              255)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("e1x1", 30),
          ("e1", 33),
          ("v35", 37),
          ("bridge", 43),
          ("t1x4", 74),
          ("e1x4", 78),
          ("eow64", 100),
          ("e3", 227),
          ("f1bridge", 241),
          ("f2bridge", 242),
          ("none", 255))
    )


_M2Type_Type.__name__ = "Integer32"
_M2Type_Object = MibScalar
m2Type = _M2Type_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 1),
    _M2Type_Type()
)
m2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2Type.setStatus("mandatory")


class _M2Description_Type(DisplayString):
    """Custom type m2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M2Description_Type.__name__ = "DisplayString"
_M2Description_Object = MibScalar
m2Description = _M2Description_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 2),
    _M2Description_Type()
)
m2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2Description.setStatus("mandatory")


class _M2Version_Type(DisplayString):
    """Custom type m2Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M2Version_Type.__name__ = "DisplayString"
_M2Version_Object = MibScalar
m2Version = _M2Version_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 3),
    _M2Version_Type()
)
m2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2Version.setStatus("mandatory")
_M2Speed_Type = Integer32
_M2Speed_Object = MibScalar
m2Speed = _M2Speed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 4),
    _M2Speed_Type()
)
m2Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2Speed.setStatus("mandatory")


class _M2Operation_Type(Integer32):
    """Custom type m2Operation based on Integer32"""
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
        *(("none", 0),
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("loopback", 4),
          ("illegalSpeed", 5),
          ("error", 6))
    )


_M2Operation_Type.__name__ = "Integer32"
_M2Operation_Object = MibScalar
m2Operation = _M2Operation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 5),
    _M2Operation_Type()
)
m2Operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2Operation.setStatus("mandatory")


class _M2Rx_Type(Integer32):
    """Custom type m2Rx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("rxAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M2Rx_Type.__name__ = "Integer32"
_M2Rx_Object = MibScalar
m2Rx = _M2Rx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 6),
    _M2Rx_Type()
)
m2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2Rx.setStatus("mandatory")


class _M2Tx_Type(Integer32):
    """Custom type m2Tx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("txAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M2Tx_Type.__name__ = "Integer32"
_M2Tx_Object = MibScalar
m2Tx = _M2Tx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 7),
    _M2Tx_Type()
)
m2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2Tx.setStatus("mandatory")


class _M2Loopback_Type(Integer32):
    """Custom type m2Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("analog", 2))
    )


_M2Loopback_Type.__name__ = "Integer32"
_M2Loopback_Object = MibScalar
m2Loopback = _M2Loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 8),
    _M2Loopback_Type()
)
m2Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2Loopback.setStatus("mandatory")


class _M2RxInput_Type(Integer32):
    """Custom type m2RxInput based on Integer32"""
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
        *(("other", 0),
          ("coax", 1),
          ("rj45", 2),
          ("v35", 3),
          ("e3", 4),
          ("db25unbalanced", 5),
          ("db25balanced", 6))
    )


_M2RxInput_Type.__name__ = "Integer32"
_M2RxInput_Object = MibScalar
m2RxInput = _M2RxInput_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 9),
    _M2RxInput_Type()
)
m2RxInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2RxInput.setStatus("mandatory")


class _M2TxMode_Type(Integer32):
    """Custom type m2TxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_M2TxMode_Type.__name__ = "Integer32"
_M2TxMode_Object = MibScalar
m2TxMode = _M2TxMode_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 10),
    _M2TxMode_Type()
)
m2TxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2TxMode.setStatus("mandatory")


class _M2TxClockSource_Type(Integer32):
    """Custom type m2TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("master", 1),
          ("slave", 2))
    )


_M2TxClockSource_Type.__name__ = "Integer32"
_M2TxClockSource_Object = MibScalar
m2TxClockSource = _M2TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 11),
    _M2TxClockSource_Type()
)
m2TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2TxClockSource.setStatus("mandatory")


class _M2TxClockPhase_Type(Integer32):
    """Custom type m2TxClockPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M2TxClockPhase_Type.__name__ = "Integer32"
_M2TxClockPhase_Object = MibScalar
m2TxClockPhase = _M2TxClockPhase_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 12),
    _M2TxClockPhase_Type()
)
m2TxClockPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2TxClockPhase.setStatus("mandatory")


class _M2DataPolarity_Type(Integer32):
    """Custom type m2DataPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M2DataPolarity_Type.__name__ = "Integer32"
_M2DataPolarity_Object = MibScalar
m2DataPolarity = _M2DataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 13),
    _M2DataPolarity_Type()
)
m2DataPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2DataPolarity.setStatus("mandatory")
_M2ChanCount_Type = Integer32
_M2ChanCount_Object = MibScalar
m2ChanCount = _M2ChanCount_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 14),
    _M2ChanCount_Type()
)
m2ChanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2ChanCount.setStatus("mandatory")
_M2port1_ObjectIdentity = ObjectIdentity
m2port1 = _M2port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 21)
)
_M2p1statbin_Type = Integer32
_M2p1statbin_Object = MibScalar
m2p1statbin = _M2p1statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 21, 1),
    _M2p1statbin_Type()
)
m2p1statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2p1statbin.setStatus("mandatory")


class _M2p1connection_Type(Integer32):
    """Custom type m2p1connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M2p1connection_Type.__name__ = "Integer32"
_M2p1connection_Object = MibScalar
m2p1connection = _M2p1connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 21, 2),
    _M2p1connection_Type()
)
m2p1connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p1connection.setStatus("mandatory")


class _M2p1flowcntrl_Type(Integer32):
    """Custom type m2p1flowcntrl based on Integer32"""
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


_M2p1flowcntrl_Type.__name__ = "Integer32"
_M2p1flowcntrl_Object = MibScalar
m2p1flowcntrl = _M2p1flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 21, 3),
    _M2p1flowcntrl_Type()
)
m2p1flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p1flowcntrl.setStatus("mandatory")


class _M2p1priority_Type(Integer32):
    """Custom type m2p1priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M2p1priority_Type.__name__ = "Integer32"
_M2p1priority_Object = MibScalar
m2p1priority = _M2p1priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 21, 4),
    _M2p1priority_Type()
)
m2p1priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p1priority.setStatus("mandatory")


class _M2p1loopback_Type(Integer32):
    """Custom type m2p1loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M2p1loopback_Type.__name__ = "Integer32"
_M2p1loopback_Object = MibScalar
m2p1loopback = _M2p1loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 21, 5),
    _M2p1loopback_Type()
)
m2p1loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p1loopback.setStatus("mandatory")
_M2port2_ObjectIdentity = ObjectIdentity
m2port2 = _M2port2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 22)
)
_M2p2statbin_Type = Integer32
_M2p2statbin_Object = MibScalar
m2p2statbin = _M2p2statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 22, 1),
    _M2p2statbin_Type()
)
m2p2statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2p2statbin.setStatus("mandatory")


class _M2p2connection_Type(Integer32):
    """Custom type m2p2connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M2p2connection_Type.__name__ = "Integer32"
_M2p2connection_Object = MibScalar
m2p2connection = _M2p2connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 22, 2),
    _M2p2connection_Type()
)
m2p2connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p2connection.setStatus("mandatory")


class _M2p2flowcntrl_Type(Integer32):
    """Custom type m2p2flowcntrl based on Integer32"""
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


_M2p2flowcntrl_Type.__name__ = "Integer32"
_M2p2flowcntrl_Object = MibScalar
m2p2flowcntrl = _M2p2flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 22, 3),
    _M2p2flowcntrl_Type()
)
m2p2flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p2flowcntrl.setStatus("mandatory")


class _M2p2priority_Type(Integer32):
    """Custom type m2p2priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M2p2priority_Type.__name__ = "Integer32"
_M2p2priority_Object = MibScalar
m2p2priority = _M2p2priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 22, 4),
    _M2p2priority_Type()
)
m2p2priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p2priority.setStatus("mandatory")


class _M2p2loopback_Type(Integer32):
    """Custom type m2p2loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M2p2loopback_Type.__name__ = "Integer32"
_M2p2loopback_Object = MibScalar
m2p2loopback = _M2p2loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 22, 5),
    _M2p2loopback_Type()
)
m2p2loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p2loopback.setStatus("mandatory")
_M2port3_ObjectIdentity = ObjectIdentity
m2port3 = _M2port3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 23)
)
_M2p3statbin_Type = Integer32
_M2p3statbin_Object = MibScalar
m2p3statbin = _M2p3statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 23, 1),
    _M2p3statbin_Type()
)
m2p3statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2p3statbin.setStatus("mandatory")


class _M2p3connection_Type(Integer32):
    """Custom type m2p3connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M2p3connection_Type.__name__ = "Integer32"
_M2p3connection_Object = MibScalar
m2p3connection = _M2p3connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 23, 2),
    _M2p3connection_Type()
)
m2p3connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p3connection.setStatus("mandatory")


class _M2p3flowcntrl_Type(Integer32):
    """Custom type m2p3flowcntrl based on Integer32"""
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


_M2p3flowcntrl_Type.__name__ = "Integer32"
_M2p3flowcntrl_Object = MibScalar
m2p3flowcntrl = _M2p3flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 23, 3),
    _M2p3flowcntrl_Type()
)
m2p3flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p3flowcntrl.setStatus("mandatory")


class _M2p3priority_Type(Integer32):
    """Custom type m2p3priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M2p3priority_Type.__name__ = "Integer32"
_M2p3priority_Object = MibScalar
m2p3priority = _M2p3priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 23, 4),
    _M2p3priority_Type()
)
m2p3priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p3priority.setStatus("mandatory")


class _M2p3loopback_Type(Integer32):
    """Custom type m2p3loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M2p3loopback_Type.__name__ = "Integer32"
_M2p3loopback_Object = MibScalar
m2p3loopback = _M2p3loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 23, 5),
    _M2p3loopback_Type()
)
m2p3loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p3loopback.setStatus("mandatory")
_M2port4_ObjectIdentity = ObjectIdentity
m2port4 = _M2port4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 24)
)
_M2p4statbin_Type = Integer32
_M2p4statbin_Object = MibScalar
m2p4statbin = _M2p4statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 24, 1),
    _M2p4statbin_Type()
)
m2p4statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m2p4statbin.setStatus("mandatory")


class _M2p4connection_Type(Integer32):
    """Custom type m2p4connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M2p4connection_Type.__name__ = "Integer32"
_M2p4connection_Object = MibScalar
m2p4connection = _M2p4connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 24, 2),
    _M2p4connection_Type()
)
m2p4connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p4connection.setStatus("mandatory")


class _M2p4flowcntrl_Type(Integer32):
    """Custom type m2p4flowcntrl based on Integer32"""
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


_M2p4flowcntrl_Type.__name__ = "Integer32"
_M2p4flowcntrl_Object = MibScalar
m2p4flowcntrl = _M2p4flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 24, 3),
    _M2p4flowcntrl_Type()
)
m2p4flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p4flowcntrl.setStatus("mandatory")


class _M2p4priority_Type(Integer32):
    """Custom type m2p4priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M2p4priority_Type.__name__ = "Integer32"
_M2p4priority_Object = MibScalar
m2p4priority = _M2p4priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 24, 4),
    _M2p4priority_Type()
)
m2p4priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p4priority.setStatus("mandatory")


class _M2p4loopback_Type(Integer32):
    """Custom type m2p4loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M2p4loopback_Type.__name__ = "Integer32"
_M2p4loopback_Object = MibScalar
m2p4loopback = _M2p4loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 2, 24, 5),
    _M2p4loopback_Type()
)
m2p4loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m2p4loopback.setStatus("mandatory")
_M3_ObjectIdentity = ObjectIdentity
m3 = _M3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3)
)


class _M3Type_Type(Integer32):
    """Custom type m3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              33,
              37,
              43,
              74,
              78,
              100,
              227,
              241,
              242,
              255)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("e1x1", 30),
          ("e1", 33),
          ("v35", 37),
          ("bridge", 43),
          ("t1x4", 74),
          ("e1x4", 78),
          ("eow64", 100),
          ("e3", 227),
          ("f1bridge", 241),
          ("f2bridge", 242),
          ("none", 255))
    )


_M3Type_Type.__name__ = "Integer32"
_M3Type_Object = MibScalar
m3Type = _M3Type_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 1),
    _M3Type_Type()
)
m3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3Type.setStatus("mandatory")


class _M3Description_Type(DisplayString):
    """Custom type m3Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M3Description_Type.__name__ = "DisplayString"
_M3Description_Object = MibScalar
m3Description = _M3Description_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 2),
    _M3Description_Type()
)
m3Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3Description.setStatus("mandatory")


class _M3Version_Type(DisplayString):
    """Custom type m3Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M3Version_Type.__name__ = "DisplayString"
_M3Version_Object = MibScalar
m3Version = _M3Version_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 3),
    _M3Version_Type()
)
m3Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3Version.setStatus("mandatory")
_M3Speed_Type = Integer32
_M3Speed_Object = MibScalar
m3Speed = _M3Speed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 4),
    _M3Speed_Type()
)
m3Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3Speed.setStatus("mandatory")


class _M3Operation_Type(Integer32):
    """Custom type m3Operation based on Integer32"""
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
        *(("none", 0),
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("loopback", 4),
          ("illegalSpeed", 5),
          ("error", 6))
    )


_M3Operation_Type.__name__ = "Integer32"
_M3Operation_Object = MibScalar
m3Operation = _M3Operation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 5),
    _M3Operation_Type()
)
m3Operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3Operation.setStatus("mandatory")


class _M3Rx_Type(Integer32):
    """Custom type m3Rx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("rxAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M3Rx_Type.__name__ = "Integer32"
_M3Rx_Object = MibScalar
m3Rx = _M3Rx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 6),
    _M3Rx_Type()
)
m3Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3Rx.setStatus("mandatory")


class _M3Tx_Type(Integer32):
    """Custom type m3Tx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("txAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M3Tx_Type.__name__ = "Integer32"
_M3Tx_Object = MibScalar
m3Tx = _M3Tx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 7),
    _M3Tx_Type()
)
m3Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3Tx.setStatus("mandatory")


class _M3Loopback_Type(Integer32):
    """Custom type m3Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("analog", 2))
    )


_M3Loopback_Type.__name__ = "Integer32"
_M3Loopback_Object = MibScalar
m3Loopback = _M3Loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 8),
    _M3Loopback_Type()
)
m3Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3Loopback.setStatus("mandatory")


class _M3RxInput_Type(Integer32):
    """Custom type m3RxInput based on Integer32"""
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
        *(("other", 0),
          ("coax", 1),
          ("rj45", 2),
          ("v35", 3),
          ("e3", 4),
          ("db25unbalanced", 5),
          ("db25balanced", 6))
    )


_M3RxInput_Type.__name__ = "Integer32"
_M3RxInput_Object = MibScalar
m3RxInput = _M3RxInput_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 9),
    _M3RxInput_Type()
)
m3RxInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3RxInput.setStatus("mandatory")


class _M3TxMode_Type(Integer32):
    """Custom type m3TxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_M3TxMode_Type.__name__ = "Integer32"
_M3TxMode_Object = MibScalar
m3TxMode = _M3TxMode_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 10),
    _M3TxMode_Type()
)
m3TxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3TxMode.setStatus("mandatory")


class _M3TxClockSource_Type(Integer32):
    """Custom type m3TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("master", 1),
          ("slave", 2))
    )


_M3TxClockSource_Type.__name__ = "Integer32"
_M3TxClockSource_Object = MibScalar
m3TxClockSource = _M3TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 11),
    _M3TxClockSource_Type()
)
m3TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3TxClockSource.setStatus("mandatory")


class _M3TxClockPhase_Type(Integer32):
    """Custom type m3TxClockPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M3TxClockPhase_Type.__name__ = "Integer32"
_M3TxClockPhase_Object = MibScalar
m3TxClockPhase = _M3TxClockPhase_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 12),
    _M3TxClockPhase_Type()
)
m3TxClockPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3TxClockPhase.setStatus("mandatory")


class _M3DataPolarity_Type(Integer32):
    """Custom type m3DataPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M3DataPolarity_Type.__name__ = "Integer32"
_M3DataPolarity_Object = MibScalar
m3DataPolarity = _M3DataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 13),
    _M3DataPolarity_Type()
)
m3DataPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3DataPolarity.setStatus("mandatory")
_M3ChanCount_Type = Integer32
_M3ChanCount_Object = MibScalar
m3ChanCount = _M3ChanCount_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 14),
    _M3ChanCount_Type()
)
m3ChanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3ChanCount.setStatus("mandatory")
_M3port1_ObjectIdentity = ObjectIdentity
m3port1 = _M3port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 21)
)
_M3p1statbin_Type = Integer32
_M3p1statbin_Object = MibScalar
m3p1statbin = _M3p1statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 21, 1),
    _M3p1statbin_Type()
)
m3p1statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3p1statbin.setStatus("mandatory")


class _M3p1connection_Type(Integer32):
    """Custom type m3p1connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M3p1connection_Type.__name__ = "Integer32"
_M3p1connection_Object = MibScalar
m3p1connection = _M3p1connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 21, 2),
    _M3p1connection_Type()
)
m3p1connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p1connection.setStatus("mandatory")


class _M3p1flowcntrl_Type(Integer32):
    """Custom type m3p1flowcntrl based on Integer32"""
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


_M3p1flowcntrl_Type.__name__ = "Integer32"
_M3p1flowcntrl_Object = MibScalar
m3p1flowcntrl = _M3p1flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 21, 3),
    _M3p1flowcntrl_Type()
)
m3p1flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p1flowcntrl.setStatus("mandatory")


class _M3p1priority_Type(Integer32):
    """Custom type m3p1priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M3p1priority_Type.__name__ = "Integer32"
_M3p1priority_Object = MibScalar
m3p1priority = _M3p1priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 21, 4),
    _M3p1priority_Type()
)
m3p1priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p1priority.setStatus("mandatory")


class _M3p1loopback_Type(Integer32):
    """Custom type m3p1loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M3p1loopback_Type.__name__ = "Integer32"
_M3p1loopback_Object = MibScalar
m3p1loopback = _M3p1loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 21, 5),
    _M3p1loopback_Type()
)
m3p1loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p1loopback.setStatus("mandatory")
_M3port2_ObjectIdentity = ObjectIdentity
m3port2 = _M3port2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 22)
)
_M3p2statbin_Type = Integer32
_M3p2statbin_Object = MibScalar
m3p2statbin = _M3p2statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 22, 1),
    _M3p2statbin_Type()
)
m3p2statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3p2statbin.setStatus("mandatory")


class _M3p2connection_Type(Integer32):
    """Custom type m3p2connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M3p2connection_Type.__name__ = "Integer32"
_M3p2connection_Object = MibScalar
m3p2connection = _M3p2connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 22, 2),
    _M3p2connection_Type()
)
m3p2connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p2connection.setStatus("mandatory")


class _M3p2flowcntrl_Type(Integer32):
    """Custom type m3p2flowcntrl based on Integer32"""
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


_M3p2flowcntrl_Type.__name__ = "Integer32"
_M3p2flowcntrl_Object = MibScalar
m3p2flowcntrl = _M3p2flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 22, 3),
    _M3p2flowcntrl_Type()
)
m3p2flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p2flowcntrl.setStatus("mandatory")


class _M3p2priority_Type(Integer32):
    """Custom type m3p2priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M3p2priority_Type.__name__ = "Integer32"
_M3p2priority_Object = MibScalar
m3p2priority = _M3p2priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 22, 4),
    _M3p2priority_Type()
)
m3p2priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p2priority.setStatus("mandatory")


class _M3p2loopback_Type(Integer32):
    """Custom type m3p2loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M3p2loopback_Type.__name__ = "Integer32"
_M3p2loopback_Object = MibScalar
m3p2loopback = _M3p2loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 22, 5),
    _M3p2loopback_Type()
)
m3p2loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p2loopback.setStatus("mandatory")
_M3port3_ObjectIdentity = ObjectIdentity
m3port3 = _M3port3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 23)
)
_M3p3statbin_Type = Integer32
_M3p3statbin_Object = MibScalar
m3p3statbin = _M3p3statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 23, 1),
    _M3p3statbin_Type()
)
m3p3statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3p3statbin.setStatus("mandatory")


class _M3p3connection_Type(Integer32):
    """Custom type m3p3connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M3p3connection_Type.__name__ = "Integer32"
_M3p3connection_Object = MibScalar
m3p3connection = _M3p3connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 23, 2),
    _M3p3connection_Type()
)
m3p3connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p3connection.setStatus("mandatory")


class _M3p3flowcntrl_Type(Integer32):
    """Custom type m3p3flowcntrl based on Integer32"""
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


_M3p3flowcntrl_Type.__name__ = "Integer32"
_M3p3flowcntrl_Object = MibScalar
m3p3flowcntrl = _M3p3flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 23, 3),
    _M3p3flowcntrl_Type()
)
m3p3flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p3flowcntrl.setStatus("mandatory")


class _M3p3priority_Type(Integer32):
    """Custom type m3p3priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M3p3priority_Type.__name__ = "Integer32"
_M3p3priority_Object = MibScalar
m3p3priority = _M3p3priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 23, 4),
    _M3p3priority_Type()
)
m3p3priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p3priority.setStatus("mandatory")


class _M3p3loopback_Type(Integer32):
    """Custom type m3p3loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M3p3loopback_Type.__name__ = "Integer32"
_M3p3loopback_Object = MibScalar
m3p3loopback = _M3p3loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 23, 5),
    _M3p3loopback_Type()
)
m3p3loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p3loopback.setStatus("mandatory")
_M3port4_ObjectIdentity = ObjectIdentity
m3port4 = _M3port4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 24)
)
_M3p4statbin_Type = Integer32
_M3p4statbin_Object = MibScalar
m3p4statbin = _M3p4statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 24, 1),
    _M3p4statbin_Type()
)
m3p4statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m3p4statbin.setStatus("mandatory")


class _M3p4connection_Type(Integer32):
    """Custom type m3p4connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M3p4connection_Type.__name__ = "Integer32"
_M3p4connection_Object = MibScalar
m3p4connection = _M3p4connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 24, 2),
    _M3p4connection_Type()
)
m3p4connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p4connection.setStatus("mandatory")


class _M3p4flowcntrl_Type(Integer32):
    """Custom type m3p4flowcntrl based on Integer32"""
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


_M3p4flowcntrl_Type.__name__ = "Integer32"
_M3p4flowcntrl_Object = MibScalar
m3p4flowcntrl = _M3p4flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 24, 3),
    _M3p4flowcntrl_Type()
)
m3p4flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p4flowcntrl.setStatus("mandatory")


class _M3p4priority_Type(Integer32):
    """Custom type m3p4priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M3p4priority_Type.__name__ = "Integer32"
_M3p4priority_Object = MibScalar
m3p4priority = _M3p4priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 24, 4),
    _M3p4priority_Type()
)
m3p4priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p4priority.setStatus("mandatory")


class _M3p4loopback_Type(Integer32):
    """Custom type m3p4loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M3p4loopback_Type.__name__ = "Integer32"
_M3p4loopback_Object = MibScalar
m3p4loopback = _M3p4loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 3, 24, 5),
    _M3p4loopback_Type()
)
m3p4loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m3p4loopback.setStatus("mandatory")
_M4_ObjectIdentity = ObjectIdentity
m4 = _M4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4)
)


class _M4Type_Type(Integer32):
    """Custom type m4Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              33,
              37,
              43,
              74,
              78,
              100,
              227,
              241,
              242,
              255)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("e1x1", 30),
          ("e1", 33),
          ("v35", 37),
          ("bridge", 43),
          ("t1x4", 74),
          ("e1x4", 78),
          ("eow64", 100),
          ("e3", 227),
          ("f1bridge", 241),
          ("f2bridge", 242),
          ("none", 255))
    )


_M4Type_Type.__name__ = "Integer32"
_M4Type_Object = MibScalar
m4Type = _M4Type_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 1),
    _M4Type_Type()
)
m4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4Type.setStatus("mandatory")


class _M4Description_Type(DisplayString):
    """Custom type m4Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M4Description_Type.__name__ = "DisplayString"
_M4Description_Object = MibScalar
m4Description = _M4Description_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 2),
    _M4Description_Type()
)
m4Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4Description.setStatus("mandatory")


class _M4Version_Type(DisplayString):
    """Custom type m4Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_M4Version_Type.__name__ = "DisplayString"
_M4Version_Object = MibScalar
m4Version = _M4Version_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 3),
    _M4Version_Type()
)
m4Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4Version.setStatus("mandatory")
_M4Speed_Type = Integer32
_M4Speed_Object = MibScalar
m4Speed = _M4Speed_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 4),
    _M4Speed_Type()
)
m4Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4Speed.setStatus("mandatory")


class _M4Operation_Type(Integer32):
    """Custom type m4Operation based on Integer32"""
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
        *(("none", 0),
          ("booting", 1),
          ("ok", 2),
          ("testing", 3),
          ("loopback", 4),
          ("illegalSpeed", 5),
          ("error", 6))
    )


_M4Operation_Type.__name__ = "Integer32"
_M4Operation_Object = MibScalar
m4Operation = _M4Operation_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 5),
    _M4Operation_Type()
)
m4Operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4Operation.setStatus("mandatory")


class _M4Rx_Type(Integer32):
    """Custom type m4Rx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("rxAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M4Rx_Type.__name__ = "Integer32"
_M4Rx_Object = MibScalar
m4Rx = _M4Rx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 6),
    _M4Rx_Type()
)
m4Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4Rx.setStatus("mandatory")


class _M4Tx_Type(Integer32):
    """Custom type m4Tx based on Integer32"""
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
        *(("none", 0),
          ("ok", 1),
          ("noSignal", 2),
          ("noLink", 3),
          ("txAIS", 4),
          ("error", 5),
          ("noData", 6))
    )


_M4Tx_Type.__name__ = "Integer32"
_M4Tx_Object = MibScalar
m4Tx = _M4Tx_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 7),
    _M4Tx_Type()
)
m4Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4Tx.setStatus("mandatory")


class _M4Loopback_Type(Integer32):
    """Custom type m4Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("analog", 2))
    )


_M4Loopback_Type.__name__ = "Integer32"
_M4Loopback_Object = MibScalar
m4Loopback = _M4Loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 8),
    _M4Loopback_Type()
)
m4Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4Loopback.setStatus("mandatory")


class _M4RxInput_Type(Integer32):
    """Custom type m4RxInput based on Integer32"""
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
        *(("other", 0),
          ("coax", 1),
          ("rj45", 2),
          ("v35", 3),
          ("e3", 4),
          ("db25unbalanced", 5),
          ("db25balanced", 6))
    )


_M4RxInput_Type.__name__ = "Integer32"
_M4RxInput_Object = MibScalar
m4RxInput = _M4RxInput_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 9),
    _M4RxInput_Type()
)
m4RxInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4RxInput.setStatus("mandatory")


class _M4TxMode_Type(Integer32):
    """Custom type m4TxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_M4TxMode_Type.__name__ = "Integer32"
_M4TxMode_Object = MibScalar
m4TxMode = _M4TxMode_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 10),
    _M4TxMode_Type()
)
m4TxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4TxMode.setStatus("mandatory")


class _M4TxClockSource_Type(Integer32):
    """Custom type m4TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("master", 1),
          ("slave", 2))
    )


_M4TxClockSource_Type.__name__ = "Integer32"
_M4TxClockSource_Object = MibScalar
m4TxClockSource = _M4TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 11),
    _M4TxClockSource_Type()
)
m4TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4TxClockSource.setStatus("mandatory")


class _M4TxClockPhase_Type(Integer32):
    """Custom type m4TxClockPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M4TxClockPhase_Type.__name__ = "Integer32"
_M4TxClockPhase_Object = MibScalar
m4TxClockPhase = _M4TxClockPhase_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 12),
    _M4TxClockPhase_Type()
)
m4TxClockPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4TxClockPhase.setStatus("mandatory")


class _M4DataPolarity_Type(Integer32):
    """Custom type m4DataPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("normal", 1),
          ("inverse", 2))
    )


_M4DataPolarity_Type.__name__ = "Integer32"
_M4DataPolarity_Object = MibScalar
m4DataPolarity = _M4DataPolarity_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 13),
    _M4DataPolarity_Type()
)
m4DataPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4DataPolarity.setStatus("mandatory")
_M4ChanCount_Type = Integer32
_M4ChanCount_Object = MibScalar
m4ChanCount = _M4ChanCount_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 14),
    _M4ChanCount_Type()
)
m4ChanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4ChanCount.setStatus("mandatory")
_M4port1_ObjectIdentity = ObjectIdentity
m4port1 = _M4port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 21)
)
_M4p1statbin_Type = Integer32
_M4p1statbin_Object = MibScalar
m4p1statbin = _M4p1statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 21, 1),
    _M4p1statbin_Type()
)
m4p1statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4p1statbin.setStatus("mandatory")


class _M4p1connection_Type(Integer32):
    """Custom type m4p1connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M4p1connection_Type.__name__ = "Integer32"
_M4p1connection_Object = MibScalar
m4p1connection = _M4p1connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 21, 2),
    _M4p1connection_Type()
)
m4p1connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p1connection.setStatus("mandatory")


class _M4p1flowcntrl_Type(Integer32):
    """Custom type m4p1flowcntrl based on Integer32"""
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


_M4p1flowcntrl_Type.__name__ = "Integer32"
_M4p1flowcntrl_Object = MibScalar
m4p1flowcntrl = _M4p1flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 21, 3),
    _M4p1flowcntrl_Type()
)
m4p1flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p1flowcntrl.setStatus("mandatory")


class _M4p1priority_Type(Integer32):
    """Custom type m4p1priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M4p1priority_Type.__name__ = "Integer32"
_M4p1priority_Object = MibScalar
m4p1priority = _M4p1priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 21, 4),
    _M4p1priority_Type()
)
m4p1priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p1priority.setStatus("mandatory")


class _M4p1loopback_Type(Integer32):
    """Custom type m4p1loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M4p1loopback_Type.__name__ = "Integer32"
_M4p1loopback_Object = MibScalar
m4p1loopback = _M4p1loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 21, 5),
    _M4p1loopback_Type()
)
m4p1loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p1loopback.setStatus("mandatory")
_M4port2_ObjectIdentity = ObjectIdentity
m4port2 = _M4port2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 22)
)
_M4p2statbin_Type = Integer32
_M4p2statbin_Object = MibScalar
m4p2statbin = _M4p2statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 22, 1),
    _M4p2statbin_Type()
)
m4p2statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4p2statbin.setStatus("mandatory")


class _M4p2connection_Type(Integer32):
    """Custom type m4p2connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M4p2connection_Type.__name__ = "Integer32"
_M4p2connection_Object = MibScalar
m4p2connection = _M4p2connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 22, 2),
    _M4p2connection_Type()
)
m4p2connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p2connection.setStatus("mandatory")


class _M4p2flowcntrl_Type(Integer32):
    """Custom type m4p2flowcntrl based on Integer32"""
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


_M4p2flowcntrl_Type.__name__ = "Integer32"
_M4p2flowcntrl_Object = MibScalar
m4p2flowcntrl = _M4p2flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 22, 3),
    _M4p2flowcntrl_Type()
)
m4p2flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p2flowcntrl.setStatus("mandatory")


class _M4p2priority_Type(Integer32):
    """Custom type m4p2priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M4p2priority_Type.__name__ = "Integer32"
_M4p2priority_Object = MibScalar
m4p2priority = _M4p2priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 22, 4),
    _M4p2priority_Type()
)
m4p2priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p2priority.setStatus("mandatory")


class _M4p2loopback_Type(Integer32):
    """Custom type m4p2loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M4p2loopback_Type.__name__ = "Integer32"
_M4p2loopback_Object = MibScalar
m4p2loopback = _M4p2loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 22, 5),
    _M4p2loopback_Type()
)
m4p2loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p2loopback.setStatus("mandatory")
_M4port3_ObjectIdentity = ObjectIdentity
m4port3 = _M4port3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 23)
)
_M4p3statbin_Type = Integer32
_M4p3statbin_Object = MibScalar
m4p3statbin = _M4p3statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 23, 1),
    _M4p3statbin_Type()
)
m4p3statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4p3statbin.setStatus("mandatory")


class _M4p3connection_Type(Integer32):
    """Custom type m4p3connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M4p3connection_Type.__name__ = "Integer32"
_M4p3connection_Object = MibScalar
m4p3connection = _M4p3connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 23, 2),
    _M4p3connection_Type()
)
m4p3connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p3connection.setStatus("mandatory")


class _M4p3flowcntrl_Type(Integer32):
    """Custom type m4p3flowcntrl based on Integer32"""
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


_M4p3flowcntrl_Type.__name__ = "Integer32"
_M4p3flowcntrl_Object = MibScalar
m4p3flowcntrl = _M4p3flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 23, 3),
    _M4p3flowcntrl_Type()
)
m4p3flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p3flowcntrl.setStatus("mandatory")


class _M4p3priority_Type(Integer32):
    """Custom type m4p3priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M4p3priority_Type.__name__ = "Integer32"
_M4p3priority_Object = MibScalar
m4p3priority = _M4p3priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 23, 4),
    _M4p3priority_Type()
)
m4p3priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p3priority.setStatus("mandatory")


class _M4p3loopback_Type(Integer32):
    """Custom type m4p3loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M4p3loopback_Type.__name__ = "Integer32"
_M4p3loopback_Object = MibScalar
m4p3loopback = _M4p3loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 23, 5),
    _M4p3loopback_Type()
)
m4p3loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p3loopback.setStatus("mandatory")
_M4port4_ObjectIdentity = ObjectIdentity
m4port4 = _M4port4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 24)
)
_M4p4statbin_Type = Integer32
_M4p4statbin_Object = MibScalar
m4p4statbin = _M4p4statbin_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 24, 1),
    _M4p4statbin_Type()
)
m4p4statbin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m4p4statbin.setStatus("mandatory")


class _M4p4connection_Type(Integer32):
    """Custom type m4p4connection based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("eth10fdx", 2),
          ("eth10hdx", 3),
          ("eth100fdx", 4),
          ("eth100hdx", 5),
          ("ds1", 6))
    )


_M4p4connection_Type.__name__ = "Integer32"
_M4p4connection_Object = MibScalar
m4p4connection = _M4p4connection_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 24, 2),
    _M4p4connection_Type()
)
m4p4connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p4connection.setStatus("mandatory")


class _M4p4flowcntrl_Type(Integer32):
    """Custom type m4p4flowcntrl based on Integer32"""
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


_M4p4flowcntrl_Type.__name__ = "Integer32"
_M4p4flowcntrl_Object = MibScalar
m4p4flowcntrl = _M4p4flowcntrl_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 24, 3),
    _M4p4flowcntrl_Type()
)
m4p4flowcntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p4flowcntrl.setStatus("mandatory")


class _M4p4priority_Type(Integer32):
    """Custom type m4p4priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_M4p4priority_Type.__name__ = "Integer32"
_M4p4priority_Object = MibScalar
m4p4priority = _M4p4priority_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 24, 4),
    _M4p4priority_Type()
)
m4p4priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p4priority.setStatus("mandatory")


class _M4p4loopback_Type(Integer32):
    """Custom type m4p4loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("analog", 1),
          ("remote", 2),
          ("digital", 4),
          ("remoteANDdigital", 6))
    )


_M4p4loopback_Type.__name__ = "Integer32"
_M4p4loopback_Object = MibScalar
m4p4loopback = _M4p4loopback_Object(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 6, 4, 24, 5),
    _M4p4loopback_Type()
)
m4p4loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m4p4loopback.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 0, 0)
)
alarmTrap.setObjects(
      *(("SAF-MPMUX-MIB", "rfAlarm"),
        ("SAF-MPMUX-MIB", "bbSyncLostAlarm"),
        ("SAF-MPMUX-MIB", "berAlarm"),
        ("SAF-MPMUX-MIB", "remoteAlarm"),
        ("SAF-MPMUX-MIB", "systemAlarm"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        ""
    )

alinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1, 2, 22, 0, 1)
)
alinkTrap.setObjects(
    ("SAF-MPMUX-MIB", "activeLink")
)
if mibBuilder.loadTexts:
    alinkTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-MPMUX-MIB",
    **{"saf": saf,
       "tehnika": tehnika,
       "microwaveRadio": microwaveRadio,
       "pointToPoint": pointToPoint,
       "cfm22": cfm22,
       "mpmux": mpmux,
       "alarmTrap": alarmTrap,
       "alinkTrap": alinkTrap,
       "terminal": terminal,
       "termProduct": termProduct,
       "termDescription": termDescription,
       "termLocation": termLocation,
       "termVersion": termVersion,
       "termOperation": termOperation,
       "termIduTemperature": termIduTemperature,
       "termFrameErrors": termFrameErrors,
       "writeConfig": writeConfig,
       "restartCPU": restartCPU,
       "serialNumber": serialNumber,
       "termRf1CablePowerStatus": termRf1CablePowerStatus,
       "termRf2CablePowerStatus": termRf2CablePowerStatus,
       "power3V3PS1": power3V3PS1,
       "power5VPS1": power5VPS1,
       "powerM5VPS1": powerM5VPS1,
       "powerODU1V": powerODU1V,
       "powerODU1I": powerODU1I,
       "powerODU1W": powerODU1W,
       "power3V3PS2": power3V3PS2,
       "power5VPS2": power5VPS2,
       "powerM5VPS2": powerM5VPS2,
       "powerODU2V": powerODU2V,
       "powerODU2I": powerODU2I,
       "powerODU2W": powerODU2W,
       "cpuUsage": cpuUsage,
       "termBFrameErr": termBFrameErr,
       "termStatCountTime": termStatCountTime,
       "termErroredSecond": termErroredSecond,
       "termSeverelyErroredSecond": termSeverelyErroredSecond,
       "termSyncLostTime": termSyncLostTime,
       "termAvailableTime": termAvailableTime,
       "termUnAvailableTime": termUnAvailableTime,
       "termBer": termBer,
       "berAlarm": berAlarm,
       "remoteAlarm": remoteAlarm,
       "systemAlarm": systemAlarm,
       "inputABCD": inputABCD,
       "outputABCD": outputABCD,
       "termBerInPwOf10": termBerInPwOf10,
       "outputMaskABCD": outputMaskABCD,
       "baseband": baseband,
       "bbVersion": bbVersion,
       "bbOperation": bbOperation,
       "bbLinkCapacity": bbLinkCapacity,
       "bbLinkCapacityDescription": bbLinkCapacityDescription,
       "bbLoopback": bbLoopback,
       "bbSyncLostAlarm": bbSyncLostAlarm,
       "radio1": radio1,
       "rf1Operation": rf1Operation,
       "rf1Alarm": rf1Alarm,
       "rf1Version": rf1Version,
       "rf1Side": rf1Side,
       "rf1Channel": rf1Channel,
       "rf1TxFrequency": rf1TxFrequency,
       "rf1RxFrequency": rf1RxFrequency,
       "rf1TxPower": rf1TxPower,
       "rf1RxState": rf1RxState,
       "rf1RxLevel": rf1RxLevel,
       "rf1CableAttenuation": rf1CableAttenuation,
       "rf1TxOut": rf1TxOut,
       "rf1TxPLL": rf1TxPLL,
       "rf1RxPLL": rf1RxPLL,
       "rf1OduTemperature": rf1OduTemperature,
       "rf1OduHumidity": rf1OduHumidity,
       "rf1Loopback": rf1Loopback,
       "rf1RxAlarmLevel": rf1RxAlarmLevel,
       "rf1txfstart": rf1txfstart,
       "rf1duplexshift": rf1duplexshift,
       "rf1chstep": rf1chstep,
       "rf1chstart": rf1chstart,
       "rf1chend": rf1chend,
       "rf1txpwmin": rf1txpwmin,
       "rf1txpwmax": rf1txpwmax,
       "rf1txpwstep": rf1txpwstep,
       "radio2": radio2,
       "rf2Operation": rf2Operation,
       "rf2Alarm": rf2Alarm,
       "rf2Version": rf2Version,
       "rf2Side": rf2Side,
       "rf2Channel": rf2Channel,
       "rf2TxFrequency": rf2TxFrequency,
       "rf2RxFrequency": rf2RxFrequency,
       "rf2TxPower": rf2TxPower,
       "rf2RxState": rf2RxState,
       "rf2RxLevel": rf2RxLevel,
       "rf2CableAttenuation": rf2CableAttenuation,
       "rf2TxOut": rf2TxOut,
       "rf2TxPLL": rf2TxPLL,
       "rf2RxPLL": rf2RxPLL,
       "rf2OduTemperature": rf2OduTemperature,
       "rf2OduHumidity": rf2OduHumidity,
       "rf2Loopback": rf2Loopback,
       "rf2RxAlarmLevel": rf2RxAlarmLevel,
       "rf2txfstart": rf2txfstart,
       "rf2duplexshift": rf2duplexshift,
       "rf2chstep": rf2chstep,
       "rf2chstart": rf2chstart,
       "rf2chend": rf2chend,
       "rf2txpwmin": rf2txpwmin,
       "rf2txpwmax": rf2txpwmax,
       "rf2txpwstep": rf2txpwstep,
       "switchCtrl": switchCtrl,
       "activeLink": activeLink,
       "activeTx": activeTx,
       "preferedLink": preferedLink,
       "forcedLink": forcedLink,
       "switchMode": switchMode,
       "odu1RxMax": odu1RxMax,
       "odu2RxMax": odu2RxMax,
       "odu1RxMin": odu1RxMin,
       "odu2RxMin": odu2RxMin,
       "rxDelta": rxDelta,
       "rxBER": rxBER,
       "switchDelay": switchDelay,
       "switchEnabledForRxBer": switchEnabledForRxBer,
       "switchReason": switchReason,
       "modules": modules,
       "m1": m1,
       "m1Type": m1Type,
       "m1Description": m1Description,
       "m1Version": m1Version,
       "m1Speed": m1Speed,
       "m1Operation": m1Operation,
       "m1Rx": m1Rx,
       "m1Tx": m1Tx,
       "m1Loopback": m1Loopback,
       "m1RxInput": m1RxInput,
       "m1TxMode": m1TxMode,
       "m1TxClockSource": m1TxClockSource,
       "m1TxClockPhase": m1TxClockPhase,
       "m1DataPolarity": m1DataPolarity,
       "m1ChanCount": m1ChanCount,
       "m1port1": m1port1,
       "m1p1statbin": m1p1statbin,
       "m1p1connection": m1p1connection,
       "m1p1flowcntrl": m1p1flowcntrl,
       "m1p1priority": m1p1priority,
       "m1p1loopback": m1p1loopback,
       "m1port2": m1port2,
       "m1p2statbin": m1p2statbin,
       "m1p2connection": m1p2connection,
       "m1p2flowcntrl": m1p2flowcntrl,
       "m1p2priority": m1p2priority,
       "m1p2loopback": m1p2loopback,
       "m1port3": m1port3,
       "m1p3statbin": m1p3statbin,
       "m1p3connection": m1p3connection,
       "m1p3flowcntrl": m1p3flowcntrl,
       "m1p3priority": m1p3priority,
       "m1p3loopback": m1p3loopback,
       "m1port4": m1port4,
       "m1p4statbin": m1p4statbin,
       "m1p4connection": m1p4connection,
       "m1p4flowcntrl": m1p4flowcntrl,
       "m1p4priority": m1p4priority,
       "m1p4loopback": m1p4loopback,
       "m2": m2,
       "m2Type": m2Type,
       "m2Description": m2Description,
       "m2Version": m2Version,
       "m2Speed": m2Speed,
       "m2Operation": m2Operation,
       "m2Rx": m2Rx,
       "m2Tx": m2Tx,
       "m2Loopback": m2Loopback,
       "m2RxInput": m2RxInput,
       "m2TxMode": m2TxMode,
       "m2TxClockSource": m2TxClockSource,
       "m2TxClockPhase": m2TxClockPhase,
       "m2DataPolarity": m2DataPolarity,
       "m2ChanCount": m2ChanCount,
       "m2port1": m2port1,
       "m2p1statbin": m2p1statbin,
       "m2p1connection": m2p1connection,
       "m2p1flowcntrl": m2p1flowcntrl,
       "m2p1priority": m2p1priority,
       "m2p1loopback": m2p1loopback,
       "m2port2": m2port2,
       "m2p2statbin": m2p2statbin,
       "m2p2connection": m2p2connection,
       "m2p2flowcntrl": m2p2flowcntrl,
       "m2p2priority": m2p2priority,
       "m2p2loopback": m2p2loopback,
       "m2port3": m2port3,
       "m2p3statbin": m2p3statbin,
       "m2p3connection": m2p3connection,
       "m2p3flowcntrl": m2p3flowcntrl,
       "m2p3priority": m2p3priority,
       "m2p3loopback": m2p3loopback,
       "m2port4": m2port4,
       "m2p4statbin": m2p4statbin,
       "m2p4connection": m2p4connection,
       "m2p4flowcntrl": m2p4flowcntrl,
       "m2p4priority": m2p4priority,
       "m2p4loopback": m2p4loopback,
       "m3": m3,
       "m3Type": m3Type,
       "m3Description": m3Description,
       "m3Version": m3Version,
       "m3Speed": m3Speed,
       "m3Operation": m3Operation,
       "m3Rx": m3Rx,
       "m3Tx": m3Tx,
       "m3Loopback": m3Loopback,
       "m3RxInput": m3RxInput,
       "m3TxMode": m3TxMode,
       "m3TxClockSource": m3TxClockSource,
       "m3TxClockPhase": m3TxClockPhase,
       "m3DataPolarity": m3DataPolarity,
       "m3ChanCount": m3ChanCount,
       "m3port1": m3port1,
       "m3p1statbin": m3p1statbin,
       "m3p1connection": m3p1connection,
       "m3p1flowcntrl": m3p1flowcntrl,
       "m3p1priority": m3p1priority,
       "m3p1loopback": m3p1loopback,
       "m3port2": m3port2,
       "m3p2statbin": m3p2statbin,
       "m3p2connection": m3p2connection,
       "m3p2flowcntrl": m3p2flowcntrl,
       "m3p2priority": m3p2priority,
       "m3p2loopback": m3p2loopback,
       "m3port3": m3port3,
       "m3p3statbin": m3p3statbin,
       "m3p3connection": m3p3connection,
       "m3p3flowcntrl": m3p3flowcntrl,
       "m3p3priority": m3p3priority,
       "m3p3loopback": m3p3loopback,
       "m3port4": m3port4,
       "m3p4statbin": m3p4statbin,
       "m3p4connection": m3p4connection,
       "m3p4flowcntrl": m3p4flowcntrl,
       "m3p4priority": m3p4priority,
       "m3p4loopback": m3p4loopback,
       "m4": m4,
       "m4Type": m4Type,
       "m4Description": m4Description,
       "m4Version": m4Version,
       "m4Speed": m4Speed,
       "m4Operation": m4Operation,
       "m4Rx": m4Rx,
       "m4Tx": m4Tx,
       "m4Loopback": m4Loopback,
       "m4RxInput": m4RxInput,
       "m4TxMode": m4TxMode,
       "m4TxClockSource": m4TxClockSource,
       "m4TxClockPhase": m4TxClockPhase,
       "m4DataPolarity": m4DataPolarity,
       "m4ChanCount": m4ChanCount,
       "m4port1": m4port1,
       "m4p1statbin": m4p1statbin,
       "m4p1connection": m4p1connection,
       "m4p1flowcntrl": m4p1flowcntrl,
       "m4p1priority": m4p1priority,
       "m4p1loopback": m4p1loopback,
       "m4port2": m4port2,
       "m4p2statbin": m4p2statbin,
       "m4p2connection": m4p2connection,
       "m4p2flowcntrl": m4p2flowcntrl,
       "m4p2priority": m4p2priority,
       "m4p2loopback": m4p2loopback,
       "m4port3": m4port3,
       "m4p3statbin": m4p3statbin,
       "m4p3connection": m4p3connection,
       "m4p3flowcntrl": m4p3flowcntrl,
       "m4p3priority": m4p3priority,
       "m4p3loopback": m4p3loopback,
       "m4port4": m4port4,
       "m4p4statbin": m4p4statbin,
       "m4p4connection": m4p4connection,
       "m4p4flowcntrl": m4p4flowcntrl,
       "m4p4priority": m4p4priority,
       "m4p4loopback": m4p4loopback}
)
