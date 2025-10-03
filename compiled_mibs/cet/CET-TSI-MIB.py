# SNMP MIB module (CET-TSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cet\CET-TSI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:14 2025
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

(cetMIB,) = mibBuilder.importSymbols(
    "CET-TSI-SMI",
    "cetMIB")

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

cetTSIMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4)
)
if mibBuilder.loadTexts:
    cetTSIMIB.setRevisions(
        ("2007-12-05 10:00",
         "2007-08-13 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TsiObjects_ObjectIdentity = ObjectIdentity
tsiObjects = _TsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1)
)
_TsiModules_ObjectIdentity = ObjectIdentity
tsiModules = _TsiModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1)
)
_TsiModuleTable_Object = MibTable
tsiModuleTable = _TsiModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tsiModuleTable.setStatus("current")
_TsiModuleTableEntry_Object = MibTableRow
tsiModuleTableEntry = _TsiModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1)
)
tsiModuleTableEntry.setIndexNames(
    (0, "CET-TSI-MIB", "tsiModuleTableIndex"),
)
if mibBuilder.loadTexts:
    tsiModuleTableEntry.setStatus("current")


class _TsiModuleTableIndex_Type(Integer32):
    """Custom type tsiModuleTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TsiModuleTableIndex_Type.__name__ = "Integer32"
_TsiModuleTableIndex_Object = MibTableColumn
tsiModuleTableIndex = _TsiModuleTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 1),
    _TsiModuleTableIndex_Type()
)
tsiModuleTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsiModuleTableIndex.setStatus("current")


class _TsiModuleSeen_Type(Integer32):
    """Custom type tsiModuleSeen based on Integer32"""
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


_TsiModuleSeen_Type.__name__ = "Integer32"
_TsiModuleSeen_Object = MibTableColumn
tsiModuleSeen = _TsiModuleSeen_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 2),
    _TsiModuleSeen_Type()
)
tsiModuleSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleSeen.setStatus("current")


class _TsiModuleACOutState_Type(Integer32):
    """Custom type tsiModuleACOutState based on Integer32"""
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
        *(("sbr", 0),
          ("sb", 1),
          ("sbwe", 2),
          ("sbwre", 3),
          ("unknown", 4))
    )


_TsiModuleACOutState_Type.__name__ = "Integer32"
_TsiModuleACOutState_Object = MibTableColumn
tsiModuleACOutState = _TsiModuleACOutState_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 3),
    _TsiModuleACOutState_Type()
)
tsiModuleACOutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleACOutState.setStatus("current")


class _TsiModuleACInState_Type(Integer32):
    """Custom type tsiModuleACInState based on Integer32"""
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
        *(("ok", 0),
          ("safe", 1),
          ("notSync", 2),
          ("off", 3),
          ("unknown", 4))
    )


_TsiModuleACInState_Type.__name__ = "Integer32"
_TsiModuleACInState_Object = MibTableColumn
tsiModuleACInState = _TsiModuleACInState_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 4),
    _TsiModuleACInState_Type()
)
tsiModuleACInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleACInState.setStatus("current")


class _TsiModuleDCInState_Type(Integer32):
    """Custom type tsiModuleDCInState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("fail", 1),
          ("unknown", 2))
    )


_TsiModuleDCInState_Type.__name__ = "Integer32"
_TsiModuleDCInState_Object = MibTableColumn
tsiModuleDCInState = _TsiModuleDCInState_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 5),
    _TsiModuleDCInState_Type()
)
tsiModuleDCInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleDCInState.setStatus("current")


class _TsiModuleAddress_Type(Integer32):
    """Custom type tsiModuleAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TsiModuleAddress_Type.__name__ = "Integer32"
_TsiModuleAddress_Object = MibTableColumn
tsiModuleAddress = _TsiModuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 6),
    _TsiModuleAddress_Type()
)
tsiModuleAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleAddress.setStatus("current")


class _TsiModuleInputRepartition_Type(Integer32):
    """Custom type tsiModuleInputRepartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiModuleInputRepartition_Type.__name__ = "Integer32"
_TsiModuleInputRepartition_Object = MibTableColumn
tsiModuleInputRepartition = _TsiModuleInputRepartition_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 7),
    _TsiModuleInputRepartition_Type()
)
tsiModuleInputRepartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleInputRepartition.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleInputRepartition.setUnits("%")


class _TsiModuleLoadRatioW_Type(Integer32):
    """Custom type tsiModuleLoadRatioW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiModuleLoadRatioW_Type.__name__ = "Integer32"
_TsiModuleLoadRatioW_Object = MibTableColumn
tsiModuleLoadRatioW = _TsiModuleLoadRatioW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 8),
    _TsiModuleLoadRatioW_Type()
)
tsiModuleLoadRatioW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleLoadRatioW.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleLoadRatioW.setUnits("%")


class _TsiModuleLoadRatioVA_Type(Integer32):
    """Custom type tsiModuleLoadRatioVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiModuleLoadRatioVA_Type.__name__ = "Integer32"
_TsiModuleLoadRatioVA_Object = MibTableColumn
tsiModuleLoadRatioVA = _TsiModuleLoadRatioVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 9),
    _TsiModuleLoadRatioVA_Type()
)
tsiModuleLoadRatioVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleLoadRatioVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleLoadRatioVA.setUnits("%")
_TsiModulePhaseNumber_Type = Integer32
_TsiModulePhaseNumber_Object = MibTableColumn
tsiModulePhaseNumber = _TsiModulePhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 10),
    _TsiModulePhaseNumber_Type()
)
tsiModulePhaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulePhaseNumber.setStatus("current")
_TsiModuleACGroupNumber_Type = Integer32
_TsiModuleACGroupNumber_Object = MibTableColumn
tsiModuleACGroupNumber = _TsiModuleACGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 11),
    _TsiModuleACGroupNumber_Type()
)
tsiModuleACGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleACGroupNumber.setStatus("current")
_TsiModuleDCGroupNumber_Type = Integer32
_TsiModuleDCGroupNumber_Object = MibTableColumn
tsiModuleDCGroupNumber = _TsiModuleDCGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 12),
    _TsiModuleDCGroupNumber_Type()
)
tsiModuleDCGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleDCGroupNumber.setStatus("current")
_TsiModuleStatus_Type = Integer32
_TsiModuleStatus_Object = MibTableColumn
tsiModuleStatus = _TsiModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 13),
    _TsiModuleStatus_Type()
)
tsiModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleStatus.setStatus("current")
_TsiModuleACInStatus_Type = Integer32
_TsiModuleACInStatus_Object = MibTableColumn
tsiModuleACInStatus = _TsiModuleACInStatus_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 14),
    _TsiModuleACInStatus_Type()
)
tsiModuleACInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleACInStatus.setStatus("current")
_TsiModuleDCInStatus_Type = Integer32
_TsiModuleDCInStatus_Object = MibTableColumn
tsiModuleDCInStatus = _TsiModuleDCInStatus_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 15),
    _TsiModuleDCInStatus_Type()
)
tsiModuleDCInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleDCInStatus.setStatus("current")
_TsiModuleVout_Type = Integer32
_TsiModuleVout_Object = MibTableColumn
tsiModuleVout = _TsiModuleVout_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 16),
    _TsiModuleVout_Type()
)
tsiModuleVout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleVout.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleVout.setUnits("0.1V")
_TsiModuleIout_Type = Integer32
_TsiModuleIout_Object = MibTableColumn
tsiModuleIout = _TsiModuleIout_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 17),
    _TsiModuleIout_Type()
)
tsiModuleIout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleIout.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleIout.setUnits("0.1A")
_TsiModulePoutW_Type = Integer32
_TsiModulePoutW_Object = MibTableColumn
tsiModulePoutW = _TsiModulePoutW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 18),
    _TsiModulePoutW_Type()
)
tsiModulePoutW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulePoutW.setStatus("current")
if mibBuilder.loadTexts:
    tsiModulePoutW.setUnits("W")
_TsiModulePoutVA_Type = Integer32
_TsiModulePoutVA_Object = MibTableColumn
tsiModulePoutVA = _TsiModulePoutVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 19),
    _TsiModulePoutVA_Type()
)
tsiModulePoutVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulePoutVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiModulePoutVA.setUnits("VA")
_TsiModuleVinAC_Type = Integer32
_TsiModuleVinAC_Object = MibTableColumn
tsiModuleVinAC = _TsiModuleVinAC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 20),
    _TsiModuleVinAC_Type()
)
tsiModuleVinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleVinAC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleVinAC.setUnits("0.1V")
_TsiModuleIinAC_Type = Integer32
_TsiModuleIinAC_Object = MibTableColumn
tsiModuleIinAC = _TsiModuleIinAC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 21),
    _TsiModuleIinAC_Type()
)
tsiModuleIinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleIinAC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleIinAC.setUnits("0.1A")
_TsiModulePinACW_Type = Integer32
_TsiModulePinACW_Object = MibTableColumn
tsiModulePinACW = _TsiModulePinACW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 22),
    _TsiModulePinACW_Type()
)
tsiModulePinACW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulePinACW.setStatus("current")
if mibBuilder.loadTexts:
    tsiModulePinACW.setUnits("W")
