# SNMP MIB module (TIMETRA-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-GLOBAL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:13 2025
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

timetraGlobalMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 1)
)
if mibBuilder.loadTexts:
    timetraGlobalMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2012-08-01 00:00",
         "2011-02-01 00:00",
         "2010-02-28 00:00",
         "2009-02-28 00:00",
         "2009-02-01 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-01-20 00:00",
         "2000-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Timetra_ObjectIdentity = ObjectIdentity
timetra = _Timetra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527)
)
_TimetraReg_ObjectIdentity = ObjectIdentity
timetraReg = _TimetraReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1)
)
_TimetraModules_ObjectIdentity = ObjectIdentity
timetraModules = _TimetraModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1)
)
_TimetraSRMIBModules_ObjectIdentity = ObjectIdentity
timetraSRMIBModules = _TimetraSRMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3)
)
_TimetraAirframeMIBModule_ObjectIdentity = ObjectIdentity
timetraAirframeMIBModule = _TimetraAirframeMIBModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 111)
)
_TimetraApplianceMIBModule_ObjectIdentity = ObjectIdentity
timetraApplianceMIBModule = _TimetraApplianceMIBModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 128)
)
_TimetraCapabilityModule_ObjectIdentity = ObjectIdentity
timetraCapabilityModule = _TimetraCapabilityModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4)
)
_Timetra7750CapModule_ObjectIdentity = ObjectIdentity
timetra7750CapModule = _Timetra7750CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 1)
)
_Timetra7450CapModule_ObjectIdentity = ObjectIdentity
timetra7450CapModule = _Timetra7450CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 2)
)
_Timetra7710CapModule_ObjectIdentity = ObjectIdentity
timetra7710CapModule = _Timetra7710CapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 3)
)
_Timetra7750MGCapModule_ObjectIdentity = ObjectIdentity
timetra7750MGCapModule = _Timetra7750MGCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 4)
)
_TimetraSROSCapModule_ObjectIdentity = ObjectIdentity
timetraSROSCapModule = _TimetraSROSCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 5)
)
_TimetraDCCapModule_ObjectIdentity = ObjectIdentity
timetraDCCapModule = _TimetraDCCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 6)
)
_TimetraMGCapModule_ObjectIdentity = ObjectIdentity
timetraMGCapModule = _TimetraMGCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 7)
)
_AlcatelCommonMIBModules_ObjectIdentity = ObjectIdentity
alcatelCommonMIBModules = _AlcatelCommonMIBModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 5)
)
_TimetraServiceRouters_ObjectIdentity = ObjectIdentity
timetraServiceRouters = _TimetraServiceRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3)
)
_TmnxModelSR1Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR1Reg = _TmnxModelSR1Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxModelSR1Reg.setStatus("current")
_TmnxModelSR4Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR4Reg = _TmnxModelSR4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxModelSR4Reg.setStatus("current")
_TmnxModelSR12Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR12Reg = _TmnxModelSR12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxModelSR12Reg.setStatus("current")
_TmnxModelSR7Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR7Reg = _TmnxModelSR7Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxModelSR7Reg.setStatus("current")
_TmnxModelSR6Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR6Reg = _TmnxModelSR6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxModelSR6Reg.setStatus("current")
_TmnxModelSRc12Reg_ObjectIdentity = ObjectIdentity
tmnxModelSRc12Reg = _TmnxModelSRc12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxModelSRc12Reg.setStatus("current")
_TmnxModelSRc4Reg_ObjectIdentity = ObjectIdentity
tmnxModelSRc4Reg = _TmnxModelSRc4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxModelSRc4Reg.setStatus("current")
_TmnxModelSR12EReg_ObjectIdentity = ObjectIdentity
tmnxModelSR12EReg = _TmnxModelSR12EReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxModelSR12EReg.setStatus("current")
_TmnxModelSRa4Reg_ObjectIdentity = ObjectIdentity
tmnxModelSRa4Reg = _TmnxModelSRa4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 9)
)
if mibBuilder.loadTexts:
    tmnxModelSRa4Reg.setStatus("current")
