# SNMP MIB module (EIP-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\efficientip\EIP-MON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:10 2025
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

eip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2440)
)
if mibBuilder.loadTexts:
    eip.setRevisions(
        ("2016-09-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1)
)
_EipHw_ObjectIdentity = ObjectIdentity
eipHw = _EipHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14)
)
_EipHwAppliance_ObjectIdentity = ObjectIdentity
eipHwAppliance = _EipHwAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 1)
)


class _EipHwApplianceModel_Type(OctetString):
    """Custom type eipHwApplianceModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EipHwApplianceModel_Type.__name__ = "OctetString"
_EipHwApplianceModel_Object = MibScalar
eipHwApplianceModel = _EipHwApplianceModel_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 1, 1),
    _EipHwApplianceModel_Type()
)
eipHwApplianceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwApplianceModel.setStatus("current")


class _EipHwApplianceSerial_Type(OctetString):
    """Custom type eipHwApplianceSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EipHwApplianceSerial_Type.__name__ = "OctetString"
_EipHwApplianceSerial_Object = MibScalar
eipHwApplianceSerial = _EipHwApplianceSerial_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 1, 2),
    _EipHwApplianceSerial_Type()
)
eipHwApplianceSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwApplianceSerial.setStatus("current")


class _EipHwApplianceBiosVersion_Type(OctetString):
    """Custom type eipHwApplianceBiosVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EipHwApplianceBiosVersion_Type.__name__ = "OctetString"
_EipHwApplianceBiosVersion_Object = MibScalar
eipHwApplianceBiosVersion = _EipHwApplianceBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 1, 3),
    _EipHwApplianceBiosVersion_Type()
)
eipHwApplianceBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwApplianceBiosVersion.setStatus("current")
_EipHwHdd_ObjectIdentity = ObjectIdentity
eipHwHdd = _EipHwHdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2)
)
_EipHwHddFreeRoot_Type = Counter64
_EipHwHddFreeRoot_Object = MibScalar
eipHwHddFreeRoot = _EipHwHddFreeRoot_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 1),
    _EipHwHddFreeRoot_Type()
)
eipHwHddFreeRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddFreeRoot.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddFreeRoot.setUnits("Kbytes")
_EipHwHddUsedRootPercent_Type = Integer32
_EipHwHddUsedRootPercent_Object = MibScalar
eipHwHddUsedRootPercent = _EipHwHddUsedRootPercent_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 2),
    _EipHwHddUsedRootPercent_Type()
)
eipHwHddUsedRootPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddUsedRootPercent.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddUsedRootPercent.setUnits("%")
_EipHwHddFreeTmp_Type = Counter64
_EipHwHddFreeTmp_Object = MibScalar
eipHwHddFreeTmp = _EipHwHddFreeTmp_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 3),
    _EipHwHddFreeTmp_Type()
)
eipHwHddFreeTmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddFreeTmp.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddFreeTmp.setUnits("Kbytes")
_EipHwHddUsedTmpPercent_Type = Integer32
_EipHwHddUsedTmpPercent_Object = MibScalar
eipHwHddUsedTmpPercent = _EipHwHddUsedTmpPercent_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 4),
    _EipHwHddUsedTmpPercent_Type()
)
eipHwHddUsedTmpPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddUsedTmpPercent.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddUsedTmpPercent.setUnits("%")
_EipHwHddFreeVar_Type = Counter64
_EipHwHddFreeVar_Object = MibScalar
eipHwHddFreeVar = _EipHwHddFreeVar_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 5),
    _EipHwHddFreeVar_Type()
)
eipHwHddFreeVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddFreeVar.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddFreeVar.setUnits("Kbytes")
_EipHwHddUsedVarPercent_Type = Integer32
_EipHwHddUsedVarPercent_Object = MibScalar
eipHwHddUsedVarPercent = _EipHwHddUsedVarPercent_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 6),
    _EipHwHddUsedVarPercent_Type()
)
eipHwHddUsedVarPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddUsedVarPercent.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddUsedVarPercent.setUnits("%")
_EipHwHddFreeData1_Type = Counter64
_EipHwHddFreeData1_Object = MibScalar
eipHwHddFreeData1 = _EipHwHddFreeData1_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 7),
    _EipHwHddFreeData1_Type()
)
eipHwHddFreeData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddFreeData1.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddFreeData1.setUnits("Kbytes")
_EipHwHddUsedData1Percent_Type = Integer32
_EipHwHddUsedData1Percent_Object = MibScalar
eipHwHddUsedData1Percent = _EipHwHddUsedData1Percent_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 8),
    _EipHwHddUsedData1Percent_Type()
)
eipHwHddUsedData1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddUsedData1Percent.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddUsedData1Percent.setUnits("%")
_EipHwHddUsedSwap_Type = Counter64
_EipHwHddUsedSwap_Object = MibScalar
eipHwHddUsedSwap = _EipHwHddUsedSwap_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 50),
    _EipHwHddUsedSwap_Type()
)
eipHwHddUsedSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddUsedSwap.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddUsedSwap.setUnits("Kbytes")
_EipHwHddUsedSwapPercent_Type = Integer32
_EipHwHddUsedSwapPercent_Object = MibScalar
eipHwHddUsedSwapPercent = _EipHwHddUsedSwapPercent_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 51),
    _EipHwHddUsedSwapPercent_Type()
)
eipHwHddUsedSwapPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddUsedSwapPercent.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddUsedSwapPercent.setUnits("%")
_EipHwHddIoLoad_Type = Integer32
_EipHwHddIoLoad_Object = MibScalar
eipHwHddIoLoad = _EipHwHddIoLoad_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 2, 100),
    _EipHwHddIoLoad_Type()
)
eipHwHddIoLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwHddIoLoad.setStatus("current")
if mibBuilder.loadTexts:
    eipHwHddIoLoad.setUnits("%")
_EipHwTemp_ObjectIdentity = ObjectIdentity
eipHwTemp = _EipHwTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 3)
)
_EipHwTempCpu_Type = Integer32
_EipHwTempCpu_Object = MibScalar
eipHwTempCpu = _EipHwTempCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 3, 1),
    _EipHwTempCpu_Type()
)
eipHwTempCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwTempCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipHwTempCpu.setUnits("degrees C")
_EipHwTempCpuCoreMax_Type = Integer32
_EipHwTempCpuCoreMax_Object = MibScalar
eipHwTempCpuCoreMax = _EipHwTempCpuCoreMax_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 3, 2),
    _EipHwTempCpuCoreMax_Type()
)
eipHwTempCpuCoreMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwTempCpuCoreMax.setStatus("current")
if mibBuilder.loadTexts:
    eipHwTempCpuCoreMax.setUnits("degrees C")
_EipHwTempCpuCoreMin_Type = Integer32
_EipHwTempCpuCoreMin_Object = MibScalar
eipHwTempCpuCoreMin = _EipHwTempCpuCoreMin_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 3, 3),
    _EipHwTempCpuCoreMin_Type()
)
eipHwTempCpuCoreMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwTempCpuCoreMin.setStatus("current")
if mibBuilder.loadTexts:
    eipHwTempCpuCoreMin.setUnits("degrees C")
_EipHwTempInlet_Type = Integer32
_EipHwTempInlet_Object = MibScalar
eipHwTempInlet = _EipHwTempInlet_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 3, 4),
    _EipHwTempInlet_Type()
)
eipHwTempInlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwTempInlet.setStatus("current")
if mibBuilder.loadTexts:
    eipHwTempInlet.setUnits("degrees C")
_EipHwTempBaseboard_Type = Integer32
_EipHwTempBaseboard_Object = MibScalar
eipHwTempBaseboard = _EipHwTempBaseboard_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 3, 5),
    _EipHwTempBaseboard_Type()
)
eipHwTempBaseboard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwTempBaseboard.setStatus("current")
if mibBuilder.loadTexts:
    eipHwTempBaseboard.setUnits("degrees C")
_EipHwTempRaidController_Type = Integer32
_EipHwTempRaidController_Object = MibScalar
eipHwTempRaidController = _EipHwTempRaidController_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 3, 6),
    _EipHwTempRaidController_Type()
)
eipHwTempRaidController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwTempRaidController.setStatus("current")
if mibBuilder.loadTexts:
    eipHwTempRaidController.setUnits("degrees C")
_EipHwFan_ObjectIdentity = ObjectIdentity
eipHwFan = _EipHwFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4)
)
_EipHwFan1Speed_Type = Integer32
_EipHwFan1Speed_Object = MibScalar
eipHwFan1Speed = _EipHwFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 1),
    _EipHwFan1Speed_Type()
)
eipHwFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan1Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan1Speed.setUnits("RPM")
_EipHwFan2Speed_Type = Integer32
_EipHwFan2Speed_Object = MibScalar
eipHwFan2Speed = _EipHwFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 2),
    _EipHwFan2Speed_Type()
)
eipHwFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan2Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan2Speed.setUnits("RPM")
_EipHwFan3Speed_Type = Integer32
_EipHwFan3Speed_Object = MibScalar
eipHwFan3Speed = _EipHwFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 3),
    _EipHwFan3Speed_Type()
)
eipHwFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan3Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan3Speed.setUnits("RPM")
_EipHwFan4Speed_Type = Integer32
_EipHwFan4Speed_Object = MibScalar
eipHwFan4Speed = _EipHwFan4Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 4),
    _EipHwFan4Speed_Type()
)
eipHwFan4Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan4Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan4Speed.setUnits("RPM")
_EipHwFan5Speed_Type = Integer32
_EipHwFan5Speed_Object = MibScalar
eipHwFan5Speed = _EipHwFan5Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 5),
    _EipHwFan5Speed_Type()
)
eipHwFan5Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan5Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan5Speed.setUnits("RPM")
_EipHwFan6Speed_Type = Integer32
_EipHwFan6Speed_Object = MibScalar
eipHwFan6Speed = _EipHwFan6Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 6),
    _EipHwFan6Speed_Type()
)
eipHwFan6Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan6Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan6Speed.setUnits("RPM")
_EipHwFan7Speed_Type = Integer32
_EipHwFan7Speed_Object = MibScalar
eipHwFan7Speed = _EipHwFan7Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 7),
    _EipHwFan7Speed_Type()
)
eipHwFan7Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan7Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan7Speed.setUnits("RPM")
_EipHwFan8Speed_Type = Integer32
_EipHwFan8Speed_Object = MibScalar
eipHwFan8Speed = _EipHwFan8Speed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 4, 8),
    _EipHwFan8Speed_Type()
)
eipHwFan8Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwFan8Speed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwFan8Speed.setUnits("RPM")
_EipHwPsu_ObjectIdentity = ObjectIdentity
eipHwPsu = _EipHwPsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 5)
)


class _EipHwPsuRedundancy_Type(Integer32):
    """Custom type eipHwPsuRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ok", 1),
          ("failed", 2))
    )


_EipHwPsuRedundancy_Type.__name__ = "Integer32"
_EipHwPsuRedundancy_Object = MibScalar
eipHwPsuRedundancy = _EipHwPsuRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 5, 1),
    _EipHwPsuRedundancy_Type()
)
eipHwPsuRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwPsuRedundancy.setStatus("current")


class _EipHwPsu1Status_Type(Integer32):
    """Custom type eipHwPsu1Status based on Integer32"""
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
        *(("disabled", 0),
          ("ok", 1),
          ("present", 2),
          ("notpresent", 3))
    )


