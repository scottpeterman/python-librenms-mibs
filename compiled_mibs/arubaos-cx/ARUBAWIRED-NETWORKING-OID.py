# SNMP MIB module (ARUBAWIRED-NETWORKING-OID) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-NETWORKING-OID
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:01 2025
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

hpeNetworking = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4)
)
if mibBuilder.loadTexts:
    hpeNetworking.setRevisions(
        ("2025-03-12 00:00",
         "2025-02-19 00:00",
         "2024-12-05 00:00",
         "2024-11-11 00:00",
         "2024-10-25 00:00",
         "2024-09-11 00:00",
         "2024-08-30 00:00",
         "2024-08-21 00:00",
         "2024-08-07 00:00",
         "2024-05-29 00:00",
         "2024-03-06 00:00",
         "2024-02-28 00:00",
         "2024-02-22 00:00",
         "2024-02-07 00:00",
         "2023-12-18 00:00",
         "2023-12-14 00:00",
         "2023-12-11 00:00",
         "2023-06-28 00:00",
         "2023-06-23 00:00",
         "2023-05-18 00:00",
         "2023-04-25 00:00",
         "2023-04-19 00:00",
         "2023-04-10 00:00",
         "2022-11-29 00:00",
         "2022-11-10 00:00",
         "2022-10-27 00:00",
         "2022-06-29 00:00",
         "2022-06-27 00:00",
         "2022-05-26 00:00",
         "2022-01-31 00:00",
         "2021-11-23 00:00",
         "2021-11-17 00:00",
         "2021-11-12 00:00",
         "2021-10-22 00:00",
         "2021-08-27 00:00",
         "2021-08-26 00:00",
         "2021-06-16 00:00",
         "2021-05-26 00:00",
         "2021-04-28 00:00",
         "2021-02-24 00:00",
         "2020-11-20 00:00",
         "2020-11-03 00:00",
         "2020-09-21 00:00",
         "2020-08-14 00:00",
         "2020-06-12 00:00",
         "2020-04-13 00:00",
         "2020-03-17 00:00",
         "2020-01-30 00:00",
         "2020-01-14 00:00",
         "2020-01-06 00:00",
         "2019-11-21 00:00",
         "2019-09-26 00:00",
         "2019-08-26 00:00",
         "2019-05-14 00:00",
         "2019-04-16 00:00",
         "2019-04-15 00:00",
         "2018-12-19 00:00",
         "2018-10-10 00:00",
         "2018-04-12 00:00",
         "2018-04-09 00:00",
         "2017-11-28 00:00",
         "2017-11-14 00:00",
         "2017-11-02 00:00",
         "2017-10-24 00:00",
         "2017-08-30 00:00",
         "2017-04-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hpe_ObjectIdentity = ObjectIdentity
hpe = _Hpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196)
)
_ReservedhpeNetworking_ObjectIdentity = ObjectIdentity
reservedhpeNetworking = _ReservedhpeNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 0)
)
_WiredNetworkingDevices_ObjectIdentity = ObjectIdentity
wiredNetworkingDevices = _WiredNetworkingDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1)
)
_ArubaOS_CX_ObjectIdentity = ObjectIdentity
arubaOS_CX = _ArubaOS_CX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1)
)
_WndDeviceIds_ObjectIdentity = ObjectIdentity
wndDeviceIds = _WndDeviceIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1)
)
_ArubaWiredSwitchJL375A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL375A = _ArubaWiredSwitchJL375A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL375A.setStatus("current")
_ArubaWiredSwitchJL479A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL479A = _ArubaWiredSwitchJL479A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL479A.setStatus("current")
_ArubaWiredSwitchJL579A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL579A = _ArubaWiredSwitchJL579A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL579A.setStatus("current")
_ArubaWiredSwitchJL581A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL581A = _ArubaWiredSwitchJL581A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL581A.setStatus("current")
_ArubaWiredSwitchJL635A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL635A = _ArubaWiredSwitchJL635A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 50)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL635A.setStatus("current")
_ArubaWiredSwitchS0G12A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G12A = _ArubaWiredSwitchS0G12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 51)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G12A.setStatus("current")
_ArubaWiredSwitchS4A48A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4A48A = _ArubaWiredSwitchS4A48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 52)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4A48A.setStatus("current")
_ArubaWiredSwitchJL636A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL636A = _ArubaWiredSwitchJL636A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 70)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL636A.setStatus("current")
_ArubaWiredSwitchS4B20A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4B20A = _ArubaWiredSwitchS4B20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 80)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4B20A.setStatus("current")
_ArubaWiredSwitchS4B21A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4B21A = _ArubaWiredSwitchS4B21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 81)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4B21A.setStatus("current")
_ArubaWiredSwitchS4B22A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4B22A = _ArubaWiredSwitchS4B22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 82)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4B22A.setStatus("current")
_ArubaWiredSwitchS4B23A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4B23A = _ArubaWiredSwitchS4B23A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 83)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4B23A.setStatus("current")
_ArubaWiredSwitchS2T42A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS2T42A = _ArubaWiredSwitchS2T42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 84)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS2T42A.setStatus("current")
_ArubaWiredSwitchS2T46A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS2T46A = _ArubaWiredSwitchS2T46A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 85)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS2T46A.setStatus("current")
_ArubaWiredSwitchS2T47A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS2T47A = _ArubaWiredSwitchS2T47A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 86)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS2T47A.setStatus("current")
_ArubaWiredSwitchS2T48A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS2T48A = _ArubaWiredSwitchS2T48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 87)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS2T48A.setStatus("current")
_ArubaWiredSwitchJL658A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL658A = _ArubaWiredSwitchJL658A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 100)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL658A.setStatus("current")
_ArubaWiredSwitchJL659A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL659A = _ArubaWiredSwitchJL659A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 101)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL659A.setStatus("current")
_ArubaWiredSwitchJL660A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL660A = _ArubaWiredSwitchJL660A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 102)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL660A.setStatus("current")
_ArubaWiredSwitchJL661A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL661A = _ArubaWiredSwitchJL661A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 103)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL661A.setStatus("current")
_ArubaWiredSwitchJL662A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL662A = _ArubaWiredSwitchJL662A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 104)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL662A.setStatus("current")
_ArubaWiredSwitchJL663A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL663A = _ArubaWiredSwitchJL663A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 105)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL663A.setStatus("current")
_ArubaWiredSwitchJL664A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL664A = _ArubaWiredSwitchJL664A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 106)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL664A.setStatus("current")
_ArubaWiredSwitchJL665A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL665A = _ArubaWiredSwitchJL665A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 107)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL665A.setStatus("current")
_ArubaWiredSwitchJL666A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL666A = _ArubaWiredSwitchJL666A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 108)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL666A.setStatus("current")
_ArubaWiredSwitchJL667A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL667A = _ArubaWiredSwitchJL667A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 109)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL667A.setStatus("current")
_ArubaWiredSwitchJL668A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL668A = _ArubaWiredSwitchJL668A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 110)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL668A.setStatus("current")
_ArubaWiredSwitchJL762A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL762A = _ArubaWiredSwitchJL762A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 111)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL762A.setStatus("current")
_ArubaWiredSwitchR8S89A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8S89A = _ArubaWiredSwitchR8S89A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 116)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8S89A.setStatus("current")
_ArubaWiredSwitchR8S90A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8S90A = _ArubaWiredSwitchR8S90A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 117)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8S90A.setStatus("current")
_ArubaWiredSwitchR8S91A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8S91A = _ArubaWiredSwitchR8S91A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 118)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8S91A.setStatus("current")
_ArubaWiredSwitchR8S92A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8S92A = _ArubaWiredSwitchR8S92A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 119)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8S92A.setStatus("current")
_ArubaWiredSwitchS0E91A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0E91A = _ArubaWiredSwitchS0E91A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 120)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0E91A.setStatus("current")
_ArubaWiredSwitchS0X44A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0X44A = _ArubaWiredSwitchS0X44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 121)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0X44A.setStatus("current")
_ArubaWiredSwitchS0F99A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0F99A = _ArubaWiredSwitchS0F99A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 122)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0F99A.setStatus("current")
_ArubaWiredSwitchS0G00A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G00A = _ArubaWiredSwitchS0G00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 123)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G00A.setStatus("current")
_ArubaWiredSwitchS0G01A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G01A = _ArubaWiredSwitchS0G01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 124)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G01A.setStatus("current")
_ArubaWiredSwitchS0G02A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G02A = _ArubaWiredSwitchS0G02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 125)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G02A.setStatus("current")
_ArubaWiredSwitchS0G03A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G03A = _ArubaWiredSwitchS0G03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 126)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G03A.setStatus("current")
_ArubaWiredSwitchS0G04A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G04A = _ArubaWiredSwitchS0G04A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 127)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G04A.setStatus("current")
_ArubaWiredSwitchS0G05A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G05A = _ArubaWiredSwitchS0G05A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 128)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G05A.setStatus("current")
_ArubaWiredSwitchS0G06A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G06A = _ArubaWiredSwitchS0G06A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 129)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G06A.setStatus("current")
_ArubaWiredSwitchS0G95A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G95A = _ArubaWiredSwitchS0G95A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 130)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G95A.setStatus("current")
_ArubaWiredSwitchS0G96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G96A = _ArubaWiredSwitchS0G96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 131)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G96A.setStatus("current")
_ArubaWiredSwitchS0G97A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G97A = _ArubaWiredSwitchS0G97A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 132)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G97A.setStatus("current")
_ArubaWiredSwitchS0G98A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G98A = _ArubaWiredSwitchS0G98A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 133)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G98A.setStatus("current")
_ArubaWiredSwitchR0X24A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X24A = _ArubaWiredSwitchR0X24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 150)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X24A.setStatus("current")
_ArubaWiredSwitchR0X25A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X25A = _ArubaWiredSwitchR0X25A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 151)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X25A.setStatus("current")
_ArubaWiredSwitchR0X24C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X24C = _ArubaWiredSwitchR0X24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 160)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X24C.setStatus("current")
_ArubaWiredSwitchR0X25C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X25C = _ArubaWiredSwitchR0X25C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 161)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X25C.setStatus("current")
_ArubaWiredSwitchJL675A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL675A = _ArubaWiredSwitchJL675A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 250)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL675A.setStatus("current")
_ArubaWiredSwitchJL676A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL676A = _ArubaWiredSwitchJL676A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 251)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL676A.setStatus("current")
_ArubaWiredSwitchJL677A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL677A = _ArubaWiredSwitchJL677A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 252)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL677A.setStatus("current")
_ArubaWiredSwitchJL678A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL678A = _ArubaWiredSwitchJL678A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 253)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL678A.setStatus("current")
_ArubaWiredSwitchJL679A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL679A = _ArubaWiredSwitchJL679A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 254)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL679A.setStatus("current")
_ArubaWiredSwitchR9Y04A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR9Y04A = _ArubaWiredSwitchR9Y04A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 260)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR9Y04A.setStatus("current")
_ArubaWiredSwitchS4U55A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U55A = _ArubaWiredSwitchS4U55A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 261)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U55A.setStatus("current")
_ArubaWiredSwitchS4U56A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U56A = _ArubaWiredSwitchS4U56A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 262)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U56A.setStatus("current")
_ArubaWiredSwitchS4U57A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U57A = _ArubaWiredSwitchS4U57A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 263)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U57A.setStatus("current")
_ArubaWiredSwitchS4U58A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U58A = _ArubaWiredSwitchS4U58A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 264)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U58A.setStatus("current")
_ArubaWiredSwitchR8N85A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N85A = _ArubaWiredSwitchR8N85A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 270)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N85A.setStatus("current")
_ArubaWiredSwitchR8N86A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N86A = _ArubaWiredSwitchR8N86A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 271)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N86A.setStatus("current")
_ArubaWiredSwitchR8N87A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N87A = _ArubaWiredSwitchR8N87A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 272)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N87A.setStatus("current")
_ArubaWiredSwitchR8N88A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N88A = _ArubaWiredSwitchR8N88A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 273)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N88A.setStatus("current")
_ArubaWiredSwitchR8N89A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N89A = _ArubaWiredSwitchR8N89A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 274)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N89A.setStatus("current")
_ArubaWiredSwitchR8N85B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N85B = _ArubaWiredSwitchR8N85B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 275)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N85B.setStatus("current")
_ArubaWiredSwitchR8N86B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N86B = _ArubaWiredSwitchR8N86B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 276)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N86B.setStatus("current")
_ArubaWiredSwitchR8N87B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N87B = _ArubaWiredSwitchR8N87B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 277)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N87B.setStatus("current")
_ArubaWiredSwitchR8N88B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N88B = _ArubaWiredSwitchR8N88B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 278)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N88B.setStatus("current")
_ArubaWiredSwitchR8N89B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8N89B = _ArubaWiredSwitchR8N89B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 279)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8N89B.setStatus("current")
_ArubaWiredSwitchR9Y03A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR9Y03A = _ArubaWiredSwitchR9Y03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 280)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR9Y03A.setStatus("current")
_ArubaWiredSwitchS4U59A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U59A = _ArubaWiredSwitchS4U59A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 281)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U59A.setStatus("current")
_ArubaWiredSwitchS4U60A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U60A = _ArubaWiredSwitchS4U60A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 282)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U60A.setStatus("current")
_ArubaWiredSwitchS4U61A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U61A = _ArubaWiredSwitchS4U61A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 283)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U61A.setStatus("current")
_ArubaWiredSwitchS4U62A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U62A = _ArubaWiredSwitchS4U62A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 284)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U62A.setStatus("current")
_ArubaWiredSwitchR9Y03B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR9Y03B = _ArubaWiredSwitchR9Y03B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 285)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR9Y03B.setStatus("current")
_ArubaWiredSwitchS4R20A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R20A = _ArubaWiredSwitchS4R20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 286)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R20A.setStatus("current")
_ArubaWiredSwitchS4R21A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R21A = _ArubaWiredSwitchS4R21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 287)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R21A.setStatus("current")
_ArubaWiredSwitchS4R22A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R22A = _ArubaWiredSwitchS4R22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 288)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R22A.setStatus("current")
_ArubaWiredSwitchS4R23A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R23A = _ArubaWiredSwitchS4R23A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 289)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R23A.setStatus("current")
_ArubaWiredSwitchS4R24A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R24A = _ArubaWiredSwitchS4R24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 290)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R24A.setStatus("current")
_ArubaWiredSwitchS4R25A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R25A = _ArubaWiredSwitchS4R25A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 291)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R25A.setStatus("current")
_ArubaWiredSwitchS4R26A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R26A = _ArubaWiredSwitchS4R26A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 292)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R26A.setStatus("current")
_ArubaWiredSwitchS4R27A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R27A = _ArubaWiredSwitchS4R27A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 293)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R27A.setStatus("current")
_ArubaWiredSwitchS4R28A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R28A = _ArubaWiredSwitchS4R28A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 294)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R28A.setStatus("current")
_ArubaWiredSwitchS4R29A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R29A = _ArubaWiredSwitchS4R29A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 295)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R29A.setStatus("current")
_ArubaWiredSwitchJL724A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL724A = _ArubaWiredSwitchJL724A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 300)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL724A.setStatus("current")
_ArubaWiredSwitchJL725A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL725A = _ArubaWiredSwitchJL725A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 301)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL725A.setStatus("current")
_ArubaWiredSwitchJL726A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL726A = _ArubaWiredSwitchJL726A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 302)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL726A.setStatus("current")
_ArubaWiredSwitchJL727A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL727A = _ArubaWiredSwitchJL727A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 303)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL727A.setStatus("current")
_ArubaWiredSwitchJL728A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL728A = _ArubaWiredSwitchJL728A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 304)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL728A.setStatus("current")
_ArubaWiredSwitchJL724B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL724B = _ArubaWiredSwitchJL724B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 305)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL724B.setStatus("current")
_ArubaWiredSwitchJL725B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL725B = _ArubaWiredSwitchJL725B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 306)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL725B.setStatus("current")
_ArubaWiredSwitchJL726B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL726B = _ArubaWiredSwitchJL726B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 307)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL726B.setStatus("current")
_ArubaWiredSwitchJL727B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL727B = _ArubaWiredSwitchJL727B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 308)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL727B.setStatus("current")
_ArubaWiredSwitchJL728B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL728B = _ArubaWiredSwitchJL728B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 309)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL728B.setStatus("current")
_ArubaWiredSwitchS0M81A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M81A = _ArubaWiredSwitchS0M81A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 310)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M81A.setStatus("current")
_ArubaWiredSwitchS0M82A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M82A = _ArubaWiredSwitchS0M82A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 311)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M82A.setStatus("current")
_ArubaWiredSwitchS0M83A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M83A = _ArubaWiredSwitchS0M83A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 312)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M83A.setStatus("current")
_ArubaWiredSwitchS0M84A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M84A = _ArubaWiredSwitchS0M84A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 313)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M84A.setStatus("current")
_ArubaWiredSwitchS0M85A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M85A = _ArubaWiredSwitchS0M85A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 314)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M85A.setStatus("current")
_ArubaWiredSwitchS0M86A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M86A = _ArubaWiredSwitchS0M86A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 315)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M86A.setStatus("current")
_ArubaWiredSwitchS0M87A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M87A = _ArubaWiredSwitchS0M87A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 316)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M87A.setStatus("current")
_ArubaWiredSwitchS0M88A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M88A = _ArubaWiredSwitchS0M88A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 317)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M88A.setStatus("current")
_ArubaWiredSwitchS0M89A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M89A = _ArubaWiredSwitchS0M89A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 318)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M89A.setStatus("current")
_ArubaWiredSwitchS0M90A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0M90A = _ArubaWiredSwitchS0M90A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 319)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0M90A.setStatus("current")
_ArubaWiredSwitchR8Q67A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8Q67A = _ArubaWiredSwitchR8Q67A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 321)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8Q67A.setStatus("current")
_ArubaWiredSwitchR8Q68A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8Q68A = _ArubaWiredSwitchR8Q68A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 322)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8Q68A.setStatus("current")
_ArubaWiredSwitchR8Q69A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8Q69A = _ArubaWiredSwitchR8Q69A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 323)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8Q69A.setStatus("current")
_ArubaWiredSwitchR8Q70A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8Q70A = _ArubaWiredSwitchR8Q70A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 324)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8Q70A.setStatus("current")
_ArubaWiredSwitchR8Q71A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8Q71A = _ArubaWiredSwitchR8Q71A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 325)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8Q71A.setStatus("current")
_ArubaWiredSwitchR8Q72A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8Q72A = _ArubaWiredSwitchR8Q72A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 326)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8Q72A.setStatus("current")
_ArubaWiredSwitchR8V08A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8V08A = _ArubaWiredSwitchR8V08A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 327)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8V08A.setStatus("current")
_ArubaWiredSwitchR8V09A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8V09A = _ArubaWiredSwitchR8V09A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 328)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8V09A.setStatus("current")
_ArubaWiredSwitchR8V10A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8V10A = _ArubaWiredSwitchR8V10A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 329)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8V10A.setStatus("current")
_ArubaWiredSwitchR8V11A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8V11A = _ArubaWiredSwitchR8V11A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 330)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8V11A.setStatus("current")
_ArubaWiredSwitchR8V12A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8V12A = _ArubaWiredSwitchR8V12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 331)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8V12A.setStatus("current")
_ArubaWiredSwitchR8V13A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8V13A = _ArubaWiredSwitchR8V13A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 332)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8V13A.setStatus("current")
_ArubaWiredSwitchS4U63A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U63A = _ArubaWiredSwitchS4U63A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 333)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U63A.setStatus("current")
_ArubaWiredSwitchS4U64A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U64A = _ArubaWiredSwitchS4U64A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 334)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U64A.setStatus("current")
_ArubaWiredSwitchS4U65A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U65A = _ArubaWiredSwitchS4U65A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 335)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U65A.setStatus("current")
_ArubaWiredSwitchS4U66A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U66A = _ArubaWiredSwitchS4U66A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 336)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U66A.setStatus("current")
_ArubaWiredSwitchS4U67A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4U67A = _ArubaWiredSwitchS4U67A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 337)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4U67A.setStatus("current")
_ArubaWiredSwitchS0G13A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G13A = _ArubaWiredSwitchS0G13A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 341)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G13A.setStatus("current")
_ArubaWiredSwitchS0G14A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G14A = _ArubaWiredSwitchS0G14A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 342)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G14A.setStatus("current")
_ArubaWiredSwitchS0G15A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G15A = _ArubaWiredSwitchS0G15A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 343)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G15A.setStatus("current")
_ArubaWiredSwitchS0G16A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G16A = _ArubaWiredSwitchS0G16A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 344)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G16A.setStatus("current")
_ArubaWiredSwitchS0G17A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0G17A = _ArubaWiredSwitchS0G17A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 345)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0G17A.setStatus("current")
_ArubaWiredSwitchJL717A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL717A = _ArubaWiredSwitchJL717A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 400)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL717A.setStatus("current")
_ArubaWiredSwitchJL718A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL718A = _ArubaWiredSwitchJL718A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 401)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL718A.setStatus("current")
_ArubaWiredSwitchJL719A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL719A = _ArubaWiredSwitchJL719A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 402)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL719A.setStatus("current")
_ArubaWiredSwitchJL720A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL720A = _ArubaWiredSwitchJL720A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 403)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL720A.setStatus("current")
_ArubaWiredSwitchJL721A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL721A = _ArubaWiredSwitchJL721A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 404)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL721A.setStatus("current")
_ArubaWiredSwitchJL722A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL722A = _ArubaWiredSwitchJL722A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 405)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL722A.setStatus("current")
_ArubaWiredSwitchJL717C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL717C = _ArubaWiredSwitchJL717C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 420)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL717C.setStatus("current")
_ArubaWiredSwitchJL718C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL718C = _ArubaWiredSwitchJL718C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 421)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL718C.setStatus("current")
_ArubaWiredSwitchJL719C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL719C = _ArubaWiredSwitchJL719C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 422)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL719C.setStatus("current")
_ArubaWiredSwitchJL720C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL720C = _ArubaWiredSwitchJL720C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 423)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL720C.setStatus("current")
_ArubaWiredSwitchJL721C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL721C = _ArubaWiredSwitchJL721C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 424)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL721C.setStatus("current")
_ArubaWiredSwitchJL722C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL722C = _ArubaWiredSwitchJL722C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 425)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL722C.setStatus("current")
_ArubaWiredSwitchJL817A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL817A = _ArubaWiredSwitchJL817A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 450)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL817A.setStatus("current")
_ArubaWiredSwitchJL818A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL818A = _ArubaWiredSwitchJL818A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 451)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL818A.setStatus("current")
_ArubaWiredSwitchR8S96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8S96A = _ArubaWiredSwitchR8S96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 600)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8S96A.setStatus("current")
_ArubaWiredSwitchS4K80A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4K80A = _ArubaWiredSwitchS4K80A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 601)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4K80A.setStatus("current")
_ArubaWiredSwitchS4R58A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R58A = _ArubaWiredSwitchS4R58A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 630)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R58A.setStatus("current")
_ArubaWiredSwitchS4R59A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4R59A = _ArubaWiredSwitchS4R59A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 631)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4R59A.setStatus("current")
_ArubaWiredSwitchR8Z96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR8Z96A = _ArubaWiredSwitchR8Z96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 700)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR8Z96A.setStatus("current")
_ArubaWiredSwitchS0F95A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0F95A = _ArubaWiredSwitchS0F95A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 710)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0F95A.setStatus("current")
_ArubaWiredSwitchS0F96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0F96A = _ArubaWiredSwitchS0F96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 711)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0F96A.setStatus("current")
_ArubaWiredSwitchR9W94A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR9W94A = _ArubaWiredSwitchR9W94A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 800)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR9W94A.setStatus("current")
_ArubaWiredSwitchR9W95A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR9W95A = _ArubaWiredSwitchR9W95A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 801)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR9W95A.setStatus("current")
_ArubaWiredSwitchR9W96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR9W96A = _ArubaWiredSwitchR9W96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 802)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR9W96A.setStatus("current")
_ArubaWiredSwitchR9W97A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR9W97A = _ArubaWiredSwitchR9W97A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 803)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR9W97A.setStatus("current")
_ArubaWiredSwitchS0U60A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U60A = _ArubaWiredSwitchS0U60A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 900)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U60A.setStatus("current")
_ArubaWiredSwitchS0U70A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U70A = _ArubaWiredSwitchS0U70A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 901)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U70A.setStatus("current")
_ArubaWiredSwitchS3L75A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS3L75A = _ArubaWiredSwitchS3L75A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1000)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS3L75A.setStatus("current")
_ArubaWiredSwitchS3L76A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS3L76A = _ArubaWiredSwitchS3L76A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1001)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS3L76A.setStatus("current")
_ArubaWiredSwitchS3L77A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS3L77A = _ArubaWiredSwitchS3L77A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1002)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS3L77A.setStatus("current")
_ArubaWiredSwitchS2P49A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS2P49A = _ArubaWiredSwitchS2P49A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1003)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS2P49A.setStatus("current")
_ArubaWiredSwitchS2P50A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS2P50A = _ArubaWiredSwitchS2P50A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1004)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS2P50A.setStatus("current")
_ArubaWiredSwitchS2P51A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS2P51A = _ArubaWiredSwitchS2P51A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1005)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS2P51A.setStatus("current")
_ArubaWiredSwitchS4P41A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P41A = _ArubaWiredSwitchS4P41A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1050)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P41A.setStatus("current")
_ArubaWiredSwitchS4P42A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P42A = _ArubaWiredSwitchS4P42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1051)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P42A.setStatus("current")
_ArubaWiredSwitchS4P43A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P43A = _ArubaWiredSwitchS4P43A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1052)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P43A.setStatus("current")
_ArubaWiredSwitchS4P44A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P44A = _ArubaWiredSwitchS4P44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1053)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P44A.setStatus("current")
_ArubaWiredSwitchS4P45A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P45A = _ArubaWiredSwitchS4P45A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1054)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P45A.setStatus("current")
_ArubaWiredSwitchS4P46A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P46A = _ArubaWiredSwitchS4P46A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1055)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P46A.setStatus("current")
_ArubaWiredSwitchS4P47A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P47A = _ArubaWiredSwitchS4P47A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1056)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P47A.setStatus("current")
_ArubaWiredSwitchS4P48A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS4P48A = _ArubaWiredSwitchS4P48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 1, 1057)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS4P48A.setStatus("current")
_WndComponentIds_ObjectIdentity = ObjectIdentity
wndComponentIds = _WndComponentIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2)
)
_WndSensors_ObjectIdentity = ObjectIdentity
wndSensors = _WndSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 1)
)
_ArubaWiredTemperatureSensor_ObjectIdentity = ObjectIdentity
arubaWiredTemperatureSensor = _ArubaWiredTemperatureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredTemperatureSensor.setStatus("current")
_ArubaWiredRPMSensor_ObjectIdentity = ObjectIdentity
arubaWiredRPMSensor = _ArubaWiredRPMSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    arubaWiredRPMSensor.setStatus("current")
_ArubaWiredPowerSensor_ObjectIdentity = ObjectIdentity
arubaWiredPowerSensor = _ArubaWiredPowerSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    arubaWiredPowerSensor.setStatus("current")
_WndSlots_ObjectIdentity = ObjectIdentity
wndSlots = _WndSlots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2)
)
_ArubaWiredSwitch8400FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8400FanTraySlot = _ArubaWiredSwitch8400FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8400FanTraySlot.setStatus("current")
_ArubaWiredSwitch8400PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8400PowerSupplySlot = _ArubaWiredSwitch8400PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8400PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch8400ManagementModuleSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8400ManagementModuleSlot = _ArubaWiredSwitch8400ManagementModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8400ManagementModuleSlot.setStatus("current")
_ArubaWiredSwitch8400LineCardSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8400LineCardSlot = _ArubaWiredSwitch8400LineCardSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8400LineCardSlot.setStatus("current")
_ArubaWiredSwitch8400FabricCardSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8400FabricCardSlot = _ArubaWiredSwitch8400FabricCardSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8400FabricCardSlot.setStatus("current")
_ArubaWiredSwitch8400RearDisplayCardSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8400RearDisplayCardSlot = _ArubaWiredSwitch8400RearDisplayCardSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8400RearDisplayCardSlot.setStatus("current")
_ArubaWiredSwitch8320FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8320FanTraySlot = _ArubaWiredSwitch8320FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8320FanTraySlot.setStatus("current")
_ArubaWiredSwitch8320PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8320PowerSupplySlot = _ArubaWiredSwitch8320PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8320PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch8325FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8325FanTraySlot = _ArubaWiredSwitch8325FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8325FanTraySlot.setStatus("current")
_ArubaWiredSwitch8325PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8325PowerSupplySlot = _ArubaWiredSwitch8325PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8325PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch6300FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6300FanTraySlot = _ArubaWiredSwitch6300FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6300FanTraySlot.setStatus("current")
_ArubaWiredSwitch6300PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6300PowerSupplySlot = _ArubaWiredSwitch6300PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6300PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch6400ManagementModuleSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6400ManagementModuleSlot = _ArubaWiredSwitch6400ManagementModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 13)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6400ManagementModuleSlot.setStatus("current")
_ArubaWiredSwitch6400LineCardSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6400LineCardSlot = _ArubaWiredSwitch6400LineCardSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 14)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6400LineCardSlot.setStatus("current")
_ArubaWiredSwitch6400FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6400FanTraySlot = _ArubaWiredSwitch6400FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 15)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6400FanTraySlot.setStatus("current")
_ArubaWiredSwitch6400PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6400PowerSupplySlot = _ArubaWiredSwitch6400PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 16)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6400PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch8360FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8360FanTraySlot = _ArubaWiredSwitch8360FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 17)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8360FanTraySlot.setStatus("current")
_ArubaWiredSwitch8360PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8360PowerSupplySlot = _ArubaWiredSwitch8360PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 18)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8360PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch10000FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch10000FanTraySlot = _ArubaWiredSwitch10000FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 19)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch10000FanTraySlot.setStatus("current")
_ArubaWiredSwitch10000PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch10000PowerSupplySlot = _ArubaWiredSwitch10000PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 20)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch10000PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch9300FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch9300FanTraySlot = _ArubaWiredSwitch9300FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 21)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch9300FanTraySlot.setStatus("current")
_ArubaWiredSwitch9300PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch9300PowerSupplySlot = _ArubaWiredSwitch9300PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 22)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch9300PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch6200FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6200FanTraySlot = _ArubaWiredSwitch6200FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 23)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6200FanTraySlot.setStatus("current")
_ArubaWiredSwitch6200PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch6200PowerSupplySlot = _ArubaWiredSwitch6200PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 24)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch6200PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch8100FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8100FanTraySlot = _ArubaWiredSwitch8100FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 25)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8100FanTraySlot.setStatus("current")
_ArubaWiredSwitch8100PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch8100PowerSupplySlot = _ArubaWiredSwitch8100PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 26)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch8100PowerSupplySlot.setStatus("current")
_ArubaWiredSwitch5420ManagementModuleSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch5420ManagementModuleSlot = _ArubaWiredSwitch5420ManagementModuleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 27)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch5420ManagementModuleSlot.setStatus("current")
_ArubaWiredSwitch5420LineCardSlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch5420LineCardSlot = _ArubaWiredSwitch5420LineCardSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 28)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch5420LineCardSlot.setStatus("current")
_ArubaWiredSwitch5420FanTraySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch5420FanTraySlot = _ArubaWiredSwitch5420FanTraySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 29)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch5420FanTraySlot.setStatus("current")
_ArubaWiredSwitch5420PowerSupplySlot_ObjectIdentity = ObjectIdentity
arubaWiredSwitch5420PowerSupplySlot = _ArubaWiredSwitch5420PowerSupplySlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 2, 30)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch5420PowerSupplySlot.setStatus("current")
_WndModules_ObjectIdentity = ObjectIdentity
wndModules = _WndModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3)
)
_ArubaWiredSwitchManagementModuleJL368A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchManagementModuleJL368A = _ArubaWiredSwitchManagementModuleJL368A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchManagementModuleJL368A.setStatus("current")
_ArubaWiredSwitchModuleJL363A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL363A = _ArubaWiredSwitchModuleJL363A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL363A.setStatus("current")
_ArubaWiredSwitchModuleJL365A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL365A = _ArubaWiredSwitchModuleJL365A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL365A.setStatus("current")
_ArubaWiredSwitchModuleJL366A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL366A = _ArubaWiredSwitchModuleJL366A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL366A.setStatus("current")
_ArubaWiredSwitchFabricModuleJL367A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFabricModuleJL367A = _ArubaWiredSwitchFabricModuleJL367A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFabricModuleJL367A.setStatus("current")
_ArubaWiredSwitchFanModuleJL370A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanModuleJL370A = _ArubaWiredSwitchFanModuleJL370A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanModuleJL370A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL372A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL372A = _ArubaWiredSwitchPowerSupplyUnitJL372A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL372A.setStatus("current")
_ArubaWiredSwitchJL369AFanTray_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL369AFanTray = _ArubaWiredSwitchJL369AFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL369AFanTray.setStatus("current")
_ArubaWiredSwitchModuleJL479A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL479A = _ArubaWiredSwitchModuleJL479A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL479A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL480A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL480A = _ArubaWiredSwitchPowerSupplyUnitJL480A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL480A.setStatus("current")
_ArubaWiredSwitchJL481AFanTray_ObjectIdentity = ObjectIdentity
arubaWiredSwitchJL481AFanTray = _ArubaWiredSwitchJL481AFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 11)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchJL481AFanTray.setStatus("current")
_ArubaWiredSwitchRearDisplayModule8400_ObjectIdentity = ObjectIdentity
arubaWiredSwitchRearDisplayModule8400 = _ArubaWiredSwitchRearDisplayModule8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 12)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchRearDisplayModule8400.setStatus("current")
_ArubaWiredSwitch1GbMaxPort_ObjectIdentity = ObjectIdentity
arubaWiredSwitch1GbMaxPort = _ArubaWiredSwitch1GbMaxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 13)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch1GbMaxPort.setStatus("current")
_ArubaWiredSwitch10GbMaxPort_ObjectIdentity = ObjectIdentity
arubaWiredSwitch10GbMaxPort = _ArubaWiredSwitch10GbMaxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 14)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch10GbMaxPort.setStatus("current")
_ArubaWiredSwitch25GbMaxPort_ObjectIdentity = ObjectIdentity
arubaWiredSwitch25GbMaxPort = _ArubaWiredSwitch25GbMaxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 15)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch25GbMaxPort.setStatus("current")
_ArubaWiredSwitch40GbMaxPort_ObjectIdentity = ObjectIdentity
arubaWiredSwitch40GbMaxPort = _ArubaWiredSwitch40GbMaxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 16)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch40GbMaxPort.setStatus("current")
_ArubaWiredSwitch100GbMaxPort_ObjectIdentity = ObjectIdentity
arubaWiredSwitch100GbMaxPort = _ArubaWiredSwitch100GbMaxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 17)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch100GbMaxPort.setStatus("current")
_ArubaWiredSwitchSmartRatePort_ObjectIdentity = ObjectIdentity
arubaWiredSwitchSmartRatePort = _ArubaWiredSwitchSmartRatePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 18)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchSmartRatePort.setStatus("current")
_ArubaWiredSwitchModuleJL579A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL579A = _ArubaWiredSwitchModuleJL579A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 19)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL579A.setStatus("current")
_ArubaWiredSwitchModuleJL581A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL581A = _ArubaWiredSwitchModuleJL581A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 20)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL581A.setStatus("current")
_ArubaWiredSwitchModuleJL635A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL635A = _ArubaWiredSwitchModuleJL635A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 21)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL635A.setStatus("current")
_ArubaWiredSwitchModuleJL624A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL624A = _ArubaWiredSwitchModuleJL624A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 22)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL624A.setStatus("current")
_ArubaWiredSwitchModuleJL625A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL625A = _ArubaWiredSwitchModuleJL625A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 23)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL625A.setStatus("current")
_ArubaWiredSwitchModuleJL636A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL636A = _ArubaWiredSwitchModuleJL636A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 24)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL636A.setStatus("current")
_ArubaWiredSwitchModuleJL626A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL626A = _ArubaWiredSwitchModuleJL626A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 25)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL626A.setStatus("current")
_ArubaWiredSwitchModuleJL627A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL627A = _ArubaWiredSwitchModuleJL627A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 26)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL627A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL632A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL632A = _ArubaWiredSwitchPowerSupplyUnitJL632A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 27)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL632A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL633A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL633A = _ArubaWiredSwitchPowerSupplyUnitJL633A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 28)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL633A.setStatus("current")
_ArubaWiredSwitchFanTrayJL628A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL628A = _ArubaWiredSwitchFanTrayJL628A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 29)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL628A.setStatus("current")
_ArubaWiredSwitchFanTrayJL629A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL629A = _ArubaWiredSwitchFanTrayJL629A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 30)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL629A.setStatus("current")
_ArubaWiredSwitchFanTrayJL630A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL630A = _ArubaWiredSwitchFanTrayJL630A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 31)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL630A.setStatus("current")
_ArubaWiredSwitchFanTrayJL631A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL631A = _ArubaWiredSwitchFanTrayJL631A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 32)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL631A.setStatus("current")
_ArubaWiredSwitchModuleJL658A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL658A = _ArubaWiredSwitchModuleJL658A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 33)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL658A.setStatus("current")
_ArubaWiredSwitchModuleJL659A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL659A = _ArubaWiredSwitchModuleJL659A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 34)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL659A.setStatus("current")
_ArubaWiredSwitchModuleJL660A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL660A = _ArubaWiredSwitchModuleJL660A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 35)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL660A.setStatus("current")
_ArubaWiredSwitchModuleJL661A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL661A = _ArubaWiredSwitchModuleJL661A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 36)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL661A.setStatus("current")
_ArubaWiredSwitchModuleJL662A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL662A = _ArubaWiredSwitchModuleJL662A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 37)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL662A.setStatus("current")
_ArubaWiredSwitchModuleJL663A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL663A = _ArubaWiredSwitchModuleJL663A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 38)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL663A.setStatus("current")
_ArubaWiredSwitchModuleJL664A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL664A = _ArubaWiredSwitchModuleJL664A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 39)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL664A.setStatus("current")
_ArubaWiredSwitchModuleJL665A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL665A = _ArubaWiredSwitchModuleJL665A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 40)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL665A.setStatus("current")
_ArubaWiredSwitchModuleJL666A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL666A = _ArubaWiredSwitchModuleJL666A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 41)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL666A.setStatus("current")
_ArubaWiredSwitchModuleJL667A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL667A = _ArubaWiredSwitchModuleJL667A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 42)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL667A.setStatus("current")
_ArubaWiredSwitchModuleJL668A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL668A = _ArubaWiredSwitchModuleJL668A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 43)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL668A.setStatus("current")
_ArubaWiredSwitchFanTrayJL669A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL669A = _ArubaWiredSwitchFanTrayJL669A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 44)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL669A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL085A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL085A = _ArubaWiredSwitchPowerSupplyUnitJL085A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 45)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL085A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL086A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL086A = _ArubaWiredSwitchPowerSupplyUnitJL086A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 46)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL086A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL087A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL087A = _ArubaWiredSwitchPowerSupplyUnitJL087A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 47)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL087A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL670A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL670A = _ArubaWiredSwitchPowerSupplyUnitJL670A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 48)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL670A.setStatus("current")
_ArubaWiredSwitch50GbMaxPort_ObjectIdentity = ObjectIdentity
arubaWiredSwitch50GbMaxPort = _ArubaWiredSwitch50GbMaxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 50)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch50GbMaxPort.setStatus("current")
_ArubaWiredSwitchR0X31A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X31A = _ArubaWiredSwitchR0X31A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 51)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X31A.setStatus("current")
_ArubaWiredSwitchR0X32A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X32A = _ArubaWiredSwitchR0X32A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 52)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X32A.setStatus("current")
_ArubaWiredSwitchR0X33A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X33A = _ArubaWiredSwitchR0X33A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 53)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X33A.setStatus("current")
_ArubaWiredSwitchR0X34A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X34A = _ArubaWiredSwitchR0X34A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 54)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X34A.setStatus("current")
_ArubaWiredSwitchR0X35A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X35A = _ArubaWiredSwitchR0X35A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 55)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X35A.setStatus("current")
_ArubaWiredSwitchR0X36A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X36A = _ArubaWiredSwitchR0X36A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 56)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X36A.setStatus("current")
_ArubaWiredSwitchR0X37A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X37A = _ArubaWiredSwitchR0X37A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 57)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X37A.setStatus("current")
_ArubaWiredSwitchR0X38A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X38A = _ArubaWiredSwitchR0X38A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 58)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X38A.setStatus("current")
_ArubaWiredSwitchR0X39A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X39A = _ArubaWiredSwitchR0X39A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 59)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X39A.setStatus("current")
_ArubaWiredSwitchR0X40A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X40A = _ArubaWiredSwitchR0X40A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 60)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X40A.setStatus("current")
_ArubaWiredSwitchR0X41A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X41A = _ArubaWiredSwitchR0X41A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 61)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X41A.setStatus("current")
_ArubaWiredSwitchR0X42A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X42A = _ArubaWiredSwitchR0X42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 62)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X42A.setStatus("current")
_ArubaWiredSwitchR0X43A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X43A = _ArubaWiredSwitchR0X43A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 63)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X43A.setStatus("current")
_ArubaWiredSwitchR0X44A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X44A = _ArubaWiredSwitchR0X44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 64)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X44A.setStatus("current")
_ArubaWiredSwitchR0X45A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X45A = _ArubaWiredSwitchR0X45A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 65)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X45A.setStatus("current")
_ArubaWiredSwitchModuleJL762A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL762A = _ArubaWiredSwitchModuleJL762A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 70)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL762A.setStatus("current")
_ArubaWiredSwitchFanTrayJL761A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL761A = _ArubaWiredSwitchFanTrayJL761A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 71)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL761A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL760A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL760A = _ArubaWiredSwitchPowerSupplyUnitJL760A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 72)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL760A.setStatus("current")
_ArubaWiredSwitchModuleR8S89A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8S89A = _ArubaWiredSwitchModuleR8S89A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 73)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8S89A.setStatus("current")
_ArubaWiredSwitchModuleR8S90A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8S90A = _ArubaWiredSwitchModuleR8S90A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 74)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8S90A.setStatus("current")
_ArubaWiredSwitchModuleR8S91A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8S91A = _ArubaWiredSwitchModuleR8S91A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 75)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8S91A.setStatus("current")
_ArubaWiredSwitchModuleR8S92A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8S92A = _ArubaWiredSwitchModuleR8S92A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 76)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8S92A.setStatus("current")
_ArubaWiredSwitchModuleS0E91A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0E91A = _ArubaWiredSwitchModuleS0E91A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 77)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0E91A.setStatus("current")
_ArubaWiredSwitchModuleS0X44A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0X44A = _ArubaWiredSwitchModuleS0X44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 78)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0X44A.setStatus("current")
_ArubaWiredSwitchModuleS3L75A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS3L75A = _ArubaWiredSwitchModuleS3L75A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 79)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS3L75A.setStatus("current")
_ArubaWiredSwitchModuleS3L76A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS3L76A = _ArubaWiredSwitchModuleS3L76A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 80)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS3L76A.setStatus("current")
_ArubaWiredSwitchModuleS3L77A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS3L77A = _ArubaWiredSwitchModuleS3L77A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 81)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS3L77A.setStatus("current")
_ArubaWiredSwitchModuleS2P49A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS2P49A = _ArubaWiredSwitchModuleS2P49A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 82)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS2P49A.setStatus("current")
_ArubaWiredSwitchModuleS2P50A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS2P50A = _ArubaWiredSwitchModuleS2P50A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 83)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS2P50A.setStatus("current")
_ArubaWiredSwitchModuleS2P51A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS2P51A = _ArubaWiredSwitchModuleS2P51A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 84)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS2P51A.setStatus("current")
_ArubaWiredSwitchModuleJL724A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL724A = _ArubaWiredSwitchModuleJL724A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 90)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL724A.setStatus("current")
_ArubaWiredSwitchModuleJL725A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL725A = _ArubaWiredSwitchModuleJL725A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 91)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL725A.setStatus("current")
_ArubaWiredSwitchModuleJL726A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL726A = _ArubaWiredSwitchModuleJL726A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 92)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL726A.setStatus("current")
_ArubaWiredSwitchModuleJL727A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL727A = _ArubaWiredSwitchModuleJL727A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 93)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL727A.setStatus("current")
_ArubaWiredSwitchModuleJL728A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL728A = _ArubaWiredSwitchModuleJL728A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 94)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL728A.setStatus("current")
_ArubaWiredSwitchModuleR8N85A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N85A = _ArubaWiredSwitchModuleR8N85A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 98)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N85A.setStatus("current")
_ArubaWiredSwitchModuleR8N86A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N86A = _ArubaWiredSwitchModuleR8N86A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 99)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N86A.setStatus("current")
_ArubaWiredSwitchModuleR8N87A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N87A = _ArubaWiredSwitchModuleR8N87A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 100)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N87A.setStatus("current")
_ArubaWiredSwitchModuleR8N88A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N88A = _ArubaWiredSwitchModuleR8N88A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 101)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N88A.setStatus("current")
_ArubaWiredSwitchModuleR8N89A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N89A = _ArubaWiredSwitchModuleR8N89A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 102)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N89A.setStatus("current")
_ArubaWiredSwitchR0X38B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X38B = _ArubaWiredSwitchR0X38B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 103)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X38B.setStatus("current")
_ArubaWiredSwitchR0X39B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X39B = _ArubaWiredSwitchR0X39B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 104)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X39B.setStatus("current")
_ArubaWiredSwitchR0X40B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchR0X40B = _ArubaWiredSwitchR0X40B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 105)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchR0X40B.setStatus("current")
_ArubaWiredSwitchModuleJL675A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL675A = _ArubaWiredSwitchModuleJL675A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 106)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL675A.setStatus("current")
_ArubaWiredSwitchModuleJL676A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL676A = _ArubaWiredSwitchModuleJL676A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 107)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL676A.setStatus("current")
_ArubaWiredSwitchModuleJL677A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL677A = _ArubaWiredSwitchModuleJL677A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 108)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL677A.setStatus("current")
_ArubaWiredSwitchModuleJL678A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL678A = _ArubaWiredSwitchModuleJL678A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 109)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL678A.setStatus("current")
_ArubaWiredSwitchModuleJL679A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL679A = _ArubaWiredSwitchModuleJL679A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 110)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL679A.setStatus("current")
_ArubaWiredSwitchNonPoEPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitchNonPoEPowerSupplyUnit = _ArubaWiredSwitchNonPoEPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 111)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchNonPoEPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitchPoEPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPoEPowerSupplyUnit = _ArubaWiredSwitchPoEPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 112)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPoEPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitchModuleJL717A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL717A = _ArubaWiredSwitchModuleJL717A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 113)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL717A.setStatus("current")
_ArubaWiredSwitchModuleJL718A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL718A = _ArubaWiredSwitchModuleJL718A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 114)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL718A.setStatus("current")
_ArubaWiredSwitchModuleJL719A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL719A = _ArubaWiredSwitchModuleJL719A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 115)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL719A.setStatus("current")
_ArubaWiredSwitchModuleJL720A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL720A = _ArubaWiredSwitchModuleJL720A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 116)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL720A.setStatus("current")
_ArubaWiredSwitchModuleJL721A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL721A = _ArubaWiredSwitchModuleJL721A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 117)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL721A.setStatus("current")
_ArubaWiredSwitchModuleJL722A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL722A = _ArubaWiredSwitchModuleJL722A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 118)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL722A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL600A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL600A = _ArubaWiredSwitchPowerSupplyUnitJL600A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 119)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL600A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL601A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL601A = _ArubaWiredSwitchPowerSupplyUnitJL601A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 120)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL601A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL712A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL712A = _ArubaWiredSwitchPowerSupplyUnitJL712A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 121)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL712A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL713A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL713A = _ArubaWiredSwitchPowerSupplyUnitJL713A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 122)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL713A.setStatus("current")
_ArubaWiredSwitchFanTrayJL714A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL714A = _ArubaWiredSwitchFanTrayJL714A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 123)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL714A.setStatus("current")
_ArubaWiredSwitchFanTrayJL715A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayJL715A = _ArubaWiredSwitchFanTrayJL715A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 124)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayJL715A.setStatus("current")
_ArubaWiredSwitch36WPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitch36WPowerSupplyUnit = _ArubaWiredSwitch36WPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 125)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch36WPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitch65WPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitch65WPowerSupplyUnit = _ArubaWiredSwitch65WPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 126)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch65WPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitch165WPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitch165WPowerSupplyUnit = _ArubaWiredSwitch165WPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 127)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch165WPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitch500WPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitch500WPowerSupplyUnit = _ArubaWiredSwitch500WPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 128)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch500WPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitchModuleJL817A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL817A = _ArubaWiredSwitchModuleJL817A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 129)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL817A.setStatus("current")
_ArubaWiredSwitchModuleJL818A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL818A = _ArubaWiredSwitchModuleJL818A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 130)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL818A.setStatus("current")
_ArubaWiredSwitch300WPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitch300WPowerSupplyUnit = _ArubaWiredSwitch300WPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 131)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch300WPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitchExternalPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitchExternalPowerSupplyUnit = _ArubaWiredSwitchExternalPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 132)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchExternalPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL757A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL757A = _ArubaWiredSwitchPowerSupplyUnitJL757A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 133)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL757A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL758A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL758A = _ArubaWiredSwitchPowerSupplyUnitJL758A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 134)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL758A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitR8R51A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitR8R51A = _ArubaWiredSwitchPowerSupplyUnitR8R51A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 135)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitR8R51A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitR8R52A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitR8R52A = _ArubaWiredSwitchPowerSupplyUnitR8R52A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 136)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitR8R52A.setStatus("current")
_ArubaWiredSwitchFanTrayR8R53A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayR8R53A = _ArubaWiredSwitchFanTrayR8R53A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 137)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayR8R53A.setStatus("current")
_ArubaWiredSwitchFanTrayR8R54A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayR8R54A = _ArubaWiredSwitchFanTrayR8R54A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 138)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayR8R54A.setStatus("current")
_ArubaWiredSwitchModuleR8S96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8S96A = _ArubaWiredSwitchModuleR8S96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 139)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8S96A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL861A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL861A = _ArubaWiredSwitchPowerSupplyUnitJL861A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 140)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL861A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitJL862A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitJL862A = _ArubaWiredSwitchPowerSupplyUnitJL862A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 141)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitJL862A.setStatus("current")
_ArubaWiredSwitchModuleJL717C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL717C = _ArubaWiredSwitchModuleJL717C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 142)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL717C.setStatus("current")
_ArubaWiredSwitchModuleJL718C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL718C = _ArubaWiredSwitchModuleJL718C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 143)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL718C.setStatus("current")
_ArubaWiredSwitchModuleJL719C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL719C = _ArubaWiredSwitchModuleJL719C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 144)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL719C.setStatus("current")
_ArubaWiredSwitchModuleJL720C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL720C = _ArubaWiredSwitchModuleJL720C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 145)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL720C.setStatus("current")
_ArubaWiredSwitchModuleJL721C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL721C = _ArubaWiredSwitchModuleJL721C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 146)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL721C.setStatus("current")
_ArubaWiredSwitchModuleJL722C_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL722C = _ArubaWiredSwitchModuleJL722C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 147)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL722C.setStatus("current")
_ArubaWiredSwitchModuleR8Z96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8Z96A = _ArubaWiredSwitchModuleR8Z96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 148)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8Z96A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitR8Z97A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitR8Z97A = _ArubaWiredSwitchPowerSupplyUnitR8Z97A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 149)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitR8Z97A.setStatus("current")
_ArubaWiredSwitchPowerSupplyUnitR8Z98A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyUnitR8Z98A = _ArubaWiredSwitchPowerSupplyUnitR8Z98A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 150)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyUnitR8Z98A.setStatus("current")
_ArubaWiredSwitchFanTrayR8Z99A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayR8Z99A = _ArubaWiredSwitchFanTrayR8Z99A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 151)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayR8Z99A.setStatus("current")
_ArubaWiredSwitchFanTrayR9A00A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayR9A00A = _ArubaWiredSwitchFanTrayR9A00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 152)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayR9A00A.setStatus("current")
_ArubaWiredSwitch400GbMaxPort_ObjectIdentity = ObjectIdentity
arubaWiredSwitch400GbMaxPort = _ArubaWiredSwitch400GbMaxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 155)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch400GbMaxPort.setStatus("current")
_ArubaWiredSwitchModuleR8Q67A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8Q67A = _ArubaWiredSwitchModuleR8Q67A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 156)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8Q67A.setStatus("current")
_ArubaWiredSwitchModuleR8Q68A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8Q68A = _ArubaWiredSwitchModuleR8Q68A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 157)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8Q68A.setStatus("current")
_ArubaWiredSwitchModuleR8Q69A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8Q69A = _ArubaWiredSwitchModuleR8Q69A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 158)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8Q69A.setStatus("current")
_ArubaWiredSwitchModuleR8Q70A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8Q70A = _ArubaWiredSwitchModuleR8Q70A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 159)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8Q70A.setStatus("current")
_ArubaWiredSwitchModuleR8Q71A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8Q71A = _ArubaWiredSwitchModuleR8Q71A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 160)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8Q71A.setStatus("current")
_ArubaWiredSwitchModuleR8Q72A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8Q72A = _ArubaWiredSwitchModuleR8Q72A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 161)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8Q72A.setStatus("current")
_ArubaWiredSwitchModuleR8V08A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8V08A = _ArubaWiredSwitchModuleR8V08A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 162)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8V08A.setStatus("current")
_ArubaWiredSwitchModuleR8V09A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8V09A = _ArubaWiredSwitchModuleR8V09A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 163)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8V09A.setStatus("current")
_ArubaWiredSwitchModuleR8V10A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8V10A = _ArubaWiredSwitchModuleR8V10A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 164)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8V10A.setStatus("current")
_ArubaWiredSwitchModuleR8V11A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8V11A = _ArubaWiredSwitchModuleR8V11A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 165)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8V11A.setStatus("current")
_ArubaWiredSwitchModuleR8V12A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8V12A = _ArubaWiredSwitchModuleR8V12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 166)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8V12A.setStatus("current")
_ArubaWiredSwitchModuleR8V13A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8V13A = _ArubaWiredSwitchModuleR8V13A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 167)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8V13A.setStatus("current")
_ArubaWiredSwitchModuleR9Y04A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR9Y04A = _ArubaWiredSwitchModuleR9Y04A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 168)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR9Y04A.setStatus("current")
_ArubaWiredSwitchModuleR9Y03A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR9Y03A = _ArubaWiredSwitchModuleR9Y03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 169)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR9Y03A.setStatus("current")
_ArubaWiredSwitch740WPowerSupplyUnit_ObjectIdentity = ObjectIdentity
arubaWiredSwitch740WPowerSupplyUnit = _ArubaWiredSwitch740WPowerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 170)
)
if mibBuilder.loadTexts:
    arubaWiredSwitch740WPowerSupplyUnit.setStatus("current")