_TsiModulePinACVA_Type = Integer32
_TsiModulePinACVA_Object = MibTableColumn
tsiModulePinACVA = _TsiModulePinACVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 23),
    _TsiModulePinACVA_Type()
)
tsiModulePinACVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulePinACVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiModulePinACVA.setUnits("VA")
_TsiModuleACinFreq_Type = Integer32
_TsiModuleACinFreq_Object = MibTableColumn
tsiModuleACinFreq = _TsiModuleACinFreq_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 24),
    _TsiModuleACinFreq_Type()
)
tsiModuleACinFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleACinFreq.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleACinFreq.setUnits("0.1Hz")
_TsiModuleVinDC_Type = Integer32
_TsiModuleVinDC_Object = MibTableColumn
tsiModuleVinDC = _TsiModuleVinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 25),
    _TsiModuleVinDC_Type()
)
tsiModuleVinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleVinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleVinDC.setUnits("0.1V")
_TsiModuleIinDC_Type = Integer32
_TsiModuleIinDC_Object = MibTableColumn
tsiModuleIinDC = _TsiModuleIinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 26),
    _TsiModuleIinDC_Type()
)
tsiModuleIinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleIinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleIinDC.setUnits("0.1A")
_TsiModulePinDC_Type = Integer32
_TsiModulePinDC_Object = MibTableColumn
tsiModulePinDC = _TsiModulePinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 27),
    _TsiModulePinDC_Type()
)
tsiModulePinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModulePinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModulePinDC.setUnits("W")
_TsiModuleTemperature_Type = Integer32
_TsiModuleTemperature_Object = MibTableColumn
tsiModuleTemperature = _TsiModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 28),
    _TsiModuleTemperature_Type()
)
tsiModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleTemperature.setUnits("K")
_TsiModuleSoftwareVersion_Type = Integer32
_TsiModuleSoftwareVersion_Object = MibTableColumn
tsiModuleSoftwareVersion = _TsiModuleSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 29),
    _TsiModuleSoftwareVersion_Type()
)
tsiModuleSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleSoftwareVersion.setStatus("current")
_TsiModuleSerialNumber_Type = Integer32
_TsiModuleSerialNumber_Object = MibTableColumn
tsiModuleSerialNumber = _TsiModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 30),
    _TsiModuleSerialNumber_Type()
)
tsiModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleSerialNumber.setStatus("current")
_TsiModuleNominalPoutW_Type = Integer32
_TsiModuleNominalPoutW_Object = MibTableColumn
tsiModuleNominalPoutW = _TsiModuleNominalPoutW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 31),
    _TsiModuleNominalPoutW_Type()
)
tsiModuleNominalPoutW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleNominalPoutW.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleNominalPoutW.setUnits("W")
_TsiModuleNominalPoutVA_Type = Integer32
_TsiModuleNominalPoutVA_Object = MibTableColumn
tsiModuleNominalPoutVA = _TsiModuleNominalPoutVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 32),
    _TsiModuleNominalPoutVA_Type()
)
tsiModuleNominalPoutVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleNominalPoutVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleNominalPoutVA.setUnits("VA")
_TsiModuleNominalVinAC_Type = Integer32
_TsiModuleNominalVinAC_Object = MibTableColumn
tsiModuleNominalVinAC = _TsiModuleNominalVinAC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 33),
    _TsiModuleNominalVinAC_Type()
)
tsiModuleNominalVinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleNominalVinAC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleNominalVinAC.setUnits("0.1V")
_TsiModuleNominalVinDC_Type = Integer32
_TsiModuleNominalVinDC_Object = MibTableColumn
tsiModuleNominalVinDC = _TsiModuleNominalVinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 34),
    _TsiModuleNominalVinDC_Type()
)
tsiModuleNominalVinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleNominalVinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleNominalVinDC.setUnits("0.1V")
_TsiModuleNominalFreqAC_Type = Integer32
_TsiModuleNominalFreqAC_Object = MibTableColumn
tsiModuleNominalFreqAC = _TsiModuleNominalFreqAC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 35),
    _TsiModuleNominalFreqAC_Type()
)
tsiModuleNominalFreqAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiModuleNominalFreqAC.setStatus("current")
if mibBuilder.loadTexts:
    tsiModuleNominalFreqAC.setUnits("0.1Hz")


class _TsiRestrained_Type(Integer32):
    """Custom type tsiRestrained based on Integer32"""
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


_TsiRestrained_Type.__name__ = "Integer32"
_TsiRestrained_Object = MibTableColumn
tsiRestrained = _TsiRestrained_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 36),
    _TsiRestrained_Type()
)
tsiRestrained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiRestrained.setStatus("current")


class _TsiEPC_Type(Integer32):
    """Custom type tsiEPC based on Integer32"""
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


_TsiEPC_Type.__name__ = "Integer32"
_TsiEPC_Object = MibTableColumn
tsiEPC = _TsiEPC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 1, 1, 1, 37),
    _TsiEPC_Type()
)
tsiEPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiEPC.setStatus("current")
_TsiPhases_ObjectIdentity = ObjectIdentity
tsiPhases = _TsiPhases_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2)
)
_TsiNbPhaseConfigured_Type = Integer32
_TsiNbPhaseConfigured_Object = MibScalar
tsiNbPhaseConfigured = _TsiNbPhaseConfigured_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 1),
    _TsiNbPhaseConfigured_Type()
)
tsiNbPhaseConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiNbPhaseConfigured.setStatus("current")
_TsiPhaseTable_Object = MibTable
tsiPhaseTable = _TsiPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tsiPhaseTable.setStatus("current")
_TsiPhaseTableEntry_Object = MibTableRow
tsiPhaseTableEntry = _TsiPhaseTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1)
)
tsiPhaseTableEntry.setIndexNames(
    (0, "CET-TSI-MIB", "tsiPhaseTableIndex"),
)
if mibBuilder.loadTexts:
    tsiPhaseTableEntry.setStatus("current")


class _TsiPhaseTableIndex_Type(Integer32):
    """Custom type tsiPhaseTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TsiPhaseTableIndex_Type.__name__ = "Integer32"
_TsiPhaseTableIndex_Object = MibTableColumn
tsiPhaseTableIndex = _TsiPhaseTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 1),
    _TsiPhaseTableIndex_Type()
)
tsiPhaseTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsiPhaseTableIndex.setStatus("current")


class _TsiPhaseAvailablePowerRatioW_Type(Integer32):
    """Custom type tsiPhaseAvailablePowerRatioW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiPhaseAvailablePowerRatioW_Type.__name__ = "Integer32"
_TsiPhaseAvailablePowerRatioW_Object = MibTableColumn
tsiPhaseAvailablePowerRatioW = _TsiPhaseAvailablePowerRatioW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 2),
    _TsiPhaseAvailablePowerRatioW_Type()
)
tsiPhaseAvailablePowerRatioW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerRatioW.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerRatioW.setUnits("%")


class _TsiPhaseAvailablePowerRatioVA_Type(Integer32):
    """Custom type tsiPhaseAvailablePowerRatioVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiPhaseAvailablePowerRatioVA_Type.__name__ = "Integer32"
_TsiPhaseAvailablePowerRatioVA_Object = MibTableColumn
tsiPhaseAvailablePowerRatioVA = _TsiPhaseAvailablePowerRatioVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 3),
    _TsiPhaseAvailablePowerRatioVA_Type()
)
tsiPhaseAvailablePowerRatioVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerRatioVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerRatioVA.setUnits("%")


class _TsiPhaseInstalledPowerRatioW_Type(Integer32):
    """Custom type tsiPhaseInstalledPowerRatioW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiPhaseInstalledPowerRatioW_Type.__name__ = "Integer32"
_TsiPhaseInstalledPowerRatioW_Object = MibTableColumn
tsiPhaseInstalledPowerRatioW = _TsiPhaseInstalledPowerRatioW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 4),
    _TsiPhaseInstalledPowerRatioW_Type()
)
tsiPhaseInstalledPowerRatioW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerRatioW.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerRatioW.setUnits("%")


