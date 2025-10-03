# SNMP MIB module (NBS-SIGCOND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mrv\NBS-SIGCOND-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:32 2025
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

(InterfaceIndex,
 ifAlias) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias")

(NbsTcMHz,
 NbsTcMilliDb,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcMHz",
    "NbsTcMilliDb",
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

nbsSigCondMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsSigCondVoaPortGrp_ObjectIdentity = ObjectIdentity
nbsSigCondVoaPortGrp = _NbsSigCondVoaPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 1)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaPortGrp.setStatus("current")
_NbsSigCondVoaPortTableSize_Type = Unsigned32
_NbsSigCondVoaPortTableSize_Object = MibScalar
nbsSigCondVoaPortTableSize = _NbsSigCondVoaPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 1),
    _NbsSigCondVoaPortTableSize_Type()
)
nbsSigCondVoaPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTableSize.setStatus("current")
_NbsSigCondVoaPortTable_Object = MibTable
nbsSigCondVoaPortTable = _NbsSigCondVoaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTable.setStatus("current")
_NbsSigCondVoaPortEntry_Object = MibTableRow
nbsSigCondVoaPortEntry = _NbsSigCondVoaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1)
)
nbsSigCondVoaPortEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondVoaPortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondVoaPortEntry.setStatus("current")
_NbsSigCondVoaPortIfIndex_Type = InterfaceIndex
_NbsSigCondVoaPortIfIndex_Object = MibTableColumn
nbsSigCondVoaPortIfIndex = _NbsSigCondVoaPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 1),
    _NbsSigCondVoaPortIfIndex_Type()
)
nbsSigCondVoaPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortIfIndex.setStatus("current")


class _NbsSigCondVoaPortRxAttenuAdmin_Type(Integer32):
    """Custom type nbsSigCondVoaPortRxAttenuAdmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVoaPortRxAttenuAdmin_Type.__name__ = "Integer32"
_NbsSigCondVoaPortRxAttenuAdmin_Object = MibTableColumn
nbsSigCondVoaPortRxAttenuAdmin = _NbsSigCondVoaPortRxAttenuAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 2),
    _NbsSigCondVoaPortRxAttenuAdmin_Type()
)
nbsSigCondVoaPortRxAttenuAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortRxAttenuAdmin.setStatus("current")


class _NbsSigCondVoaPortRxAttenuOper_Type(Integer32):
    """Custom type nbsSigCondVoaPortRxAttenuOper based on Integer32"""
    defaultValue = 0


_NbsSigCondVoaPortRxAttenuOper_Type.__name__ = "Integer32"
_NbsSigCondVoaPortRxAttenuOper_Object = MibTableColumn
nbsSigCondVoaPortRxAttenuOper = _NbsSigCondVoaPortRxAttenuOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 3),
    _NbsSigCondVoaPortRxAttenuOper_Type()
)
nbsSigCondVoaPortRxAttenuOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortRxAttenuOper.setStatus("current")


class _NbsSigCondVoaPortTxAttenuAdmin_Type(Integer32):
    """Custom type nbsSigCondVoaPortTxAttenuAdmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVoaPortTxAttenuAdmin_Type.__name__ = "Integer32"
_NbsSigCondVoaPortTxAttenuAdmin_Object = MibTableColumn
nbsSigCondVoaPortTxAttenuAdmin = _NbsSigCondVoaPortTxAttenuAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 4),
    _NbsSigCondVoaPortTxAttenuAdmin_Type()
)
nbsSigCondVoaPortTxAttenuAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTxAttenuAdmin.setStatus("current")


class _NbsSigCondVoaPortTxAttenuOper_Type(Integer32):
    """Custom type nbsSigCondVoaPortTxAttenuOper based on Integer32"""
    defaultValue = 0


_NbsSigCondVoaPortTxAttenuOper_Type.__name__ = "Integer32"
_NbsSigCondVoaPortTxAttenuOper_Object = MibTableColumn
nbsSigCondVoaPortTxAttenuOper = _NbsSigCondVoaPortTxAttenuOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 1, 2, 1, 5),
    _NbsSigCondVoaPortTxAttenuOper_Type()
)
nbsSigCondVoaPortTxAttenuOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaPortTxAttenuOper.setStatus("current")
_NbsSigCondVoaChannelGrp_ObjectIdentity = ObjectIdentity
nbsSigCondVoaChannelGrp = _NbsSigCondVoaChannelGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelGrp.setStatus("current")
_NbsSigCondVoaChannelRangeTableSize_Type = Unsigned32
_NbsSigCondVoaChannelRangeTableSize_Object = MibScalar
nbsSigCondVoaChannelRangeTableSize = _NbsSigCondVoaChannelRangeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 1),
    _NbsSigCondVoaChannelRangeTableSize_Type()
)
nbsSigCondVoaChannelRangeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelRangeTableSize.setStatus("current")
_NbsSigCondVoaChannelRangeTable_Object = MibTable
nbsSigCondVoaChannelRangeTable = _NbsSigCondVoaChannelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelRangeTable.setStatus("current")
_NbsSigCondVoaChannelRangeEntry_Object = MibTableRow
nbsSigCondVoaChannelRangeEntry = _NbsSigCondVoaChannelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1)
)
nbsSigCondVoaChannelRangeEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondVoaChannelRangeIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelRangeEntry.setStatus("current")
_NbsSigCondVoaChannelRangeIfIndex_Type = InterfaceIndex
_NbsSigCondVoaChannelRangeIfIndex_Object = MibTableColumn
nbsSigCondVoaChannelRangeIfIndex = _NbsSigCondVoaChannelRangeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 1),
    _NbsSigCondVoaChannelRangeIfIndex_Type()
)
nbsSigCondVoaChannelRangeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelRangeIfIndex.setStatus("current")


