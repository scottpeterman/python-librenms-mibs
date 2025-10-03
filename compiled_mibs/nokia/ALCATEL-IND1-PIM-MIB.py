# SNMP MIB module (ALCATEL-IND1-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-PIM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:55 2025
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

(routingIND1Pim,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Pim")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1PIMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PIMMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PIMMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBObjects = _AlcatelIND1PIMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1)
)
_AlaPimsmGlobalConfig_ObjectIdentity = ObjectIdentity
alaPimsmGlobalConfig = _AlaPimsmGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1)
)


class _AlaPimsmAdminStatus_Type(Integer32):
    """Custom type alaPimsmAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmAdminStatus_Type.__name__ = "Integer32"
_AlaPimsmAdminStatus_Object = MibScalar
alaPimsmAdminStatus = _AlaPimsmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 1),
    _AlaPimsmAdminStatus_Type()
)
alaPimsmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminStatus.setStatus("current")
_AlaPimsmAdminBSRAddress_Type = IpAddress
_AlaPimsmAdminBSRAddress_Object = MibScalar
alaPimsmAdminBSRAddress = _AlaPimsmAdminBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 2),
    _AlaPimsmAdminBSRAddress_Type()
)
alaPimsmAdminBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimsmAdminBSRAddress.setStatus("obsolete")


class _AlaPimsmAdminBSRHashmasklen_Type(Integer32):
    """Custom type alaPimsmAdminBSRHashmasklen based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AlaPimsmAdminBSRHashmasklen_Type.__name__ = "Integer32"
_AlaPimsmAdminBSRHashmasklen_Object = MibScalar
alaPimsmAdminBSRHashmasklen = _AlaPimsmAdminBSRHashmasklen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 3),
    _AlaPimsmAdminBSRHashmasklen_Type()
)
alaPimsmAdminBSRHashmasklen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminBSRHashmasklen.setStatus("obsolete")


class _AlaPimsmAdminBSRPriority_Type(Integer32):
    """Custom type alaPimsmAdminBSRPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaPimsmAdminBSRPriority_Type.__name__ = "Integer32"
_AlaPimsmAdminBSRPriority_Object = MibScalar
alaPimsmAdminBSRPriority = _AlaPimsmAdminBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 4),
    _AlaPimsmAdminBSRPriority_Type()
)
alaPimsmAdminBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimsmAdminBSRPriority.setStatus("obsolete")


class _AlaPimsmCRPExpiryTime_Type(Integer32):
    """Custom type alaPimsmCRPExpiryTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AlaPimsmCRPExpiryTime_Type.__name__ = "Integer32"
_AlaPimsmCRPExpiryTime_Object = MibScalar
alaPimsmCRPExpiryTime = _AlaPimsmCRPExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 5),
    _AlaPimsmCRPExpiryTime_Type()
)
alaPimsmCRPExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmCRPExpiryTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    alaPimsmCRPExpiryTime.setUnits("seconds")


class _AlaPimsmCRPInterval_Type(Integer32):
    """Custom type alaPimsmCRPInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AlaPimsmCRPInterval_Type.__name__ = "Integer32"
_AlaPimsmCRPInterval_Object = MibScalar
alaPimsmCRPInterval = _AlaPimsmCRPInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 6),
    _AlaPimsmCRPInterval_Type()
)
alaPimsmCRPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmCRPInterval.setStatus("obsolete")
_AlaPimsmAdminCRPAddress_Type = IpAddress
_AlaPimsmAdminCRPAddress_Object = MibScalar
alaPimsmAdminCRPAddress = _AlaPimsmAdminCRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 7),
    _AlaPimsmAdminCRPAddress_Type()
)
alaPimsmAdminCRPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminCRPAddress.setStatus("obsolete")


class _AlaPimsmAdminCRPPriority_Type(Integer32):
    """Custom type alaPimsmAdminCRPPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaPimsmAdminCRPPriority_Type.__name__ = "Integer32"
_AlaPimsmAdminCRPPriority_Object = MibScalar
alaPimsmAdminCRPPriority = _AlaPimsmAdminCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 8),
    _AlaPimsmAdminCRPPriority_Type()
)
alaPimsmAdminCRPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminCRPPriority.setStatus("obsolete")