class _TsiPhaseInstalledPowerRatioVA_Type(Integer32):
    """Custom type tsiPhaseInstalledPowerRatioVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiPhaseInstalledPowerRatioVA_Type.__name__ = "Integer32"
_TsiPhaseInstalledPowerRatioVA_Object = MibTableColumn
tsiPhaseInstalledPowerRatioVA = _TsiPhaseInstalledPowerRatioVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 5),
    _TsiPhaseInstalledPowerRatioVA_Type()
)
tsiPhaseInstalledPowerRatioVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerRatioVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerRatioVA.setUnits("%")
_TsiPhaseVout_Type = Integer32
_TsiPhaseVout_Object = MibTableColumn
tsiPhaseVout = _TsiPhaseVout_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 6),
    _TsiPhaseVout_Type()
)
tsiPhaseVout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseVout.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseVout.setUnits("0.1V")
_TsiPhaseIout_Type = Integer32
_TsiPhaseIout_Object = MibTableColumn
tsiPhaseIout = _TsiPhaseIout_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 7),
    _TsiPhaseIout_Type()
)
tsiPhaseIout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseIout.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseIout.setUnits("0.1V")
_TsiPhaseACOutFreq_Type = Integer32
_TsiPhaseACOutFreq_Object = MibTableColumn
tsiPhaseACOutFreq = _TsiPhaseACOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 8),
    _TsiPhaseACOutFreq_Type()
)
tsiPhaseACOutFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseACOutFreq.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseACOutFreq.setUnits("0.1Hz")
_TsiPhasePinDC_Type = Integer32
_TsiPhasePinDC_Object = MibTableColumn
tsiPhasePinDC = _TsiPhasePinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 9),
    _TsiPhasePinDC_Type()
)
tsiPhasePinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhasePinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhasePinDC.setUnits("W")
_TsiPhasePinACW_Type = Integer32
_TsiPhasePinACW_Object = MibTableColumn
tsiPhasePinACW = _TsiPhasePinACW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 10),
    _TsiPhasePinACW_Type()
)
tsiPhasePinACW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhasePinACW.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhasePinACW.setUnits("W")
_TsiPhasePinACVA_Type = Integer32
_TsiPhasePinACVA_Object = MibTableColumn
tsiPhasePinACVA = _TsiPhasePinACVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 11),
    _TsiPhasePinACVA_Type()
)
tsiPhasePinACVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhasePinACVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhasePinACVA.setUnits("VA")
_TsiPhaseCurrentPowerInW_Type = Integer32
_TsiPhaseCurrentPowerInW_Object = MibTableColumn
tsiPhaseCurrentPowerInW = _TsiPhaseCurrentPowerInW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 12),
    _TsiPhaseCurrentPowerInW_Type()
)
tsiPhaseCurrentPowerInW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseCurrentPowerInW.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseCurrentPowerInW.setUnits("W")
_TsiPhaseCurrentPowerInVA_Type = Integer32
_TsiPhaseCurrentPowerInVA_Object = MibTableColumn
tsiPhaseCurrentPowerInVA = _TsiPhaseCurrentPowerInVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 13),
    _TsiPhaseCurrentPowerInVA_Type()
)
tsiPhaseCurrentPowerInVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseCurrentPowerInVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseCurrentPowerInVA.setUnits("VA")
_TsiPhaseInstalledPowerInW_Type = Integer32
_TsiPhaseInstalledPowerInW_Object = MibTableColumn
tsiPhaseInstalledPowerInW = _TsiPhaseInstalledPowerInW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 14),
    _TsiPhaseInstalledPowerInW_Type()
)
tsiPhaseInstalledPowerInW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerInW.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerInW.setUnits("W")
_TsiPhaseInstalledPowerInVA_Type = Integer32
_TsiPhaseInstalledPowerInVA_Object = MibTableColumn
tsiPhaseInstalledPowerInVA = _TsiPhaseInstalledPowerInVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 15),
    _TsiPhaseInstalledPowerInVA_Type()
)
tsiPhaseInstalledPowerInVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerInVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseInstalledPowerInVA.setUnits("VA")
_TsiPhaseAvailablePowerInW_Type = Integer32
_TsiPhaseAvailablePowerInW_Object = MibTableColumn
tsiPhaseAvailablePowerInW = _TsiPhaseAvailablePowerInW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 16),
    _TsiPhaseAvailablePowerInW_Type()
)
tsiPhaseAvailablePowerInW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerInW.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerInW.setUnits("W")
_TsiPhaseAvailablePowerInVA_Type = Integer32
_TsiPhaseAvailablePowerInVA_Object = MibTableColumn
tsiPhaseAvailablePowerInVA = _TsiPhaseAvailablePowerInVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 17),
    _TsiPhaseAvailablePowerInVA_Type()
)
tsiPhaseAvailablePowerInVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerInVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiPhaseAvailablePowerInVA.setUnits("VA")
_TsiPhaseNbModConfigured_Type = Integer32
_TsiPhaseNbModConfigured_Object = MibTableColumn
tsiPhaseNbModConfigured = _TsiPhaseNbModConfigured_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 18),
    _TsiPhaseNbModConfigured_Type()
)
tsiPhaseNbModConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseNbModConfigured.setStatus("current")
_TsiPhaseRedundancy_Type = Integer32
_TsiPhaseRedundancy_Object = MibTableColumn
tsiPhaseRedundancy = _TsiPhaseRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 19),
    _TsiPhaseRedundancy_Type()
)
tsiPhaseRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseRedundancy.setStatus("current")
_TsiPhaseNbModSeen_Type = Integer32
_TsiPhaseNbModSeen_Object = MibTableColumn
tsiPhaseNbModSeen = _TsiPhaseNbModSeen_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 20),
    _TsiPhaseNbModSeen_Type()
)
tsiPhaseNbModSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseNbModSeen.setStatus("current")
_TsiPhaseNbModOK_Type = Integer32
_TsiPhaseNbModOK_Object = MibTableColumn
tsiPhaseNbModOK = _TsiPhaseNbModOK_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 21),
    _TsiPhaseNbModOK_Type()
)
tsiPhaseNbModOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseNbModOK.setStatus("current")
_TsiPhaseNbModMO_Type = Integer32
_TsiPhaseNbModMO_Object = MibTableColumn
tsiPhaseNbModMO = _TsiPhaseNbModMO_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 22),
    _TsiPhaseNbModMO_Type()
)
tsiPhaseNbModMO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseNbModMO.setStatus("current")
_TsiPhaseNbModKO_Type = Integer32
_TsiPhaseNbModKO_Object = MibTableColumn
tsiPhaseNbModKO = _TsiPhaseNbModKO_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 23),
    _TsiPhaseNbModKO_Type()
)
tsiPhaseNbModKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseNbModKO.setStatus("current")
_TsiPhaseNbModNT_Type = Integer32
_TsiPhaseNbModNT_Object = MibTableColumn
tsiPhaseNbModNT = _TsiPhaseNbModNT_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 2, 2, 1, 24),
    _TsiPhaseNbModNT_Type()
)
tsiPhaseNbModNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiPhaseNbModNT.setStatus("current")
_TsiACGroups_ObjectIdentity = ObjectIdentity
tsiACGroups = _TsiACGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3)
)
_TsiNbACGroupConfigured_Type = Integer32
_TsiNbACGroupConfigured_Object = MibScalar
tsiNbACGroupConfigured = _TsiNbACGroupConfigured_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 1),
    _TsiNbACGroupConfigured_Type()
)
tsiNbACGroupConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiNbACGroupConfigured.setStatus("current")
_TsiACGroupTable_Object = MibTable
tsiACGroupTable = _TsiACGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tsiACGroupTable.setStatus("current")
_TsiACGroupTableEntry_Object = MibTableRow
tsiACGroupTableEntry = _TsiACGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1)
)
tsiACGroupTableEntry.setIndexNames(
    (0, "CET-TSI-MIB", "tsiACGroupTableIndex"),
)
if mibBuilder.loadTexts:
    tsiACGroupTableEntry.setStatus("current")


class _TsiACGroupTableIndex_Type(Integer32):
    """Custom type tsiACGroupTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TsiACGroupTableIndex_Type.__name__ = "Integer32"
_TsiACGroupTableIndex_Object = MibTableColumn
tsiACGroupTableIndex = _TsiACGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 1),
    _TsiACGroupTableIndex_Type()
)
tsiACGroupTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsiACGroupTableIndex.setStatus("current")
_TsiACGroupVinAC_Type = Integer32
_TsiACGroupVinAC_Object = MibTableColumn
tsiACGroupVinAC = _TsiACGroupVinAC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 2),
    _TsiACGroupVinAC_Type()
)
tsiACGroupVinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupVinAC.setStatus("current")
if mibBuilder.loadTexts:
    tsiACGroupVinAC.setUnits("0.1V")