_TmnxModelSRa8Reg_ObjectIdentity = ObjectIdentity
tmnxModelSRa8Reg = _TmnxModelSRa8Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxModelSRa8Reg.setStatus("current")
_TmnxModelSR1eReg_ObjectIdentity = ObjectIdentity
tmnxModelSR1eReg = _TmnxModelSR1eReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 11)
)
if mibBuilder.loadTexts:
    tmnxModelSR1eReg.setStatus("current")
_TmnxModelSR2eReg_ObjectIdentity = ObjectIdentity
tmnxModelSR2eReg = _TmnxModelSR2eReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 12)
)
if mibBuilder.loadTexts:
    tmnxModelSR2eReg.setStatus("current")
_TmnxModelSR3eReg_ObjectIdentity = ObjectIdentity
tmnxModelSR3eReg = _TmnxModelSR3eReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 13)
)
if mibBuilder.loadTexts:
    tmnxModelSR3eReg.setStatus("current")
_TmnxModelSARHmReg_ObjectIdentity = ObjectIdentity
tmnxModelSARHmReg = _TmnxModelSARHmReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 14)
)
if mibBuilder.loadTexts:
    tmnxModelSARHmReg.setStatus("current")
_TmnxModelSR1v2Reg_ObjectIdentity = ObjectIdentity
tmnxModelSR1v2Reg = _TmnxModelSR1v2Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 15)
)
if mibBuilder.loadTexts:
    tmnxModelSR1v2Reg.setStatus("current")
_TmnxModelSR14sReg_ObjectIdentity = ObjectIdentity
tmnxModelSR14sReg = _TmnxModelSR14sReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 16)
)
if mibBuilder.loadTexts:
    tmnxModelSR14sReg.setStatus("current")
_TmnxModelSR7sReg_ObjectIdentity = ObjectIdentity
tmnxModelSR7sReg = _TmnxModelSR7sReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 17)
)
if mibBuilder.loadTexts:
    tmnxModelSR7sReg.setStatus("current")
_TmnxModelSR1sReg_ObjectIdentity = ObjectIdentity
tmnxModelSR1sReg = _TmnxModelSR1sReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 18)
)
if mibBuilder.loadTexts:
    tmnxModelSR1sReg.setStatus("current")
_TmnxModelSR2sReg_ObjectIdentity = ObjectIdentity
tmnxModelSR2sReg = _TmnxModelSR2sReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 19)
)
if mibBuilder.loadTexts:
    tmnxModelSR2sReg.setStatus("current")
_TmnxModelIXRr6Reg_ObjectIdentity = ObjectIdentity
tmnxModelIXRr6Reg = _TmnxModelIXRr6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 20)
)
if mibBuilder.loadTexts:
    tmnxModelIXRr6Reg.setStatus("current")
_TmnxModelIXR6Reg_ObjectIdentity = ObjectIdentity
tmnxModelIXR6Reg = _TmnxModelIXR6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 21)
)
if mibBuilder.loadTexts:
    tmnxModelIXR6Reg.setStatus("current")
_TmnxModelIXR10Reg_ObjectIdentity = ObjectIdentity
tmnxModelIXR10Reg = _TmnxModelIXR10Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 22)
)
if mibBuilder.loadTexts:
    tmnxModelIXR10Reg.setStatus("current")
_TmnxModelIXRsReg_ObjectIdentity = ObjectIdentity
tmnxModelIXRsReg = _TmnxModelIXRsReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 23)
)
if mibBuilder.loadTexts:
    tmnxModelIXRsReg.setStatus("current")
_TmnxModelSARHmcReg_ObjectIdentity = ObjectIdentity
tmnxModelSARHmcReg = _TmnxModelSARHmcReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 24)
)
if mibBuilder.loadTexts:
    tmnxModelSARHmcReg.setStatus("current")
_TmnxModelIXReReg_ObjectIdentity = ObjectIdentity
tmnxModelIXReReg = _TmnxModelIXReReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 25)
)
if mibBuilder.loadTexts:
    tmnxModelIXReReg.setStatus("current")
_TmnxModelIXRr4Reg_ObjectIdentity = ObjectIdentity
tmnxModelIXRr4Reg = _TmnxModelIXRr4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 26)
)
if mibBuilder.loadTexts:
    tmnxModelIXRr4Reg.setStatus("current")