class _NbsSigCondVoaChannelRangeMin_Type(NbsTcMilliDb):
    """Custom type nbsSigCondVoaChannelRangeMin based on NbsTcMilliDb"""
    defaultValue = 0


_NbsSigCondVoaChannelRangeMin_Type.__name__ = "NbsTcMilliDb"
_NbsSigCondVoaChannelRangeMin_Object = MibTableColumn
nbsSigCondVoaChannelRangeMin = _NbsSigCondVoaChannelRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 2),
    _NbsSigCondVoaChannelRangeMin_Type()
)
nbsSigCondVoaChannelRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelRangeMin.setStatus("current")


class _NbsSigCondVoaChannelRangeMax_Type(NbsTcMilliDb):
    """Custom type nbsSigCondVoaChannelRangeMax based on NbsTcMilliDb"""
    defaultValue = 0


_NbsSigCondVoaChannelRangeMax_Type.__name__ = "NbsTcMilliDb"
_NbsSigCondVoaChannelRangeMax_Object = MibTableColumn
nbsSigCondVoaChannelRangeMax = _NbsSigCondVoaChannelRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 3),
    _NbsSigCondVoaChannelRangeMax_Type()
)
nbsSigCondVoaChannelRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelRangeMax.setStatus("current")


class _NbsSigCondVoaChannelRangeIncr_Type(NbsTcMilliDb):
    """Custom type nbsSigCondVoaChannelRangeIncr based on NbsTcMilliDb"""
    defaultValue = 0


_NbsSigCondVoaChannelRangeIncr_Type.__name__ = "NbsTcMilliDb"
_NbsSigCondVoaChannelRangeIncr_Object = MibTableColumn
nbsSigCondVoaChannelRangeIncr = _NbsSigCondVoaChannelRangeIncr_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 2, 2, 1, 4),
    _NbsSigCondVoaChannelRangeIncr_Type()
)
nbsSigCondVoaChannelRangeIncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVoaChannelRangeIncr.setStatus("current")
_NbsSigCondRamanGrp_ObjectIdentity = ObjectIdentity
nbsSigCondRamanGrp = _NbsSigCondRamanGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 3)
)
if mibBuilder.loadTexts:
    nbsSigCondRamanGrp.setStatus("current")
_NbsSigCondRamanTableSize_Type = Unsigned32
_NbsSigCondRamanTableSize_Object = MibScalar
nbsSigCondRamanTableSize = _NbsSigCondRamanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 1),
    _NbsSigCondRamanTableSize_Type()
)
nbsSigCondRamanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRamanTableSize.setStatus("current")
_NbsSigCondRamanTable_Object = MibTable
nbsSigCondRamanTable = _NbsSigCondRamanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondRamanTable.setStatus("current")
_NbsSigCondRamanEntry_Object = MibTableRow
nbsSigCondRamanEntry = _NbsSigCondRamanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1)
)
nbsSigCondRamanEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondRamanIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondRamanEntry.setStatus("current")
_NbsSigCondRamanIfIndex_Type = InterfaceIndex
_NbsSigCondRamanIfIndex_Object = MibTableColumn
nbsSigCondRamanIfIndex = _NbsSigCondRamanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 1),
    _NbsSigCondRamanIfIndex_Type()
)
nbsSigCondRamanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondRamanIfIndex.setStatus("current")
_NbsSigCondRamanPumpPwrAdmin_Type = Integer32
_NbsSigCondRamanPumpPwrAdmin_Object = MibTableColumn
nbsSigCondRamanPumpPwrAdmin = _NbsSigCondRamanPumpPwrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 2),
    _NbsSigCondRamanPumpPwrAdmin_Type()
)
nbsSigCondRamanPumpPwrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondRamanPumpPwrAdmin.setStatus("current")
_NbsSigCondRamanPumpPwrOper_Type = Integer32
_NbsSigCondRamanPumpPwrOper_Object = MibTableColumn
nbsSigCondRamanPumpPwrOper = _NbsSigCondRamanPumpPwrOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 3, 2, 1, 3),
    _NbsSigCondRamanPumpPwrOper_Type()
)
nbsSigCondRamanPumpPwrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRamanPumpPwrOper.setStatus("current")
_NbsSigCondEqualizeGrp_ObjectIdentity = ObjectIdentity
nbsSigCondEqualizeGrp = _NbsSigCondEqualizeGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 20)
)
if mibBuilder.loadTexts:
    nbsSigCondEqualizeGrp.setStatus("current")