_EipHwPsu1Status_Type.__name__ = "Integer32"
_EipHwPsu1Status_Object = MibScalar
eipHwPsu1Status = _EipHwPsu1Status_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 5, 2),
    _EipHwPsu1Status_Type()
)
eipHwPsu1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwPsu1Status.setStatus("current")


class _EipHwPsu2Status_Type(Integer32):
    """Custom type eipHwPsu2Status based on Integer32"""
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
        *(("disabled", 0),
          ("ok", 1),
          ("present", 2),
          ("notpresent", 3))
    )


_EipHwPsu2Status_Type.__name__ = "Integer32"
_EipHwPsu2Status_Object = MibScalar
eipHwPsu2Status = _EipHwPsu2Status_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 5, 3),
    _EipHwPsu2Status_Type()
)
eipHwPsu2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwPsu2Status.setStatus("current")
_EipHwPower_ObjectIdentity = ObjectIdentity
eipHwPower = _EipHwPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 6)
)
_EipHwPowerInstant_Type = Integer32
_EipHwPowerInstant_Object = MibScalar
eipHwPowerInstant = _EipHwPowerInstant_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 6, 1),
    _EipHwPowerInstant_Type()
)
eipHwPowerInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwPowerInstant.setStatus("current")
if mibBuilder.loadTexts:
    eipHwPowerInstant.setUnits("W")
_EipHwPowerCumulative_Type = Integer32
_EipHwPowerCumulative_Object = MibScalar
eipHwPowerCumulative = _EipHwPowerCumulative_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 6, 2),
    _EipHwPowerCumulative_Type()
)
eipHwPowerCumulative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwPowerCumulative.setStatus("current")
if mibBuilder.loadTexts:
    eipHwPowerCumulative.setUnits("kWh")
_EipHwPowerPeak_Type = Integer32
_EipHwPowerPeak_Object = MibScalar
eipHwPowerPeak = _EipHwPowerPeak_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 6, 3),
    _EipHwPowerPeak_Type()
)
eipHwPowerPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwPowerPeak.setStatus("current")
if mibBuilder.loadTexts:
    eipHwPowerPeak.setUnits("W")
_EipHwPowerPeakAmperage_Type = Integer32
_EipHwPowerPeakAmperage_Object = MibScalar
eipHwPowerPeakAmperage = _EipHwPowerPeakAmperage_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 6, 4),
    _EipHwPowerPeakAmperage_Type()
)
eipHwPowerPeakAmperage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwPowerPeakAmperage.setStatus("current")
if mibBuilder.loadTexts:
    eipHwPowerPeakAmperage.setUnits("mA")
_EipHwRaid_ObjectIdentity = ObjectIdentity
eipHwRaid = _EipHwRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7)
)
_EipHwRaidController_Type = OctetString
_EipHwRaidController_Object = MibScalar
eipHwRaidController = _EipHwRaidController_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7, 1),
    _EipHwRaidController_Type()
)
eipHwRaidController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwRaidController.setStatus("current")


class _EipHwRaidStatus_Type(Integer32):
    """Custom type eipHwRaidStatus based on Integer32"""
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
        *(("disabled", 0),
          ("ok", 1),
          ("degraded", 2),
          ("offline", 3))
    )


_EipHwRaidStatus_Type.__name__ = "Integer32"
_EipHwRaidStatus_Object = MibScalar
eipHwRaidStatus = _EipHwRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7, 2),
    _EipHwRaidStatus_Type()
)
eipHwRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwRaidStatus.setStatus("current")
_EipHwRaidDisks_Type = Integer32
_EipHwRaidDisks_Object = MibScalar
eipHwRaidDisks = _EipHwRaidDisks_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7, 3),
    _EipHwRaidDisks_Type()
)
eipHwRaidDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwRaidDisks.setStatus("current")
_EipHwRaidDisksCritical_Type = Integer32
_EipHwRaidDisksCritical_Object = MibScalar
eipHwRaidDisksCritical = _EipHwRaidDisksCritical_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7, 4),
    _EipHwRaidDisksCritical_Type()
)
eipHwRaidDisksCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwRaidDisksCritical.setStatus("current")
_EipHwRaidDisksFailed_Type = Integer32
_EipHwRaidDisksFailed_Object = MibScalar
eipHwRaidDisksFailed = _EipHwRaidDisksFailed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7, 5),
    _EipHwRaidDisksFailed_Type()
)
eipHwRaidDisksFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwRaidDisksFailed.setStatus("current")


class _EipHwRaidBbuStatus_Type(Integer32):
    """Custom type eipHwRaidBbuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ok", 1),
          ("degraded", 2))
    )


_EipHwRaidBbuStatus_Type.__name__ = "Integer32"
_EipHwRaidBbuStatus_Object = MibScalar
eipHwRaidBbuStatus = _EipHwRaidBbuStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7, 6),
    _EipHwRaidBbuStatus_Type()
)
eipHwRaidBbuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwRaidBbuStatus.setStatus("current")
_EipHwRaidBbuCharge_Type = Integer32
_EipHwRaidBbuCharge_Object = MibScalar
eipHwRaidBbuCharge = _EipHwRaidBbuCharge_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 7, 7),
    _EipHwRaidBbuCharge_Type()
)
eipHwRaidBbuCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwRaidBbuCharge.setStatus("current")
if mibBuilder.loadTexts:
    eipHwRaidBbuCharge.setUnits("%")
_EipHwCpu_ObjectIdentity = ObjectIdentity
eipHwCpu = _EipHwCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 8)
)
_EipHwCpuLoadInt_Type = Integer32
_EipHwCpuLoadInt_Object = MibScalar
eipHwCpuLoadInt = _EipHwCpuLoadInt_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 8, 1),
    _EipHwCpuLoadInt_Type()
)
eipHwCpuLoadInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwCpuLoadInt.setStatus("current")
_EipHwCpuCoreNumber_Type = Integer32
_EipHwCpuCoreNumber_Object = MibScalar
eipHwCpuCoreNumber = _EipHwCpuCoreNumber_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 8, 2),
    _EipHwCpuCoreNumber_Type()
)
eipHwCpuCoreNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwCpuCoreNumber.setStatus("current")
_EipHwMem_ObjectIdentity = ObjectIdentity
eipHwMem = _EipHwMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 9)
)
_EipHwMemUsed_Type = Integer32
_EipHwMemUsed_Object = MibScalar
eipHwMemUsed = _EipHwMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 9, 1),
    _EipHwMemUsed_Type()
)
eipHwMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    eipHwMemUsed.setUnits("%")
_EipHwChassis_ObjectIdentity = ObjectIdentity
eipHwChassis = _EipHwChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 10)
)


class _EipHwChassisIntrusion_Type(Integer32):
    """Custom type eipHwChassisIntrusion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("inactive", 1),
          ("active", 2))
    )


_EipHwChassisIntrusion_Type.__name__ = "Integer32"
_EipHwChassisIntrusion_Object = MibScalar
eipHwChassisIntrusion = _EipHwChassisIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 14, 10, 1),
    _EipHwChassisIntrusion_Type()
)
eipHwChassisIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipHwChassisIntrusion.setStatus("current")
_EipNet_ObjectIdentity = ObjectIdentity
eipNet = _EipNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15)
)
_EipNetCfg_ObjectIdentity = ObjectIdentity
eipNetCfg = _EipNetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1)
)
_EipNetCarp_ObjectIdentity = ObjectIdentity
eipNetCarp = _EipNetCarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1)
)
_EipNetCarpIf_ObjectIdentity = ObjectIdentity
eipNetCarpIf = _EipNetCarpIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1)
)
_EipNetCarpIfNumber_Type = Integer32
_EipNetCarpIfNumber_Object = MibScalar
eipNetCarpIfNumber = _EipNetCarpIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 1),
    _EipNetCarpIfNumber_Type()
)
eipNetCarpIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfNumber.setStatus("current")
_EipNetCarpIfTable_Object = MibTable
eipNetCarpIfTable = _EipNetCarpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eipNetCarpIfTable.setStatus("current")
_EipNetCarpIfEntry_Object = MibTableRow
eipNetCarpIfEntry = _EipNetCarpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1)
)
eipNetCarpIfEntry.setIndexNames(
    (0, "EIP-MON-MIB", "eipNetCarpIfIndex"),
)
if mibBuilder.loadTexts:
    eipNetCarpIfEntry.setStatus("current")


class _EipNetCarpIfIndex_Type(Integer32):
    """Custom type eipNetCarpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EipNetCarpIfIndex_Type.__name__ = "Integer32"
_EipNetCarpIfIndex_Object = MibTableColumn
eipNetCarpIfIndex = _EipNetCarpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1, 1),
    _EipNetCarpIfIndex_Type()
)
eipNetCarpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfIndex.setStatus("current")
_EipNetCarpIfDescr_Type = OctetString
_EipNetCarpIfDescr_Object = MibTableColumn
eipNetCarpIfDescr = _EipNetCarpIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1, 2),
    _EipNetCarpIfDescr_Type()
)
eipNetCarpIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfDescr.setStatus("current")
_EipNetCarpIfVhid_Type = Integer32
_EipNetCarpIfVhid_Object = MibTableColumn
eipNetCarpIfVhid = _EipNetCarpIfVhid_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1, 3),
    _EipNetCarpIfVhid_Type()
)
eipNetCarpIfVhid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfVhid.setStatus("current")
_EipNetCarpIfDev_Type = OctetString
_EipNetCarpIfDev_Object = MibTableColumn
eipNetCarpIfDev = _EipNetCarpIfDev_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1, 4),
    _EipNetCarpIfDev_Type()
)
eipNetCarpIfDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfDev.setStatus("current")
_EipNetCarpIfAdvbase_Type = Integer32
_EipNetCarpIfAdvbase_Object = MibTableColumn
eipNetCarpIfAdvbase = _EipNetCarpIfAdvbase_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1, 5),
    _EipNetCarpIfAdvbase_Type()
)
eipNetCarpIfAdvbase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfAdvbase.setStatus("current")
_EipNetCarpIfAdvskew_Type = Integer32
_EipNetCarpIfAdvskew_Object = MibTableColumn
eipNetCarpIfAdvskew = _EipNetCarpIfAdvskew_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1, 6),
    _EipNetCarpIfAdvskew_Type()
)
eipNetCarpIfAdvskew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfAdvskew.setStatus("current")


class _EipNetCarpIfState_Type(Integer32):
    """Custom type eipNetCarpIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("backup", 1),
          ("master", 2))
    )


_EipNetCarpIfState_Type.__name__ = "Integer32"
_EipNetCarpIfState_Object = MibTableColumn
eipNetCarpIfState = _EipNetCarpIfState_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 1, 1, 2, 1, 7),
    _EipNetCarpIfState_Type()
)
eipNetCarpIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetCarpIfState.setStatus("current")
_EipNetLagg_ObjectIdentity = ObjectIdentity
eipNetLagg = _EipNetLagg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 2)
)