class _AlaPimsmDataTimeout_Type(Integer32):
    """Custom type alaPimsmDataTimeout based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AlaPimsmDataTimeout_Type.__name__ = "Integer32"
_AlaPimsmDataTimeout_Object = MibScalar
alaPimsmDataTimeout = _AlaPimsmDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 9),
    _AlaPimsmDataTimeout_Type()
)
alaPimsmDataTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDataTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    alaPimsmDataTimeout.setUnits("seconds")


class _AlaPimsmMaxRPs_Type(Integer32):
    """Custom type alaPimsmMaxRPs based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaPimsmMaxRPs_Type.__name__ = "Integer32"
_AlaPimsmMaxRPs_Object = MibScalar
alaPimsmMaxRPs = _AlaPimsmMaxRPs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 10),
    _AlaPimsmMaxRPs_Type()
)
alaPimsmMaxRPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmMaxRPs.setStatus("current")


class _AlaPimsmProbeTime_Type(Integer32):
    """Custom type alaPimsmProbeTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AlaPimsmProbeTime_Type.__name__ = "Integer32"
_AlaPimsmProbeTime_Object = MibScalar
alaPimsmProbeTime = _AlaPimsmProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 11),
    _AlaPimsmProbeTime_Type()
)
alaPimsmProbeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmProbeTime.setStatus("current")
if mibBuilder.loadTexts:
    alaPimsmProbeTime.setUnits("seconds")


class _AlaPimsmOldRegisterMessageSupport_Type(Integer32):
    """Custom type alaPimsmOldRegisterMessageSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("header", 1),
          ("full", 2))
    )


_AlaPimsmOldRegisterMessageSupport_Type.__name__ = "Integer32"
_AlaPimsmOldRegisterMessageSupport_Object = MibScalar
alaPimsmOldRegisterMessageSupport = _AlaPimsmOldRegisterMessageSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 12),
    _AlaPimsmOldRegisterMessageSupport_Type()
)
alaPimsmOldRegisterMessageSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmOldRegisterMessageSupport.setStatus("current")


class _AlaPimsmRegisterSuppressionTimeout_Type(Integer32):
    """Custom type alaPimsmRegisterSuppressionTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AlaPimsmRegisterSuppressionTimeout_Type.__name__ = "Integer32"
_AlaPimsmRegisterSuppressionTimeout_Object = MibScalar
alaPimsmRegisterSuppressionTimeout = _AlaPimsmRegisterSuppressionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 13),
    _AlaPimsmRegisterSuppressionTimeout_Type()
)
alaPimsmRegisterSuppressionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmRegisterSuppressionTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    alaPimsmRegisterSuppressionTimeout.setUnits("seconds")


class _AlaPimsmAdminStaticRPConfig_Type(Integer32):
    """Custom type alaPimsmAdminStaticRPConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmAdminStaticRPConfig_Type.__name__ = "Integer32"
_AlaPimsmAdminStaticRPConfig_Object = MibScalar
alaPimsmAdminStaticRPConfig = _AlaPimsmAdminStaticRPConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 14),
    _AlaPimsmAdminStaticRPConfig_Type()
)
alaPimsmAdminStaticRPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminStaticRPConfig.setStatus("obsolete")
_AlaPimsmStaticRPTable_Object = MibTable
alaPimsmStaticRPTable = _AlaPimsmStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaPimsmStaticRPTable.setStatus("obsolete")
_AlaPimsmStaticRPEntry_Object = MibTableRow
alaPimsmStaticRPEntry = _AlaPimsmStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 15, 1)
)
alaPimsmStaticRPEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-MIB", "alaPimsmStaticRPGroupAddress"),
    (0, "ALCATEL-IND1-PIM-MIB", "alaPimsmStaticRPGroupMask"),
    (0, "ALCATEL-IND1-PIM-MIB", "alaPimsmStaticRPAddress"),
)
if mibBuilder.loadTexts:
    alaPimsmStaticRPEntry.setStatus("obsolete")
