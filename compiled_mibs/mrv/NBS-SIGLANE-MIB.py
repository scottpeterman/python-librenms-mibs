# SNMP MIB module (NBS-SIGLANE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-SIGLANE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:33 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(NbsCmmcChannelBand,) = mibBuilder.importSymbols(
    "NBS-CMMCENUM-MIB",
    "NbsCmmcChannelBand")

(NbsTcMHz,
 NbsTcMicroAmp,
 NbsTcMilliDb,
 NbsTcTemperature,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcMHz",
    "NbsTcMicroAmp",
    "NbsTcMilliDb",
    "NbsTcTemperature",
    "nbs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nbsSigLaneMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsSigLanePortGrp_ObjectIdentity = ObjectIdentity
nbsSigLanePortGrp = _NbsSigLanePortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 10)
)
if mibBuilder.loadTexts:
    nbsSigLanePortGrp.setStatus("current")
_NbsSigLanePortTable_Object = MibTable
nbsSigLanePortTable = _NbsSigLanePortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1)
)
if mibBuilder.loadTexts:
    nbsSigLanePortTable.setStatus("current")
_NbsSigLanePortEntry_Object = MibTableRow
nbsSigLanePortEntry = _NbsSigLanePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1)
)
nbsSigLanePortEntry.setIndexNames(
    (0, "NBS-SIGLANE-MIB", "nbsSigLanePortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigLanePortEntry.setStatus("current")
_NbsSigLanePortIfIndex_Type = InterfaceIndex
_NbsSigLanePortIfIndex_Object = MibTableColumn
nbsSigLanePortIfIndex = _NbsSigLanePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 1),
    _NbsSigLanePortIfIndex_Type()
)
nbsSigLanePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLanePortIfIndex.setStatus("current")


class _NbsSigLanePortFacility_Type(Integer32):
    """Custom type nbsSigLanePortFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("fiber", 2),
          ("lambda", 3))
    )


_NbsSigLanePortFacility_Type.__name__ = "Integer32"
_NbsSigLanePortFacility_Object = MibTableColumn
nbsSigLanePortFacility = _NbsSigLanePortFacility_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 10),
    _NbsSigLanePortFacility_Type()
)
nbsSigLanePortFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLanePortFacility.setStatus("current")
_NbsSigLanePortLanes_Type = Integer32
_NbsSigLanePortLanes_Object = MibTableColumn
nbsSigLanePortLanes = _NbsSigLanePortLanes_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 20),
    _NbsSigLanePortLanes_Type()
)
nbsSigLanePortLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLanePortLanes.setStatus("current")
_NbsSigLaneLaneGrp_ObjectIdentity = ObjectIdentity
nbsSigLaneLaneGrp = _NbsSigLaneLaneGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 20)
)
if mibBuilder.loadTexts:
    nbsSigLaneLaneGrp.setStatus("current")
_NbsSigLaneLaneTable_Object = MibTable
nbsSigLaneLaneTable = _NbsSigLaneLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1)
)
if mibBuilder.loadTexts:
    nbsSigLaneLaneTable.setStatus("current")
_NbsSigLaneLaneEntry_Object = MibTableRow
nbsSigLaneLaneEntry = _NbsSigLaneLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1)
)
nbsSigLaneLaneEntry.setIndexNames(
    (0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIfIndex"),
    (0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIndex"),
)
if mibBuilder.loadTexts:
    nbsSigLaneLaneEntry.setStatus("current")
_NbsSigLaneLaneIfIndex_Type = InterfaceIndex
_NbsSigLaneLaneIfIndex_Object = MibTableColumn
nbsSigLaneLaneIfIndex = _NbsSigLaneLaneIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 1),
    _NbsSigLaneLaneIfIndex_Type()
)
nbsSigLaneLaneIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneIfIndex.setStatus("current")
_NbsSigLaneLaneIndex_Type = Integer32
_NbsSigLaneLaneIndex_Object = MibTableColumn
nbsSigLaneLaneIndex = _NbsSigLaneLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 2),
    _NbsSigLaneLaneIndex_Type()
)
nbsSigLaneLaneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneIndex.setStatus("current")
_NbsSigLaneLaneFrequency_Type = NbsTcMHz
_NbsSigLaneLaneFrequency_Object = MibTableColumn
nbsSigLaneLaneFrequency = _NbsSigLaneLaneFrequency_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 10),
    _NbsSigLaneLaneFrequency_Type()
)
nbsSigLaneLaneFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneFrequency.setStatus("current")


class _NbsSigLaneLaneWavelengthX_Type(DisplayString):
    """Custom type nbsSigLaneLaneWavelengthX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_NbsSigLaneLaneWavelengthX_Type.__name__ = "DisplayString"