_NbsSigCondEqualizeTableSize_Type = Unsigned32
_NbsSigCondEqualizeTableSize_Object = MibScalar
nbsSigCondEqualizeTableSize = _NbsSigCondEqualizeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 1),
    _NbsSigCondEqualizeTableSize_Type()
)
nbsSigCondEqualizeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeTableSize.setStatus("current")
_NbsSigCondEqualizeTable_Object = MibTable
nbsSigCondEqualizeTable = _NbsSigCondEqualizeTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondEqualizeTable.setStatus("current")
_NbsSigCondEqualizeEntry_Object = MibTableRow
nbsSigCondEqualizeEntry = _NbsSigCondEqualizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1)
)
nbsSigCondEqualizeEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondEqualizeEntry.setStatus("current")
_NbsSigCondEqualizeIfIndex_Type = InterfaceIndex
_NbsSigCondEqualizeIfIndex_Object = MibTableColumn
nbsSigCondEqualizeIfIndex = _NbsSigCondEqualizeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 1),
    _NbsSigCondEqualizeIfIndex_Type()
)
nbsSigCondEqualizeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeIfIndex.setStatus("current")


class _NbsSigCondEqualizeState_Type(Integer32):
    """Custom type nbsSigCondEqualizeState based on Integer32"""
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
        *(("notSupported", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_NbsSigCondEqualizeState_Type.__name__ = "Integer32"
_NbsSigCondEqualizeState_Object = MibTableColumn
nbsSigCondEqualizeState = _NbsSigCondEqualizeState_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 10),
    _NbsSigCondEqualizeState_Type()
)
nbsSigCondEqualizeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeState.setStatus("current")
_NbsSigCondEqualizeLimitMin_Type = NbsTcMilliDb
_NbsSigCondEqualizeLimitMin_Object = MibTableColumn
nbsSigCondEqualizeLimitMin = _NbsSigCondEqualizeLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 11),
    _NbsSigCondEqualizeLimitMin_Type()
)
nbsSigCondEqualizeLimitMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeLimitMin.setStatus("current")
_NbsSigCondEqualizeLimitMax_Type = NbsTcMilliDb
_NbsSigCondEqualizeLimitMax_Object = MibTableColumn
nbsSigCondEqualizeLimitMax = _NbsSigCondEqualizeLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 12),
    _NbsSigCondEqualizeLimitMax_Type()
)
nbsSigCondEqualizeLimitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeLimitMax.setStatus("current")


class _NbsSigCondEqualizeDesiredMin_Type(NbsTcMilliDb):
    """Custom type nbsSigCondEqualizeDesiredMin based on NbsTcMilliDb"""
    defaultValue = -50000


_NbsSigCondEqualizeDesiredMin_Type.__name__ = "NbsTcMilliDb"
_NbsSigCondEqualizeDesiredMin_Object = MibTableColumn
nbsSigCondEqualizeDesiredMin = _NbsSigCondEqualizeDesiredMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 21),
    _NbsSigCondEqualizeDesiredMin_Type()
)
nbsSigCondEqualizeDesiredMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeDesiredMin.setStatus("current")


class _NbsSigCondEqualizeDesiredMax_Type(NbsTcMilliDb):
    """Custom type nbsSigCondEqualizeDesiredMax based on NbsTcMilliDb"""
    defaultValue = 0


_NbsSigCondEqualizeDesiredMax_Type.__name__ = "NbsTcMilliDb"
_NbsSigCondEqualizeDesiredMax_Object = MibTableColumn
nbsSigCondEqualizeDesiredMax = _NbsSigCondEqualizeDesiredMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 22),
    _NbsSigCondEqualizeDesiredMax_Type()
)
nbsSigCondEqualizeDesiredMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeDesiredMax.setStatus("current")


class _NbsSigCondEqualizeDesiredVal_Type(NbsTcMilliDb):
    """Custom type nbsSigCondEqualizeDesiredVal based on NbsTcMilliDb"""
    defaultValue = -25000


_NbsSigCondEqualizeDesiredVal_Type.__name__ = "NbsTcMilliDb"
_NbsSigCondEqualizeDesiredVal_Object = MibTableColumn
nbsSigCondEqualizeDesiredVal = _NbsSigCondEqualizeDesiredVal_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 20, 2, 1, 23),
    _NbsSigCondEqualizeDesiredVal_Type()
)
nbsSigCondEqualizeDesiredVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondEqualizeDesiredVal.setStatus("current")
_NbsSigCondRedundGrp_ObjectIdentity = ObjectIdentity
nbsSigCondRedundGrp = _NbsSigCondRedundGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 30)
)
if mibBuilder.loadTexts:
    nbsSigCondRedundGrp.setStatus("current")