_TmnxModelIXRx1Reg_ObjectIdentity = ObjectIdentity
tmnxModelIXRx1Reg = _TmnxModelIXRx1Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 27)
)
if mibBuilder.loadTexts:
    tmnxModelIXRx1Reg.setStatus("current")
_TmnxModelIXRx3Reg_ObjectIdentity = ObjectIdentity
tmnxModelIXRx3Reg = _TmnxModelIXRx3Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 29)
)
if mibBuilder.loadTexts:
    tmnxModelIXRx3Reg.setStatus("current")
_TmnxModelIXRecReg_ObjectIdentity = ObjectIdentity
tmnxModelIXRecReg = _TmnxModelIXRecReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 31)
)
if mibBuilder.loadTexts:
    tmnxModelIXRecReg.setStatus("current")
_TmnxModelIXRr6dReg_ObjectIdentity = ObjectIdentity
tmnxModelIXRr6dReg = _TmnxModelIXRr6dReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 32)
)
if mibBuilder.loadTexts:
    tmnxModelIXRr6dReg.setStatus("current")
_TmnxModelIXRr6dlReg_ObjectIdentity = ObjectIdentity
tmnxModelIXRr6dlReg = _TmnxModelIXRr6dlReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 3, 33)
)
if mibBuilder.loadTexts:
    tmnxModelIXRr6dlReg.setStatus("current")
_TimetraServiceSwitches_ObjectIdentity = ObjectIdentity
timetraServiceSwitches = _TimetraServiceSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6)
)
_TmnxModelESS1Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS1Reg = _TmnxModelESS1Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxModelESS1Reg.setStatus("current")
_TmnxModelESS4Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS4Reg = _TmnxModelESS4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxModelESS4Reg.setStatus("current")
_TmnxModelESS7Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS7Reg = _TmnxModelESS7Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxModelESS7Reg.setStatus("current")
_TmnxModelESS12Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS12Reg = _TmnxModelESS12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxModelESS12Reg.setStatus("current")
_TmnxModelESS6Reg_ObjectIdentity = ObjectIdentity
tmnxModelESS6Reg = _TmnxModelESS6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxModelESS6Reg.setStatus("current")
_TmnxModelESS6vReg_ObjectIdentity = ObjectIdentity
tmnxModelESS6vReg = _TmnxModelESS6vReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 6, 6)
)
if mibBuilder.loadTexts:
    tmnxModelESS6vReg.setStatus("current")
_Alcatel7710ServiceRouters_ObjectIdentity = ObjectIdentity
alcatel7710ServiceRouters = _Alcatel7710ServiceRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 9)
)
_TmnxModel7710SRc12Reg_ObjectIdentity = ObjectIdentity
tmnxModel7710SRc12Reg = _TmnxModel7710SRc12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxModel7710SRc12Reg.setStatus("current")
_TmnxModel7710SRc4Reg_ObjectIdentity = ObjectIdentity
tmnxModel7710SRc4Reg = _TmnxModel7710SRc4Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxModel7710SRc4Reg.setStatus("current")
_Alcatel7750MobileGateways_ObjectIdentity = ObjectIdentity
alcatel7750MobileGateways = _Alcatel7750MobileGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 12)
)
_TmnxModel7750MGSR7Reg_ObjectIdentity = ObjectIdentity
tmnxModel7750MGSR7Reg = _TmnxModel7750MGSR7Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxModel7750MGSR7Reg.setStatus("current")
_TmnxModel7750MGSR12Reg_ObjectIdentity = ObjectIdentity
tmnxModel7750MGSR12Reg = _TmnxModel7750MGSR12Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 12, 2)
)
if mibBuilder.loadTexts:
    tmnxModel7750MGSR12Reg.setStatus("current")
_AlcatelMGVMExtRoutingSystems_ObjectIdentity = ObjectIdentity
alcatelMGVMExtRoutingSystems = _AlcatelMGVMExtRoutingSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 13)
)
_TmnxModelCMGa6Reg_ObjectIdentity = ObjectIdentity
tmnxModelCMGa6Reg = _TmnxModelCMGa6Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 13, 8)
)
if mibBuilder.loadTexts:
    tmnxModelCMGa6Reg.setStatus("current")