_TsiACGroupIinAC_Type = Integer32
_TsiACGroupIinAC_Object = MibTableColumn
tsiACGroupIinAC = _TsiACGroupIinAC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 3),
    _TsiACGroupIinAC_Type()
)
tsiACGroupIinAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupIinAC.setStatus("current")
if mibBuilder.loadTexts:
    tsiACGroupIinAC.setUnits("0.1A")
_TsiACGroupPinACW_Type = Integer32
_TsiACGroupPinACW_Object = MibTableColumn
tsiACGroupPinACW = _TsiACGroupPinACW_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 4),
    _TsiACGroupPinACW_Type()
)
tsiACGroupPinACW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupPinACW.setStatus("current")
if mibBuilder.loadTexts:
    tsiACGroupPinACW.setUnits("W")
_TsiACGroupPinACVA_Type = Integer32
_TsiACGroupPinACVA_Object = MibTableColumn
tsiACGroupPinACVA = _TsiACGroupPinACVA_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 5),
    _TsiACGroupPinACVA_Type()
)
tsiACGroupPinACVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupPinACVA.setStatus("current")
if mibBuilder.loadTexts:
    tsiACGroupPinACVA.setUnits("VA")
_TsiACGroupNbModSeen_Type = Integer32
_TsiACGroupNbModSeen_Object = MibTableColumn
tsiACGroupNbModSeen = _TsiACGroupNbModSeen_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 6),
    _TsiACGroupNbModSeen_Type()
)
tsiACGroupNbModSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupNbModSeen.setStatus("current")
_TsiACGroupNbModOK_Type = Integer32
_TsiACGroupNbModOK_Object = MibTableColumn
tsiACGroupNbModOK = _TsiACGroupNbModOK_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 7),
    _TsiACGroupNbModOK_Type()
)
tsiACGroupNbModOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupNbModOK.setStatus("current")
_TsiACGroupNbModMO_Type = Integer32
_TsiACGroupNbModMO_Object = MibTableColumn
tsiACGroupNbModMO = _TsiACGroupNbModMO_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 8),
    _TsiACGroupNbModMO_Type()
)
tsiACGroupNbModMO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupNbModMO.setStatus("current")
_TsiACGroupNbModKO_Type = Integer32
_TsiACGroupNbModKO_Object = MibTableColumn
tsiACGroupNbModKO = _TsiACGroupNbModKO_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 9),
    _TsiACGroupNbModKO_Type()
)
tsiACGroupNbModKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupNbModKO.setStatus("current")
_TsiACGroupNbModACinOK_Type = Integer32
_TsiACGroupNbModACinOK_Object = MibTableColumn
tsiACGroupNbModACinOK = _TsiACGroupNbModACinOK_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 10),
    _TsiACGroupNbModACinOK_Type()
)
tsiACGroupNbModACinOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupNbModACinOK.setStatus("current")
_TsiACGroupACinFreq_Type = Integer32
_TsiACGroupACinFreq_Object = MibTableColumn
tsiACGroupACinFreq = _TsiACGroupACinFreq_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 3, 2, 1, 11),
    _TsiACGroupACinFreq_Type()
)
tsiACGroupACinFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACGroupACinFreq.setStatus("current")
if mibBuilder.loadTexts:
    tsiACGroupACinFreq.setUnits("0.1Hz")
_TsiDCGroups_ObjectIdentity = ObjectIdentity
tsiDCGroups = _TsiDCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4)
)
_TsiNbDCGroupConfigured_Type = Integer32
_TsiNbDCGroupConfigured_Object = MibScalar
tsiNbDCGroupConfigured = _TsiNbDCGroupConfigured_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 1),
    _TsiNbDCGroupConfigured_Type()
)
tsiNbDCGroupConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiNbDCGroupConfigured.setStatus("current")
_TsiDCGroupTable_Object = MibTable
tsiDCGroupTable = _TsiDCGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tsiDCGroupTable.setStatus("current")
_TsiDCGroupTableEntry_Object = MibTableRow
tsiDCGroupTableEntry = _TsiDCGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1)
)
tsiDCGroupTableEntry.setIndexNames(
    (0, "CET-TSI-MIB", "tsiDCGroupTableIndex"),
)
if mibBuilder.loadTexts:
    tsiDCGroupTableEntry.setStatus("current")


class _TsiDCGroupTableIndex_Type(Integer32):
    """Custom type tsiDCGroupTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TsiDCGroupTableIndex_Type.__name__ = "Integer32"
_TsiDCGroupTableIndex_Object = MibTableColumn
tsiDCGroupTableIndex = _TsiDCGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 1),
    _TsiDCGroupTableIndex_Type()
)
tsiDCGroupTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsiDCGroupTableIndex.setStatus("current")
_TsiDCGroupVinDC_Type = Integer32
_TsiDCGroupVinDC_Object = MibTableColumn
tsiDCGroupVinDC = _TsiDCGroupVinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 2),
    _TsiDCGroupVinDC_Type()
)
tsiDCGroupVinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupVinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiDCGroupVinDC.setUnits("0.1V")
_TsiDCGroupIinDC_Type = Integer32
_TsiDCGroupIinDC_Object = MibTableColumn
tsiDCGroupIinDC = _TsiDCGroupIinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 3),
    _TsiDCGroupIinDC_Type()
)
tsiDCGroupIinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupIinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiDCGroupIinDC.setUnits("0.1A")
_TsiDCGroupPinDC_Type = Integer32
_TsiDCGroupPinDC_Object = MibTableColumn
tsiDCGroupPinDC = _TsiDCGroupPinDC_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 4),
    _TsiDCGroupPinDC_Type()
)
tsiDCGroupPinDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupPinDC.setStatus("current")
if mibBuilder.loadTexts:
    tsiDCGroupPinDC.setUnits("W")
_TsiDCGroupNbModSeen_Type = Integer32
_TsiDCGroupNbModSeen_Object = MibTableColumn
tsiDCGroupNbModSeen = _TsiDCGroupNbModSeen_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 5),
    _TsiDCGroupNbModSeen_Type()
)
tsiDCGroupNbModSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupNbModSeen.setStatus("current")
_TsiDCGroupNbModOK_Type = Integer32
_TsiDCGroupNbModOK_Object = MibTableColumn
tsiDCGroupNbModOK = _TsiDCGroupNbModOK_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 6),
    _TsiDCGroupNbModOK_Type()
)
tsiDCGroupNbModOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupNbModOK.setStatus("current")
_TsiDCGroupNbModMO_Type = Integer32
_TsiDCGroupNbModMO_Object = MibTableColumn
tsiDCGroupNbModMO = _TsiDCGroupNbModMO_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 7),
    _TsiDCGroupNbModMO_Type()
)
tsiDCGroupNbModMO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupNbModMO.setStatus("current")
_TsiDCGroupNbModKO_Type = Integer32
_TsiDCGroupNbModKO_Object = MibTableColumn
tsiDCGroupNbModKO = _TsiDCGroupNbModKO_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 8),
    _TsiDCGroupNbModKO_Type()
)
tsiDCGroupNbModKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupNbModKO.setStatus("current")
_TsiDCGroupNbModDCinOK_Type = Integer32
_TsiDCGroupNbModDCinOK_Object = MibTableColumn
tsiDCGroupNbModDCinOK = _TsiDCGroupNbModDCinOK_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 4, 2, 1, 9),
    _TsiDCGroupNbModDCinOK_Type()
)
tsiDCGroupNbModDCinOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDCGroupNbModDCinOK.setStatus("current")
_TsiAlarms_ObjectIdentity = ObjectIdentity
tsiAlarms = _TsiAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5)
)
_TsiNbMinorAlarm_Type = Integer32
_TsiNbMinorAlarm_Object = MibScalar
tsiNbMinorAlarm = _TsiNbMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 1),
    _TsiNbMinorAlarm_Type()
)
tsiNbMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiNbMinorAlarm.setStatus("current")
_TsiNbMajorAlarm_Type = Integer32
_TsiNbMajorAlarm_Object = MibScalar
tsiNbMajorAlarm = _TsiNbMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 2),
    _TsiNbMajorAlarm_Type()
)
tsiNbMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiNbMajorAlarm.setStatus("current")
_TsiTotalAlarmNumber_Type = Integer32
_TsiTotalAlarmNumber_Object = MibScalar
tsiTotalAlarmNumber = _TsiTotalAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 3),
    _TsiTotalAlarmNumber_Type()
)
tsiTotalAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiTotalAlarmNumber.setStatus("current")
_TsiAlarmTable_Object = MibTable
tsiAlarmTable = _TsiAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tsiAlarmTable.setStatus("current")
_TsiAlarmEntry_Object = MibTableRow
tsiAlarmEntry = _TsiAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4, 1)
)
tsiAlarmEntry.setIndexNames(
    (0, "CET-TSI-MIB", "tsiAlarmIndex"),
)
if mibBuilder.loadTexts:
    tsiAlarmEntry.setStatus("current")


class _TsiAlarmIndex_Type(Integer32):
    """Custom type tsiAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TsiAlarmIndex_Type.__name__ = "Integer32"