_AlaPimsmStaticRPGroupAddress_Type = IpAddress
_AlaPimsmStaticRPGroupAddress_Object = MibTableColumn
alaPimsmStaticRPGroupAddress = _AlaPimsmStaticRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 15, 1, 1),
    _AlaPimsmStaticRPGroupAddress_Type()
)
alaPimsmStaticRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimsmStaticRPGroupAddress.setStatus("obsolete")
_AlaPimsmStaticRPGroupMask_Type = IpAddress
_AlaPimsmStaticRPGroupMask_Object = MibTableColumn
alaPimsmStaticRPGroupMask = _AlaPimsmStaticRPGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 15, 1, 2),
    _AlaPimsmStaticRPGroupMask_Type()
)
alaPimsmStaticRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimsmStaticRPGroupMask.setStatus("obsolete")
_AlaPimsmStaticRPAddress_Type = IpAddress
_AlaPimsmStaticRPAddress_Object = MibTableColumn
alaPimsmStaticRPAddress = _AlaPimsmStaticRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 15, 1, 3),
    _AlaPimsmStaticRPAddress_Type()
)
alaPimsmStaticRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimsmStaticRPAddress.setStatus("obsolete")
_AlaPimsmStaticRPRowStatus_Type = RowStatus
_AlaPimsmStaticRPRowStatus_Object = MibTableColumn
alaPimsmStaticRPRowStatus = _AlaPimsmStaticRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 15, 1, 4),
    _AlaPimsmStaticRPRowStatus_Type()
)
alaPimsmStaticRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimsmStaticRPRowStatus.setStatus("obsolete")


class _AlaPimsmAdminSPTConfig_Type(Integer32):
    """Custom type alaPimsmAdminSPTConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmAdminSPTConfig_Type.__name__ = "Integer32"
_AlaPimsmAdminSPTConfig_Object = MibScalar
alaPimsmAdminSPTConfig = _AlaPimsmAdminSPTConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 16),
    _AlaPimsmAdminSPTConfig_Type()
)
alaPimsmAdminSPTConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmAdminSPTConfig.setStatus("current")


class _AlaPimsmRPThreshold_Type(Integer32):
    """Custom type alaPimsmRPThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaPimsmRPThreshold_Type.__name__ = "Integer32"
_AlaPimsmRPThreshold_Object = MibScalar
alaPimsmRPThreshold = _AlaPimsmRPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 17),
    _AlaPimsmRPThreshold_Type()
)
alaPimsmRPThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmRPThreshold.setStatus("current")


class _AlaPimsmV6AdminStatus_Type(Integer32):
    """Custom type alaPimsmV6AdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmV6AdminStatus_Type.__name__ = "Integer32"
_AlaPimsmV6AdminStatus_Object = MibScalar
alaPimsmV6AdminStatus = _AlaPimsmV6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 18),
    _AlaPimsmV6AdminStatus_Type()
)
alaPimsmV6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmV6AdminStatus.setStatus("current")


class _AlaPimsmV6SPTConfig_Type(Integer32):
    """Custom type alaPimsmV6SPTConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmV6SPTConfig_Type.__name__ = "Integer32"
_AlaPimsmV6SPTConfig_Object = MibScalar
alaPimsmV6SPTConfig = _AlaPimsmV6SPTConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 19),
    _AlaPimsmV6SPTConfig_Type()
)
alaPimsmV6SPTConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmV6SPTConfig.setStatus("current")


class _AlaPimsmV6RPSwitchover_Type(Integer32):
    """Custom type alaPimsmV6RPSwitchover based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmV6RPSwitchover_Type.__name__ = "Integer32"
_AlaPimsmV6RPSwitchover_Object = MibScalar
alaPimsmV6RPSwitchover = _AlaPimsmV6RPSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 1, 20),
    _AlaPimsmV6RPSwitchover_Type()
)
alaPimsmV6RPSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmV6RPSwitchover.setStatus("current")
_AlaPimsmDebugConfig_ObjectIdentity = ObjectIdentity
alaPimsmDebugConfig = _AlaPimsmDebugConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2)
)


class _AlaPimsmDebugLevel_Type(Integer32):
    """Custom type alaPimsmDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaPimsmDebugLevel_Type.__name__ = "Integer32"
_AlaPimsmDebugLevel_Object = MibScalar
alaPimsmDebugLevel = _AlaPimsmDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 1),
    _AlaPimsmDebugLevel_Type()
)
alaPimsmDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugLevel.setStatus("deprecated")


