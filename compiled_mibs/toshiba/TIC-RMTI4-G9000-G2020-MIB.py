# SNMP MIB module (TIC-RMTI4-G9000-G2020-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\toshiba\TIC-RMTI4-G9000-G2020-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:17 2025
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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Toshiba_ObjectIdentity = ObjectIdentity
toshiba = _Toshiba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186)
)
_Equ_ObjectIdentity = ObjectIdentity
equ = _Equ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1)
)
_EquUPS_ObjectIdentity = ObjectIdentity
equUPS = _EquUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19)
)
_TicUPS_ObjectIdentity = ObjectIdentity
ticUPS = _TicUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2)
)
_Rmti4_ObjectIdentity = ObjectIdentity
rmti4 = _Rmti4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5)
)
_UpsG9000_G2020_ObjectIdentity = ObjectIdentity
upsG9000_G2020 = _UpsG9000_G2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 1)
)


class _UpsIdentManufacturer_Type(DisplayString):
    """Custom type upsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentManufacturer_Type.__name__ = "DisplayString"
_UpsIdentManufacturer_Object = MibScalar
upsIdentManufacturer = _UpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 1, 1),
    _UpsIdentManufacturer_Type()
)
upsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturer.setStatus("mandatory")


class _UpsIdentTypeform_Type(DisplayString):
    """Custom type upsIdentTypeform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UpsIdentTypeform_Type.__name__ = "DisplayString"
_UpsIdentTypeform_Object = MibScalar
upsIdentTypeform = _UpsIdentTypeform_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 1, 2),
    _UpsIdentTypeform_Type()
)
upsIdentTypeform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentTypeform.setStatus("mandatory")


class _UpsIdentUPSFirmwareVersion_Type(DisplayString):
    """Custom type upsIdentUPSFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentUPSFirmwareVersion_Type.__name__ = "DisplayString"
_UpsIdentUPSFirmwareVersion_Object = MibScalar
upsIdentUPSFirmwareVersion = _UpsIdentUPSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 1, 3),
    _UpsIdentUPSFirmwareVersion_Type()
)
upsIdentUPSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentUPSFirmwareVersion.setStatus("mandatory")


class _UpsIdentSysName_Type(DisplayString):
    """Custom type upsIdentSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentSysName_Type.__name__ = "DisplayString"
_UpsIdentSysName_Object = MibScalar
upsIdentSysName = _UpsIdentSysName_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 1, 4),
    _UpsIdentSysName_Type()
)
upsIdentSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentSysName.setStatus("mandatory")