_NbsSigCondRedundTableSize_Type = Unsigned32
_NbsSigCondRedundTableSize_Object = MibScalar
nbsSigCondRedundTableSize = _NbsSigCondRedundTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 1),
    _NbsSigCondRedundTableSize_Type()
)
nbsSigCondRedundTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRedundTableSize.setStatus("current")
_NbsSigCondRedundTable_Object = MibTable
nbsSigCondRedundTable = _NbsSigCondRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondRedundTable.setStatus("current")
_NbsSigCondRedundEntry_Object = MibTableRow
nbsSigCondRedundEntry = _NbsSigCondRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1)
)
nbsSigCondRedundEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondRedundIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondRedundEntry.setStatus("current")
_NbsSigCondRedundIfIndex_Type = InterfaceIndex
_NbsSigCondRedundIfIndex_Object = MibTableColumn
nbsSigCondRedundIfIndex = _NbsSigCondRedundIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 1),
    _NbsSigCondRedundIfIndex_Type()
)
nbsSigCondRedundIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRedundIfIndex.setStatus("current")
_NbsSigCondRedundLimitMin_Type = NbsTcMilliDb
_NbsSigCondRedundLimitMin_Object = MibTableColumn
nbsSigCondRedundLimitMin = _NbsSigCondRedundLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 5),
    _NbsSigCondRedundLimitMin_Type()
)
nbsSigCondRedundLimitMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRedundLimitMin.setStatus("current")
_NbsSigCondRedundLimitMax_Type = NbsTcMilliDb
_NbsSigCondRedundLimitMax_Object = MibTableColumn
nbsSigCondRedundLimitMax = _NbsSigCondRedundLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 8),
    _NbsSigCondRedundLimitMax_Type()
)
nbsSigCondRedundLimitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondRedundLimitMax.setStatus("current")
_NbsSigCondRedundDesiredMin_Type = NbsTcMilliDb
_NbsSigCondRedundDesiredMin_Object = MibTableColumn
nbsSigCondRedundDesiredMin = _NbsSigCondRedundDesiredMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 10),
    _NbsSigCondRedundDesiredMin_Type()
)
nbsSigCondRedundDesiredMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondRedundDesiredMin.setStatus("current")
_NbsSigCondRedundDesiredMax_Type = NbsTcMilliDb
_NbsSigCondRedundDesiredMax_Object = MibTableColumn
nbsSigCondRedundDesiredMax = _NbsSigCondRedundDesiredMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 30, 2, 1, 15),
    _NbsSigCondRedundDesiredMax_Type()
)
nbsSigCondRedundDesiredMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondRedundDesiredMax.setStatus("current")
_NbsSigCondPortGrp_ObjectIdentity = ObjectIdentity
nbsSigCondPortGrp = _NbsSigCondPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 40)
)
if mibBuilder.loadTexts:
    nbsSigCondPortGrp.setStatus("current")
_NbsSigCondPortTableSize_Type = Unsigned32
_NbsSigCondPortTableSize_Object = MibScalar
nbsSigCondPortTableSize = _NbsSigCondPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 1),
    _NbsSigCondPortTableSize_Type()
)
nbsSigCondPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortTableSize.setStatus("current")
_NbsSigCondPortTable_Object = MibTable
nbsSigCondPortTable = _NbsSigCondPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondPortTable.setStatus("current")
_NbsSigCondPortEntry_Object = MibTableRow
nbsSigCondPortEntry = _NbsSigCondPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1)
)
nbsSigCondPortEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondPortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondPortEntry.setStatus("current")
_NbsSigCondPortIfIndex_Type = InterfaceIndex
_NbsSigCondPortIfIndex_Object = MibTableColumn
nbsSigCondPortIfIndex = _NbsSigCondPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 1),
    _NbsSigCondPortIfIndex_Type()
)
nbsSigCondPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondPortIfIndex.setStatus("current")
_NbsSigCondPortRxPower_Type = Integer32
_NbsSigCondPortRxPower_Object = MibTableColumn
nbsSigCondPortRxPower = _NbsSigCondPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 2),
    _NbsSigCondPortRxPower_Type()
)
nbsSigCondPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortRxPower.setStatus("current")
_NbsSigCondPortTxPower_Type = Integer32
_NbsSigCondPortTxPower_Object = MibTableColumn
nbsSigCondPortTxPower = _NbsSigCondPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 3),
    _NbsSigCondPortTxPower_Type()
)
nbsSigCondPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortTxPower.setStatus("current")
_NbsSigCondPortReflection_Type = Integer32
_NbsSigCondPortReflection_Object = MibTableColumn
nbsSigCondPortReflection = _NbsSigCondPortReflection_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 4),
    _NbsSigCondPortReflection_Type()
)
nbsSigCondPortReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortReflection.setStatus("current")
_NbsSigCondPortRxPowerMin_Type = Integer32
_NbsSigCondPortRxPowerMin_Object = MibTableColumn
nbsSigCondPortRxPowerMin = _NbsSigCondPortRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 5),
    _NbsSigCondPortRxPowerMin_Type()
)
nbsSigCondPortRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortRxPowerMin.setStatus("current")
_NbsSigCondPortRxPowerMax_Type = Integer32
_NbsSigCondPortRxPowerMax_Object = MibTableColumn
nbsSigCondPortRxPowerMax = _NbsSigCondPortRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 6),
    _NbsSigCondPortRxPowerMax_Type()
)
nbsSigCondPortRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortRxPowerMax.setStatus("current")
_NbsSigCondPortNoiseFigure_Type = Integer32
_NbsSigCondPortNoiseFigure_Object = MibTableColumn
nbsSigCondPortNoiseFigure = _NbsSigCondPortNoiseFigure_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 40, 2, 1, 7),
    _NbsSigCondPortNoiseFigure_Type()
)
nbsSigCondPortNoiseFigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondPortNoiseFigure.setStatus("current")
_NbsSigCondChannelGrp_ObjectIdentity = ObjectIdentity
nbsSigCondChannelGrp = _NbsSigCondChannelGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 50)
)
if mibBuilder.loadTexts:
    nbsSigCondChannelGrp.setStatus("current")
