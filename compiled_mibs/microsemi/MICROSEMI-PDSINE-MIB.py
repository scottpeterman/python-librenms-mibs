# SNMP MIB module (MICROSEMI-PDSINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsemi\MICROSEMI-PDSINE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:32 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

polPowerOverLan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7428)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1)
)
_Description_ObjectIdentity = ObjectIdentity
description = _Description_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1)
)
_SysObjectID_ObjectIdentity = ObjectIdentity
sysObjectID = _SysObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1)
)
_MidspanUnknown_ObjectIdentity = ObjectIdentity
midspanUnknown = _MidspanUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 1)
)
_Midspan6portAC_ObjectIdentity = ObjectIdentity
midspan6portAC = _Midspan6portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 2)
)
_Midspan6portACDC_ObjectIdentity = ObjectIdentity
midspan6portACDC = _Midspan6portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 3)
)
_Midspan12portAC_ObjectIdentity = ObjectIdentity
midspan12portAC = _Midspan12portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 4)
)
_Midspan12portACDC_ObjectIdentity = ObjectIdentity
midspan12portACDC = _Midspan12portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 5)
)
_Midspan24portAC_ObjectIdentity = ObjectIdentity
midspan24portAC = _Midspan24portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 6)
)
_Midspan24portACDC_ObjectIdentity = ObjectIdentity
midspan24portACDC = _Midspan24portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 7)
)
_Midspan48portAC_ObjectIdentity = ObjectIdentity
midspan48portAC = _Midspan48portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 8)
)
_Midspan48portACDC_ObjectIdentity = ObjectIdentity
midspan48portACDC = _Midspan48portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 9)
)
_Midspan6portHPAC_ObjectIdentity = ObjectIdentity
midspan6portHPAC = _Midspan6portHPAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 10)
)
_Midspan6portHPACDC_ObjectIdentity = ObjectIdentity
midspan6portHPACDC = _Midspan6portHPACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 11)
)
_Midspan12portHPAC_ObjectIdentity = ObjectIdentity
midspan12portHPAC = _Midspan12portHPAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 12)
)
_Midspan12portHPACDC_ObjectIdentity = ObjectIdentity
midspan12portHPACDC = _Midspan12portHPACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 13)
)
_MidspanGigabit6portAC_ObjectIdentity = ObjectIdentity
midspanGigabit6portAC = _MidspanGigabit6portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 14)
)
_MidspanGigabit12portAC_ObjectIdentity = ObjectIdentity
midspanGigabit12portAC = _MidspanGigabit12portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 15)
)
_MidspanGigabit24portAC_ObjectIdentity = ObjectIdentity
midspanGigabit24portAC = _MidspanGigabit24portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 16)
)
_MidspanHiPoEGigabit6portAC_ObjectIdentity = ObjectIdentity
midspanHiPoEGigabit6portAC = _MidspanHiPoEGigabit6portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 17)
)
_MidspanHiPoEGigabit12portAC_ObjectIdentity = ObjectIdentity
midspanHiPoEGigabit12portAC = _MidspanHiPoEGigabit12portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 18)
)
_MidspanHiPoEGigabit24portAC_ObjectIdentity = ObjectIdentity
midspanHiPoEGigabit24portAC = _MidspanHiPoEGigabit24portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 19)
)
_MidspanHiPoEATGigabit6portAC_ObjectIdentity = ObjectIdentity
midspanHiPoEATGigabit6portAC = _MidspanHiPoEATGigabit6portAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 20)
)
_MidspanHiPoEATGigabit12portACDC_ObjectIdentity = ObjectIdentity
midspanHiPoEATGigabit12portACDC = _MidspanHiPoEATGigabit12portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 21)
)
_MidspanHiPoEATGigabit24portACDC_ObjectIdentity = ObjectIdentity
midspanHiPoEATGigabit24portACDC = _MidspanHiPoEATGigabit24portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 22)
)
_Midspan4PairATGigabit6portACDC_ObjectIdentity = ObjectIdentity
midspan4PairATGigabit6portACDC = _Midspan4PairATGigabit6portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 23)
)
_Midspan4PairATGigabit12portACDC_ObjectIdentity = ObjectIdentity
midspan4PairATGigabit12portACDC = _Midspan4PairATGigabit12portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 24)
)
_MidspanHiPoEATGigabit6portDC_ObjectIdentity = ObjectIdentity
midspanHiPoEATGigabit6portDC = _MidspanHiPoEATGigabit6portDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 25)
)
_MidspanHiPoEATGigabit12portDC_ObjectIdentity = ObjectIdentity
midspanHiPoEATGigabit12portDC = _MidspanHiPoEATGigabit12portDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 26)
)
_MidspanHiPoEATGigabit24portDC_ObjectIdentity = ObjectIdentity
midspanHiPoEATGigabit24portDC = _MidspanHiPoEATGigabit24portDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 27)
)
_Midspan4PairATGigabit24portACDC_ObjectIdentity = ObjectIdentity
midspan4PairATGigabit24portACDC = _Midspan4PairATGigabit24portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 28)
)
_MidspanEEPoEGigabit24portACDC_ObjectIdentity = ObjectIdentity
midspanEEPoEGigabit24portACDC = _MidspanEEPoEGigabit24portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 29)
)
_MidspanPoHGigabit6portACDC_ObjectIdentity = ObjectIdentity
midspanPoHGigabit6portACDC = _MidspanPoHGigabit6portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 30)
)
_MidspanPoHGigabit12portACDC_ObjectIdentity = ObjectIdentity
midspanPoHGigabit12portACDC = _MidspanPoHGigabit12portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 31)
)
_MidspanPoHGigabit24portACDC_ObjectIdentity = ObjectIdentity
midspanPoHGigabit24portACDC = _MidspanPoHGigabit24portACDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 1, 1, 32)
)
_PseDevice_ObjectIdentity = ObjectIdentity
pseDevice = _PseDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2)
)
_PortObjects_ObjectIdentity = ObjectIdentity
portObjects = _PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1)
)
portEntry.setIndexNames(
    (0, "MICROSEMI-PDSINE-MIB", "portGroupIndex"),
    (0, "MICROSEMI-PDSINE-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortGroupIndex_Type(Integer32):
    """Custom type portGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortGroupIndex_Type.__name__ = "Integer32"
_PortGroupIndex_Object = MibTableColumn
portGroupIndex = _PortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 1),
    _PortGroupIndex_Type()
)
portGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portGroupIndex.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 2),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")
_PortConsumptionPower_Type = Gauge32
_PortConsumptionPower_Object = MibTableColumn
portConsumptionPower = _PortConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 3),
    _PortConsumptionPower_Type()
)
portConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    portConsumptionPower.setUnits("Watt")


class _PortMaxPower_Type(Integer32):
    """Custom type portMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PortMaxPower_Type.__name__ = "Integer32"
_PortMaxPower_Object = MibTableColumn
portMaxPower = _PortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 4),
    _PortMaxPower_Type()
)
portMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    portMaxPower.setUnits("Watt")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twopair", 1),
          ("fourpair", 2))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 1, 1, 1, 5),
    _PortType_Type()
)
portType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portType.setStatus("current")
_MainObjects_ObjectIdentity = ObjectIdentity
mainObjects = _MainObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2)
)
_MainPseTable_Object = MibTable
mainPseTable = _MainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mainPseTable.setStatus("current")
_MainPseEntry_Object = MibTableRow
mainPseEntry = _MainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1)
)
mainPseEntry.setIndexNames(
    (0, "MICROSEMI-PDSINE-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    mainPseEntry.setStatus("current")


class _MainGroupIndex_Type(Integer32):
    """Custom type mainGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MainGroupIndex_Type.__name__ = "Integer32"
_MainGroupIndex_Object = MibTableColumn
mainGroupIndex = _MainGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 1),
    _MainGroupIndex_Type()
)
mainGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainGroupIndex.setStatus("current")


class _MainVoltage_Type(Gauge32):
    """Custom type mainVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MainVoltage_Type.__name__ = "Gauge32"
_MainVoltage_Object = MibTableColumn
mainVoltage = _MainVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 2),
    _MainVoltage_Type()
)
mainVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainVoltage.setStatus("current")
if mibBuilder.loadTexts:
    mainVoltage.setUnits("Volt")