class _AlaPimsmDebugError_Type(Integer32):
    """Custom type alaPimsmDebugError based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugError_Type.__name__ = "Integer32"
_AlaPimsmDebugError_Object = MibScalar
alaPimsmDebugError = _AlaPimsmDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 2),
    _AlaPimsmDebugError_Type()
)
alaPimsmDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugError.setStatus("deprecated")


class _AlaPimsmDebugHello_Type(Integer32):
    """Custom type alaPimsmDebugHello based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugHello_Type.__name__ = "Integer32"
_AlaPimsmDebugHello_Object = MibScalar
alaPimsmDebugHello = _AlaPimsmDebugHello_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 3),
    _AlaPimsmDebugHello_Type()
)
alaPimsmDebugHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugHello.setStatus("deprecated")


class _AlaPimsmDebugNbr_Type(Integer32):
    """Custom type alaPimsmDebugNbr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugNbr_Type.__name__ = "Integer32"
_AlaPimsmDebugNbr_Object = MibScalar
alaPimsmDebugNbr = _AlaPimsmDebugNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 4),
    _AlaPimsmDebugNbr_Type()
)
alaPimsmDebugNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugNbr.setStatus("deprecated")


class _AlaPimsmDebugBootstrap_Type(Integer32):
    """Custom type alaPimsmDebugBootstrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugBootstrap_Type.__name__ = "Integer32"
_AlaPimsmDebugBootstrap_Object = MibScalar
alaPimsmDebugBootstrap = _AlaPimsmDebugBootstrap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 5),
    _AlaPimsmDebugBootstrap_Type()
)
alaPimsmDebugBootstrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugBootstrap.setStatus("deprecated")


class _AlaPimsmDebugCRP_Type(Integer32):
    """Custom type alaPimsmDebugCRP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugCRP_Type.__name__ = "Integer32"
_AlaPimsmDebugCRP_Object = MibScalar
alaPimsmDebugCRP = _AlaPimsmDebugCRP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 6),
    _AlaPimsmDebugCRP_Type()
)
alaPimsmDebugCRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugCRP.setStatus("deprecated")


class _AlaPimsmDebugRoute_Type(Integer32):
    """Custom type alaPimsmDebugRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugRoute_Type.__name__ = "Integer32"
_AlaPimsmDebugRoute_Object = MibScalar
alaPimsmDebugRoute = _AlaPimsmDebugRoute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 7),
    _AlaPimsmDebugRoute_Type()
)
alaPimsmDebugRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugRoute.setStatus("deprecated")


class _AlaPimsmDebugJoinPrune_Type(Integer32):
    """Custom type alaPimsmDebugJoinPrune based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugJoinPrune_Type.__name__ = "Integer32"
_AlaPimsmDebugJoinPrune_Object = MibScalar
alaPimsmDebugJoinPrune = _AlaPimsmDebugJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 8),
    _AlaPimsmDebugJoinPrune_Type()
)
alaPimsmDebugJoinPrune.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugJoinPrune.setStatus("deprecated")


class _AlaPimsmDebugAssert_Type(Integer32):
    """Custom type alaPimsmDebugAssert based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugAssert_Type.__name__ = "Integer32"
_AlaPimsmDebugAssert_Object = MibScalar
alaPimsmDebugAssert = _AlaPimsmDebugAssert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 9),
    _AlaPimsmDebugAssert_Type()
)
alaPimsmDebugAssert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugAssert.setStatus("deprecated")


class _AlaPimsmDebugTime_Type(Integer32):
    """Custom type alaPimsmDebugTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugTime_Type.__name__ = "Integer32"
_AlaPimsmDebugTime_Object = MibScalar
alaPimsmDebugTime = _AlaPimsmDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 10),
    _AlaPimsmDebugTime_Type()
)
alaPimsmDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugTime.setStatus("deprecated")


class _AlaPimsmDebugIgmp_Type(Integer32):
    """Custom type alaPimsmDebugIgmp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugIgmp_Type.__name__ = "Integer32"
_AlaPimsmDebugIgmp_Object = MibScalar
alaPimsmDebugIgmp = _AlaPimsmDebugIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 11),
    _AlaPimsmDebugIgmp_Type()
)
alaPimsmDebugIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugIgmp.setStatus("deprecated")