_NbsSigCondChannelTableSize_Type = Unsigned32
_NbsSigCondChannelTableSize_Object = MibScalar
nbsSigCondChannelTableSize = _NbsSigCondChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 1),
    _NbsSigCondChannelTableSize_Type()
)
nbsSigCondChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondChannelTableSize.setStatus("current")
_NbsSigCondChannelTable_Object = MibTable
nbsSigCondChannelTable = _NbsSigCondChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondChannelTable.setStatus("current")
_NbsSigCondChannelEntry_Object = MibTableRow
nbsSigCondChannelEntry = _NbsSigCondChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1)
)
nbsSigCondChannelEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondChannelIfIndex"),
    (0, "NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"),
)
if mibBuilder.loadTexts:
    nbsSigCondChannelEntry.setStatus("current")
_NbsSigCondChannelIfIndex_Type = InterfaceIndex
_NbsSigCondChannelIfIndex_Object = MibTableColumn
nbsSigCondChannelIfIndex = _NbsSigCondChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 1),
    _NbsSigCondChannelIfIndex_Type()
)
nbsSigCondChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondChannelIfIndex.setStatus("current")
_NbsSigCondChannelCenterline_Type = NbsTcMHz
_NbsSigCondChannelCenterline_Object = MibTableColumn
nbsSigCondChannelCenterline = _NbsSigCondChannelCenterline_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 2),
    _NbsSigCondChannelCenterline_Type()
)
nbsSigCondChannelCenterline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondChannelCenterline.setStatus("current")
_NbsSigCondChannelRxPower_Type = NbsTcMilliDb
_NbsSigCondChannelRxPower_Object = MibTableColumn
nbsSigCondChannelRxPower = _NbsSigCondChannelRxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 11),
    _NbsSigCondChannelRxPower_Type()
)
nbsSigCondChannelRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondChannelRxPower.setStatus("current")
_NbsSigCondChannelTxPower_Type = NbsTcMilliDb
_NbsSigCondChannelTxPower_Object = MibTableColumn
nbsSigCondChannelTxPower = _NbsSigCondChannelTxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 12),
    _NbsSigCondChannelTxPower_Type()
)
nbsSigCondChannelTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondChannelTxPower.setStatus("current")
_NbsSigCondChannelTxAttenu_Type = NbsTcMilliDb
_NbsSigCondChannelTxAttenu_Object = MibTableColumn
nbsSigCondChannelTxAttenu = _NbsSigCondChannelTxAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 14),
    _NbsSigCondChannelTxAttenu_Type()
)
nbsSigCondChannelTxAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondChannelTxAttenu.setStatus("current")
_NbsSigCondChannelRxAttenu_Type = NbsTcMilliDb
_NbsSigCondChannelRxAttenu_Object = MibTableColumn
nbsSigCondChannelRxAttenu = _NbsSigCondChannelRxAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 50, 2, 1, 15),
    _NbsSigCondChannelRxAttenu_Type()
)
nbsSigCondChannelRxAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondChannelRxAttenu.setStatus("current")
_NbsSigCondVodPortGrp_ObjectIdentity = ObjectIdentity
nbsSigCondVodPortGrp = _NbsSigCondVodPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 60)
)
if mibBuilder.loadTexts:
    nbsSigCondVodPortGrp.setStatus("current")
_NbsSigCondVodPortTableSize_Type = Unsigned32
_NbsSigCondVodPortTableSize_Object = MibScalar
nbsSigCondVodPortTableSize = _NbsSigCondVodPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 1),
    _NbsSigCondVodPortTableSize_Type()
)
nbsSigCondVodPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortTableSize.setStatus("current")
_NbsSigCondVodPortTable_Object = MibTable
nbsSigCondVodPortTable = _NbsSigCondVodPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2)
)
if mibBuilder.loadTexts:
    nbsSigCondVodPortTable.setStatus("current")
_NbsSigCondVodPortEntry_Object = MibTableRow
nbsSigCondVodPortEntry = _NbsSigCondVodPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1)
)
nbsSigCondVodPortEntry.setIndexNames(
    (0, "NBS-SIGCOND-MIB", "nbsSigCondVodPortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigCondVodPortEntry.setStatus("current")
_NbsSigCondVodPortIfIndex_Type = InterfaceIndex
_NbsSigCondVodPortIfIndex_Object = MibTableColumn
nbsSigCondVodPortIfIndex = _NbsSigCondVodPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 1),
    _NbsSigCondVodPortIfIndex_Type()
)
nbsSigCondVodPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSigCondVodPortIfIndex.setStatus("current")