class _EipNetLaggStatus_Type(Integer32):
    """Custom type eipNetLaggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ok", 1),
          ("failed", 2))
    )


_EipNetLaggStatus_Type.__name__ = "Integer32"
_EipNetLaggStatus_Object = MibScalar
eipNetLaggStatus = _EipNetLaggStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 1, 2, 1),
    _EipNetLaggStatus_Type()
)
eipNetLaggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetLaggStatus.setStatus("current")
_EipNetStat_ObjectIdentity = ObjectIdentity
eipNetStat = _EipNetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2)
)
_EipNetStatHttp_ObjectIdentity = ObjectIdentity
eipNetStatHttp = _EipNetStatHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 1)
)
_EipNetStatHttpInOctets_Type = Counter64
_EipNetStatHttpInOctets_Object = MibScalar
eipNetStatHttpInOctets = _EipNetStatHttpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 1, 1),
    _EipNetStatHttpInOctets_Type()
)
eipNetStatHttpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatHttpInOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatHttpInOctets.setUnits("bytes")
_EipNetStatHttpInPkts_Type = Counter64
_EipNetStatHttpInPkts_Object = MibScalar
eipNetStatHttpInPkts = _EipNetStatHttpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 1, 2),
    _EipNetStatHttpInPkts_Type()
)
eipNetStatHttpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatHttpInPkts.setStatus("current")
_EipNetStatHttpOutOctets_Type = Counter64
_EipNetStatHttpOutOctets_Object = MibScalar
eipNetStatHttpOutOctets = _EipNetStatHttpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 1, 3),
    _EipNetStatHttpOutOctets_Type()
)
eipNetStatHttpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatHttpOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatHttpOutOctets.setUnits("bytes")
_EipNetStatHttpOutPkts_Type = Counter64
_EipNetStatHttpOutPkts_Object = MibScalar
eipNetStatHttpOutPkts = _EipNetStatHttpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 1, 4),
    _EipNetStatHttpOutPkts_Type()
)
eipNetStatHttpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatHttpOutPkts.setStatus("current")
_EipNetStatDns_ObjectIdentity = ObjectIdentity
eipNetStatDns = _EipNetStatDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 2)
)
_EipNetStatDnsInOctets_Type = Counter64
_EipNetStatDnsInOctets_Object = MibScalar
eipNetStatDnsInOctets = _EipNetStatDnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 2, 1),
    _EipNetStatDnsInOctets_Type()
)
eipNetStatDnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDnsInOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatDnsInOctets.setUnits("bytes")
_EipNetStatDnsInPkts_Type = Counter64
_EipNetStatDnsInPkts_Object = MibScalar
eipNetStatDnsInPkts = _EipNetStatDnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 2, 2),
    _EipNetStatDnsInPkts_Type()
)
eipNetStatDnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDnsInPkts.setStatus("current")
_EipNetStatDnsOutOctets_Type = Counter64
_EipNetStatDnsOutOctets_Object = MibScalar
eipNetStatDnsOutOctets = _EipNetStatDnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 2, 3),
    _EipNetStatDnsOutOctets_Type()
)
eipNetStatDnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDnsOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatDnsOutOctets.setUnits("bytes")
_EipNetStatDnsOutPkts_Type = Counter64
_EipNetStatDnsOutPkts_Object = MibScalar
eipNetStatDnsOutPkts = _EipNetStatDnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 2, 4),
    _EipNetStatDnsOutPkts_Type()
)
eipNetStatDnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDnsOutPkts.setStatus("current")
_EipNetStatDhcp_ObjectIdentity = ObjectIdentity
eipNetStatDhcp = _EipNetStatDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 3)
)
_EipNetStatDhcpInOctets_Type = Counter64
_EipNetStatDhcpInOctets_Object = MibScalar
eipNetStatDhcpInOctets = _EipNetStatDhcpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 3, 1),
    _EipNetStatDhcpInOctets_Type()
)
eipNetStatDhcpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDhcpInOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatDhcpInOctets.setUnits("bytes")
_EipNetStatDhcpInPkts_Type = Counter64
_EipNetStatDhcpInPkts_Object = MibScalar
eipNetStatDhcpInPkts = _EipNetStatDhcpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 3, 2),
    _EipNetStatDhcpInPkts_Type()
)
eipNetStatDhcpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDhcpInPkts.setStatus("current")
_EipNetStatDhcpOutOctets_Type = Counter64
_EipNetStatDhcpOutOctets_Object = MibScalar
eipNetStatDhcpOutOctets = _EipNetStatDhcpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 3, 3),
    _EipNetStatDhcpOutOctets_Type()
)
eipNetStatDhcpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDhcpOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatDhcpOutOctets.setUnits("bytes")
_EipNetStatDhcpOutPkts_Type = Counter64
_EipNetStatDhcpOutPkts_Object = MibScalar
eipNetStatDhcpOutPkts = _EipNetStatDhcpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 3, 4),
    _EipNetStatDhcpOutPkts_Type()
)
eipNetStatDhcpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDhcpOutPkts.setStatus("current")
_EipNetStatDb_ObjectIdentity = ObjectIdentity
eipNetStatDb = _EipNetStatDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 4)
)
_EipNetStatDbInOctets_Type = Counter64
_EipNetStatDbInOctets_Object = MibScalar
eipNetStatDbInOctets = _EipNetStatDbInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 4, 1),
    _EipNetStatDbInOctets_Type()
)
eipNetStatDbInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDbInOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatDbInOctets.setUnits("bytes")
_EipNetStatDbInPkts_Type = Counter64
_EipNetStatDbInPkts_Object = MibScalar
eipNetStatDbInPkts = _EipNetStatDbInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 4, 2),
    _EipNetStatDbInPkts_Type()
)
eipNetStatDbInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDbInPkts.setStatus("current")
_EipNetStatDbOutOctets_Type = Counter64
_EipNetStatDbOutOctets_Object = MibScalar
eipNetStatDbOutOctets = _EipNetStatDbOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 4, 3),
    _EipNetStatDbOutOctets_Type()
)
eipNetStatDbOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDbOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatDbOutOctets.setUnits("bytes")
_EipNetStatDbOutPkts_Type = Counter64
_EipNetStatDbOutPkts_Object = MibScalar
eipNetStatDbOutPkts = _EipNetStatDbOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 4, 4),
    _EipNetStatDbOutPkts_Type()
)
eipNetStatDbOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatDbOutPkts.setStatus("current")
_EipNetStatSnmp_ObjectIdentity = ObjectIdentity
eipNetStatSnmp = _EipNetStatSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 5)
)
_EipNetStatSnmpInOctets_Type = Counter64
_EipNetStatSnmpInOctets_Object = MibScalar
eipNetStatSnmpInOctets = _EipNetStatSnmpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 5, 1),
    _EipNetStatSnmpInOctets_Type()
)
eipNetStatSnmpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatSnmpInOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatSnmpInOctets.setUnits("bytes")
_EipNetStatSnmpInPkts_Type = Counter64
_EipNetStatSnmpInPkts_Object = MibScalar
eipNetStatSnmpInPkts = _EipNetStatSnmpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 5, 2),
    _EipNetStatSnmpInPkts_Type()
)
eipNetStatSnmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatSnmpInPkts.setStatus("current")
_EipNetStatSnmpOutOctets_Type = Counter64
_EipNetStatSnmpOutOctets_Object = MibScalar
eipNetStatSnmpOutOctets = _EipNetStatSnmpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 5, 3),
    _EipNetStatSnmpOutOctets_Type()
)
eipNetStatSnmpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatSnmpOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    eipNetStatSnmpOutOctets.setUnits("bytes")
_EipNetStatSnmpOutPkts_Type = Counter64
_EipNetStatSnmpOutPkts_Object = MibScalar
eipNetStatSnmpOutPkts = _EipNetStatSnmpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 2, 5, 4),
    _EipNetStatSnmpOutPkts_Type()
)
eipNetStatSnmpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipNetStatSnmpOutPkts.setStatus("current")
_EipSvc_ObjectIdentity = ObjectIdentity
eipSvc = _EipSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16)
)
_EipSvcSyslog_ObjectIdentity = ObjectIdentity
eipSvcSyslog = _EipSvcSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 1)
)


class _EipSvcSyslogStatus_Type(Integer32):
    """Custom type eipSvcSyslogStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcSyslogStatus_Type.__name__ = "Integer32"
_EipSvcSyslogStatus_Object = MibScalar
eipSvcSyslogStatus = _EipSvcSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 1, 1),
    _EipSvcSyslogStatus_Type()
)
eipSvcSyslogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSyslogStatus.setStatus("current")
_EipSvcSyslogCpu_Type = Gauge32
_EipSvcSyslogCpu_Object = MibScalar
eipSvcSyslogCpu = _EipSvcSyslogCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 1, 2),
    _EipSvcSyslogCpu_Type()
)
eipSvcSyslogCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSyslogCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSyslogCpu.setUnits("%")
_EipSvcSyslogMem_Type = Gauge32
_EipSvcSyslogMem_Object = MibScalar
eipSvcSyslogMem = _EipSvcSyslogMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 1, 3),
    _EipSvcSyslogMem_Type()
)
eipSvcSyslogMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSyslogMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSyslogMem.setUnits("Kbytes")
_EipSvcSyslogDiskIoRead_Type = Gauge32
_EipSvcSyslogDiskIoRead_Object = MibScalar
eipSvcSyslogDiskIoRead = _EipSvcSyslogDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 1, 4),
    _EipSvcSyslogDiskIoRead_Type()
)
eipSvcSyslogDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSyslogDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSyslogDiskIoRead.setUnits("blocks")
_EipSvcSyslogDiskIoWrite_Type = Gauge32
_EipSvcSyslogDiskIoWrite_Object = MibScalar
eipSvcSyslogDiskIoWrite = _EipSvcSyslogDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 1, 5),
    _EipSvcSyslogDiskIoWrite_Type()
)
eipSvcSyslogDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSyslogDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSyslogDiskIoWrite.setUnits("blocks")
_EipSvcSsh_ObjectIdentity = ObjectIdentity
eipSvcSsh = _EipSvcSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 2)
)


class _EipSvcSshStatus_Type(Integer32):
    """Custom type eipSvcSshStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcSshStatus_Type.__name__ = "Integer32"
_EipSvcSshStatus_Object = MibScalar
eipSvcSshStatus = _EipSvcSshStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 2, 1),
    _EipSvcSshStatus_Type()
)
eipSvcSshStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSshStatus.setStatus("current")
_EipSvcSshCpu_Type = Gauge32
_EipSvcSshCpu_Object = MibScalar
eipSvcSshCpu = _EipSvcSshCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 2, 2),
    _EipSvcSshCpu_Type()
)
eipSvcSshCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSshCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSshCpu.setUnits("%")
_EipSvcSshMem_Type = Gauge32
_EipSvcSshMem_Object = MibScalar
eipSvcSshMem = _EipSvcSshMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 2, 3),
    _EipSvcSshMem_Type()
)
eipSvcSshMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSshMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSshMem.setUnits("Kbytes")
_EipSvcSshDiskIoRead_Type = Gauge32
_EipSvcSshDiskIoRead_Object = MibScalar
eipSvcSshDiskIoRead = _EipSvcSshDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 2, 4),
    _EipSvcSshDiskIoRead_Type()
)
eipSvcSshDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSshDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSshDiskIoRead.setUnits("blocks")
_EipSvcSshDiskIoWrite_Type = Gauge32
_EipSvcSshDiskIoWrite_Object = MibScalar
eipSvcSshDiskIoWrite = _EipSvcSshDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 2, 5),
    _EipSvcSshDiskIoWrite_Type()
)
eipSvcSshDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSshDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSshDiskIoWrite.setUnits("blocks")
_EipSvcSshConnections_Type = Integer32
_EipSvcSshConnections_Object = MibScalar
eipSvcSshConnections = _EipSvcSshConnections_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 2, 6),
    _EipSvcSshConnections_Type()
)
eipSvcSshConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSshConnections.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSshConnections.setUnits("connections")
_EipSvcApache_ObjectIdentity = ObjectIdentity
eipSvcApache = _EipSvcApache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 3)
)


class _EipSvcApacheStatus_Type(Integer32):
    """Custom type eipSvcApacheStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcApacheStatus_Type.__name__ = "Integer32"
