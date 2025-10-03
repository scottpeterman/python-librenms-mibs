# SNMP MIB module (IONODES-IONSERIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ionodes\IONODES-IONSERIES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:53 2025
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

ionSeriesModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AnalogVideoSignalLockState(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )



class AnalogVideoStandard(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntsc", 1),
          ("pal", 2))
    )



class DigitalVideoConnState(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notconnected", 2))
    )



class DigitalVideoStandard(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("hdmi720p", 1),
          ("hdmi720p50", 2),
          ("hdmi1080i", 3),
          ("hdmi1080i50", 4),
          ("hdmi1080p", 5),
          ("hdmi1080p50", 6),
          ("hdmi1080p25", 7),
          ("hdmi1080p30", 8))
    )



class StreamState(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notconnected", 2))
    )



class IoPinState(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Ionodes_ObjectIdentity = ObjectIdentity
ionodes = _Ionodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748)
)
_IonReg_ObjectIdentity = ObjectIdentity
ionReg = _IonReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1)
)
_IonModules_ObjectIdentity = ObjectIdentity
ionModules = _IonModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 1)
)
_IonConformance_ObjectIdentity = ObjectIdentity
ionConformance = _IonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 2)
)
_IonProducts_ObjectIdentity = ObjectIdentity
ionProducts = _IonProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3)
)
_IonIONSeries_ObjectIdentity = ObjectIdentity
ionIONSeries = _IonIONSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 1)
)
_IonE100_ObjectIdentity = ObjectIdentity
ionE100 = _IonE100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 1)
)
_IonE400_ObjectIdentity = ObjectIdentity
ionE400 = _IonE400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 2)
)
_IonE100Mini_ObjectIdentity = ObjectIdentity
ionE100Mini = _IonE100Mini_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 3)
)
_IonE100HD_ObjectIdentity = ObjectIdentity
ionE100HD = _IonE100HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 4)
)
_IonR100_ObjectIdentity = ObjectIdentity
ionR100 = _IonR100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 5)
)
_Tve110sd_ObjectIdentity = ObjectIdentity
tve110sd = _Tve110sd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 6)
)
_IonCIRRUSSeries_ObjectIdentity = ObjectIdentity
ionCIRRUSSeries = _IonCIRRUSSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 1, 3, 2)
)
_IonSystem_ObjectIdentity = ObjectIdentity
ionSystem = _IonSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 2)
)


class _IonSysCpuUsage_Type(Integer32):
    """Custom type ionSysCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IonSysCpuUsage_Type.__name__ = "Integer32"
_IonSysCpuUsage_Object = MibScalar
ionSysCpuUsage = _IonSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 40748, 2, 1),
    _IonSysCpuUsage_Type()
)
ionSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionSysCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    ionSysCpuUsage.setUnits("%")


class _IonSysMemUsage_Type(Integer32):
    """Custom type ionSysMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IonSysMemUsage_Type.__name__ = "Integer32"
_IonSysMemUsage_Object = MibScalar
ionSysMemUsage = _IonSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 40748, 2, 2),
    _IonSysMemUsage_Type()
)
ionSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionSysMemUsage.setStatus("current")
if mibBuilder.loadTexts:
    ionSysMemUsage.setUnits("%")
_IonSysTemperature_Type = Integer32
_IonSysTemperature_Object = MibScalar
ionSysTemperature = _IonSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40748, 2, 3),
    _IonSysTemperature_Type()
)
ionSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionSysTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ionSysTemperature.setUnits("Celcius")
_IonVideoInputs_ObjectIdentity = ObjectIdentity
ionVideoInputs = _IonVideoInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 3)
)
_IonVInNumber_Type = Integer32
_IonVInNumber_Object = MibScalar
ionVInNumber = _IonVInNumber_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 1),
    _IonVInNumber_Type()
)
ionVInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVInNumber.setStatus("current")
_IonVInTable_Object = MibTable
ionVInTable = _IonVInTable_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2)
)
if mibBuilder.loadTexts:
    ionVInTable.setStatus("current")
_IonVInEntry_Object = MibTableRow
ionVInEntry = _IonVInEntry_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2, 1)
)
ionVInEntry.setIndexNames(
    (0, "IONODES-IONSERIES-MIB", "ionVInIndex"),
)
if mibBuilder.loadTexts:
    ionVInEntry.setStatus("current")