class _NbsSigCondVodPortDispersionMin_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionMin_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionMin_Object = MibTableColumn
nbsSigCondVodPortDispersionMin = _NbsSigCondVodPortDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 2),
    _NbsSigCondVodPortDispersionMin_Type()
)
nbsSigCondVodPortDispersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionMin.setStatus("current")


class _NbsSigCondVodPortDispersionMax_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionMax_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionMax_Object = MibTableColumn
nbsSigCondVodPortDispersionMax = _NbsSigCondVodPortDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 3),
    _NbsSigCondVodPortDispersionMax_Type()
)
nbsSigCondVodPortDispersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionMax.setStatus("current")


class _NbsSigCondVodPortDispersionAdmin_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionAdmin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionAdmin_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionAdmin_Object = MibTableColumn
nbsSigCondVodPortDispersionAdmin = _NbsSigCondVodPortDispersionAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 4),
    _NbsSigCondVodPortDispersionAdmin_Type()
)
nbsSigCondVodPortDispersionAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionAdmin.setStatus("current")


class _NbsSigCondVodPortDispersionOper_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionOper based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionOper_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionOper_Object = MibTableColumn
nbsSigCondVodPortDispersionOper = _NbsSigCondVodPortDispersionOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 5),
    _NbsSigCondVodPortDispersionOper_Type()
)
nbsSigCondVodPortDispersionOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionOper.setStatus("current")
_NbsSigCondVodPortDispersionGridOffsetCenter_Type = Integer32
_NbsSigCondVodPortDispersionGridOffsetCenter_Object = MibTableColumn
nbsSigCondVodPortDispersionGridOffsetCenter = _NbsSigCondVodPortDispersionGridOffsetCenter_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 10),
    _NbsSigCondVodPortDispersionGridOffsetCenter_Type()
)
nbsSigCondVodPortDispersionGridOffsetCenter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionGridOffsetCenter.setStatus("current")


class _NbsSigCondVodPortDispersionGridOffsetMin_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionGridOffsetMin based on Integer32"""
    defaultValue = -100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionGridOffsetMin_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionGridOffsetMin_Object = MibTableColumn
nbsSigCondVodPortDispersionGridOffsetMin = _NbsSigCondVodPortDispersionGridOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 11),
    _NbsSigCondVodPortDispersionGridOffsetMin_Type()
)
nbsSigCondVodPortDispersionGridOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionGridOffsetMin.setStatus("current")


class _NbsSigCondVodPortDispersionGridOffsetMax_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionGridOffsetMax based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionGridOffsetMax_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionGridOffsetMax_Object = MibTableColumn
nbsSigCondVodPortDispersionGridOffsetMax = _NbsSigCondVodPortDispersionGridOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 12),
    _NbsSigCondVodPortDispersionGridOffsetMax_Type()
)
nbsSigCondVodPortDispersionGridOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionGridOffsetMax.setStatus("current")


class _NbsSigCondVodPortDispersionGridOffsetStep_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionGridOffsetStep based on Integer32"""
    defaultValue = 1


_NbsSigCondVodPortDispersionGridOffsetStep_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionGridOffsetStep_Object = MibTableColumn
nbsSigCondVodPortDispersionGridOffsetStep = _NbsSigCondVodPortDispersionGridOffsetStep_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 13),
    _NbsSigCondVodPortDispersionGridOffsetStep_Type()
)
nbsSigCondVodPortDispersionGridOffsetStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionGridOffsetStep.setStatus("current")


class _NbsSigCondVodPortDispersionGridOffsetExponent_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionGridOffsetExponent based on Integer32"""
    defaultValue = 9


_NbsSigCondVodPortDispersionGridOffsetExponent_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionGridOffsetExponent_Object = MibTableColumn
nbsSigCondVodPortDispersionGridOffsetExponent = _NbsSigCondVodPortDispersionGridOffsetExponent_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 14),
    _NbsSigCondVodPortDispersionGridOffsetExponent_Type()
)
nbsSigCondVodPortDispersionGridOffsetExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionGridOffsetExponent.setStatus("current")


class _NbsSigCondVodPortDispersionGridOffsetAdmin_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionGridOffsetAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionGridOffsetAdmin_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionGridOffsetAdmin_Object = MibTableColumn
nbsSigCondVodPortDispersionGridOffsetAdmin = _NbsSigCondVodPortDispersionGridOffsetAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 15),
    _NbsSigCondVodPortDispersionGridOffsetAdmin_Type()
)
nbsSigCondVodPortDispersionGridOffsetAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionGridOffsetAdmin.setStatus("current")


class _NbsSigCondVodPortDispersionGridOffsetOper_Type(Integer32):
    """Custom type nbsSigCondVodPortDispersionGridOffsetOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsSigCondVodPortDispersionGridOffsetOper_Type.__name__ = "Integer32"