class _MainDetectionMethod_Type(Integer32):
    """Custom type mainDetectionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023afat", 1),
          ("ieee8023afatandlegacy", 2))
    )


_MainDetectionMethod_Type.__name__ = "Integer32"
_MainDetectionMethod_Object = MibTableColumn
mainDetectionMethod = _MainDetectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 3),
    _MainDetectionMethod_Type()
)
mainDetectionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainDetectionMethod.setStatus("current")


class _MainPowerUsageBudget_Type(Integer32):
    """Custom type mainPowerUsageBudget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_MainPowerUsageBudget_Type.__name__ = "Integer32"
_MainPowerUsageBudget_Object = MibTableColumn
mainPowerUsageBudget = _MainPowerUsageBudget_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 4),
    _MainPowerUsageBudget_Type()
)
mainPowerUsageBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainPowerUsageBudget.setStatus("current")
if mibBuilder.loadTexts:
    mainPowerUsageBudget.setUnits("%")


class _MainPSEMaxPower_Type(Gauge32):
    """Custom type mainPSEMaxPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MainPSEMaxPower_Type.__name__ = "Gauge32"
_MainPSEMaxPower_Object = MibTableColumn
mainPSEMaxPower = _MainPSEMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 5),
    _MainPSEMaxPower_Type()
)
mainPSEMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSEMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    mainPSEMaxPower.setUnits("Watts")


class _HighPowerLegacyPDSupport_Type(Integer32):
    """Custom type highPowerLegacyPDSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notsupported", 3))
    )