class _UpsIdentAttachedDevices_Type(DisplayString):
    """Custom type upsIdentAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentAttachedDevices_Type.__name__ = "DisplayString"
_UpsIdentAttachedDevices_Object = MibScalar
upsIdentAttachedDevices = _UpsIdentAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 1, 5),
    _UpsIdentAttachedDevices_Type()
)
upsIdentAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentAttachedDevices.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2)
)
_UpsInputNumOfPhases_Type = NonNegativeInteger
_UpsInputNumOfPhases_Object = MibScalar
upsInputNumOfPhases = _UpsInputNumOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 1),
    _UpsInputNumOfPhases_Type()
)
upsInputNumOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumOfPhases.setStatus("mandatory")
_UpsInputLLVoltageAB_Type = NonNegativeInteger
_UpsInputLLVoltageAB_Object = MibScalar
upsInputLLVoltageAB = _UpsInputLLVoltageAB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 2),
    _UpsInputLLVoltageAB_Type()
)
upsInputLLVoltageAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLLVoltageAB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputLLVoltageAB.setUnits("RMS Volts")
_UpsInputLLVoltageBC_Type = NonNegativeInteger
_UpsInputLLVoltageBC_Object = MibScalar
upsInputLLVoltageBC = _UpsInputLLVoltageBC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 3),
    _UpsInputLLVoltageBC_Type()
)
upsInputLLVoltageBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLLVoltageBC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputLLVoltageBC.setUnits("RMS Volts")
_UpsInputLLVoltageCA_Type = NonNegativeInteger
_UpsInputLLVoltageCA_Object = MibScalar
upsInputLLVoltageCA = _UpsInputLLVoltageCA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 4),
    _UpsInputLLVoltageCA_Type()
)
upsInputLLVoltageCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLLVoltageCA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputLLVoltageCA.setUnits("RMS Volts")
_UpsInputLLVoltagePercentAB_Type = NonNegativeInteger
_UpsInputLLVoltagePercentAB_Object = MibScalar
upsInputLLVoltagePercentAB = _UpsInputLLVoltagePercentAB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 5),
    _UpsInputLLVoltagePercentAB_Type()
)
upsInputLLVoltagePercentAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLLVoltagePercentAB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputLLVoltagePercentAB.setUnits("Percentage")
_UpsInputLLVoltagePercentBC_Type = NonNegativeInteger
_UpsInputLLVoltagePercentBC_Object = MibScalar
upsInputLLVoltagePercentBC = _UpsInputLLVoltagePercentBC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 6),
    _UpsInputLLVoltagePercentBC_Type()
)
upsInputLLVoltagePercentBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLLVoltagePercentBC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputLLVoltagePercentBC.setUnits("Percentage")
_UpsInputLLVoltagePercentCA_Type = NonNegativeInteger
_UpsInputLLVoltagePercentCA_Object = MibScalar
upsInputLLVoltagePercentCA = _UpsInputLLVoltagePercentCA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 7),
    _UpsInputLLVoltagePercentCA_Type()
)
upsInputLLVoltagePercentCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLLVoltagePercentCA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputLLVoltagePercentCA.setUnits("Percentage")
_UpsInputCurrentPhaseA_Type = NonNegativeInteger
_UpsInputCurrentPhaseA_Object = MibScalar
upsInputCurrentPhaseA = _UpsInputCurrentPhaseA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 8),
    _UpsInputCurrentPhaseA_Type()
)
upsInputCurrentPhaseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentPhaseA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputCurrentPhaseA.setUnits("0.1 RMS Amps")
_UpsInputCurrentPhaseB_Type = NonNegativeInteger
_UpsInputCurrentPhaseB_Object = MibScalar
upsInputCurrentPhaseB = _UpsInputCurrentPhaseB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 9),
    _UpsInputCurrentPhaseB_Type()
)
upsInputCurrentPhaseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentPhaseB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputCurrentPhaseB.setUnits("0.1 RMS Amps")
_UpsInputCurrentPhaseC_Type = NonNegativeInteger
_UpsInputCurrentPhaseC_Object = MibScalar
upsInputCurrentPhaseC = _UpsInputCurrentPhaseC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 10),
    _UpsInputCurrentPhaseC_Type()
)
upsInputCurrentPhaseC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrentPhaseC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputCurrentPhaseC.setUnits("0.1 RMS Amps")
_UpsInputFrequency_Type = NonNegativeInteger
_UpsInputFrequency_Object = MibScalar
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 11),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputFrequency.setUnits("0.1 Hertz")
_UpsInputActivePowerA_Type = NonNegativeInteger
_UpsInputActivePowerA_Object = MibScalar
upsInputActivePowerA = _UpsInputActivePowerA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 12),
    _UpsInputActivePowerA_Type()
)
upsInputActivePowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputActivePowerA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputActivePowerA.setUnits("Watts")
_UpsInputActivePowerB_Type = NonNegativeInteger
_UpsInputActivePowerB_Object = MibScalar
upsInputActivePowerB = _UpsInputActivePowerB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 13),
    _UpsInputActivePowerB_Type()
)
upsInputActivePowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputActivePowerB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputActivePowerB.setUnits("Watts")
_UpsInputActivePowerC_Type = NonNegativeInteger
_UpsInputActivePowerC_Object = MibScalar
upsInputActivePowerC = _UpsInputActivePowerC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 14),
    _UpsInputActivePowerC_Type()
)
upsInputActivePowerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputActivePowerC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputActivePowerC.setUnits("Watts")
_UpsInputTotalActivePower_Type = NonNegativeInteger
_UpsInputTotalActivePower_Object = MibScalar
upsInputTotalActivePower = _UpsInputTotalActivePower_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 15),
    _UpsInputTotalActivePower_Type()
)
upsInputTotalActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputTotalActivePower.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputTotalActivePower.setUnits("Watts")
_UpsInputRatedLLVoltage_Type = NonNegativeInteger
_UpsInputRatedLLVoltage_Object = MibScalar
upsInputRatedLLVoltage = _UpsInputRatedLLVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 2, 16),
    _UpsInputRatedLLVoltage_Type()
)
upsInputRatedLLVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputRatedLLVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsInputRatedLLVoltage.setUnits("RMS Volts")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3)
)


class _UpsOutputSource_Type(Integer32):
    """Custom type upsOutputSource based on Integer32"""
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
        *(("other", 1),
          ("none", 2),
          ("normal", 3),
          ("bypass", 4),
          ("battery", 5))
    )


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 1),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("mandatory")
_UpsOutputNumOfPhases_Type = NonNegativeInteger
_UpsOutputNumOfPhases_Object = MibScalar
upsOutputNumOfPhases = _UpsOutputNumOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 2),
    _UpsOutputNumOfPhases_Type()
)
upsOutputNumOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumOfPhases.setStatus("mandatory")
_UpsOutputLLVoltageAB_Type = NonNegativeInteger
_UpsOutputLLVoltageAB_Object = MibScalar
upsOutputLLVoltageAB = _UpsOutputLLVoltageAB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 3),
    _UpsOutputLLVoltageAB_Type()
)
upsOutputLLVoltageAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLLVoltageAB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputLLVoltageAB.setUnits("RMS Volts")
_UpsOutputLLVoltageBC_Type = NonNegativeInteger
_UpsOutputLLVoltageBC_Object = MibScalar
upsOutputLLVoltageBC = _UpsOutputLLVoltageBC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 4),
    _UpsOutputLLVoltageBC_Type()
)
upsOutputLLVoltageBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLLVoltageBC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputLLVoltageBC.setUnits("RMS Volts")
_UpsOutputLLVoltageCA_Type = NonNegativeInteger
_UpsOutputLLVoltageCA_Object = MibScalar
upsOutputLLVoltageCA = _UpsOutputLLVoltageCA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 5),
    _UpsOutputLLVoltageCA_Type()
)
upsOutputLLVoltageCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLLVoltageCA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputLLVoltageCA.setUnits("RMS Volts")
_UpsOutputCurrentPhaseA_Type = NonNegativeInteger
_UpsOutputCurrentPhaseA_Object = MibScalar
upsOutputCurrentPhaseA = _UpsOutputCurrentPhaseA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 6),
    _UpsOutputCurrentPhaseA_Type()
)
upsOutputCurrentPhaseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentPhaseA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputCurrentPhaseA.setUnits("RMS Amps")
_UpsOutputCurrentPhaseB_Type = NonNegativeInteger
_UpsOutputCurrentPhaseB_Object = MibScalar
upsOutputCurrentPhaseB = _UpsOutputCurrentPhaseB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 7),
    _UpsOutputCurrentPhaseB_Type()
)
upsOutputCurrentPhaseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentPhaseB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputCurrentPhaseB.setUnits("RMS Amps")
_UpsOutputCurrentPhaseC_Type = NonNegativeInteger
_UpsOutputCurrentPhaseC_Object = MibScalar
upsOutputCurrentPhaseC = _UpsOutputCurrentPhaseC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 8),
    _UpsOutputCurrentPhaseC_Type()
)
upsOutputCurrentPhaseC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentPhaseC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputCurrentPhaseC.setUnits("RMS Amps")
_UpsOutputFrequency_Type = NonNegativeInteger
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 9),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputFrequency.setUnits("0.1 Hertz")
_UpsOutputCurrentPercentA_Type = Integer32
_UpsOutputCurrentPercentA_Object = MibScalar
upsOutputCurrentPercentA = _UpsOutputCurrentPercentA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 10),
    _UpsOutputCurrentPercentA_Type()
)
upsOutputCurrentPercentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentPercentA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputCurrentPercentA.setUnits("PERCENT")
_UpsOutputCurrentPercentB_Type = Integer32
_UpsOutputCurrentPercentB_Object = MibScalar
upsOutputCurrentPercentB = _UpsOutputCurrentPercentB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 11),
    _UpsOutputCurrentPercentB_Type()
)
upsOutputCurrentPercentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentPercentB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputCurrentPercentB.setUnits("PERCENT")
_UpsOutputCurrentPercentC_Type = Integer32
_UpsOutputCurrentPercentC_Object = MibScalar
upsOutputCurrentPercentC = _UpsOutputCurrentPercentC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 12),
    _UpsOutputCurrentPercentC_Type()
)
upsOutputCurrentPercentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrentPercentC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputCurrentPercentC.setUnits("PERCENT")
_UpsOutputTotalActivePower_Type = NonNegativeInteger
_UpsOutputTotalActivePower_Object = MibScalar
upsOutputTotalActivePower = _UpsOutputTotalActivePower_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 13),
    _UpsOutputTotalActivePower_Type()
)
upsOutputTotalActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputTotalActivePower.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputTotalActivePower.setUnits("kWatts")
_UpsOutputTotalActivePowerPercent_Type = NonNegativeInteger
_UpsOutputTotalActivePowerPercent_Object = MibScalar
upsOutputTotalActivePowerPercent = _UpsOutputTotalActivePowerPercent_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 14),
    _UpsOutputTotalActivePowerPercent_Type()
)
upsOutputTotalActivePowerPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputTotalActivePowerPercent.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputTotalActivePowerPercent.setUnits("percentage")
_UpsOutputPowerFactor_Type = NonNegativeInteger
_UpsOutputPowerFactor_Object = MibScalar
upsOutputPowerFactor = _UpsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 15),
    _UpsOutputPowerFactor_Type()
)
upsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPowerFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputPowerFactor.setUnits("0.01")
_UpsOutputRatedActivePower_Type = NonNegativeInteger
_UpsOutputRatedActivePower_Object = MibScalar
upsOutputRatedActivePower = _UpsOutputRatedActivePower_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 16),
    _UpsOutputRatedActivePower_Type()
)
upsOutputRatedActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputRatedActivePower.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputRatedActivePower.setUnits("Watts")
_UpsOutputRatedApparentPower_Type = NonNegativeInteger
_UpsOutputRatedApparentPower_Object = MibScalar
upsOutputRatedApparentPower = _UpsOutputRatedApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 17),
    _UpsOutputRatedApparentPower_Type()
)
upsOutputRatedApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputRatedApparentPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputRatedApparentPower.setUnits("VA")
_UpsOutputRatedLLVoltage_Type = NonNegativeInteger
_UpsOutputRatedLLVoltage_Object = MibScalar
upsOutputRatedLLVoltage = _UpsOutputRatedLLVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 3, 18),
    _UpsOutputRatedLLVoltage_Type()
)
upsOutputRatedLLVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputRatedLLVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsOutputRatedLLVoltage.setUnits("RMS Volts")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 4)
)
_UpsBypassNumOfPhases_Type = NonNegativeInteger
_UpsBypassNumOfPhases_Object = MibScalar
upsBypassNumOfPhases = _UpsBypassNumOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 4, 1),
    _UpsBypassNumOfPhases_Type()
)
upsBypassNumOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumOfPhases.setStatus("mandatory")
_UpsBypassLLVoltageAB_Type = NonNegativeInteger
_UpsBypassLLVoltageAB_Object = MibScalar
upsBypassLLVoltageAB = _UpsBypassLLVoltageAB_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 4, 2),
    _UpsBypassLLVoltageAB_Type()
)
upsBypassLLVoltageAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassLLVoltageAB.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBypassLLVoltageAB.setUnits("RMS Volts")
_UpsBypassLLVoltageBC_Type = NonNegativeInteger
_UpsBypassLLVoltageBC_Object = MibScalar
upsBypassLLVoltageBC = _UpsBypassLLVoltageBC_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 4, 3),
    _UpsBypassLLVoltageBC_Type()
)
upsBypassLLVoltageBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassLLVoltageBC.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBypassLLVoltageBC.setUnits("RMS Volts")
_UpsBypassLLVoltageCA_Type = NonNegativeInteger
_UpsBypassLLVoltageCA_Object = MibScalar
upsBypassLLVoltageCA = _UpsBypassLLVoltageCA_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 4, 4),
    _UpsBypassLLVoltageCA_Type()
)
upsBypassLLVoltageCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassLLVoltageCA.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBypassLLVoltageCA.setUnits("RMS Volts")
_UpsBypassFrequency_Type = NonNegativeInteger
_UpsBypassFrequency_Object = MibScalar
upsBypassFrequency = _UpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 4, 5),
    _UpsBypassFrequency_Type()
)
upsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBypassFrequency.setUnits("0.1 Hertz")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5)
)


class _UpsBatteryStatus_Type(Integer32):
    """Custom type upsBatteryStatus based on Integer32"""
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
          ("batteryNormal", 2),
          ("batteryLow", 3),
          ("batteryDepleted", 4),
          ("batteryDischarging", 5),
          ("batteryFailure", 6))
    )


_UpsBatteryStatus_Type.__name__ = "Integer32"
_UpsBatteryStatus_Object = MibScalar
upsBatteryStatus = _UpsBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 1),
    _UpsBatteryStatus_Type()
)
upsBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStatus.setStatus("mandatory")
_UpsElapsedTimeOnBatteryPower_Type = NonNegativeInteger
_UpsElapsedTimeOnBatteryPower_Object = MibScalar
upsElapsedTimeOnBatteryPower = _UpsElapsedTimeOnBatteryPower_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 2),
    _UpsElapsedTimeOnBatteryPower_Type()
)
upsElapsedTimeOnBatteryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsElapsedTimeOnBatteryPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsElapsedTimeOnBatteryPower.setUnits("seconds")
_UpsEstimatedBatteryRuntime_Type = PositiveInteger
_UpsEstimatedBatteryRuntime_Object = MibScalar
upsEstimatedBatteryRuntime = _UpsEstimatedBatteryRuntime_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 3),
    _UpsEstimatedBatteryRuntime_Type()
)
upsEstimatedBatteryRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEstimatedBatteryRuntime.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsEstimatedBatteryRuntime.setUnits("minutes")
_UpsBatteryVoltage_Type = NonNegativeInteger
_UpsBatteryVoltage_Object = MibScalar
upsBatteryVoltage = _UpsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 4),
    _UpsBatteryVoltage_Type()
)
upsBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBatteryVoltage.setUnits("Volt DC")
_UpsBatteryVoltagePercent_Type = NonNegativeInteger
_UpsBatteryVoltagePercent_Object = MibScalar
upsBatteryVoltagePercent = _UpsBatteryVoltagePercent_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 5),
    _UpsBatteryVoltagePercent_Type()
)
upsBatteryVoltagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltagePercent.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBatteryVoltagePercent.setUnits("percentage")


class _UpsBatteryEstimatedCharge_Type(Integer32):
    """Custom type upsBatteryEstimatedCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsBatteryEstimatedCharge_Type.__name__ = "Integer32"