_AlcatelMobileSbaSystems_ObjectIdentity = ObjectIdentity
alcatelMobileSbaSystems = _AlcatelMobileSbaSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 14)
)
_TmnxModelNrdReg_ObjectIdentity = ObjectIdentity
tmnxModelNrdReg = _TmnxModelNrdReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tmnxModelNrdReg.setStatus("current")
_Alcatel7950ExtRoutingSystems_ObjectIdentity = ObjectIdentity
alcatel7950ExtRoutingSystems = _Alcatel7950ExtRoutingSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 15)
)
_TmnxModel7950XRS20Reg_ObjectIdentity = ObjectIdentity
tmnxModel7950XRS20Reg = _TmnxModel7950XRS20Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxModel7950XRS20Reg.setStatus("current")
_TmnxModel7950XRS16Reg_ObjectIdentity = ObjectIdentity
tmnxModel7950XRS16Reg = _TmnxModel7950XRS16Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 15, 2)
)
if mibBuilder.loadTexts:
    tmnxModel7950XRS16Reg.setStatus("current")
_TmnxModel7950XRS20EReg_ObjectIdentity = ObjectIdentity
tmnxModel7950XRS20EReg = _TmnxModel7950XRS20EReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 15, 3)
)
if mibBuilder.loadTexts:
    tmnxModel7950XRS20EReg.setStatus("current")
_Alcatel7nnnExtServiceRouters_ObjectIdentity = ObjectIdentity
alcatel7nnnExtServiceRouters = _Alcatel7nnnExtServiceRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 18)
)
_AlcatelVMExtRoutingSystems_ObjectIdentity = ObjectIdentity
alcatelVMExtRoutingSystems = _AlcatelVMExtRoutingSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 19)
)
_TmnxModelVSRReg_ObjectIdentity = ObjectIdentity
tmnxModelVSRReg = _TmnxModelVSRReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 19, 1)
)
if mibBuilder.loadTexts:
    tmnxModelVSRReg.setStatus("current")
_TmnxModelVSRcReg_ObjectIdentity = ObjectIdentity
tmnxModelVSRcReg = _TmnxModelVSRcReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 19, 2)
)
if mibBuilder.loadTexts:
    tmnxModelVSRcReg.setStatus("current")