class _IonVInIndex_Type(Integer32):
    """Custom type ionVInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IonVInIndex_Type.__name__ = "Integer32"
_IonVInIndex_Object = MibTableColumn
ionVInIndex = _IonVInIndex_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 1),
    _IonVInIndex_Type()
)
ionVInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVInIndex.setStatus("current")
_IonVInDescr_Type = OctetString
_IonVInDescr_Object = MibTableColumn
ionVInDescr = _IonVInDescr_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 2),
    _IonVInDescr_Type()
)
ionVInDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVInDescr.setStatus("current")
_IonVInAnalogSignalLock_Type = AnalogVideoSignalLockState
_IonVInAnalogSignalLock_Object = MibTableColumn
ionVInAnalogSignalLock = _IonVInAnalogSignalLock_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 3),
    _IonVInAnalogSignalLock_Type()
)
ionVInAnalogSignalLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVInAnalogSignalLock.setStatus("current")
_IonVInAnalogStandard_Type = AnalogVideoStandard
_IonVInAnalogStandard_Object = MibTableColumn
ionVInAnalogStandard = _IonVInAnalogStandard_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 4),
    _IonVInAnalogStandard_Type()
)
ionVInAnalogStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVInAnalogStandard.setStatus("current")
_IonVInDigitalConnState_Type = DigitalVideoConnState
_IonVInDigitalConnState_Object = MibTableColumn
ionVInDigitalConnState = _IonVInDigitalConnState_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 5),
    _IonVInDigitalConnState_Type()
)
ionVInDigitalConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVInDigitalConnState.setStatus("current")
_IonVInDigitalStandard_Type = DigitalVideoStandard
_IonVInDigitalStandard_Object = MibTableColumn
ionVInDigitalStandard = _IonVInDigitalStandard_Object(
    (1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 6),
    _IonVInDigitalStandard_Type()
)
ionVInDigitalStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVInDigitalStandard.setStatus("current")
_IonVideoOutputs_ObjectIdentity = ObjectIdentity
ionVideoOutputs = _IonVideoOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 4)
)
_IonVOutNumber_Type = Integer32
_IonVOutNumber_Object = MibScalar
ionVOutNumber = _IonVOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 1),
    _IonVOutNumber_Type()
)
ionVOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutNumber.setStatus("current")
_IonVOutTable_Object = MibTable
ionVOutTable = _IonVOutTable_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2)
)
if mibBuilder.loadTexts:
    ionVOutTable.setStatus("current")
_IonVOutEntry_Object = MibTableRow
ionVOutEntry = _IonVOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1)
)
ionVOutEntry.setIndexNames(
    (0, "IONODES-IONSERIES-MIB", "ionVOutIndex"),
)
if mibBuilder.loadTexts:
    ionVOutEntry.setStatus("current")


class _IonVOutIndex_Type(Integer32):
    """Custom type ionVOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IonVOutIndex_Type.__name__ = "Integer32"
_IonVOutIndex_Object = MibTableColumn
ionVOutIndex = _IonVOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 1),
    _IonVOutIndex_Type()
)
ionVOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutIndex.setStatus("current")
_IonVOutDescr_Type = OctetString
_IonVOutDescr_Object = MibTableColumn
ionVOutDescr = _IonVOutDescr_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 2),
    _IonVOutDescr_Type()
)
ionVOutDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutDescr.setStatus("current")
_IonVOutAnalogSignalLock_Type = AnalogVideoSignalLockState
_IonVOutAnalogSignalLock_Object = MibTableColumn
ionVOutAnalogSignalLock = _IonVOutAnalogSignalLock_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 3),
    _IonVOutAnalogSignalLock_Type()
)
ionVOutAnalogSignalLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutAnalogSignalLock.setStatus("current")
_IonVOutAnalogStandard_Type = AnalogVideoStandard
_IonVOutAnalogStandard_Object = MibTableColumn
ionVOutAnalogStandard = _IonVOutAnalogStandard_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 4),
    _IonVOutAnalogStandard_Type()
)
ionVOutAnalogStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutAnalogStandard.setStatus("current")
_IonVOutDigitalConnState_Type = DigitalVideoConnState
_IonVOutDigitalConnState_Object = MibTableColumn
ionVOutDigitalConnState = _IonVOutDigitalConnState_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 5),
    _IonVOutDigitalConnState_Type()
)
ionVOutDigitalConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutDigitalConnState.setStatus("current")
_IonVOutDigitalStandard_Type = DigitalVideoStandard
_IonVOutDigitalStandard_Object = MibTableColumn
ionVOutDigitalStandard = _IonVOutDigitalStandard_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 6),
    _IonVOutDigitalStandard_Type()
)
ionVOutDigitalStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutDigitalStandard.setStatus("current")
_IonVOutStream1State_Type = StreamState
_IonVOutStream1State_Object = MibTableColumn
ionVOutStream1State = _IonVOutStream1State_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 7),
    _IonVOutStream1State_Type()
)
ionVOutStream1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutStream1State.setStatus("current")
_IonVOutStream2State_Type = StreamState
_IonVOutStream2State_Object = MibTableColumn
ionVOutStream2State = _IonVOutStream2State_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 8),
    _IonVOutStream2State_Type()
)
ionVOutStream2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutStream2State.setStatus("current")
_IonVOutStream3State_Type = StreamState
_IonVOutStream3State_Object = MibTableColumn
ionVOutStream3State = _IonVOutStream3State_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 9),
    _IonVOutStream3State_Type()
)
ionVOutStream3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutStream3State.setStatus("current")
_IonVOutStream4State_Type = StreamState
_IonVOutStream4State_Object = MibTableColumn
ionVOutStream4State = _IonVOutStream4State_Object(
    (1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 10),
    _IonVOutStream4State_Type()
)
ionVOutStream4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionVOutStream4State.setStatus("current")
_IonAudioInputs_ObjectIdentity = ObjectIdentity
ionAudioInputs = _IonAudioInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 5)
)
_IonAudioOutputs_ObjectIdentity = ObjectIdentity
ionAudioOutputs = _IonAudioOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 6)
)
_IonIoInputs_ObjectIdentity = ObjectIdentity
ionIoInputs = _IonIoInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 7)
)
_IonIoInNumber_Type = Integer32
_IonIoInNumber_Object = MibScalar
ionIoInNumber = _IonIoInNumber_Object(
    (1, 3, 6, 1, 4, 1, 40748, 7, 1),
    _IonIoInNumber_Type()
)
ionIoInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoInNumber.setStatus("current")
_IonIoInTable_Object = MibTable
ionIoInTable = _IonIoInTable_Object(
    (1, 3, 6, 1, 4, 1, 40748, 7, 2)
)
if mibBuilder.loadTexts:
    ionIoInTable.setStatus("current")