_UpsBatteryEstimatedCharge_Object = MibScalar
upsBatteryEstimatedCharge = _UpsBatteryEstimatedCharge_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 6),
    _UpsBatteryEstimatedCharge_Type()
)
upsBatteryEstimatedCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryEstimatedCharge.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBatteryEstimatedCharge.setUnits("percentage")
_UpsBatteryDischargeCurrent_Type = Integer32
_UpsBatteryDischargeCurrent_Object = MibScalar
upsBatteryDischargeCurrent = _UpsBatteryDischargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 7),
    _UpsBatteryDischargeCurrent_Type()
)
upsBatteryDischargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryDischargeCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBatteryDischargeCurrent.setUnits("percentage")
_UpsBatteryChargeCurrent_Type = Integer32
_UpsBatteryChargeCurrent_Object = MibScalar
upsBatteryChargeCurrent = _UpsBatteryChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 8),
    _UpsBatteryChargeCurrent_Type()
)
upsBatteryChargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryChargeCurrent.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBatteryChargeCurrent.setUnits("percentage")


class _UpsBatteryModel_Type(DisplayString):
    """Custom type upsBatteryModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsBatteryModel_Type.__name__ = "DisplayString"
_UpsBatteryModel_Object = MibScalar
upsBatteryModel = _UpsBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 9),
    _UpsBatteryModel_Type()
)
upsBatteryModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryModel.setStatus("mandatory")
_UpsBatteryInSeries_Type = NonNegativeInteger
_UpsBatteryInSeries_Object = MibScalar
upsBatteryInSeries = _UpsBatteryInSeries_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 10),
    _UpsBatteryInSeries_Type()
)
upsBatteryInSeries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryInSeries.setStatus("mandatory")
_UpsBatteryNumStrings_Type = NonNegativeInteger
_UpsBatteryNumStrings_Object = MibScalar
upsBatteryNumStrings = _UpsBatteryNumStrings_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 11),
    _UpsBatteryNumStrings_Type()
)
upsBatteryNumStrings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryNumStrings.setStatus("mandatory")
_UpsBatteryRatedAmpereHour_Type = NonNegativeInteger
_UpsBatteryRatedAmpereHour_Object = MibScalar
upsBatteryRatedAmpereHour = _UpsBatteryRatedAmpereHour_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 12),
    _UpsBatteryRatedAmpereHour_Type()
)
upsBatteryRatedAmpereHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryRatedAmpereHour.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBatteryRatedAmpereHour.setUnits("Ampere Hour")


class _UpsBatteryRatedBackupTime_Type(DisplayString):
    """Custom type upsBatteryRatedBackupTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_UpsBatteryRatedBackupTime_Type.__name__ = "DisplayString"
_UpsBatteryRatedBackupTime_Object = MibScalar
upsBatteryRatedBackupTime = _UpsBatteryRatedBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 13),
    _UpsBatteryRatedBackupTime_Type()
)
upsBatteryRatedBackupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryRatedBackupTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsBatteryRatedBackupTime.setUnits("minutes")