_NbsSigCondVodPortDispersionGridOffsetOper_Object = MibTableColumn
nbsSigCondVodPortDispersionGridOffsetOper = _NbsSigCondVodPortDispersionGridOffsetOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 227, 60, 2, 1, 16),
    _NbsSigCondVodPortDispersionGridOffsetOper_Type()
)
nbsSigCondVodPortDispersionGridOffsetOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigCondVodPortDispersionGridOffsetOper.setStatus("current")
_NbsSigCondTraps_ObjectIdentity = ObjectIdentity
nbsSigCondTraps = _NbsSigCondTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 200)
)
if mibBuilder.loadTexts:
    nbsSigCondTraps.setStatus("current")
_NbsSigCondEvent_ObjectIdentity = ObjectIdentity
nbsSigCondEvent = _NbsSigCondEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 227, 200, 0)
)
if mibBuilder.loadTexts:
    nbsSigCondEvent.setStatus("current")

# Managed Objects groups


# Notification objects

nbsSigCondEventEqualizeOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 227, 200, 0, 20)
)
nbsSigCondEventEqualizeOk.setObjects(
      *(("NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"),
        ("NBS-SIGCOND-MIB", "nbsSigCondChannelTxPower"),
        ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMin"),
        ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMax"))
)
if mibBuilder.loadTexts:
    nbsSigCondEventEqualizeOk.setStatus(
        "current"
    )

nbsSigCondEventEqualizeTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 227, 200, 0, 21)
)
nbsSigCondEventEqualizeTooLow.setObjects(
      *(("NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"),
        ("NBS-SIGCOND-MIB", "nbsSigCondChannelTxPower"),
        ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMin"))
)
if mibBuilder.loadTexts:
    nbsSigCondEventEqualizeTooLow.setStatus(
        "current"
    )

nbsSigCondEventEqualizeTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 227, 200, 0, 22)
)
nbsSigCondEventEqualizeTooHigh.setObjects(
      *(("NBS-SIGCOND-MIB", "nbsSigCondEqualizeIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-SIGCOND-MIB", "nbsSigCondChannelCenterline"),
        ("NBS-SIGCOND-MIB", "nbsSigCondChannelTxPower"),
        ("NBS-SIGCOND-MIB", "nbsSigCondEqualizeDesiredMax"))
)
if mibBuilder.loadTexts:
    nbsSigCondEventEqualizeTooHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-SIGCOND-MIB",
    **{"nbsSigCondMib": nbsSigCondMib,
       "nbsSigCondVoaPortGrp": nbsSigCondVoaPortGrp,
       "nbsSigCondVoaPortTableSize": nbsSigCondVoaPortTableSize,
       "nbsSigCondVoaPortTable": nbsSigCondVoaPortTable,
       "nbsSigCondVoaPortEntry": nbsSigCondVoaPortEntry,
       "nbsSigCondVoaPortIfIndex": nbsSigCondVoaPortIfIndex,
       "nbsSigCondVoaPortRxAttenuAdmin": nbsSigCondVoaPortRxAttenuAdmin,
       "nbsSigCondVoaPortRxAttenuOper": nbsSigCondVoaPortRxAttenuOper,
       "nbsSigCondVoaPortTxAttenuAdmin": nbsSigCondVoaPortTxAttenuAdmin,
       "nbsSigCondVoaPortTxAttenuOper": nbsSigCondVoaPortTxAttenuOper,
       "nbsSigCondVoaChannelGrp": nbsSigCondVoaChannelGrp,
       "nbsSigCondVoaChannelRangeTableSize": nbsSigCondVoaChannelRangeTableSize,
       "nbsSigCondVoaChannelRangeTable": nbsSigCondVoaChannelRangeTable,
       "nbsSigCondVoaChannelRangeEntry": nbsSigCondVoaChannelRangeEntry,
       "nbsSigCondVoaChannelRangeIfIndex": nbsSigCondVoaChannelRangeIfIndex,
       "nbsSigCondVoaChannelRangeMin": nbsSigCondVoaChannelRangeMin,
       "nbsSigCondVoaChannelRangeMax": nbsSigCondVoaChannelRangeMax,
       "nbsSigCondVoaChannelRangeIncr": nbsSigCondVoaChannelRangeIncr,
       "nbsSigCondRamanGrp": nbsSigCondRamanGrp,
       "nbsSigCondRamanTableSize": nbsSigCondRamanTableSize,
       "nbsSigCondRamanTable": nbsSigCondRamanTable,
       "nbsSigCondRamanEntry": nbsSigCondRamanEntry,
       "nbsSigCondRamanIfIndex": nbsSigCondRamanIfIndex,
       "nbsSigCondRamanPumpPwrAdmin": nbsSigCondRamanPumpPwrAdmin,
       "nbsSigCondRamanPumpPwrOper": nbsSigCondRamanPumpPwrOper,
       "nbsSigCondEqualizeGrp": nbsSigCondEqualizeGrp,
       "nbsSigCondEqualizeTableSize": nbsSigCondEqualizeTableSize,
       "nbsSigCondEqualizeTable": nbsSigCondEqualizeTable,
       "nbsSigCondEqualizeEntry": nbsSigCondEqualizeEntry,
       "nbsSigCondEqualizeIfIndex": nbsSigCondEqualizeIfIndex,
       "nbsSigCondEqualizeState": nbsSigCondEqualizeState,
       "nbsSigCondEqualizeLimitMin": nbsSigCondEqualizeLimitMin,
       "nbsSigCondEqualizeLimitMax": nbsSigCondEqualizeLimitMax,
       "nbsSigCondEqualizeDesiredMin": nbsSigCondEqualizeDesiredMin,
       "nbsSigCondEqualizeDesiredMax": nbsSigCondEqualizeDesiredMax,
       "nbsSigCondEqualizeDesiredVal": nbsSigCondEqualizeDesiredVal,
       "nbsSigCondRedundGrp": nbsSigCondRedundGrp,
       "nbsSigCondRedundTableSize": nbsSigCondRedundTableSize,
       "nbsSigCondRedundTable": nbsSigCondRedundTable,
       "nbsSigCondRedundEntry": nbsSigCondRedundEntry,
       "nbsSigCondRedundIfIndex": nbsSigCondRedundIfIndex,
       "nbsSigCondRedundLimitMin": nbsSigCondRedundLimitMin,
       "nbsSigCondRedundLimitMax": nbsSigCondRedundLimitMax,
       "nbsSigCondRedundDesiredMin": nbsSigCondRedundDesiredMin,
       "nbsSigCondRedundDesiredMax": nbsSigCondRedundDesiredMax,
       "nbsSigCondPortGrp": nbsSigCondPortGrp,
       "nbsSigCondPortTableSize": nbsSigCondPortTableSize,
       "nbsSigCondPortTable": nbsSigCondPortTable,
       "nbsSigCondPortEntry": nbsSigCondPortEntry,
       "nbsSigCondPortIfIndex": nbsSigCondPortIfIndex,
       "nbsSigCondPortRxPower": nbsSigCondPortRxPower,
       "nbsSigCondPortTxPower": nbsSigCondPortTxPower,
       "nbsSigCondPortReflection": nbsSigCondPortReflection,
       "nbsSigCondPortRxPowerMin": nbsSigCondPortRxPowerMin,
       "nbsSigCondPortRxPowerMax": nbsSigCondPortRxPowerMax,
       "nbsSigCondPortNoiseFigure": nbsSigCondPortNoiseFigure,
       "nbsSigCondChannelGrp": nbsSigCondChannelGrp,
       "nbsSigCondChannelTableSize": nbsSigCondChannelTableSize,
       "nbsSigCondChannelTable": nbsSigCondChannelTable,
       "nbsSigCondChannelEntry": nbsSigCondChannelEntry,
       "nbsSigCondChannelIfIndex": nbsSigCondChannelIfIndex,
       "nbsSigCondChannelCenterline": nbsSigCondChannelCenterline,
       "nbsSigCondChannelRxPower": nbsSigCondChannelRxPower,
       "nbsSigCondChannelTxPower": nbsSigCondChannelTxPower,
       "nbsSigCondChannelTxAttenu": nbsSigCondChannelTxAttenu,
       "nbsSigCondChannelRxAttenu": nbsSigCondChannelRxAttenu,
       "nbsSigCondVodPortGrp": nbsSigCondVodPortGrp,
       "nbsSigCondVodPortTableSize": nbsSigCondVodPortTableSize,
       "nbsSigCondVodPortTable": nbsSigCondVodPortTable,
       "nbsSigCondVodPortEntry": nbsSigCondVodPortEntry,
       "nbsSigCondVodPortIfIndex": nbsSigCondVodPortIfIndex,
       "nbsSigCondVodPortDispersionMin": nbsSigCondVodPortDispersionMin,
       "nbsSigCondVodPortDispersionMax": nbsSigCondVodPortDispersionMax,
       "nbsSigCondVodPortDispersionAdmin": nbsSigCondVodPortDispersionAdmin,
       "nbsSigCondVodPortDispersionOper": nbsSigCondVodPortDispersionOper,
       "nbsSigCondVodPortDispersionGridOffsetCenter": nbsSigCondVodPortDispersionGridOffsetCenter,
       "nbsSigCondVodPortDispersionGridOffsetMin": nbsSigCondVodPortDispersionGridOffsetMin,
       "nbsSigCondVodPortDispersionGridOffsetMax": nbsSigCondVodPortDispersionGridOffsetMax,
       "nbsSigCondVodPortDispersionGridOffsetStep": nbsSigCondVodPortDispersionGridOffsetStep,
       "nbsSigCondVodPortDispersionGridOffsetExponent": nbsSigCondVodPortDispersionGridOffsetExponent,
       "nbsSigCondVodPortDispersionGridOffsetAdmin": nbsSigCondVodPortDispersionGridOffsetAdmin,
       "nbsSigCondVodPortDispersionGridOffsetOper": nbsSigCondVodPortDispersionGridOffsetOper,
       "nbsSigCondTraps": nbsSigCondTraps,
       "nbsSigCondEvent": nbsSigCondEvent,
       "nbsSigCondEventEqualizeOk": nbsSigCondEventEqualizeOk,
       "nbsSigCondEventEqualizeTooLow": nbsSigCondEventEqualizeTooLow,
       "nbsSigCondEventEqualizeTooHigh": nbsSigCondEventEqualizeTooHigh}
)