_HighPowerLegacyPDSupport_Type.__name__ = "Integer32"
_HighPowerLegacyPDSupport_Object = MibTableColumn
highPowerLegacyPDSupport = _HighPowerLegacyPDSupport_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 6),
    _HighPowerLegacyPDSupport_Type()
)
highPowerLegacyPDSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highPowerLegacyPDSupport.setStatus("current")


class _HighPowerExtendedPortPower_Type(Integer32):
    """Custom type highPowerExtendedPortPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notsupported", 3))
    )


_HighPowerExtendedPortPower_Type.__name__ = "Integer32"
_HighPowerExtendedPortPower_Object = MibTableColumn
highPowerExtendedPortPower = _HighPowerExtendedPortPower_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 7),
    _HighPowerExtendedPortPower_Type()
)
highPowerExtendedPortPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highPowerExtendedPortPower.setStatus("current")


class _PowerBackupStatus_Type(Integer32):
    """Custom type powerBackupStatus based on Integer32"""
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
        *(("standalone", 1),
          ("powerbackupbyrps", 2),
          ("powerbackupbymidspan", 3),
          ("incompatiblepowerbackupdevice", 4))
    )


_PowerBackupStatus_Type.__name__ = "Integer32"
_PowerBackupStatus_Object = MibTableColumn
powerBackupStatus = _PowerBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 8),
    _PowerBackupStatus_Type()
)
powerBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerBackupStatus.setStatus("current")


class _InternalPowerSourceStatus_Type(Integer32):
    """Custom type internalPowerSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2))
    )


_InternalPowerSourceStatus_Type.__name__ = "Integer32"
_InternalPowerSourceStatus_Object = MibTableColumn
internalPowerSourceStatus = _InternalPowerSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 9),
    _InternalPowerSourceStatus_Type()
)
internalPowerSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPowerSourceStatus.setStatus("current")


class _ExternalPowerSourceStatus_Type(Integer32):
    """Custom type externalPowerSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2),
          ("notsupported", 3))
    )


_ExternalPowerSourceStatus_Type.__name__ = "Integer32"
_ExternalPowerSourceStatus_Object = MibTableColumn
externalPowerSourceStatus = _ExternalPowerSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 10),
    _ExternalPowerSourceStatus_Type()
)
externalPowerSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPowerSourceStatus.setStatus("current")
_Temperature_Type = Integer32
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 11),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
if mibBuilder.loadTexts:
    temperature.setUnits("Degree")


class _Temperatureformat_Type(Integer32):
    """Custom type temperatureformat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("celcius", 1),
          ("fahrenheit", 2),
          ("notsupported", 3))
    )


_Temperatureformat_Type.__name__ = "Integer32"
_Temperatureformat_Object = MibTableColumn
temperatureformat = _Temperatureformat_Object(
    (1, 3, 6, 1, 4, 1, 7428, 1, 2, 2, 1, 1, 12),
    _Temperatureformat_Type()
)
temperatureformat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureformat.setStatus("current")
_PoeNotifications_ObjectIdentity = ObjectIdentity
poeNotifications = _PoeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7428, 1, 3)
)

# Managed Objects groups


# Notification objects

powerBackupStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7428, 1, 3, 1)
)
powerBackupStatusNotification.setObjects(
    ("MICROSEMI-PDSINE-MIB", "powerBackupStatus")
)
if mibBuilder.loadTexts:
    powerBackupStatusNotification.setStatus(
        "current"
    )

internalPowerSourceStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7428, 1, 3, 2)
)
internalPowerSourceStatusNotification.setObjects(
    ("MICROSEMI-PDSINE-MIB", "internalPowerSourceStatus")
)
if mibBuilder.loadTexts:
    internalPowerSourceStatusNotification.setStatus(
        "current"
    )

externalPowerSourceStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 7428, 1, 3, 3)
)
externalPowerSourceStatusNotification.setObjects(
    ("MICROSEMI-PDSINE-MIB", "externalPowerSourceStatus")
)
if mibBuilder.loadTexts:
    externalPowerSourceStatusNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICROSEMI-PDSINE-MIB",
    **{"polPowerOverLan": polPowerOverLan,
       "products": products,
       "description": description,
       "sysObjectID": sysObjectID,
       "midspanUnknown": midspanUnknown,
       "midspan6portAC": midspan6portAC,
       "midspan6portACDC": midspan6portACDC,
       "midspan12portAC": midspan12portAC,
       "midspan12portACDC": midspan12portACDC,
       "midspan24portAC": midspan24portAC,
       "midspan24portACDC": midspan24portACDC,
       "midspan48portAC": midspan48portAC,
       "midspan48portACDC": midspan48portACDC,
       "midspan6portHPAC": midspan6portHPAC,
       "midspan6portHPACDC": midspan6portHPACDC,
       "midspan12portHPAC": midspan12portHPAC,
       "midspan12portHPACDC": midspan12portHPACDC,
       "midspanGigabit6portAC": midspanGigabit6portAC,
       "midspanGigabit12portAC": midspanGigabit12portAC,
       "midspanGigabit24portAC": midspanGigabit24portAC,
       "midspanHiPoEGigabit6portAC": midspanHiPoEGigabit6portAC,
       "midspanHiPoEGigabit12portAC": midspanHiPoEGigabit12portAC,
       "midspanHiPoEGigabit24portAC": midspanHiPoEGigabit24portAC,
       "midspanHiPoEATGigabit6portAC": midspanHiPoEATGigabit6portAC,
       "midspanHiPoEATGigabit12portACDC": midspanHiPoEATGigabit12portACDC,
       "midspanHiPoEATGigabit24portACDC": midspanHiPoEATGigabit24portACDC,
       "midspan4PairATGigabit6portACDC": midspan4PairATGigabit6portACDC,
       "midspan4PairATGigabit12portACDC": midspan4PairATGigabit12portACDC,
       "midspanHiPoEATGigabit6portDC": midspanHiPoEATGigabit6portDC,
       "midspanHiPoEATGigabit12portDC": midspanHiPoEATGigabit12portDC,
       "midspanHiPoEATGigabit24portDC": midspanHiPoEATGigabit24portDC,
       "midspan4PairATGigabit24portACDC": midspan4PairATGigabit24portACDC,
       "midspanEEPoEGigabit24portACDC": midspanEEPoEGigabit24portACDC,
       "midspanPoHGigabit6portACDC": midspanPoHGigabit6portACDC,
       "midspanPoHGigabit12portACDC": midspanPoHGigabit12portACDC,
       "midspanPoHGigabit24portACDC": midspanPoHGigabit24portACDC,
       "pseDevice": pseDevice,
       "portObjects": portObjects,
       "portTable": portTable,
       "portEntry": portEntry,
       "portGroupIndex": portGroupIndex,
       "portIndex": portIndex,
       "portConsumptionPower": portConsumptionPower,
       "portMaxPower": portMaxPower,
       "portType": portType,
       "mainObjects": mainObjects,
       "mainPseTable": mainPseTable,
       "mainPseEntry": mainPseEntry,
       "mainGroupIndex": mainGroupIndex,
       "mainVoltage": mainVoltage,
       "mainDetectionMethod": mainDetectionMethod,
       "mainPowerUsageBudget": mainPowerUsageBudget,
       "mainPSEMaxPower": mainPSEMaxPower,
       "highPowerLegacyPDSupport": highPowerLegacyPDSupport,
       "highPowerExtendedPortPower": highPowerExtendedPortPower,
       "powerBackupStatus": powerBackupStatus,
       "internalPowerSourceStatus": internalPowerSourceStatus,
       "externalPowerSourceStatus": externalPowerSourceStatus,
       "temperature": temperature,
       "temperatureformat": temperatureformat,
       "poeNotifications": poeNotifications,
       "powerBackupStatusNotification": powerBackupStatusNotification,
       "internalPowerSourceStatusNotification": internalPowerSourceStatusNotification,
       "externalPowerSourceStatusNotification": externalPowerSourceStatusNotification}
)