class _UpsBatteryInstallationDate_Type(DisplayString):
    """Custom type upsBatteryInstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_UpsBatteryInstallationDate_Type.__name__ = "DisplayString"
_UpsBatteryInstallationDate_Object = MibScalar
upsBatteryInstallationDate = _UpsBatteryInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 5, 14),
    _UpsBatteryInstallationDate_Type()
)
upsBatteryInstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryInstallationDate.setStatus("mandatory")
_UpsAlarm_ObjectIdentity = ObjectIdentity
upsAlarm = _UpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6)
)
_UpsAlarmsPresent_Type = Gauge32
_UpsAlarmsPresent_Object = MibScalar
upsAlarmsPresent = _UpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 1),
    _UpsAlarmsPresent_Type()
)
upsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmsPresent.setStatus("mandatory")
_UpsAlarmTable_Object = MibTable
upsAlarmTable = _UpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 2)
)
if mibBuilder.loadTexts:
    upsAlarmTable.setStatus("mandatory")
_UpsAlarmEntry_Object = MibTableRow
upsAlarmEntry = _UpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 2, 1)
)
upsAlarmEntry.setIndexNames(
    (0, "TIC-RMTI4-G9000-G2020-MIB", "upsAlarmId"),
)
if mibBuilder.loadTexts:
    upsAlarmEntry.setStatus("mandatory")
_UpsAlarmId_Type = PositiveInteger
_UpsAlarmId_Object = MibTableColumn
upsAlarmId = _UpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 2, 1, 1),
    _UpsAlarmId_Type()
)
upsAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upsAlarmId.setStatus("mandatory")
_UpsAlarmDescr_Type = AutonomousType
_UpsAlarmDescr_Object = MibTableColumn
upsAlarmDescr = _UpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 2, 1, 2),
    _UpsAlarmDescr_Type()
)
upsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDescr.setStatus("mandatory")
_UpsAlarmTime_Type = TimeStamp
_UpsAlarmTime_Object = MibTableColumn
upsAlarmTime = _UpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 2, 1, 3),
    _UpsAlarmTime_Type()
)
upsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmTime.setStatus("mandatory")
_UpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
upsWellKnownAlarms = _UpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3)
)
_UpsAlarmFault_Type = Integer32
_UpsAlarmFault_Object = MibScalar
upsAlarmFault = _UpsAlarmFault_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 1),
    _UpsAlarmFault_Type()
)
upsAlarmFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmFault.setStatus("mandatory")
_UpsAlarmOnBattery_Type = Integer32
_UpsAlarmOnBattery_Object = MibScalar
upsAlarmOnBattery = _UpsAlarmOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 2),
    _UpsAlarmOnBattery_Type()
)
upsAlarmOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBattery.setStatus("mandatory")
_UpsAlarmBatteryLow_Type = Integer32
_UpsAlarmBatteryLow_Object = MibScalar
upsAlarmBatteryLow = _UpsAlarmBatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 3),
    _UpsAlarmBatteryLow_Type()
)
upsAlarmBatteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryLow.setStatus("mandatory")
_UpsAlarmBatteryDepleted_Type = Integer32
_UpsAlarmBatteryDepleted_Object = MibScalar
upsAlarmBatteryDepleted = _UpsAlarmBatteryDepleted_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 4),
    _UpsAlarmBatteryDepleted_Type()
)
upsAlarmBatteryDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryDepleted.setStatus("mandatory")
_UpsAlarmBatteryOverheat_Type = Integer32
_UpsAlarmBatteryOverheat_Object = MibScalar
upsAlarmBatteryOverheat = _UpsAlarmBatteryOverheat_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 5),
    _UpsAlarmBatteryOverheat_Type()
)
upsAlarmBatteryOverheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryOverheat.setStatus("mandatory")
_UpsAlarmBatteryVoltageAbnormal_Type = Integer32
_UpsAlarmBatteryVoltageAbnormal_Object = MibScalar
upsAlarmBatteryVoltageAbnormal = _UpsAlarmBatteryVoltageAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 6),
    _UpsAlarmBatteryVoltageAbnormal_Type()
)
upsAlarmBatteryVoltageAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmBatteryVoltageAbnormal.setStatus("mandatory")
_UpsAlarmUPSOverheat_Type = Integer32
_UpsAlarmUPSOverheat_Object = MibScalar
upsAlarmUPSOverheat = _UpsAlarmUPSOverheat_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 7),
    _UpsAlarmUPSOverheat_Type()
)
upsAlarmUPSOverheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUPSOverheat.setStatus("mandatory")
_UpsAlarmPowerFailure_Type = Integer32
_UpsAlarmPowerFailure_Object = MibScalar
upsAlarmPowerFailure = _UpsAlarmPowerFailure_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 8),
    _UpsAlarmPowerFailure_Type()
)
upsAlarmPowerFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmPowerFailure.setStatus("mandatory")
_UpsAlarmUPSOverload_Type = Integer32
_UpsAlarmUPSOverload_Object = MibScalar
upsAlarmUPSOverload = _UpsAlarmUPSOverload_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 9),
    _UpsAlarmUPSOverload_Type()
)
upsAlarmUPSOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUPSOverload.setStatus("mandatory")
_UpsAlarmUserDefinedOverloadWarning_Type = Integer32
_UpsAlarmUserDefinedOverloadWarning_Object = MibScalar
upsAlarmUserDefinedOverloadWarning = _UpsAlarmUserDefinedOverloadWarning_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 10),
    _UpsAlarmUserDefinedOverloadWarning_Type()
)
upsAlarmUserDefinedOverloadWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmUserDefinedOverloadWarning.setStatus("mandatory")
_UpsAlarmOnBypass_Type = Integer32
_UpsAlarmOnBypass_Object = MibScalar
upsAlarmOnBypass = _UpsAlarmOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 11),
    _UpsAlarmOnBypass_Type()
)
upsAlarmOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOnBypass.setStatus("mandatory")
_UpsAlarmOutputOff_Type = Integer32
_UpsAlarmOutputOff_Object = MibScalar
upsAlarmOutputOff = _UpsAlarmOutputOff_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 12),
    _UpsAlarmOutputOff_Type()
)
upsAlarmOutputOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOff.setStatus("mandatory")
_UpsAlarmAsyncOperation_Type = Integer32
_UpsAlarmAsyncOperation_Object = MibScalar
upsAlarmAsyncOperation = _UpsAlarmAsyncOperation_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 13),
    _UpsAlarmAsyncOperation_Type()
)
upsAlarmAsyncOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmAsyncOperation.setStatus("mandatory")
_UpsAlarmDCBusOverCurrent_Type = Integer32
_UpsAlarmDCBusOverCurrent_Object = MibScalar
upsAlarmDCBusOverCurrent = _UpsAlarmDCBusOverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 14),
    _UpsAlarmDCBusOverCurrent_Type()
)
upsAlarmDCBusOverCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDCBusOverCurrent.setStatus("mandatory")
_UpsAlarmDCBusOverVoltage_Type = Integer32
_UpsAlarmDCBusOverVoltage_Object = MibScalar
upsAlarmDCBusOverVoltage = _UpsAlarmDCBusOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 15),
    _UpsAlarmDCBusOverVoltage_Type()
)
upsAlarmDCBusOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDCBusOverVoltage.setStatus("mandatory")
_UpsAlarmDCBusUnderVoltage_Type = Integer32
_UpsAlarmDCBusUnderVoltage_Object = MibScalar
upsAlarmDCBusUnderVoltage = _UpsAlarmDCBusUnderVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 16),
    _UpsAlarmDCBusUnderVoltage_Type()
)
upsAlarmDCBusUnderVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDCBusUnderVoltage.setStatus("mandatory")
_UpsAlarmDCBusImbalanced_Type = Integer32
_UpsAlarmDCBusImbalanced_Object = MibScalar
upsAlarmDCBusImbalanced = _UpsAlarmDCBusImbalanced_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 17),
    _UpsAlarmDCBusImbalanced_Type()
)
upsAlarmDCBusImbalanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmDCBusImbalanced.setStatus("mandatory")
_UpsAlarmOutputUnderVoltage_Type = Integer32
_UpsAlarmOutputUnderVoltage_Object = MibScalar
upsAlarmOutputUnderVoltage = _UpsAlarmOutputUnderVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 18),
    _UpsAlarmOutputUnderVoltage_Type()
)
upsAlarmOutputUnderVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputUnderVoltage.setStatus("mandatory")
_UpsAlarmOutputOverVoltage_Type = Integer32
_UpsAlarmOutputOverVoltage_Object = MibScalar
upsAlarmOutputOverVoltage = _UpsAlarmOutputOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 19),
    _UpsAlarmOutputOverVoltage_Type()
)
upsAlarmOutputOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmOutputOverVoltage.setStatus("mandatory")
_UpsAlarmInverterOverload_Type = Integer32
_UpsAlarmInverterOverload_Object = MibScalar
upsAlarmInverterOverload = _UpsAlarmInverterOverload_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 20),
    _UpsAlarmInverterOverload_Type()
)
upsAlarmInverterOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterOverload.setStatus("mandatory")
_UpsAlarmInverterOvercurrent_Type = Integer32
_UpsAlarmInverterOvercurrent_Object = MibScalar
upsAlarmInverterOvercurrent = _UpsAlarmInverterOvercurrent_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 21),
    _UpsAlarmInverterOvercurrent_Type()
)
upsAlarmInverterOvercurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmInverterOvercurrent.setStatus("mandatory")
_UpsAlarmRemotEyeCommError_Type = Integer32
_UpsAlarmRemotEyeCommError_Object = MibScalar
upsAlarmRemotEyeCommError = _UpsAlarmRemotEyeCommError_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 6, 3, 22),
    _UpsAlarmRemotEyeCommError_Type()
)
upsAlarmRemotEyeCommError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsAlarmRemotEyeCommError.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7)
)


class _UpsConfigModelIDString_Type(DisplayString):
    """Custom type upsConfigModelIDString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsConfigModelIDString_Type.__name__ = "DisplayString"