_TsiAlarmIndex_Object = MibTableColumn
tsiAlarmIndex = _TsiAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4, 1, 1),
    _TsiAlarmIndex_Type()
)
tsiAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsiAlarmIndex.setStatus("current")
_TsiAlarmID_Type = Integer32
_TsiAlarmID_Object = MibTableColumn
tsiAlarmID = _TsiAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4, 1, 2),
    _TsiAlarmID_Type()
)
tsiAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiAlarmID.setStatus("current")


class _TsiAlarmType_Type(Integer32):
    """Custom type tsiAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("minor", 1),
          ("major", 2))
    )


_TsiAlarmType_Type.__name__ = "Integer32"
_TsiAlarmType_Object = MibTableColumn
tsiAlarmType = _TsiAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4, 1, 3),
    _TsiAlarmType_Type()
)
tsiAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiAlarmType.setStatus("current")


class _TsiAlarmSource_Type(Integer32):
    """Custom type tsiAlarmSource based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("t2s", 0),
          ("module01", 1),
          ("module02", 2),
          ("module03", 3),
          ("module04", 4),
          ("module05", 5),
          ("module06", 6),
          ("module07", 7),
          ("module08", 8),
          ("module09", 9),
          ("module10", 10),
          ("module11", 11),
          ("module12", 12),
          ("module13", 13),
          ("module14", 14),
          ("module15", 15),
          ("module16", 16),
          ("module17", 17),
          ("module18", 18),
          ("module19", 19),
          ("module20", 20),
          ("module21", 21),
          ("module22", 22),
          ("module23", 23),
          ("module24", 24),
          ("module25", 25),
          ("module26", 26),
          ("module27", 27),
          ("module28", 28),
          ("module29", 29),
          ("module30", 30),
          ("module31", 31),
          ("module32", 32),
          ("system", 33))
    )


_TsiAlarmSource_Type.__name__ = "Integer32"
_TsiAlarmSource_Object = MibTableColumn
tsiAlarmSource = _TsiAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4, 1, 4),
    _TsiAlarmSource_Type()
)
tsiAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiAlarmSource.setStatus("current")
_TsiAlarmDescription_Type = DisplayString
_TsiAlarmDescription_Object = MibTableColumn
tsiAlarmDescription = _TsiAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4, 1, 5),
    _TsiAlarmDescription_Type()
)
tsiAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiAlarmDescription.setStatus("current")
_TsiAlarmTime_Type = DateAndTime
_TsiAlarmTime_Object = MibTableColumn
tsiAlarmTime = _TsiAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 4, 1, 6),
    _TsiAlarmTime_Type()
)
tsiAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiAlarmTime.setStatus("current")
_TsiTempoMajorRelay_Type = Integer32
_TsiTempoMajorRelay_Object = MibScalar
tsiTempoMajorRelay = _TsiTempoMajorRelay_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 5),
    _TsiTempoMajorRelay_Type()
)
tsiTempoMajorRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiTempoMajorRelay.setStatus("current")
if mibBuilder.loadTexts:
    tsiTempoMajorRelay.setUnits("s")
_TsiTempoMinorRelay_Type = Integer32
_TsiTempoMinorRelay_Object = MibScalar
tsiTempoMinorRelay = _TsiTempoMinorRelay_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 6),
    _TsiTempoMinorRelay_Type()
)
tsiTempoMinorRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiTempoMinorRelay.setStatus("current")
if mibBuilder.loadTexts:
    tsiTempoMinorRelay.setUnits("s")


class _TsiACInputPresent_Type(Integer32):
    """Custom type tsiACInputPresent based on Integer32"""
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


_TsiACInputPresent_Type.__name__ = "Integer32"
_TsiACInputPresent_Object = MibScalar
tsiACInputPresent = _TsiACInputPresent_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 7),
    _TsiACInputPresent_Type()
)
tsiACInputPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiACInputPresent.setStatus("current")


class _TsiSaturationThreshold_Type(Integer32):
    """Custom type tsiSaturationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiSaturationThreshold_Type.__name__ = "Integer32"
_TsiSaturationThreshold_Object = MibScalar
tsiSaturationThreshold = _TsiSaturationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 8),
    _TsiSaturationThreshold_Type()
)
tsiSaturationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiSaturationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tsiSaturationThreshold.setUnits("%")


class _TsiProgrammableRelay_Type(Integer32):
    """Custom type tsiProgrammableRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TsiProgrammableRelay_Type.__name__ = "Integer32"
_TsiProgrammableRelay_Object = MibScalar
tsiProgrammableRelay = _TsiProgrammableRelay_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 5, 9),
    _TsiProgrammableRelay_Type()
)
tsiProgrammableRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiProgrammableRelay.setStatus("current")
if mibBuilder.loadTexts:
    tsiProgrammableRelay.setUnits("%")
_TsiTraps_ObjectIdentity = ObjectIdentity
tsiTraps = _TsiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 6)
)
_TsiTrapsPrefix_ObjectIdentity = ObjectIdentity
tsiTrapsPrefix = _TsiTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 6, 0)
)
_TsiEventDescription_ObjectIdentity = ObjectIdentity
tsiEventDescription = _TsiEventDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 7)
)
_TsiEventDescriptionTable_Object = MibTable
tsiEventDescriptionTable = _TsiEventDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tsiEventDescriptionTable.setStatus("current")
_TsiEventDescriptionEntry_Object = MibTableRow
tsiEventDescriptionEntry = _TsiEventDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 7, 1, 1)
)
tsiEventDescriptionEntry.setIndexNames(
    (0, "CET-TSI-MIB", "tsiEventDescriptionIndex"),
)
if mibBuilder.loadTexts:
    tsiEventDescriptionEntry.setStatus("current")


class _TsiEventDescriptionIndex_Type(Integer32):
    """Custom type tsiEventDescriptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TsiEventDescriptionIndex_Type.__name__ = "Integer32"
_TsiEventDescriptionIndex_Object = MibTableColumn
tsiEventDescriptionIndex = _TsiEventDescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 7, 1, 1, 1),
    _TsiEventDescriptionIndex_Type()
)
tsiEventDescriptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsiEventDescriptionIndex.setStatus("current")
_TsiEventDescriptionString_Type = DisplayString
_TsiEventDescriptionString_Object = MibTableColumn
tsiEventDescriptionString = _TsiEventDescriptionString_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 7, 1, 1, 2),
    _TsiEventDescriptionString_Type()
)
tsiEventDescriptionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiEventDescriptionString.setStatus("current")
_TsiT2SInfo_ObjectIdentity = ObjectIdentity
tsiT2SInfo = _TsiT2SInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8)
)
_TsiT2SSoftwareVersion_Type = DisplayString
_TsiT2SSoftwareVersion_Object = MibScalar
tsiT2SSoftwareVersion = _TsiT2SSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8, 1),
    _TsiT2SSoftwareVersion_Type()
)
tsiT2SSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiT2SSoftwareVersion.setStatus("deprecated")
_TsiT2SSerialNumber_Type = DisplayString
_TsiT2SSerialNumber_Object = MibScalar
tsiT2SSerialNumber = _TsiT2SSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8, 2),
    _TsiT2SSerialNumber_Type()
)
tsiT2SSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiT2SSerialNumber.setStatus("current")
_TsiT2SDateAndTime_Type = DateAndTime
_TsiT2SDateAndTime_Object = MibScalar
tsiT2SDateAndTime = _TsiT2SDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8, 3),
    _TsiT2SDateAndTime_Type()
)
tsiT2SDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiT2SDateAndTime.setStatus("current")
_TsiT2SMainSoftwareVersion_Type = Integer32
_TsiT2SMainSoftwareVersion_Object = MibScalar
tsiT2SMainSoftwareVersion = _TsiT2SMainSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8, 4),
    _TsiT2SMainSoftwareVersion_Type()
)
tsiT2SMainSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiT2SMainSoftwareVersion.setStatus("current")
_TsiT2SSubSoftwareVersion_Type = Integer32
_TsiT2SSubSoftwareVersion_Object = MibScalar
tsiT2SSubSoftwareVersion = _TsiT2SSubSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8, 5),
    _TsiT2SSubSoftwareVersion_Type()
)
tsiT2SSubSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiT2SSubSoftwareVersion.setStatus("current")
_TsiT2SMaxKnownParameters_Type = Integer32
_TsiT2SMaxKnownParameters_Object = MibScalar
tsiT2SMaxKnownParameters = _TsiT2SMaxKnownParameters_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8, 6),
    _TsiT2SMaxKnownParameters_Type()
)
tsiT2SMaxKnownParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiT2SMaxKnownParameters.setStatus("current")
_TsiT2SVersionTextError_Type = Integer32
_TsiT2SVersionTextError_Object = MibScalar
tsiT2SVersionTextError = _TsiT2SVersionTextError_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 8, 7),
    _TsiT2SVersionTextError_Type()
)
tsiT2SVersionTextError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiT2SVersionTextError.setStatus("current")
_TsiConfiguration_ObjectIdentity = ObjectIdentity
tsiConfiguration = _TsiConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9)
)
_TsiConfigurationTable_Object = MibTable
tsiConfigurationTable = _TsiConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tsiConfigurationTable.setStatus("current")
_TsiConfigurationEntry_Object = MibTableRow
tsiConfigurationEntry = _TsiConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1, 1)
)
tsiConfigurationEntry.setIndexNames(
    (0, "CET-TSI-MIB", "tsiConfigurationIndex"),
)
if mibBuilder.loadTexts:
    tsiConfigurationEntry.setStatus("current")


class _TsiConfigurationIndex_Type(Integer32):
    """Custom type tsiConfigurationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_TsiConfigurationIndex_Type.__name__ = "Integer32"