_IonIoInEntry_Object = MibTableRow
ionIoInEntry = _IonIoInEntry_Object(
    (1, 3, 6, 1, 4, 1, 40748, 7, 2, 1)
)
ionIoInEntry.setIndexNames(
    (0, "IONODES-IONSERIES-MIB", "ionIoInIndex"),
)
if mibBuilder.loadTexts:
    ionIoInEntry.setStatus("current")


class _IonIoInIndex_Type(Integer32):
    """Custom type ionIoInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IonIoInIndex_Type.__name__ = "Integer32"
_IonIoInIndex_Object = MibTableColumn
ionIoInIndex = _IonIoInIndex_Object(
    (1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 1),
    _IonIoInIndex_Type()
)
ionIoInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoInIndex.setStatus("current")
_IonIoInDescr_Type = OctetString
_IonIoInDescr_Object = MibTableColumn
ionIoInDescr = _IonIoInDescr_Object(
    (1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 2),
    _IonIoInDescr_Type()
)
ionIoInDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoInDescr.setStatus("current")
_IonIoInPinState_Type = IoPinState
_IonIoInPinState_Object = MibTableColumn
ionIoInPinState = _IonIoInPinState_Object(
    (1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 3),
    _IonIoInPinState_Type()
)
ionIoInPinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoInPinState.setStatus("current")
_IonIoOutputs_ObjectIdentity = ObjectIdentity
ionIoOutputs = _IonIoOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 8)
)
_IonIoOutNumber_Type = Integer32
_IonIoOutNumber_Object = MibScalar
ionIoOutNumber = _IonIoOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 40748, 8, 1),
    _IonIoOutNumber_Type()
)
ionIoOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoOutNumber.setStatus("current")
_IonIoOutTable_Object = MibTable
ionIoOutTable = _IonIoOutTable_Object(
    (1, 3, 6, 1, 4, 1, 40748, 8, 2)
)
if mibBuilder.loadTexts:
    ionIoOutTable.setStatus("current")
_IonIoOutEntry_Object = MibTableRow
ionIoOutEntry = _IonIoOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 40748, 8, 2, 1)
)
ionIoOutEntry.setIndexNames(
    (0, "IONODES-IONSERIES-MIB", "ionIoOutIndex"),
)
if mibBuilder.loadTexts:
    ionIoOutEntry.setStatus("current")


class _IonIoOutIndex_Type(Integer32):
    """Custom type ionIoOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IonIoOutIndex_Type.__name__ = "Integer32"
_IonIoOutIndex_Object = MibTableColumn
ionIoOutIndex = _IonIoOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 1),
    _IonIoOutIndex_Type()
)
ionIoOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoOutIndex.setStatus("current")
_IonIoOutDescr_Type = OctetString
_IonIoOutDescr_Object = MibTableColumn
ionIoOutDescr = _IonIoOutDescr_Object(
    (1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 2),
    _IonIoOutDescr_Type()
)
ionIoOutDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoOutDescr.setStatus("current")
_IonIoOutPinState_Type = IoPinState
_IonIoOutPinState_Object = MibTableColumn
ionIoOutPinState = _IonIoOutPinState_Object(
    (1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 3),
    _IonIoOutPinState_Type()
)
ionIoOutPinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ionIoOutPinState.setStatus("current")
_IonSerialPorts_ObjectIdentity = ObjectIdentity
ionSerialPorts = _IonSerialPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40748, 9)
)