_UpsConfigModelIDString_Object = MibScalar
upsConfigModelIDString = _UpsConfigModelIDString_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 1),
    _UpsConfigModelIDString_Type()
)
upsConfigModelIDString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigModelIDString.setStatus("mandatory")


class _UpsConfigUPSFirmwareVersion_Type(DisplayString):
    """Custom type upsConfigUPSFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsConfigUPSFirmwareVersion_Type.__name__ = "DisplayString"
_UpsConfigUPSFirmwareVersion_Object = MibScalar
upsConfigUPSFirmwareVersion = _UpsConfigUPSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 2),
    _UpsConfigUPSFirmwareVersion_Type()
)
upsConfigUPSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigUPSFirmwareVersion.setStatus("mandatory")
_UpsConfigInputNumOfPhases_Type = NonNegativeInteger
_UpsConfigInputNumOfPhases_Object = MibScalar
upsConfigInputNumOfPhases = _UpsConfigInputNumOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 3),
    _UpsConfigInputNumOfPhases_Type()
)
upsConfigInputNumOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigInputNumOfPhases.setStatus("mandatory")
_UpsConfigRatedInputFrequency_Type = NonNegativeInteger
_UpsConfigRatedInputFrequency_Object = MibScalar
upsConfigRatedInputFrequency = _UpsConfigRatedInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 4),
    _UpsConfigRatedInputFrequency_Type()
)
upsConfigRatedInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigRatedInputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedInputFrequency.setUnits("0.1 Hertz")
_UpsConfigRatedInputLLVoltage_Type = NonNegativeInteger
_UpsConfigRatedInputLLVoltage_Object = MibScalar
upsConfigRatedInputLLVoltage = _UpsConfigRatedInputLLVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 5),
    _UpsConfigRatedInputLLVoltage_Type()
)
upsConfigRatedInputLLVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigRatedInputLLVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedInputLLVoltage.setUnits("RMS Volts")
_UpsConfigRatedInputPowerFactor_Type = PositiveInteger
_UpsConfigRatedInputPowerFactor_Object = MibScalar
upsConfigRatedInputPowerFactor = _UpsConfigRatedInputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 6),
    _UpsConfigRatedInputPowerFactor_Type()
)
upsConfigRatedInputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigRatedInputPowerFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedInputPowerFactor.setUnits("0.01")
_UpsConfigOutputNumOfPhases_Type = NonNegativeInteger
_UpsConfigOutputNumOfPhases_Object = MibScalar
upsConfigOutputNumOfPhases = _UpsConfigOutputNumOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 7),
    _UpsConfigOutputNumOfPhases_Type()
)
upsConfigOutputNumOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputNumOfPhases.setStatus("mandatory")
_UpsConfigRatedOutputFrequency_Type = NonNegativeInteger
_UpsConfigRatedOutputFrequency_Object = MibScalar
upsConfigRatedOutputFrequency = _UpsConfigRatedOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 8),
    _UpsConfigRatedOutputFrequency_Type()
)
upsConfigRatedOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigRatedOutputFrequency.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedOutputFrequency.setUnits("0.1 Hertz")
_UpsConfigRatedOutputLLVoltage_Type = NonNegativeInteger
_UpsConfigRatedOutputLLVoltage_Object = MibScalar
upsConfigRatedOutputLLVoltage = _UpsConfigRatedOutputLLVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 9),
    _UpsConfigRatedOutputLLVoltage_Type()
)
upsConfigRatedOutputLLVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigRatedOutputLLVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedOutputLLVoltage.setUnits("RMS Volts")
_UpsConfigRatedOutputApperentPower_Type = NonNegativeInteger
_UpsConfigRatedOutputApperentPower_Object = MibScalar
upsConfigRatedOutputApperentPower = _UpsConfigRatedOutputApperentPower_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 10),
    _UpsConfigRatedOutputApperentPower_Type()
)
upsConfigRatedOutputApperentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigRatedOutputApperentPower.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedOutputApperentPower.setUnits("Volt-Amps")
_UpsConfigRatedOutputActivePower_Type = NonNegativeInteger
_UpsConfigRatedOutputActivePower_Object = MibScalar
upsConfigRatedOutputActivePower = _UpsConfigRatedOutputActivePower_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 11),
    _UpsConfigRatedOutputActivePower_Type()
)
upsConfigRatedOutputActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigRatedOutputActivePower.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedOutputActivePower.setUnits("KWatts")
_UpsConfigRatedOutputPowerFactor_Type = NonNegativeInteger
_UpsConfigRatedOutputPowerFactor_Object = MibScalar
upsConfigRatedOutputPowerFactor = _UpsConfigRatedOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 12),
    _UpsConfigRatedOutputPowerFactor_Type()
)
upsConfigRatedOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigRatedOutputPowerFactor.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedOutputPowerFactor.setUnits("0.01")
_UpsConfigBypassNumOfPhases_Type = NonNegativeInteger
_UpsConfigBypassNumOfPhases_Object = MibScalar
upsConfigBypassNumOfPhases = _UpsConfigBypassNumOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 13),
    _UpsConfigBypassNumOfPhases_Type()
)
upsConfigBypassNumOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigBypassNumOfPhases.setStatus("mandatory")
_UpsConfigLowVoltageTransferPoint_Type = NonNegativeInteger
_UpsConfigLowVoltageTransferPoint_Object = MibScalar
upsConfigLowVoltageTransferPoint = _UpsConfigLowVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 14),
    _UpsConfigLowVoltageTransferPoint_Type()
)
upsConfigLowVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigLowVoltageTransferPoint.setUnits("percentage")
_UpsConfigHighVoltageTransferPoint_Type = NonNegativeInteger
_UpsConfigHighVoltageTransferPoint_Object = MibScalar
upsConfigHighVoltageTransferPoint = _UpsConfigHighVoltageTransferPoint_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 15),
    _UpsConfigHighVoltageTransferPoint_Type()
)
upsConfigHighVoltageTransferPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigHighVoltageTransferPoint.setUnits("percentage")
_UpsConfigBatteryInSeries_Type = NonNegativeInteger
_UpsConfigBatteryInSeries_Object = MibScalar
upsConfigBatteryInSeries = _UpsConfigBatteryInSeries_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 16),
    _UpsConfigBatteryInSeries_Type()
)
upsConfigBatteryInSeries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryInSeries.setStatus("mandatory")
_UpsConfigBatteryNumStrings_Type = NonNegativeInteger
_UpsConfigBatteryNumStrings_Object = MibScalar
upsConfigBatteryNumStrings = _UpsConfigBatteryNumStrings_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 17),
    _UpsConfigBatteryNumStrings_Type()
)
upsConfigBatteryNumStrings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryNumStrings.setStatus("mandatory")
_UpsConfigRatedBatteryVoltage_Type = NonNegativeInteger
_UpsConfigRatedBatteryVoltage_Object = MibScalar
upsConfigRatedBatteryVoltage = _UpsConfigRatedBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 18),
    _UpsConfigRatedBatteryVoltage_Type()
)
upsConfigRatedBatteryVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigRatedBatteryVoltage.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedBatteryVoltage.setUnits("Volts DC")
_UpsConfigRatedBatteryAmpereHour_Type = Integer32
_UpsConfigRatedBatteryAmpereHour_Object = MibScalar
upsConfigRatedBatteryAmpereHour = _UpsConfigRatedBatteryAmpereHour_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 19),
    _UpsConfigRatedBatteryAmpereHour_Type()
)
upsConfigRatedBatteryAmpereHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigRatedBatteryAmpereHour.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigRatedBatteryAmpereHour.setUnits("Ahr")


class _UpsConfigBatteryModel_Type(DisplayString):
    """Custom type upsConfigBatteryModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsConfigBatteryModel_Type.__name__ = "DisplayString"