_EipSvcApacheStatus_Object = MibScalar
eipSvcApacheStatus = _EipSvcApacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 3, 1),
    _EipSvcApacheStatus_Type()
)
eipSvcApacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcApacheStatus.setStatus("current")
_EipSvcApacheCpu_Type = Gauge32
_EipSvcApacheCpu_Object = MibScalar
eipSvcApacheCpu = _EipSvcApacheCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 3, 2),
    _EipSvcApacheCpu_Type()
)
eipSvcApacheCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcApacheCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcApacheCpu.setUnits("%")
_EipSvcApacheMem_Type = Gauge32
_EipSvcApacheMem_Object = MibScalar
eipSvcApacheMem = _EipSvcApacheMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 3, 3),
    _EipSvcApacheMem_Type()
)
eipSvcApacheMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcApacheMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcApacheMem.setUnits("Kbytes")
_EipSvcApacheDiskIoRead_Type = Gauge32
_EipSvcApacheDiskIoRead_Object = MibScalar
eipSvcApacheDiskIoRead = _EipSvcApacheDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 3, 4),
    _EipSvcApacheDiskIoRead_Type()
)
eipSvcApacheDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcApacheDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcApacheDiskIoRead.setUnits("blocks")
_EipSvcApacheDiskIoWrite_Type = Gauge32
_EipSvcApacheDiskIoWrite_Object = MibScalar
eipSvcApacheDiskIoWrite = _EipSvcApacheDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 3, 5),
    _EipSvcApacheDiskIoWrite_Type()
)
eipSvcApacheDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcApacheDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcApacheDiskIoWrite.setUnits("blocks")
_EipSvcApacheConnections_Type = Integer32
_EipSvcApacheConnections_Object = MibScalar
eipSvcApacheConnections = _EipSvcApacheConnections_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 3, 6),
    _EipSvcApacheConnections_Type()
)
eipSvcApacheConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcApacheConnections.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcApacheConnections.setUnits("sessions")
_EipSvcIpmServer_ObjectIdentity = ObjectIdentity
eipSvcIpmServer = _EipSvcIpmServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4)
)


class _EipSvcIpmServerStatus_Type(Integer32):
    """Custom type eipSvcIpmServerStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcIpmServerStatus_Type.__name__ = "Integer32"
_EipSvcIpmServerStatus_Object = MibScalar
eipSvcIpmServerStatus = _EipSvcIpmServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 1),
    _EipSvcIpmServerStatus_Type()
)
eipSvcIpmServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerStatus.setStatus("current")
_EipSvcIpmServerCpu_Type = Gauge32
_EipSvcIpmServerCpu_Object = MibScalar
eipSvcIpmServerCpu = _EipSvcIpmServerCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 2),
    _EipSvcIpmServerCpu_Type()
)
eipSvcIpmServerCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcIpmServerCpu.setUnits("%")
_EipSvcIpmServerMem_Type = Gauge32
_EipSvcIpmServerMem_Object = MibScalar
eipSvcIpmServerMem = _EipSvcIpmServerMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 3),
    _EipSvcIpmServerMem_Type()
)
eipSvcIpmServerMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcIpmServerMem.setUnits("Kbytes")
_EipSvcIpmServerDiskIoRead_Type = Gauge32
_EipSvcIpmServerDiskIoRead_Object = MibScalar
eipSvcIpmServerDiskIoRead = _EipSvcIpmServerDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 4),
    _EipSvcIpmServerDiskIoRead_Type()
)
eipSvcIpmServerDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcIpmServerDiskIoRead.setUnits("blocks")
_EipSvcIpmServerDiskIoWrite_Type = Gauge32
_EipSvcIpmServerDiskIoWrite_Object = MibScalar
eipSvcIpmServerDiskIoWrite = _EipSvcIpmServerDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 5),
    _EipSvcIpmServerDiskIoWrite_Type()
)
eipSvcIpmServerDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcIpmServerDiskIoWrite.setUnits("blocks")
_EipSvcIpmServerUserSessions_Type = Gauge32
_EipSvcIpmServerUserSessions_Object = MibScalar
eipSvcIpmServerUserSessions = _EipSvcIpmServerUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 6),
    _EipSvcIpmServerUserSessions_Type()
)
eipSvcIpmServerUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerUserSessions.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcIpmServerUserSessions.setUnits("sessions")
_EipSvcIpmServerThreads_Type = Counter32
_EipSvcIpmServerThreads_Object = MibScalar
eipSvcIpmServerThreads = _EipSvcIpmServerThreads_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 7),
    _EipSvcIpmServerThreads_Type()
)
eipSvcIpmServerThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerThreads.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcIpmServerThreads.setUnits("threads")
_EipSvcIpmServerDbQueries_Type = Counter32
_EipSvcIpmServerDbQueries_Object = MibScalar
eipSvcIpmServerDbQueries = _EipSvcIpmServerDbQueries_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 4, 8),
    _EipSvcIpmServerDbQueries_Type()
)
eipSvcIpmServerDbQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcIpmServerDbQueries.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcIpmServerDbQueries.setUnits("queries")
_EipSvcDatabase_ObjectIdentity = ObjectIdentity
eipSvcDatabase = _EipSvcDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5)
)


class _EipSvcDatabaseStatus_Type(Integer32):
    """Custom type eipSvcDatabaseStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcDatabaseStatus_Type.__name__ = "Integer32"
_EipSvcDatabaseStatus_Object = MibScalar
eipSvcDatabaseStatus = _EipSvcDatabaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 1),
    _EipSvcDatabaseStatus_Type()
)
eipSvcDatabaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseStatus.setStatus("current")
_EipSvcDatabaseCpu_Type = Gauge32
_EipSvcDatabaseCpu_Object = MibScalar
eipSvcDatabaseCpu = _EipSvcDatabaseCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 2),
    _EipSvcDatabaseCpu_Type()
)
eipSvcDatabaseCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDatabaseCpu.setUnits("%")
_EipSvcDatabaseMem_Type = Gauge32
_EipSvcDatabaseMem_Object = MibScalar
eipSvcDatabaseMem = _EipSvcDatabaseMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 3),
    _EipSvcDatabaseMem_Type()
)
eipSvcDatabaseMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDatabaseMem.setUnits("Kbytes")
_EipSvcDatabaseDiskIoRead_Type = Gauge32
_EipSvcDatabaseDiskIoRead_Object = MibScalar
eipSvcDatabaseDiskIoRead = _EipSvcDatabaseDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 4),
    _EipSvcDatabaseDiskIoRead_Type()
)
eipSvcDatabaseDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDatabaseDiskIoRead.setUnits("blocks")
_EipSvcDatabaseDiskIoWrite_Type = Gauge32
_EipSvcDatabaseDiskIoWrite_Object = MibScalar
eipSvcDatabaseDiskIoWrite = _EipSvcDatabaseDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 5),
    _EipSvcDatabaseDiskIoWrite_Type()
)
eipSvcDatabaseDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDatabaseDiskIoWrite.setUnits("blocks")


class _EipSvcDatabaseReplicationStatus_Type(Integer32):
    """Custom type eipSvcDatabaseReplicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("active", 1),
          ("initializing", 2))
    )


_EipSvcDatabaseReplicationStatus_Type.__name__ = "Integer32"
_EipSvcDatabaseReplicationStatus_Object = MibScalar
eipSvcDatabaseReplicationStatus = _EipSvcDatabaseReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 6),
    _EipSvcDatabaseReplicationStatus_Type()
)
eipSvcDatabaseReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseReplicationStatus.setStatus("current")
_EipSvcDatabaseReplicationOffset_Type = Gauge32
_EipSvcDatabaseReplicationOffset_Object = MibScalar
eipSvcDatabaseReplicationOffset = _EipSvcDatabaseReplicationOffset_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 7),
    _EipSvcDatabaseReplicationOffset_Type()
)
eipSvcDatabaseReplicationOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseReplicationOffset.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDatabaseReplicationOffset.setUnits("Kbytes")
_EipSvcDatabaseReplicationLastReplay_Type = Gauge32
_EipSvcDatabaseReplicationLastReplay_Object = MibScalar
eipSvcDatabaseReplicationLastReplay = _EipSvcDatabaseReplicationLastReplay_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 8),
    _EipSvcDatabaseReplicationLastReplay_Type()
)
eipSvcDatabaseReplicationLastReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseReplicationLastReplay.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDatabaseReplicationLastReplay.setUnits("s")
_EipSvcDatabaseBackends_Type = Gauge32
_EipSvcDatabaseBackends_Object = MibScalar
eipSvcDatabaseBackends = _EipSvcDatabaseBackends_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 9),
    _EipSvcDatabaseBackends_Type()
)
eipSvcDatabaseBackends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseBackends.setStatus("current")
_EipSvcDatabaseDeadlocks_Type = Gauge32
_EipSvcDatabaseDeadlocks_Object = MibScalar
eipSvcDatabaseDeadlocks = _EipSvcDatabaseDeadlocks_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 10),
    _EipSvcDatabaseDeadlocks_Type()
)
eipSvcDatabaseDeadlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseDeadlocks.setStatus("current")
_EipSvcDatabaseBloat_Type = Gauge32
_EipSvcDatabaseBloat_Object = MibScalar
eipSvcDatabaseBloat = _EipSvcDatabaseBloat_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 5, 11),
    _EipSvcDatabaseBloat_Type()
)
eipSvcDatabaseBloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDatabaseBloat.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDatabaseBloat.setUnits("Kbytes")
_EipSvcDhcp_ObjectIdentity = ObjectIdentity
eipSvcDhcp = _EipSvcDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6)
)


class _EipSvcDhcpStatus_Type(Integer32):
    """Custom type eipSvcDhcpStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcDhcpStatus_Type.__name__ = "Integer32"
_EipSvcDhcpStatus_Object = MibScalar
eipSvcDhcpStatus = _EipSvcDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 1),
    _EipSvcDhcpStatus_Type()
)
eipSvcDhcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpStatus.setStatus("current")
_EipSvcDhcpCpu_Type = Gauge32
_EipSvcDhcpCpu_Object = MibScalar
eipSvcDhcpCpu = _EipSvcDhcpCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 2),
    _EipSvcDhcpCpu_Type()
)
eipSvcDhcpCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpCpu.setUnits("%")
_EipSvcDhcpMem_Type = Gauge32
_EipSvcDhcpMem_Object = MibScalar
eipSvcDhcpMem = _EipSvcDhcpMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 3),
    _EipSvcDhcpMem_Type()
)
eipSvcDhcpMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpMem.setUnits("Kbytes")
_EipSvcDhcpDiskIoRead_Type = Gauge32
_EipSvcDhcpDiskIoRead_Object = MibScalar
eipSvcDhcpDiskIoRead = _EipSvcDhcpDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 4),
    _EipSvcDhcpDiskIoRead_Type()
)
eipSvcDhcpDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpDiskIoRead.setUnits("blocks")
_EipSvcDhcpDiskIoWrite_Type = Gauge32
_EipSvcDhcpDiskIoWrite_Object = MibScalar
eipSvcDhcpDiskIoWrite = _EipSvcDhcpDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 5),
    _EipSvcDhcpDiskIoWrite_Type()
)
eipSvcDhcpDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpDiskIoWrite.setUnits("blocks")
_EipSvcDhcpFailoverNumber_Type = Integer32
_EipSvcDhcpFailoverNumber_Object = MibScalar
eipSvcDhcpFailoverNumber = _EipSvcDhcpFailoverNumber_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 6),
    _EipSvcDhcpFailoverNumber_Type()
)
eipSvcDhcpFailoverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpFailoverNumber.setStatus("current")
_EipSvcDhcpFailoverTable_Object = MibTable
eipSvcDhcpFailoverTable = _EipSvcDhcpFailoverTable_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 7)
)
if mibBuilder.loadTexts:
    eipSvcDhcpFailoverTable.setStatus("current")