# Managed Objects groups

ionObjectGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 40748, 1, 2, 1)
)
ionObjectGroups.setObjects(
      *(("IONODES-IONSERIES-MIB", "ionSysCpuUsage"),
        ("IONODES-IONSERIES-MIB", "ionSysMemUsage"),
        ("IONODES-IONSERIES-MIB", "ionSysTemperature"),
        ("IONODES-IONSERIES-MIB", "ionVInNumber"),
        ("IONODES-IONSERIES-MIB", "ionVInIndex"),
        ("IONODES-IONSERIES-MIB", "ionVInDescr"),
        ("IONODES-IONSERIES-MIB", "ionVInAnalogSignalLock"),
        ("IONODES-IONSERIES-MIB", "ionVInAnalogStandard"))
)
if mibBuilder.loadTexts:
    ionObjectGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IONODES-IONSERIES-MIB",
    **{"AnalogVideoSignalLockState": AnalogVideoSignalLockState,
       "AnalogVideoStandard": AnalogVideoStandard,
       "DigitalVideoConnState": DigitalVideoConnState,
       "DigitalVideoStandard": DigitalVideoStandard,
       "StreamState": StreamState,
       "IoPinState": IoPinState,
       "ionodes": ionodes,
       "ionReg": ionReg,
       "ionModules": ionModules,
       "ionSeriesModule": ionSeriesModule,
       "ionConformance": ionConformance,
       "ionObjectGroups": ionObjectGroups,
       "ionProducts": ionProducts,
       "ionIONSeries": ionIONSeries,
       "ionE100": ionE100,
       "ionE400": ionE400,
       "ionE100Mini": ionE100Mini,
       "ionE100HD": ionE100HD,
       "ionR100": ionR100,
       "tve110sd": tve110sd,
       "ionCIRRUSSeries": ionCIRRUSSeries,
       "ionSystem": ionSystem,
       "ionSysCpuUsage": ionSysCpuUsage,
       "ionSysMemUsage": ionSysMemUsage,
       "ionSysTemperature": ionSysTemperature,
       "ionVideoInputs": ionVideoInputs,
       "ionVInNumber": ionVInNumber,
       "ionVInTable": ionVInTable,
       "ionVInEntry": ionVInEntry,
       "ionVInIndex": ionVInIndex,
       "ionVInDescr": ionVInDescr,
       "ionVInAnalogSignalLock": ionVInAnalogSignalLock,
       "ionVInAnalogStandard": ionVInAnalogStandard,
       "ionVInDigitalConnState": ionVInDigitalConnState,
       "ionVInDigitalStandard": ionVInDigitalStandard,
       "ionVideoOutputs": ionVideoOutputs,
       "ionVOutNumber": ionVOutNumber,
       "ionVOutTable": ionVOutTable,
       "ionVOutEntry": ionVOutEntry,
       "ionVOutIndex": ionVOutIndex,
       "ionVOutDescr": ionVOutDescr,
       "ionVOutAnalogSignalLock": ionVOutAnalogSignalLock,
       "ionVOutAnalogStandard": ionVOutAnalogStandard,
       "ionVOutDigitalConnState": ionVOutDigitalConnState,
       "ionVOutDigitalStandard": ionVOutDigitalStandard,
       "ionVOutStream1State": ionVOutStream1State,
       "ionVOutStream2State": ionVOutStream2State,
       "ionVOutStream3State": ionVOutStream3State,
       "ionVOutStream4State": ionVOutStream4State,
       "ionAudioInputs": ionAudioInputs,
       "ionAudioOutputs": ionAudioOutputs,
       "ionIoInputs": ionIoInputs,
       "ionIoInNumber": ionIoInNumber,
       "ionIoInTable": ionIoInTable,
       "ionIoInEntry": ionIoInEntry,
       "ionIoInIndex": ionIoInIndex,
       "ionIoInDescr": ionIoInDescr,
       "ionIoInPinState": ionIoInPinState,
       "ionIoOutputs": ionIoOutputs,
       "ionIoOutNumber": ionIoOutNumber,
       "ionIoOutTable": ionIoOutTable,
       "ionIoOutEntry": ionIoOutEntry,
       "ionIoOutIndex": ionIoOutIndex,
       "ionIoOutDescr": ionIoOutDescr,
       "ionIoOutPinState": ionIoOutPinState,
       "ionSerialPorts": ionSerialPorts}
)