class _AlaPimsmDebugSpt_Type(Integer32):
    """Custom type alaPimsmDebugSpt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugSpt_Type.__name__ = "Integer32"
_AlaPimsmDebugSpt_Object = MibScalar
alaPimsmDebugSpt = _AlaPimsmDebugSpt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 12),
    _AlaPimsmDebugSpt_Type()
)
alaPimsmDebugSpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugSpt.setStatus("deprecated")


class _AlaPimsmDebugMip_Type(Integer32):
    """Custom type alaPimsmDebugMip based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugMip_Type.__name__ = "Integer32"
_AlaPimsmDebugMip_Object = MibScalar
alaPimsmDebugMip = _AlaPimsmDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 13),
    _AlaPimsmDebugMip_Type()
)
alaPimsmDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugMip.setStatus("deprecated")


class _AlaPimsmDebugInit_Type(Integer32):
    """Custom type alaPimsmDebugInit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugInit_Type.__name__ = "Integer32"
_AlaPimsmDebugInit_Object = MibScalar
alaPimsmDebugInit = _AlaPimsmDebugInit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 14),
    _AlaPimsmDebugInit_Type()
)
alaPimsmDebugInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugInit.setStatus("deprecated")


class _AlaPimsmDebugTm_Type(Integer32):
    """Custom type alaPimsmDebugTm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugTm_Type.__name__ = "Integer32"
_AlaPimsmDebugTm_Object = MibScalar
alaPimsmDebugTm = _AlaPimsmDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 15),
    _AlaPimsmDebugTm_Type()
)
alaPimsmDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugTm.setStatus("deprecated")


class _AlaPimsmDebugIpmrm_Type(Integer32):
    """Custom type alaPimsmDebugIpmrm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugIpmrm_Type.__name__ = "Integer32"
_AlaPimsmDebugIpmrm_Object = MibScalar
alaPimsmDebugIpmrm = _AlaPimsmDebugIpmrm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 16),
    _AlaPimsmDebugIpmrm_Type()
)
alaPimsmDebugIpmrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugIpmrm.setStatus("deprecated")


class _AlaPimsmDebugMisc_Type(Integer32):
    """Custom type alaPimsmDebugMisc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugMisc_Type.__name__ = "Integer32"
_AlaPimsmDebugMisc_Object = MibScalar
alaPimsmDebugMisc = _AlaPimsmDebugMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 17),
    _AlaPimsmDebugMisc_Type()
)
alaPimsmDebugMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugMisc.setStatus("deprecated")


class _AlaPimsmDebugAll_Type(Integer32):
    """Custom type alaPimsmDebugAll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimsmDebugAll_Type.__name__ = "Integer32"
_AlaPimsmDebugAll_Object = MibScalar
alaPimsmDebugAll = _AlaPimsmDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 2, 18),
    _AlaPimsmDebugAll_Type()
)
alaPimsmDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimsmDebugAll.setStatus("deprecated")
_AlaPimdmGlobalConfig_ObjectIdentity = ObjectIdentity
alaPimdmGlobalConfig = _AlaPimdmGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 3)
)


class _AlaPimdmAdminStatus_Type(Integer32):
    """Custom type alaPimdmAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimdmAdminStatus_Type.__name__ = "Integer32"
_AlaPimdmAdminStatus_Object = MibScalar
alaPimdmAdminStatus = _AlaPimdmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 3, 1),
    _AlaPimdmAdminStatus_Type()
)
alaPimdmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmAdminStatus.setStatus("current")


class _AlaPimdmStateRefreshTimeToLive_Type(Integer32):
    """Custom type alaPimdmStateRefreshTimeToLive based on Integer32"""
    defaultValue = 16


_AlaPimdmStateRefreshTimeToLive_Type.__name__ = "Integer32"
_AlaPimdmStateRefreshTimeToLive_Object = MibScalar
alaPimdmStateRefreshTimeToLive = _AlaPimdmStateRefreshTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 3, 2),
    _AlaPimdmStateRefreshTimeToLive_Type()
)
alaPimdmStateRefreshTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmStateRefreshTimeToLive.setStatus("current")