_EipSvcDhcpFailoverEntry_Object = MibTableRow
eipSvcDhcpFailoverEntry = _EipSvcDhcpFailoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 7, 1)
)
eipSvcDhcpFailoverEntry.setIndexNames(
    (0, "EIP-MON-MIB", "eipSvcDhcpFailoverIndex"),
)
if mibBuilder.loadTexts:
    eipSvcDhcpFailoverEntry.setStatus("current")


class _EipSvcDhcpFailoverIndex_Type(Integer32):
    """Custom type eipSvcDhcpFailoverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EipSvcDhcpFailoverIndex_Type.__name__ = "Integer32"
_EipSvcDhcpFailoverIndex_Object = MibTableColumn
eipSvcDhcpFailoverIndex = _EipSvcDhcpFailoverIndex_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 7, 1, 1),
    _EipSvcDhcpFailoverIndex_Type()
)
eipSvcDhcpFailoverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpFailoverIndex.setStatus("current")
_EipSvcDhcpFailoverName_Type = OctetString
_EipSvcDhcpFailoverName_Object = MibTableColumn
eipSvcDhcpFailoverName = _EipSvcDhcpFailoverName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 7, 1, 2),
    _EipSvcDhcpFailoverName_Type()
)
eipSvcDhcpFailoverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpFailoverName.setStatus("current")


class _EipSvcDhcpFailoverStatus_Type(Integer32):
    """Custom type eipSvcDhcpFailoverStatus based on Integer32"""
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
              254)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("startup", 1),
          ("normal", 2),
          ("communicationsInterrupted", 3),
          ("partnerDown", 4),
          ("potentialConflict", 5),
          ("recover", 6),
          ("paused", 7),
          ("shutdown", 8),
          ("recoverDone", 9),
          ("resolutionInterrupted", 10),
          ("conflictDone", 11),
          ("recoverWait", 254))
    )


_EipSvcDhcpFailoverStatus_Type.__name__ = "Integer32"
_EipSvcDhcpFailoverStatus_Object = MibTableColumn
eipSvcDhcpFailoverStatus = _EipSvcDhcpFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 6, 7, 1, 3),
    _EipSvcDhcpFailoverStatus_Type()
)
eipSvcDhcpFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpFailoverStatus.setStatus("current")
_EipSvcDhcpMs_ObjectIdentity = ObjectIdentity
eipSvcDhcpMs = _EipSvcDhcpMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 7)
)


class _EipSvcDhcpMsStatus_Type(Integer32):
    """Custom type eipSvcDhcpMsStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcDhcpMsStatus_Type.__name__ = "Integer32"
_EipSvcDhcpMsStatus_Object = MibScalar
eipSvcDhcpMsStatus = _EipSvcDhcpMsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 7, 1),
    _EipSvcDhcpMsStatus_Type()
)
eipSvcDhcpMsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpMsStatus.setStatus("current")
_EipSvcDhcpMsCpu_Type = Gauge32
_EipSvcDhcpMsCpu_Object = MibScalar
eipSvcDhcpMsCpu = _EipSvcDhcpMsCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 7, 2),
    _EipSvcDhcpMsCpu_Type()
)
eipSvcDhcpMsCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpMsCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpMsCpu.setUnits("%")
_EipSvcDhcpMsMem_Type = Gauge32
_EipSvcDhcpMsMem_Object = MibScalar
eipSvcDhcpMsMem = _EipSvcDhcpMsMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 7, 3),
    _EipSvcDhcpMsMem_Type()
)
eipSvcDhcpMsMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpMsMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpMsMem.setUnits("Kbytes")
_EipSvcDhcpMsDiskIoRead_Type = Gauge32
_EipSvcDhcpMsDiskIoRead_Object = MibScalar
eipSvcDhcpMsDiskIoRead = _EipSvcDhcpMsDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 7, 4),
    _EipSvcDhcpMsDiskIoRead_Type()
)
eipSvcDhcpMsDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpMsDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpMsDiskIoRead.setUnits("blocks")
_EipSvcDhcpMsDiskIoWrite_Type = Gauge32
_EipSvcDhcpMsDiskIoWrite_Object = MibScalar
eipSvcDhcpMsDiskIoWrite = _EipSvcDhcpMsDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 7, 5),
    _EipSvcDhcpMsDiskIoWrite_Type()
)
eipSvcDhcpMsDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDhcpMsDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDhcpMsDiskIoWrite.setUnits("blocks")
_EipSvcDns_ObjectIdentity = ObjectIdentity
eipSvcDns = _EipSvcDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 8)
)


class _EipSvcDnsStatus_Type(Integer32):
    """Custom type eipSvcDnsStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcDnsStatus_Type.__name__ = "Integer32"
_EipSvcDnsStatus_Object = MibScalar
eipSvcDnsStatus = _EipSvcDnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 8, 1),
    _EipSvcDnsStatus_Type()
)
eipSvcDnsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDnsStatus.setStatus("current")
_EipSvcDnsCpu_Type = Gauge32
_EipSvcDnsCpu_Object = MibScalar
eipSvcDnsCpu = _EipSvcDnsCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 8, 2),
    _EipSvcDnsCpu_Type()
)
eipSvcDnsCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDnsCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDnsCpu.setUnits("%")
_EipSvcDnsMem_Type = Gauge32
_EipSvcDnsMem_Object = MibScalar
eipSvcDnsMem = _EipSvcDnsMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 8, 3),
    _EipSvcDnsMem_Type()
)
eipSvcDnsMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDnsMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDnsMem.setUnits("Kbytes")
_EipSvcDnsDiskIoRead_Type = Gauge32
_EipSvcDnsDiskIoRead_Object = MibScalar
eipSvcDnsDiskIoRead = _EipSvcDnsDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 8, 4),
    _EipSvcDnsDiskIoRead_Type()
)
eipSvcDnsDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDnsDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDnsDiskIoRead.setUnits("blocks")
_EipSvcDnsDiskIoWrite_Type = Gauge32
_EipSvcDnsDiskIoWrite_Object = MibScalar
eipSvcDnsDiskIoWrite = _EipSvcDnsDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 8, 5),
    _EipSvcDnsDiskIoWrite_Type()
)
eipSvcDnsDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDnsDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDnsDiskIoWrite.setUnits("blocks")


class _EipSvcDnsEngine_Type(OctetString):
    """Custom type eipSvcDnsEngine based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EipSvcDnsEngine_Type.__name__ = "OctetString"
_EipSvcDnsEngine_Object = MibScalar
eipSvcDnsEngine = _EipSvcDnsEngine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 8, 6),
    _EipSvcDnsEngine_Type()
)
eipSvcDnsEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcDnsEngine.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcDnsEngine.setUnits("blocks")
_EipSvcGuardian_ObjectIdentity = ObjectIdentity
eipSvcGuardian = _EipSvcGuardian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 9)
)


class _EipSvcGuardianStatus_Type(Integer32):
    """Custom type eipSvcGuardianStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcGuardianStatus_Type.__name__ = "Integer32"
_EipSvcGuardianStatus_Object = MibScalar
eipSvcGuardianStatus = _EipSvcGuardianStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 9, 1),
    _EipSvcGuardianStatus_Type()
)
eipSvcGuardianStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcGuardianStatus.setStatus("current")
_EipSvcGuardianCpu_Type = Gauge32
_EipSvcGuardianCpu_Object = MibScalar
eipSvcGuardianCpu = _EipSvcGuardianCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 9, 2),
    _EipSvcGuardianCpu_Type()
)
eipSvcGuardianCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcGuardianCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcGuardianCpu.setUnits("%")
_EipSvcGuardianMem_Type = Gauge32
_EipSvcGuardianMem_Object = MibScalar
eipSvcGuardianMem = _EipSvcGuardianMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 9, 3),
    _EipSvcGuardianMem_Type()
)
eipSvcGuardianMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcGuardianMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcGuardianMem.setUnits("Kbytes")
_EipSvcGuardianDiskIoRead_Type = Gauge32
_EipSvcGuardianDiskIoRead_Object = MibScalar
eipSvcGuardianDiskIoRead = _EipSvcGuardianDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 9, 4),
    _EipSvcGuardianDiskIoRead_Type()
)
eipSvcGuardianDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcGuardianDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcGuardianDiskIoRead.setUnits("blocks")
_EipSvcGuardianDiskIoWrite_Type = Gauge32
_EipSvcGuardianDiskIoWrite_Object = MibScalar
eipSvcGuardianDiskIoWrite = _EipSvcGuardianDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 9, 5),
    _EipSvcGuardianDiskIoWrite_Type()
)
eipSvcGuardianDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcGuardianDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcGuardianDiskIoWrite.setUnits("blocks")
_EipSvcQuagga_ObjectIdentity = ObjectIdentity
eipSvcQuagga = _EipSvcQuagga_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 10)
)


class _EipSvcQuaggaStatus_Type(Integer32):
    """Custom type eipSvcQuaggaStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcQuaggaStatus_Type.__name__ = "Integer32"
_EipSvcQuaggaStatus_Object = MibScalar
eipSvcQuaggaStatus = _EipSvcQuaggaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 10, 1),
    _EipSvcQuaggaStatus_Type()
)
eipSvcQuaggaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcQuaggaStatus.setStatus("current")
_EipSvcQuaggaCpu_Type = Gauge32
_EipSvcQuaggaCpu_Object = MibScalar
eipSvcQuaggaCpu = _EipSvcQuaggaCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 10, 2),
    _EipSvcQuaggaCpu_Type()
)
eipSvcQuaggaCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcQuaggaCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcQuaggaCpu.setUnits("%")
_EipSvcQuaggaMem_Type = Gauge32
_EipSvcQuaggaMem_Object = MibScalar
eipSvcQuaggaMem = _EipSvcQuaggaMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 10, 3),
    _EipSvcQuaggaMem_Type()
)
eipSvcQuaggaMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcQuaggaMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcQuaggaMem.setUnits("Kbytes")
_EipSvcQuaggaDiskIoRead_Type = Gauge32
_EipSvcQuaggaDiskIoRead_Object = MibScalar
eipSvcQuaggaDiskIoRead = _EipSvcQuaggaDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 10, 4),
    _EipSvcQuaggaDiskIoRead_Type()
)
eipSvcQuaggaDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcQuaggaDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcQuaggaDiskIoRead.setUnits("blocks")
_EipSvcQuaggaDiskIoWrite_Type = Gauge32
_EipSvcQuaggaDiskIoWrite_Object = MibScalar
eipSvcQuaggaDiskIoWrite = _EipSvcQuaggaDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 10, 5),
    _EipSvcQuaggaDiskIoWrite_Type()
)
eipSvcQuaggaDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcQuaggaDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcQuaggaDiskIoWrite.setUnits("blocks")
_EipSvcNtp_ObjectIdentity = ObjectIdentity
eipSvcNtp = _EipSvcNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 11)
)