_TsiConfigurationIndex_Object = MibTableColumn
tsiConfigurationIndex = _TsiConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1, 1, 1),
    _TsiConfigurationIndex_Type()
)
tsiConfigurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsiConfigurationIndex.setStatus("current")
_TsiConfigurationID_Type = Integer32
_TsiConfigurationID_Object = MibTableColumn
tsiConfigurationID = _TsiConfigurationID_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1, 1, 2),
    _TsiConfigurationID_Type()
)
tsiConfigurationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiConfigurationID.setStatus("current")
_TsiConfigurationValue_Type = Integer32
_TsiConfigurationValue_Object = MibTableColumn
tsiConfigurationValue = _TsiConfigurationValue_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1, 1, 3),
    _TsiConfigurationValue_Type()
)
tsiConfigurationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiConfigurationValue.setStatus("current")
_TsiConfigurationDescription_Type = DisplayString
_TsiConfigurationDescription_Object = MibTableColumn
tsiConfigurationDescription = _TsiConfigurationDescription_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1, 1, 4),
    _TsiConfigurationDescription_Type()
)
tsiConfigurationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiConfigurationDescription.setStatus("current")
_TsiConfigurationUnits_Type = Integer32
_TsiConfigurationUnits_Object = MibTableColumn
tsiConfigurationUnits = _TsiConfigurationUnits_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1, 1, 5),
    _TsiConfigurationUnits_Type()
)
tsiConfigurationUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiConfigurationUnits.setStatus("current")
_TsiConfigurationValidity_Type = DisplayString
_TsiConfigurationValidity_Object = MibTableColumn
tsiConfigurationValidity = _TsiConfigurationValidity_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 1, 1, 6),
    _TsiConfigurationValidity_Type()
)
tsiConfigurationValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiConfigurationValidity.setStatus("current")
_TsiDigInpLabel1_Type = DisplayString
_TsiDigInpLabel1_Object = MibScalar
tsiDigInpLabel1 = _TsiDigInpLabel1_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 2),
    _TsiDigInpLabel1_Type()
)
tsiDigInpLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDigInpLabel1.setStatus("current")
_TsiDigInpLabel2_Type = DisplayString
_TsiDigInpLabel2_Object = MibScalar
tsiDigInpLabel2 = _TsiDigInpLabel2_Object(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 9, 3),
    _TsiDigInpLabel2_Type()
)
tsiDigInpLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsiDigInpLabel2.setStatus("current")
_TsiConformance_ObjectIdentity = ObjectIdentity
tsiConformance = _TsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2)
)
_TsiMIBCompliances_ObjectIdentity = ObjectIdentity
tsiMIBCompliances = _TsiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2, 1)
)
_TsiMIBGroups_ObjectIdentity = ObjectIdentity
tsiMIBGroups = _TsiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2, 2)
)

# Managed Objects groups

tsiFunctionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2, 2, 1)
)
tsiFunctionalGroup.setObjects(
      *(("CET-TSI-MIB", "tsiModuleSeen"),
        ("CET-TSI-MIB", "tsiModuleACOutState"),
        ("CET-TSI-MIB", "tsiModuleACInState"),
        ("CET-TSI-MIB", "tsiModuleDCInState"),
        ("CET-TSI-MIB", "tsiModuleAddress"),
        ("CET-TSI-MIB", "tsiModuleInputRepartition"),
        ("CET-TSI-MIB", "tsiModuleLoadRatioW"),
        ("CET-TSI-MIB", "tsiModuleLoadRatioVA"),
        ("CET-TSI-MIB", "tsiModulePhaseNumber"),
        ("CET-TSI-MIB", "tsiModuleACGroupNumber"),
        ("CET-TSI-MIB", "tsiModuleDCGroupNumber"),
        ("CET-TSI-MIB", "tsiModuleStatus"),
        ("CET-TSI-MIB", "tsiModuleACInStatus"),
        ("CET-TSI-MIB", "tsiModuleDCInStatus"),
        ("CET-TSI-MIB", "tsiModuleVout"),
        ("CET-TSI-MIB", "tsiModuleIout"),
        ("CET-TSI-MIB", "tsiModulePoutW"),
        ("CET-TSI-MIB", "tsiModulePoutVA"),
        ("CET-TSI-MIB", "tsiModuleVinAC"),
        ("CET-TSI-MIB", "tsiModuleIinAC"),
        ("CET-TSI-MIB", "tsiModulePinACW"),
        ("CET-TSI-MIB", "tsiModulePinACVA"),
        ("CET-TSI-MIB", "tsiModuleACinFreq"),
        ("CET-TSI-MIB", "tsiModuleVinDC"),
        ("CET-TSI-MIB", "tsiModuleIinDC"),
        ("CET-TSI-MIB", "tsiModulePinDC"),
        ("CET-TSI-MIB", "tsiModuleTemperature"),
        ("CET-TSI-MIB", "tsiModuleSoftwareVersion"),
        ("CET-TSI-MIB", "tsiModuleSerialNumber"),
        ("CET-TSI-MIB", "tsiModuleNominalPoutW"),
        ("CET-TSI-MIB", "tsiModuleNominalPoutVA"),
        ("CET-TSI-MIB", "tsiModuleNominalVinAC"),
        ("CET-TSI-MIB", "tsiModuleNominalVinDC"),
        ("CET-TSI-MIB", "tsiModuleNominalFreqAC"),
        ("CET-TSI-MIB", "tsiRestrained"),
        ("CET-TSI-MIB", "tsiEPC"),
        ("CET-TSI-MIB", "tsiNbPhaseConfigured"),
        ("CET-TSI-MIB", "tsiPhaseAvailablePowerRatioW"),
        ("CET-TSI-MIB", "tsiPhaseAvailablePowerRatioVA"),
        ("CET-TSI-MIB", "tsiPhaseInstalledPowerRatioW"),
        ("CET-TSI-MIB", "tsiPhaseInstalledPowerRatioVA"),
        ("CET-TSI-MIB", "tsiPhaseVout"),
        ("CET-TSI-MIB", "tsiPhaseIout"),
        ("CET-TSI-MIB", "tsiPhaseACOutFreq"),
        ("CET-TSI-MIB", "tsiPhasePinDC"),
        ("CET-TSI-MIB", "tsiPhasePinACW"),
        ("CET-TSI-MIB", "tsiPhasePinACVA"),
        ("CET-TSI-MIB", "tsiPhaseCurrentPowerInW"),
        ("CET-TSI-MIB", "tsiPhaseCurrentPowerInVA"),
        ("CET-TSI-MIB", "tsiPhaseInstalledPowerInW"),
        ("CET-TSI-MIB", "tsiPhaseInstalledPowerInVA"),
        ("CET-TSI-MIB", "tsiPhaseAvailablePowerInW"),
        ("CET-TSI-MIB", "tsiPhaseAvailablePowerInVA"),
        ("CET-TSI-MIB", "tsiPhaseNbModConfigured"),
        ("CET-TSI-MIB", "tsiPhaseRedundancy"),
        ("CET-TSI-MIB", "tsiPhaseNbModSeen"),
        ("CET-TSI-MIB", "tsiPhaseNbModOK"),
        ("CET-TSI-MIB", "tsiPhaseNbModMO"),
        ("CET-TSI-MIB", "tsiPhaseNbModKO"),
        ("CET-TSI-MIB", "tsiPhaseNbModNT"),
        ("CET-TSI-MIB", "tsiNbACGroupConfigured"),
        ("CET-TSI-MIB", "tsiACGroupVinAC"),
        ("CET-TSI-MIB", "tsiACGroupIinAC"),
        ("CET-TSI-MIB", "tsiACGroupPinACW"),
        ("CET-TSI-MIB", "tsiACGroupPinACVA"),
        ("CET-TSI-MIB", "tsiACGroupNbModSeen"),
        ("CET-TSI-MIB", "tsiACGroupNbModOK"),
        ("CET-TSI-MIB", "tsiACGroupNbModMO"),
        ("CET-TSI-MIB", "tsiACGroupNbModKO"),
        ("CET-TSI-MIB", "tsiACGroupNbModACinOK"),
        ("CET-TSI-MIB", "tsiACGroupACinFreq"),
        ("CET-TSI-MIB", "tsiNbDCGroupConfigured"),
        ("CET-TSI-MIB", "tsiDCGroupVinDC"),
        ("CET-TSI-MIB", "tsiDCGroupIinDC"),
        ("CET-TSI-MIB", "tsiDCGroupPinDC"),
        ("CET-TSI-MIB", "tsiDCGroupNbModSeen"),
        ("CET-TSI-MIB", "tsiDCGroupNbModOK"),
        ("CET-TSI-MIB", "tsiDCGroupNbModMO"),
        ("CET-TSI-MIB", "tsiDCGroupNbModKO"),
        ("CET-TSI-MIB", "tsiDCGroupNbModDCinOK"),
        ("CET-TSI-MIB", "tsiNbMinorAlarm"),
        ("CET-TSI-MIB", "tsiNbMajorAlarm"),
        ("CET-TSI-MIB", "tsiTotalAlarmNumber"),
        ("CET-TSI-MIB", "tsiAlarmID"),
        ("CET-TSI-MIB", "tsiAlarmType"),
        ("CET-TSI-MIB", "tsiAlarmSource"),
        ("CET-TSI-MIB", "tsiAlarmDescription"),
        ("CET-TSI-MIB", "tsiAlarmTime"),
        ("CET-TSI-MIB", "tsiTempoMajorRelay"),
        ("CET-TSI-MIB", "tsiTempoMinorRelay"),
        ("CET-TSI-MIB", "tsiACInputPresent"),
        ("CET-TSI-MIB", "tsiSaturationThreshold"),
        ("CET-TSI-MIB", "tsiProgrammableRelay"),
        ("CET-TSI-MIB", "tsiEventDescriptionString"),
        ("CET-TSI-MIB", "tsiT2SSerialNumber"),
        ("CET-TSI-MIB", "tsiT2SDateAndTime"),
        ("CET-TSI-MIB", "tsiT2SMainSoftwareVersion"),
        ("CET-TSI-MIB", "tsiT2SSubSoftwareVersion"),
        ("CET-TSI-MIB", "tsiT2SMaxKnownParameters"),
        ("CET-TSI-MIB", "tsiT2SVersionTextError"),
        ("CET-TSI-MIB", "tsiConfigurationID"),
        ("CET-TSI-MIB", "tsiConfigurationValue"),
        ("CET-TSI-MIB", "tsiConfigurationDescription"),
        ("CET-TSI-MIB", "tsiConfigurationUnits"),
        ("CET-TSI-MIB", "tsiConfigurationValidity"),
        ("CET-TSI-MIB", "tsiDigInpLabel1"),
        ("CET-TSI-MIB", "tsiDigInpLabel2"))
)
if mibBuilder.loadTexts:
    tsiFunctionalGroup.setStatus("current")

tsiDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2, 2, 3)
)
tsiDeprecatedGroup.setObjects(
    ("CET-TSI-MIB", "tsiT2SSoftwareVersion")
)
if mibBuilder.loadTexts:
    tsiDeprecatedGroup.setStatus("deprecated")


# Notification objects

tsiTrapMajorAlarmAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 6, 0, 1)
)
tsiTrapMajorAlarmAdded.setObjects(
      *(("CET-TSI-MIB", "tsiAlarmID"),
        ("CET-TSI-MIB", "tsiAlarmSource"),
        ("CET-TSI-MIB", "tsiAlarmDescription"),
        ("CET-TSI-MIB", "tsiAlarmTime"))
)
if mibBuilder.loadTexts:
    tsiTrapMajorAlarmAdded.setStatus(
        "current"
    )

tsiTrapMajorAlarmRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 6, 0, 2)
)
tsiTrapMajorAlarmRemoved.setObjects(
      *(("CET-TSI-MIB", "tsiAlarmID"),
        ("CET-TSI-MIB", "tsiAlarmSource"),
        ("CET-TSI-MIB", "tsiAlarmDescription"),
        ("CET-TSI-MIB", "tsiAlarmTime"))
)
if mibBuilder.loadTexts:
    tsiTrapMajorAlarmRemoved.setStatus(
        "current"
    )

tsiTrapMinorAlarmAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 6, 0, 3)
)
tsiTrapMinorAlarmAdded.setObjects(
      *(("CET-TSI-MIB", "tsiAlarmID"),
        ("CET-TSI-MIB", "tsiAlarmSource"),
        ("CET-TSI-MIB", "tsiAlarmDescription"),
        ("CET-TSI-MIB", "tsiAlarmTime"))
)
if mibBuilder.loadTexts:
    tsiTrapMinorAlarmAdded.setStatus(
        "current"
    )

tsiTrapMinorAlarmRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 12551, 4, 1, 6, 0, 4)
)
tsiTrapMinorAlarmRemoved.setObjects(
      *(("CET-TSI-MIB", "tsiAlarmID"),
        ("CET-TSI-MIB", "tsiAlarmSource"),
        ("CET-TSI-MIB", "tsiAlarmDescription"),
        ("CET-TSI-MIB", "tsiAlarmTime"))
)
if mibBuilder.loadTexts:
    tsiTrapMinorAlarmRemoved.setStatus(
        "current"
    )


# Notifications groups

tsiNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2, 2, 2)
)
tsiNotificationGroup.setObjects(
      *(("CET-TSI-MIB", "tsiTrapMajorAlarmAdded"),
        ("CET-TSI-MIB", "tsiTrapMajorAlarmRemoved"),
        ("CET-TSI-MIB", "tsiTrapMinorAlarmAdded"),
        ("CET-TSI-MIB", "tsiTrapMinorAlarmRemoved"))
)
if mibBuilder.loadTexts:
    tsiNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tsiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2, 1, 1)
)
tsiMIBCompliance.setObjects(
      *(("CET-TSI-MIB", "tsiFunctionalGroup"),
        ("CET-TSI-MIB", "tsiNotificationGroup"))
)
if mibBuilder.loadTexts:
    tsiMIBCompliance.setStatus(
        "current"
    )