class _AlaPimdmStateRefreshLimitInterval_Type(TimeTicks):
    """Custom type alaPimdmStateRefreshLimitInterval based on TimeTicks"""
    defaultValue = 0


_AlaPimdmStateRefreshLimitInterval_Type.__name__ = "TimeTicks"
_AlaPimdmStateRefreshLimitInterval_Object = MibScalar
alaPimdmStateRefreshLimitInterval = _AlaPimdmStateRefreshLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 3, 3),
    _AlaPimdmStateRefreshLimitInterval_Type()
)
alaPimdmStateRefreshLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmStateRefreshLimitInterval.setStatus("current")


class _AlaPimdmV6AdminStatus_Type(Integer32):
    """Custom type alaPimdmV6AdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaPimdmV6AdminStatus_Type.__name__ = "Integer32"
_AlaPimdmV6AdminStatus_Object = MibScalar
alaPimdmV6AdminStatus = _AlaPimdmV6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 1, 3, 4),
    _AlaPimdmV6AdminStatus_Type()
)
alaPimdmV6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimdmV6AdminStatus.setStatus("current")
_AlcatelIND1PIMMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBConformance = _AlcatelIND1PIMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2)
)
_AlcatelIND1PIMMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBCompliances = _AlcatelIND1PIMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2, 1)
)
_AlcatelIND1PIMMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PIMMIBGroups = _AlcatelIND1PIMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2, 2)
)

# Managed Objects groups

alaPimsmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2, 2, 1)
)
alaPimsmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminBSRAddress"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminBSRHashmasklen"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminBSRPriority"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmCRPExpiryTime"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmCRPInterval"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminCRPAddress"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminCRPPriority"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDataTimeout"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmMaxRPs"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmProbeTime"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmOldRegisterMessageSupport"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmRegisterSuppressionTimeout"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminStaticRPConfig"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmStaticRPRowStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmAdminSPTConfig"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmRPThreshold"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6AdminStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6SPTConfig"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmV6RPSwitchover"))
)
if mibBuilder.loadTexts:
    alaPimsmConfigMIBGroup.setStatus("current")

alaPimsmDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2, 2, 2)
)
alaPimsmDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugLevel"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugError"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugHello"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugNbr"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugBootstrap"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugCRP"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugRoute"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugJoinPrune"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugAssert"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugTime"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugIgmp"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugSpt"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugMip"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugInit"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugTm"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugIpmrm"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugMisc"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugAll"))
)
if mibBuilder.loadTexts:
    alaPimsmDebugMIBGroup.setStatus("current")

alaPimdmConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2, 2, 3)
)
alaPimdmConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimdmAdminStatus"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmStateRefreshTimeToLive"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmStateRefreshLimitInterval"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimdmV6AdminStatus"))
)
if mibBuilder.loadTexts:
    alaPimdmConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaPimsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2, 1, 1)
)
alaPimsmCompliance.setObjects(
      *(("ALCATEL-IND1-PIM-MIB", "alaPimsmConfigMIBGroup"),
        ("ALCATEL-IND1-PIM-MIB", "alaPimsmDebugMIBGroup"))
)
if mibBuilder.loadTexts:
    alaPimsmCompliance.setStatus(
        "current"
    )

alaPimdmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 6, 1, 2, 1, 2)
)
alaPimdmCompliance.setObjects(
    ("ALCATEL-IND1-PIM-MIB", "alaPimdmConfigMIBGroup")
)
if mibBuilder.loadTexts:
    alaPimdmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PIM-MIB",
    **{"alcatelIND1PIMMIB": alcatelIND1PIMMIB,
       "alcatelIND1PIMMIBObjects": alcatelIND1PIMMIBObjects,
       "alaPimsmGlobalConfig": alaPimsmGlobalConfig,
       "alaPimsmAdminStatus": alaPimsmAdminStatus,
       "alaPimsmAdminBSRAddress": alaPimsmAdminBSRAddress,
       "alaPimsmAdminBSRHashmasklen": alaPimsmAdminBSRHashmasklen,
       "alaPimsmAdminBSRPriority": alaPimsmAdminBSRPriority,
       "alaPimsmCRPExpiryTime": alaPimsmCRPExpiryTime,
       "alaPimsmCRPInterval": alaPimsmCRPInterval,
       "alaPimsmAdminCRPAddress": alaPimsmAdminCRPAddress,
       "alaPimsmAdminCRPPriority": alaPimsmAdminCRPPriority,
       "alaPimsmDataTimeout": alaPimsmDataTimeout,
       "alaPimsmMaxRPs": alaPimsmMaxRPs,
       "alaPimsmProbeTime": alaPimsmProbeTime,
       "alaPimsmOldRegisterMessageSupport": alaPimsmOldRegisterMessageSupport,
       "alaPimsmRegisterSuppressionTimeout": alaPimsmRegisterSuppressionTimeout,
       "alaPimsmAdminStaticRPConfig": alaPimsmAdminStaticRPConfig,
       "alaPimsmStaticRPTable": alaPimsmStaticRPTable,
       "alaPimsmStaticRPEntry": alaPimsmStaticRPEntry,
       "alaPimsmStaticRPGroupAddress": alaPimsmStaticRPGroupAddress,
       "alaPimsmStaticRPGroupMask": alaPimsmStaticRPGroupMask,
       "alaPimsmStaticRPAddress": alaPimsmStaticRPAddress,
       "alaPimsmStaticRPRowStatus": alaPimsmStaticRPRowStatus,
       "alaPimsmAdminSPTConfig": alaPimsmAdminSPTConfig,
       "alaPimsmRPThreshold": alaPimsmRPThreshold,
       "alaPimsmV6AdminStatus": alaPimsmV6AdminStatus,
       "alaPimsmV6SPTConfig": alaPimsmV6SPTConfig,
       "alaPimsmV6RPSwitchover": alaPimsmV6RPSwitchover,
       "alaPimsmDebugConfig": alaPimsmDebugConfig,
       "alaPimsmDebugLevel": alaPimsmDebugLevel,
       "alaPimsmDebugError": alaPimsmDebugError,
       "alaPimsmDebugHello": alaPimsmDebugHello,
       "alaPimsmDebugNbr": alaPimsmDebugNbr,
       "alaPimsmDebugBootstrap": alaPimsmDebugBootstrap,
       "alaPimsmDebugCRP": alaPimsmDebugCRP,
       "alaPimsmDebugRoute": alaPimsmDebugRoute,
       "alaPimsmDebugJoinPrune": alaPimsmDebugJoinPrune,
       "alaPimsmDebugAssert": alaPimsmDebugAssert,
       "alaPimsmDebugTime": alaPimsmDebugTime,
       "alaPimsmDebugIgmp": alaPimsmDebugIgmp,
       "alaPimsmDebugSpt": alaPimsmDebugSpt,
       "alaPimsmDebugMip": alaPimsmDebugMip,
       "alaPimsmDebugInit": alaPimsmDebugInit,
       "alaPimsmDebugTm": alaPimsmDebugTm,
       "alaPimsmDebugIpmrm": alaPimsmDebugIpmrm,
       "alaPimsmDebugMisc": alaPimsmDebugMisc,
       "alaPimsmDebugAll": alaPimsmDebugAll,
       "alaPimdmGlobalConfig": alaPimdmGlobalConfig,
       "alaPimdmAdminStatus": alaPimdmAdminStatus,
       "alaPimdmStateRefreshTimeToLive": alaPimdmStateRefreshTimeToLive,
       "alaPimdmStateRefreshLimitInterval": alaPimdmStateRefreshLimitInterval,
       "alaPimdmV6AdminStatus": alaPimdmV6AdminStatus,
       "alcatelIND1PIMMIBConformance": alcatelIND1PIMMIBConformance,
       "alcatelIND1PIMMIBCompliances": alcatelIND1PIMMIBCompliances,
       "alaPimsmCompliance": alaPimsmCompliance,
       "alaPimdmCompliance": alaPimdmCompliance,
       "alcatelIND1PIMMIBGroups": alcatelIND1PIMMIBGroups,
       "alaPimsmConfigMIBGroup": alaPimsmConfigMIBGroup,
       "alaPimsmDebugMIBGroup": alaPimsmDebugMIBGroup,
       "alaPimdmConfigMIBGroup": alaPimdmConfigMIBGroup}
)