_TimetraGeneric_ObjectIdentity = ObjectIdentity
timetraGeneric = _TimetraGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 2)
)
_TimetraProducts_ObjectIdentity = ObjectIdentity
timetraProducts = _TimetraProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3)
)
_TmnxSRMIB_ObjectIdentity = ObjectIdentity
tmnxSRMIB = _TmnxSRMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1)
)
_TmnxSRConfs_ObjectIdentity = ObjectIdentity
tmnxSRConfs = _TmnxSRConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1)
)
_TmnxSRObjs_ObjectIdentity = ObjectIdentity
tmnxSRObjs = _TmnxSRObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2)
)
_TmnxSRNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxSRNotifyPrefix = _TmnxSRNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3)
)
_TmnxESSMIB_ObjectIdentity = ObjectIdentity
tmnxESSMIB = _TmnxESSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2)
)
_TmnxESSConfs_ObjectIdentity = ObjectIdentity
tmnxESSConfs = _TmnxESSConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 1)
)
_TmnxESSObjs_ObjectIdentity = ObjectIdentity
tmnxESSObjs = _TmnxESSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 2)
)
_TmnxESSNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxESSNotifyPrefix = _TmnxESSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 2, 3)
)
_AlcatelCommonMIB_ObjectIdentity = ObjectIdentity
alcatelCommonMIB = _AlcatelCommonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3)
)
_AlcatelConformance_ObjectIdentity = ObjectIdentity
alcatelConformance = _AlcatelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1)
)
_AlcatelObjects_ObjectIdentity = ObjectIdentity
alcatelObjects = _AlcatelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2)
)
_AlcatelNotifyPrefix_ObjectIdentity = ObjectIdentity
alcatelNotifyPrefix = _AlcatelNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3)
)
_TmnxMGMIB_ObjectIdentity = ObjectIdentity
tmnxMGMIB = _TmnxMGMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4)
)
_TmnxMGConfs_ObjectIdentity = ObjectIdentity
tmnxMGConfs = _TmnxMGConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4, 1)
)
_TmnxMGObjs_ObjectIdentity = ObjectIdentity
tmnxMGObjs = _TmnxMGObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4, 2)
)
_TmnxMGNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMGNotifyPrefix = _TmnxMGNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 4, 3)
)
_TmnxAgentCapability_ObjectIdentity = ObjectIdentity
tmnxAgentCapability = _TmnxAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4)
)
_Tmnx7750AgentCapability_ObjectIdentity = ObjectIdentity
tmnx7750AgentCapability = _Tmnx7750AgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4, 1)
)
_Tmnx7450AgentCapability_ObjectIdentity = ObjectIdentity
tmnx7450AgentCapability = _Tmnx7450AgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4, 2)
)
_Tmnx7710AgentCapability_ObjectIdentity = ObjectIdentity
tmnx7710AgentCapability = _Tmnx7710AgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 4, 3)
)
_TmnxProductCapability_ObjectIdentity = ObjectIdentity
tmnxProductCapability = _TmnxProductCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5)
)
_Tmnx7750Capability_ObjectIdentity = ObjectIdentity
tmnx7750Capability = _Tmnx7750Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1)
)
_Tmnx7750V3v0_ObjectIdentity = ObjectIdentity
tmnx7750V3v0 = _Tmnx7750V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 1)
)
_Tmnx7750V4v0_ObjectIdentity = ObjectIdentity
tmnx7750V4v0 = _Tmnx7750V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 2)
)
_Tmnx7750V5v0_ObjectIdentity = ObjectIdentity
tmnx7750V5v0 = _Tmnx7750V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 3)
)
_Tmnx7750V6v0_ObjectIdentity = ObjectIdentity
tmnx7750V6v0 = _Tmnx7750V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 4)
)
_Tmnx7750V6v1_ObjectIdentity = ObjectIdentity
tmnx7750V6v1 = _Tmnx7750V6v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 5)
)
_Tmnx7750V7v0_ObjectIdentity = ObjectIdentity
tmnx7750V7v0 = _Tmnx7750V7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 6)
)
_Tmnx7750V8v0_ObjectIdentity = ObjectIdentity
tmnx7750V8v0 = _Tmnx7750V8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 1, 7)
)
_Tmnx7450Capability_ObjectIdentity = ObjectIdentity
tmnx7450Capability = _Tmnx7450Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2)
)
_Tmnx7450V3v0_ObjectIdentity = ObjectIdentity
tmnx7450V3v0 = _Tmnx7450V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 1)
)
_Tmnx7450V4v0_ObjectIdentity = ObjectIdentity
tmnx7450V4v0 = _Tmnx7450V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 2)
)
_Tmnx7450V5v0_ObjectIdentity = ObjectIdentity
tmnx7450V5v0 = _Tmnx7450V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 3)
)
_Tmnx7450V6v0_ObjectIdentity = ObjectIdentity
tmnx7450V6v0 = _Tmnx7450V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 4)
)
_Tmnx7450V6v1_ObjectIdentity = ObjectIdentity
tmnx7450V6v1 = _Tmnx7450V6v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 5)
)
_Tmnx7450V7v0_ObjectIdentity = ObjectIdentity
tmnx7450V7v0 = _Tmnx7450V7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 6)
)
_Tmnx7450V8v0_ObjectIdentity = ObjectIdentity
tmnx7450V8v0 = _Tmnx7450V8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 2, 7)
)
_Tmnx7710Capability_ObjectIdentity = ObjectIdentity
tmnx7710Capability = _Tmnx7710Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3)
)
_Tmnx7710V3v0_ObjectIdentity = ObjectIdentity
tmnx7710V3v0 = _Tmnx7710V3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 1)
)
_Tmnx7710V4v0_ObjectIdentity = ObjectIdentity
tmnx7710V4v0 = _Tmnx7710V4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 2)
)
_Tmnx7710V5v0_ObjectIdentity = ObjectIdentity
tmnx7710V5v0 = _Tmnx7710V5v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 3)
)
_Tmnx7710V6v0_ObjectIdentity = ObjectIdentity
tmnx7710V6v0 = _Tmnx7710V6v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 4)
)
_Tmnx7710V6v1_ObjectIdentity = ObjectIdentity
tmnx7710V6v1 = _Tmnx7710V6v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 5)
)
_Tmnx7710V7v0_ObjectIdentity = ObjectIdentity
tmnx7710V7v0 = _Tmnx7710V7v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 6)
)
_Tmnx7710V8v0_ObjectIdentity = ObjectIdentity
tmnx7710V8v0 = _Tmnx7710V8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 3, 7)
)
_Tmnx7750MGCapability_ObjectIdentity = ObjectIdentity
tmnx7750MGCapability = _Tmnx7750MGCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 4)
)
_Tmnx7750MGV1v0_ObjectIdentity = ObjectIdentity
tmnx7750MGV1v0 = _Tmnx7750MGV1v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 4, 1)
)
_Tmnx7750MGV2v0_ObjectIdentity = ObjectIdentity
tmnx7750MGV2v0 = _Tmnx7750MGV2v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 4, 2)
)
_Tmnx7750MGV3v0_ObjectIdentity = ObjectIdentity
tmnx7750MGV3v0 = _Tmnx7750MGV3v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 4, 3)
)
_Tmnx7750MGV4v0_ObjectIdentity = ObjectIdentity
tmnx7750MGV4v0 = _Tmnx7750MGV4v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 4, 4)
)
_TmnxSROSCapability_ObjectIdentity = ObjectIdentity
tmnxSROSCapability = _TmnxSROSCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5)
)
_TmnxSROSV8v0_ObjectIdentity = ObjectIdentity
tmnxSROSV8v0 = _TmnxSROSV8v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5, 1)
)
_TmnxSROSV9v0_ObjectIdentity = ObjectIdentity
tmnxSROSV9v0 = _TmnxSROSV9v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5, 2)
)
_TmnxSROSV10v0_ObjectIdentity = ObjectIdentity
tmnxSROSV10v0 = _TmnxSROSV10v0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 5, 5, 3)
)
_TmnxBasedProducts_ObjectIdentity = ObjectIdentity
tmnxBasedProducts = _TmnxBasedProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6)
)
_TimetraConformance_ObjectIdentity = ObjectIdentity
timetraConformance = _TimetraConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 999)
)
_TimetraCompliances_ObjectIdentity = ObjectIdentity
timetraCompliances = _TimetraCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 999, 1)
)
_TimetraGroups_ObjectIdentity = ObjectIdentity
timetraGroups = _TimetraGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 999, 2)
)
_TimetraEoM_Type = DateAndTime
_TimetraEoM_Object = MibScalar
timetraEoM = _TimetraEoM_Object(
    (1, 3, 6, 1, 4, 1, 6527, 1000),
    _TimetraEoM_Type()
)
timetraEoM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timetraEoM.setStatus("current")