_ArubaWiredSwitchModuleR9W94A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR9W94A = _ArubaWiredSwitchModuleR9W94A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 171)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR9W94A.setStatus("current")
_ArubaWiredSwitchModuleR9W95A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR9W95A = _ArubaWiredSwitchModuleR9W95A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 172)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR9W95A.setStatus("current")
_ArubaWiredSwitchModuleR9W96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR9W96A = _ArubaWiredSwitchModuleR9W96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 173)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR9W96A.setStatus("current")
_ArubaWiredSwitchModuleR9W97A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR9W97A = _ArubaWiredSwitchModuleR9W97A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 174)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR9W97A.setStatus("current")
_ArubaWiredSwitchModuleJL724B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL724B = _ArubaWiredSwitchModuleJL724B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 175)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL724B.setStatus("current")
_ArubaWiredSwitchModuleJL725B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL725B = _ArubaWiredSwitchModuleJL725B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 176)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL725B.setStatus("current")
_ArubaWiredSwitchModuleJL726B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL726B = _ArubaWiredSwitchModuleJL726B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 177)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL726B.setStatus("current")
_ArubaWiredSwitchModuleJL727B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL727B = _ArubaWiredSwitchModuleJL727B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 178)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL727B.setStatus("current")
_ArubaWiredSwitchModuleJL728B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL728B = _ArubaWiredSwitchModuleJL728B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 179)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL728B.setStatus("current")
_ArubaWiredSwitchModuleS0M81A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M81A = _ArubaWiredSwitchModuleS0M81A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 180)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M81A.setStatus("current")
_ArubaWiredSwitchModuleS0M82A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M82A = _ArubaWiredSwitchModuleS0M82A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 181)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M82A.setStatus("current")
_ArubaWiredSwitchModuleS0M83A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M83A = _ArubaWiredSwitchModuleS0M83A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 182)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M83A.setStatus("current")
_ArubaWiredSwitchModuleS0M84A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M84A = _ArubaWiredSwitchModuleS0M84A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 183)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M84A.setStatus("current")
_ArubaWiredSwitchModuleS0M85A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M85A = _ArubaWiredSwitchModuleS0M85A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 184)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M85A.setStatus("current")
_ArubaWiredSwitchModuleS0M86A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M86A = _ArubaWiredSwitchModuleS0M86A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 185)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M86A.setStatus("current")
_ArubaWiredSwitchModuleS0M87A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M87A = _ArubaWiredSwitchModuleS0M87A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 186)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M87A.setStatus("current")
_ArubaWiredSwitchModuleS0M88A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M88A = _ArubaWiredSwitchModuleS0M88A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 187)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M88A.setStatus("current")
_ArubaWiredSwitchModuleS0M89A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M89A = _ArubaWiredSwitchModuleS0M89A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 188)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M89A.setStatus("current")
_ArubaWiredSwitchModuleS0M90A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0M90A = _ArubaWiredSwitchModuleS0M90A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 189)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0M90A.setStatus("current")
_ArubaWiredSwitchModuleS0G13A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G13A = _ArubaWiredSwitchModuleS0G13A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 190)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G13A.setStatus("current")
_ArubaWiredSwitchModuleS0G14A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G14A = _ArubaWiredSwitchModuleS0G14A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 191)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G14A.setStatus("current")
_ArubaWiredSwitchModuleS0G15A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G15A = _ArubaWiredSwitchModuleS0G15A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 192)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G15A.setStatus("current")
_ArubaWiredSwitchModuleS0G16A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G16A = _ArubaWiredSwitchModuleS0G16A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 193)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G16A.setStatus("current")
_ArubaWiredSwitchModuleS0G17A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G17A = _ArubaWiredSwitchModuleS0G17A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 194)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G17A.setStatus("current")
_ArubaWiredSwitchModuleS0E48A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0E48A = _ArubaWiredSwitchModuleS0E48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 195)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0E48A.setStatus("current")
_ArubaWiredSwitchModuleS1T83A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS1T83A = _ArubaWiredSwitchModuleS1T83A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 196)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS1T83A.setStatus("current")
_ArubaWiredSwitchModuleS0F99A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0F99A = _ArubaWiredSwitchModuleS0F99A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 197)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0F99A.setStatus("current")
_ArubaWiredSwitchModuleS0G00A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G00A = _ArubaWiredSwitchModuleS0G00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 198)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G00A.setStatus("current")
_ArubaWiredSwitchModuleS0G01A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G01A = _ArubaWiredSwitchModuleS0G01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 199)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G01A.setStatus("current")
_ArubaWiredSwitchModuleS0G02A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G02A = _ArubaWiredSwitchModuleS0G02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 200)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G02A.setStatus("current")
_ArubaWiredSwitchModuleS0G03A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G03A = _ArubaWiredSwitchModuleS0G03A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 201)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G03A.setStatus("current")
_ArubaWiredSwitchModuleS0G04A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G04A = _ArubaWiredSwitchModuleS0G04A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 202)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G04A.setStatus("current")
_ArubaWiredSwitchModuleS0G05A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G05A = _ArubaWiredSwitchModuleS0G05A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 203)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G05A.setStatus("current")
_ArubaWiredSwitchModuleS0G06A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G06A = _ArubaWiredSwitchModuleS0G06A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 204)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G06A.setStatus("current")
_ArubaWiredSwitchModuleS0G95A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G95A = _ArubaWiredSwitchModuleS0G95A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 205)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G95A.setStatus("current")
_ArubaWiredSwitchModuleS0G96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G96A = _ArubaWiredSwitchModuleS0G96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 206)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G96A.setStatus("current")
_ArubaWiredSwitchModuleS0G97A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G97A = _ArubaWiredSwitchModuleS0G97A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 207)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G97A.setStatus("current")
_ArubaWiredSwitchModuleS0G98A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G98A = _ArubaWiredSwitchModuleS0G98A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 208)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G98A.setStatus("current")
_ArubaWiredSwitchModuleS0G12A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G12A = _ArubaWiredSwitchModuleS0G12A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 209)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G12A.setStatus("current")
_ArubaWiredSwitchModuleS0G27A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G27A = _ArubaWiredSwitchModuleS0G27A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 210)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G27A.setStatus("current")
_ArubaWiredSwitchModuleS0G28A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G28A = _ArubaWiredSwitchModuleS0G28A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 211)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G28A.setStatus("current")
_ArubaWiredSwitchModuleS0G29A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G29A = _ArubaWiredSwitchModuleS0G29A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 212)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G29A.setStatus("current")
_ArubaWiredSwitchModuleS0G30A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0G30A = _ArubaWiredSwitchModuleS0G30A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 213)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0G30A.setStatus("current")
_ArubaWiredSwitchS0U55A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U55A = _ArubaWiredSwitchS0U55A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 214)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U55A.setStatus("current")
_ArubaWiredSwitchS0U58A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U58A = _ArubaWiredSwitchS0U58A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 215)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U58A.setStatus("current")
_ArubaWiredSwitchS0U54A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U54A = _ArubaWiredSwitchS0U54A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 216)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U54A.setStatus("current")
_ArubaWiredSwitchS0U53A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U53A = _ArubaWiredSwitchS0U53A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 217)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U53A.setStatus("current")
_ArubaWiredSwitchS0U61A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U61A = _ArubaWiredSwitchS0U61A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 218)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U61A.setStatus("current")
_ArubaWiredSwitchS0U62A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U62A = _ArubaWiredSwitchS0U62A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 219)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U62A.setStatus("current")
_ArubaWiredSwitchS0U63A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U63A = _ArubaWiredSwitchS0U63A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 220)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U63A.setStatus("current")
_ArubaWiredSwitchS0U64A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U64A = _ArubaWiredSwitchS0U64A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 221)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U64A.setStatus("current")
_ArubaWiredSwitchS0U65A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U65A = _ArubaWiredSwitchS0U65A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 222)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U65A.setStatus("current")
_ArubaWiredSwitchS0U66A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U66A = _ArubaWiredSwitchS0U66A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 223)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U66A.setStatus("current")
_ArubaWiredSwitchS0U67A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U67A = _ArubaWiredSwitchS0U67A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 224)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U67A.setStatus("current")
_ArubaWiredSwitchS0U68A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U68A = _ArubaWiredSwitchS0U68A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 225)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U68A.setStatus("current")
_ArubaWiredSwitchS0U71A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U71A = _ArubaWiredSwitchS0U71A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 226)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U71A.setStatus("current")
_ArubaWiredSwitchS0U72A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U72A = _ArubaWiredSwitchS0U72A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 227)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U72A.setStatus("current")
_ArubaWiredSwitchS0U73A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U73A = _ArubaWiredSwitchS0U73A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 228)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U73A.setStatus("current")
_ArubaWiredSwitchS0U74A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U74A = _ArubaWiredSwitchS0U74A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 229)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U74A.setStatus("current")
_ArubaWiredSwitchS0U75A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U75A = _ArubaWiredSwitchS0U75A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 230)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U75A.setStatus("current")
_ArubaWiredSwitchS0U76A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U76A = _ArubaWiredSwitchS0U76A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 231)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U76A.setStatus("current")
_ArubaWiredSwitchS0U77A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U77A = _ArubaWiredSwitchS0U77A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 232)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U77A.setStatus("current")
_ArubaWiredSwitchS0U78A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchS0U78A = _ArubaWiredSwitchS0U78A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 233)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchS0U78A.setStatus("current")
_ArubaWiredSwitchPowerSupplyS0F91A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyS0F91A = _ArubaWiredSwitchPowerSupplyS0F91A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 234)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyS0F91A.setStatus("current")
_ArubaWiredSwitchPowerSupplyS0F92A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchPowerSupplyS0F92A = _ArubaWiredSwitchPowerSupplyS0F92A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 235)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchPowerSupplyS0F92A.setStatus("current")
_ArubaWiredSwitchFanTrayS0F93A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayS0F93A = _ArubaWiredSwitchFanTrayS0F93A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 236)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayS0F93A.setStatus("current")
_ArubaWiredSwitchFanTrayS0F94A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchFanTrayS0F94A = _ArubaWiredSwitchFanTrayS0F94A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 237)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchFanTrayS0F94A.setStatus("current")
_ArubaWiredSwitchModuleS0F95A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0F95A = _ArubaWiredSwitchModuleS0F95A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 238)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0F95A.setStatus("current")
_ArubaWiredSwitchModuleS0F96A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS0F96A = _ArubaWiredSwitchModuleS0F96A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 239)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS0F96A.setStatus("current")
_ArubaWiredSwitchModuleS4K80A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4K80A = _ArubaWiredSwitchModuleS4K80A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 240)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4K80A.setStatus("current")
_ArubaWiredSwitchModuleS4B20A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4B20A = _ArubaWiredSwitchModuleS4B20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 241)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4B20A.setStatus("current")
_ArubaWiredSwitchModuleS4B21A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4B21A = _ArubaWiredSwitchModuleS4B21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 242)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4B21A.setStatus("current")
_ArubaWiredSwitchModuleS4B22A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4B22A = _ArubaWiredSwitchModuleS4B22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 243)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4B22A.setStatus("current")
_ArubaWiredSwitchModuleS4B23A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4B23A = _ArubaWiredSwitchModuleS4B23A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 244)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4B23A.setStatus("current")
_ArubaWiredSwitchModuleS2T42A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS2T42A = _ArubaWiredSwitchModuleS2T42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 245)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS2T42A.setStatus("current")
_ArubaWiredSwitchModuleS2T46A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS2T46A = _ArubaWiredSwitchModuleS2T46A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 246)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS2T46A.setStatus("current")
_ArubaWiredSwitchModuleS2T47A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS2T47A = _ArubaWiredSwitchModuleS2T47A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 247)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS2T47A.setStatus("current")
_ArubaWiredSwitchModuleS2T48A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS2T48A = _ArubaWiredSwitchModuleS2T48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 248)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS2T48A.setStatus("current")
_ArubaWiredSwitchModuleS4A48A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4A48A = _ArubaWiredSwitchModuleS4A48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 249)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4A48A.setStatus("current")
_ArubaWiredSwitchModuleS4P41A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P41A = _ArubaWiredSwitchModuleS4P41A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 250)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P41A.setStatus("current")
_ArubaWiredSwitchModuleS4P42A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P42A = _ArubaWiredSwitchModuleS4P42A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 251)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P42A.setStatus("current")
_ArubaWiredSwitchModuleS4P43A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P43A = _ArubaWiredSwitchModuleS4P43A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 252)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P43A.setStatus("current")
_ArubaWiredSwitchModuleS4P44A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P44A = _ArubaWiredSwitchModuleS4P44A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 253)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P44A.setStatus("current")
_ArubaWiredSwitchModuleS4P45A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P45A = _ArubaWiredSwitchModuleS4P45A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 254)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P45A.setStatus("current")
_ArubaWiredSwitchModuleS4P46A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P46A = _ArubaWiredSwitchModuleS4P46A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 255)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P46A.setStatus("current")
_ArubaWiredSwitchModuleS4P47A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P47A = _ArubaWiredSwitchModuleS4P47A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 256)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P47A.setStatus("current")
_ArubaWiredSwitchModuleS4P48A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4P48A = _ArubaWiredSwitchModuleS4P48A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 257)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4P48A.setStatus("current")
_ArubaWiredSwitchModuleS4U55A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U55A = _ArubaWiredSwitchModuleS4U55A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 258)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U55A.setStatus("current")
_ArubaWiredSwitchModuleS4U56A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U56A = _ArubaWiredSwitchModuleS4U56A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 259)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U56A.setStatus("current")
_ArubaWiredSwitchModuleS4U57A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U57A = _ArubaWiredSwitchModuleS4U57A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 260)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U57A.setStatus("current")
_ArubaWiredSwitchModuleS4U58A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U58A = _ArubaWiredSwitchModuleS4U58A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 261)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U58A.setStatus("current")
_ArubaWiredSwitchModuleS4U59A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U59A = _ArubaWiredSwitchModuleS4U59A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 262)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U59A.setStatus("current")
_ArubaWiredSwitchModuleS4U60A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U60A = _ArubaWiredSwitchModuleS4U60A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 263)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U60A.setStatus("current")
_ArubaWiredSwitchModuleS4U61A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U61A = _ArubaWiredSwitchModuleS4U61A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 264)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U61A.setStatus("current")
_ArubaWiredSwitchModuleS4U62A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U62A = _ArubaWiredSwitchModuleS4U62A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 265)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U62A.setStatus("current")
_ArubaWiredSwitchModuleS4U63A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U63A = _ArubaWiredSwitchModuleS4U63A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 266)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U63A.setStatus("current")
_ArubaWiredSwitchModuleS4U64A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U64A = _ArubaWiredSwitchModuleS4U64A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 267)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U64A.setStatus("current")
_ArubaWiredSwitchModuleS4U65A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U65A = _ArubaWiredSwitchModuleS4U65A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 268)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U65A.setStatus("current")
_ArubaWiredSwitchModuleS4U66A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U66A = _ArubaWiredSwitchModuleS4U66A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 269)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U66A.setStatus("current")
_ArubaWiredSwitchModuleS4U67A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4U67A = _ArubaWiredSwitchModuleS4U67A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 270)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4U67A.setStatus("current")
_ArubaWiredSwitchModule8325HPowerSupply_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModule8325HPowerSupply = _ArubaWiredSwitchModule8325HPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 271)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModule8325HPowerSupply.setStatus("current")
_ArubaWiredSwitchModule8325HFanTray_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModule8325HFanTray = _ArubaWiredSwitchModule8325HFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 272)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModule8325HFanTray.setStatus("current")
_ArubaWiredSwitchModuleR8N85B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N85B = _ArubaWiredSwitchModuleR8N85B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 273)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N85B.setStatus("current")
_ArubaWiredSwitchModuleR8N86B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N86B = _ArubaWiredSwitchModuleR8N86B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 274)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N86B.setStatus("current")
_ArubaWiredSwitchModuleR8N87B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N87B = _ArubaWiredSwitchModuleR8N87B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 275)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N87B.setStatus("current")
_ArubaWiredSwitchModuleR8N88B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N88B = _ArubaWiredSwitchModuleR8N88B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 276)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N88B.setStatus("current")
_ArubaWiredSwitchModuleR8N89B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR8N89B = _ArubaWiredSwitchModuleR8N89B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 277)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR8N89B.setStatus("current")
_ArubaWiredSwitchModuleR9Y03B_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleR9Y03B = _ArubaWiredSwitchModuleR9Y03B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 278)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleR9Y03B.setStatus("current")
_ArubaWiredSwitchModuleS4R20A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R20A = _ArubaWiredSwitchModuleS4R20A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 279)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R20A.setStatus("current")
_ArubaWiredSwitchModuleS4R21A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R21A = _ArubaWiredSwitchModuleS4R21A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 280)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R21A.setStatus("current")
_ArubaWiredSwitchModuleS4R22A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R22A = _ArubaWiredSwitchModuleS4R22A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 281)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R22A.setStatus("current")
_ArubaWiredSwitchModuleS4R23A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R23A = _ArubaWiredSwitchModuleS4R23A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 282)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R23A.setStatus("current")
_ArubaWiredSwitchModuleS4R24A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R24A = _ArubaWiredSwitchModuleS4R24A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 283)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R24A.setStatus("current")
_ArubaWiredSwitchModuleS4R25A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R25A = _ArubaWiredSwitchModuleS4R25A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 284)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R25A.setStatus("current")
_ArubaWiredSwitchModuleS4R26A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R26A = _ArubaWiredSwitchModuleS4R26A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 285)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R26A.setStatus("current")
_ArubaWiredSwitchModuleS4R27A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R27A = _ArubaWiredSwitchModuleS4R27A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 286)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R27A.setStatus("current")
_ArubaWiredSwitchModuleS4R28A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R28A = _ArubaWiredSwitchModuleS4R28A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 287)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R28A.setStatus("current")
_ArubaWiredSwitchModuleS4R29A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R29A = _ArubaWiredSwitchModuleS4R29A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 288)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R29A.setStatus("current")
_ArubaWiredSwitchModuleS4R50A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R50A = _ArubaWiredSwitchModuleS4R50A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 289)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R50A.setStatus("current")
_ArubaWiredSwitchModuleS4R51A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R51A = _ArubaWiredSwitchModuleS4R51A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 290)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R51A.setStatus("current")
_ArubaWiredSwitchModuleS4R52A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R52A = _ArubaWiredSwitchModuleS4R52A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 291)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R52A.setStatus("current")
_ArubaWiredSwitchModuleS4R53A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R53A = _ArubaWiredSwitchModuleS4R53A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 292)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R53A.setStatus("current")
_ArubaWiredSwitchModuleS4R58A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R58A = _ArubaWiredSwitchModuleS4R58A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 293)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R58A.setStatus("current")
_ArubaWiredSwitchModuleS4R59A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleS4R59A = _ArubaWiredSwitchModuleS4R59A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 294)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleS4R59A.setStatus("current")
_ArubaWiredSwitchModuleJL687A_ObjectIdentity = ObjectIdentity
arubaWiredSwitchModuleJL687A = _ArubaWiredSwitchModuleJL687A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 2, 3, 350)
)
if mibBuilder.loadTexts:
    arubaWiredSwitchModuleJL687A.setStatus("current")