class _EipSvcNtpStatus_Type(Integer32):
    """Custom type eipSvcNtpStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcNtpStatus_Type.__name__ = "Integer32"
_EipSvcNtpStatus_Object = MibScalar
eipSvcNtpStatus = _EipSvcNtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 11, 1),
    _EipSvcNtpStatus_Type()
)
eipSvcNtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcNtpStatus.setStatus("current")
_EipSvcNtpCpu_Type = Gauge32
_EipSvcNtpCpu_Object = MibScalar
eipSvcNtpCpu = _EipSvcNtpCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 11, 2),
    _EipSvcNtpCpu_Type()
)
eipSvcNtpCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcNtpCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcNtpCpu.setUnits("%")
_EipSvcNtpMem_Type = Gauge32
_EipSvcNtpMem_Object = MibScalar
eipSvcNtpMem = _EipSvcNtpMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 11, 3),
    _EipSvcNtpMem_Type()
)
eipSvcNtpMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcNtpMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcNtpMem.setUnits("Kbytes")
_EipSvcNtpDiskIoRead_Type = Gauge32
_EipSvcNtpDiskIoRead_Object = MibScalar
eipSvcNtpDiskIoRead = _EipSvcNtpDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 11, 4),
    _EipSvcNtpDiskIoRead_Type()
)
eipSvcNtpDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcNtpDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcNtpDiskIoRead.setUnits("blocks")
_EipSvcNtpDiskIoWrite_Type = Gauge32
_EipSvcNtpDiskIoWrite_Object = MibScalar
eipSvcNtpDiskIoWrite = _EipSvcNtpDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 11, 5),
    _EipSvcNtpDiskIoWrite_Type()
)
eipSvcNtpDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcNtpDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcNtpDiskIoWrite.setUnits("blocks")
_EipSvcTftp_ObjectIdentity = ObjectIdentity
eipSvcTftp = _EipSvcTftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 12)
)


class _EipSvcTftpStatus_Type(Integer32):
    """Custom type eipSvcTftpStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcTftpStatus_Type.__name__ = "Integer32"
_EipSvcTftpStatus_Object = MibScalar
eipSvcTftpStatus = _EipSvcTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 12, 1),
    _EipSvcTftpStatus_Type()
)
eipSvcTftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcTftpStatus.setStatus("current")
_EipSvcTftpCpu_Type = Gauge32
_EipSvcTftpCpu_Object = MibScalar
eipSvcTftpCpu = _EipSvcTftpCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 12, 2),
    _EipSvcTftpCpu_Type()
)
eipSvcTftpCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcTftpCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcTftpCpu.setUnits("%")
_EipSvcTftpMem_Type = Gauge32
_EipSvcTftpMem_Object = MibScalar
eipSvcTftpMem = _EipSvcTftpMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 12, 3),
    _EipSvcTftpMem_Type()
)
eipSvcTftpMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcTftpMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcTftpMem.setUnits("Kbytes")
_EipSvcTftpDiskIoRead_Type = Gauge32
_EipSvcTftpDiskIoRead_Object = MibScalar
eipSvcTftpDiskIoRead = _EipSvcTftpDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 12, 4),
    _EipSvcTftpDiskIoRead_Type()
)
eipSvcTftpDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcTftpDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcTftpDiskIoRead.setUnits("blocks")
_EipSvcTftpDiskIoWrite_Type = Gauge32
_EipSvcTftpDiskIoWrite_Object = MibScalar
eipSvcTftpDiskIoWrite = _EipSvcTftpDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 12, 5),
    _EipSvcTftpDiskIoWrite_Type()
)
eipSvcTftpDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcTftpDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcTftpDiskIoWrite.setUnits("blocks")
_EipSvcSnmp_ObjectIdentity = ObjectIdentity
eipSvcSnmp = _EipSvcSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 13)
)


class _EipSvcSnmpStatus_Type(Integer32):
    """Custom type eipSvcSnmpStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcSnmpStatus_Type.__name__ = "Integer32"
_EipSvcSnmpStatus_Object = MibScalar
eipSvcSnmpStatus = _EipSvcSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 13, 1),
    _EipSvcSnmpStatus_Type()
)
eipSvcSnmpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSnmpStatus.setStatus("current")
_EipSvcSnmpCpu_Type = Gauge32
_EipSvcSnmpCpu_Object = MibScalar
eipSvcSnmpCpu = _EipSvcSnmpCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 13, 2),
    _EipSvcSnmpCpu_Type()
)
eipSvcSnmpCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSnmpCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSnmpCpu.setUnits("%")
_EipSvcSnmpMem_Type = Gauge32
_EipSvcSnmpMem_Object = MibScalar
eipSvcSnmpMem = _EipSvcSnmpMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 13, 3),
    _EipSvcSnmpMem_Type()
)
eipSvcSnmpMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSnmpMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSnmpMem.setUnits("Kbytes")
_EipSvcSnmpDiskIoRead_Type = Gauge32
_EipSvcSnmpDiskIoRead_Object = MibScalar
eipSvcSnmpDiskIoRead = _EipSvcSnmpDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 13, 4),
    _EipSvcSnmpDiskIoRead_Type()
)
eipSvcSnmpDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSnmpDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSnmpDiskIoRead.setUnits("blocks")
_EipSvcSnmpDiskIoWrite_Type = Gauge32
_EipSvcSnmpDiskIoWrite_Object = MibScalar
eipSvcSnmpDiskIoWrite = _EipSvcSnmpDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 13, 5),
    _EipSvcSnmpDiskIoWrite_Type()
)
eipSvcSnmpDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSnmpDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSnmpDiskIoWrite.setUnits("blocks")
_EipSvcSendmail_ObjectIdentity = ObjectIdentity
eipSvcSendmail = _EipSvcSendmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 14)
)


class _EipSvcSendmailStatus_Type(Integer32):
    """Custom type eipSvcSendmailStatus based on Integer32"""
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
        *(("disabled", 0),
          ("running", 1),
          ("misconfigured", 2),
          ("failed", 3))
    )


_EipSvcSendmailStatus_Type.__name__ = "Integer32"
_EipSvcSendmailStatus_Object = MibScalar
eipSvcSendmailStatus = _EipSvcSendmailStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 14, 1),
    _EipSvcSendmailStatus_Type()
)
eipSvcSendmailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSendmailStatus.setStatus("current")
_EipSvcSendmailCpu_Type = Gauge32
_EipSvcSendmailCpu_Object = MibScalar
eipSvcSendmailCpu = _EipSvcSendmailCpu_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 14, 2),
    _EipSvcSendmailCpu_Type()
)
eipSvcSendmailCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSendmailCpu.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSendmailCpu.setUnits("%")
_EipSvcSendmailMem_Type = Gauge32
_EipSvcSendmailMem_Object = MibScalar
eipSvcSendmailMem = _EipSvcSendmailMem_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 14, 3),
    _EipSvcSendmailMem_Type()
)
eipSvcSendmailMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSendmailMem.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSendmailMem.setUnits("Kbytes")
_EipSvcSendmailDiskIoRead_Type = Gauge32
_EipSvcSendmailDiskIoRead_Object = MibScalar
eipSvcSendmailDiskIoRead = _EipSvcSendmailDiskIoRead_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 14, 4),
    _EipSvcSendmailDiskIoRead_Type()
)
eipSvcSendmailDiskIoRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSendmailDiskIoRead.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSendmailDiskIoRead.setUnits("blocks")
_EipSvcSendmailDiskIoWrite_Type = Gauge32
_EipSvcSendmailDiskIoWrite_Object = MibScalar
eipSvcSendmailDiskIoWrite = _EipSvcSendmailDiskIoWrite_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 14, 5),
    _EipSvcSendmailDiskIoWrite_Type()
)
eipSvcSendmailDiskIoWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSendmailDiskIoWrite.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSendmailDiskIoWrite.setUnits("blocks")
_EipSvcSendmailQueueSize_Type = Integer32
_EipSvcSendmailQueueSize_Object = MibScalar
eipSvcSendmailQueueSize = _EipSvcSendmailQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 14, 6),
    _EipSvcSendmailQueueSize_Type()
)
eipSvcSendmailQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSvcSendmailQueueSize.setStatus("current")
if mibBuilder.loadTexts:
    eipSvcSendmailQueueSize.setUnits("messages")
_EipSds_ObjectIdentity = ObjectIdentity
eipSds = _EipSds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17)
)
_EipSdsVersion_ObjectIdentity = ObjectIdentity
eipSdsVersion = _EipSdsVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17, 1)
)


class _EipSdsVersionOs_Type(Integer32):
    """Custom type eipSdsVersionOs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("i386", 0),
          ("amd64", 1))
    )


_EipSdsVersionOs_Type.__name__ = "Integer32"
_EipSdsVersionOs_Object = MibScalar
eipSdsVersionOs = _EipSdsVersionOs_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17, 1, 1),
    _EipSdsVersionOs_Type()
)
eipSdsVersionOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSdsVersionOs.setStatus("current")


class _EipSdsVersionNumber_Type(OctetString):
    """Custom type eipSdsVersionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EipSdsVersionNumber_Type.__name__ = "OctetString"
_EipSdsVersionNumber_Object = MibScalar
eipSdsVersionNumber = _EipSdsVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17, 1, 2),
    _EipSdsVersionNumber_Type()
)
eipSdsVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSdsVersionNumber.setStatus("current")


class _EipSdsVersionDate_Type(OctetString):
    """Custom type eipSdsVersionDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_EipSdsVersionDate_Type.__name__ = "OctetString"
_EipSdsVersionDate_Object = MibScalar
eipSdsVersionDate = _EipSdsVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17, 1, 3),
    _EipSdsVersionDate_Type()
)
eipSdsVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSdsVersionDate.setStatus("current")
_EipSdsMember_ObjectIdentity = ObjectIdentity
eipSdsMember = _EipSdsMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17, 2)
)


class _EipSdsMemberRole_Type(Integer32):
    """Custom type eipSdsMemberRole based on Integer32"""
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
        *(("standalone", 0),
          ("master", 1),
          ("hotStandby", 2),
          ("masterRecovered", 3))
    )


_EipSdsMemberRole_Type.__name__ = "Integer32"
_EipSdsMemberRole_Object = MibScalar
eipSdsMemberRole = _EipSdsMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17, 2, 1),
    _EipSdsMemberRole_Type()
)
eipSdsMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSdsMemberRole.setStatus("current")