tsiMIBDeprecated = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12551, 4, 2, 1, 2)
)
tsiMIBDeprecated.setObjects(
    ("CET-TSI-MIB", "tsiDeprecatedGroup")
)
if mibBuilder.loadTexts:
    tsiMIBDeprecated.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CET-TSI-MIB",
    **{"cetTSIMIB": cetTSIMIB,
       "tsiObjects": tsiObjects,
       "tsiModules": tsiModules,
       "tsiModuleTable": tsiModuleTable,
       "tsiModuleTableEntry": tsiModuleTableEntry,
       "tsiModuleTableIndex": tsiModuleTableIndex,
       "tsiModuleSeen": tsiModuleSeen,
       "tsiModuleACOutState": tsiModuleACOutState,
       "tsiModuleACInState": tsiModuleACInState,
       "tsiModuleDCInState": tsiModuleDCInState,
       "tsiModuleAddress": tsiModuleAddress,
       "tsiModuleInputRepartition": tsiModuleInputRepartition,
       "tsiModuleLoadRatioW": tsiModuleLoadRatioW,
       "tsiModuleLoadRatioVA": tsiModuleLoadRatioVA,
       "tsiModulePhaseNumber": tsiModulePhaseNumber,
       "tsiModuleACGroupNumber": tsiModuleACGroupNumber,
       "tsiModuleDCGroupNumber": tsiModuleDCGroupNumber,
       "tsiModuleStatus": tsiModuleStatus,
       "tsiModuleACInStatus": tsiModuleACInStatus,
       "tsiModuleDCInStatus": tsiModuleDCInStatus,
       "tsiModuleVout": tsiModuleVout,
       "tsiModuleIout": tsiModuleIout,
       "tsiModulePoutW": tsiModulePoutW,
       "tsiModulePoutVA": tsiModulePoutVA,
       "tsiModuleVinAC": tsiModuleVinAC,
       "tsiModuleIinAC": tsiModuleIinAC,
       "tsiModulePinACW": tsiModulePinACW,
       "tsiModulePinACVA": tsiModulePinACVA,
       "tsiModuleACinFreq": tsiModuleACinFreq,
       "tsiModuleVinDC": tsiModuleVinDC,
       "tsiModuleIinDC": tsiModuleIinDC,
       "tsiModulePinDC": tsiModulePinDC,
       "tsiModuleTemperature": tsiModuleTemperature,
       "tsiModuleSoftwareVersion": tsiModuleSoftwareVersion,
       "tsiModuleSerialNumber": tsiModuleSerialNumber,
       "tsiModuleNominalPoutW": tsiModuleNominalPoutW,
       "tsiModuleNominalPoutVA": tsiModuleNominalPoutVA,
       "tsiModuleNominalVinAC": tsiModuleNominalVinAC,
       "tsiModuleNominalVinDC": tsiModuleNominalVinDC,
       "tsiModuleNominalFreqAC": tsiModuleNominalFreqAC,
       "tsiRestrained": tsiRestrained,
       "tsiEPC": tsiEPC,
       "tsiPhases": tsiPhases,
       "tsiNbPhaseConfigured": tsiNbPhaseConfigured,
       "tsiPhaseTable": tsiPhaseTable,
       "tsiPhaseTableEntry": tsiPhaseTableEntry,
       "tsiPhaseTableIndex": tsiPhaseTableIndex,
       "tsiPhaseAvailablePowerRatioW": tsiPhaseAvailablePowerRatioW,
       "tsiPhaseAvailablePowerRatioVA": tsiPhaseAvailablePowerRatioVA,
       "tsiPhaseInstalledPowerRatioW": tsiPhaseInstalledPowerRatioW,
       "tsiPhaseInstalledPowerRatioVA": tsiPhaseInstalledPowerRatioVA,
       "tsiPhaseVout": tsiPhaseVout,
       "tsiPhaseIout": tsiPhaseIout,
       "tsiPhaseACOutFreq": tsiPhaseACOutFreq,
       "tsiPhasePinDC": tsiPhasePinDC,
       "tsiPhasePinACW": tsiPhasePinACW,
       "tsiPhasePinACVA": tsiPhasePinACVA,
       "tsiPhaseCurrentPowerInW": tsiPhaseCurrentPowerInW,
       "tsiPhaseCurrentPowerInVA": tsiPhaseCurrentPowerInVA,
       "tsiPhaseInstalledPowerInW": tsiPhaseInstalledPowerInW,
       "tsiPhaseInstalledPowerInVA": tsiPhaseInstalledPowerInVA,
       "tsiPhaseAvailablePowerInW": tsiPhaseAvailablePowerInW,
       "tsiPhaseAvailablePowerInVA": tsiPhaseAvailablePowerInVA,
       "tsiPhaseNbModConfigured": tsiPhaseNbModConfigured,
       "tsiPhaseRedundancy": tsiPhaseRedundancy,
       "tsiPhaseNbModSeen": tsiPhaseNbModSeen,
       "tsiPhaseNbModOK": tsiPhaseNbModOK,
       "tsiPhaseNbModMO": tsiPhaseNbModMO,
       "tsiPhaseNbModKO": tsiPhaseNbModKO,
       "tsiPhaseNbModNT": tsiPhaseNbModNT,
       "tsiACGroups": tsiACGroups,
       "tsiNbACGroupConfigured": tsiNbACGroupConfigured,
       "tsiACGroupTable": tsiACGroupTable,
       "tsiACGroupTableEntry": tsiACGroupTableEntry,
       "tsiACGroupTableIndex": tsiACGroupTableIndex,
       "tsiACGroupVinAC": tsiACGroupVinAC,
       "tsiACGroupIinAC": tsiACGroupIinAC,
       "tsiACGroupPinACW": tsiACGroupPinACW,
       "tsiACGroupPinACVA": tsiACGroupPinACVA,
       "tsiACGroupNbModSeen": tsiACGroupNbModSeen,
       "tsiACGroupNbModOK": tsiACGroupNbModOK,
       "tsiACGroupNbModMO": tsiACGroupNbModMO,
       "tsiACGroupNbModKO": tsiACGroupNbModKO,
       "tsiACGroupNbModACinOK": tsiACGroupNbModACinOK,
       "tsiACGroupACinFreq": tsiACGroupACinFreq,
       "tsiDCGroups": tsiDCGroups,
       "tsiNbDCGroupConfigured": tsiNbDCGroupConfigured,
       "tsiDCGroupTable": tsiDCGroupTable,
       "tsiDCGroupTableEntry": tsiDCGroupTableEntry,
       "tsiDCGroupTableIndex": tsiDCGroupTableIndex,
       "tsiDCGroupVinDC": tsiDCGroupVinDC,
       "tsiDCGroupIinDC": tsiDCGroupIinDC,
       "tsiDCGroupPinDC": tsiDCGroupPinDC,
       "tsiDCGroupNbModSeen": tsiDCGroupNbModSeen,
       "tsiDCGroupNbModOK": tsiDCGroupNbModOK,
       "tsiDCGroupNbModMO": tsiDCGroupNbModMO,
       "tsiDCGroupNbModKO": tsiDCGroupNbModKO,
       "tsiDCGroupNbModDCinOK": tsiDCGroupNbModDCinOK,
       "tsiAlarms": tsiAlarms,
       "tsiNbMinorAlarm": tsiNbMinorAlarm,
       "tsiNbMajorAlarm": tsiNbMajorAlarm,
       "tsiTotalAlarmNumber": tsiTotalAlarmNumber,
       "tsiAlarmTable": tsiAlarmTable,
       "tsiAlarmEntry": tsiAlarmEntry,
       "tsiAlarmIndex": tsiAlarmIndex,
       "tsiAlarmID": tsiAlarmID,
       "tsiAlarmType": tsiAlarmType,
       "tsiAlarmSource": tsiAlarmSource,
       "tsiAlarmDescription": tsiAlarmDescription,
       "tsiAlarmTime": tsiAlarmTime,
       "tsiTempoMajorRelay": tsiTempoMajorRelay,
       "tsiTempoMinorRelay": tsiTempoMinorRelay,
       "tsiACInputPresent": tsiACInputPresent,
       "tsiSaturationThreshold": tsiSaturationThreshold,
       "tsiProgrammableRelay": tsiProgrammableRelay,
       "tsiTraps": tsiTraps,
       "tsiTrapsPrefix": tsiTrapsPrefix,
       "tsiTrapMajorAlarmAdded": tsiTrapMajorAlarmAdded,
       "tsiTrapMajorAlarmRemoved": tsiTrapMajorAlarmRemoved,
       "tsiTrapMinorAlarmAdded": tsiTrapMinorAlarmAdded,
       "tsiTrapMinorAlarmRemoved": tsiTrapMinorAlarmRemoved,
       "tsiEventDescription": tsiEventDescription,
       "tsiEventDescriptionTable": tsiEventDescriptionTable,
       "tsiEventDescriptionEntry": tsiEventDescriptionEntry,
       "tsiEventDescriptionIndex": tsiEventDescriptionIndex,
       "tsiEventDescriptionString": tsiEventDescriptionString,
       "tsiT2SInfo": tsiT2SInfo,
       "tsiT2SSoftwareVersion": tsiT2SSoftwareVersion,
       "tsiT2SSerialNumber": tsiT2SSerialNumber,
       "tsiT2SDateAndTime": tsiT2SDateAndTime,
       "tsiT2SMainSoftwareVersion": tsiT2SMainSoftwareVersion,
       "tsiT2SSubSoftwareVersion": tsiT2SSubSoftwareVersion,
       "tsiT2SMaxKnownParameters": tsiT2SMaxKnownParameters,
       "tsiT2SVersionTextError": tsiT2SVersionTextError,
       "tsiConfiguration": tsiConfiguration,
       "tsiConfigurationTable": tsiConfigurationTable,
       "tsiConfigurationEntry": tsiConfigurationEntry,
       "tsiConfigurationIndex": tsiConfigurationIndex,
       "tsiConfigurationID": tsiConfigurationID,
       "tsiConfigurationValue": tsiConfigurationValue,
       "tsiConfigurationDescription": tsiConfigurationDescription,
       "tsiConfigurationUnits": tsiConfigurationUnits,
       "tsiConfigurationValidity": tsiConfigurationValidity,
       "tsiDigInpLabel1": tsiDigInpLabel1,
       "tsiDigInpLabel2": tsiDigInpLabel2,
       "tsiConformance": tsiConformance,
       "tsiMIBCompliances": tsiMIBCompliances,
       "tsiMIBCompliance": tsiMIBCompliance,
       "tsiMIBDeprecated": tsiMIBDeprecated,
       "tsiMIBGroups": tsiMIBGroups,
       "tsiFunctionalGroup": tsiFunctionalGroup,
       "tsiNotificationGroup": tsiNotificationGroup,
       "tsiDeprecatedGroup": tsiDeprecatedGroup}
)