_WndFeatures_ObjectIdentity = ObjectIdentity
wndFeatures = _WndFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3)
)
_ArubaWiredLoopProtectMIB_ObjectIdentity = ObjectIdentity
arubaWiredLoopProtectMIB = _ArubaWiredLoopProtectMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 1)
)
_ArubaWiredMclagMIB_ObjectIdentity = ObjectIdentity
arubaWiredMclagMIB = _ArubaWiredMclagMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 2)
)
_ArubaWiredMgmdSnoopingMIB_ObjectIdentity = ObjectIdentity
arubaWiredMgmdSnoopingMIB = _ArubaWiredMgmdSnoopingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3)
)
_ArubaWiredMgmdRmonTrapMIB_ObjectIdentity = ObjectIdentity
arubaWiredMgmdRmonTrapMIB = _ArubaWiredMgmdRmonTrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 4)
)
_ArubaWiredRpvstMIB_ObjectIdentity = ObjectIdentity
arubaWiredRpvstMIB = _ArubaWiredRpvstMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 5)
)
_ArubaWiredMvrpMIB_ObjectIdentity = ObjectIdentity
arubaWiredMvrpMIB = _ArubaWiredMvrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 6)
)
_ArubaWiredVsxMIB_ObjectIdentity = ObjectIdentity
arubaWiredVsxMIB = _ArubaWiredVsxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 7)
)
_ArubaWiredPoeMIB_ObjectIdentity = ObjectIdentity
arubaWiredPoeMIB = _ArubaWiredPoeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 8)
)
_ArubaWiredLldpMIB_ObjectIdentity = ObjectIdentity
arubaWiredLldpMIB = _ArubaWiredLldpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 9)
)
_ArubaWiredVsfMIB_ObjectIdentity = ObjectIdentity
arubaWiredVsfMIB = _ArubaWiredVsfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 10)
)
_ArubaWiredChassisMIB_ObjectIdentity = ObjectIdentity
arubaWiredChassisMIB = _ArubaWiredChassisMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11)
)
_ArubaWiredCiptMIB_ObjectIdentity = ObjectIdentity
arubaWiredCiptMIB = _ArubaWiredCiptMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 12)
)
_ArubaWiredMstpMIB_ObjectIdentity = ObjectIdentity
arubaWiredMstpMIB = _ArubaWiredMstpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 13)
)
_ArubaWiredMdnsMIB_ObjectIdentity = ObjectIdentity
arubaWiredMdnsMIB = _ArubaWiredMdnsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 14)
)
_ArubaWiredVsfv2MIB_ObjectIdentity = ObjectIdentity
arubaWiredVsfv2MIB = _ArubaWiredVsfv2MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 15)
)
_ArubaWiredAAAMIB_ObjectIdentity = ObjectIdentity
arubaWiredAAAMIB = _ArubaWiredAAAMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 16)
)
_ArubaWiredPortAccessMIB_ObjectIdentity = ObjectIdentity
arubaWiredPortAccessMIB = _ArubaWiredPortAccessMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 17)
)
_ArubaWiredPortVlanMIB_ObjectIdentity = ObjectIdentity
arubaWiredPortVlanMIB = _ArubaWiredPortVlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 18)
)
_ArubaWiredMacNotifyMIB_ObjectIdentity = ObjectIdentity
arubaWiredMacNotifyMIB = _ArubaWiredMacNotifyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 19)
)
_ArubaWiredConfigMIB_ObjectIdentity = ObjectIdentity
arubaWiredConfigMIB = _ArubaWiredConfigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 20)
)
_ArubaWiredPortSecurityMIB_ObjectIdentity = ObjectIdentity
arubaWiredPortSecurityMIB = _ArubaWiredPortSecurityMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 21)
)
_ArubaWiredSystemInfoMIB_ObjectIdentity = ObjectIdentity
arubaWiredSystemInfoMIB = _ArubaWiredSystemInfoMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 22)
)
_ArubawiredProviderBridgeMIB_ObjectIdentity = ObjectIdentity
arubawiredProviderBridgeMIB = _ArubawiredProviderBridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 23)
)
_ArubaWiredInterfaceMIB_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceMIB = _ArubaWiredInterfaceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24)
)
_ArubaWiredDistServicesMIB_ObjectIdentity = ObjectIdentity
arubaWiredDistServicesMIB = _ArubaWiredDistServicesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 25)
)
_ArubaWiredSwitchImage_ObjectIdentity = ObjectIdentity
arubaWiredSwitchImage = _ArubaWiredSwitchImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 26)
)
_ArubaWiredPmMIB_ObjectIdentity = ObjectIdentity
arubaWiredPmMIB = _ArubaWiredPmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 27)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    **{"hpe": hpe,
       "hpeNetworking": hpeNetworking,
       "reservedhpeNetworking": reservedhpeNetworking,
       "wiredNetworkingDevices": wiredNetworkingDevices,
       "arubaOS-CX": arubaOS_CX,
       "wndDeviceIds": wndDeviceIds,
       "arubaWiredSwitchJL375A": arubaWiredSwitchJL375A,
       "arubaWiredSwitchJL479A": arubaWiredSwitchJL479A,
       "arubaWiredSwitchJL579A": arubaWiredSwitchJL579A,
       "arubaWiredSwitchJL581A": arubaWiredSwitchJL581A,
       "arubaWiredSwitchJL635A": arubaWiredSwitchJL635A,
       "arubaWiredSwitchS0G12A": arubaWiredSwitchS0G12A,
       "arubaWiredSwitchS4A48A": arubaWiredSwitchS4A48A,
       "arubaWiredSwitchJL636A": arubaWiredSwitchJL636A,
       "arubaWiredSwitchS4B20A": arubaWiredSwitchS4B20A,
       "arubaWiredSwitchS4B21A": arubaWiredSwitchS4B21A,
       "arubaWiredSwitchS4B22A": arubaWiredSwitchS4B22A,
       "arubaWiredSwitchS4B23A": arubaWiredSwitchS4B23A,
       "arubaWiredSwitchS2T42A": arubaWiredSwitchS2T42A,
       "arubaWiredSwitchS2T46A": arubaWiredSwitchS2T46A,
       "arubaWiredSwitchS2T47A": arubaWiredSwitchS2T47A,
       "arubaWiredSwitchS2T48A": arubaWiredSwitchS2T48A,
       "arubaWiredSwitchJL658A": arubaWiredSwitchJL658A,
       "arubaWiredSwitchJL659A": arubaWiredSwitchJL659A,
       "arubaWiredSwitchJL660A": arubaWiredSwitchJL660A,
       "arubaWiredSwitchJL661A": arubaWiredSwitchJL661A,
       "arubaWiredSwitchJL662A": arubaWiredSwitchJL662A,
       "arubaWiredSwitchJL663A": arubaWiredSwitchJL663A,
       "arubaWiredSwitchJL664A": arubaWiredSwitchJL664A,
       "arubaWiredSwitchJL665A": arubaWiredSwitchJL665A,
       "arubaWiredSwitchJL666A": arubaWiredSwitchJL666A,
       "arubaWiredSwitchJL667A": arubaWiredSwitchJL667A,
       "arubaWiredSwitchJL668A": arubaWiredSwitchJL668A,
       "arubaWiredSwitchJL762A": arubaWiredSwitchJL762A,
       "arubaWiredSwitchR8S89A": arubaWiredSwitchR8S89A,
       "arubaWiredSwitchR8S90A": arubaWiredSwitchR8S90A,
       "arubaWiredSwitchR8S91A": arubaWiredSwitchR8S91A,
       "arubaWiredSwitchR8S92A": arubaWiredSwitchR8S92A,
       "arubaWiredSwitchS0E91A": arubaWiredSwitchS0E91A,
       "arubaWiredSwitchS0X44A": arubaWiredSwitchS0X44A,
       "arubaWiredSwitchS0F99A": arubaWiredSwitchS0F99A,
       "arubaWiredSwitchS0G00A": arubaWiredSwitchS0G00A,
       "arubaWiredSwitchS0G01A": arubaWiredSwitchS0G01A,
       "arubaWiredSwitchS0G02A": arubaWiredSwitchS0G02A,
       "arubaWiredSwitchS0G03A": arubaWiredSwitchS0G03A,
       "arubaWiredSwitchS0G04A": arubaWiredSwitchS0G04A,
       "arubaWiredSwitchS0G05A": arubaWiredSwitchS0G05A,
       "arubaWiredSwitchS0G06A": arubaWiredSwitchS0G06A,
       "arubaWiredSwitchS0G95A": arubaWiredSwitchS0G95A,
       "arubaWiredSwitchS0G96A": arubaWiredSwitchS0G96A,
       "arubaWiredSwitchS0G97A": arubaWiredSwitchS0G97A,
       "arubaWiredSwitchS0G98A": arubaWiredSwitchS0G98A,
       "arubaWiredSwitchR0X24A": arubaWiredSwitchR0X24A,
       "arubaWiredSwitchR0X25A": arubaWiredSwitchR0X25A,
       "arubaWiredSwitchR0X24C": arubaWiredSwitchR0X24C,
       "arubaWiredSwitchR0X25C": arubaWiredSwitchR0X25C,
       "arubaWiredSwitchJL675A": arubaWiredSwitchJL675A,
       "arubaWiredSwitchJL676A": arubaWiredSwitchJL676A,
       "arubaWiredSwitchJL677A": arubaWiredSwitchJL677A,
       "arubaWiredSwitchJL678A": arubaWiredSwitchJL678A,
       "arubaWiredSwitchJL679A": arubaWiredSwitchJL679A,
       "arubaWiredSwitchR9Y04A": arubaWiredSwitchR9Y04A,
       "arubaWiredSwitchS4U55A": arubaWiredSwitchS4U55A,
       "arubaWiredSwitchS4U56A": arubaWiredSwitchS4U56A,
       "arubaWiredSwitchS4U57A": arubaWiredSwitchS4U57A,
       "arubaWiredSwitchS4U58A": arubaWiredSwitchS4U58A,
       "arubaWiredSwitchR8N85A": arubaWiredSwitchR8N85A,
       "arubaWiredSwitchR8N86A": arubaWiredSwitchR8N86A,
       "arubaWiredSwitchR8N87A": arubaWiredSwitchR8N87A,
       "arubaWiredSwitchR8N88A": arubaWiredSwitchR8N88A,
       "arubaWiredSwitchR8N89A": arubaWiredSwitchR8N89A,
       "arubaWiredSwitchR8N85B": arubaWiredSwitchR8N85B,
       "arubaWiredSwitchR8N86B": arubaWiredSwitchR8N86B,
       "arubaWiredSwitchR8N87B": arubaWiredSwitchR8N87B,
       "arubaWiredSwitchR8N88B": arubaWiredSwitchR8N88B,
       "arubaWiredSwitchR8N89B": arubaWiredSwitchR8N89B,
       "arubaWiredSwitchR9Y03A": arubaWiredSwitchR9Y03A,
       "arubaWiredSwitchS4U59A": arubaWiredSwitchS4U59A,
       "arubaWiredSwitchS4U60A": arubaWiredSwitchS4U60A,
       "arubaWiredSwitchS4U61A": arubaWiredSwitchS4U61A,
       "arubaWiredSwitchS4U62A": arubaWiredSwitchS4U62A,
       "arubaWiredSwitchR9Y03B": arubaWiredSwitchR9Y03B,
       "arubaWiredSwitchS4R20A": arubaWiredSwitchS4R20A,
       "arubaWiredSwitchS4R21A": arubaWiredSwitchS4R21A,
       "arubaWiredSwitchS4R22A": arubaWiredSwitchS4R22A,
       "arubaWiredSwitchS4R23A": arubaWiredSwitchS4R23A,
       "arubaWiredSwitchS4R24A": arubaWiredSwitchS4R24A,
       "arubaWiredSwitchS4R25A": arubaWiredSwitchS4R25A,
       "arubaWiredSwitchS4R26A": arubaWiredSwitchS4R26A,
       "arubaWiredSwitchS4R27A": arubaWiredSwitchS4R27A,
       "arubaWiredSwitchS4R28A": arubaWiredSwitchS4R28A,
       "arubaWiredSwitchS4R29A": arubaWiredSwitchS4R29A,
       "arubaWiredSwitchJL724A": arubaWiredSwitchJL724A,
       "arubaWiredSwitchJL725A": arubaWiredSwitchJL725A,
       "arubaWiredSwitchJL726A": arubaWiredSwitchJL726A,
       "arubaWiredSwitchJL727A": arubaWiredSwitchJL727A,
       "arubaWiredSwitchJL728A": arubaWiredSwitchJL728A,
       "arubaWiredSwitchJL724B": arubaWiredSwitchJL724B,
       "arubaWiredSwitchJL725B": arubaWiredSwitchJL725B,
       "arubaWiredSwitchJL726B": arubaWiredSwitchJL726B,
       "arubaWiredSwitchJL727B": arubaWiredSwitchJL727B,
       "arubaWiredSwitchJL728B": arubaWiredSwitchJL728B,
       "arubaWiredSwitchS0M81A": arubaWiredSwitchS0M81A,
       "arubaWiredSwitchS0M82A": arubaWiredSwitchS0M82A,
       "arubaWiredSwitchS0M83A": arubaWiredSwitchS0M83A,
       "arubaWiredSwitchS0M84A": arubaWiredSwitchS0M84A,
       "arubaWiredSwitchS0M85A": arubaWiredSwitchS0M85A,
       "arubaWiredSwitchS0M86A": arubaWiredSwitchS0M86A,
       "arubaWiredSwitchS0M87A": arubaWiredSwitchS0M87A,
       "arubaWiredSwitchS0M88A": arubaWiredSwitchS0M88A,
       "arubaWiredSwitchS0M89A": arubaWiredSwitchS0M89A,
       "arubaWiredSwitchS0M90A": arubaWiredSwitchS0M90A,
       "arubaWiredSwitchR8Q67A": arubaWiredSwitchR8Q67A,
       "arubaWiredSwitchR8Q68A": arubaWiredSwitchR8Q68A,
       "arubaWiredSwitchR8Q69A": arubaWiredSwitchR8Q69A,
       "arubaWiredSwitchR8Q70A": arubaWiredSwitchR8Q70A,
       "arubaWiredSwitchR8Q71A": arubaWiredSwitchR8Q71A,
       "arubaWiredSwitchR8Q72A": arubaWiredSwitchR8Q72A,
       "arubaWiredSwitchR8V08A": arubaWiredSwitchR8V08A,
       "arubaWiredSwitchR8V09A": arubaWiredSwitchR8V09A,
       "arubaWiredSwitchR8V10A": arubaWiredSwitchR8V10A,
       "arubaWiredSwitchR8V11A": arubaWiredSwitchR8V11A,
       "arubaWiredSwitchR8V12A": arubaWiredSwitchR8V12A,
       "arubaWiredSwitchR8V13A": arubaWiredSwitchR8V13A,
       "arubaWiredSwitchS4U63A": arubaWiredSwitchS4U63A,
       "arubaWiredSwitchS4U64A": arubaWiredSwitchS4U64A,
       "arubaWiredSwitchS4U65A": arubaWiredSwitchS4U65A,
       "arubaWiredSwitchS4U66A": arubaWiredSwitchS4U66A,
       "arubaWiredSwitchS4U67A": arubaWiredSwitchS4U67A,
       "arubaWiredSwitchS0G13A": arubaWiredSwitchS0G13A,
       "arubaWiredSwitchS0G14A": arubaWiredSwitchS0G14A,
       "arubaWiredSwitchS0G15A": arubaWiredSwitchS0G15A,
       "arubaWiredSwitchS0G16A": arubaWiredSwitchS0G16A,
       "arubaWiredSwitchS0G17A": arubaWiredSwitchS0G17A,
       "arubaWiredSwitchJL717A": arubaWiredSwitchJL717A,
       "arubaWiredSwitchJL718A": arubaWiredSwitchJL718A,
       "arubaWiredSwitchJL719A": arubaWiredSwitchJL719A,
       "arubaWiredSwitchJL720A": arubaWiredSwitchJL720A,
       "arubaWiredSwitchJL721A": arubaWiredSwitchJL721A,
       "arubaWiredSwitchJL722A": arubaWiredSwitchJL722A,
       "arubaWiredSwitchJL717C": arubaWiredSwitchJL717C,
       "arubaWiredSwitchJL718C": arubaWiredSwitchJL718C,
       "arubaWiredSwitchJL719C": arubaWiredSwitchJL719C,
       "arubaWiredSwitchJL720C": arubaWiredSwitchJL720C,
       "arubaWiredSwitchJL721C": arubaWiredSwitchJL721C,
       "arubaWiredSwitchJL722C": arubaWiredSwitchJL722C,
       "arubaWiredSwitchJL817A": arubaWiredSwitchJL817A,
       "arubaWiredSwitchJL818A": arubaWiredSwitchJL818A,
       "arubaWiredSwitchR8S96A": arubaWiredSwitchR8S96A,
       "arubaWiredSwitchS4K80A": arubaWiredSwitchS4K80A,
       "arubaWiredSwitchS4R58A": arubaWiredSwitchS4R58A,
       "arubaWiredSwitchS4R59A": arubaWiredSwitchS4R59A,
       "arubaWiredSwitchR8Z96A": arubaWiredSwitchR8Z96A,
       "arubaWiredSwitchS0F95A": arubaWiredSwitchS0F95A,
       "arubaWiredSwitchS0F96A": arubaWiredSwitchS0F96A,
       "arubaWiredSwitchR9W94A": arubaWiredSwitchR9W94A,
       "arubaWiredSwitchR9W95A": arubaWiredSwitchR9W95A,
       "arubaWiredSwitchR9W96A": arubaWiredSwitchR9W96A,
       "arubaWiredSwitchR9W97A": arubaWiredSwitchR9W97A,
       "arubaWiredSwitchS0U60A": arubaWiredSwitchS0U60A,
       "arubaWiredSwitchS0U70A": arubaWiredSwitchS0U70A,
       "arubaWiredSwitchS3L75A": arubaWiredSwitchS3L75A,
       "arubaWiredSwitchS3L76A": arubaWiredSwitchS3L76A,
       "arubaWiredSwitchS3L77A": arubaWiredSwitchS3L77A,
       "arubaWiredSwitchS2P49A": arubaWiredSwitchS2P49A,
       "arubaWiredSwitchS2P50A": arubaWiredSwitchS2P50A,
       "arubaWiredSwitchS2P51A": arubaWiredSwitchS2P51A,
       "arubaWiredSwitchS4P41A": arubaWiredSwitchS4P41A,
       "arubaWiredSwitchS4P42A": arubaWiredSwitchS4P42A,
       "arubaWiredSwitchS4P43A": arubaWiredSwitchS4P43A,
       "arubaWiredSwitchS4P44A": arubaWiredSwitchS4P44A,
       "arubaWiredSwitchS4P45A": arubaWiredSwitchS4P45A,
       "arubaWiredSwitchS4P46A": arubaWiredSwitchS4P46A,
       "arubaWiredSwitchS4P47A": arubaWiredSwitchS4P47A,
       "arubaWiredSwitchS4P48A": arubaWiredSwitchS4P48A,
       "wndComponentIds": wndComponentIds,
       "wndSensors": wndSensors,
       "arubaWiredTemperatureSensor": arubaWiredTemperatureSensor,
       "arubaWiredRPMSensor": arubaWiredRPMSensor,
       "arubaWiredPowerSensor": arubaWiredPowerSensor,
       "wndSlots": wndSlots,
       "arubaWiredSwitch8400FanTraySlot": arubaWiredSwitch8400FanTraySlot,
       "arubaWiredSwitch8400PowerSupplySlot": arubaWiredSwitch8400PowerSupplySlot,
       "arubaWiredSwitch8400ManagementModuleSlot": arubaWiredSwitch8400ManagementModuleSlot,
       "arubaWiredSwitch8400LineCardSlot": arubaWiredSwitch8400LineCardSlot,
       "arubaWiredSwitch8400FabricCardSlot": arubaWiredSwitch8400FabricCardSlot,
       "arubaWiredSwitch8400RearDisplayCardSlot": arubaWiredSwitch8400RearDisplayCardSlot,
       "arubaWiredSwitch8320FanTraySlot": arubaWiredSwitch8320FanTraySlot,
       "arubaWiredSwitch8320PowerSupplySlot": arubaWiredSwitch8320PowerSupplySlot,
       "arubaWiredSwitch8325FanTraySlot": arubaWiredSwitch8325FanTraySlot,
       "arubaWiredSwitch8325PowerSupplySlot": arubaWiredSwitch8325PowerSupplySlot,
       "arubaWiredSwitch6300FanTraySlot": arubaWiredSwitch6300FanTraySlot,
       "arubaWiredSwitch6300PowerSupplySlot": arubaWiredSwitch6300PowerSupplySlot,
       "arubaWiredSwitch6400ManagementModuleSlot": arubaWiredSwitch6400ManagementModuleSlot,
       "arubaWiredSwitch6400LineCardSlot": arubaWiredSwitch6400LineCardSlot,
       "arubaWiredSwitch6400FanTraySlot": arubaWiredSwitch6400FanTraySlot,
       "arubaWiredSwitch6400PowerSupplySlot": arubaWiredSwitch6400PowerSupplySlot,
       "arubaWiredSwitch8360FanTraySlot": arubaWiredSwitch8360FanTraySlot,
       "arubaWiredSwitch8360PowerSupplySlot": arubaWiredSwitch8360PowerSupplySlot,
       "arubaWiredSwitch10000FanTraySlot": arubaWiredSwitch10000FanTraySlot,
       "arubaWiredSwitch10000PowerSupplySlot": arubaWiredSwitch10000PowerSupplySlot,
       "arubaWiredSwitch9300FanTraySlot": arubaWiredSwitch9300FanTraySlot,
       "arubaWiredSwitch9300PowerSupplySlot": arubaWiredSwitch9300PowerSupplySlot,
       "arubaWiredSwitch6200FanTraySlot": arubaWiredSwitch6200FanTraySlot,
       "arubaWiredSwitch6200PowerSupplySlot": arubaWiredSwitch6200PowerSupplySlot,
       "arubaWiredSwitch8100FanTraySlot": arubaWiredSwitch8100FanTraySlot,
       "arubaWiredSwitch8100PowerSupplySlot": arubaWiredSwitch8100PowerSupplySlot,
       "arubaWiredSwitch5420ManagementModuleSlot": arubaWiredSwitch5420ManagementModuleSlot,
       "arubaWiredSwitch5420LineCardSlot": arubaWiredSwitch5420LineCardSlot,
       "arubaWiredSwitch5420FanTraySlot": arubaWiredSwitch5420FanTraySlot,
       "arubaWiredSwitch5420PowerSupplySlot": arubaWiredSwitch5420PowerSupplySlot,
       "wndModules": wndModules,
       "arubaWiredSwitchManagementModuleJL368A": arubaWiredSwitchManagementModuleJL368A,
       "arubaWiredSwitchModuleJL363A": arubaWiredSwitchModuleJL363A,
       "arubaWiredSwitchModuleJL365A": arubaWiredSwitchModuleJL365A,
       "arubaWiredSwitchModuleJL366A": arubaWiredSwitchModuleJL366A,
       "arubaWiredSwitchFabricModuleJL367A": arubaWiredSwitchFabricModuleJL367A,
       "arubaWiredSwitchFanModuleJL370A": arubaWiredSwitchFanModuleJL370A,
       "arubaWiredSwitchPowerSupplyUnitJL372A": arubaWiredSwitchPowerSupplyUnitJL372A,
       "arubaWiredSwitchJL369AFanTray": arubaWiredSwitchJL369AFanTray,
       "arubaWiredSwitchModuleJL479A": arubaWiredSwitchModuleJL479A,
       "arubaWiredSwitchPowerSupplyUnitJL480A": arubaWiredSwitchPowerSupplyUnitJL480A,
       "arubaWiredSwitchJL481AFanTray": arubaWiredSwitchJL481AFanTray,
       "arubaWiredSwitchRearDisplayModule8400": arubaWiredSwitchRearDisplayModule8400,
       "arubaWiredSwitch1GbMaxPort": arubaWiredSwitch1GbMaxPort,
       "arubaWiredSwitch10GbMaxPort": arubaWiredSwitch10GbMaxPort,
       "arubaWiredSwitch25GbMaxPort": arubaWiredSwitch25GbMaxPort,
       "arubaWiredSwitch40GbMaxPort": arubaWiredSwitch40GbMaxPort,
       "arubaWiredSwitch100GbMaxPort": arubaWiredSwitch100GbMaxPort,
       "arubaWiredSwitchSmartRatePort": arubaWiredSwitchSmartRatePort,
       "arubaWiredSwitchModuleJL579A": arubaWiredSwitchModuleJL579A,
       "arubaWiredSwitchModuleJL581A": arubaWiredSwitchModuleJL581A,
       "arubaWiredSwitchModuleJL635A": arubaWiredSwitchModuleJL635A,
       "arubaWiredSwitchModuleJL624A": arubaWiredSwitchModuleJL624A,
       "arubaWiredSwitchModuleJL625A": arubaWiredSwitchModuleJL625A,
       "arubaWiredSwitchModuleJL636A": arubaWiredSwitchModuleJL636A,
       "arubaWiredSwitchModuleJL626A": arubaWiredSwitchModuleJL626A,
       "arubaWiredSwitchModuleJL627A": arubaWiredSwitchModuleJL627A,
       "arubaWiredSwitchPowerSupplyUnitJL632A": arubaWiredSwitchPowerSupplyUnitJL632A,
       "arubaWiredSwitchPowerSupplyUnitJL633A": arubaWiredSwitchPowerSupplyUnitJL633A,
       "arubaWiredSwitchFanTrayJL628A": arubaWiredSwitchFanTrayJL628A,
       "arubaWiredSwitchFanTrayJL629A": arubaWiredSwitchFanTrayJL629A,
       "arubaWiredSwitchFanTrayJL630A": arubaWiredSwitchFanTrayJL630A,
       "arubaWiredSwitchFanTrayJL631A": arubaWiredSwitchFanTrayJL631A,
       "arubaWiredSwitchModuleJL658A": arubaWiredSwitchModuleJL658A,
       "arubaWiredSwitchModuleJL659A": arubaWiredSwitchModuleJL659A,
       "arubaWiredSwitchModuleJL660A": arubaWiredSwitchModuleJL660A,
       "arubaWiredSwitchModuleJL661A": arubaWiredSwitchModuleJL661A,
       "arubaWiredSwitchModuleJL662A": arubaWiredSwitchModuleJL662A,
       "arubaWiredSwitchModuleJL663A": arubaWiredSwitchModuleJL663A,
       "arubaWiredSwitchModuleJL664A": arubaWiredSwitchModuleJL664A,
       "arubaWiredSwitchModuleJL665A": arubaWiredSwitchModuleJL665A,
       "arubaWiredSwitchModuleJL666A": arubaWiredSwitchModuleJL666A,
       "arubaWiredSwitchModuleJL667A": arubaWiredSwitchModuleJL667A,
       "arubaWiredSwitchModuleJL668A": arubaWiredSwitchModuleJL668A,
       "arubaWiredSwitchFanTrayJL669A": arubaWiredSwitchFanTrayJL669A,
       "arubaWiredSwitchPowerSupplyUnitJL085A": arubaWiredSwitchPowerSupplyUnitJL085A,
       "arubaWiredSwitchPowerSupplyUnitJL086A": arubaWiredSwitchPowerSupplyUnitJL086A,
       "arubaWiredSwitchPowerSupplyUnitJL087A": arubaWiredSwitchPowerSupplyUnitJL087A,
       "arubaWiredSwitchPowerSupplyUnitJL670A": arubaWiredSwitchPowerSupplyUnitJL670A,
       "arubaWiredSwitch50GbMaxPort": arubaWiredSwitch50GbMaxPort,
       "arubaWiredSwitchR0X31A": arubaWiredSwitchR0X31A,
       "arubaWiredSwitchR0X32A": arubaWiredSwitchR0X32A,
       "arubaWiredSwitchR0X33A": arubaWiredSwitchR0X33A,
       "arubaWiredSwitchR0X34A": arubaWiredSwitchR0X34A,
       "arubaWiredSwitchR0X35A": arubaWiredSwitchR0X35A,
       "arubaWiredSwitchR0X36A": arubaWiredSwitchR0X36A,
       "arubaWiredSwitchR0X37A": arubaWiredSwitchR0X37A,
       "arubaWiredSwitchR0X38A": arubaWiredSwitchR0X38A,
       "arubaWiredSwitchR0X39A": arubaWiredSwitchR0X39A,
       "arubaWiredSwitchR0X40A": arubaWiredSwitchR0X40A,
       "arubaWiredSwitchR0X41A": arubaWiredSwitchR0X41A,
       "arubaWiredSwitchR0X42A": arubaWiredSwitchR0X42A,
       "arubaWiredSwitchR0X43A": arubaWiredSwitchR0X43A,
       "arubaWiredSwitchR0X44A": arubaWiredSwitchR0X44A,
       "arubaWiredSwitchR0X45A": arubaWiredSwitchR0X45A,
       "arubaWiredSwitchModuleJL762A": arubaWiredSwitchModuleJL762A,
       "arubaWiredSwitchFanTrayJL761A": arubaWiredSwitchFanTrayJL761A,
       "arubaWiredSwitchPowerSupplyUnitJL760A": arubaWiredSwitchPowerSupplyUnitJL760A,
       "arubaWiredSwitchModuleR8S89A": arubaWiredSwitchModuleR8S89A,
       "arubaWiredSwitchModuleR8S90A": arubaWiredSwitchModuleR8S90A,
       "arubaWiredSwitchModuleR8S91A": arubaWiredSwitchModuleR8S91A,
       "arubaWiredSwitchModuleR8S92A": arubaWiredSwitchModuleR8S92A,
       "arubaWiredSwitchModuleS0E91A": arubaWiredSwitchModuleS0E91A,
       "arubaWiredSwitchModuleS0X44A": arubaWiredSwitchModuleS0X44A,
       "arubaWiredSwitchModuleS3L75A": arubaWiredSwitchModuleS3L75A,
       "arubaWiredSwitchModuleS3L76A": arubaWiredSwitchModuleS3L76A,
       "arubaWiredSwitchModuleS3L77A": arubaWiredSwitchModuleS3L77A,
       "arubaWiredSwitchModuleS2P49A": arubaWiredSwitchModuleS2P49A,
       "arubaWiredSwitchModuleS2P50A": arubaWiredSwitchModuleS2P50A,
       "arubaWiredSwitchModuleS2P51A": arubaWiredSwitchModuleS2P51A,
       "arubaWiredSwitchModuleJL724A": arubaWiredSwitchModuleJL724A,
       "arubaWiredSwitchModuleJL725A": arubaWiredSwitchModuleJL725A,
       "arubaWiredSwitchModuleJL726A": arubaWiredSwitchModuleJL726A,
       "arubaWiredSwitchModuleJL727A": arubaWiredSwitchModuleJL727A,
       "arubaWiredSwitchModuleJL728A": arubaWiredSwitchModuleJL728A,
       "arubaWiredSwitchModuleR8N85A": arubaWiredSwitchModuleR8N85A,
       "arubaWiredSwitchModuleR8N86A": arubaWiredSwitchModuleR8N86A,
       "arubaWiredSwitchModuleR8N87A": arubaWiredSwitchModuleR8N87A,
       "arubaWiredSwitchModuleR8N88A": arubaWiredSwitchModuleR8N88A,
       "arubaWiredSwitchModuleR8N89A": arubaWiredSwitchModuleR8N89A,
       "arubaWiredSwitchR0X38B": arubaWiredSwitchR0X38B,
       "arubaWiredSwitchR0X39B": arubaWiredSwitchR0X39B,
       "arubaWiredSwitchR0X40B": arubaWiredSwitchR0X40B,
       "arubaWiredSwitchModuleJL675A": arubaWiredSwitchModuleJL675A,
       "arubaWiredSwitchModuleJL676A": arubaWiredSwitchModuleJL676A,
       "arubaWiredSwitchModuleJL677A": arubaWiredSwitchModuleJL677A,
       "arubaWiredSwitchModuleJL678A": arubaWiredSwitchModuleJL678A,
       "arubaWiredSwitchModuleJL679A": arubaWiredSwitchModuleJL679A,
       "arubaWiredSwitchNonPoEPowerSupplyUnit": arubaWiredSwitchNonPoEPowerSupplyUnit,
       "arubaWiredSwitchPoEPowerSupplyUnit": arubaWiredSwitchPoEPowerSupplyUnit,
       "arubaWiredSwitchModuleJL717A": arubaWiredSwitchModuleJL717A,
       "arubaWiredSwitchModuleJL718A": arubaWiredSwitchModuleJL718A,
       "arubaWiredSwitchModuleJL719A": arubaWiredSwitchModuleJL719A,
       "arubaWiredSwitchModuleJL720A": arubaWiredSwitchModuleJL720A,
       "arubaWiredSwitchModuleJL721A": arubaWiredSwitchModuleJL721A,
       "arubaWiredSwitchModuleJL722A": arubaWiredSwitchModuleJL722A,
       "arubaWiredSwitchPowerSupplyUnitJL600A": arubaWiredSwitchPowerSupplyUnitJL600A,
       "arubaWiredSwitchPowerSupplyUnitJL601A": arubaWiredSwitchPowerSupplyUnitJL601A,
       "arubaWiredSwitchPowerSupplyUnitJL712A": arubaWiredSwitchPowerSupplyUnitJL712A,
       "arubaWiredSwitchPowerSupplyUnitJL713A": arubaWiredSwitchPowerSupplyUnitJL713A,
       "arubaWiredSwitchFanTrayJL714A": arubaWiredSwitchFanTrayJL714A,
       "arubaWiredSwitchFanTrayJL715A": arubaWiredSwitchFanTrayJL715A,
       "arubaWiredSwitch36WPowerSupplyUnit": arubaWiredSwitch36WPowerSupplyUnit,
       "arubaWiredSwitch65WPowerSupplyUnit": arubaWiredSwitch65WPowerSupplyUnit,
       "arubaWiredSwitch165WPowerSupplyUnit": arubaWiredSwitch165WPowerSupplyUnit,
       "arubaWiredSwitch500WPowerSupplyUnit": arubaWiredSwitch500WPowerSupplyUnit,
       "arubaWiredSwitchModuleJL817A": arubaWiredSwitchModuleJL817A,
       "arubaWiredSwitchModuleJL818A": arubaWiredSwitchModuleJL818A,
       "arubaWiredSwitch300WPowerSupplyUnit": arubaWiredSwitch300WPowerSupplyUnit,
       "arubaWiredSwitchExternalPowerSupplyUnit": arubaWiredSwitchExternalPowerSupplyUnit,
       "arubaWiredSwitchPowerSupplyUnitJL757A": arubaWiredSwitchPowerSupplyUnitJL757A,
       "arubaWiredSwitchPowerSupplyUnitJL758A": arubaWiredSwitchPowerSupplyUnitJL758A,
       "arubaWiredSwitchPowerSupplyUnitR8R51A": arubaWiredSwitchPowerSupplyUnitR8R51A,
       "arubaWiredSwitchPowerSupplyUnitR8R52A": arubaWiredSwitchPowerSupplyUnitR8R52A,
       "arubaWiredSwitchFanTrayR8R53A": arubaWiredSwitchFanTrayR8R53A,
       "arubaWiredSwitchFanTrayR8R54A": arubaWiredSwitchFanTrayR8R54A,
       "arubaWiredSwitchModuleR8S96A": arubaWiredSwitchModuleR8S96A,
       "arubaWiredSwitchPowerSupplyUnitJL861A": arubaWiredSwitchPowerSupplyUnitJL861A,
       "arubaWiredSwitchPowerSupplyUnitJL862A": arubaWiredSwitchPowerSupplyUnitJL862A,
       "arubaWiredSwitchModuleJL717C": arubaWiredSwitchModuleJL717C,
       "arubaWiredSwitchModuleJL718C": arubaWiredSwitchModuleJL718C,
       "arubaWiredSwitchModuleJL719C": arubaWiredSwitchModuleJL719C,
       "arubaWiredSwitchModuleJL720C": arubaWiredSwitchModuleJL720C,
       "arubaWiredSwitchModuleJL721C": arubaWiredSwitchModuleJL721C,
       "arubaWiredSwitchModuleJL722C": arubaWiredSwitchModuleJL722C,
       "arubaWiredSwitchModuleR8Z96A": arubaWiredSwitchModuleR8Z96A,
       "arubaWiredSwitchPowerSupplyUnitR8Z97A": arubaWiredSwitchPowerSupplyUnitR8Z97A,
       "arubaWiredSwitchPowerSupplyUnitR8Z98A": arubaWiredSwitchPowerSupplyUnitR8Z98A,
       "arubaWiredSwitchFanTrayR8Z99A": arubaWiredSwitchFanTrayR8Z99A,
       "arubaWiredSwitchFanTrayR9A00A": arubaWiredSwitchFanTrayR9A00A,
       "arubaWiredSwitch400GbMaxPort": arubaWiredSwitch400GbMaxPort,
       "arubaWiredSwitchModuleR8Q67A": arubaWiredSwitchModuleR8Q67A,
       "arubaWiredSwitchModuleR8Q68A": arubaWiredSwitchModuleR8Q68A,
       "arubaWiredSwitchModuleR8Q69A": arubaWiredSwitchModuleR8Q69A,
       "arubaWiredSwitchModuleR8Q70A": arubaWiredSwitchModuleR8Q70A,
       "arubaWiredSwitchModuleR8Q71A": arubaWiredSwitchModuleR8Q71A,
       "arubaWiredSwitchModuleR8Q72A": arubaWiredSwitchModuleR8Q72A,
       "arubaWiredSwitchModuleR8V08A": arubaWiredSwitchModuleR8V08A,
       "arubaWiredSwitchModuleR8V09A": arubaWiredSwitchModuleR8V09A,
       "arubaWiredSwitchModuleR8V10A": arubaWiredSwitchModuleR8V10A,
       "arubaWiredSwitchModuleR8V11A": arubaWiredSwitchModuleR8V11A,
       "arubaWiredSwitchModuleR8V12A": arubaWiredSwitchModuleR8V12A,
       "arubaWiredSwitchModuleR8V13A": arubaWiredSwitchModuleR8V13A,
       "arubaWiredSwitchModuleR9Y04A": arubaWiredSwitchModuleR9Y04A,
       "arubaWiredSwitchModuleR9Y03A": arubaWiredSwitchModuleR9Y03A,
       "arubaWiredSwitch740WPowerSupplyUnit": arubaWiredSwitch740WPowerSupplyUnit,
       "arubaWiredSwitchModuleR9W94A": arubaWiredSwitchModuleR9W94A,
       "arubaWiredSwitchModuleR9W95A": arubaWiredSwitchModuleR9W95A,
       "arubaWiredSwitchModuleR9W96A": arubaWiredSwitchModuleR9W96A,
       "arubaWiredSwitchModuleR9W97A": arubaWiredSwitchModuleR9W97A,
       "arubaWiredSwitchModuleJL724B": arubaWiredSwitchModuleJL724B,
       "arubaWiredSwitchModuleJL725B": arubaWiredSwitchModuleJL725B,
       "arubaWiredSwitchModuleJL726B": arubaWiredSwitchModuleJL726B,
       "arubaWiredSwitchModuleJL727B": arubaWiredSwitchModuleJL727B,
       "arubaWiredSwitchModuleJL728B": arubaWiredSwitchModuleJL728B,
       "arubaWiredSwitchModuleS0M81A": arubaWiredSwitchModuleS0M81A,
       "arubaWiredSwitchModuleS0M82A": arubaWiredSwitchModuleS0M82A,
       "arubaWiredSwitchModuleS0M83A": arubaWiredSwitchModuleS0M83A,
       "arubaWiredSwitchModuleS0M84A": arubaWiredSwitchModuleS0M84A,
       "arubaWiredSwitchModuleS0M85A": arubaWiredSwitchModuleS0M85A,
       "arubaWiredSwitchModuleS0M86A": arubaWiredSwitchModuleS0M86A,
       "arubaWiredSwitchModuleS0M87A": arubaWiredSwitchModuleS0M87A,
       "arubaWiredSwitchModuleS0M88A": arubaWiredSwitchModuleS0M88A,
       "arubaWiredSwitchModuleS0M89A": arubaWiredSwitchModuleS0M89A,
       "arubaWiredSwitchModuleS0M90A": arubaWiredSwitchModuleS0M90A,
       "arubaWiredSwitchModuleS0G13A": arubaWiredSwitchModuleS0G13A,
       "arubaWiredSwitchModuleS0G14A": arubaWiredSwitchModuleS0G14A,
       "arubaWiredSwitchModuleS0G15A": arubaWiredSwitchModuleS0G15A,
       "arubaWiredSwitchModuleS0G16A": arubaWiredSwitchModuleS0G16A,
       "arubaWiredSwitchModuleS0G17A": arubaWiredSwitchModuleS0G17A,
       "arubaWiredSwitchModuleS0E48A": arubaWiredSwitchModuleS0E48A,
       "arubaWiredSwitchModuleS1T83A": arubaWiredSwitchModuleS1T83A,
       "arubaWiredSwitchModuleS0F99A": arubaWiredSwitchModuleS0F99A,
       "arubaWiredSwitchModuleS0G00A": arubaWiredSwitchModuleS0G00A,
       "arubaWiredSwitchModuleS0G01A": arubaWiredSwitchModuleS0G01A,
       "arubaWiredSwitchModuleS0G02A": arubaWiredSwitchModuleS0G02A,
       "arubaWiredSwitchModuleS0G03A": arubaWiredSwitchModuleS0G03A,
       "arubaWiredSwitchModuleS0G04A": arubaWiredSwitchModuleS0G04A,
       "arubaWiredSwitchModuleS0G05A": arubaWiredSwitchModuleS0G05A,
       "arubaWiredSwitchModuleS0G06A": arubaWiredSwitchModuleS0G06A,
       "arubaWiredSwitchModuleS0G95A": arubaWiredSwitchModuleS0G95A,
       "arubaWiredSwitchModuleS0G96A": arubaWiredSwitchModuleS0G96A,
       "arubaWiredSwitchModuleS0G97A": arubaWiredSwitchModuleS0G97A,
       "arubaWiredSwitchModuleS0G98A": arubaWiredSwitchModuleS0G98A,
       "arubaWiredSwitchModuleS0G12A": arubaWiredSwitchModuleS0G12A,
       "arubaWiredSwitchModuleS0G27A": arubaWiredSwitchModuleS0G27A,
       "arubaWiredSwitchModuleS0G28A": arubaWiredSwitchModuleS0G28A,
       "arubaWiredSwitchModuleS0G29A": arubaWiredSwitchModuleS0G29A,
       "arubaWiredSwitchModuleS0G30A": arubaWiredSwitchModuleS0G30A,
       "arubaWiredSwitchS0U55A": arubaWiredSwitchS0U55A,
       "arubaWiredSwitchS0U58A": arubaWiredSwitchS0U58A,
       "arubaWiredSwitchS0U54A": arubaWiredSwitchS0U54A,
       "arubaWiredSwitchS0U53A": arubaWiredSwitchS0U53A,
       "arubaWiredSwitchS0U61A": arubaWiredSwitchS0U61A,
       "arubaWiredSwitchS0U62A": arubaWiredSwitchS0U62A,
       "arubaWiredSwitchS0U63A": arubaWiredSwitchS0U63A,
       "arubaWiredSwitchS0U64A": arubaWiredSwitchS0U64A,
       "arubaWiredSwitchS0U65A": arubaWiredSwitchS0U65A,
       "arubaWiredSwitchS0U66A": arubaWiredSwitchS0U66A,
       "arubaWiredSwitchS0U67A": arubaWiredSwitchS0U67A,
       "arubaWiredSwitchS0U68A": arubaWiredSwitchS0U68A,
       "arubaWiredSwitchS0U71A": arubaWiredSwitchS0U71A,
       "arubaWiredSwitchS0U72A": arubaWiredSwitchS0U72A,
       "arubaWiredSwitchS0U73A": arubaWiredSwitchS0U73A,
       "arubaWiredSwitchS0U74A": arubaWiredSwitchS0U74A,
       "arubaWiredSwitchS0U75A": arubaWiredSwitchS0U75A,
       "arubaWiredSwitchS0U76A": arubaWiredSwitchS0U76A,
       "arubaWiredSwitchS0U77A": arubaWiredSwitchS0U77A,
       "arubaWiredSwitchS0U78A": arubaWiredSwitchS0U78A,
       "arubaWiredSwitchPowerSupplyS0F91A": arubaWiredSwitchPowerSupplyS0F91A,
       "arubaWiredSwitchPowerSupplyS0F92A": arubaWiredSwitchPowerSupplyS0F92A,
       "arubaWiredSwitchFanTrayS0F93A": arubaWiredSwitchFanTrayS0F93A,
       "arubaWiredSwitchFanTrayS0F94A": arubaWiredSwitchFanTrayS0F94A,
       "arubaWiredSwitchModuleS0F95A": arubaWiredSwitchModuleS0F95A,
       "arubaWiredSwitchModuleS0F96A": arubaWiredSwitchModuleS0F96A,
       "arubaWiredSwitchModuleS4K80A": arubaWiredSwitchModuleS4K80A,
       "arubaWiredSwitchModuleS4B20A": arubaWiredSwitchModuleS4B20A,
       "arubaWiredSwitchModuleS4B21A": arubaWiredSwitchModuleS4B21A,
       "arubaWiredSwitchModuleS4B22A": arubaWiredSwitchModuleS4B22A,
       "arubaWiredSwitchModuleS4B23A": arubaWiredSwitchModuleS4B23A,
       "arubaWiredSwitchModuleS2T42A": arubaWiredSwitchModuleS2T42A,
       "arubaWiredSwitchModuleS2T46A": arubaWiredSwitchModuleS2T46A,
       "arubaWiredSwitchModuleS2T47A": arubaWiredSwitchModuleS2T47A,
       "arubaWiredSwitchModuleS2T48A": arubaWiredSwitchModuleS2T48A,
       "arubaWiredSwitchModuleS4A48A": arubaWiredSwitchModuleS4A48A,
       "arubaWiredSwitchModuleS4P41A": arubaWiredSwitchModuleS4P41A,
       "arubaWiredSwitchModuleS4P42A": arubaWiredSwitchModuleS4P42A,
       "arubaWiredSwitchModuleS4P43A": arubaWiredSwitchModuleS4P43A,
       "arubaWiredSwitchModuleS4P44A": arubaWiredSwitchModuleS4P44A,
       "arubaWiredSwitchModuleS4P45A": arubaWiredSwitchModuleS4P45A,
       "arubaWiredSwitchModuleS4P46A": arubaWiredSwitchModuleS4P46A,
       "arubaWiredSwitchModuleS4P47A": arubaWiredSwitchModuleS4P47A,
       "arubaWiredSwitchModuleS4P48A": arubaWiredSwitchModuleS4P48A,
       "arubaWiredSwitchModuleS4U55A": arubaWiredSwitchModuleS4U55A,
       "arubaWiredSwitchModuleS4U56A": arubaWiredSwitchModuleS4U56A,
       "arubaWiredSwitchModuleS4U57A": arubaWiredSwitchModuleS4U57A,
       "arubaWiredSwitchModuleS4U58A": arubaWiredSwitchModuleS4U58A,
       "arubaWiredSwitchModuleS4U59A": arubaWiredSwitchModuleS4U59A,
       "arubaWiredSwitchModuleS4U60A": arubaWiredSwitchModuleS4U60A,
       "arubaWiredSwitchModuleS4U61A": arubaWiredSwitchModuleS4U61A,
       "arubaWiredSwitchModuleS4U62A": arubaWiredSwitchModuleS4U62A,
       "arubaWiredSwitchModuleS4U63A": arubaWiredSwitchModuleS4U63A,
       "arubaWiredSwitchModuleS4U64A": arubaWiredSwitchModuleS4U64A,
       "arubaWiredSwitchModuleS4U65A": arubaWiredSwitchModuleS4U65A,
       "arubaWiredSwitchModuleS4U66A": arubaWiredSwitchModuleS4U66A,
       "arubaWiredSwitchModuleS4U67A": arubaWiredSwitchModuleS4U67A,
       "arubaWiredSwitchModule8325HPowerSupply": arubaWiredSwitchModule8325HPowerSupply,
       "arubaWiredSwitchModule8325HFanTray": arubaWiredSwitchModule8325HFanTray,
       "arubaWiredSwitchModuleR8N85B": arubaWiredSwitchModuleR8N85B,
       "arubaWiredSwitchModuleR8N86B": arubaWiredSwitchModuleR8N86B,
       "arubaWiredSwitchModuleR8N87B": arubaWiredSwitchModuleR8N87B,
       "arubaWiredSwitchModuleR8N88B": arubaWiredSwitchModuleR8N88B,
       "arubaWiredSwitchModuleR8N89B": arubaWiredSwitchModuleR8N89B,
       "arubaWiredSwitchModuleR9Y03B": arubaWiredSwitchModuleR9Y03B,
       "arubaWiredSwitchModuleS4R20A": arubaWiredSwitchModuleS4R20A,
       "arubaWiredSwitchModuleS4R21A": arubaWiredSwitchModuleS4R21A,
       "arubaWiredSwitchModuleS4R22A": arubaWiredSwitchModuleS4R22A,
       "arubaWiredSwitchModuleS4R23A": arubaWiredSwitchModuleS4R23A,
       "arubaWiredSwitchModuleS4R24A": arubaWiredSwitchModuleS4R24A,
       "arubaWiredSwitchModuleS4R25A": arubaWiredSwitchModuleS4R25A,
       "arubaWiredSwitchModuleS4R26A": arubaWiredSwitchModuleS4R26A,
       "arubaWiredSwitchModuleS4R27A": arubaWiredSwitchModuleS4R27A,
       "arubaWiredSwitchModuleS4R28A": arubaWiredSwitchModuleS4R28A,
       "arubaWiredSwitchModuleS4R29A": arubaWiredSwitchModuleS4R29A,
       "arubaWiredSwitchModuleS4R50A": arubaWiredSwitchModuleS4R50A,
       "arubaWiredSwitchModuleS4R51A": arubaWiredSwitchModuleS4R51A,
       "arubaWiredSwitchModuleS4R52A": arubaWiredSwitchModuleS4R52A,
       "arubaWiredSwitchModuleS4R53A": arubaWiredSwitchModuleS4R53A,
       "arubaWiredSwitchModuleS4R58A": arubaWiredSwitchModuleS4R58A,
       "arubaWiredSwitchModuleS4R59A": arubaWiredSwitchModuleS4R59A,
       "arubaWiredSwitchModuleJL687A": arubaWiredSwitchModuleJL687A,
       "wndFeatures": wndFeatures,
       "arubaWiredLoopProtectMIB": arubaWiredLoopProtectMIB,
       "arubaWiredMclagMIB": arubaWiredMclagMIB,
       "arubaWiredMgmdSnoopingMIB": arubaWiredMgmdSnoopingMIB,
       "arubaWiredMgmdRmonTrapMIB": arubaWiredMgmdRmonTrapMIB,
       "arubaWiredRpvstMIB": arubaWiredRpvstMIB,
       "arubaWiredMvrpMIB": arubaWiredMvrpMIB,
       "arubaWiredVsxMIB": arubaWiredVsxMIB,
       "arubaWiredPoeMIB": arubaWiredPoeMIB,
       "arubaWiredLldpMIB": arubaWiredLldpMIB,
       "arubaWiredVsfMIB": arubaWiredVsfMIB,
       "arubaWiredChassisMIB": arubaWiredChassisMIB,
       "arubaWiredCiptMIB": arubaWiredCiptMIB,
       "arubaWiredMstpMIB": arubaWiredMstpMIB,
       "arubaWiredMdnsMIB": arubaWiredMdnsMIB,
       "arubaWiredVsfv2MIB": arubaWiredVsfv2MIB,
       "arubaWiredAAAMIB": arubaWiredAAAMIB,
       "arubaWiredPortAccessMIB": arubaWiredPortAccessMIB,
       "arubaWiredPortVlanMIB": arubaWiredPortVlanMIB,
       "arubaWiredMacNotifyMIB": arubaWiredMacNotifyMIB,
       "arubaWiredConfigMIB": arubaWiredConfigMIB,
       "arubaWiredPortSecurityMIB": arubaWiredPortSecurityMIB,
       "arubaWiredSystemInfoMIB": arubaWiredSystemInfoMIB,
       "arubawiredProviderBridgeMIB": arubawiredProviderBridgeMIB,
       "arubaWiredInterfaceMIB": arubaWiredInterfaceMIB,
       "arubaWiredDistServicesMIB": arubaWiredDistServicesMIB,
       "arubaWiredSwitchImage": arubaWiredSwitchImage,
       "arubaWiredPmMIB": arubaWiredPmMIB}
)