class _EipSdsMemberStatus_Type(Integer32):
    """Custom type eipSdsMemberStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("notConfigured", 1),
          ("upgrading", 2),
          ("initStandby", 3),
          ("invalidCredentials", 4),
          ("remoteManaged", 5),
          ("timeout", 6),
          ("splitBrain", 7),
          ("replicationStopped", 8))
    )


_EipSdsMemberStatus_Type.__name__ = "Integer32"
_EipSdsMemberStatus_Object = MibScalar
eipSdsMemberStatus = _EipSdsMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 17, 2, 2),
    _EipSdsMemberStatus_Type()
)
eipSdsMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipSdsMemberStatus.setStatus("current")
_EipCompliances_ObjectIdentity = ObjectIdentity
eipCompliances = _EipCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 1000)
)

# Managed Objects groups

eipNetStatIn = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 201)
)
eipNetStatIn.setObjects(
      *(("EIP-MON-MIB", "eipNetStatHttpInOctets"),
        ("EIP-MON-MIB", "eipNetStatHttpInPkts"),
        ("EIP-MON-MIB", "eipNetStatDnsInOctets"),
        ("EIP-MON-MIB", "eipNetStatDnsInPkts"),
        ("EIP-MON-MIB", "eipNetStatDhcpInOctets"),
        ("EIP-MON-MIB", "eipNetStatDhcpInPkts"),
        ("EIP-MON-MIB", "eipNetStatDbInOctets"),
        ("EIP-MON-MIB", "eipNetStatDbInPkts"),
        ("EIP-MON-MIB", "eipNetStatSnmpInOctets"),
        ("EIP-MON-MIB", "eipNetStatSnmpInPkts"))
)
if mibBuilder.loadTexts:
    eipNetStatIn.setStatus("current")

eipNetStatOut = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2440, 1, 15, 202)
)
eipNetStatOut.setObjects(
      *(("EIP-MON-MIB", "eipNetStatHttpOutOctets"),
        ("EIP-MON-MIB", "eipNetStatHttpOutPkts"),
        ("EIP-MON-MIB", "eipNetStatDnsOutOctets"),
        ("EIP-MON-MIB", "eipNetStatDnsOutPkts"),
        ("EIP-MON-MIB", "eipNetStatDhcpOutOctets"),
        ("EIP-MON-MIB", "eipNetStatDhcpOutPkts"),
        ("EIP-MON-MIB", "eipNetStatDbOutOctets"),
        ("EIP-MON-MIB", "eipNetStatDbOutPkts"),
        ("EIP-MON-MIB", "eipNetStatSnmpOutPkts"),
        ("EIP-MON-MIB", "eipNetStatSnmpOutPkts"))
)
if mibBuilder.loadTexts:
    eipNetStatOut.setStatus("current")

eipSvcStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 201)
)
eipSvcStatus.setObjects(
      *(("EIP-MON-MIB", "eipSvcSyslogStatus"),
        ("EIP-MON-MIB", "eipSvcSshStatus"),
        ("EIP-MON-MIB", "eipSvcApacheStatus"),
        ("EIP-MON-MIB", "eipSvcIpmServerStatus"),
        ("EIP-MON-MIB", "eipSvcDatabaseStatus"),
        ("EIP-MON-MIB", "eipSvcDhcpStatus"),
        ("EIP-MON-MIB", "eipSvcDhcpMsStatus"),
        ("EIP-MON-MIB", "eipSvcDnsStatus"),
        ("EIP-MON-MIB", "eipSvcGuardianStatus"),
        ("EIP-MON-MIB", "eipSvcQuaggaStatus"),
        ("EIP-MON-MIB", "eipSvcNtpStatus"),
        ("EIP-MON-MIB", "eipSvcTftpStatus"),
        ("EIP-MON-MIB", "eipSvcSnmpStatus"),
        ("EIP-MON-MIB", "eipSvcSendmailStatus"))
)
if mibBuilder.loadTexts:
    eipSvcStatus.setStatus("current")

eipSvcCpu = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 202)
)
eipSvcCpu.setObjects(
      *(("EIP-MON-MIB", "eipSvcSyslogCpu"),
        ("EIP-MON-MIB", "eipSvcSshCpu"),
        ("EIP-MON-MIB", "eipSvcApacheCpu"),
        ("EIP-MON-MIB", "eipSvcIpmServerCpu"),
        ("EIP-MON-MIB", "eipSvcDatabaseCpu"),
        ("EIP-MON-MIB", "eipSvcDhcpCpu"),
        ("EIP-MON-MIB", "eipSvcDhcpMsCpu"),
        ("EIP-MON-MIB", "eipSvcDnsCpu"),
        ("EIP-MON-MIB", "eipSvcGuardianCpu"),
        ("EIP-MON-MIB", "eipSvcQuaggaCpu"),
        ("EIP-MON-MIB", "eipSvcNtpCpu"),
        ("EIP-MON-MIB", "eipSvcTftpCpu"),
        ("EIP-MON-MIB", "eipSvcSnmpCpu"),
        ("EIP-MON-MIB", "eipSvcSendmailCpu"))
)
if mibBuilder.loadTexts:
    eipSvcCpu.setStatus("current")

eipSvcMem = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 203)
)
eipSvcMem.setObjects(
      *(("EIP-MON-MIB", "eipSvcSyslogMem"),
        ("EIP-MON-MIB", "eipSvcSshMem"),
        ("EIP-MON-MIB", "eipSvcApacheMem"),
        ("EIP-MON-MIB", "eipSvcIpmServerMem"),
        ("EIP-MON-MIB", "eipSvcDatabaseMem"),
        ("EIP-MON-MIB", "eipSvcDhcpMem"),
        ("EIP-MON-MIB", "eipSvcDhcpMsMem"),
        ("EIP-MON-MIB", "eipSvcDnsMem"),
        ("EIP-MON-MIB", "eipSvcGuardianMem"),
        ("EIP-MON-MIB", "eipSvcQuaggaMem"),
        ("EIP-MON-MIB", "eipSvcNtpMem"),
        ("EIP-MON-MIB", "eipSvcTftpMem"),
        ("EIP-MON-MIB", "eipSvcSnmpMem"),
        ("EIP-MON-MIB", "eipSvcSendmailMem"))
)
if mibBuilder.loadTexts:
    eipSvcMem.setStatus("current")

eipSvcDiskIoRead = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 204)
)
eipSvcDiskIoRead.setObjects(
      *(("EIP-MON-MIB", "eipSvcSyslogDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcSshDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcApacheDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcIpmServerDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcDatabaseDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcDhcpDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcDhcpMsDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcDnsDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcGuardianDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcQuaggaDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcNtpDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcTftpDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcSnmpDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcSendmailDiskIoRead"))
)
if mibBuilder.loadTexts:
    eipSvcDiskIoRead.setStatus("current")

eipSvcDiskIoWrite = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2440, 1, 16, 205)
)
eipSvcDiskIoWrite.setObjects(
      *(("EIP-MON-MIB", "eipSvcSyslogDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcSshDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcApacheDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcIpmServerDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcDatabaseDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcDhcpDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcDhcpMsDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcDnsDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcGuardianDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcQuaggaDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcNtpDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcTftpDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcSnmpDiskIoWrite"),
        ("EIP-MON-MIB", "eipSvcSendmailDiskIoWrite"))
)
if mibBuilder.loadTexts:
    eipSvcDiskIoWrite.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

eipMainCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2440, 1, 1000, 1)
)
eipMainCompliance.setObjects(
      *(("EIP-MON-MIB", "eipNetStatIn"),
        ("EIP-MON-MIB", "eipNetStatOut"),
        ("EIP-MON-MIB", "eipSvcStatus"),
        ("EIP-MON-MIB", "eipSvcCpu"),
        ("EIP-MON-MIB", "eipSvcMem"),
        ("EIP-MON-MIB", "eipSvcDiskIoRead"),
        ("EIP-MON-MIB", "eipSvcDiskIoWrite"))
)
if mibBuilder.loadTexts:
    eipMainCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EIP-MON-MIB",
    **{"eip": eip,
       "products": products,
       "eipHw": eipHw,
       "eipHwAppliance": eipHwAppliance,
       "eipHwApplianceModel": eipHwApplianceModel,
       "eipHwApplianceSerial": eipHwApplianceSerial,
       "eipHwApplianceBiosVersion": eipHwApplianceBiosVersion,
       "eipHwHdd": eipHwHdd,
       "eipHwHddFreeRoot": eipHwHddFreeRoot,
       "eipHwHddUsedRootPercent": eipHwHddUsedRootPercent,
       "eipHwHddFreeTmp": eipHwHddFreeTmp,
       "eipHwHddUsedTmpPercent": eipHwHddUsedTmpPercent,
       "eipHwHddFreeVar": eipHwHddFreeVar,
       "eipHwHddUsedVarPercent": eipHwHddUsedVarPercent,
       "eipHwHddFreeData1": eipHwHddFreeData1,
       "eipHwHddUsedData1Percent": eipHwHddUsedData1Percent,
       "eipHwHddUsedSwap": eipHwHddUsedSwap,
       "eipHwHddUsedSwapPercent": eipHwHddUsedSwapPercent,
       "eipHwHddIoLoad": eipHwHddIoLoad,
       "eipHwTemp": eipHwTemp,
       "eipHwTempCpu": eipHwTempCpu,
       "eipHwTempCpuCoreMax": eipHwTempCpuCoreMax,
       "eipHwTempCpuCoreMin": eipHwTempCpuCoreMin,
       "eipHwTempInlet": eipHwTempInlet,
       "eipHwTempBaseboard": eipHwTempBaseboard,
       "eipHwTempRaidController": eipHwTempRaidController,
       "eipHwFan": eipHwFan,
       "eipHwFan1Speed": eipHwFan1Speed,
       "eipHwFan2Speed": eipHwFan2Speed,
       "eipHwFan3Speed": eipHwFan3Speed,
       "eipHwFan4Speed": eipHwFan4Speed,
       "eipHwFan5Speed": eipHwFan5Speed,
       "eipHwFan6Speed": eipHwFan6Speed,
       "eipHwFan7Speed": eipHwFan7Speed,
       "eipHwFan8Speed": eipHwFan8Speed,
       "eipHwPsu": eipHwPsu,
       "eipHwPsuRedundancy": eipHwPsuRedundancy,
       "eipHwPsu1Status": eipHwPsu1Status,
       "eipHwPsu2Status": eipHwPsu2Status,
       "eipHwPower": eipHwPower,
       "eipHwPowerInstant": eipHwPowerInstant,
       "eipHwPowerCumulative": eipHwPowerCumulative,
       "eipHwPowerPeak": eipHwPowerPeak,
       "eipHwPowerPeakAmperage": eipHwPowerPeakAmperage,
       "eipHwRaid": eipHwRaid,
       "eipHwRaidController": eipHwRaidController,
       "eipHwRaidStatus": eipHwRaidStatus,
       "eipHwRaidDisks": eipHwRaidDisks,
       "eipHwRaidDisksCritical": eipHwRaidDisksCritical,
       "eipHwRaidDisksFailed": eipHwRaidDisksFailed,
       "eipHwRaidBbuStatus": eipHwRaidBbuStatus,
       "eipHwRaidBbuCharge": eipHwRaidBbuCharge,
       "eipHwCpu": eipHwCpu,
       "eipHwCpuLoadInt": eipHwCpuLoadInt,
       "eipHwCpuCoreNumber": eipHwCpuCoreNumber,
       "eipHwMem": eipHwMem,
       "eipHwMemUsed": eipHwMemUsed,
       "eipHwChassis": eipHwChassis,
       "eipHwChassisIntrusion": eipHwChassisIntrusion,
       "eipNet": eipNet,
       "eipNetCfg": eipNetCfg,
       "eipNetCarp": eipNetCarp,
       "eipNetCarpIf": eipNetCarpIf,
       "eipNetCarpIfNumber": eipNetCarpIfNumber,
       "eipNetCarpIfTable": eipNetCarpIfTable,
       "eipNetCarpIfEntry": eipNetCarpIfEntry,
       "eipNetCarpIfIndex": eipNetCarpIfIndex,
       "eipNetCarpIfDescr": eipNetCarpIfDescr,
       "eipNetCarpIfVhid": eipNetCarpIfVhid,
       "eipNetCarpIfDev": eipNetCarpIfDev,
       "eipNetCarpIfAdvbase": eipNetCarpIfAdvbase,
       "eipNetCarpIfAdvskew": eipNetCarpIfAdvskew,
       "eipNetCarpIfState": eipNetCarpIfState,
       "eipNetLagg": eipNetLagg,
       "eipNetLaggStatus": eipNetLaggStatus,
       "eipNetStat": eipNetStat,
       "eipNetStatHttp": eipNetStatHttp,
       "eipNetStatHttpInOctets": eipNetStatHttpInOctets,
       "eipNetStatHttpInPkts": eipNetStatHttpInPkts,
       "eipNetStatHttpOutOctets": eipNetStatHttpOutOctets,
       "eipNetStatHttpOutPkts": eipNetStatHttpOutPkts,
       "eipNetStatDns": eipNetStatDns,
       "eipNetStatDnsInOctets": eipNetStatDnsInOctets,
       "eipNetStatDnsInPkts": eipNetStatDnsInPkts,
       "eipNetStatDnsOutOctets": eipNetStatDnsOutOctets,
       "eipNetStatDnsOutPkts": eipNetStatDnsOutPkts,
       "eipNetStatDhcp": eipNetStatDhcp,
       "eipNetStatDhcpInOctets": eipNetStatDhcpInOctets,
       "eipNetStatDhcpInPkts": eipNetStatDhcpInPkts,
       "eipNetStatDhcpOutOctets": eipNetStatDhcpOutOctets,
       "eipNetStatDhcpOutPkts": eipNetStatDhcpOutPkts,
       "eipNetStatDb": eipNetStatDb,
       "eipNetStatDbInOctets": eipNetStatDbInOctets,
       "eipNetStatDbInPkts": eipNetStatDbInPkts,
       "eipNetStatDbOutOctets": eipNetStatDbOutOctets,
       "eipNetStatDbOutPkts": eipNetStatDbOutPkts,
       "eipNetStatSnmp": eipNetStatSnmp,
       "eipNetStatSnmpInOctets": eipNetStatSnmpInOctets,
       "eipNetStatSnmpInPkts": eipNetStatSnmpInPkts,
       "eipNetStatSnmpOutOctets": eipNetStatSnmpOutOctets,
       "eipNetStatSnmpOutPkts": eipNetStatSnmpOutPkts,
       "eipNetStatIn": eipNetStatIn,
       "eipNetStatOut": eipNetStatOut,
       "eipSvc": eipSvc,
       "eipSvcSyslog": eipSvcSyslog,
       "eipSvcSyslogStatus": eipSvcSyslogStatus,
       "eipSvcSyslogCpu": eipSvcSyslogCpu,
       "eipSvcSyslogMem": eipSvcSyslogMem,
       "eipSvcSyslogDiskIoRead": eipSvcSyslogDiskIoRead,
       "eipSvcSyslogDiskIoWrite": eipSvcSyslogDiskIoWrite,
       "eipSvcSsh": eipSvcSsh,
       "eipSvcSshStatus": eipSvcSshStatus,
       "eipSvcSshCpu": eipSvcSshCpu,
       "eipSvcSshMem": eipSvcSshMem,
       "eipSvcSshDiskIoRead": eipSvcSshDiskIoRead,
       "eipSvcSshDiskIoWrite": eipSvcSshDiskIoWrite,
       "eipSvcSshConnections": eipSvcSshConnections,
       "eipSvcApache": eipSvcApache,
       "eipSvcApacheStatus": eipSvcApacheStatus,
       "eipSvcApacheCpu": eipSvcApacheCpu,
       "eipSvcApacheMem": eipSvcApacheMem,
       "eipSvcApacheDiskIoRead": eipSvcApacheDiskIoRead,
       "eipSvcApacheDiskIoWrite": eipSvcApacheDiskIoWrite,
       "eipSvcApacheConnections": eipSvcApacheConnections,
       "eipSvcIpmServer": eipSvcIpmServer,
       "eipSvcIpmServerStatus": eipSvcIpmServerStatus,
       "eipSvcIpmServerCpu": eipSvcIpmServerCpu,
       "eipSvcIpmServerMem": eipSvcIpmServerMem,
       "eipSvcIpmServerDiskIoRead": eipSvcIpmServerDiskIoRead,
       "eipSvcIpmServerDiskIoWrite": eipSvcIpmServerDiskIoWrite,
       "eipSvcIpmServerUserSessions": eipSvcIpmServerUserSessions,
       "eipSvcIpmServerThreads": eipSvcIpmServerThreads,
       "eipSvcIpmServerDbQueries": eipSvcIpmServerDbQueries,
       "eipSvcDatabase": eipSvcDatabase,
       "eipSvcDatabaseStatus": eipSvcDatabaseStatus,
       "eipSvcDatabaseCpu": eipSvcDatabaseCpu,
       "eipSvcDatabaseMem": eipSvcDatabaseMem,
       "eipSvcDatabaseDiskIoRead": eipSvcDatabaseDiskIoRead,
       "eipSvcDatabaseDiskIoWrite": eipSvcDatabaseDiskIoWrite,
       "eipSvcDatabaseReplicationStatus": eipSvcDatabaseReplicationStatus,
       "eipSvcDatabaseReplicationOffset": eipSvcDatabaseReplicationOffset,
       "eipSvcDatabaseReplicationLastReplay": eipSvcDatabaseReplicationLastReplay,
       "eipSvcDatabaseBackends": eipSvcDatabaseBackends,
       "eipSvcDatabaseDeadlocks": eipSvcDatabaseDeadlocks,
       "eipSvcDatabaseBloat": eipSvcDatabaseBloat,
       "eipSvcDhcp": eipSvcDhcp,
       "eipSvcDhcpStatus": eipSvcDhcpStatus,
       "eipSvcDhcpCpu": eipSvcDhcpCpu,
       "eipSvcDhcpMem": eipSvcDhcpMem,
       "eipSvcDhcpDiskIoRead": eipSvcDhcpDiskIoRead,
       "eipSvcDhcpDiskIoWrite": eipSvcDhcpDiskIoWrite,
       "eipSvcDhcpFailoverNumber": eipSvcDhcpFailoverNumber,
       "eipSvcDhcpFailoverTable": eipSvcDhcpFailoverTable,
       "eipSvcDhcpFailoverEntry": eipSvcDhcpFailoverEntry,
       "eipSvcDhcpFailoverIndex": eipSvcDhcpFailoverIndex,
       "eipSvcDhcpFailoverName": eipSvcDhcpFailoverName,
       "eipSvcDhcpFailoverStatus": eipSvcDhcpFailoverStatus,
       "eipSvcDhcpMs": eipSvcDhcpMs,
       "eipSvcDhcpMsStatus": eipSvcDhcpMsStatus,
       "eipSvcDhcpMsCpu": eipSvcDhcpMsCpu,
       "eipSvcDhcpMsMem": eipSvcDhcpMsMem,
       "eipSvcDhcpMsDiskIoRead": eipSvcDhcpMsDiskIoRead,
       "eipSvcDhcpMsDiskIoWrite": eipSvcDhcpMsDiskIoWrite,
       "eipSvcDns": eipSvcDns,
       "eipSvcDnsStatus": eipSvcDnsStatus,
       "eipSvcDnsCpu": eipSvcDnsCpu,
       "eipSvcDnsMem": eipSvcDnsMem,
       "eipSvcDnsDiskIoRead": eipSvcDnsDiskIoRead,
       "eipSvcDnsDiskIoWrite": eipSvcDnsDiskIoWrite,
       "eipSvcDnsEngine": eipSvcDnsEngine,
       "eipSvcGuardian": eipSvcGuardian,
       "eipSvcGuardianStatus": eipSvcGuardianStatus,
       "eipSvcGuardianCpu": eipSvcGuardianCpu,
       "eipSvcGuardianMem": eipSvcGuardianMem,
       "eipSvcGuardianDiskIoRead": eipSvcGuardianDiskIoRead,
       "eipSvcGuardianDiskIoWrite": eipSvcGuardianDiskIoWrite,
       "eipSvcQuagga": eipSvcQuagga,
       "eipSvcQuaggaStatus": eipSvcQuaggaStatus,
       "eipSvcQuaggaCpu": eipSvcQuaggaCpu,
       "eipSvcQuaggaMem": eipSvcQuaggaMem,
       "eipSvcQuaggaDiskIoRead": eipSvcQuaggaDiskIoRead,
       "eipSvcQuaggaDiskIoWrite": eipSvcQuaggaDiskIoWrite,
       "eipSvcNtp": eipSvcNtp,
       "eipSvcNtpStatus": eipSvcNtpStatus,
       "eipSvcNtpCpu": eipSvcNtpCpu,
       "eipSvcNtpMem": eipSvcNtpMem,
       "eipSvcNtpDiskIoRead": eipSvcNtpDiskIoRead,
       "eipSvcNtpDiskIoWrite": eipSvcNtpDiskIoWrite,
       "eipSvcTftp": eipSvcTftp,
       "eipSvcTftpStatus": eipSvcTftpStatus,
       "eipSvcTftpCpu": eipSvcTftpCpu,
       "eipSvcTftpMem": eipSvcTftpMem,
       "eipSvcTftpDiskIoRead": eipSvcTftpDiskIoRead,
       "eipSvcTftpDiskIoWrite": eipSvcTftpDiskIoWrite,
       "eipSvcSnmp": eipSvcSnmp,
       "eipSvcSnmpStatus": eipSvcSnmpStatus,
       "eipSvcSnmpCpu": eipSvcSnmpCpu,
       "eipSvcSnmpMem": eipSvcSnmpMem,
       "eipSvcSnmpDiskIoRead": eipSvcSnmpDiskIoRead,
       "eipSvcSnmpDiskIoWrite": eipSvcSnmpDiskIoWrite,
       "eipSvcSendmail": eipSvcSendmail,
       "eipSvcSendmailStatus": eipSvcSendmailStatus,
       "eipSvcSendmailCpu": eipSvcSendmailCpu,
       "eipSvcSendmailMem": eipSvcSendmailMem,
       "eipSvcSendmailDiskIoRead": eipSvcSendmailDiskIoRead,
       "eipSvcSendmailDiskIoWrite": eipSvcSendmailDiskIoWrite,
       "eipSvcSendmailQueueSize": eipSvcSendmailQueueSize,
       "eipSvcStatus": eipSvcStatus,
       "eipSvcCpu": eipSvcCpu,
       "eipSvcMem": eipSvcMem,
       "eipSvcDiskIoRead": eipSvcDiskIoRead,
       "eipSvcDiskIoWrite": eipSvcDiskIoWrite,
       "eipSds": eipSds,
       "eipSdsVersion": eipSdsVersion,
       "eipSdsVersionOs": eipSdsVersionOs,
       "eipSdsVersionNumber": eipSdsVersionNumber,
       "eipSdsVersionDate": eipSdsVersionDate,
       "eipSdsMember": eipSdsMember,
       "eipSdsMemberRole": eipSdsMemberRole,
       "eipSdsMemberStatus": eipSdsMemberStatus,
       "eipCompliances": eipCompliances,
       "eipMainCompliance": eipMainCompliance}
)