_UpsConfigBatteryModel_Object = MibScalar
upsConfigBatteryModel = _UpsConfigBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 20),
    _UpsConfigBatteryModel_Type()
)
upsConfigBatteryModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryModel.setStatus("mandatory")
_UpsConfigBatteryRatedBackupTime_Type = NonNegativeInteger
_UpsConfigBatteryRatedBackupTime_Object = MibScalar
upsConfigBatteryRatedBackupTime = _UpsConfigBatteryRatedBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 21),
    _UpsConfigBatteryRatedBackupTime_Type()
)
upsConfigBatteryRatedBackupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryRatedBackupTime.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigBatteryRatedBackupTime.setUnits("minutes")
_UpsConfigUserDefinedOverloadSetPoint_Type = Integer32
_UpsConfigUserDefinedOverloadSetPoint_Object = MibScalar
upsConfigUserDefinedOverloadSetPoint = _UpsConfigUserDefinedOverloadSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 22),
    _UpsConfigUserDefinedOverloadSetPoint_Type()
)
upsConfigUserDefinedOverloadSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigUserDefinedOverloadSetPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigUserDefinedOverloadSetPoint.setUnits("%")


class _UpsConfigBatteryInstallationDate_Type(DisplayString):
    """Custom type upsConfigBatteryInstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_UpsConfigBatteryInstallationDate_Type.__name__ = "DisplayString"
_UpsConfigBatteryInstallationDate_Object = MibScalar
upsConfigBatteryInstallationDate = _UpsConfigBatteryInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 23),
    _UpsConfigBatteryInstallationDate_Type()
)
upsConfigBatteryInstallationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigBatteryInstallationDate.setStatus("mandatory")
if mibBuilder.loadTexts:
    upsConfigBatteryInstallationDate.setUnits("mm/dd/yyyy")


class _UpsConfigSysName_Type(DisplayString):
    """Custom type upsConfigSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsConfigSysName_Type.__name__ = "DisplayString"
_UpsConfigSysName_Object = MibScalar
upsConfigSysName = _UpsConfigSysName_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 24),
    _UpsConfigSysName_Type()
)
upsConfigSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigSysName.setStatus("mandatory")


class _UpsConfigAttachedDevices_Type(DisplayString):
    """Custom type upsConfigAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsConfigAttachedDevices_Type.__name__ = "DisplayString"
_UpsConfigAttachedDevices_Object = MibScalar
upsConfigAttachedDevices = _UpsConfigAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 25),
    _UpsConfigAttachedDevices_Type()
)
upsConfigAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigAttachedDevices.setStatus("mandatory")


class _UpsConfigPassword_Type(DisplayString):
    """Custom type upsConfigPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsConfigPassword_Type.__name__ = "DisplayString"
_UpsConfigPassword_Object = MibScalar
upsConfigPassword = _UpsConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 7, 26),
    _UpsConfigPassword_Type()
)
upsConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigPassword.setStatus("mandatory")
_UpsTime_ObjectIdentity = ObjectIdentity
upsTime = _UpsTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 8)
)


class _UpsTimeRealDate_Type(DisplayString):
    """Custom type upsTimeRealDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsTimeRealDate_Type.__name__ = "DisplayString"
_UpsTimeRealDate_Object = MibScalar
upsTimeRealDate = _UpsTimeRealDate_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 8, 1),
    _UpsTimeRealDate_Type()
)
upsTimeRealDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimeRealDate.setStatus("mandatory")


class _UpsTimeRealTime_Type(DisplayString):
    """Custom type upsTimeRealTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsTimeRealTime_Type.__name__ = "DisplayString"
_UpsTimeRealTime_Object = MibScalar
upsTimeRealTime = _UpsTimeRealTime_Object(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 8, 2),
    _UpsTimeRealTime_Type()
)
upsTimeRealTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTimeRealTime.setStatus("mandatory")
_UpsTrap_ObjectIdentity = ObjectIdentity
upsTrap = _UpsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 9)
)

# Managed Objects groups


# Notification objects

upsTrapFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 1)
)
if mibBuilder.loadTexts:
    upsTrapFault.setStatus(
        ""
    )

upsTrapFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 2)
)
if mibBuilder.loadTexts:
    upsTrapFaultClear.setStatus(
        ""
    )

upsTrapOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 3)
)
if mibBuilder.loadTexts:
    upsTrapOnBattery.setStatus(
        ""
    )

upsTrapOnBatteryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 4)
)
if mibBuilder.loadTexts:
    upsTrapOnBatteryClear.setStatus(
        ""
    )

upsTrapBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 5)
)
if mibBuilder.loadTexts:
    upsTrapBatteryLow.setStatus(
        ""
    )

upsTrapBatteryLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 6)
)
if mibBuilder.loadTexts:
    upsTrapBatteryLowClear.setStatus(
        ""
    )

upsTrapBatteryDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 7)
)
if mibBuilder.loadTexts:
    upsTrapBatteryDepleted.setStatus(
        ""
    )

upsTrapBatteryDepletedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 8)
)
if mibBuilder.loadTexts:
    upsTrapBatteryDepletedClear.setStatus(
        ""
    )

upsTrapBatteryOverheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 9)
)
if mibBuilder.loadTexts:
    upsTrapBatteryOverheat.setStatus(
        ""
    )

upsTrapBatteryOverheatClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 10)
)
if mibBuilder.loadTexts:
    upsTrapBatteryOverheatClear.setStatus(
        ""
    )

upsTrapBatteryVoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 11)
)
if mibBuilder.loadTexts:
    upsTrapBatteryVoltageAbnormal.setStatus(
        ""
    )

upsTrapBatteryVoltageAbnormalClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 12)
)
if mibBuilder.loadTexts:
    upsTrapBatteryVoltageAbnormalClear.setStatus(
        ""
    )

upsTrapUPSOverheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 13)
)
if mibBuilder.loadTexts:
    upsTrapUPSOverheat.setStatus(
        ""
    )

upsTrapUPSOverheatClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 14)
)
if mibBuilder.loadTexts:
    upsTrapUPSOverheatClear.setStatus(
        ""
    )

upsTrapPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 15)
)
if mibBuilder.loadTexts:
    upsTrapPowerFailure.setStatus(
        ""
    )

upsTrapPowerFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 16)
)
if mibBuilder.loadTexts:
    upsTrapPowerFailureClear.setStatus(
        ""
    )

upsTrapUPSOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 17)
)
if mibBuilder.loadTexts:
    upsTrapUPSOverload.setStatus(
        ""
    )

upsTrapUPSOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 18)
)
if mibBuilder.loadTexts:
    upsTrapUPSOverloadClear.setStatus(
        ""
    )

upsTrapUserDefinedOverloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 19)
)
if mibBuilder.loadTexts:
    upsTrapUserDefinedOverloadWarning.setStatus(
        ""
    )

upsTrapUserDefinedOverloadWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 20)
)
if mibBuilder.loadTexts:
    upsTrapUserDefinedOverloadWarningClear.setStatus(
        ""
    )

upsTrapOnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 21)
)
if mibBuilder.loadTexts:
    upsTrapOnBypass.setStatus(
        ""
    )

upsTrapOnBypassClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 22)
)
if mibBuilder.loadTexts:
    upsTrapOnBypassClear.setStatus(
        ""
    )

upsTrapOutputOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 23)
)
if mibBuilder.loadTexts:
    upsTrapOutputOff.setStatus(
        ""
    )

upsTrapOutputOffClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 24)
)
if mibBuilder.loadTexts:
    upsTrapOutputOffClear.setStatus(
        ""
    )

upsTrapAsyncOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 25)
)
if mibBuilder.loadTexts:
    upsTrapAsyncOperation.setStatus(
        ""
    )

upsTrapAsyncOperationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 26)
)
if mibBuilder.loadTexts:
    upsTrapAsyncOperationClear.setStatus(
        ""
    )

upsTrapDCBusOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 27)
)
if mibBuilder.loadTexts:
    upsTrapDCBusOverCurrent.setStatus(
        ""
    )

upsTrapDCBusOverCurrentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 28)
)
if mibBuilder.loadTexts:
    upsTrapDCBusOverCurrentClear.setStatus(
        ""
    )

upsTrapDCBusOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 29)
)
if mibBuilder.loadTexts:
    upsTrapDCBusOverVoltage.setStatus(
        ""
    )

upsTrapDCBusOverVoltageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 30)
)
if mibBuilder.loadTexts:
    upsTrapDCBusOverVoltageClear.setStatus(
        ""
    )

upsTrapDCBusUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 31)
)
if mibBuilder.loadTexts:
    upsTrapDCBusUnderVoltage.setStatus(
        ""
    )

upsTrapDCBusUnderVoltageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 32)
)
if mibBuilder.loadTexts:
    upsTrapDCBusUnderVoltageClear.setStatus(
        ""
    )

upsTrapDCBusImbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 33)
)
if mibBuilder.loadTexts:
    upsTrapDCBusImbalance.setStatus(
        ""
    )

upsTrapDCBusImbalanceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 34)
)
if mibBuilder.loadTexts:
    upsTrapDCBusImbalanceClear.setStatus(
        ""
    )

upsTrapOutputUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 35)
)
if mibBuilder.loadTexts:
    upsTrapOutputUnderVoltage.setStatus(
        ""
    )

upsTrapOutputUnderVoltageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 36)
)
if mibBuilder.loadTexts:
    upsTrapOutputUnderVoltageClear.setStatus(
        ""
    )

upsTrapOutputOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 37)
)
if mibBuilder.loadTexts:
    upsTrapOutputOverVoltage.setStatus(
        ""
    )

upsTrapOutputOverVoltageClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 38)
)
if mibBuilder.loadTexts:
    upsTrapOutputOverVoltageClear.setStatus(
        ""
    )

upsTrapInverterOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 39)
)
if mibBuilder.loadTexts:
    upsTrapInverterOverload.setStatus(
        ""
    )

upsTrapInverterOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 40)
)
if mibBuilder.loadTexts:
    upsTrapInverterOverloadClear.setStatus(
        ""
    )

upsTrapInverterOvercurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 41)
)
if mibBuilder.loadTexts:
    upsTrapInverterOvercurrent.setStatus(
        ""
    )

upsTrapInverterOvercurrentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 42)
)
if mibBuilder.loadTexts:
    upsTrapInverterOvercurrentClear.setStatus(
        ""
    )

upsTrapRemotEyeCommError = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 43)
)
if mibBuilder.loadTexts:
    upsTrapRemotEyeCommError.setStatus(
        ""
    )

upsTrapRemotEyeCommErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 186, 1, 19, 2, 5, 1, 0, 44)
)
if mibBuilder.loadTexts:
    upsTrapRemotEyeCommErrorClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIC-RMTI4-G9000-G2020-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "toshiba": toshiba,
       "equ": equ,
       "equUPS": equUPS,
       "ticUPS": ticUPS,
       "rmti4": rmti4,
       "upsG9000-G2020": upsG9000_G2020,
       "upsTrapFault": upsTrapFault,
       "upsTrapFaultClear": upsTrapFaultClear,
       "upsTrapOnBattery": upsTrapOnBattery,
       "upsTrapOnBatteryClear": upsTrapOnBatteryClear,
       "upsTrapBatteryLow": upsTrapBatteryLow,
       "upsTrapBatteryLowClear": upsTrapBatteryLowClear,
       "upsTrapBatteryDepleted": upsTrapBatteryDepleted,
       "upsTrapBatteryDepletedClear": upsTrapBatteryDepletedClear,
       "upsTrapBatteryOverheat": upsTrapBatteryOverheat,
       "upsTrapBatteryOverheatClear": upsTrapBatteryOverheatClear,
       "upsTrapBatteryVoltageAbnormal": upsTrapBatteryVoltageAbnormal,
       "upsTrapBatteryVoltageAbnormalClear": upsTrapBatteryVoltageAbnormalClear,
       "upsTrapUPSOverheat": upsTrapUPSOverheat,
       "upsTrapUPSOverheatClear": upsTrapUPSOverheatClear,
       "upsTrapPowerFailure": upsTrapPowerFailure,
       "upsTrapPowerFailureClear": upsTrapPowerFailureClear,
       "upsTrapUPSOverload": upsTrapUPSOverload,
       "upsTrapUPSOverloadClear": upsTrapUPSOverloadClear,
       "upsTrapUserDefinedOverloadWarning": upsTrapUserDefinedOverloadWarning,
       "upsTrapUserDefinedOverloadWarningClear": upsTrapUserDefinedOverloadWarningClear,
       "upsTrapOnBypass": upsTrapOnBypass,
       "upsTrapOnBypassClear": upsTrapOnBypassClear,
       "upsTrapOutputOff": upsTrapOutputOff,
       "upsTrapOutputOffClear": upsTrapOutputOffClear,
       "upsTrapAsyncOperation": upsTrapAsyncOperation,
       "upsTrapAsyncOperationClear": upsTrapAsyncOperationClear,
       "upsTrapDCBusOverCurrent": upsTrapDCBusOverCurrent,
       "upsTrapDCBusOverCurrentClear": upsTrapDCBusOverCurrentClear,
       "upsTrapDCBusOverVoltage": upsTrapDCBusOverVoltage,
       "upsTrapDCBusOverVoltageClear": upsTrapDCBusOverVoltageClear,
       "upsTrapDCBusUnderVoltage": upsTrapDCBusUnderVoltage,
       "upsTrapDCBusUnderVoltageClear": upsTrapDCBusUnderVoltageClear,
       "upsTrapDCBusImbalance": upsTrapDCBusImbalance,
       "upsTrapDCBusImbalanceClear": upsTrapDCBusImbalanceClear,
       "upsTrapOutputUnderVoltage": upsTrapOutputUnderVoltage,
       "upsTrapOutputUnderVoltageClear": upsTrapOutputUnderVoltageClear,
       "upsTrapOutputOverVoltage": upsTrapOutputOverVoltage,
       "upsTrapOutputOverVoltageClear": upsTrapOutputOverVoltageClear,
       "upsTrapInverterOverload": upsTrapInverterOverload,
       "upsTrapInverterOverloadClear": upsTrapInverterOverloadClear,
       "upsTrapInverterOvercurrent": upsTrapInverterOvercurrent,
       "upsTrapInverterOvercurrentClear": upsTrapInverterOvercurrentClear,
       "upsTrapRemotEyeCommError": upsTrapRemotEyeCommError,
       "upsTrapRemotEyeCommErrorClear": upsTrapRemotEyeCommErrorClear,
       "upsIdent": upsIdent,
       "upsIdentManufacturer": upsIdentManufacturer,
       "upsIdentTypeform": upsIdentTypeform,
       "upsIdentUPSFirmwareVersion": upsIdentUPSFirmwareVersion,
       "upsIdentSysName": upsIdentSysName,
       "upsIdentAttachedDevices": upsIdentAttachedDevices,
       "upsInput": upsInput,
       "upsInputNumOfPhases": upsInputNumOfPhases,
       "upsInputLLVoltageAB": upsInputLLVoltageAB,
       "upsInputLLVoltageBC": upsInputLLVoltageBC,
       "upsInputLLVoltageCA": upsInputLLVoltageCA,
       "upsInputLLVoltagePercentAB": upsInputLLVoltagePercentAB,
       "upsInputLLVoltagePercentBC": upsInputLLVoltagePercentBC,
       "upsInputLLVoltagePercentCA": upsInputLLVoltagePercentCA,
       "upsInputCurrentPhaseA": upsInputCurrentPhaseA,
       "upsInputCurrentPhaseB": upsInputCurrentPhaseB,
       "upsInputCurrentPhaseC": upsInputCurrentPhaseC,
       "upsInputFrequency": upsInputFrequency,
       "upsInputActivePowerA": upsInputActivePowerA,
       "upsInputActivePowerB": upsInputActivePowerB,
       "upsInputActivePowerC": upsInputActivePowerC,
       "upsInputTotalActivePower": upsInputTotalActivePower,
       "upsInputRatedLLVoltage": upsInputRatedLLVoltage,
       "upsOutput": upsOutput,
       "upsOutputSource": upsOutputSource,
       "upsOutputNumOfPhases": upsOutputNumOfPhases,
       "upsOutputLLVoltageAB": upsOutputLLVoltageAB,
       "upsOutputLLVoltageBC": upsOutputLLVoltageBC,
       "upsOutputLLVoltageCA": upsOutputLLVoltageCA,
       "upsOutputCurrentPhaseA": upsOutputCurrentPhaseA,
       "upsOutputCurrentPhaseB": upsOutputCurrentPhaseB,
       "upsOutputCurrentPhaseC": upsOutputCurrentPhaseC,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputCurrentPercentA": upsOutputCurrentPercentA,
       "upsOutputCurrentPercentB": upsOutputCurrentPercentB,
       "upsOutputCurrentPercentC": upsOutputCurrentPercentC,
       "upsOutputTotalActivePower": upsOutputTotalActivePower,
       "upsOutputTotalActivePowerPercent": upsOutputTotalActivePowerPercent,
       "upsOutputPowerFactor": upsOutputPowerFactor,
       "upsOutputRatedActivePower": upsOutputRatedActivePower,
       "upsOutputRatedApparentPower": upsOutputRatedApparentPower,
       "upsOutputRatedLLVoltage": upsOutputRatedLLVoltage,
       "upsBypass": upsBypass,
       "upsBypassNumOfPhases": upsBypassNumOfPhases,
       "upsBypassLLVoltageAB": upsBypassLLVoltageAB,
       "upsBypassLLVoltageBC": upsBypassLLVoltageBC,
       "upsBypassLLVoltageCA": upsBypassLLVoltageCA,
       "upsBypassFrequency": upsBypassFrequency,
       "upsBattery": upsBattery,
       "upsBatteryStatus": upsBatteryStatus,
       "upsElapsedTimeOnBatteryPower": upsElapsedTimeOnBatteryPower,
       "upsEstimatedBatteryRuntime": upsEstimatedBatteryRuntime,
       "upsBatteryVoltage": upsBatteryVoltage,
       "upsBatteryVoltagePercent": upsBatteryVoltagePercent,
       "upsBatteryEstimatedCharge": upsBatteryEstimatedCharge,
       "upsBatteryDischargeCurrent": upsBatteryDischargeCurrent,
       "upsBatteryChargeCurrent": upsBatteryChargeCurrent,
       "upsBatteryModel": upsBatteryModel,
       "upsBatteryInSeries": upsBatteryInSeries,
       "upsBatteryNumStrings": upsBatteryNumStrings,
       "upsBatteryRatedAmpereHour": upsBatteryRatedAmpereHour,
       "upsBatteryRatedBackupTime": upsBatteryRatedBackupTime,
       "upsBatteryInstallationDate": upsBatteryInstallationDate,
       "upsAlarm": upsAlarm,
       "upsAlarmsPresent": upsAlarmsPresent,
       "upsAlarmTable": upsAlarmTable,
       "upsAlarmEntry": upsAlarmEntry,
       "upsAlarmId": upsAlarmId,
       "upsAlarmDescr": upsAlarmDescr,
       "upsAlarmTime": upsAlarmTime,
       "upsWellKnownAlarms": upsWellKnownAlarms,
       "upsAlarmFault": upsAlarmFault,
       "upsAlarmOnBattery": upsAlarmOnBattery,
       "upsAlarmBatteryLow": upsAlarmBatteryLow,
       "upsAlarmBatteryDepleted": upsAlarmBatteryDepleted,
       "upsAlarmBatteryOverheat": upsAlarmBatteryOverheat,
       "upsAlarmBatteryVoltageAbnormal": upsAlarmBatteryVoltageAbnormal,
       "upsAlarmUPSOverheat": upsAlarmUPSOverheat,
       "upsAlarmPowerFailure": upsAlarmPowerFailure,
       "upsAlarmUPSOverload": upsAlarmUPSOverload,
       "upsAlarmUserDefinedOverloadWarning": upsAlarmUserDefinedOverloadWarning,
       "upsAlarmOnBypass": upsAlarmOnBypass,
       "upsAlarmOutputOff": upsAlarmOutputOff,
       "upsAlarmAsyncOperation": upsAlarmAsyncOperation,
       "upsAlarmDCBusOverCurrent": upsAlarmDCBusOverCurrent,
       "upsAlarmDCBusOverVoltage": upsAlarmDCBusOverVoltage,
       "upsAlarmDCBusUnderVoltage": upsAlarmDCBusUnderVoltage,
       "upsAlarmDCBusImbalanced": upsAlarmDCBusImbalanced,
       "upsAlarmOutputUnderVoltage": upsAlarmOutputUnderVoltage,
       "upsAlarmOutputOverVoltage": upsAlarmOutputOverVoltage,
       "upsAlarmInverterOverload": upsAlarmInverterOverload,
       "upsAlarmInverterOvercurrent": upsAlarmInverterOvercurrent,
       "upsAlarmRemotEyeCommError": upsAlarmRemotEyeCommError,
       "upsConfig": upsConfig,
       "upsConfigModelIDString": upsConfigModelIDString,
       "upsConfigUPSFirmwareVersion": upsConfigUPSFirmwareVersion,
       "upsConfigInputNumOfPhases": upsConfigInputNumOfPhases,
       "upsConfigRatedInputFrequency": upsConfigRatedInputFrequency,
       "upsConfigRatedInputLLVoltage": upsConfigRatedInputLLVoltage,
       "upsConfigRatedInputPowerFactor": upsConfigRatedInputPowerFactor,
       "upsConfigOutputNumOfPhases": upsConfigOutputNumOfPhases,
       "upsConfigRatedOutputFrequency": upsConfigRatedOutputFrequency,
       "upsConfigRatedOutputLLVoltage": upsConfigRatedOutputLLVoltage,
       "upsConfigRatedOutputApperentPower": upsConfigRatedOutputApperentPower,
       "upsConfigRatedOutputActivePower": upsConfigRatedOutputActivePower,
       "upsConfigRatedOutputPowerFactor": upsConfigRatedOutputPowerFactor,
       "upsConfigBypassNumOfPhases": upsConfigBypassNumOfPhases,
       "upsConfigLowVoltageTransferPoint": upsConfigLowVoltageTransferPoint,
       "upsConfigHighVoltageTransferPoint": upsConfigHighVoltageTransferPoint,
       "upsConfigBatteryInSeries": upsConfigBatteryInSeries,
       "upsConfigBatteryNumStrings": upsConfigBatteryNumStrings,
       "upsConfigRatedBatteryVoltage": upsConfigRatedBatteryVoltage,
       "upsConfigRatedBatteryAmpereHour": upsConfigRatedBatteryAmpereHour,
       "upsConfigBatteryModel": upsConfigBatteryModel,
       "upsConfigBatteryRatedBackupTime": upsConfigBatteryRatedBackupTime,
       "upsConfigUserDefinedOverloadSetPoint": upsConfigUserDefinedOverloadSetPoint,
       "upsConfigBatteryInstallationDate": upsConfigBatteryInstallationDate,
       "upsConfigSysName": upsConfigSysName,
       "upsConfigAttachedDevices": upsConfigAttachedDevices,
       "upsConfigPassword": upsConfigPassword,
       "upsTime": upsTime,
       "upsTimeRealDate": upsTimeRealDate,
       "upsTimeRealTime": upsTimeRealTime,
       "upsTrap": upsTrap}
)