# Managed Objects groups

timetraGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 999, 2, 1)
)
timetraGroup.setObjects(
    ("TIMETRA-GLOBAL-MIB", "timetraEoM")
)
if mibBuilder.loadTexts:
    timetraGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

timetraCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 999, 1, 1)
)
timetraCompliance.setObjects(
    ("TIMETRA-GLOBAL-MIB", "timetraGroup")
)
if mibBuilder.loadTexts:
    timetraCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-GLOBAL-MIB",
    **{"timetra": timetra,
       "timetraReg": timetraReg,
       "timetraModules": timetraModules,
       "timetraGlobalMIBModule": timetraGlobalMIBModule,
       "timetraSRMIBModules": timetraSRMIBModules,
       "timetraAirframeMIBModule": timetraAirframeMIBModule,
       "timetraApplianceMIBModule": timetraApplianceMIBModule,
       "timetraCapabilityModule": timetraCapabilityModule,
       "timetra7750CapModule": timetra7750CapModule,
       "timetra7450CapModule": timetra7450CapModule,
       "timetra7710CapModule": timetra7710CapModule,
       "timetra7750MGCapModule": timetra7750MGCapModule,
       "timetraSROSCapModule": timetraSROSCapModule,
       "timetraDCCapModule": timetraDCCapModule,
       "timetraMGCapModule": timetraMGCapModule,
       "alcatelCommonMIBModules": alcatelCommonMIBModules,
       "timetraServiceRouters": timetraServiceRouters,
       "tmnxModelSR1Reg": tmnxModelSR1Reg,
       "tmnxModelSR4Reg": tmnxModelSR4Reg,
       "tmnxModelSR12Reg": tmnxModelSR12Reg,
       "tmnxModelSR7Reg": tmnxModelSR7Reg,
       "tmnxModelSR6Reg": tmnxModelSR6Reg,
       "tmnxModelSRc12Reg": tmnxModelSRc12Reg,
       "tmnxModelSRc4Reg": tmnxModelSRc4Reg,
       "tmnxModelSR12EReg": tmnxModelSR12EReg,
       "tmnxModelSRa4Reg": tmnxModelSRa4Reg,
       "tmnxModelSRa8Reg": tmnxModelSRa8Reg,
       "tmnxModelSR1eReg": tmnxModelSR1eReg,
       "tmnxModelSR2eReg": tmnxModelSR2eReg,
       "tmnxModelSR3eReg": tmnxModelSR3eReg,
       "tmnxModelSARHmReg": tmnxModelSARHmReg,
       "tmnxModelSR1v2Reg": tmnxModelSR1v2Reg,
       "tmnxModelSR14sReg": tmnxModelSR14sReg,
       "tmnxModelSR7sReg": tmnxModelSR7sReg,
       "tmnxModelSR1sReg": tmnxModelSR1sReg,
       "tmnxModelSR2sReg": tmnxModelSR2sReg,
       "tmnxModelIXRr6Reg": tmnxModelIXRr6Reg,
       "tmnxModelIXR6Reg": tmnxModelIXR6Reg,
       "tmnxModelIXR10Reg": tmnxModelIXR10Reg,
       "tmnxModelIXRsReg": tmnxModelIXRsReg,
       "tmnxModelSARHmcReg": tmnxModelSARHmcReg,
       "tmnxModelIXReReg": tmnxModelIXReReg,
       "tmnxModelIXRr4Reg": tmnxModelIXRr4Reg,
       "tmnxModelIXRx1Reg": tmnxModelIXRx1Reg,
       "tmnxModelIXRx3Reg": tmnxModelIXRx3Reg,
       "tmnxModelIXRecReg": tmnxModelIXRecReg,
       "tmnxModelIXRr6dReg": tmnxModelIXRr6dReg,
       "tmnxModelIXRr6dlReg": tmnxModelIXRr6dlReg,
       "timetraServiceSwitches": timetraServiceSwitches,
       "tmnxModelESS1Reg": tmnxModelESS1Reg,
       "tmnxModelESS4Reg": tmnxModelESS4Reg,
       "tmnxModelESS7Reg": tmnxModelESS7Reg,
       "tmnxModelESS12Reg": tmnxModelESS12Reg,
       "tmnxModelESS6Reg": tmnxModelESS6Reg,
       "tmnxModelESS6vReg": tmnxModelESS6vReg,
       "alcatel7710ServiceRouters": alcatel7710ServiceRouters,
       "tmnxModel7710SRc12Reg": tmnxModel7710SRc12Reg,
       "tmnxModel7710SRc4Reg": tmnxModel7710SRc4Reg,
       "alcatel7750MobileGateways": alcatel7750MobileGateways,
       "tmnxModel7750MGSR7Reg": tmnxModel7750MGSR7Reg,
       "tmnxModel7750MGSR12Reg": tmnxModel7750MGSR12Reg,
       "alcatelMGVMExtRoutingSystems": alcatelMGVMExtRoutingSystems,
       "tmnxModelCMGa6Reg": tmnxModelCMGa6Reg,
       "alcatelMobileSbaSystems": alcatelMobileSbaSystems,
       "tmnxModelNrdReg": tmnxModelNrdReg,
       "alcatel7950ExtRoutingSystems": alcatel7950ExtRoutingSystems,
       "tmnxModel7950XRS20Reg": tmnxModel7950XRS20Reg,
       "tmnxModel7950XRS16Reg": tmnxModel7950XRS16Reg,
       "tmnxModel7950XRS20EReg": tmnxModel7950XRS20EReg,
       "alcatel7nnnExtServiceRouters": alcatel7nnnExtServiceRouters,
       "alcatelVMExtRoutingSystems": alcatelVMExtRoutingSystems,
       "tmnxModelVSRReg": tmnxModelVSRReg,
       "tmnxModelVSRcReg": tmnxModelVSRcReg,
       "timetraGeneric": timetraGeneric,
       "timetraProducts": timetraProducts,
       "tmnxSRMIB": tmnxSRMIB,
       "tmnxSRConfs": tmnxSRConfs,
       "tmnxSRObjs": tmnxSRObjs,
       "tmnxSRNotifyPrefix": tmnxSRNotifyPrefix,
       "tmnxESSMIB": tmnxESSMIB,
       "tmnxESSConfs": tmnxESSConfs,
       "tmnxESSObjs": tmnxESSObjs,
       "tmnxESSNotifyPrefix": tmnxESSNotifyPrefix,
       "alcatelCommonMIB": alcatelCommonMIB,
       "alcatelConformance": alcatelConformance,
       "alcatelObjects": alcatelObjects,
       "alcatelNotifyPrefix": alcatelNotifyPrefix,
       "tmnxMGMIB": tmnxMGMIB,
       "tmnxMGConfs": tmnxMGConfs,
       "tmnxMGObjs": tmnxMGObjs,
       "tmnxMGNotifyPrefix": tmnxMGNotifyPrefix,
       "tmnxAgentCapability": tmnxAgentCapability,
       "tmnx7750AgentCapability": tmnx7750AgentCapability,
       "tmnx7450AgentCapability": tmnx7450AgentCapability,
       "tmnx7710AgentCapability": tmnx7710AgentCapability,
       "tmnxProductCapability": tmnxProductCapability,
       "tmnx7750Capability": tmnx7750Capability,
       "tmnx7750V3v0": tmnx7750V3v0,
       "tmnx7750V4v0": tmnx7750V4v0,
       "tmnx7750V5v0": tmnx7750V5v0,
       "tmnx7750V6v0": tmnx7750V6v0,
       "tmnx7750V6v1": tmnx7750V6v1,
       "tmnx7750V7v0": tmnx7750V7v0,
       "tmnx7750V8v0": tmnx7750V8v0,
       "tmnx7450Capability": tmnx7450Capability,
       "tmnx7450V3v0": tmnx7450V3v0,
       "tmnx7450V4v0": tmnx7450V4v0,
       "tmnx7450V5v0": tmnx7450V5v0,
       "tmnx7450V6v0": tmnx7450V6v0,
       "tmnx7450V6v1": tmnx7450V6v1,
       "tmnx7450V7v0": tmnx7450V7v0,
       "tmnx7450V8v0": tmnx7450V8v0,
       "tmnx7710Capability": tmnx7710Capability,
       "tmnx7710V3v0": tmnx7710V3v0,
       "tmnx7710V4v0": tmnx7710V4v0,
       "tmnx7710V5v0": tmnx7710V5v0,
       "tmnx7710V6v0": tmnx7710V6v0,
       "tmnx7710V6v1": tmnx7710V6v1,
       "tmnx7710V7v0": tmnx7710V7v0,
       "tmnx7710V8v0": tmnx7710V8v0,
       "tmnx7750MGCapability": tmnx7750MGCapability,
       "tmnx7750MGV1v0": tmnx7750MGV1v0,
       "tmnx7750MGV2v0": tmnx7750MGV2v0,
       "tmnx7750MGV3v0": tmnx7750MGV3v0,
       "tmnx7750MGV4v0": tmnx7750MGV4v0,
       "tmnxSROSCapability": tmnxSROSCapability,
       "tmnxSROSV8v0": tmnxSROSV8v0,
       "tmnxSROSV9v0": tmnxSROSV9v0,
       "tmnxSROSV10v0": tmnxSROSV10v0,
       "tmnxBasedProducts": tmnxBasedProducts,
       "timetraConformance": timetraConformance,
       "timetraCompliances": timetraCompliances,
       "timetraCompliance": timetraCompliance,
       "timetraGroups": timetraGroups,
       "timetraGroup": timetraGroup,
       "timetraEoM": timetraEoM}
)