_NbsSigLaneLaneWavelengthX_Object = MibTableColumn
nbsSigLaneLaneWavelengthX = _NbsSigLaneLaneWavelengthX_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 11),
    _NbsSigLaneLaneWavelengthX_Type()
)
nbsSigLaneLaneWavelengthX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneWavelengthX.setStatus("current")
_NbsSigLaneLaneChannelBand_Type = NbsCmmcChannelBand
_NbsSigLaneLaneChannelBand_Object = MibTableColumn
nbsSigLaneLaneChannelBand = _NbsSigLaneLaneChannelBand_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 12),
    _NbsSigLaneLaneChannelBand_Type()
)
nbsSigLaneLaneChannelBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneChannelBand.setStatus("current")
_NbsSigLaneLaneChannelNumber_Type = Integer32
_NbsSigLaneLaneChannelNumber_Object = MibTableColumn
nbsSigLaneLaneChannelNumber = _NbsSigLaneLaneChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 13),
    _NbsSigLaneLaneChannelNumber_Type()
)
nbsSigLaneLaneChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneChannelNumber.setStatus("current")


class _NbsSigLaneLaneTxDisable_Type(Integer32):
    """Custom type nbsSigLaneLaneTxDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("no", 2),
          ("yes", 3))
    )


_NbsSigLaneLaneTxDisable_Type.__name__ = "Integer32"
_NbsSigLaneLaneTxDisable_Object = MibTableColumn
nbsSigLaneLaneTxDisable = _NbsSigLaneLaneTxDisable_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 14),
    _NbsSigLaneLaneTxDisable_Type()
)
nbsSigLaneLaneTxDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigLaneLaneTxDisable.setStatus("current")


class _NbsSigLaneLaneFaultsCaps_Type(OctetString):
    """Custom type nbsSigLaneLaneFaultsCaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_NbsSigLaneLaneFaultsCaps_Type.__name__ = "OctetString"
_NbsSigLaneLaneFaultsCaps_Object = MibTableColumn
nbsSigLaneLaneFaultsCaps = _NbsSigLaneLaneFaultsCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 15),
    _NbsSigLaneLaneFaultsCaps_Type()
)
nbsSigLaneLaneFaultsCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneFaultsCaps.setStatus("current")


class _NbsSigLaneLaneFaultsOper_Type(OctetString):
    """Custom type nbsSigLaneLaneFaultsOper based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_NbsSigLaneLaneFaultsOper_Type.__name__ = "OctetString"
_NbsSigLaneLaneFaultsOper_Object = MibTableColumn
nbsSigLaneLaneFaultsOper = _NbsSigLaneLaneFaultsOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 16),
    _NbsSigLaneLaneFaultsOper_Type()
)
nbsSigLaneLaneFaultsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneFaultsOper.setStatus("current")


class _NbsSigLaneLaneTxPowerLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneTxPowerLevel based on Integer32"""
    defaultValue = 4

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
        *(("notSupported", 1),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("ok", 4),
          ("highWarning", 5),
          ("highAlarm", 6))
    )


_NbsSigLaneLaneTxPowerLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneTxPowerLevel_Object = MibTableColumn
nbsSigLaneLaneTxPowerLevel = _NbsSigLaneLaneTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 20),
    _NbsSigLaneLaneTxPowerLevel_Type()
)
nbsSigLaneLaneTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneTxPowerLevel.setStatus("current")


class _NbsSigLaneLaneTxPower_Type(NbsTcMilliDb):
    """Custom type nbsSigLaneLaneTxPower based on NbsTcMilliDb"""
    defaultValue = -2147483648


_NbsSigLaneLaneTxPower_Type.__name__ = "NbsTcMilliDb"
_NbsSigLaneLaneTxPower_Object = MibTableColumn
nbsSigLaneLaneTxPower = _NbsSigLaneLaneTxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 21),
    _NbsSigLaneLaneTxPower_Type()
)
nbsSigLaneLaneTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneTxPower.setStatus("current")


class _NbsSigLaneLaneTxPowerAdmin_Type(NbsTcMilliDb):
    """Custom type nbsSigLaneLaneTxPowerAdmin based on NbsTcMilliDb"""
    defaultValue = -2147483648


_NbsSigLaneLaneTxPowerAdmin_Type.__name__ = "NbsTcMilliDb"
_NbsSigLaneLaneTxPowerAdmin_Object = MibTableColumn
nbsSigLaneLaneTxPowerAdmin = _NbsSigLaneLaneTxPowerAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 22),
    _NbsSigLaneLaneTxPowerAdmin_Type()
)
nbsSigLaneLaneTxPowerAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigLaneLaneTxPowerAdmin.setStatus("current")


class _NbsSigLaneLaneRxPowerLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneRxPowerLevel based on Integer32"""
    defaultValue = 4

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
        *(("notSupported", 1),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("ok", 4),
          ("highWarning", 5),
          ("highAlarm", 6))
    )


_NbsSigLaneLaneRxPowerLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneRxPowerLevel_Object = MibTableColumn
nbsSigLaneLaneRxPowerLevel = _NbsSigLaneLaneRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 30),
    _NbsSigLaneLaneRxPowerLevel_Type()
)
nbsSigLaneLaneRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneRxPowerLevel.setStatus("current")


class _NbsSigLaneLaneRxPower_Type(NbsTcMilliDb):
    """Custom type nbsSigLaneLaneRxPower based on NbsTcMilliDb"""
    defaultValue = -2147483648


_NbsSigLaneLaneRxPower_Type.__name__ = "NbsTcMilliDb"
_NbsSigLaneLaneRxPower_Object = MibTableColumn
nbsSigLaneLaneRxPower = _NbsSigLaneLaneRxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 31),
    _NbsSigLaneLaneRxPower_Type()
)
nbsSigLaneLaneRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneRxPower.setStatus("current")


class _NbsSigLaneLaneBiasAmpsLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneBiasAmpsLevel based on Integer32"""
    defaultValue = 4

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
        *(("notSupported", 1),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("ok", 4),
          ("highWarning", 5),
          ("highAlarm", 6))
    )


_NbsSigLaneLaneBiasAmpsLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneBiasAmpsLevel_Object = MibTableColumn
nbsSigLaneLaneBiasAmpsLevel = _NbsSigLaneLaneBiasAmpsLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 40),
    _NbsSigLaneLaneBiasAmpsLevel_Type()
)
nbsSigLaneLaneBiasAmpsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneBiasAmpsLevel.setStatus("current")


class _NbsSigLaneLaneBiasAmps_Type(NbsTcMicroAmp):
    """Custom type nbsSigLaneLaneBiasAmps based on NbsTcMicroAmp"""
    defaultValue = -1


_NbsSigLaneLaneBiasAmps_Type.__name__ = "NbsTcMicroAmp"
_NbsSigLaneLaneBiasAmps_Object = MibTableColumn
nbsSigLaneLaneBiasAmps = _NbsSigLaneLaneBiasAmps_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 41),
    _NbsSigLaneLaneBiasAmps_Type()
)
nbsSigLaneLaneBiasAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneBiasAmps.setStatus("current")


class _NbsSigLaneLaneLaserTempLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneLaserTempLevel based on Integer32"""
    defaultValue = 4

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
        *(("notSupported", 1),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("ok", 4),
          ("highWarning", 5),
          ("highAlarm", 6))
    )


_NbsSigLaneLaneLaserTempLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneLaserTempLevel_Object = MibTableColumn
nbsSigLaneLaneLaserTempLevel = _NbsSigLaneLaneLaserTempLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 50),
    _NbsSigLaneLaneLaserTempLevel_Type()
)
nbsSigLaneLaneLaserTempLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneLaserTempLevel.setStatus("current")


class _NbsSigLaneLaneLaserTemp_Type(NbsTcTemperature):
    """Custom type nbsSigLaneLaneLaserTemp based on NbsTcTemperature"""
    defaultValue = -2147483648


_NbsSigLaneLaneLaserTemp_Type.__name__ = "NbsTcTemperature"
_NbsSigLaneLaneLaserTemp_Object = MibTableColumn
nbsSigLaneLaneLaserTemp = _NbsSigLaneLaneLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 51),
    _NbsSigLaneLaneLaserTemp_Type()
)
nbsSigLaneLaneLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneLaserTemp.setStatus("current")
_NbsSigLaneLaneEthTxAllOctets_Type = Counter64
_NbsSigLaneLaneEthTxAllOctets_Object = MibTableColumn
nbsSigLaneLaneEthTxAllOctets = _NbsSigLaneLaneEthTxAllOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 60),
    _NbsSigLaneLaneEthTxAllOctets_Type()
)
nbsSigLaneLaneEthTxAllOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneEthTxAllOctets.setStatus("current")
_NbsSigLaneLaneEthTxAllFrames_Type = Counter64
_NbsSigLaneLaneEthTxAllFrames_Object = MibTableColumn
nbsSigLaneLaneEthTxAllFrames = _NbsSigLaneLaneEthTxAllFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 61),
    _NbsSigLaneLaneEthTxAllFrames_Type()
)
nbsSigLaneLaneEthTxAllFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneEthTxAllFrames.setStatus("current")
_NbsSigLaneLaneEthRxAllOctets_Type = Counter64
_NbsSigLaneLaneEthRxAllOctets_Object = MibTableColumn
nbsSigLaneLaneEthRxAllOctets = _NbsSigLaneLaneEthRxAllOctets_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 70),
    _NbsSigLaneLaneEthRxAllOctets_Type()
)
nbsSigLaneLaneEthRxAllOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneEthRxAllOctets.setStatus("current")
_NbsSigLaneLaneEthRxAllFrames_Type = Counter64
_NbsSigLaneLaneEthRxAllFrames_Object = MibTableColumn
nbsSigLaneLaneEthRxAllFrames = _NbsSigLaneLaneEthRxAllFrames_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 71),
    _NbsSigLaneLaneEthRxAllFrames_Type()
)
nbsSigLaneLaneEthRxAllFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneEthRxAllFrames.setStatus("current")
_NbsSigLaneTraps_ObjectIdentity = ObjectIdentity
nbsSigLaneTraps = _NbsSigLaneTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 100)
)
if mibBuilder.loadTexts:
    nbsSigLaneTraps.setStatus("current")
_NbsSigLaneTraps0_ObjectIdentity = ObjectIdentity
nbsSigLaneTraps0 = _NbsSigLaneTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 100, 0)
)
if mibBuilder.loadTexts:
    nbsSigLaneTraps0.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-SIGLANE-MIB",
    **{"nbsSigLaneMib": nbsSigLaneMib,
       "nbsSigLanePortGrp": nbsSigLanePortGrp,
       "nbsSigLanePortTable": nbsSigLanePortTable,
       "nbsSigLanePortEntry": nbsSigLanePortEntry,
       "nbsSigLanePortIfIndex": nbsSigLanePortIfIndex,
       "nbsSigLanePortFacility": nbsSigLanePortFacility,
       "nbsSigLanePortLanes": nbsSigLanePortLanes,
       "nbsSigLaneLaneGrp": nbsSigLaneLaneGrp,
       "nbsSigLaneLaneTable": nbsSigLaneLaneTable,
       "nbsSigLaneLaneEntry": nbsSigLaneLaneEntry,
       "nbsSigLaneLaneIfIndex": nbsSigLaneLaneIfIndex,
       "nbsSigLaneLaneIndex": nbsSigLaneLaneIndex,
       "nbsSigLaneLaneFrequency": nbsSigLaneLaneFrequency,
       "nbsSigLaneLaneWavelengthX": nbsSigLaneLaneWavelengthX,
       "nbsSigLaneLaneChannelBand": nbsSigLaneLaneChannelBand,
       "nbsSigLaneLaneChannelNumber": nbsSigLaneLaneChannelNumber,
       "nbsSigLaneLaneTxDisable": nbsSigLaneLaneTxDisable,
       "nbsSigLaneLaneFaultsCaps": nbsSigLaneLaneFaultsCaps,
       "nbsSigLaneLaneFaultsOper": nbsSigLaneLaneFaultsOper,
       "nbsSigLaneLaneTxPowerLevel": nbsSigLaneLaneTxPowerLevel,
       "nbsSigLaneLaneTxPower": nbsSigLaneLaneTxPower,
       "nbsSigLaneLaneTxPowerAdmin": nbsSigLaneLaneTxPowerAdmin,
       "nbsSigLaneLaneRxPowerLevel": nbsSigLaneLaneRxPowerLevel,
       "nbsSigLaneLaneRxPower": nbsSigLaneLaneRxPower,
       "nbsSigLaneLaneBiasAmpsLevel": nbsSigLaneLaneBiasAmpsLevel,
       "nbsSigLaneLaneBiasAmps": nbsSigLaneLaneBiasAmps,
       "nbsSigLaneLaneLaserTempLevel": nbsSigLaneLaneLaserTempLevel,
       "nbsSigLaneLaneLaserTemp": nbsSigLaneLaneLaserTemp,
       "nbsSigLaneLaneEthTxAllOctets": nbsSigLaneLaneEthTxAllOctets,
       "nbsSigLaneLaneEthTxAllFrames": nbsSigLaneLaneEthTxAllFrames,
       "nbsSigLaneLaneEthRxAllOctets": nbsSigLaneLaneEthRxAllOctets,
       "nbsSigLaneLaneEthRxAllFrames": nbsSigLaneLaneEthRxAllFrames,
       "nbsSigLaneTraps": nbsSigLaneTraps,
       "nbsSigLaneTraps0": nbsSigLaneTraps0}
)
